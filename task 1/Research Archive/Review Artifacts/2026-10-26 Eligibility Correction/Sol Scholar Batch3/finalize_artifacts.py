"""Record the completed, hand-authored secondary pass and run structural QC."""
from collections import Counter
import csv
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(name, data):
    (HERE/name).write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')

freeze = json.loads((HERE/'input_freeze.json').read_text())
qa = json.loads((HERE/'secondary_QA_freeze.json').read_text())
primary = json.loads((HERE/'primary_itemwise_checks.json').read_text())
assert sha(HERE/'primary_itemwise_checks.json') == qa['primary_checks_sha256']
assert sha(HERE/'author_checks.psv') == qa['authored_sha256']
assert not (HERE/'qc_results.json').exists(), 'Final pass already recorded; do not overwrite'
original = {r['occurrence_E_ID']:r for r in csv.DictReader(Path(next(p for p in freeze['inputs'] if p.endswith('REVIEWQUEUE.csv'))).open()) if r['occurrence_E_ID'] in freeze['targets']}
producer_path = next(p for p in freeze['inputs'] if p.endswith('Scholar Batch 3/overlay.csv'))
producer = {r['occurrence_E_ID']:r for r in csv.DictReader(Path(producer_path).open())}
rows = list(csv.DictReader((HERE/'overlay.csv').open()))
authored = list(csv.DictReader((HERE/'secondary_author_checks.psv').open(), delimiter='|'))
assert [a['eid'] for a in authored] == qa['target_EIDs']
assert sha(HERE/'overlay.csv') == qa['overlay_primary_sha256']
(HERE/'overlay.primary.csv').write_bytes((HERE/'overlay.csv').read_bytes())
results = []
for a in authored:
    eid = a['eid']; r = original[eid]
    groups = [k for k,v in qa['groups'].items() if v['selected'] == eid]
    results.append(dict(occurrence_E_ID=eid,
        status='checked-no-further-discrepancy',
        secondary_observation=a['secondary_observation'],
        producer_exclusion_critical=eid in qa['producer_exclusions'],
        sol_exclusion_critical=eid in qa['sol_proposed_exclusions'],
        selected_groups=groups,
        original_title=r['title'], original_snippet=r['abstract_or_snippet'],
        original_raw_metadata=r['raw_record_metadata'],
        original_record_sha256=hashlib.sha256(json.dumps(r,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
        original_anchor='REVIEWQUEUE.csv / occurrence_E_ID='+eid,
        checker='Sol AI separate-pass self-audit; NOT independent human scientific review',
        review_date='2026-10-26'))
checked = {a['eid'] for a in authored}
for r in rows:
    r['secondary_QA'] = 'checked-no-further-discrepancy' if r['occurrence_E_ID'] in checked else 'NOT SELECTED; primary semantic review completed'
    r['audit_type'] = 'Sol AI after Luna; primary itemwise review + frozen separate-pass self-audit; not independent human review'
with (HERE/'overlay.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
save('qc_results.json',dict(
    secondary_freeze_sha256=sha(HERE/'secondary_QA_freeze.json'),
    checks=results, groups={k:dict(selected=v['selected'],status='checked-no-further-discrepancy',check_EID=v['selected']) for k,v in qa['groups'].items()},
    new_substantive_discrepancies=0,
    prospective_expansions=[], expansion_reason='No new substantive discrepancy in the frozen secondary pass; all producer exclusions were already critical and reread',
    limitation='AI separate-pass self-audit, not independent scientific review; only metadata/snippet semantic routing checked'))
raw_fields=['source_csv_row_1based','operation','query','rank','title','display_record_label','dedup_key','duplicate_occurrence','first_occurrence','local_exact_filename_match','publication_year','publication_date','language','source_platform','abstract_or_snippet','abstract_status','Q_ID','platform_record_id','record_url','doi','raw_record_metadata','candidate_duplicate_target_E_ID','raw_first_occurrence_E_ID','request_url','request_timestamp_local','request_timestamp_utc','response_sha256_claimed','raw_body_location_scratch_only']
assert [r['occurrence_E_ID'] for r in rows] == freeze['targets']
assert [r['corrective_event_ID'] for r in rows] == freeze['corrective_events']
assert len(primary) == 100
for r in rows:
    eid=r['occurrence_E_ID']; raw=original[eid]
    assert all(r[k]==raw[k] for k in raw_fields), eid
    assert all(r[q] for q in ['R1','R2','R3','R4','R5','R6'])
    assert r['stage1_decision'] in ['ADVANCE','EXCLUDE']
    assert r['stage1_primary_code'] == ('X3' if r['stage1_decision']=='EXCLUDE' else '')
    assert r['claim_support']==r['methodological_confidence']=='UNASSESSED'
    assert r['fulltext_pass']==r['citation_pass']=='NOT RUN'
    assert r['canonical_work_ID']==r['canonical_SID']==r['canonical_primary_exclusion_code']==''
    assert r['candidate_R_tags']==';'.join(next(p for p in primary if p['occurrence_E_ID']==eid)['candidate_R_tags'])
assert set(qa['producer_exclusions']) <= checked
assert set(qa['sol_proposed_exclusions']) <= checked
assert all(v['selected'] in checked and v['selected']==min(v['members']) for v in qa['groups'].values())
receipt={path:dict(expected_sha256=expected,actual_sha256=sha(Path(path)),unchanged=sha(Path(path))==expected) for path,expected in freeze['inputs'].items()}
assert all(v['unchanged'] for v in receipt.values())
save('preservation_receipt.json',dict(timestamp=datetime.datetime.now().astimezone().isoformat(),inputs=receipt,raw_occurrence_fields_checked=raw_fields,raw_field_matching_rows=100,primary_checks_and_freeze_preserved=True,no_merges=True,no_shared_tracker_writes=True))
rejected=[r['occurrence_E_ID'] for r in rows if producer[r['occurrence_E_ID']]['stage1_disposition_reviewed']=='EXCLUDE' and r['stage1_decision']=='ADVANCE']
retained=[r['occurrence_E_ID'] for r in rows if producer[r['occurrence_E_ID']]['stage1_disposition_reviewed']=='EXCLUDE' and r['stage1_decision']=='EXCLUDE']
dups=[dict(occurrence_E_ID=r['occurrence_E_ID'],candidate_target=r['candidate_duplicate_target_E_ID'],semantic_disposition=r['stage1_decision'],identity_status=r['identity_status']) for r in rows if r['duplicate_occurrence']=='True']
counts=dict(target_occurrences=100,primary_original_reads=100,primary_six_question_checks=100,
    producer_counts=dict(Counter(producer[e]['stage1_disposition_reviewed'] for e in freeze['targets'])),
    corrected_occurrence_counts=dict(Counter(r['stage1_decision'] for r in rows)),
    metadata_stage1_pending=0,canonical_identity_unverified=100,
    rejected_producer_exclusions=len(rejected),rejected_producer_exclusion_EIDs=rejected,
    retained_producer_exclusions=len(retained),retained_producer_exclusion_EIDs=retained,
    new_semantic_exclusions_from_producer_DUP=['E-0636'],
    duplicate_candidates_reviewed=10,duplicate_candidates=dups,accepted_DUP_work_merges=0,
    secondary_original_rereads=len(results),secondary_critical_union=len(qa['critical_EIDs']),
    producer_exclusions_secondary_checked=31,sol_exclusions_secondary_checked=8,
    explicit_groups_frozen=len(qa['groups']),explicit_groups_checked=len(qa['groups']),
    additional_pattern_expansions=0,unreviewed_primary_occurrences=0,
    primary_only_not_secondary_sampled=100-len(results),
    fulltext_pass='NOT RUN',citation_pass='NOT RUN',claim_support='UNASSESSED',methodological_confidence='UNASSESSED',
    independent_works='UNDETERMINED; occurrence counts are not unique-work counts',fulltext_inclusions='NOT ADJUDICATED',
    protocol='ERP-2026-10-25-v1.0',cutoff='2026-10-25 inclusive')
save('qc_counts.json',counts)
print(json.dumps(counts,indent=2))

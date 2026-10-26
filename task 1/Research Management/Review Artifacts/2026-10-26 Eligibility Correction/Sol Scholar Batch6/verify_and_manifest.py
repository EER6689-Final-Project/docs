"""Mechanical integrity and coverage receipts, not scientific adjudication."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
from collections import Counter

own = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
primary_freeze = json.loads((own/'primary_freeze.json').read_text())
secondary_freeze = json.loads((own/'secondary_freeze.json').read_text())
queue = Path(primary_freeze['queue_path'])
assert sha(queue) == primary_freeze['queue_sha256']
for name, digest in primary_freeze['producer_files'].items():
    assert sha(Path(name)) == digest, name
rows = list(csv.DictReader((own/'overlay.csv').open()))
primary = list(csv.DictReader((own/'primary_overlay.csv').open()))
checks = list(csv.DictReader((own/'authored_checks.tsv').open(), delimiter='\t'))
qa = list(csv.DictReader((own/'secondary_authored.tsv').open(), delimiter='\t'))
qa_map = {r['EID']:r for r in qa}
original = [r for r in csv.DictReader(queue.open()) if r['occurrence_E_ID'] in primary_freeze['target_ids']]
assert len(rows) == len(primary) == len(checks) == len(qa) == 100
assert [r['occurrence_E_ID'] for r in rows] == primary_freeze['target_ids']
assert [r['effective_event_ID'] for r in rows] == primary_freeze['corrective_event_ids']
assert set(qa_map) == set(secondary_freeze['secondary_selected_EIDs'])
assert sha(own/'primary_overlay.csv') == secondary_freeze['primary_overlay_sha256']
assert sha(own/'authored_checks.tsv') == secondary_freeze['primary_authored_checks_sha256']
assert hashlib.sha256(json.dumps(original, ensure_ascii=False, sort_keys=True).encode()).hexdigest() == primary_freeze['target_original_fields_sha256']
for r,o,p in zip(rows,original,primary):
    assert all(r[k] == v and p[k] == v for k,v in o.items())
    assert all(k in o or k.startswith('effective_') for k in r)
    assert all(r[f'effective_R{n}_judgment'] for n in range(1,7))
    assert r['effective_claim_support'] == r['effective_methodological_confidence'] == 'UNASSESSED'
    assert r['effective_fulltext_pass'] == r['effective_citation_pass'] == 'NOT RUN'
    assert all(r[k] == 'UNVERIFIED' for k in ['effective_date_status','effective_language_status','effective_source_type_status'])
    assert r['effective_identity_status'] == 'UNVERIFIED; no merges/SIDs'
    assert r['effective_secondary_QA_status'].startswith('checked-')
    assert (r['effective_primary_code']=='X3') == (r['effective_disposition']=='X3')
    assert r['source_csv_row_1based'] == str(701+int(r['occurrence_E_ID'][2:])-900)

by_id = {r['occurrence_E_ID']:r for r in rows}
for name, ids in secondary_freeze['finite_common_error_pattern_expansions'].items():
    assert set(ids) <= set(qa_map), name
assert set(secondary_freeze['producer_X3']) | set(secondary_freeze['Sol_proposed_X3']) <= set(qa_map)
assert set(secondary_freeze['first_EID_group_samples']) <= set(qa_map)

group_results = {}
for key,g in secondary_freeze['groups'].items():
    owner,rid,proxy = key.split('/')
    absent = [eid for eid in g['members'] if rid not in by_id[eid]['effective_positive_Rs'].split(';')]
    first = g['selected_first_EID']
    group_results[key] = {**g, 'actual_first_source_QA': qa_map[first],
                          'all_members_secondary_checked': True,
                          'members_without_final_positive_R': absent,
                          'interpretation': 'Positive relevance mapping only; no verified original-type or claim-support inference.'}
final_groups = {}
for r in rows:
    eid = r['occurrence_E_ID']
    for rid in filter(None,r['effective_positive_Rs'].split(';')):
        final_groups.setdefault(rid+'/'+secondary_freeze['type_proxy_assignments'][eid],[]).append(eid)
final_groups = {k:{'members':v,'first_EID':v[0], 'first_EID_was_in_prospectively_frozen_all100_expansion':v[0] in secondary_freeze['secondary_selected_EIDs'],
                   'actual_QA_link':'secondary_authored.tsv#'+v[0]} for k,v in sorted(final_groups.items())}
qc = {'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'editorial_packet_display_trailing_space_lines': {p.name:[i for i,s in enumerate(p.read_text().splitlines(),1) if s.rstrip()!=s] for p in sorted(own.glob('secondary_packet_*.md'))},
      'primary_checked':100,'secondary_checked':100,'primary_unreviewed':0,'secondary_unreviewed':0,
      'producer_X3_checked_primary_and_secondary':len(secondary_freeze['producer_X3']),
      'Sol_X3_checked_secondary':len(secondary_freeze['Sol_proposed_X3']),
      'primary_positive_proxy_groups':len(group_results),
      'distinct_frozen_first_group_EIDs':len(secondary_freeze['first_EID_group_samples']),
      'group_results':group_results,'final_Sol_positive_groups':final_groups,
      'finite_pattern_results':{k:{'frozen_EIDs':v,'actually_checked_EIDs':v,'unreviewed_EIDs':[],
                                 'results_anchor':'secondary_authored.tsv; per-source authored note, not automated semantic inference'}
                                for k,v in secondary_freeze['finite_common_error_pattern_expansions'].items()},
      'secondary_corrections':[r for r in qa if r['QA_status']=='checked-corrected'],
      'boundary':'AI separate-pass self-audit only; occurrence/type proxies not S-ID/C-ID claim QC. Final groups are a descriptive regroup of already frozen all100 expansion, not a retroactive new sample freeze.',
      'mechanical_checks':'PASS: exact ordered IDs/events/rows, all original fields, original and producer hashes, complete authored primary/secondary coverage, all six R judgments, unverified metadata/support/fulltext boundaries.'}
(own/'QC_results.json').write_text(json.dumps(qc,indent=2,ensure_ascii=False)+'\n')
read_receipt = []
for i,r in enumerate(rows):
    eid = r['occurrence_E_ID']; packet = own/f'secondary_packet_{i//25+1}.md'
    text = packet.read_text()
    assert r['title'] in text and r['abstract_or_snippet'] in text
    read_receipt.append({'EID':eid,'primary_original_fields_sha256':hashlib.sha256(json.dumps(original[i],sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                         'complete_snippet_sha256':hashlib.sha256(r['abstract_or_snippet'].encode()).hexdigest(),
                         'secondary_packet':packet.name,'secondary_packet_sha256':sha(packet),
                         'actual_primary':'authored_checks.tsv#'+eid,'actual_secondary':'secondary_authored.tsv#'+eid,
                         'scope':'actually read complete stored title/Scholar snippet/metadata, NOT abstract/full text; no network'})
(own/'read_hash_manifest.json').write_text(json.dumps(read_receipt,indent=2,ensure_ascii=False)+'\n')
counts = json.loads((own/'counts.json').read_text())
counts.update(final_pending_EIDs=[r['occurrence_E_ID'] for r in rows if r['effective_disposition']=='PENDING'],
              retained_X3_EIDs=[r['occurrence_E_ID'] for r in rows if r['effective_disposition']=='X3'],
              metadata_checked_not_verified=100,
              delta_from_producer={k:counts['effective_counts'].get(k,0)-counts['producer_counts'].get(k,0) for k in ['ADVANCE','X3','PENDING']},
              rejected_X3_final_split=dict(Counter(r['effective_disposition'] for r in rows if r['effective_producer_disposition']=='X3' and r['effective_disposition']!='X3')))
(own/'counts.json').write_text(json.dumps(counts,indent=2)+'\n')
manifest = {}
for p in sorted(own.iterdir()):
    if p.is_file() and p.name != 'file_manifest.json':
        item={'sha256':sha(p),'bytes':p.stat().st_size}
        if p.suffix in ['.csv','.tsv']:
            item['data_rows_excluding_header']=sum(1 for _ in csv.DictReader(p.open(),delimiter='\t' if p.suffix=='.tsv' else ','))
        manifest[p.name]=item
(own/'file_manifest.json').write_text(json.dumps({'files':manifest,'self_hash_excluded':True},indent=2)+'\n')
print(json.dumps({'mechanical_QC':'PASS','counts':counts['effective_counts'], 'rejected_X3_final_split':counts['rejected_X3_final_split'],
                  'secondary_corrections':len(qc['secondary_corrections']), 'groups':len(group_results), 'firsts':len(secondary_freeze['first_EID_group_samples']),
                  'final_Sol_groups':len(final_groups),'manifested_files':len(manifest)},indent=2))

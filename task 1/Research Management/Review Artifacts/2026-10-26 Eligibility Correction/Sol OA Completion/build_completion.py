"""Mechanical joins and receipts only; semantic judgments are authored in TSVs."""
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from freeze import HERE, ROOT, QUEUE, digest, rows

def write_json(name, value):
    with (HERE / name).open('x') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

def write_csv(name, records, fields=None):
    with (HERE / name).open('x', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields or list(records[0]))
        w.writeheader()
        w.writerows(records)

freeze = json.loads((HERE / 'target_freeze.json').read_text())
plan = json.loads((HERE / 'group_exclusion_freeze.json').read_text())
for path, expected in freeze['inputs'].items():
    assert digest(ROOT.parent / path) == expected, path
assert digest(HERE / 'item_checks.tsv') == plan['item_checks_sha256']
qrows = rows(QUEUE)
q = {r['occurrence_E_ID']: r for r in qrows}
base = rows(ROOT / 'Sol_effective_state_838.csv')
luna = {r['target_occurrence_EID']: r for r in rows(ROOT / 'OA Remaining 105/overlay.csv')}
checks = list(csv.DictReader((HERE / 'item_checks.tsv').open(), delimiter='\t'))
second = {r['target_EID']: r for r in csv.DictReader((HERE / 'second_pass_checks.tsv').open(), delimiter='\t')}
assert [c['target_EID'] for c in checks] == freeze['targets']
selected = {g['selected'] for g in plan['groups']}
excluded = {c['target_EID'] for c in checks if c['proposed_status'] == 'X3'}
assert set(second) == selected | excluded
assert all(r['actual_state'] == 'checked-no-discrepancy' for r in second.values())
overlay = []
for i, c in enumerate(checks):
    eid = c['target_EID']
    s, p = q[eid], luna[eid]
    md = json.loads(s['raw_record_metadata'])
    status = c['proposed_status']
    rationale = c['rationale']
    if status == 'X3':
        rationale += ' Accepted only after group_exclusion_freeze.json and actual second-pass entry in second_pass_checks.tsv.'
    overlay.append(dict(new_review_event_EID=f'E-{2600+i}', target_occurrence_EID=eid, source_csv_row_1based=s['source_csv_row_1based'], source_queue_sha256=digest(QUEUE), title=s['title'], platform_record_id=s['platform_record_id'], doi=s['doi'], publication_date_metadata=s['publication_date'], language_metadata=s['language'], source_type_metadata=md.get('type'), abstract_status=s['abstract_status'], abstract_chars=len(s['abstract_or_snippet']), original_export_row_sha256=__import__('hashlib').sha256(json.dumps(s,sort_keys=True,ensure_ascii=False).encode()).hexdigest(), original_export_content_read='YES; title + entire supplied abstract field or its absence/defect + all metadata', stage1_disposition=status, primary_exclusion_code='X3' if status=='X3' else '', explicit_RIDs=c['RIDs'], itemwise_relevance_and_transfer_rationale=rationale, producer_event_EID=p['new_review_event_EID'], producer_disposition=p['stage1_disposition'], producer_R_mapping=p['provisional_R_mapping'], producer_rationale=p['itemwise_relevance_and_transfer_rationale'], disposition_comparison='CHANGED' if status!=p['stage1_disposition'] else 'RETAINED; rationale independently specified', mapping_comparison='CHANGED explicit token assignment' if c['RIDs']!=p['provisional_R_mapping'] else 'Same tokens; source-specific rationale rechecked', original_export_anchor=f'original_export_targets.csv#occurrence_E_ID={eid}', second_pass_anchor=f'second_pass_checks.tsv#target_EID={eid}' if eid in second else 'Not selected; original-text semantic check completed', identity='ID-PENDING; no canonical S-ID/work/merge', date_language_type='PENDING original-source/version/full-text verification; metadata-only screen; no X2', fulltext='NOT RUN', citations='NOT RUN', claim_support='UNASSESSED', methodological_confidence='UNASSESSED', source_claim_QC='UNASSESSED', checker='Sol AI separate-pass technical self-audit after Luna; NOT independent human review', protocol='ERP-2026-10-25-v1.0 unchanged', review_date='2026-10-26', history_link=f'../Sol_effective_state_838.csv#occurrence_E_ID={eid}; ../OA Remaining 105/overlay.csv#new_review_event_EID={p["new_review_event_EID"]}', gate_effect='NONE; B-010/G3/G4 OPEN'))
write_csv('overlay.csv', overlay)
write_csv('original_export_targets.csv', [q[eid] for eid in freeze['targets']])
o = {r['target_occurrence_EID']:r for r in overlay}
effective = []
for b in base:
    r = dict(b)
    eid = r['occurrence_E_ID']
    r['completion_history_json'] = ''
    if eid in o:
        c = o[eid]
        assert b['effective_stage1_status'] == 'PENDING'
        r['completion_history_json'] = json.dumps(dict(baseline=dict(path='../Sol_effective_state_838.csv', corrective_event=b['effective_corrective_event_EID'], history_link=b['effective_history_link'], status=b['effective_stage1_status'], RIDs=b['effective_RIDs'], rationale=b['effective_rationale']), producer=dict(path='../OA Remaining 105/overlay.csv', event=c['producer_event_EID'], disposition=c['producer_disposition'], RIDs=c['producer_R_mapping']), completion=dict(path='overlay.csv', event=c['new_review_event_EID'])), ensure_ascii=False)
        r.update(effective_stage1_status=c['stage1_disposition'], effective_primary_code=c['primary_exclusion_code'], effective_RIDs=c['explicit_RIDs'], effective_rationale=c['itemwise_relevance_and_transfer_rationale'], effective_corrective_event_EID=c['new_review_event_EID'], effective_history_link=f'completion_history_json; overlay.csv#target_occurrence_EID={eid}; ../OA Remaining 105/overlay.csv#new_review_event_EID={c["producer_event_EID"]}', effective_QA_coverage=c['original_export_content_read'])
    effective.append(r)
write_csv('effective_state_838.csv', effective)
assert all(all(r[k]==q[r['occurrence_E_ID']][k] for k in qrows[0]) for r in effective)
assert all(all(r[k]==b[k] for k in b) for b,r in zip(base,effective) if b['occurrence_E_ID'] not in o)
groups = []
for g in plan['groups']:
    a = second[g['selected']]
    groups.append(dict(g, state=a['actual_state'], actual_observation=a['actual_observation'], original_anchor=f'original_export_targets.csv#occurrence_E_ID={g["selected"]}', plan_anchor='group_exclusion_freeze.json', checker='Sol separate-pass AI self-audit; not independent human review'))
write_json('group_exclusion_QA_results.json', dict(completed_utc=datetime.now(timezone.utc).isoformat(), frozen_plan_sha256=digest(HERE/'group_exclusion_freeze.json'), actual_checks_sha256=digest(HERE/'second_pass_checks.tsv'), scope='105 cohort metadata eligibility proxies ONLY; not canonical claim QC; not complete global 300 grouping', groups=groups, distinct_group_sample_occurrences=len(selected), proposed_exclusions=[dict(target_EID=e, actual=second[e], accepted_status='X3') for e in sorted(excluded)], planned_group_count=len(groups), actually_checked_group_count=len(groups), planned_only_groups=[], unresolved_mappings=plan['unmapped_pending'], global_300_group_QA='OPEN: earlier 195 not rechecked/regrouped; 57 earlier unresolved mappings + 9 here remain pending; old root planned group snapshot is unchanged'))
counts = dict(baseline=dict(Counter(r['effective_stage1_status'] for r in base)), target_before={'PENDING':105}, target_after=dict(Counter(r['stage1_disposition'] for r in overlay)), prospective_delta={'ADVANCE':95,'X3':1,'PENDING':-96}, effective=dict(Counter(r['effective_stage1_status'] for r in effective)), OA_effective=dict(Counter(r['effective_stage1_status'] for r in effective[:300])), Scholar_effective=dict(Counter(r['effective_stage1_status'] for r in effective[300:])), producer_transition_counts=dict(Counter(f'{r["producer_disposition"]}->{r["stage1_disposition"]}' for r in overlay)), producer_disposition_changes=[r['target_occurrence_EID'] for r in overlay if r['stage1_disposition']!=r['producer_disposition']], producer_mapping_token_changes=[r['target_occurrence_EID'] for r in overlay if r['explicit_RIDs']!=r['producer_R_mapping']], original_text_checked=105, original_text_unreviewed=[], second_pass_distinct_group_occurrences=len(selected), second_pass_groups_checked=len(groups), second_pass_exclusions_checked=len(excluded), pending_distinct_cohorts={'earlier_OA_195_unresolved':57,'completion_OA_105_unresolved':9,'Scholar_not_promoted':538}, pending_target_EIDs=plan['unmapped_pending'], unchanged_original_X3=44, untouched_prior_OA_original_text_checks=195, occurrence_not_work_counts=True)
assert counts['effective']=={'ADVANCE':189,'X3':45,'PENDING':604}
assert counts['Scholar_effective']=={'PENDING':538}
write_json('counts.json', counts)
write_json('integrity_checks.json', dict(checked_utc=datetime.now(timezone.utc).isoformat(), all_frozen_input_hashes_unchanged=True, queue_sha256=digest(QUEUE), original_838_fields_unchanged=True, prior_195_effective_fields_unchanged=True, Scholar_538_effective_fields_unchanged=True, original_44_X3_unchanged=True, target_order_and_exact_set_preserved=True, corrective_events=[overlay[0]['new_review_event_EID'],overlay[-1]['new_review_event_EID']], corrective_event_count=105, source_support_confidence_UNASSESSED=True, date_language_type_identity_still_pending=True, final_group_freeze_preceded_actual_second_pass=True, planned_versus_actual_link='group_exclusion_QA_results.json', no_fulltext_citations_library_or_gate_actions=True))
print(json.dumps(counts, indent=2))

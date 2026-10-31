"""Finalize only this owned subtree; frozen primary files stay byte-identical."""
import csv
import json
from collections import Counter
from review_tools import HERE, FREEZE, PROSPECTIVE, QUEUE, SNAPSHOT, load, sha, stamp

def save(name, obj):
    p = HERE / name
    assert not p.exists(), p
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n')

f, q, s = load()
assert sha(PROSPECTIVE.read_bytes()) == f['base_freeze_sha256']
pf = json.loads((HERE/'primary_results_freeze.json').read_text())
for name, expected in pf['primary_output_hashes'].items():
    assert sha((HERE/name).read_bytes()) == expected, name
sf = json.loads((HERE/'secondary_freeze.json').read_text())
assert sha((HERE/'primary_results_freeze.json').read_bytes()) == sf['primary_results_freeze_sha256']
assert sha((HERE/'overlay_130.csv').read_bytes()) == sf['overlay_sha256']
secondary = {}
for p in sorted(HERE.glob('authored_secondary_*.json')):
    a = json.loads(p.read_text()); assert not set(a) & set(secondary); secondary.update(a)
assert set(secondary) == set(sf['selected_targets'])
secondary_receipts = {}
for p in sorted(HERE.glob('secondary_read_receipt*.json')):
    for r in json.loads(p.read_text())['records']:
        assert r['target'] not in secondary_receipts
        secondary_receipts[r['target']] = p.name
assert set(secondary_receipts) == set(secondary)
pattern_freeze = json.loads((HERE/'secondary_pattern_expansion_freeze.json').read_text())
pattern = json.loads((HERE/'authored_pattern_QA.json').read_text())
pattern_ids = pattern_freeze['exact_targets']
assert all(e in pattern for e in pattern_ids)
pr = json.loads((HERE/'pattern_read_receipt_000_002.json').read_text())
assert [r['target'] for r in pr['records']] == pattern_ids
assert not set(pattern_ids) & set(secondary)
corrections = json.loads((HERE/'secondary_corrections.json').read_text())['corrections']
rows = list(csv.DictReader((HERE/'overlay_130.csv').open()))
all_judgments = {}
qc_rows = []
for i, row in enumerate(rows):
    e = row['target_occurrence_EID']; assert e == f['exact_targets'][i]
    assert row['new_review_event_EID'] == f'E-{3500+i}'
    a = json.loads(row['affected_mapping_judgments_json'])
    if e in corrections:
        c = corrections[e]
        a[c['R']] = [c['corrected_result'], c['corrected_rationale']]
        row['corrected_explicit_RIDs'] = c['final_corrected_explicit_RIDs']
        row['supported_affected_RIDs'] = ';'.join(sorted(r for r,v in a.items() if v[0]=='supported'))
        row['unclear_affected_RIDs'] = c['final_unclear_affected_RIDs']
        row['routing'] = c['routing']
        row['affected_mapping_judgments_json'] = json.dumps(a, ensure_ascii=False, sort_keys=True)
    all_judgments[e] = a
    row['primary_history'] = 'overlay_130.csv; primary_results_freeze.json'
    row['secondary_correction_history'] = 'secondary_corrections.json#'+e if e in corrections else 'NONE'
    if e in secondary:
        state, reason = secondary[e]
        row['secondary_QA'] = state+'; '+secondary_receipts[e]
        qc_rows.append({'local_QA_key': 'OAX-QA-'+e, 'target_occurrence_EID': e,
                        'review_event_EID': row['new_review_event_EID'], 'phase': 'frozen-secondary',
                        'result':state, 'rationale':reason, 'read_receipt':secondary_receipts[e]})
    elif e in pattern_ids:
        a2 = pattern[e]
        row['secondary_QA'] = a2['result']+'; additive frozen R4 pattern check ONLY'
        qc_rows.append({'local_QA_key': 'OAX-PATTERN-'+e, 'target_occurrence_EID':e,
                        'review_event_EID':row['new_review_event_EID'], 'phase':'frozen-pattern-R4-only',
                        'result':a2['result'], 'rationale':a2['rationale'],
                        'read_receipt':'pattern_read_receipt_000_002.json'})
    else:
        row['secondary_QA'] = 'NOT SELECTED; primary checked only; no inferred QA pass'

for name, data in [('overlay_130_final.csv',rows), ('secondary_QA_results.csv',qc_rows)]:
    p=HERE/name; assert not p.exists()
    with p.open('w',newline='') as out:
        w=csv.DictWriter(out,fieldnames=list(data[0]));w.writeheader();w.writerows(data)

groups=[]
by_e={r['target_occurrence_EID']:r for r in rows}
for g in f['affected_groups']:
    outcomes={k:[e for e in g['members'] if all_judgments[e][g['R']][0]==k] for k in ('supported','unclear','outside')}
    members=outcomes['supported']
    first=min(members) if members else None
    old_first=next(x['first_EID'] for x in sf['corrected_affected_groups'] if x['R']==g['R'] and x['source_type_metadata_proxy']==g['source_type_metadata_proxy'])
    assert first == old_first  # QA correction created no new deterministic selection.
    groups.append({'R':g['R'],'source_type_metadata_proxy':g['source_type_metadata_proxy'],
        'original_global_QC':g['qc'],'original_global_result':'held; preserved, not retrospectively passed',
        'original_members':g['members'],'final_results':outcomes,
        'final_positive_first_EID':first,
        'first_EID_secondary_actually_checked': first in secondary or first in pattern_ids if first else 'EMPTY GROUP',
        'original_source_type_fit':'PENDING; raw metadata proxy only'})
save('final_group_results.json',{'groups':groups,'group_count':12,'scope':'Affected memberships only; no all-42 or all-300 QC pass'})
mc=Counter(v[0] for a in all_judgments.values() for v in a.values())
changed=[e for e,r in by_e.items() if r['previous_RIDs']!=r['corrected_explicit_RIDs']]
assert set(changed)<=set(secondary)
unclear={e:';'.join(r for r,v in a.items() if v[0]=='unclear') for e,a in all_judgments.items() if any(v[0]=='unclear' for v in a.values())}
save('final_counts.json',{
    'primary_targets_planned':130,'primary_targets_checked':130,'primary_targets_unreviewed':[],
    'affected_mapping_count':sum(mc.values()),'final_affected_mapping_results':dict(mc),
    'positive_mapping_set_changed_target_count':len(changed),'changed_target_EIDs':changed,
    'unclear_mapping_targets':unclear,'new_mappings':0,'new_SIDs':0,'DUP_merges':0,'new_X3_proposals':0,'new_exclusions':0,
    'secondary_original_planned':63,'secondary_original_checked':len(secondary),'secondary_original_unreviewed':[],
    'secondary_original_result_counts':dict(Counter(v[0] for v in secondary.values())),
    'secondary_additional_pattern_planned':2,'secondary_additional_pattern_checked':2,'secondary_additional_pattern_unreviewed':[],
    'total_secondary_unique_targets_checked':65,'primary_only_not_selected_for_secondary': [e for e in f['exact_targets'] if e not in secondary and e not in pattern_ids],
    'secondary_mapping_corrections':{'E-0483':'R4 supported -> unclear; inherited R6 retained'},
    'target_status_before':dict(Counter(r['previous_status'] for r in rows)),
    'target_status_proposed_after':dict(Counter(r['proposed_stage1_status'] for r in rows)),
    'status_transitions':[{ 'EID':r['target_occurrence_EID'],'before':r['previous_status'],'proposed_after':r['proposed_stage1_status']} for r in rows if r['previous_status']!=r['proposed_stage1_status']],
    'original_global_QA_preserved':{'groups':42,'supported':30,'held':12},
    'whole_OA_QC_pass':False,'all_inherited_mappings_revalidated':False,
    'fulltext':'NOT RUN','citations':'NOT RUN','claim_support':'UNASSESSED','methodological_confidence':'UNASSESSED',
    'identity_date_language_type':'PENDING original verification','G3':'OPEN','G4':'OPEN',
    'network':'No external network used; no network tool interruption observed in this agent execution. User-reported earlier network issue has no diagnostic/timestamp available here.'})
save('completion_checkpoint.json',{'generated_at_utc':stamp(),'primary_checked':130,'primary_unreviewed':0,
    'secondary_selected_checked':63,'secondary_selected_unreviewed':0,'additional_pattern_checked':2,
    'final_overlay_sha256':sha((HERE/'overlay_130_final.csv').read_bytes()),
    'authored_primary_hashes':{p.name:sha(p.read_bytes()) for p in sorted(HERE.glob('authored_primary*.json'))},
    'authored_secondary_hashes':{p.name:sha(p.read_bytes()) for p in sorted(HERE.glob('authored_secondary*.json'))},
    'pattern_hashes':{name:sha((HERE/name).read_bytes()) for name in ('secondary_pattern_expansion_freeze.json','pattern_read_receipt_000_002.json','authored_pattern_QA.json')},
    'input_hashes':{str(p):sha(p.read_bytes()) for p in (QUEUE,SNAPSHOT,FREEZE,PROSPECTIVE)}})
print(json.dumps({'final_mapping_counts':dict(mc),'secondary_result_counts':dict(Counter(v[0] for v in secondary.values())),
    'status_transitions':[r['target_occurrence_EID'] for r in rows if r['previous_status']!=r['proposed_stage1_status']],
    'group_summary':[{ 'R':g['R'],'type':g['source_type_metadata_proxy'], 'counts':{k:len(v) for k,v in g['final_results'].items()}, 'first':g['final_positive_first_EID']} for g in groups]},indent=2))

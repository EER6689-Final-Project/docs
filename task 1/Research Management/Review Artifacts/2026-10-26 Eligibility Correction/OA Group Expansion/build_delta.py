"""Derive transport files from human-readable, Sol-authored mapping checks."""
import csv
import json
from collections import Counter
from review_tools import HERE, FREEZE, PROSPECTIVE, QUEUE, SNAPSHOT, load, sha, stamp

def write_json(name, obj):
    p = HERE / name
    assert not p.exists(), p
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n')

f, q, s = load()
authored = {}
for p in sorted(HERE.glob('authored_primary_*.json')):
    a = json.loads(p.read_text())
    assert not set(a) & set(authored)
    authored.update(a)
assert set(authored) == set(f['exact_targets'])
receipts = {}
for p in sorted(HERE.glob('primary_read_receipt*.json')):
    for r in json.loads(p.read_text())['records']:
        assert r['target'] not in receipts
        receipts[r['target']] = (p.name, r)
assert set(receipts) == set(authored)
rows = []
mapping_counts = Counter()
for i, e in enumerate(f['exact_targets']):
    a = authored[e]
    affected = {g['R'] for g in f['affected_groups'] if e in g['members']}
    assert set(a) == affected
    assert all(v[0] in ('supported', 'unclear', 'outside') and len(v[1]) > 100 for v in a.values())
    original = set(filter(None, s[e]['effective_RIDs'].split(';')))
    inherited = original - affected
    supported = {r for r, v in a.items() if v[0] == 'supported'}
    unclear = {r for r, v in a.items() if v[0] == 'unclear'}
    outside = {r for r, v in a.items() if v[0] == 'outside'}
    corrected = inherited | supported
    status = s[e]['effective_stage1_status'] if corrected else 'PENDING'
    metadata = json.loads(q[e]['raw_record_metadata'])
    row = {'target_occurrence_EID': e, 'new_review_event_EID': f'E-{3500+i}',
           'primary_check_state': 'CHECKED', 'source_type_metadata_proxy': metadata.get('type') or 'UNKNOWN',
           'previous_status': s[e]['effective_stage1_status'], 'previous_RIDs': s[e]['effective_RIDs'],
           'affected_RIDs': ';'.join(sorted(affected)), 'supported_affected_RIDs': ';'.join(sorted(supported)),
           'unclear_affected_RIDs': ';'.join(sorted(unclear)), 'outside_affected_RIDs': ';'.join(sorted(outside)),
           'inherited_unrevalidated_RIDs': ';'.join(sorted(inherited)), 'corrected_explicit_RIDs': ';'.join(sorted(corrected)),
           'proposed_stage1_status': status, 'proposed_primary_code': 'advance/uncertain' if status == 'ADVANCE' else 'PENDING',
           'routing': 'Retain lead; retrieve original/resolve affected mapping. Not X3; no all-R exclusion review.' if unclear or not corrected else 'Retain existing lead; full-text and identity checks pending.',
           'affected_mapping_judgments_json': json.dumps(a, ensure_ascii=False, sort_keys=True),
           'read_receipt': receipts[e][0], 'queue_record_sha256': receipts[e][1]['queue_record_sha256'],
           'abstract_status': q[e]['abstract_status'], 'metadata_unknown_fields': ';'.join(k for k in ('type','language','venue','publication_date') if not metadata.get(k)),
           'metadata_unknown_mapping_boundary': 'UNCLEAR for any mapping inference dependent on missing metadata; semantic judgments above use only supplied text, never inferred source eligibility.',
           'identity_date_language_type': 'PENDING original-source/version/full-text verification',
           'fulltext': 'NOT RUN', 'citations': 'NOT RUN', 'claim_support': 'UNASSESSED', 'methodological_confidence': 'UNASSESSED',
           'reviewer': 'GPT-6.1 Sol AI technical reviewer; separate-pass self-audit, not independent human',
           'gate_effect': 'NONE; G3/G4 OPEN', 'secondary_QA': 'PLANNED; consult secondary artifacts'}
    for v in a.values(): mapping_counts[v[0]] += 1
    rows.append(row)
p = HERE / 'overlay_130.csv'
assert not p.exists()
with p.open('w', newline='') as out:
    writer = csv.DictWriter(out, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
by_e = {r['target_occurrence_EID']: r for r in rows}
changed = [e for e in f['exact_targets'] if by_e[e]['previous_RIDs'] != by_e[e]['corrected_explicit_RIDs']]
groups = []
for g in f['affected_groups']:
    members = [e for e in g['members'] if g['R'] in by_e[e]['corrected_explicit_RIDs'].split(';')]
    groups.append({'R': g['R'], 'source_type_metadata_proxy': g['source_type_metadata_proxy'], 'original_QC': g['qc'],
                   'corrected_positive_members': members, 'first_EID': min(members) if members else None,
                   'nonpositive_unresolved_or_outside_members': [e for e in g['members'] if e not in members]})
selected = set(changed) | {g['first_EID'] for g in groups if g['first_EID']}
write_json('primary_results_freeze.json', {'frozen_at_utc': stamp(), 'state': 'PRIMARY COMPLETE; secondary not yet read',
    'target_order': f['exact_targets'], 'event_order': [r['new_review_event_EID'] for r in rows],
    'input_hashes': {str(p): sha(p.read_bytes()) for p in (QUEUE, SNAPSHOT, FREEZE, PROSPECTIVE)},
    'primary_output_hashes': {p.name: sha(p.read_bytes()) for p in sorted(HERE.glob('authored_primary*.json'))+sorted(HERE.glob('primary_read_receipt*.json'))+[HERE/'overlay_130.csv']},
    'mapping_result_counts': dict(mapping_counts), 'affected_groups': groups})
write_json('secondary_freeze.json', {'frozen_at_utc': stamp(), 'state': 'PLANNED before any secondary original-export checks',
    'primary_results_freeze_sha256': sha((HERE/'primary_results_freeze.json').read_bytes()),
    'overlay_sha256': sha((HERE/'overlay_130.csv').read_bytes()),
    'selection_rule': 'Every target whose positive RID set changed, plus first EID in each nonempty corrected affected R/type group; all new exclusions (none). No new mappings or X3 proposals.',
    'changed_positive_members': changed, 'new_exclusions': [], 'corrected_affected_groups': groups,
    'selected_targets': [e for e in f['exact_targets'] if e in selected],
    'selected_count': len(selected), 'reviewer': 'Sol separate-pass AI self-audit; not independent human'})
write_json('primary_counts.json', {'primary_checked': 130, 'primary_unreviewed': 0,
    'affected_mapping_count': sum(mapping_counts.values()), 'affected_mapping_results': dict(mapping_counts),
    'positive_mapping_set_changed_targets': len(changed), 'new_mappings': 0, 'new_X3_proposals': 0,
    'new_exclusions': 0, 'secondary_planned': len(selected), 'secondary_checked_at_freeze': 0,
    'old_status_counts': dict(Counter(r['previous_status'] for r in rows)),
    'proposed_status_counts': dict(Counter(r['proposed_stage1_status'] for r in rows)),
    'original_global_results': {'groups':42, 'supported':30, 'held':12, 'preserved':True},
    'full_text': 'NOT RUN', 'citations': 'NOT RUN', 'claim_support': 'UNASSESSED',
    'methodological_confidence': 'UNASSESSED', 'G3':'OPEN','G4':'OPEN'})
print(json.dumps({'primary_checked':len(rows), 'mapping_counts':dict(mapping_counts), 'changed':len(changed), 'secondary_selected':len(selected), 'secondary_targets':[e for e in f['exact_targets'] if e in selected]}, indent=2))

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from freeze import HERE, ROOT, QUEUE, digest, rows

checks = list(csv.DictReader((HERE / 'item_checks.tsv').open(), delimiter='\t'))
freeze = json.loads((HERE / 'target_freeze.json').read_text())
assert [c['target_EID'] for c in checks] == freeze['targets']
q = {r['occurrence_E_ID']: r for r in rows(QUEUE)}
groups = {}
for c in checks:
    assert c['rationale'] and c['proposed_status'] in ['ADVANCE', 'PENDING', 'X3']
    for rid in filter(None, c['RIDs'].split(';')):
        assert rid in ['R1', 'R2', 'R3', 'R4', 'R5', 'R6']
        typ = json.loads(q[c['target_EID']]['raw_record_metadata']).get('type') or 'unknown'
        groups.setdefault(f'{rid}|{typ}', []).append(c['target_EID'])
snapshot = dict(created_utc=datetime.now(timezone.utc).isoformat(), phase='PLANNED BEFORE second-pass group/exclusion QA', original_queue_sha256=digest(QUEUE), item_checks_sha256=digest(HERE / 'item_checks.tsv'), scope='105 remaining OA occurrences only; metadata type and explicit authored R tokens, first lexicographic occurrence EID; not canonical S-ID/C-ID claim QC', groups=[dict(group=k, members=sorted(v), selected=min(v), nonselected_count=len(v)-1, state='PLANNED') for k,v in sorted(groups.items())], proposed_exclusions=[c for c in checks if c['proposed_status']=='X3'], unmapped_pending=[c['target_EID'] for c in checks if c['proposed_status']=='PENDING' and not c['RIDs']], proposed_counts=dict(Counter(c['proposed_status'] for c in checks)), original_text_checks_completed=105, original_text_checks_unreviewed=[])
with (HERE / 'group_exclusion_freeze.json').open('x') as f:
    json.dump(snapshot, f, indent=2)
    f.write('\n')
print(json.dumps({k:v for k,v in snapshot.items() if k not in ['groups','proposed_exclusions']},indent=2))
print('GROUP SAMPLE', [(g['group'],g['selected']) for g in snapshot['groups']])

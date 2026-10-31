"""Freeze metadata-QA targets before reading; never modifies producer receipts."""
import csv
import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'

def rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def producer():
    result = {}
    for name in ['OA1', 'OA2']:
        for row in rows(BASE / name / 'overlay.csv'):
            eid = row['target_occurrence_EID']
            status = row.get('new_semantic_disposition') or {'exclude': 'X3', 'advance': 'ADVANCE', 'pending': 'PENDING'}[row['stage1_disposition'].lower()]
            result[eid] = dict(folder=name, status=status.upper(), event=row['new_review_event_EID'], RIDs=row.get('RIDs', row.get('actual_scope_RIDs', '')), raw=row)
    return result

if __name__ == '__main__':
    assert sha(SOURCE) == '92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad'
    original = rows(SOURCE)
    proposed = producer()
    target = [r for r in original if r['occurrence_E_ID'] in proposed and proposed[r['occurrence_E_ID']]['status'] == 'X3']
    assert len(target) == 173
    groups = defaultdict(list)
    for row in original[:300]:
        p = proposed[row['occurrence_E_ID']]
        if p['status'] == 'X3':
            continue
        for rid in sorted(set(re.findall(r'R[1-6]', p['RIDs']))):
            groups[(rid, json.loads(row['raw_record_metadata']).get('type', 'unknown'))].append(row['occurrence_E_ID'])
    files = {}
    for folder in ['OA1', 'OA2', 'Scholar']:
        for path in sorted((BASE / folder).iterdir()):
            if path.is_file():
                files[str(path.relative_to(BASE))] = sha(path)
    manifest = dict(created_utc=datetime.now(timezone.utc).isoformat(), protocol='ERP-2026-10-25-v1.0', input_sha256=sha(SOURCE), input_rows=len(original), producer_hashes=files, target_count=173, targets=[dict(EID=r['occurrence_E_ID'], platform_ID=r['platform_record_id'], source_url=r['record_url'], producer=proposed[r['occurrence_E_ID']]['folder'], producer_event=proposed[r['occurrence_E_ID']]['event']) for r in target], groups=[dict(RID=k[0], metadata_type=k[1], members=v, selected=v[0], nonselected_count=len(v)-1) for k,v in sorted(groups.items())], group_rule='First original occurrence EID per provisional producer R/type group among 127 advance/pending records; occurrence proxy, NOT ERP claim/SID QC.', status='FROZEN BEFORE SOL ORIGINAL-TEXT RECHECK; producer Scholar freeze remains missed; original claims unassessed')
    dest = BASE / 'Sol_frozen_QA_manifest.json'
    assert not dest.exists(), 'Do not overwrite frozen selection'
    dest.write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(dict(manifest_sha256=sha(dest), target_count=len(target), group_count=len(groups), exact_selected_EIDs=sorted({v[0] for v in groups.values()})), indent=2))

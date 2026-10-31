import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
QUEUE = ROOT.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def rows(p):
    with p.open(newline='') as f:
        return list(csv.DictReader(f))

if __name__ == '__main__':
    targets = [r['target_occurrence_EID'] for r in rows(ROOT / 'OA Remaining 105/overlay.csv')]
    original = rows(QUEUE)
    assert len(targets) == len(set(targets)) == 105
    assert [r['occurrence_E_ID'] for r in original if r['occurrence_E_ID'] in targets] == targets
    assert digest(QUEUE) == '92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad'
    inputs = [QUEUE, ROOT / 'Sol_effective_state_838.csv', ROOT / 'Sol_OA_unvalidated_semantic_QA.csv'] + sorted((ROOT / 'OA Remaining 105').iterdir())
    receipt = dict(created_utc=datetime.now(timezone.utc).isoformat(), phase='BEFORE Sol original-text recheck', targets=targets, corrective_events=[f'E-{2600+i}' for i in range(105)], inputs={str(p.relative_to(ROOT.parent)): digest(p) for p in inputs}, baseline={'ADVANCE':94,'X3':44,'PENDING':700}, planned_original_text_checks=105, exclusions_proposed=[], limits='Occurrence eligibility only; no SIDs/claims/fulltexts/citations/gate closure. Group sample will be frozen separately after actual item mapping.')
    with (HERE / 'target_freeze.json').open('x') as f:
        json.dump(receipt, f, indent=2)
        f.write('\n')

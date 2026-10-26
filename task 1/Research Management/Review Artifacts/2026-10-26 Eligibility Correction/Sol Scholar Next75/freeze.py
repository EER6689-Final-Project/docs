from pathlib import Path
import hashlib, json
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
# Resolve relative to Research Management, without opening any queue records.
QUEUE = HERE.parent.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = HERE.parent / 'Scholar Batch 2'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
inputs = [QUEUE, *(PRODUCER / n for n in ['overlay.csv', 'target_freeze.json', 'summary.json', 'handoff.md'])]
out = {
    'protocol': 'ERP-2026-10-25-v1.0', 'cutoff': '2026-10-25 inclusive',
    'frozen_at_utc': datetime.now(timezone.utc).isoformat(),
    'target_EIDs': [f'E-{n:04d}' for n in range(525,600)],
    'event_IDs': [f'E-{n}' for n in range(3100,3175)],
    'input_sha256': {str(p): sha(p) for p in inputs},
    'original_record_read_status_at_freeze': 'NOT RUN',
    'producer_secondary_QA': 'NOT RUN; not inherited as complete',
    'scope': 'Only Sol Scholar Next75; no canonical or aggregate updates'
}
assert out['input_sha256'][str(QUEUE)] == '92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad'
assert out['input_sha256'][str(PRODUCER / 'overlay.csv')] == '07ffe6c53f45704428287e6687c2dbd66b2cdbed3d719821be837dc8a7d77b0d'
dest = HERE / 'target_freeze.json'
with dest.open('x') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(dest)

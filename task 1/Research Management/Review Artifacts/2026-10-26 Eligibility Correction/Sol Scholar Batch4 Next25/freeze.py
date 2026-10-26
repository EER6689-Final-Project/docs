import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path('/home/mendydias/Projects/eei6689')
QUEUE = ROOT / 'task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = HERE.parent / 'Scholar Batch4 Remaining75'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

if __name__ == '__main__':
    ids = [f'E-{n:04d}' for n in range(725, 750)]
    inputs = [QUEUE] + sorted(p for p in PRODUCER.iterdir() if p.is_file())
    receipt = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                   phase='before Sol original stored export reads',
                   protocol='ERP-2026-10-25-v1.0', cutoff='2026-10-25',
                   target_ids=ids, target_count=25,
                   target_ids_sha256=hashlib.sha256(('\n'.join(ids)+'\n').encode()).hexdigest(),
                   corrective_events=[f'E-{n}' for n in range(3800,3825)],
                   producer_events_preserved=[f'E-{n}' for n in range(3700,3725)],
                   inputs={str(p.relative_to(ROOT)):sha(p) for p in inputs},
                   outside_scope='E-0750–E-0799 unreviewed by this task; no other batch reads')
    with (HERE / 'target_freeze.json').open('x') as f:
        json.dump(receipt, f, indent=2)
        f.write('\n')
    print(json.dumps(receipt, indent=2))

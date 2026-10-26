import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path('/home/mendydias/Projects/eei6689')
QUEUE = ROOT / 'task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = HERE.parent / 'Scholar Batch4/overlay_first25.csv'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if __name__ == '__main__':
    ids = [f'E-{n:04d}' for n in range(700, 725)]
    # Freeze bytes and exact requested IDs before parsing/displaying original records.
    receipt = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'protocol': 'ERP-2026-10-25-v1.0', 'cutoff': '2026-10-25',
        'phase': 'before Sol original stored export reread',
        'original_queue': str(QUEUE.relative_to(ROOT)), 'original_queue_sha256': sha(QUEUE),
        'producer': str(PRODUCER.relative_to(ROOT)), 'producer_sha256': sha(PRODUCER),
        'target_ids': ids, 'target_count': 25,
        'target_ids_sha256': hashlib.sha256(('\n'.join(ids)+'\n').encode()).hexdigest(),
        'corrective_events': [f'E-{n}' for n in range(3400,3425)],
        'producer_events_preserved': [f'E-{n}' for n in range(3300,3325)],
        'other_75': 'E-0725–E-0799 not reviewed in this task',
        'stage1_scope': 'original stored title/snippet/metadata only; no online retrieval',
    }
    with (HERE / 'target_freeze.json').open('x') as f:
        json.dump(receipt, f, indent=2)
        f.write('\n')
    print(json.dumps(receipt, indent=2))

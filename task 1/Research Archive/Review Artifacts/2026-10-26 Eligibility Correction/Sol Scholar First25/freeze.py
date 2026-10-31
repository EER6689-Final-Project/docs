"""One-shot prospective receipt; hashes original bytes without reading source fields."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
QUEUE = ROOT / 'Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = HERE.parent / 'Scholar Batch 1'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if __name__ == '__main__':
    target = HERE / 'target_freeze.json'
    assert not target.exists(), 'Never overwrite a freeze'
    receipt = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'phase': 'Before Sol original TITLE/SNIPPET/metadata semantic inspection; producer overlay already read',
        'protocol': 'ERP-2026-10-25-v1.0', 'cutoff_inclusive': '2026-10-25',
        'queue_path': str(QUEUE), 'queue_sha256': sha(QUEUE),
        'targets': [f'E-{i:04d}' for i in range(500, 525)],
        'corrective_events': [f'E-{i:04d}' for i in range(2800, 2825)],
        'producer_files': {p.name: sha(p) for p in sorted(PRODUCER.iterdir()) if p.is_file()},
        'baseline_only': {'ADVANCE': 94, 'X3': 44, 'PENDING': 700},
        'scope': '25 metadata occurrences only; no concurrent overlay read/merge; no full-text, citation, claims or gates',
    }
    assert receipt['queue_sha256'] == '92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad'
    target.write_text(json.dumps(receipt, indent=2) + '\n')
    print(sha(target))

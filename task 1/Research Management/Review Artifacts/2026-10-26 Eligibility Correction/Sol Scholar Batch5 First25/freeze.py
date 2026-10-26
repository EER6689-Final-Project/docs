from pathlib import Path
import csv, hashlib, json, datetime

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
SOURCE = ROOT / 'task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = OUT.parent / 'Scholar Batch5'
def digest(p):
    b = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
rows = list(csv.DictReader(SOURCE.open(newline='')))
ids = [f'E-{i:04d}' for i in range(800,825)]
key = next(k for k in rows[0] if rows[600].get(k) == 'E-0800')
selected = [r for r in rows if r[key] in ids]
assert [r[key] for r in selected] == ids
freeze = {'frozen_at': datetime.datetime.now().astimezone().isoformat(), 'protocol': 'ERP-2026-10-25-v1.0', 'cutoff': '2026-10-25', 'source': digest(SOURCE), 'producer_files': [digest(p) for p in sorted(PRODUCER.iterdir()) if p.is_file()], 'id_column': key, 'scope': ids, 'source_rows_sha256': hashlib.sha256(json.dumps(selected,ensure_ascii=False,sort_keys=True).encode()).hexdigest(), 'event_mapping': dict(zip(ids,[f'E-{i:04d}' for i in range(4000,4025)])), 'original_text_read_started': False}
(OUT/'primary-input-freeze.json').write_text(json.dumps(freeze,indent=2)+'\n')
print(json.dumps(freeze,indent=2))

"""Local, delta-only review receipts; never mutates inputs or other directories."""
import utils.session
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
QUEUE = BASE.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'
SNAPSHOT = BASE / 'Accepted Snapshot 3/effective_state_838.csv'
FREEZE = BASE / 'OA Global Group QA/expansion_freeze.json'
PROSPECTIVE = BASE / 'OA Global Group QA/prospective_freeze.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def stamp():
    return datetime.now(timezone.utc).isoformat()

def load():
    f = json.loads(FREEZE.read_text())
    assert len(f['exact_targets']) == len(set(f['exact_targets'])) == 130
    assert len(f['affected_groups']) == 12
    assert sha(QUEUE.read_bytes()) == f['input']['original_queue_sha256']
    assert sha(SNAPSHOT.read_bytes()) == f['input']['sha256']
    q = {r['occurrence_E_ID']: r for r in csv.DictReader(QUEUE.open())}
    s = {r['occurrence_E_ID']: r for r in csv.DictReader(SNAPSHOT.open())}
    for g in f['affected_groups']:
        members = sorted(e for e, r in s.items() if e.startswith('E-0') and 200 <= int(e[2:]) < 500
                         and g['R'] in r['effective_RIDs'].split(';')
                         and json.loads(q[e]['raw_record_metadata']).get('type', 'unknown') == g['source_type_metadata_proxy'])
        assert members == g['members'], (g, members)
    return f, q, s

def emit(start, end, phase='primary'):
    f, q, s = load()
    ids = f['exact_targets'][start:end]
    if phase == 'secondary':
        ids = json.loads((HERE / 'secondary_freeze.json').read_text())['selected_targets'][start:end]
    if phase == 'pattern':
        ids = json.loads((HERE / 'secondary_pattern_expansion_freeze.json').read_text())['exact_targets'][start:end]
    receipt = {'phase': phase, 'emitted_at_utc': stamp(), 'note': 'Tool emission, not elapsed semantic reading time or live source access.', 'records': []}
    for e in ids:
        r = q[e]
        obj = {'target': e, 'event': f"E-{3500+f['exact_targets'].index(e)}", 'affected': [g['R'] for g in f['affected_groups'] if e in g['members']],
               'previous_RIDs': s[e]['effective_RIDs'], 'previous_status': s[e]['effective_stage1_status'],
               'title': r['title'], 'abstract_status': r['abstract_status'], 'entire_abstract': r['abstract_or_snippet'],
               'metadata': {k: r[k] for k in ('publication_year', 'publication_date', 'language', 'doi', 'platform_record_id', 'record_url', 'raw_record_metadata', 'operation', 'query', 'rank', 'source_platform')},
               'queue_record_sha256': sha(json.dumps(r, ensure_ascii=False, sort_keys=True).encode())}
        receipt['records'].append(obj)
        print(json.dumps(obj, ensure_ascii=False))
    p = HERE / f'{phase}_read_receipt_{start:03d}_{end:03d}.json'
    assert not p.exists(), p
    p.write_text(json.dumps(receipt, indent=2, ensure_ascii=False)+'\n')

def checkpoint():
    f, q, s = load()
    authored = {}
    paths = sorted(HERE.glob('authored_primary_*.json'))
    for p in paths:
        a = json.loads(p.read_text())
        assert not set(a) & set(authored)
        authored.update(a)
    for e, judgments in authored.items():
        assert set(judgments) == {g['R'] for g in f['affected_groups'] if e in g['members']}
    obj = {'created_at_utc': stamp(), 'authored_checked_count': len(authored),
           'checked_targets': [e for e in f['exact_targets'] if e in authored],
           'unreviewed_targets': [e for e in f['exact_targets'] if e not in authored],
           'input_hashes': {str(p): sha(p.read_bytes()) for p in (QUEUE, SNAPSHOT, FREEZE, PROSPECTIVE)},
           'authored_file_hashes': {p.name: sha(p.read_bytes()) for p in paths},
           'receipt_hashes': {p.name: sha(p.read_bytes()) for p in sorted(HERE.glob('*read_receipt*.json'))}}
    p = HERE / f'checkpoint_{len(authored):03d}.json'
    assert not p.exists()
    p.write_text(json.dumps(obj, indent=2)+'\n')
    print(json.dumps({'checkpoint': p.name, 'sha256': sha(p.read_bytes()), 'checked': len(authored), 'unreviewed': len(f['exact_targets'])-len(authored)}))

if __name__ == '__main__':
    if sys.argv[1] == 'checkpoint':
        checkpoint()
    else:
        emit(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3] if len(sys.argv)>3 else 'primary')

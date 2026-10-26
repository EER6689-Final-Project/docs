"""Validate durable outputs; never overwrite a receipt."""
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def read_csv(p):
    with p.open(newline='') as f:
        return list(csv.DictReader(f))

freeze = json.loads((HERE/'target_freeze.json').read_text())
for path, expected in freeze['inputs'].items():
    assert sha(ROOT.parent/path) == expected, path
queue = read_csv(ROOT.parent/'2026-10-26 Discovery/REVIEWQUEUE.csv')
baseline = read_csv(ROOT/'Sol_effective_state_838.csv')
effective = read_csv(HERE/'effective_state_838.csv')
overlay = read_csv(HERE/'overlay.csv')
assert len(queue) == len(baseline) == len(effective) == 838
assert len(overlay) == 105
assert [r['target_occurrence_EID'] for r in overlay] == freeze['targets']
assert [r['new_review_event_EID'] for r in overlay] == freeze['corrective_events']
targets = set(freeze['targets'])
for q,b,e in zip(queue,baseline,effective):
    assert all(e[k]==v for k,v in q.items())
    assert e['effective_claim_support'] == e['effective_methodological_confidence'] == 'UNASSESSED'
    assert e['effective_fulltext'] == e['effective_citations'] == 'NOT RUN'
    if q['occurrence_E_ID'] not in targets:
        assert all(e[k]==v for k,v in b.items())
    else:
        h = json.loads(e['completion_history_json'])
        assert h['baseline']['corrective_event'] == b['effective_corrective_event_EID']
        assert h['baseline']['history_link'] == b['effective_history_link']
        assert h['completion']['event'] == e['effective_corrective_event_EID']
for r in overlay:
    assert r['claim_support'] == r['methodological_confidence'] == r['source_claim_QC'] == 'UNASSESSED'
    assert r['fulltext'] == r['citations'] == 'NOT RUN'
qtargets = [q for q in queue if q['occurrence_E_ID'] in targets]
assert read_csv(HERE/'original_export_targets.csv') == qtargets
assert len(json.loads((HERE/'group_exclusion_QA_results.json').read_text())['groups']) == 18
manifest = []
for p in sorted(HERE.iterdir()):
    if p.is_dir():
        raise AssertionError(f'Unexpected generated directory: {p}')
    if p.name == 'file_manifest.json':
        continue
    entry = dict(path=p.name, sha256=sha(p), bytes=p.stat().st_size)
    if p.suffix in ['.csv','.tsv']:
        with p.open(newline='') as f:
            reader=csv.reader(f, delimiter='\t' if p.suffix=='.tsv' else ',')
            records=list(reader)
        entry.update(record_count=len(records)-1, count_basis='data records excluding header; occurrences/events/checks as named, not distinct works')
        assert all(len(r)==len(records[0]) for r in records)
    else:
        entry.update(line_count=len(p.read_text().splitlines()), count_basis='text lines, not source or work counts')
    manifest.append(entry)
with (HERE/'file_manifest.json').open('x') as f:
    json.dump(dict(algorithm='SHA-256', self_excluded=True, mechanical_verification='PASSED; does not establish scientific validity', files=manifest),f,indent=2)
    f.write('\n')
print(f'PASS: {len(manifest)} files hashed; 838 original rows preserved; 105 ordered events; prior 195 and Scholar 538 unchanged.')

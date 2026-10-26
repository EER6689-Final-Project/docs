import csv
import json
from datetime import datetime, timezone
from freeze import HERE, QUEUE, PRODUCER, sha

freeze = json.loads((HERE / 'target_freeze.json').read_text())
assert sha(QUEUE) == freeze['original_queue_sha256']
assert sha(PRODUCER) == freeze['producer_sha256']
with QUEUE.open() as f:
    rows = [r for r in csv.DictReader(f) if r['occurrence_E_ID'] in freeze['target_ids']]
with PRODUCER.open() as f:
    producers = {r['occurrence_E_ID']: r for r in csv.DictReader(f)}
judgments = json.loads((HERE / 'judgments.json').read_text())
assert [r['occurrence_E_ID'] for r in rows] == [j['id'] for j in judgments] == freeze['target_ids']
out = []
groups = {}
for i, (r, j) in enumerate(zip(rows, judgments)):
    eid = j['id']
    p = producers[eid]
    assert p['producer_review_event_ID'] == f'E-{3300+i}'
    item = dict(r)
    item.update({
        'corrective_event_ID': f'E-{3400+i}', 'producer_event_ID_preserved': p['producer_review_event_ID'],
        'producer_disposition_preserved': p['stage1_disposition'],
        'effective_stage1_disposition': 'ADVANCE', 'effective_primary_exclusion_code': '',
        'effective_R1_judgment': f"NOT ESTABLISHED: {r['title']} concerns non-browser measurement comparison; no browser metric definition, unit or lifecycle construct is exported.",
        'effective_R2_judgment': f"NOT ESTABLISHED: This {j['proxy']} supplies no capture/observation manipulation or profiling off/on contrast; method measurement error is not automatically observer perturbation.",
        'effective_R3_judgment': f"NOT ESTABLISHED: The exported comparison in {r['raw_record_metadata']} does not establish synthetic-to-field browser workload or user transfer.",
        'effective_R4_judgment': j['r4'], 'effective_R5_judgment': j['r5'],
        'effective_R6_judgment': f"NOT ESTABLISHED: {r['title']} supplies no browser solution-overlap, fixture causality or allocation/blocking evidence; generic comparison/design wording is insufficient.",
        'effective_explicit_R_IDs': 'R4;R5' if j['r4'].startswith(('ANALOGUE', 'LIMITATION')) else 'R5',
        'effective_itemwise_rationale': j['reason'], 'source_type_proxy': j['proxy'],
        'effective_identity': 'PENDING; no SID/DUP/merge adjudication',
        'effective_date': 'PENDING; original date/version unverified; no cutoff exclusion',
        'effective_language': 'PENDING; full-text language/authorized translation unverified',
        'effective_source_type': 'PENDING; proxy is not validated primary-evidence classification',
        'effective_fulltext': 'NOT RUN', 'effective_citations': 'NOT RUN',
        'effective_claim_support': 'UNASSESSED', 'effective_methodological_confidence': 'UNASSESSED',
        'primary_original_export_read': 'YES; entire stored title/snippet and metadata inspected',
    })
    out.append(item)
    for rid in item['effective_explicit_R_IDs'].split(';'):
        groups.setdefault(f'{rid}|{j["proxy"]}', []).append(eid)
with (HERE / 'delta_overlay25.csv').open('x', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
with (HERE / 'item_checks.tsv').open('x', newline='') as f:
    keys = ['occurrence_E_ID', 'corrective_event_ID', 'source_type_proxy', 'effective_explicit_R_IDs'] + [f'effective_R{i}_judgment' for i in range(1,7)] + ['effective_itemwise_rationale']
    w = csv.DictWriter(f, fieldnames=keys, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(out)
receipt = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'phase': 'after completed primary review; before secondary original-export reread',
    'primary_overlay_sha256': sha(HERE / 'delta_overlay25.csv'),
    'judgments_sha256': sha(HERE / 'judgments.json'),
    'original_queue_sha256': sha(QUEUE), 'producer_sha256': sha(PRODUCER),
    'proposed_exclusions': [],
    'group_basis': 'actual explicit positive R4/R5 judgments only; exported title/metadata source-type proxies, not query membership; no canonical S/C groups',
    'groups': [{'group': k, 'members': v, 'selected_first_EID': min(v), 'nonselected_count': len(v)-1} for k,v in sorted(groups.items())],
    'selected_ids': sorted({min(v) for v in groups.values()}),
    'checker': 'Sol separate-pass AI self-audit; not independent human review',
}
with (HERE / 'qa_freeze.json').open('x') as f:
    json.dump(receipt, f, indent=2); f.write('\n')
print(json.dumps(receipt, indent=2))

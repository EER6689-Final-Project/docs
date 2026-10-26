"""Mechanical joins and receipts only; semantic judgments are authored separately."""
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from freeze import HERE, QUEUE, PRODUCER, sha

def dump(name, obj):
    p = HERE / name
    assert not p.exists(), f'Never overwrite {name}'
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n')

def table(name, rows):
    p = HERE / name
    assert not p.exists()
    with p.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

if __name__ == '__main__':
    freeze = json.loads((HERE / 'target_freeze.json').read_text())
    assert sha(QUEUE) == freeze['queue_sha256']
    assert all(sha(PRODUCER / n) == h for n, h in freeze['producer_files'].items())
    source = list(csv.DictReader(QUEUE.open()))
    targets = [r for r in source if r['occurrence_E_ID'] in freeze['targets']]
    producer = list(csv.DictReader((PRODUCER / 'overlay_first25.csv').open()))
    checks = json.loads((HERE / 'author_checks.json').read_text())
    assert len(source) == 838 and len(targets) == len(checks) == len(producer) == 25
    overlay, actual, groups, oldgroups = [], [], {}, {}
    for n, (r, p, c) in enumerate(zip(targets, producer, checks)):
        eid = r['occurrence_E_ID']
        assert eid == p['occurrence_E_ID'] == c['id'] == freeze['targets'][n]
        assert r['title'] == p['title'] and r['abstract_or_snippet'] == p['source_snippet']
        o = dict(r)
        o.update(event_E_ID=f'E-{2800+n:04d}', supersedes_producer_event=p['event_E_ID'], producer_disposition=p['stage1_disposition'], effective_stage1_disposition=c['decision'], effective_primary_code=c['decision'], effective_reason=c['reason'], effective_source_type_proxy=c['type'], correction=c['correction'], actual_original_metadata_check='CHECKED; entire supplied title/snippet and metadata, not full text', effective_claim_support='UNASSESSED', effective_methodological_confidence='UNASSESSED', effective_fulltext_pass='NOT RUN', effective_citation_pass='NOT RUN', effective_identity='PENDING; no canonical reconciliation', effective_date='PENDING; year-only or absent; original date/version unverified', effective_language='PENDING; no full-text language verified', effective_source_type='PENDING; displayed metadata/type proxy only', effective_reviewer='Sol AI metadata QA after Luna AI; not independent human scientific review', effective_review_date='2026-10-26')
        for i, judgment in enumerate(c['R'], 1):
            assert judgment.split(':')[0] in ('relevant', 'unclear', 'outside')
            o[f'effective_R{i}'] = judgment
            if judgment.startswith('relevant:'):
                groups.setdefault(f'R{i}|{c["type"]}', []).append(eid)
            # Exact cell comparison: generic R1–R6 ranges are never parsed as tags.
            if p[f'R{i}'] == f'R{i} relevant':
                oldgroups.setdefault(f'R{i}|{c["type"]}', []).append(eid)
        overlay.append(o)
        actual.append({'occurrence_E_ID': eid, 'event_E_ID': o['event_E_ID'], 'title': r['title'], 'snippet': r['abstract_or_snippet'], 'raw_record_metadata': r['raw_record_metadata'], 'original_year': r['publication_year'], 'original_date': r['publication_date'], 'original_language': r['language'], 'source_type_proxy': c['type'], 'producer_disposition': p['stage1_disposition'], 'Sol_disposition': c['decision'], **{f'R{i}': v for i, v in enumerate(c['R'], 1)}, 'reason': c['reason'], 'correction': c['correction']})
    table('overlay25.csv', overlay)
    table('actual_checks.csv', actual)
    dump('qc_freeze.json', {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'phase': 'AFTER primary original-item review; BEFORE separate secondary original-item pass',
        'target_freeze_sha256': sha(HERE / 'target_freeze.json'),
        'overlay_sha256': sha(HERE / 'overlay25.csv'),
        'author_checks_sha256': sha(HERE / 'author_checks.json'),
        'all_producer_proposed_exclusions': [p['occurrence_E_ID'] for p in producer if p['stage1_disposition'] == 'X3'],
        'all_Sol_proposed_exclusions': [c['id'] for c in checks if c['decision'] == 'X3'],
        'corrected_explicit_R_type_groups': {k: {'members': v, 'first_EID': min(v), 'nonselected_count': len(v)-1} for k, v in sorted(groups.items())},
        'producer_explicit_R_type_groups_for_discrepancy_audit': {k: {'members': v, 'first_EID': min(v), 'nonselected_count': len(v)-1} for k, v in sorted(oldgroups.items())},
        'finite_expansion': freeze['targets'],
        'expansion_reason': 'Unsupported producer mappings and copied rationale; recheck all 25, not only deterministic group samples',
        'status_at_freeze': 'PLANNED; secondary check not yet performed',
        'group_limit': 'Occurrence EIDs and displayed type proxies, not canonical S-ID/C-ID protocol claim QC',
        'checker': 'Sol separate-pass AI self-audit; no independent human review'
    })
    print(json.dumps({'counts': dict(Counter(c['decision'] for c in checks)), 'corrected_groups': len(groups), 'producer_groups': len(oldgroups), 'qc_freeze_sha256': sha(HERE / 'qc_freeze.json')}))

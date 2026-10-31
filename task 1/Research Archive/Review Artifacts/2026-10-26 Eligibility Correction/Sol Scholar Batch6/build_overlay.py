"""Mechanical join only; semantic judgments are authored in authored_checks.tsv."""
from pathlib import Path
import csv
import hashlib
import json
from collections import Counter

OWN = Path(__file__).resolve().parent
BASE = OWN.parent
QUEUE = BASE.parent / '2026-10-26 Discovery' / 'REVIEWQUEUE.csv'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
freeze = json.loads((OWN / 'primary_freeze.json').read_text())
assert sha(QUEUE) == freeze['queue_sha256']
for name, digest in freeze['producer_files'].items():
    assert sha(Path(name)) == digest, name
originals = [r for r in csv.DictReader(QUEUE.open()) if r['occurrence_E_ID'] in freeze['target_ids']]
producer = {r['occurrence_E_ID']: r for r in csv.DictReader((BASE / 'Scholar Batch6/overlay.csv').open())}
checks = list(csv.DictReader((OWN / 'authored_checks.tsv').open(), delimiter='\t'))
by_id = {r['EID']: r for r in checks}
assert len(by_id) == len(checks)
qa_path = OWN / 'secondary_authored.tsv'
qa = {r['EID']: r for r in csv.DictReader(qa_path.open(), delimiter='\t')} if qa_path.exists() else {}
if qa and not (OWN / 'primary_overlay.csv').exists():
    secondary_freeze = json.loads((OWN / 'secondary_freeze.json').read_text())
    assert sha(OWN / 'overlay.csv') == secondary_freeze['primary_overlay_sha256']
    (OWN / 'primary_overlay.csv').write_bytes((OWN / 'overlay.csv').read_bytes())
out = []
reads = []
for i, original in enumerate(originals):
    eid = original['occurrence_E_ID']
    c = by_id.get(eid)
    r = dict(original)
    r.update(effective_event_ID=f'E-{4200+i}', effective_disposition=c['disposition'] if c else 'PENDING',
             effective_primary_code='X3' if c and c['disposition'] == 'X3' else '',
             effective_positive_Rs=c['positive_Rs'] if c else '',
             effective_rationale=c['rationale'] if c else 'UNREVIEWED: original content semantic QA not completed.',
             effective_review_status='PRIMARY_CHECKED' if c else 'UNREVIEWED',
             effective_reviewer='Sol AI metadata technical QA; not independent human review',
             effective_review_date='2026-10-26', effective_date_status='UNVERIFIED',
             effective_language_status='UNVERIFIED', effective_source_type_status='UNVERIFIED',
             effective_identity_status='UNVERIFIED; no merges/SIDs', effective_claim_support='UNASSESSED',
             effective_methodological_confidence='UNASSESSED', effective_fulltext_pass='NOT RUN',
             effective_citation_pass='NOT RUN', effective_producer_disposition=producer[eid]['producer_disposition'],
             effective_semantic_basis='Complete stored Scholar snippet/title/exported metadata only; NOT abstract/full text')
    for n in range(1, 7):
        r[f'effective_R{n}_judgment'] = c[f'R{n}'] if c else 'UNREVIEWED'
    r['effective_primary_rationale'] = r['effective_rationale']
    r['effective_secondary_QA_status'] = qa[eid]['QA_status'] if eid in qa else 'PLANNED; NOT CHECKED'
    r['effective_secondary_rationale'] = qa[eid]['secondary_rationale'] if eid in qa else ''
    if eid in qa:
        q = qa[eid]
        r['effective_disposition'] = q['final_disposition']
        r['effective_positive_Rs'] = q['final_positive_Rs']
        r['effective_primary_code'] = 'X3' if q['final_disposition'] == 'X3' else ''
        if q['QA_status'] == 'checked-corrected':
            r['effective_rationale'] = q['secondary_rationale']
            removed = set(c['positive_Rs'].split(';')) - set(q['final_positive_Rs'].split(';'))
            for rid in filter(None, removed):
                r[f'effective_{rid}_judgment'] = 'NOT ESTABLISHED after secondary reread: '+q['secondary_rationale']
            if eid == 'E-0943':
                r['effective_R2_judgment'] = 'Redundant signal capture for fault detection; channel independence unverified'
                r['effective_R5_judgment'] = 'Cross-device signal fault checks; shared-error assumptions unresolved'
    assert all(r[k] == v for k, v in original.items())
    out.append(r)
    if c:
        reads.append({'EID': eid, 'title': original['title'], 'snippet_characters': len(original['abstract_or_snippet']),
                      'original_fields_sha256': hashlib.sha256(json.dumps(original, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
                      'status': 'actually read complete supplied title/snippet/metadata in primary pass',
                      'authored_check': 'authored_checks.tsv#'+eid})
with (OWN / 'overlay.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
(OWN / 'primary_read_manifest.json').write_text(json.dumps(reads, indent=2, ensure_ascii=False)+'\n')
summary = {'target_count': len(out), 'primary_actually_checked': len(checks), 'primary_unreviewed': len(out)-len(checks),
           'secondary_actually_checked': len(qa), 'secondary_unreviewed': len(out)-len(qa),
           'secondary_corrections': [r['EID'] for r in qa.values() if r['QA_status']=='checked-corrected'],
           'effective_counts': dict(Counter(r['effective_disposition'] for r in out)),
           'producer_counts': dict(Counter(r['effective_producer_disposition'] for r in out)),
           'producer_X3_checked': sum(r['effective_producer_disposition']=='X3' and r['effective_review_status']=='PRIMARY_CHECKED' for r in out),
           'rejected_producer_X3': [r['occurrence_E_ID'] for r in out if r['effective_producer_disposition']=='X3' and r['effective_disposition']!='X3' and r['effective_review_status']=='PRIMARY_CHECKED'],
           'producer_advance_holds': [r['occurrence_E_ID'] for r in out if r['effective_producer_disposition']=='ADVANCE' and r['effective_disposition']=='PENDING'],
           'transition_counts': dict(Counter(r['effective_producer_disposition']+' -> '+r['effective_disposition'] for r in out)),
           'original_fields_unchanged': True, 'queue_sha256': sha(QUEUE),
           'accepted_snapshot': 'Snapshot 5 remains accepted until orchestrator acceptance; this is delta only'}
(OWN / 'counts.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))

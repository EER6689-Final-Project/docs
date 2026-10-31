from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import csv, json, hashlib

HERE = Path(__file__).resolve().parent
QUEUE = HERE.parent.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = HERE.parent / 'Scholar Batch 2/overlay.csv'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def readcsv(p, delimiter=','):
    with p.open(newline='') as f:
        return list(csv.DictReader(f, delimiter=delimiter))
def writejson(name, obj):
    with (HERE / name).open('x') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')

freeze = json.loads((HERE / 'target_freeze.json').read_text())
for p, digest in freeze['input_sha256'].items():
    assert sha(Path(p)) == digest, p
targets = freeze['target_EIDs']
originals = {r['occurrence_E_ID']: r for r in readcsv(QUEUE)}
producer = {r['occurrence_E_ID']: r for r in readcsv(PRODUCER)}
checks = readcsv(HERE / 'author_checks.tsv', '\t')
assert [r['EID'] for r in checks] == targets
assert all(all(r[f'R{i}'].startswith(('candidate:', 'unclear:', 'outside:')) for i in range(1,7)) for r in checks)
assert all(originals[e]['abstract_or_snippet'] for e in targets)
rows, groups = [], defaultdict(list)
for idx, c in enumerate(checks):
    eid = c['EID']
    o, p = originals[eid], producer[eid]
    r = dict(o)
    r.update({
        'event_E_ID': f'E-{3100+idx}', 'producer_event_E_ID': p['event_E_ID'],
        'producer_disposition': p['stage1_disposition_reviewed'],
        'producer_reason': p['itemwise_reason'],
        'stage1_disposition_reviewed': c['decision'],
        'primary_code_reviewed': 'X3' if c['decision'] == 'EXCLUDE' else ('advance/uncertain' if c['decision'] == 'ADVANCE' else 'uncertain relevance/type'),
        'itemwise_reason': c['reason'],
        'Sol_reviewer': 'Sol AI; separate original-export validation',
        'Sol_review_date': '2026-10-26',
        'Sol_access': 'Original title/Scholar snippet/metadata only; not abstract, full text or methods/findings verification',
        'source_type_proxy': o['display_record_label'] or 'unlabelled export; type pending',
        'metadata_verification': 'PENDING: date/cutoff, version, full-text language/translation, source type/originality, canonical identity and duplicates',
        'identity_action': 'No SID assignment, DUP decision, version merge or library mutation',
        'Sol_claim_support': 'UNASSESSED', 'Sol_methodological_confidence': 'UNASSESSED',
        'Sol_fulltext_pass': 'NOT RUN', 'Sol_citation_pass': 'NOT RUN',
        'Sol_secondary_QA_at_primary_freeze': 'PLANNED; consult qc_results.json for actual separate pass',
    })
    changed = []
    for i in range(1,7):
        key = f'R{i}'
        r['producer_'+key] = p[key]
        r[key] = c[key]
        status = c[key].split(':',1)[0]
        if status != {'relevant':'candidate','unclear':'unclear','outside':'outside'}[p[key]]:
            changed.append(key)
        # Membership is a positive, explicitly authored per-R judgment, never a regex over prose.
        if status == 'candidate':
            groups[(key, r['source_type_proxy'])].append(eid)
    r['changed_R_statuses'] = ';'.join(changed)
    r['disposition_changed'] = str(c['decision'] != p['stage1_disposition_reviewed']).lower()
    rows.append(r)
with (HERE / 'overlay75.csv').open('x', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader(); w.writerows(rows)
writejson('primary_receipt.json', {
    'completed_at_utc': datetime.now(timezone.utc).isoformat(),
    'original_records_actually_read': 75, 'authored_six_question_records': 75,
    'original_snippets_present': 75, 'missing_snippets': 0,
    'dispositions': dict(Counter(r['stage1_disposition_reviewed'] for r in rows)),
    'producer_dispositions': dict(Counter(r['producer_disposition'] for r in rows)),
    'overlay_sha256': sha(HERE / 'overlay75.csv'),
    'author_checks_sha256': sha(HERE / 'author_checks.tsv'),
    'source_claims': 'UNASSESSED; all primary judgments are stage-1 routing only',
})
writejson('qc_freeze.json', {
    'frozen_at_utc': datetime.now(timezone.utc).isoformat(),
    'status_at_freeze': 'PLANNED; secondary original-field rereads NOT RUN yet',
    'primary_overlay_sha256': sha(HERE / 'overlay75.csv'),
    'author_checks_sha256': sha(HERE / 'author_checks.tsv'),
    'all_proposed_exclusions': [r['occurrence_E_ID'] for r in rows if r['stage1_disposition_reviewed'] == 'EXCLUDE'],
    'actual_explicit_R_type_proxy_groups': [
        {'R': key[0], 'source_type_proxy': key[1], 'members': members,
         'first_EID': min(members), 'nonselected_count': len(members)-1}
        for key,members in sorted(groups.items())],
    'group_rule': 'Only explicit candidate: fields; source type is exported display label proxy, NOT verified publication type. First EID per actual R/proxy group. No range parsing.',
    'expanded_error_pattern': {
        'reason': 'Producer R6 generic instrumenter/intervention transfer; R4 overhead/experimental-word inflation; semantic-web false associations; native-mechanism omissions. These overlap across the entire finite batch, so check every target rather than infer completion from samples.',
        'members': targets,
    },
    'selected_union': targets,
    'fields_to_recheck': ['title', 'abstract_or_snippet', 'raw_record_metadata', 'publication_year', 'publication_date', 'language', 'display_record_label', 'record_url', 'platform_record_id', 'doi', 'candidate_duplicate_target_E_ID', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'disposition and reason'],
    'checker': 'Sol AI separate-pass self-audit; not independent human scientific review',
    'fulltext_citations': 'NOT RUN',
})
print(json.dumps(json.loads((HERE / 'primary_receipt.json').read_text()), indent=2))
print('QC frozen; no secondary completion asserted.')

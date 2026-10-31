from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv, json, hashlib

HERE = Path(__file__).resolve().parent
QUEUE = HERE.parent.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p, delim=','):
    with p.open(newline='') as f:
        return list(csv.DictReader(f, delimiter=delim))
def dump(name, obj):
    with (HERE / name).open('x') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False); f.write('\n')

frozen = json.loads((HERE / 'target_freeze.json').read_text())
qc = json.loads((HERE / 'qc_freeze.json').read_text())
assert sha(HERE / 'overlay75.csv') == qc['primary_overlay_sha256']
assert sha(HERE / 'author_checks.tsv') == qc['author_checks_sha256']
preservation = {p: {'frozen_sha256': h, 'current_sha256': sha(Path(p)), 'unchanged': sha(Path(p)) == h}
                for p,h in frozen['input_sha256'].items()}
assert all(v['unchanged'] for v in preservation.values())
rows = load(HERE / 'overlay75.csv')
originals = {r['occurrence_E_ID']: r for r in load(QUEUE)}
notes = load(HERE / 'secondary_notes.tsv', '\t')
assert [r['EID'] for r in notes] == qc['selected_union'] == frozen['target_EIDs']
assert [r['event_E_ID'] for r in rows] == frozen['event_IDs']
assert [r['producer_event_E_ID'] for r in rows] == [f'E-{n}' for n in range(2900,2975)]
assert len(rows) == len(notes) == 75
assert all(r['Sol_claim_support'] == r['Sol_methodological_confidence'] == 'UNASSESSED' for r in rows)
assert all(r['Sol_fulltext_pass'] == r['Sol_citation_pass'] == 'NOT RUN' for r in rows)
# Every exported original column is retained byte-for-value; Sol judgments use additive columns.
assert all(all(r[k] == v for k,v in originals[r['occurrence_E_ID']].items()) for r in rows)
actual = []
for r,n in zip(rows,notes):
    eid = r['occurrence_E_ID']
    actual.append({
        'occurrence_E_ID': eid, 'event_E_ID': r['event_E_ID'],
        'status': 'checked-no-discrepancy',
        'status_comparator': 'Sol frozen primary overlay; producer corrections are separately retained in overlay',
        'checker': 'Sol AI', 'pass': 'separate-pass self-audit, not independent human review',
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'queue_sha256': sha(QUEUE),
        'original_record_sha256': hashlib.sha256(json.dumps(originals[eid], sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
        'original_anchor': str(QUEUE) + '#' + eid,
        'original_fields_actually_reread': ';'.join(qc['fields_to_recheck']),
        'original_field_recheck_note': n['original_field_recheck_note'],
        'metadata_result': 'Export fields inspected; underlying date/version/language/type/identity still PENDING',
        'resolution': 'Retain frozen Sol stage-1 decision and six judgments; no additional secondary correction',
        'fulltext_citations': 'NOT RUN', 'claim_support': 'UNASSESSED', 'confidence': 'UNASSESSED',
    })
with (HERE / 'actual_checks.csv').open('x', newline='') as f:
    w=csv.DictWriter(f, fieldnames=list(actual[0])); w.writeheader(); w.writerows(actual)
exclusions = qc['all_proposed_exclusions']
group_results = []
for g in qc['actual_explicit_R_type_proxy_groups']:
    group_results.append({**g, 'status': 'checked-no-discrepancy',
                          'actual_check_EID': g['first_EID'],
                          'actual_check_anchor': 'actual_checks.csv#'+g['first_EID']})
dump('qc_results.json', {
    'completed_at_utc': datetime.now(timezone.utc).isoformat(),
    'frozen_plan_sha256': sha(HERE / 'qc_freeze.json'),
    'frozen_planned': 75, 'actually_checked': 75, 'not_run': 0,
    'separate_pass': True, 'independent_human_review': False,
    'actual_check_statuses': dict(Counter(r['status'] for r in actual)),
    'all_proposed_exclusion_results': [
        {'EID': e, 'code': 'X3', 'status': 'checked-no-discrepancy',
         'check_anchor': 'actual_checks.csv#'+e} for e in exclusions],
    'actual_explicit_group_results': group_results,
    'expanded_error_pattern_results': {
        'members': qc['expanded_error_pattern']['members'],
        'checked': 75, 'remaining': [], 'status': 'checked-no-discrepancy',
        'meaning': 'No further discrepancy against Sol primary after explicit producer corrections; does not certify producer or whole Scholar.'},
    'R4_R5_groups': 'No positive candidate judgment; unclear/outside is not positive mapped membership. All 75 nevertheless expanded and checked.',
    'metadata_verification': 'PENDING despite inspecting exported metadata fields',
    'claims_confidence': 'UNASSESSED', 'fulltext_citations': 'NOT RUN',
})
changed = [r for r in rows if r['disposition_changed'] == 'true']
counts = {
    'scope': 'Only E-0525 through E-0599 occurrences, not distinct works or whole Scholar',
    'targets': 75, 'primary_original_reads': 75, 'authored_six_R_checks': 75,
    'secondary_original_field_checks': 75, 'primary_unreviewed': 0, 'secondary_unreviewed': 0,
    'producer_dispositions': dict(Counter(r['producer_disposition'] for r in rows)),
    'Sol_dispositions': dict(Counter(r['stage1_disposition_reviewed'] for r in rows)),
    'disposition_changes': len(changed),
    'transition_counts': dict(Counter(r['producer_disposition']+' -> '+r['stage1_disposition_reviewed'] for r in rows)),
    'changed_disposition_EIDs': [r['occurrence_E_ID'] for r in changed],
    'rows_with_R_status_changes': sum(bool(r['changed_R_statuses']) for r in rows),
    'R_status_changes_by_question': {f'R{i}': sum(f'R{i}' in r['changed_R_statuses'].split(';') for r in rows) for i in range(1,7)},
    'positive_candidate_memberships': {f'R{i}': sum(r[f'R{i}'].startswith('candidate:') for r in rows) for i in range(1,7)},
    'X3_occurrences': len(exclusions), 'X3_EIDs': exclusions,
    'actual_R_type_proxy_groups': len(group_results),
    'group_selected_unique_EIDs': sorted({g['first_EID'] for g in group_results}),
    'frozen_exclusions_checked': len(exclusions), 'expanded_checked': 75,
    'stage1_pending_EIDs': [r['occurrence_E_ID'] for r in rows if r['stage1_disposition_reviewed'] == 'PENDING'],
    'metadata_pending': 75, 'claim_support_unassessed': 75, 'confidence_unassessed': 75,
    'fulltext_pass': 'NOT RUN', 'citation_pass': 'NOT RUN', 'canonical_merges': 0,
    'secondary_corrections_against_Sol_primary': 0,
}
dump('counts.json', counts)
dump('preservation_receipt.json', {'inputs': preservation,
    'original_export_fields_preserved_all_75': True,
    'writes_scoped_to': str(HERE),
    'shared_active_outputs': 'Not read or merged; no aggregate updates',
    'producer_secondary_QA': 'Remains NOT RUN; this is a new Sol separate pass only'})
handoff = f'''# Sol Scholar Next75 — bounded validation handoff

**Completed:** all 75 original E-0525–E-0599 title/Scholar-snippet/metadata records read and given six explicit R1–R6 judgments plus case reasoning. Events E-3100–E-3174 retain Luna E-2900–E-2974 as history. Rules: ERP-2026-10-25-v1.0; cutoff 2026-10-25 inclusive. Input hashes and ordered IDs were frozen before Sol's original-record read.

## Delta, not aggregate acceptance

- Producer: 50 ADVANCE / 25 PENDING / 0 EXCLUDE. Sol: **50 ADVANCE / 20 PENDING / 5 X3 EXCLUDE** (occurrences, not unique works).
- {len(changed)} disposition changes: 8 ADVANCE→PENDING, 8 PENDING→ADVANCE, 5 PENDING→EXCLUDE. All 75 received newly authored reasons and question-specific judgments; {counts['rows_with_R_status_changes']} have R-status changes. See `counts.json` and the producer/Sol fields in `overlay75.csv`.
- Removed unsupported semantics→metric, experiment/overhead→R4, protocol/tool comparison→R5, and generic intervention/instrumentation→R6 transfers. Retained exact native mechanisms: plan-loading setup cost (E-0568), dynamic probes (E-0585), live/compiler-inserted hooks (E-0591/E-0594), sampled-memory capture/cost (E-0595), and time/space perturbation (E-0599). These are bounded analogues, not browser validation.
- X3 E-0526: semantic question answering/search; E-0530: replication/object semantics with web performance in biography; E-0538 and E-0544: semantic ontology mapping; E-0547: semantic digital-library architecture. Each was reread against all six questions; no actual measurement/observer/statistical/workload-transfer mechanism is visible. No exclusion is based on access, venue, language metadata, or the word survey. Heuristic duplicate E-0544 remains a separate occurrence, not a second verified work.

## Actually executed QC

`qc_freeze.json` froze every proposed exclusion, all eight nonempty explicit positive-R/exported-type-proxy groups and their first EIDs, plus the expanded full list of 75 **before** secondary rereads. R4/R5 have no positive groups; no generic R-range extraction was used. Unclear fields are not positive memberships; all records were checked through expansion anyway.

After the freeze, all 75 original titles, snippets and metadata/identity fields were reread against the frozen Sol judgments. `secondary_notes.tsv` contains new case-specific reread notes; `actual_checks.csv` records executed checks and original anchors. Five exclusions, eight group representatives and all 75 expanded records are checked; no additional discrepancy against the Sol primary overlay was found. The immutable primary overlay remains unchanged. Primary unreviewed: **0**. Secondary unreviewed: **0**. Pending **eligibility/source-role** cases: **20**, enumerated in `counts.json`; pending is not unfinished screening or exclusion.

Luna's planned secondary QC remains **NOT RUN** in its unchanged artifact. This Sol pass is a separate-pass AI self-audit, **not independent human scientific review**. It applies only to these 75 occurrences, not the whole Scholar corpus or another batch.

## Limits and next owner

These are stage-1 routing decisions only; no abstracts, full texts, methods passages or findings were read, and snippet numbers are not verified source claims. All records had snippets, so no missing-snippet abstract fallback was required. Date/cutoff (especially year-only 2026 and arXiv 2610.22697), version, full-text language/authorized translation, source type/originality, canonical identity and duplicate relationships remain **PENDING for all 75**, including excluded occurrence metadata. Claim support and methodological confidence remain **UNASSESSED**; full-text and citation passes **NOT RUN**. No SID assignment, work merge, library operation, novelty/coverage/gate claim, commit or staging.

The orchestrator may combine this disjoint delta only after acceptance, preserving its finite scope and pending blockers. No parallel OA-completion/Scholar-Batch-3 active outputs were read or combined, and no aggregate snapshot was authored. `preservation_receipt.json` verifies unchanged queue/producer inputs; `file_manifest.json` hashes every deliverable except itself (self-hashing is not possible).
'''
# Verify prose transition counts rather than let a fixed narrative silently drift.
assert counts['transition_counts'].get('ADVANCE -> PENDING') == 8
assert counts['transition_counts'].get('PENDING -> ADVANCE') == 8
assert counts['transition_counts'].get('PENDING -> EXCLUDE') == 5
with (HERE / 'handoff.md').open('x') as f:
    f.write(handoff)
dump('file_manifest.json', {
    'algorithm': 'SHA-256', 'manifest_self_excluded': True,
    'files': {p.name: {'sha256': sha(p), 'bytes': p.stat().st_size}
              for p in sorted(HERE.iterdir()) if p.is_file() and p.name != 'file_manifest.json'},
})
print(json.dumps(counts, indent=2))

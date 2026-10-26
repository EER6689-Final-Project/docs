"""Record actual separately performed secondary review and verify bounded outputs."""
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from freeze import HERE, QUEUE, PRODUCER, sha
from build import dump

FINDINGS = {
    'E-0500': 'Confounding structures are explicit; R6 candidate stands, no uncertainty procedure inferred.',
    'E-0501': 'Only this snippet names cross-browser load-time semantics; workload-complexity candidate stands.',
    'E-0502': 'Click evaluation supports construct contrast; actual user behavior alone does not demonstrate transfer.',
    'E-0503': 'HTML table excerpt cannot sustain earlier R5 relevance; book remains contextual pending.',
    'E-0504': 'Ontology title justifies uncertain routing, not a verified browser definition.',
    'E-0505': 'Replay/network hook stands; accurate title and historical DUP do not establish agreement or identity.',
    'E-0506': 'Network vantage analogue is explicit and bounded; no browser capture/overhead result inferred.',
    'E-0507': 'Confirmed copied cross-browser wording absent; all six mappings appropriately unclear.',
    'E-0508': 'Session semantics support workload-fixture analogy; simulation statistics do not imply R4 methods.',
    'E-0509': 'Thesis/HTML remediation supports R6 only; relation to later conference occurrence unresolved.',
    'E-0510': 'Named aggregate indicators and trustworthiness leave exact timing-construct transfer pending.',
    'E-0511': 'DOM remediation title supports R6, not automatic workload coverage or runtime capture.',
    'E-0512': 'Governance excerpt and book-like metadata leave specific measurement role pending.',
    'E-0513': 'Various link conditions support network-factor transfer, not metric definition or agreement.',
    'E-0514': 'Synthetic/real-user title supports routing; protocol snippet supplies no repeated-measure methods.',
    'E-0515': 'Low-bandwidth and prefetch state support narrow context transfer, not verified effects.',
    'E-0516': 'Protocol comparison is R6 candidate, not matched-tool agreement; workload specifics absent.',
    'E-0517': 'Page-specific FNs support bounded diagnostic dependence, not measurement capture accuracy.',
    'E-0518': 'Proposed novel framework explicit; advance under stage-1 uncertainty, no non-originality presumption.',
    'E-0519': 'Six item-specific outside judgments rechecked. Semantic service reuse/integration/scalability and truncated comparison basis expose no transferable measurement mechanism; X3 stands at snippet-limited stage 1.',
    'E-0520': 'Site-goal click outcome supports R1 contrast; missing year and unresolved repository identity remain holds.',
    'E-0521': 'User success construct is distinct from timing; near-matching E-0520 is not counted as resolved duplicate.',
    'E-0522': 'Overview/server scaling is contextual pending; no precise workload-method transfer assumed.',
    'E-0523': 'Specialized first-view runtime framework supports bounded four-question routing; truncated title/date unresolved.',
    'E-0524': 'Mock data/request semantics support fidelity candidate; experimental label does not establish R4 method.',
}

if __name__ == '__main__':
    freeze = json.loads((HERE / 'target_freeze.json').read_text())
    qc = json.loads((HERE / 'qc_freeze.json').read_text())
    checks = json.loads((HERE / 'author_checks.json').read_text())
    overlay = list(csv.DictReader((HERE / 'overlay25.csv').open()))
    producer = list(csv.DictReader((PRODUCER / 'overlay_first25.csv').open()))
    original = {r['occurrence_E_ID']: r for r in csv.DictReader(QUEUE.open())}
    assert sha(QUEUE) == freeze['queue_sha256']
    assert sha(HERE / 'overlay25.csv') == qc['overlay_sha256']
    assert all(sha(PRODUCER / n) == h for n, h in freeze['producer_files'].items())
    assert set(FINDINGS) == set(freeze['targets'])
    mapping_changed = []
    disposition_changed = []
    for o, p, c in zip(overlay, producer, checks):
        eid = c['id']
        assert all(o[k] == v for k, v in original[eid].items())
        assert o['event_E_ID'] == f'E-{2800+int(eid[2:])-500:04d}'
        if any(p[f'R{i}'].split()[-1] != c['R'][i-1].split(':')[0] for i in range(1, 7)):
            mapping_changed.append(eid)
        if p['stage1_disposition'] != c['decision']:
            disposition_changed.append(eid)
    outcomes = {}
    for label in ('corrected_explicit_R_type_groups', 'producer_explicit_R_type_groups_for_discrepancy_audit'):
        outcomes[label] = {}
        for group, g in qc[label].items():
            eid = g['first_EID']
            rid = int(group.split('|')[0][1:])
            c = checks[freeze['targets'].index(eid)]
            outcomes[label][group] = {'selected_EID': eid, 'status': 'checked-no-discrepancy' if label.startswith('corrected') or c['R'][rid-1].startswith('relevant:') else 'checked-corrected', 'actual_judgment': c['R'][rid-1], 'finding': FINDINGS[eid]}
    counts = dict(Counter(c['decision'] for c in checks))
    dump('qc_results.json', {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'qc_freeze_sha256': sha(HERE / 'qc_freeze.json'),
        'primary_checked': 25, 'secondary_original_item_checked': 25, 'unreviewed_targets': [],
        'results': [{'E_ID': c['id'], 'status': 'checked-no-discrepancy against corrected primary overlay', 'disposition': c['decision'], 'finding': FINDINGS[c['id']]} for c in checks],
        'group_outcomes': outcomes,
        'producer_X3_checked': ['E-0519'], 'producer_X3_retained': ['E-0519'], 'invalid_X3_caught': [],
        'secondary_changes_to_Sol_overlay': [],
        'review_limit': 'Actual original exported snippet/metadata recheck by same Sol AI, not independent human or passage-level claim QC'
    })
    dump('counts.json', {
        'unit': 'metadata occurrences, not works or full-text inclusions',
        'targets': 25, 'actual_primary_checks': 25, 'actual_secondary_checks': 25, 'unreviewed_in_target25': [],
        'Luna': dict(Counter(p['stage1_disposition'] for p in producer)), 'Sol': counts,
        'disposition_changed_EIDs': disposition_changed, 'R_status_changed_EIDs': mapping_changed,
        'all_25_have_new_itemwise_bounded_rationale': True,
        'baseline': {'ADVANCE': 94, 'X3': 44, 'PENDING': 700},
        'baseline_delta_ONLY': {'ADVANCE': counts['ADVANCE'], 'X3': counts['X3'], 'PENDING': -counts['ADVANCE']-counts['X3']},
        'other_Scholar_not_reviewed_by_this_pass': 513,
        'exact_2026_cutoff_date_pending': [o['occurrence_E_ID'] for o in overlay if o['publication_year'] == '2026'],
        'year_missing': [o['occurrence_E_ID'] for o in overlay if not o['publication_year']],
        'all_25_exact_date_version_language_identity_type_verification': 'PENDING',
        'support_and_confidence': 'UNASSESSED', 'fulltext_and_citation_pass': 'NOT RUN',
        'producer_preservation_hashes_checked': True, 'original_fields_preserved_in_overlay': True,
        'no_concurrent_output_read_or_merge': True
    })
    print(json.dumps({'counts': counts, 'disposition_changed': disposition_changed, 'R_status_changed_count': len(mapping_changed), 'producer_group_samples_corrected': sum(v['status'] == 'checked-corrected' for v in outcomes['producer_explicit_R_type_groups_for_discrepancy_audit'].values())}))

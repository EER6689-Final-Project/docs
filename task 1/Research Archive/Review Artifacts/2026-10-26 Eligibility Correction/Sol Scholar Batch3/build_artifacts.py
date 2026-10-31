"""Serialize hand-authored decisions; no keyword screening or range-tag parsing."""
from pathlib import Path
import csv
import datetime
import hashlib
import json
from collections import Counter, defaultdict

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
QUEUE = BASE / '2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = HERE.parent / 'Scholar Batch 3/overlay.csv'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')

def write_csv(name, rows):
    with (HERE / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

# Individual exclusion checks deliberately address the six actual questions.
EXCLUSIONS = {
    'E-0617': [
        'Silk stress-strain is a mechanical material outcome, not a browser timing/memory/interaction construct.',
        'Biomechanics/ecology text supplies no capture API or observation-induced execution mechanism.',
        'Natural/synthetic silk materials and representative curves do not describe synthetic computer workloads or user populations.',
        'A representative stress-strain curve supplies no repeated-estimator, dependence or uncertainty procedure.',
        'Material strength comparisons do not establish paired reference-tool agreement.',
        'Silk architecture/ecology is not profiler prior work or a specified transferable fixture/allocation design.',
    ],
    'E-0624': [
        'Spider foraging/web mechanics under humidity is not browser metric scope or units.',
        'Temperature/humidity effects on silk are not a described instrumentation capture or observer-effect method.',
        'Geographic limits on spider-web constructs provide no synthetic-page/user sampling procedure.',
        'The generalization warning supplies no repeated-run hierarchy, variance estimator or stopping method.',
        'No paired measurement-method comparison or reference-tool conformance is described.',
        'Climate/foraging modeling offers no exact transferable experimental allocation or browser solution overlap.',
    ],
    'E-0636': [
        'This occurrence concerns dragline-silk stress-strain, not a browser measurement construct.',
        'No execution capture/perturbation mechanism appears in this biomechanics snippet.',
        'Synthetic materials here are silk comparators, not simulated page/user workloads.',
        'Representative stress-strain curves are not a described repetition-uncertainty method.',
        'No matched measurement tools, pairing or agreement procedure is supplied.',
        'Ecology/behavior integration does not specify a transferable fixture/control design or browser profiler prior work.',
    ],
    'E-0646': [
        'Mention of Web Performance WG specifications does not define their metrics or implementation semantics.',
        'Organizational-interest analysis supplies no browser capture or profiling perturbation mechanism.',
        'Shuffled organization data is not a web workload/user fidelity evaluation.',
        'Independent organization shuffling tests correlations, not uncertainty of repeated performance measurements.',
        'Organization correlations are not matched-method agreement or reference conformance.',
        'W3C governance topics do not specify a browser evaluation corpus, fixture design or profiler solution; shuffling alone does not supply that bridge.',
    ],
    'E-0665': [
        'Turbine temperature prediction reliability is not browser metric semantics.',
        'No instrumentation capture or measurement-induced perturbation is described.',
        'No synthetic-versus-field workload or sampling coverage mechanism is supplied.',
        'Neural prediction uncertainty is described, but no repeated-measure estimator/hierarchy or concrete calibration procedure bridges it to performance runs.',
        'Benchmarking neural predictions supplies no matched measurement-method agreement design.',
        'The excerpt supplies no general fixture, allocation, corpus or closest browser solution design beyond turbine prediction benchmarking.',
    ],
    'E-0682': [
        'River width/cross-sectional area and discharge are physical hydraulic constructs, not browser metrics.',
        'Altimetry algorithm evaluation supplies no transferable capture or observer-overhead mechanism here.',
        'Dry-season river measurement is a physical-condition requirement, not synthetic page/user population coverage.',
        'Repeated area observations estimate a hydraulic minimum; no general repeated-performance uncertainty estimator is supplied, and width uncertainty is expressly omitted.',
        'Discharge-algorithm benchmarking is not demonstrated matched measurement agreement, pairing or tolerances.',
        'The supplied dry-season parameter requirement supplies no exact transferable control/allocation or fixture design; river benchmark alone is insufficient.',
    ],
    'E-0686': [
        'Weighted Maxcut objective and quantum-state outcomes do not define browser metric constructs.',
        'Quantum amplification readout supplies no browser capture/observer-effect analogue with a stated bridge.',
        'Extrapolation beyond a simulated range is not a supplied web/user workload coverage procedure.',
        'Four quantum-state measurements are not a described performance-run estimator, independence model or uncertainty method.',
        'Heuristic results and extrapolation uncertainty do not describe matched reference-method agreement.',
        'No transferable allocation, benchmark corpus/control procedure or closest browser solution is given beyond this quantum heuristic.',
    ],
    'E-0697': [
        'ROC AUC versus signal-strength uncertainty is classifier discrimination, not a proposed browser metric definition.',
        'No profiling capture, missingness or observation-perturbation mechanism is supplied.',
        'Realistically weighted particle training is not synthetic browser workload/user transfer, and no general sampling-fidelity procedure is described.',
        'Signal-strength prediction uncertainty/ranking supplies no repeated-run measurement estimator or dependence handling.',
        'Correlation between AUC and uncertainty rankings is not measurement agreement or reference conformance.',
        'The architecture benchmark offers no exact transferable fixture/allocation/corpus design here; performance-rank correlation alone is not a design bridge.',
    ],
}

def build_primary():
    if (HERE / 'secondary_QA_freeze.json').exists():
        raise RuntimeError('Primary artifacts already frozen; do not overwrite review history')
    freeze = json.loads((HERE / 'input_freeze.json').read_text())
    for path, expected in freeze['inputs'].items():
        assert sha(Path(path)) == expected, path
    targets = freeze['targets']
    source = {r['occurrence_E_ID']: r for r in csv.DictReader(QUEUE.open()) if r['occurrence_E_ID'] in targets}
    producer = {r['occurrence_E_ID']: r for r in csv.DictReader(PRODUCER.open())}
    authored = list(csv.DictReader((HERE / 'author_checks.psv').open(), delimiter='|'))
    assert [a['eid'] for a in authored] == targets
    negative = {
        'R1': 'No explicit browser metric definition/scope, units or construct-equivalence contribution is supplied by this excerpt.',
        'R2': 'No capture-boundary, missing-event or observer-induced overhead mechanism is supplied; measurement alone is not an R2 mapping.',
        'R3': 'No workload/user population fidelity or selection-coverage mechanism is supplied; non-browser benchmarking alone is not an R3 mapping.',
        'R4': 'No procedure for repeated-performance uncertainty, dependence or precision is supplied; experiments/reproducibility alone are not R4.',
        'R5': 'No matched measurement-reference conformance/agreement procedure is supplied; comparison, validation or correlation alone is not R5.',
        'R6': 'No specific fixture/corpus/allocation design or closest browser-profiler solution is established beyond the separately tagged candidate questions.',
    }
    rows = []
    checks = []
    for event, a in zip(freeze['corrective_events'], authored):
        eid = a['eid']; raw = source[eid]; old = producer[eid]
        tags = a['tags'].split(';') if a['tags'] else []
        assert all(t in negative for t in tags)
        assert (not tags) == (eid in EXCLUSIONS)
        decision = 'EXCLUDE' if eid in EXCLUSIONS else 'ADVANCE'
        six = {}
        for i, rq in enumerate(negative):
            if eid in EXCLUSIONS:
                six[rq] = EXCLUSIONS[eid][i]
            elif rq in tags:
                six[rq] = 'CANDIDATE only: ' + a['phenomenon_and_reason'] + ' Boundary: ' + a['bounded_transfer']
            else:
                six[rq] = 'Not mapped on supplied text about ' + raw['title'] + '. ' + negative[rq]
        check = dict(occurrence_E_ID=eid, corrective_event_ID=event,
                     original_title=raw['title'], original_snippet=raw['abstract_or_snippet'],
                     original_raw_metadata=raw['raw_record_metadata'],
                     read_boundary='Full supplied title + Scholar snippet (NOT abstract) + original metadata; no full text',
                     producer_disposition=old['stage1_disposition_reviewed'],
                     producer_reason=old['itemwise_reason'],
                     candidate_R_tags=tags, source_type_proxy=a['type_proxy'],
                     source_type_status='UNVERIFIED; proxy for grouping only, not X4 adjudication',
                     six_question_checks=six, reason=a['phenomenon_and_reason'],
                     transfer=a['bounded_transfer'], primary_disposition=decision,
                     independent_scientific_review=False)
        checks.append(check)
        row = dict(raw)
        row.update(corrective_event_ID=event, target_occurrence_E_ID=eid,
                   predecessor_event_ID='E-' + str(3000 + targets.index(eid)),
                   producer_disposition=old['stage1_disposition_reviewed'],
                   producer_reason=old['itemwise_reason'],
                   stage1_decision=decision, stage1_primary_code='X3' if decision == 'EXCLUDE' else '',
                   stage1_reason=a['phenomenon_and_reason'] + ' ' + a['bounded_transfer'],
                   stage1_disposition_reviewed=decision, primary_code_reviewed='X3' if decision == 'EXCLUDE' else '',
                   candidate_R_tags=a['tags'], bounded_transfer=a['bounded_transfer'],
                   source_type_proxy=a['type_proxy'], source_type_fit='UNVERIFIED',
                   semantic_eligibility='OUTSIDE-R1-R6 at title/snippet stage' if decision == 'EXCLUDE' else 'CANDIDATE; full-text eligibility pending',
                   candidate_relevance=a['tags'] or 'Outside all six questions; see explicit itemwise checks',
                   identity_status='DUP-CANDIDATE; UNADJUDICATED; NO MERGE' if raw['duplicate_occurrence'] == 'True' else 'ID-PENDING; UNVERIFIED',
                   canonical_identity_status='UNRESOLVED; no canonical reconciliation authorized',
                   canonical_pending_state='ID-PENDING', canonical_pending_reason='Semantic routing only; edition/author/DOI identity reconciliation not performed',
                   canonical_work_ID='', canonical_SID='', canonical_primary_exclusion_code='',
                   date_eligibility='UNVERIFIED; reported year is not exact cutoff evidence',
                   fulltext_language_translation='UNVERIFIED; no X2 from metadata',
                   stage2='FT-PENDING; NOT RUN', fulltext_pass='NOT RUN', citation_pass='NOT RUN',
                   claim_support='UNASSESSED', methodological_confidence='UNASSESSED',
                   reviewer='Sol AI technical review after Luna; not independent human scientific review',
                   audit_type='Primary itemwise semantic review; secondary self-audit tracked separately',
                   review_date='2026-10-26', secondary_QA='NOT YET RUN', **six)
        rows.append(row)
    write_json('primary_itemwise_checks.json', checks)
    write_csv('overlay.csv', rows)
    groups = defaultdict(list)
    for a in authored:
        for tag in a['tags'].split(';') if a['tags'] else ['OUTSIDE-ALL-SIX']:
            groups[tag + ' / ' + a['type_proxy']].append(a['eid'])
    snapshots = {k: {'members': sorted(v), 'selected': min(v), 'nonselected_count': len(v)-1} for k,v in sorted(groups.items())}
    producer_x = [e for e in targets if producer[e]['stage1_disposition_reviewed'] == 'EXCLUDE']
    sol_x = [e for e in targets if e in EXCLUSIONS]
    selected = {v['selected'] for v in snapshots.values()}
    critical = set(producer_x + sol_x)
    union = [e for e in targets if e in critical | selected]
    write_json('secondary_QA_freeze.json', dict(
        timestamp=datetime.datetime.now().astimezone().isoformat(),
        primary_checks_sha256=sha(HERE/'primary_itemwise_checks.json'),
        authored_sha256=sha(HERE/'author_checks.psv'),
        overlay_primary_sha256=sha(HERE/'overlay.csv'),
        producer_exclusions=producer_x, sol_proposed_exclusions=sol_x,
        groups=snapshots, selection_rule='Lexicographically first explicit E-ID per explicit corrected R/type-proxy group; no range parsing',
        critical_EIDs=[e for e in targets if e in critical], target_EIDs=union,
        status='FROZEN BEFORE SECONDARY ORIGINAL REREAD',
        pattern_expansion_rule='If substantive discrepancy emerges, prospectively freeze finite same-pattern list before rereading; otherwise no expansion claimed',
        checks_completed=False))
    print(json.dumps({'primary_counts':dict(Counter(r['stage1_decision'] for r in rows)), 'producer_exclusions':len(producer_x),'sol_exclusions':len(sol_x),'groups':len(groups),'secondary_frozen_count':len(union),'secondary_targets':union},indent=2))

if __name__ == '__main__':
    build_primary()

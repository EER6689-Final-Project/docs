"""Reproduce receipt joins/counts, NOT semantic decisions. Decisions are in Sol_item_checks.tsv.

Writes only to this authorized artifact subtree; producer observations are read-only.
"""
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE.parent / '2026-10-26 Discovery/REVIEWQUEUE.csv'
EXPECTED = '92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path, delimiter=','):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))


def write_csv(name, data):
    assert data
    with (BASE / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(data[0]))
        writer.writeheader()
        writer.writerows(data)


def write_json(name, value):
    (BASE / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def status_of(row, folder):
    if folder == 'OA2':
        return row['new_semantic_disposition'].upper()
    return {'exclude': 'X3', 'advance': 'ADVANCE', 'pending': 'PENDING'}[row['stage1_disposition'].lower()]


def build():
    assert sha(SOURCE) == EXPECTED
    frozen = json.loads((BASE / 'Sol_frozen_QA_manifest.json').read_text())
    for name, expected in frozen['producer_hashes'].items():
        assert sha(BASE / name) == expected, name
    copies = []
    for folder, scratch in [('OA2', '/tmp/opencode/eei6689-screen-oa2'), ('Scholar', '/tmp/opencode/eei6689-screen-scholar')]:
        for destination in sorted((BASE / folder).iterdir()):
            if not destination.is_file():
                continue
            source = Path(scratch) / destination.name
            # Later reproducibility must not depend on scratch surviving a restart.
            source_present = source.is_file()
            if source_present:
                assert sha(source) == sha(destination), destination
            copies.append(dict(source_path=str(source), durable_path=str(destination.relative_to(BASE)), durable_sha256=sha(destination), bytes=destination.stat().st_size, source_exists_at_check=source_present, current_source_byte_equality='PASS' if source_present else 'scratch unavailable; durable frozen hash independently checked above'))
    assert len(copies) == 9
    write_json('Sol_preservation_receipt.json', dict(files=copies, actual_files=9, fabricated_files=0, OA1='Already durable; frozen hash checked, never overwritten', scratch_independence='Durable producer files remain usable if external scratch is lost.'))
    original = read_csv(SOURCE)
    assert len(original) == 838
    assert [r['occurrence_E_ID'] for r in original] == [f'E-{n:04}' for n in range(200, 1038)]
    oa = [r for r in original if r['source_platform'] == 'OpenAlex']
    assert len(oa) == 300 and oa == original[:300]
    checks = read_csv(BASE / 'Sol_item_checks.tsv', '\t')
    assert len(checks) == len({r['EID'] for r in checks}) == 195
    checked = {r['EID']: r for r in checks}
    targets = {r['EID'] for r in frozen['targets']}
    assert len(targets) == 173 and targets <= checked.keys()
    samples = {g['selected'] for g in frozen['groups']}
    assert len(samples) == 22 and samples <= checked.keys()
    assert checked.keys() == targets | samples
    producer = {}
    for folder in ['OA1', 'OA2']:
        for row in read_csv(BASE / folder / 'overlay.csv'):
            eid = row['target_occurrence_EID']
            assert eid not in producer
            producer[eid] = (folder, row, status_of(row, folder))
    assert set(producer) == {r['occurrence_E_ID'] for r in oa}
    assert Counter(v[2] for v in producer.values()) == Counter(ADVANCE=104, X3=173, PENDING=23)
    events = []
    for index, row in enumerate(oa):
        eid = row['occurrence_E_ID']
        folder, previous, old_status = producer[eid]
        check = checked.get(eid)
        metadata = json.loads(row['raw_record_metadata'])
        if folder == 'OA1':
            assert all(previous[k] == v for k, v in row.items()), eid
        else:
            assert previous['platform_record_ID'] == row['platform_record_id']
            assert previous['original_URL'] == row['record_url']
        status = check['status'] if check else 'PENDING'
        rationale = check['rationale'] if check else 'Bounded title/date/language/type/abstract-availability and producer-map inspection only. Original exported abstract NOT rechecked by Sol; producer relevance/transfer mapping remains unvalidated after extraction-pattern discrepancies. Hold pending for finite expanded QA, not an exclusion or proof of irrelevance.'
        assert status in ['ADVANCE', 'PENDING', 'X3']
        assert check is None or len(rationale) > 100
        events.append(dict(
            corrective_event_EID=f'E-{2000 + index:04}',
            target_occurrence_EID=eid,
            input_row_1based=index + 1,
            input_sha256=EXPECTED,
            producer_folder=folder,
            producer_event_EID=previous['new_review_event_EID'],
            producer_status=old_status,
            original_provisional_status=row['stage1_decision'],
            original_canonical_pending_state=row['canonical_pending_state'],
            history_link=f'{folder}/overlay.csv#target_occurrence_EID={eid}; new_review_event_EID={previous["new_review_event_EID"]}',
            title=row['title'],
            platform_record_id=row['platform_record_id'],
            record_url=row['record_url'],
            doi=row['doi'],
            publication_date_metadata=row['publication_date'],
            language_metadata=row['language'],
            source_type_metadata=metadata.get('type', ''),
            abstract_status=row['abstract_status'],
            exported_abstract_chars=len(row['abstract_or_snippet']),
            effective_stage1_status=status,
            effective_primary_code='X3' if status == 'X3' else '',
            stage1_RIDs=check['RIDs'] if check else '',
            stage1_rationale=rationale,
            actual_QA_coverage='original title + entire supplied abstract/status + date/language/type/venue metadata read; source-specific rationale' if check else 'title/bounded metadata inspected ONLY; original exported text semantic recheck NOT DONE',
            technical_QA_status=('checked-no-disposition-change' if status == old_status else 'checked-corrected') if check else 'UNREVIEWED-SEMANTIC-QA; administrative hold pending',
            frozen_target_X3='yes' if eid in targets else 'no',
            frozen_group_sample='yes' if eid in samples else 'no',
            checker='Sol AI after Luna AI; metadata eligibility technical QA, NOT independent human review',
            review_date='2026-10-26',
            protocol='ERP-2026-10-25-v1.0; correction of semantic overclaim, NOT amendment',
            QA_freeze_sha256=sha(BASE / 'Sol_frozen_QA_manifest.json'),
            canonical_identity='PENDING; no work/alias adjudication, S-ID allocation or merge',
            date_eligibility='PENDING original date/version verification; export metadata only, no X1 assigned',
            fulltext_language_translation='PENDING; metadata language not full-text/translation evidence, no X2',
            source_type_fit='PENDING original/version verification; export type is provisional, no X4',
            fulltext_review='NOT RUN; exported text only, not a publisher full-text verification',
            citation_pass='NOT RUN',
            claim_support='UNASSESSED',
            methodological_confidence='UNASSESSED',
            source_claim_QC='UNASSESSED; not passage-level QC',
            independent_human_review='NOT DONE',
            gates='B-010/G3/G4 remain OPEN; no gate edits or closure',
        ))
    write_csv('Sol_OA_corrective_events.csv', events)
    write_csv('Sol_X3_adjudications.csv', [e for e in events if e['frozen_target_X3'] == 'yes'])
    write_csv('Sol_OA_unvalidated_semantic_QA.csv', [e for e in events if e['target_occurrence_EID'] not in checked])
    by_eid = {e['target_occurrence_EID']: e for e in events}
    effective = []
    for row in original:
        event = by_eid.get(row['occurrence_E_ID'])
        result = dict(row)
        # Original fields stay byte-value-identical; effective_* are explicit, separate occurrence states.
        result.update(dict(
            effective_stage1_status=event['effective_stage1_status'] if event else 'PENDING',
            effective_primary_code=event['effective_primary_code'] if event else '',
            effective_RIDs=event['stage1_RIDs'] if event else '',
            effective_rationale=event['stage1_rationale'] if event else 'Scholar semantic mapping FAILED/not completed; 538 pending. Producer metadata/snippet reading does not establish eligibility. Prospective freeze missed; exclusion/group QC not performed.',
            effective_corrective_event_EID=event['corrective_event_EID'] if event else '',
            effective_history_link=event['history_link'] if event else f'Scholar/overlay.csv#target_occurrence_EID={row["occurrence_E_ID"]}; historical producer receipt only, NOT applied as semantic adjudication',
            effective_QA_coverage=event['actual_QA_coverage'] if event else 'NO Sol semantic review; snippet not abstract; Scholar failed itemwise semantic RQ mapping',
            effective_identity_status='ID-PENDING',
            effective_source_date_language_type='PENDING original-source/version/full-text checks',
            effective_fulltext='NOT RUN',
            effective_citations='NOT RUN',
            effective_claim_support='UNASSESSED',
            effective_methodological_confidence='UNASSESSED',
            effective_independent_human_review='NOT DONE',
            effective_gate_effect='NONE; B-010/G3/G4 OPEN',
        ))
        assert all(result[k] == v for k, v in row.items())
        effective.append(result)
    write_csv('Sol_effective_state_838.csv', effective)
    group_results = []
    for group in frozen['groups']:
        check = checked[group['selected']]
        retained_mapping = group['RID'] in check['RIDs'].split(';')
        group_results.append(dict(**group, source_check='CHECKED original exported text; AI metadata technical QA', group_result='checked-no-mapping-discrepancy' if retained_mapping else 'checked-corrected; producer selected-source RID not substantiated/removed from confirmed stage1 mapping', evidence_rationale=check['rationale'], retained_selected_RIDs=check['RIDs'], correction_expansion='Sol_expansion_freeze.json: all 300 OA targets; NOT all semantically rechecked', limitation='provisional occurrence/source-type screen only; no SIDs/CIDs, no claim QC, no independent human reviewer'))
    write_json('Sol_frozen_group_QA_results.json', dict(frozen_manifest_sha256=sha(BASE / 'Sol_frozen_QA_manifest.json'), frozen_groups=35, distinct_selected_sources=22, actual_original_export_checks=22, group_results=group_results, final_regroup_QC='NOT DONE; changed mappings/newly retained rows mean these 35 producer-snapshot checks are not final group coverage or ERP section 9 claim QC.'))
    # Freeze, but do not claim to execute, the new first-EID grouping after corrections.
    groups = defaultdict(list)
    for event in events:
        if event['effective_stage1_status'] == 'X3':
            continue
        for rid in event['stage1_RIDs'].split(';'):
            if re.fullmatch(r'R[1-6]', rid):
                groups[(rid, event['source_type_metadata'])].append(event['target_occurrence_EID'])
    final_groups = [dict(RID=k[0], metadata_type=k[1], members=v, selected=v[0], nonselected_count=len(v)-1, status='PLANNED ONLY; no post-correction group recheck claimed') for k, v in sorted(groups.items())]
    write_json('Sol_final_group_snapshot_PLANNED.json', dict(created_utc=datetime.now(timezone.utc).isoformat(), selection='First occurrence EID per nonempty final mapped R/type group; no RIDs invented for unresolved rows', groups=final_groups, unresolved_unmapped_rows=[e['target_occurrence_EID'] for e in events if e['effective_stage1_status'] != 'X3' and not e['stage1_RIDs']], final_QC='OPEN; snapshot for next separate pass, not retrospective success'))
    counts = dict(
        immutable_input_sha256=EXPECTED,
        original_occurrences=838,
        tentative_producer_OA=dict(Counter(v[2] for v in producer.values())),
        X3_targets=173,
        X3_original_export_rechecked=173,
        X3_targets_unchecked=[],
        X3_adjudications=dict(Counter(checked[e]['status'] for e in targets)),
        X3_dispositions_rejected=129,
        additional_frozen_sample_original_export_checks=22,
        full_original_export_QA_rows=195,
        bounded_metadata_only_rows=105,
        bounded_metadata_only_EIDs=[e['target_occurrence_EID'] for e in events if e['target_occurrence_EID'] not in checked],
        after_QA_OA=dict(Counter(e['effective_stage1_status'] for e in events)),
        after_QA_OA_by_producer={name: dict(Counter(e['effective_stage1_status'] for e in events if e['producer_folder'] == name)) for name in ['OA1', 'OA2']},
        checked_unchanged_disposition=sum(e['technical_QA_status'] == 'checked-no-disposition-change' for e in events),
        checked_changed_disposition=sum(e['technical_QA_status'] == 'checked-corrected' for e in events),
        unchecked_semantic_QA_pending=105,
        transition_matrix={f'{old} -> {new}': sum(e['producer_status'] == old and e['effective_stage1_status'] == new for e in events) for old in ['ADVANCE', 'X3', 'PENDING'] for new in ['ADVANCE', 'X3', 'PENDING']},
        Scholar_occurrences=538,
        Scholar_semantic_review='FAILED/not completed; all pending; freeze missed; no exclusion or group QC',
        after_QA_all838=dict(Counter(r['effective_stage1_status'] for r in effective)),
        source_works='UNKNOWN; occurrence counts only; no SIDs/identity merges',
        support_confidence='UNASSESSED for all rows',
        metadata_group_QA=dict(planned_groups=35, selected_sources=22, selected_sources_original_export_checked=22, corrected_group_mappings=sum('checked-corrected' in r['group_result'] for r in group_results), final_group_snapshot_count=len(final_groups), final_group_QC='NOT RUN'),
        receipt_hashes_rechecked='PASS for all frozen OA1/OA2/Scholar receipts',
        input_hash_rechecked='PASS',
        original_fields_preserved='PASS for every field in all 838 effective rows',
        allocated_event_IDs='E-2000..E-2299 exactly, original OA input order; producer events not reused',
        library_shared_trackers_staging_commits='NOT TOUCHED',
        B010_G3_G4='OPEN; metadata eligibility does not close identity/citation/full-text blockers',
    )
    assert counts['after_QA_OA'] == dict(X3=44, ADVANCE=94, PENDING=162)
    assert counts['after_QA_all838'] == dict(X3=44, ADVANCE=94, PENDING=700)
    write_json('Sol_QA_counts.json', counts)
    assert sha(SOURCE) == EXPECTED
    print(json.dumps(counts, indent=2))


def inventory():
    entries = []
    for path in sorted(BASE.rglob('*')):
        if not path.is_file() or path.name == 'Sol_file_manifest.json':
            continue
        record = dict(path=str(path.relative_to(BASE)), sha256=sha(path), bytes=path.stat().st_size)
        if path.suffix in ['.csv', '.tsv']:
            record.update(data_rows=len(read_csv(path, '\t' if path.suffix == '.tsv' else ',')), row_count_basis='CSV data records excluding header')
        elif path.suffix == '.json':
            value = json.loads(path.read_text())
            record.update(data_rows=len(value) if isinstance(value, list) else 1, row_count_basis='top-level JSON objects; nested cohort counts recorded in content')
        else:
            record.update(data_rows=len(path.read_text().splitlines()), row_count_basis='physical text lines, NOT research records')
        entries.append(record)
    write_json('Sol_file_manifest.json', dict(created_utc=datetime.now(timezone.utc).isoformat(), scope='Every actual file in authorized correction subtree except this self-referential manifest; no hashes invented for absent scratch files', manifest_self_hash='Report externally; not self-hashed', file_count=len(entries), files=entries))


if __name__ == '__main__':
    build()
    inventory()

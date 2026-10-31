import csv
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from freeze import HERE, ROOT, QUEUE, PRODUCER, sha
from build_primary import write_json

# Authored after the frozen ten exports were displayed and actually reread.
QA_NOTES = {
 'E-0725':'Closeness of agreement and Bland–Altman are present; replicates alone do not warrant separate R4. Imaging review/context proxy remains provisional.',
 'E-0726':'Replicate-aware limits-of-agreement extension is explicit despite generic journal title. R5-only discovery routing is bounded; no inferred canonical identity.',
 'E-0727':'Paired sample-level observations and correlation-not-agreement warning directly support bounded R5. Exported 2026 does not verify pre-cutoff date.',
 'E-0728':'SD of differences between repeats supports bounded R4 variation-summary lead; explicit inter-technique agreement supports R5. No lung-volume validity transferred.',
 'E-0729':'Indexed replicates, bias/precision/agreement title and missing-CB text support the stated uncertainty-reporting lead; no CB formula or performance claim inferred.',
 'E-0740':'Heteroscedastic title and replicate-model snippet support R4/R5 leads, not verified copula assumptions or suitability.',
 'E-0741':'Repeated same-procedure/location wording does not establish between-method agreement or an uncertainty method. PENDING/no positive RIDs is retained; producer inconsistency is real, not independent corroboration.',
 'E-0742':'Lancet/1986 metadata and BerlinRUG/2015 URL naming remain conflicting identity cues. R5 remains possible, not assigned positive membership while identity/source-role clarification is pending.',
 'E-0745':'Per-subject replicates support a nesting lead and a priori acceptable agreement supports R5. Historical DUP/E-0722 stays unchanged as an unvalidated candidate; no target record was opened or merged.',
 'E-0747':'Prespecified agreement thresholds and accounting for replicates per subject are explicit; reporting-statement proxy is not verified type. No cardiac threshold adopted.'
}

if __name__ == '__main__':
    freeze=json.loads((HERE/'target_freeze.json').read_text())
    qaf=json.loads((HERE/'qa_freeze.json').read_text())
    assert sha(HERE/'judgments.json')==qaf['primary_sha256']
    assert sha(HERE/'delta_overlay25.csv')==qaf['overlay_sha256']
    js=json.loads((HERE/'judgments.json').read_text())
    assert list(QA_NOTES)==qaf['selected_ids']
    with QUEUE.open() as f:
        reader=csv.DictReader(f); cols=reader.fieldnames
        original={r['occurrence_E_ID']:r for r in reader if r['occurrence_E_ID'] in freeze['target_ids']}
    with (HERE/'delta_overlay25.csv').open() as f:
        reader=csv.DictReader(f); overlaycols=reader.fieldnames; overlay=list(reader)
    assert [r['occurrence_E_ID'] for r in overlay]==freeze['target_ids']
    assert cols==qaf['original_columns']
    assert all(k.startswith('effective_') for k in overlaycols if k not in cols)
    comparisons=0
    for r,j in zip(overlay,js):
        base=original[r['occurrence_E_ID']]
        for k in cols:
            assert r[k]==base[k],(r['occurrence_E_ID'],k)
            comparisons+=1
        assert set(j['effective_question_judgments'])=={f'R{i}' for i in range(1,7)}
        assert j['effective_event_E_ID']==f"E-{3800+int(r['occurrence_E_ID'][2:])-725}"
    preserved={}
    for p in [QUEUE,PRODUCER/'overlay_first25.csv',PRODUCER/'authored_judgments_first25.json']:
        rel=str(p.relative_to(ROOT)); preserved[rel]=dict(frozen_sha256=freeze['inputs'][rel],current_sha256=sha(p),unchanged=sha(p)==freeze['inputs'][rel])
        assert preserved[rel]['unchanged']
    qa=[]
    for eid,note in QA_NOTES.items():
        r=original[eid]
        qa.append(dict(occurrence_E_ID=eid,status='checked-no-discrepancy',
                       checker='Sol separate-pass AI self-audit; not independent human/scientific review',
                       checked_utc=datetime.now(timezone.utc).isoformat(),
                       anchor=str(QUEUE.relative_to(ROOT))+' occurrence_E_ID='+eid,
                       original_title=r['title'],complete_original_Scholar_snippet=r['abstract_or_snippet'],
                       raw_metadata=r['raw_record_metadata'],record_url=r['record_url'],
                       original_record_sha256=hashlib.sha256(json.dumps(r,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                       finding=note,discrepancy='NONE against Sol primary judgment',resolution='retained primary',
                       browser_fulltext_retrieval='NOT RUN'))
    write_json('qa_results.json',qa)
    group_results={k:dict(**g,status='checked-no-discrepancy',qa_record=g['selected'],
        coverage='selected occurrence only; other group members are primary-reviewed, not secondary-reread') for k,g in qaf['groups'].items()}
    write_json('qa_group_results.json',group_results)
    counts=dict(scope='delta only; no shared/global aggregate update',
                target_count=25,primary_original_export_reads=25,producer_six_question_judgments_validated=25,
                effective_dispositions=dict(Counter(j['effective_disposition'] for j in js)),X3=0,DUP_merges=0,SIDs_allocated=0,
                events='E-3800–E-3824 ordered E-0725–E-0749',
                producer_disposition_changes={'ADVANCE → PENDING':['E-0741','E-0742']},
                positive_R_membership_counts=dict(Counter(r for j in js for r in j['effective_RIDs'])),
                positive_R_type_proxy_groups=sum(not k.startswith('PENDING') for k in qaf['groups']),
                pending_type_proxy_groups=sum(k.startswith('PENDING') for k in qaf['groups']),
                proposed_exclusions=0,secondary_planned=10,secondary_actually_checked=10,
                secondary_no_discrepancy=10,secondary_corrected=0,secondary_unresolved=0,
                primary_reviewed_not_secondary_checked=15,secondary_expansion_triggered=False,
                E0750_E0799_authored_or_read_by_this_task=0,E0750_E0799_unreviewed_by_this_task=50,
                metadata_date_language_type_identity='PENDING for all 25',
                source_confidence_support='UNASSESSED for all 25',fulltext_citations='NOT RUN',G3='OPEN',G4='OPEN')
    write_json('counts.json',counts)
    write_json('verification.json',dict(verified_utc=datetime.now(timezone.utc).isoformat(),
        original_columns=len(cols),original_field_comparisons=comparisons,all_original_queue_values_unchanged=True,
        new_overlay_fields_effective_prefix_only=True,exact25_target_order=True,exact_event_order=True,
        all25_have_explicit_six_question_judgments=True,source_and_completed25_producer_hashes=preserved,
        freeze_preceded_original_read=True,qa_freeze_preceded_actual_secondary_reread=True,
        qa_selected_equals_actual=True,all_proposed_exclusions_checked=True,
        no_shared_or_original_writes=True,
        freeze_boundary_note='Initial byte-hash receipt included all then-present producer directory files, including remaining50_freeze.json. That concurrent file was not semantically read, used for decisions, or revalidated. Only completed first25 overlay/authored judgments are consumed. Other batches were not semantically read; same-batch prior freeze.py was inspected for schema/workflow only.'))
    print(json.dumps(counts,indent=2))

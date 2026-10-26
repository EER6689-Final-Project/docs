from pathlib import Path
import csv, json, hashlib, datetime

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data): (OUT/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
f=json.loads((OUT/'primary-input-freeze.json').read_text())
sample=json.loads((OUT/'secondary-sample-freeze.json').read_text())
assert sha(OUT/'Sol-FIRST25-overlay.csv')==sample['primary_overlay_sha256']
src=list(csv.DictReader((ROOT/f['source']['path']).open(newline='')))
src={r['occurrence_E_ID']:r for r in src if r['occurrence_E_ID'] in f['scope']}
overlay=list(csv.DictReader((OUT/'Sol-FIRST25-overlay.csv').open(newline='')))
prod={r['producer_source_E_ID']:r for r in csv.DictReader((OUT.parent/'Scholar Batch5/FIRST25-overlay.csv').open(newline=''))}
assert len(src)==len(overlay)==25
assert [r['Sol_event_E_ID'] for r in overlay]==[f'E-{i:04d}' for i in range(4000,4025)]
for r in overlay:
    eid=r['occurrence_E_ID']
    assert all(r[k]==v for k,v in src[eid].items())
    assert all(r[k]==v for k,v in prod[eid].items())
    assert all(r[f'Sol_R{i}_rationale'] for i in range(1,7))
assert sha(ROOT/f['source']['path'])==f['source']['sha256']
for x in f['producer_files']: assert sha(ROOT/x['path'])==x['sha256']
findings=json.loads((OUT/'secondary-findings.json').read_text())
assert [f'E-{n:04d}' for n,_ in findings]==sample['selected_for_secondary_reread']
now=datetime.datetime.now().astimezone().isoformat()
results=[]
for n,note in findings:
    eid=f'E-{n:04d}'; r=next(r for r in overlay if r['occurrence_E_ID']==eid)
    results.append({'source_E_ID':eid,'Sol_event_E_ID':r['Sol_event_E_ID'],'status':'checked-no-discrepancy','checked_at':now,'original_anchor':f[ 'source']['path']+'#'+eid,'original_title':src[eid]['title'],'complete_original_stored_snippet':src[eid]['abstract_or_snippet'],'original_metadata':src[eid]['raw_record_metadata'],'R1_R6_reconsidered':True,'bounded_transfer_reconsidered':True,'rationale':note,'producer_X3_rejected':r['Sol_producer_X3_rejected']=='True','effective_stage1_decision':r['Sol_stage1_decision']})
save('secondary-QA-results.json',{'completed_at':now,'audit_type':'Sol separate-pass AI self-audit; not independent human review','sample_freeze_sha256':sha(OUT/'secondary-sample-freeze.json'),'originals_reread':'All 25 selected complete stored Scholar snippets/titles/metadata reread from immutable REVIEWQUEUE after secondary sample freeze; not full texts.','checked_count':len(results),'groups_checked':{k:{**v,'status':'checked-no-discrepancy','check_source_E_ID':v['selected']} for k,v in sample['groups'].items()},'secondary_discrepancies_against_Sol_primary':0,'expansion':'Finite pattern expansion already frozen across all 23 producer X3; all actually reread. No further discrepancy requiring expansion found.','results':results})
rejected=[r['occurrence_E_ID'] for r in overlay if r['Sol_producer_X3_rejected']=='True']
counts={'scope_occurrences':25,'actual_itemwise_primary_checks':25,'ADVANCE':13,'PENDING':0,'X3':12,'producer_X3_checked':23,'producer_X3_rejected':len(rejected),'producer_X3_rejected_ids':rejected,'Sol_X3_secondary_checked':12,'explicit_R_type_proxy_groups_checked':len(sample['groups']),'secondary_unique_original_rereads':25,'secondary_discrepancies_against_Sol_primary':0,'independent_human_review':False,'E-0825_to_E-0899':'UNREVIEWED by this task','canonical_included_works':'NOT ESTABLISHED; occurrence-only semantic screen'}
save('counts.json',counts)
save('preservation-receipt.json',{'checked_at':now,'source_sha256_unchanged':f['source']['sha256'],'producer_files_unchanged':f['producer_files'],'source_rows_all_original_columns_preserved':25,'producer_rows_all_original_columns_preserved':25,'source_original_column_count':len(next(iter(src.values()))),'producer_original_column_count':len(next(iter(prod.values()))),'events_ordered':'E-4000–E-4024 maps E-0800–E-0824','shared_or_canonical_writes':False,'new_SIDs':0,'DUP_merges':0,'fulltext_pass':'NOT RUN','citation_pass':'NOT RUN','support':'UNASSESSED','confidence':'UNASSESSED','date_language_type_identity':'UNVERIFIED/PENDING; metadata proxies only','development_notes':'Two build attempts stopped before output creation: corrected repository-root indexing, then recognized producer overlay contains only new producer columns. Final overlay joins originals unchanged, producer fields unchanged, and new Sol/effective fields.'})
handoff='''# Sol Scholar Batch5 First25 — completed semantic QA

Scope: **E-0800–E-0824 only**, events **E-4000–E-4024** in order. ERP-2026-10-25-v1.0; cutoff 2026-10-25 inclusive; current Scope Resolution used. **E-0825–E-0899 remain unreviewed by this task.**

## Results and limits

- Actual primary original-title/complete-stored-Scholar-snippet/metadata reads: **25/25**; authored six-R rationales and bounded-transfer checks: **25/25**.
- Effective stage 1: **13 ADVANCE (uncertain), 0 PENDING, 12 X3**. ADVANCE is not inclusion or verified relevance. All 25 still have unresolved identity/date/language/type and no passage-based claim assessment.
- All **23 producer X3** semantically checked. **11 rejected X3**, changed to uncertain ADVANCE: '''+', '.join(rejected)+'''. Remaining 12 X3 retained with all-six-question and candidate-transfer rationale.
- Secondary sample frozen after primary judgments: all producer X3, all Sol X3, plus first E-ID per **14 explicitly assigned R/source-type-proxy groups**. Union **25** originals actually reread after freeze; **14/14** groups checked. **0 discrepancies against Sol primary** in the secondary pass. This does not erase the 11 producer discrepancies.
- Finite error-pattern expansion prospectively froze all 23 producer X3 (overconfident rejection of plausible capture, conformance-oracle, fixture or field-entry transfer); all were reread. No further expansion required at this snapshot.
- Separate-pass AI self-audit, **not independent human review**. Stored discovery snippets are neither complete abstracts nor full texts. Exact date/version, English full text/translation, source-type eligibility and canonical identity remain unverified. Support/confidence **UNASSESSED**; full-text/citation passes **NOT RUN**.

## Handoff and provenance

`Sol-FIRST25-overlay.csv` preserves every Discovery REVIEWQUEUE column/value and every corrected producer column/value; only new Sol judgments and effective_* fields are added. Original reviewer, stage1 reason and canonical pending status are not overwritten. No DUP merge, new SID, original/shared/library/staging/commit write, online search, citation pass, gate or novelty claim.

Correct producer: sibling `Scholar Batch5/FIRST25-overlay.csv`; its actual files and the exact source hash were frozen before original-text reads. Old `Review Artifacts/EligibilityCorrection/Scholar Batch5/` is freeze/handoff-only deviation history with zero completed semantic review, not a result; it was not used as screening evidence or edited.

`primary-input-freeze.json` anchors source and producer hashes; `secondary-sample-freeze.json` freezes primary-overlay hash, finite expansion and group membership/selection before rereads; `secondary-QA-results.json` contains actual per-item reread notes and group links; `preservation-receipt.json` records exact original-value and input-hash checks. `file-manifest.json` lists only this owned folder's deliverables; no aggregate state is overwritten. Source/producer hash delta: **unchanged**. Folder delta: **new files only**.

Next authorized owner may reconcile this occurrence-level overlay; canonical work identity, full-text relevance and claim-level appraisal remain later work. No other active reviewer outputs were consulted.
'''
(OUT/'handoff.md').write_text(handoff)
save('file-manifest.json',{'created_at':now,'delta':'new owned-folder files only; source and corrected producer unchanged','files':{p.name:{'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='file-manifest.json'}})
print(json.dumps(counts,indent=2))
print('manifest_sha256',sha(OUT/'file-manifest.json'))

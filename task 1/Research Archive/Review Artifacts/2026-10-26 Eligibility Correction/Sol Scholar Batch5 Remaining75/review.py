from pathlib import Path
import csv, json, hashlib, datetime, sys

HERE = Path(__file__).resolve().parent
ROOT = Path('/home/mendydias/Projects/eei6689')
BASE = HERE.parent
SOURCE = ROOT / 'task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
PRODUCER = BASE / 'Scholar Batch5'
IDS = [f'E-{i:04}' for i in range(825, 900)]
def digest(p):
    return {'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
def save(name, obj):
    (HERE/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n')
def freeze():
    assert not (HERE/'primary-freeze.json').exists()
    save('primary-freeze.json', {'time':datetime.datetime.now().astimezone().isoformat(), 'protocol':'ERP-2026-10-25-v1.0', 'cutoff':'2026-10-25', 'target_ids':IDS, 'Sol_ids':[f'E-{i}' for i in range(4025,4100)], 'producer_ids':[f'E-{i}' for i in range(3925,4000)], 'source':digest(SOURCE), 'producer_files':[digest(PRODUCER/n) for n in ['remaining75-overlay.csv','remaining75-handoff.md','remaining75-manifest.json']], 'original_content_read_before_freeze':False, 'accepted_snapshot':'5; unchanged until parent combines validated disjoint deltas'})
def loadcsv(p, delimiter=','):
    with p.open(newline='') as f:
        rd=csv.DictReader(f, delimiter=delimiter)
        fields=rd.fieldnames
        rows=list(rd)
    assert all(None not in r and all(v is not None for v in r.values()) for r in rows), str(p)
    return fields, rows
NEG = {
 1:'This description does not specify a browser metric definition, units, aggregation or absent-versus-zero semantics; a performance subject label is not a positive R1 mapping.',
 2:'No additional capture channel, observable-event contract or observation-induced execution change is described here; a tool name or interface alone is not an R2 mechanism.',
 3:'No additional synthetic-to-observed workload linkage, user sampling frame, state/vantage coverage or representativeness method is specified here; merely having users is not validation.',
 4:'No repeated performance-run hierarchy, dependence, drift, variance, interval or stopping method is specified here; experimental or statistical terminology alone is not R4.',
 5:'No paired same-construct measurements, reference error, agreement limits, tolerance or metric-conformance procedure is specified here; comparison or other-domain conformance is not R5.',
 6:'No browser-profiler solution, performance fixture/corpus construction or exact transferable experimental-design mechanism beyond the separately mapped questions is established here; unrelated application architecture is not closest work.'
}
def build():
    frozen=json.loads((HERE/'primary-freeze.json').read_text())
    assert digest(SOURCE)==frozen['source']
    assert [digest(PRODUCER/Path(x['path']).name) for x in frozen['producer_files']]==frozen['producer_files']
    sf, sr=loadcsv(SOURCE); sr={r['occurrence_E_ID']:r for r in sr if r['occurrence_E_ID'] in IDS}
    pf, pr=loadcsv(PRODUCER/'remaining75-overlay.csv'); assert [r['producer_source_E_ID'] for r in pr]==IDS
    pr={r['producer_source_E_ID']:r for r in pr}
    _, cr=loadcsv(HERE/'authored-producer-X3.tsv', '\t')
    cr={f"E-{int(r['number']):04}":r for r in cr}
    assert set(cr)=={k for k,v in pr.items() if v['producer_stage1_decision']=='X3'}
    _, ar=loadcsv(HERE/'authored-primary.tsv', '\t')
    assert [int(r['number']) for r in ar]==list(range(825,825+len(ar)))
    out=[]; checks=[]
    for a in ar:
        n=int(a['number']); eid=f'E-{n:04}'; s=sr[eid]; p=pr[eid]
        positives={int(x[1:x.index('=')]):x[x.index('=')+1:] for x in a['positive_maps'].split('|') if x}
        e={'effective_E_ID':f'E-{n+3200}', 'effective_source_E_ID':eid, 'effective_producer_E_ID':p['producer_E_ID'], 'effective_stage1_decision':a['decision'], 'effective_stage1_code':'X3' if a['decision']=='X3' else ('RELEVANCE-PENDING' if a['decision']=='PENDING' else 'advance/uncertain'), 'effective_stage1_rationale':a['case_basis']+' '+a['transfer_limit'], 'effective_positive_R_map':';'.join('R'+str(i) for i in positives), 'effective_type_proxy':a['type_proxy'], 'effective_transfer_boundary':a['transfer_limit']}
        changed=[]
        for i in range(1,7):
            e[f'effective_R{i}_judgment']='POSITIVE_CANDIDATE' if i in positives else ('NO_MAPPING_SHOWN' if a['decision']=='X3' else 'UNRESOLVED_NOT_POSITIVE')
            e[f'effective_R{i}_rationale']=a['case_basis']+' '+(positives[i]+' '+a['transfer_limit'] if i in positives else NEG[i]+' '+a['transfer_limit'])
            if eid in cr:
                e[f'effective_R{i}_rationale']=cr[eid][f'R{i}']+' '+a['transfer_limit']
            pp=p[f'producer_R{i}_judgment']!='no plausible relevance shown'
            if pp!=(i in positives): changed.append('R'+str(i))
        e.update({'effective_date_check':'PENDING: metadata year '+(s['publication_year'] or 'missing')+'; exact publication/version date not cleared against 2026-10-25', 'effective_language_check':'PENDING: English snippet does not clear full-text language/authorized translation', 'effective_source_type_check':'PENDING: '+a['type_proxy']+' is a stored-metadata proxy only, not source-type eligibility', 'effective_identity_check':'PENDING: no canonical crosswalk, SID allocation, DUP disposition or merge', 'effective_claim_support':'UNASSESSED', 'effective_methodological_confidence':'UNASSESSED', 'effective_fulltext_citation_pass':'NOT RUN', 'effective_review_date':'2026-10-26', 'effective_reviewer':'Sol AI source-content review; not independent human review', 'effective_primary_status':'ACTUALLY_READ_TITLE_COMPLETE_STORED_SNIPPET_METADATA', 'effective_secondary_status':'NOT RUN', 'effective_changed_positive_R_fields':';'.join(changed), 'effective_disposition_changed':str(a['decision']!=p['producer_stage1_decision']).lower()})
        assert not set(sf)&set(pf)
        out.append({**s,**p,**e})
        checks.append({'source_E_ID':eid, 'Sol_E_ID':e['effective_E_ID'], 'producer_E_ID':p['producer_E_ID'], 'original_stored_content':{k:s[k] for k in ['title','abstract_or_snippet','raw_record_metadata','publication_year','publication_date','language','record_url','doi','abstract_status']}, 'source_row_sha256':hashlib.sha256(json.dumps(s,sort_keys=True,ensure_ascii=False).encode()).hexdigest(), 'producer_six_rationale_fields_inspected':True, 'producer_blank_rationale_fields':[f'R{i}' for i in range(1,7) if not p[f'producer_R{i}_rationale'].strip()], 'content_positive_map_corrections':changed, 'producer_decision':p['producer_stage1_decision'], 'Sol_decision':a['decision'], 'six_authored_judgments':{f'R{i}':{'judgment':e[f'effective_R{i}_judgment'],'rationale':e[f'effective_R{i}_rationale']} for i in range(1,7)}, 'case_basis':a['case_basis'], 'transfer_limit':a['transfer_limit']})
    with (HERE/'remaining75-overlay.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    save('author-checks.json',checks)
    counts={x:sum(r['effective_stage1_decision']==x for r in out) for x in ['ADVANCE','PENDING','X3']}
    save(f'primary-progress-{len(ar):02}.json', {'time':datetime.datetime.now().astimezone().isoformat(), 'actually_primary_read':len(ar),'not_yet_reviewed':75-len(ar),'counts':counts,'overlay':digest(HERE/'remaining75-overlay.csv'),'author_checks':digest(HERE/'author-checks.json')})
    print(json.dumps(counts))
def secondary_freeze():
    assert not (HERE/'secondary-freeze.json').exists()
    _, rows=loadcsv(HERE/'remaining75-overlay.csv')
    assert [r['occurrence_E_ID'] for r in rows]==IDS
    groups={}
    for r in rows:
        for rq in r['effective_positive_R_map'].split(';'):
            if rq:
                groups.setdefault(rq+' / '+r['effective_type_proxy'],[]).append(r['effective_E_ID'])
    group_records={k:{'members':sorted(v),'selected_first':min(v),'nonselected_count':len(v)-1} for k,v in sorted(groups.items())}
    producer_x3=[r['occurrence_E_ID'] for r in rows if r['producer_stage1_decision']=='X3']
    sol_x3=[r['occurrence_E_ID'] for r in rows if r['effective_stage1_decision']=='X3']
    base=set(producer_x3+sol_x3+[rows[int(g['selected_first'][2:])-4025]['occurrence_E_ID'] for g in group_records.values()])
    save('secondary-freeze.json',{'time':datetime.datetime.now().astimezone().isoformat(),'status':'FROZEN BEFORE SECONDARY ORIGINAL-EXPORT REREAD','source':digest(SOURCE),'producer_files':json.loads((HERE/'primary-freeze.json').read_text())['producer_files'],'primary_overlay':digest(HERE/'remaining75-overlay.csv'),'primary_author_checks':digest(HERE/'author-checks.json'),'producer_all_proposed_exclusions':producer_x3,'Sol_all_proposed_exclusions':sol_x3,'corrected_positive_R_type_proxy_groups':group_records,'base_selected_source_ids':sorted(base),'finite_pattern_expansion':{'reason':'Primary found occurrence-dependent X3 (E-0846), inconsistent intrinsic-profiler treatment (E-0843), broad performance labels promoted to R1 and tool comparison promoted to R5. Six rationale-field repairs do not settle semantic validity. Shared producer extraction patterns occur across the entire assigned 75, so freeze expansion to all 75 before rereading.','expanded_source_ids':[x for x in IDS if x not in base],'bounded_to':IDS},'selected_source_ids':IDS,'selected_count':75,'secondary_actually_read_at_freeze':0,'review_type':'Sol AI separate-pass source-content audit; not independent human review','network_fulltext_citations':'NOT RUN'})
    print('Frozen 75 secondary rereads; base selected',len(base),'groups',len(groups))
def finalize():
    frozen=json.loads((HERE/'primary-freeze.json').read_text())
    sample=json.loads((HERE/'secondary-freeze.json').read_text())
    assert digest(SOURCE)==frozen['source']==sample['source']
    assert [digest(PRODUCER/Path(x['path']).name) for x in frozen['producer_files']]==frozen['producer_files']
    assert digest(HERE/'remaining75-overlay.csv')==sample['primary_overlay'], 'Run finalize only once on frozen primary overlay'
    fields, rows=loadcsv(HERE/'remaining75-overlay.csv')
    _, secondary=loadcsv(HERE/'authored-secondary.tsv','\t')
    assert [f"E-{int(r['number']):04}" for r in secondary]==sample['selected_source_ids']==IDS
    old_by_id={r['occurrence_E_ID']:dict(r) for r in rows}
    primary_by_id={r['source_E_ID']:r for r in json.loads((HERE/'author-checks.json').read_text())}
    corrections={
        'E-0836':(2, 'The exact snippet only says that the profiler uses intrinsic mechanisms of the, with its object truncated. No actual intrinsic capture mechanism or runtime behavior is stated; remove the positive R2 map. Retain ADVANCE uncertain to inspect the mechanism; the browser is only an upload interface.'),
        'E-0843':(2, 'This occurrence also ends at intrinsic mechanisms of the, without naming the mechanism or its object. Remove the inferred runtime-intrinsic R2 positive; retain ADVANCE uncertain for inspection, not an X3 or duplicate disposition.'),
        'E-0898':(3, 'The complete stored snippet ends at client-, not a stated client condition or transfer/sampling mechanism. Remove positive R3; retain R6 as a candidate assessment-model solution lead. Do not infer the truncated word or factors.')
    }
    results=[]
    for row,note in zip(rows,secondary):
        eid=row['occurrence_E_ID']; old=old_by_id[eid]
        if eid in corrections:
            i,reason=corrections[eid]
            row[f'effective_R{i}_judgment']='UNRESOLVED_NOT_POSITIVE'
            row[f'effective_R{i}_rationale']=reason
            row['effective_positive_R_map']=';'.join(x for x in row['effective_positive_R_map'].split(';') if x!='R'+str(i))
            row['effective_transfer_boundary']=reason
            row['effective_stage1_rationale']=reason
        row['effective_secondary_status']=note['status']
        row['effective_secondary_finding']=note['finding']
        changed=[]
        for i in range(1,7):
            if (row[f'producer_R{i}_judgment']!='no plausible relevance shown')!=(row[f'effective_R{i}_judgment']=='POSITIVE_CANDIDATE'):
                changed.append('R'+str(i))
        row['effective_changed_positive_R_fields']=';'.join(changed)
        results.append({'source_E_ID':eid,'Sol_E_ID':row['effective_E_ID'],'status':note['status'],'actual_original_stored_export_reread':True,'source_row_sha256':primary_by_id[eid]['source_row_sha256'],'six_R_and_transfer_checked':True,'finding':note['finding'],'old_positive_map':old['effective_positive_R_map'],'new_positive_map':row['effective_positive_R_map'],'disposition':row['effective_stage1_decision'],'review_type':'Sol AI separate-pass source-content audit, not independent human review'})
    fields+=['effective_secondary_finding']
    with (HERE/'remaining75-overlay.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(rows)
    save('secondary-results.json',{'freeze_sha256':digest(HERE/'secondary-freeze.json')['sha256'],'actually_reread':75,'checked_no_discrepancy':72,'checked_corrected':3,'unresolved_secondary_discrepancies':0,'records':results,'limits':'Not independent human review; no full text or network. Corrected mapping does not imply final eligibility or claim support.'})
    sf,sr=loadcsv(SOURCE);src={r['occurrence_E_ID']:r for r in sr if r['occurrence_E_ID'] in IDS}
    pf,pr=loadcsv(PRODUCER/'remaining75-overlay.csv');pro={r['producer_source_E_ID']:r for r in pr}
    source_faults=[(r['occurrence_E_ID'],k) for r in rows for k in sf if r[k]!=src[r['occurrence_E_ID']][k]]
    producer_faults=[(r['occurrence_E_ID'],k) for r in rows for k in pf if r[k]!=pro[r['occurrence_E_ID']][k]]
    blanks=[(r['occurrence_E_ID'],f'R{i}') for r in rows for i in range(1,7) if not r[f'producer_R{i}_rationale'].strip()]
    assert not source_faults and not producer_faults and not blanks
    assert [r['effective_E_ID'] for r in rows]==[f'E-{i}' for i in range(4025,4100)]
    assert [r['producer_E_ID'] for r in rows]==[f'E-{i}' for i in range(3925,4000)]
    assert all(k in sf+pf or k.startswith('effective_') for k in fields)
    assert all(r[f'effective_R{i}_rationale'].strip() for r in rows for i in range(1,7))
    assert all(r['effective_claim_support']==r['effective_methodological_confidence']=='UNASSESSED' and r['effective_fulltext_citation_pass']=='NOT RUN' for r in rows)
    corrected_groups={}
    for r in rows:
        for rq in r['effective_positive_R_map'].split(';'):
            if rq:corrected_groups.setdefault(rq+' / '+r['effective_type_proxy'],[]).append(r['effective_E_ID'])
    save('final-group-coverage.json',{'note':'Post-QC descriptive coverage, not a retrospective replacement for the prospective secondary freeze. All final groups are covered by already-frozen all75 selection.','groups':{k:{'members':sorted(v),'first':min(v),'first_actually_checked':True} for k,v in sorted(corrected_groups.items())}})
    rejected=[r['occurrence_E_ID'] for r in rows if r['producer_stage1_decision']=='X3' and r['effective_stage1_decision']!='X3']
    mapping_rows=[r['occurrence_E_ID'] for r in rows if r['effective_changed_positive_R_fields']]
    counts={'scope':'E-0825–E-0899 only; delta, not canonical snapshot','primary_actual_read':75,'secondary_actual_reread':75,'unreviewed':0,'producer_counts':{d:sum(r['producer_stage1_decision']==d for r in rows) for d in ['ADVANCE','PENDING','X3']},'Sol_counts':{d:sum(r['effective_stage1_decision']==d for r in rows) for d in ['ADVANCE','PENDING','X3']},'producer_X3_critical_checked':27,'producer_X3_rejected_count':len(rejected),'producer_X3_rejected_ids':rejected,'producer_ADVANCE_to_PENDING':[r['occurrence_E_ID'] for r in rows if r['producer_stage1_decision']=='ADVANCE' and r['effective_stage1_decision']=='PENDING'],'producer_positive_mapping_changed_records':len(mapping_rows),'producer_positive_mapping_changed_record_ids':mapping_rows,'producer_positive_mapping_changed_cells':sum(len(r['effective_changed_positive_R_fields'].split(';')) for r in rows if r['effective_changed_positive_R_fields']),'final_positive_counts':{f'R{i}':sum(r[f'effective_R{i}_judgment']=='POSITIVE_CANDIDATE' for r in rows) for i in range(1,7)},'secondary_selected':75,'secondary_base_selected':len(sample['base_selected_source_ids']),'secondary_groups_frozen':len(sample['corrected_positive_R_type_proxy_groups']),'secondary_expansion':len(sample['finite_pattern_expansion']['expanded_source_ids']),'secondary_checked_no_discrepancy':72,'secondary_checked_corrected':3,'current_producer_missing_six_rationale_cells':len(blanks),'current_producer_schema_shape_faults':0,'source_value_preservation_faults':len(source_faults),'producer_value_preservation_faults':len(producer_faults),'new_non_effective_columns':0,'claim_support':'UNASSESSED','methodological_confidence':'UNASSESSED','fulltext_citations':'NOT RUN','date_language_type_identity_clearance':'PENDING all75','accepted_snapshot':'5 remains current pending parent integration'}
    save('QC-counts.json',counts)
    save('preservation-receipt.json',{'time':datetime.datetime.now().astimezone().isoformat(),'source_before':frozen['source'],'source_after':digest(SOURCE),'assigned_producer_files_before':frozen['producer_files'],'assigned_producer_files_after':[digest(PRODUCER/Path(x['path']).name) for x in frozen['producer_files']],'source_columns_preserved':sf,'source_original_values_checked':len(sf)*75,'producer_columns_preserved':pf,'producer_original_values_checked':len(pf)*75,'source_value_mismatches':source_faults,'producer_value_mismatches':producer_faults,'new_columns_effective_prefix_only':True,'other_jobs_first25_shared_files':'Not written by this job; not claimed hash-validated because not assigned frozen inputs','scope_and_id_order_validated':True})
    handoff=f'''# Sol Scholar Batch5 Remaining75 — delta-only handoff

Protocol: ERP-2026-10-25-v1.0; cutoff 2026-10-25 inclusive; Scope Resolution read. Only E-0825–E-0899; producer E-3925–E-3999 preserved in target order; Sol E-4025–E-4099. Current accepted state remains Snapshot 5 until parent integrates disjoint validated deltas.

## Actual review and results

- Actually read all 75 original stored titles, complete Scholar snippets and metadata; authored six R judgments per record, not copied producer dispositions. Full text/network/citations NOT RUN; no eligibility, identity, DUP or S-ID clearance.
- Producer: 48 ADVANCE / 0 PENDING / 27 X3. Sol: **53 ADVANCE / 3 PENDING / 19 X3**. Unreviewed: 0. These are occurrence-level stage-1 dispositions, not unique/included works or claim support.
- All 27 producer X3 received six case-specific mechanism/transfer checks in `authored-producer-X3.tsv`. Rejected **8**: {', '.join(rejected)}. Six advance for bounded capture/usage analogues; E-0833/E-0840 remain pending for a named statistical method in the official manual. E-0846's earlier-advanced-occurrence rationale is not an irrelevance or duplicate ruling; E-0843's mechanism lead cannot receive contradictory treatment solely by occurrence.
- E-0891 changes ADVANCE to PENDING: customer/marketing performance versus technical runtime remains unresolved, with no explicit positive map.
- Changed producer positive-map presence in {len(mapping_rows)} records / {counts['producer_positive_mapping_changed_cells']} cells. R1 cannot follow from a broad performance label; R5 cannot follow from juxtaposing tools (E-0899). No positive R4 or R5 is supported at this stored-snippet stage. All positive maps are candidate relevance, not verified evidence.

## Prospective secondary audit and corrections

After primary work, `secondary-freeze.json` froze every producer/Sol exclusion, first Sol E-ID in each of 34 corrected-positive-R/type-proxy groups (48 base records), and a finite shared-pattern expansion of 27 additional assigned records. All **75** selected stored originals were then actually reread: **72 checked-no-discrepancy / 3 checked-corrected**. Removed my own R2 positives for E-0836/E-0843 (truncated intrinsic-mechanism description does not name a runtime capture mechanism) and R3 for E-0898 (truncated `client-` does not state client conditions/transfer). Dispositions did not change. The original primary author checks remain history; final effective fields and secondary results control this delta. Final group coverage is descriptive, not a retrospective sample freeze. AI separate-pass audit is **not independent human review**.

## Content/schema checks and limits

Inspected all 75 producer six-judgment/six-rationale fields against source content. Current missing rationale cells: **0**; current CSV shape faults: **0**. The producer reports six records repaired after its QC; nonempty repaired fields were not treated as semantic validation. Source-content faults include unsupported broad R1 mappings, E-0899 comparison-only R5, occurrence-dependent E-0846 X3, and inconsistent truncated-profiler handling. Counts/list details are in `QC-counts.json` and per-record evidence in `author-checks.json` / `secondary-results.json`.

All {len(sf)} original source columns and {len(pf)} producer columns/values are preserved unchanged; only new `effective_*` fields are added. No Batch3 history-column reuse. Every final effective judgment has a rationale. Date/version, full-text language/authorized translation, type eligibility and canonical identity remain PENDING for all 75. Claim support and methodological confidence remain UNASSESSED; full-text citation pass NOT RUN. No source PDFs, library, first25, shared/root trackers, other jobs, stage or commit writes. No broad searches, gates, method selection or novelty findings.

## Hash receipts

- Original REVIEWQUEUE SHA-256: `{digest(SOURCE)['sha256']}`.
- Frozen producer overlay SHA-256: `{frozen['producer_files'][0]['sha256']}`.
- Frozen producer handoff SHA-256: `{frozen['producer_files'][1]['sha256']}`.
- Frozen producer manifest SHA-256: `{frozen['producer_files'][2]['sha256']}`.
- Final overlay SHA-256: `{digest(HERE/'remaining75-overlay.csv')['sha256']}`.
- `preservation-receipt.json` verifies before/after input hashes and every joined source/producer value; `remaining75-manifest.json` hashes every owned deliverable except itself (no recursive self-hash).
'''
    (HERE/'remaining75-handoff.md').write_text(handoff)
    save('secondary-progress-75.json',{'actually_reread':75,'checked_no_discrepancy':72,'checked_corrected':3,'author_notes':digest(HERE/'authored-secondary.tsv')})
    save('remaining75-manifest.json',{'created':datetime.datetime.now().astimezone().isoformat(),'scope_ids':IDS,'Sol_ids':[r['effective_E_ID'] for r in rows],'producer_ids':[r['producer_E_ID'] for r in rows],'delta_only':True,'accepted_snapshot_unchanged':'5','counts':counts,'files':{p.name:digest(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='remaining75-manifest.json'}})
    print(json.dumps(counts,indent=2))
if __name__ == '__main__':
    {'freeze':freeze,'build':build,'secondary-freeze':secondary_freeze,'finalize':finalize}[sys.argv[1] if len(sys.argv)>1 else 'freeze']()

from pathlib import Path
import csv, json, hashlib, datetime

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
freeze=json.loads((OUT/'primary-input-freeze.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(ROOT/freeze['source']['path']) == freeze['source']['sha256']
for x in freeze['producer_files']: assert sha(ROOT/x['path']) == x['sha256']
source=list(csv.DictReader((ROOT/freeze['source']['path']).open(newline='')))
source=[r for r in source if r['occurrence_E_ID'] in freeze['scope']]
producer=list(csv.DictReader((OUT.parent/'Scholar Batch5/FIRST25-overlay.csv').open(newline='')))
assert len(source)==len(producer)==25
judgments=json.loads((OUT/'judgments.json').read_text())
rows=[]
for i,(s,p,j) in enumerate(zip(source,producer,judgments)):
    n,decision,typ,rs,reason,*rest=j
    rationales,transfer=rest[:6],rest[6]
    assert len(rest)==7 and s['occurrence_E_ID']==f'E-{n:04d}'==p['producer_source_E_ID']
    assert not set(p)&set(s)
    row={**s,**p}
    fields={'Sol_event_E_ID':f'E-{4000+i:04d}', 'Sol_source_E_ID':s['occurrence_E_ID'], 'Sol_reviewer':'Sol (AI semantic QA; not independent human review)', 'Sol_review_date':'2026-10-26','Sol_stage1_decision':decision,'Sol_stage1_code':'X3' if decision=='X3' else 'advance/uncertain','Sol_stage1_rationale':reason,'Sol_explicit_R_groups':rs,'Sol_source_type_proxy':typ,'Sol_bounded_transfer_check':transfer,'Sol_producer_X3_rejected':str(p['producer_stage1_decision']=='X3' and decision!='X3'),'effective_stage1_decision':decision,'effective_stage1_primary_code':'X3' if decision=='X3' else 'advance/uncertain','effective_stage1_reason':reason,'effective_semantic_eligibility':'OUTSIDE-ALL-SIX; snippet-bounded X3' if decision=='X3' else 'POSSIBLE; full-text relevance unresolved','effective_date_eligibility':'UNVERIFIED; exact date/version through 2026-10-25 not checked','effective_fulltext_language_translation':'UNVERIFIED','effective_source_type_fit':'UNVERIFIED; proxy only','effective_identity_status':'ID-PENDING; no canonical crosswalk, DUP or new SID','effective_fulltext_pass':'NOT RUN','effective_citation_pass':'NOT RUN','effective_claim_support':'UNASSESSED','effective_methodological_confidence':'UNASSESSED'}
    for r,rat in enumerate(rationales,1):
        fields[f'Sol_R{r}_judgment']='POSSIBLE; advance/uncertain' if f'R{r}' in rs.split(',') else 'NO ESTABLISHED LINK in stored text; see rationale'
        fields[f'Sol_R{r}_rationale']=rat
    assert not set(fields)&set(row)
    row.update(fields); rows.append(row)
with (OUT/'Sol-FIRST25-overlay.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
groups={}
for r in rows:
    for q in r['Sol_explicit_R_groups'].split(','):
        if q!='none': groups.setdefault(q+'|'+r['Sol_source_type_proxy'],[]).append(r['occurrence_E_ID'])
groups={k:{'members':v,'selected':min(v),'nonselected_count':len(v)-1} for k,v in sorted(groups.items())}
px=[r['occurrence_E_ID'] for r in rows if r['producer_stage1_decision']=='X3']
sx=[r['occurrence_E_ID'] for r in rows if r['Sol_stage1_decision']=='X3']
selected=sorted(set(px+sx+[g['selected'] for g in groups.values()]))
manifest={'frozen_at':datetime.datetime.now().astimezone().isoformat(),'phase':'after primary judgments, before secondary reread','primary_overlay_sha256':sha(OUT/'Sol-FIRST25-overlay.csv'),'authored_judgments_sha256':sha(OUT/'judgments.json'),'producer_X3':px,'Sol_proposed_X3':sx,'groups':groups,'group_rule':'First lexicographic source E-ID for each explicitly assigned corrected R/source-type-proxy group; no automatic all-R grouping. Proxies are not verified source types.','selected_for_secondary_reread':selected,'finite_error_pattern_expansion':{'pattern':'Overconfident all-R rejection despite a plausible concrete capture, conformance-oracle, fixture or field-entry transfer hidden by short snippets.','affected_finite_ids':px,'action':'All 23 producer X3 receive six-R and bounded-transfer reread, regardless of corrected disposition.'},'secondary_status':'PLANNED; no reread completion claimed by freeze','audit_type':'separate-pass AI self-audit; no independent human review'}
(OUT/'secondary-sample-freeze.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'primary_rows':len(rows),'ADVANCE':sum(r['Sol_stage1_decision']=='ADVANCE' for r in rows),'X3':len(sx),'rejected_producer_X3':[r['occurrence_E_ID'] for r in rows if r['Sol_producer_X3_rejected']=='True'],'groups':groups,'secondary_selected':selected},indent=2))

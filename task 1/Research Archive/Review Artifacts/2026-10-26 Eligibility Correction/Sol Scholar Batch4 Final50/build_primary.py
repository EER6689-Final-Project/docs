import csv,json,datetime,hashlib
from pathlib import Path
from freeze import OUT,ROOT,QUEUE,PROD,sha
def dump(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def positive(s): return s.startswith(('YES','ADVANCE'))
f=json.loads((OUT/'target_freeze.json').read_text())
assert all(sha(ROOT/p)==h for p,h in f['inputs'].items())
with QUEUE.open() as h:
    reader=csv.DictReader(h); original_columns=reader.fieldnames; original={r['occurrence_E_ID']:r for r in reader}
targets=[original[e] for e in f['targets']]
authors=list(csv.DictReader((OUT/'author_checks.psv').open(),delimiter='|'))
assert [r['eid'] for r in authors]==f['targets']
producer={r['occurrence_E_ID']:r for r in csv.DictReader((PROD/'overlay_remaining50.csv').open())}
judgments=[];overlay=[];checks=[]
for i,(r,a) in enumerate(zip(targets,authors)):
    eid=r['occurrence_E_ID'];p=producer[eid]
    preserved={k:p.get('producer_'+k)==r[k] for k in original_columns}
    changes=[q for q in ['R1','R2','R3','R4','R5','R6'] if positive(p[q])!=positive(a[q])]
    j={'occurrence_E_ID':eid,'six_question_judgments':{q:a[q] for q in ['R1','R2','R3','R4','R5','R6']},'decision':a['decision'],'routing_reason':a['routing_reason'],'type_proxy':a['type_proxy'],'producer_mapping_changes':changes,'producer_decision':p['new_decision'],'producer_original_field_mismatches':[k for k,v in preserved.items() if not v]}
    judgments.append(j)
    e={**r,'effective_event_E_ID':f['events'][i],'effective_stage1_decision':a['decision'],'effective_primary_code':'X3' if a['decision']=='X3' else ('ID-PENDING' if a['decision']=='PENDING' else ''),'effective_stage1_reason':a['routing_reason'],**{'effective_'+q:a[q] for q in ['R1','R2','R3','R4','R5','R6']},'effective_source_type_proxy':a['type_proxy']+'; selection proxy only, UNVERIFIED','effective_date_eligibility':'PENDING; exact date/version and inclusive 2026-10-25 cutoff unverified','effective_language':'PENDING; full-text language/authorized translation unverified','effective_source_type':'UNASSESSED; metadata proxy not source-type adjudication','effective_identity':'ID-PENDING; no DUP adjudication, merge or inherited eligibility','effective_claim_support':'UNASSESSED','effective_methodological_confidence':'UNASSESSED','effective_fulltext_pass':'NOT RUN','effective_citation_pass':'NOT RUN','effective_reviewer':'Sol separate-pass AI self-audit; not independent scientific review','effective_protocol':'ERP-2026-10-25-v1.0','effective_review_date':'2026-10-26'}
    overlay.append(e)
    checks.append({'occurrence_E_ID':eid,'original_title_entire_stored_snippet_metadata_read':'YES','original_row_sha256':hashlib.sha256(json.dumps(r,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),'producer_original_columns_match':all(preserved.values()),'positive_mapping_changes':','.join(changes),'decision_changed':a['decision']!=p['new_decision'],'routing_reason':a['routing_reason']})
with (OUT/'delta_overlay50.csv').open('w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=list(overlay[0]));w.writeheader();w.writerows(overlay)
with (OUT/'item_checks.tsv').open('w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=list(checks[0]),delimiter='\t');w.writeheader();w.writerows(checks)
dump('primary_judgments.json',judgments)
dump('primary_read_receipt.json',{'read_boundary':'All 50 original titles, entire stored Scholar snippets and exported metadata displayed in two 25-item original-queue reads after target freeze, before authoring. No full texts or online reads.','target_count':50,'original_columns':original_columns,'targets':f['targets']})
groups={}
for label,data in [('producer',producer.values()),('Sol',authors)]:
    data=list(data)
    for q in ['R1','R2','R3','R4','R5','R6']:
        ids=[r.get('eid',r.get('occurrence_E_ID')) for r in data if positive(r[q])]
        if ids:groups[label+' '+q+' explicit positive (including bounded possible/context)']=sorted(ids)
    if label=='Sol':
        for t in sorted({r['type_proxy'] for r in data}):groups['Sol provisional type proxy '+t]=[r['eid'] for r in data if r['type_proxy']==t]
px=[e for e,p in producer.items() if p['new_decision']=='X3'];sx=[a['eid'] for a in authors if a['decision']=='X3']
selected=sorted(set(px+sx+[ids[0] for ids in groups.values()]))
dump('qa_freeze.json',{'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'after all 50 primary judgments, before secondary original-export rereads','queue_sha256':sha(QUEUE),'primary_hashes':{n:sha(OUT/n) for n in ['author_checks.psv','primary_judgments.json','delta_overlay50.csv','item_checks.tsv']},'assigned_producer_hashes':{p:h for p,h in f['inputs'].items() if 'Scholar Batch4 Remaining75/' in p},'producer_X3':px,'Sol_X3':sx,'explicit_positive_and_provisional_type_groups':groups,'minimum_first_EID_union_all_X3':selected,'finite_pattern_check':{'scope':f['targets'],'reason':'Producer positive R4/design/forecast conflation and R2/server-runtime conflation found in primary pass. Check all 50 original exports for overbroad R1-R6 mappings, citation/acknowledgement snippets promoted to own methods, human-literature scope, identity hold and source-type proxies. Includes every assigned occurrence, not other batches.','selected_for_actual_secondary_reread':f['targets'],'count':50},'producer_history_schema_notes':['Producer retains original queue fields under producer_* aliases rather than exact original names. Sol delta uses original column names/values plus effective_* only; aliases not mistaken for original authority.','Producer secondary freeze selected five originals and no source-type proxies; prospective Sol proxy groups are explicitly unverified, not established types.','Producer shared file_manifest/handoff may have grown across first25/final50 passes; only actual assigned-file hashes are asserted here.'],'status':'PLANNED; no secondary checks credited yet','audit':'Separate-pass AI self-audit, not independent human or canonical passage QC'})
print(json.dumps({'primary':len(judgments),'producer_original_field_mismatches':sum(bool(j['producer_original_field_mismatches']) for j in judgments),'mapping_changed_occurrences':sum(bool(j['producer_mapping_changes']) for j in judgments),'minimum_QA':selected,'expanded_secondary':50},indent=2))

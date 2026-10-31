import csv, json, hashlib, os

ROOT=os.path.dirname(__file__)
QUEUE='task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
RIDS=['R1','R2','R3','R4','R5','R6']
# Positive mappings are deliberately sparse and state the item-specific bridge.
P={
'E-1001':{'R2':'HTTP/2 domain sharding in lossy cellular networks is a browser-adjacent transport intervention; possible evidence about network conditions and performance observation, not profiler overhead.','R3':'The named cellular-network condition bounds transport/workload transfer; no synthetic-versus-user comparison is asserted.'},
'E-1002':{'R3':'Distributed web-cache evaluation and consistency/latency are a bounded network/cache context for workload and delivered-performance transfer; not browser-runtime evidence.'},
'E-1003':{'R1':'Title and snippet explicitly concern website-performance measurement and characterize its practice as ad hoc; a discovery lead for construct/operationalization boundaries only, with browser-metric equivalence unestablished.'},
'E-1004':{'R3':'A study of people navigating destination websites and telepresence is a bounded prior human/task-population context for user-side web observations; it is not a synthetic-agent comparison or browser-timing validation.'},
'E-1006':{'R6':'A study of topics in W3C standards work may inform discovery of standards/closest-work coverage; the snippet does not establish normative metric definitions or a solution.'},
'E-1009':{'R3':'Cross-platform and hardware-architecture web-technology performance is a bounded context for platform/workload generalization; browser identity/version remains unverified.'},
'E-1010':{'R6':'Same work as another occurrence is not merged here; its W3C topic-mapping subject can inform discovery coverage, not normative semantics.'},
'E-1011':{'R2':'HTTP/2 domain sharding in lossy cellular networks is a browser-adjacent transport intervention; possible evidence about network conditions and performance observation, not profiler overhead.','R3':'The named cellular-network condition bounds transport/workload transfer; no synthetic-versus-user comparison is asserted.'},
'E-1014':{'R6':'Web-site experimentation rules directly concern design of online experiments and are a candidate methods lead; snippet alone does not establish browser-performance design details.'},
'E-1015':{'R3':'Distributed web-cache evaluation and consistency/latency are a bounded network/cache context for workload and delivered-performance transfer; not browser-runtime evidence.'},
'E-1016':{'R3':'Cloud QoS workload characterization and prediction is a bounded workload/resource-performance analogue; transfer to browser runs is unvalidated.'},
'E-1017':{'R2':'Title explicitly identifies runtime instrumentation and time-to-first-view measurement; snippet mentions uncertainty/reporting, making it directly relevant to capture and measurement perturbation questions, without assuming its results.'},
'E-1018':{'R3':'Web caching is explicitly linked to end-user latency; rough-set uncertainty is potentially relevant to cache/workload context but is not browser metric validation.'},
'E-1019':{'R3':'Empirical technical/informational accessibility and web-traffic associations may bound site/user population and content heterogeneity; not evidence about synthetic agents or browser timing.'},
'E-1021':{'R6':'Large-scale online controlled experiments are directly relevant to experimental-design precedent; no browser-specific design is presumed.'},
'E-1022':{'R1':'The snippet names session duration and web-performance metrics; useful as a possible construct-boundary contrast between behavioral/analytics measures and browser timing, not validation of either.'},
'E-1023':{'R3':'The title/snippet explicitly link technical web optimization, web performance and user experience; possible workload/site-context lead, with the industrial setting and exact performance construct unresolved.'},
'E-1024':{'R3':'An eye-movement study of older adults with/without mild cognitive impairment during web usability tasks is a bounded human/task-population analogue; not a synthetic-agent comparison.'},
'E-1025':{'R3':'Web-server workload prediction explicitly concerns workload and web-performance metrics; bounded server-side context, not browser execution.'},
'E-1027':{'R3':'Study of deaf users navigating textual websites and reported web-performance measures may inform user/task/population boundaries; not browser instrumentation validation.'},
'E-1033':{'R4':'CPU-load evaluation with statistical comparison and a stated uncertainty-reduction approach is a potentially transferable measurement-method analogue; repeated browser runs or applicability are not established.'},
'E-1037':{'R1':'The title concerns efficiency estimation of information web resources and snippet names request complexity, data volume and hardware as uncertainty factors; possible construct/measurement-boundary evidence, not browser metric equivalence.','R3':'Request complexity, resource-data volume and hardware are explicit workload/context factors; browser/user transfer remains unverified.'}
}
WHY={
'E-1000':'Marketing antecedents/correlates of website performance; snippet does not identify browser timing, instrumentation, synthetic transfer, repeated-measure methods, agreement, or design analogue.',
'E-1001':'',
'E-1002':'',
'E-1003':'',
'E-1004':'',
'E-1005':'Institutional repository visibility/ranking is a web presence construct, not browser performance measurement; no explicit transfer mechanism is stated.',
'E-1006':'',
'E-1007':'Land-use allocation is the titled subject; Pylot appears only in an apparently incidental search snippet fragment and supplies no defensible transfer.',
'E-1008':'Spider-web mechanical performance is a biological construct, not web/browser performance; no transfer rationale is stated.',
'E-1009':'',
'E-1010':'',
'E-1011':'',
'E-1012':'Broad edited/book volume and disconnected snippet fragments do not identify a specific transferable browser-performance method or claim; generic statistical-analysis wording is insufficient.',
'E-1013':'Cognitive-radio energy detection is a distinct communications phenomenon; incidental web-performance wording in the snippet does not state a transferable mechanism.',
'E-1014':'',
'E-1015':'',
'E-1016':'',
'E-1017':'',
'E-1018':'',
'E-1019':'',
'E-1020':'Internet marketing/web analytics and third-party ranking statistics concern business/marketing outcomes; no explicit browser metric, capture or method transfer is stated.',
'E-1021':'',
'E-1022':'',
'E-1023':'',
'E-1024':'',
'E-1025':'',
'E-1026':'Small mammals/foraminifera and Miocene geology are the titled subject; browser-performance phrases are unrelated snippet contamination.',
'E-1027':'',
'E-1028':'Industrial information-systems security indexing is the stated subject; incidental Lighthouse/W3C phrase is insufficient to establish a performance-measurement contribution.',
'E-1029':'Intelligence-reporting systems and data consolidation do not state a browser-performance target or explicit transferable method.',
'E-1030':'SEO/business web-performance evaluation and Search Console are not browser-runtime measures; no explicit transfer to R1–R6 is stated.',
'E-1031':'Warehouse management/demand uncertainty is the stated subject; isolated web-performance wording does not establish a relevant target or transfer.',
'E-1032':'Self-healing web applications concern recovery behavior; snippet mentions statistical correlation but no performance measurement, runtime capture, or transferable repeated-measure/agreement method.',
'E-1033':'',
'E-1034':'Stakeholder perceptions and institutional web rankings concern organizational visibility/performance, not browser metrics; no explicit transfer is stated.',
'E-1035':'Web planning models and fuzzy probability are too broad; snippet gives no specific browser/performance measurement mechanism or defensible transfer.',
'E-1036':'Export marketing and web capabilities concern business outcomes, not browser performance measurement; no explicit transfer is stated.',
'E-1037':''}

with open(QUEUE,encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
by={r['occurrence_E_ID']:r for r in rows}
ids=[f'E-{i}' for i in range(1000,1038)]
assert all(i in by for i in ids)
items=[]
for eid in ids:
 r=by[eid]; pos=P.get(eid,{})
 disposition='ADVANCE' if pos else 'X3'
 checks=[]
 for rid in RIDS:
  if rid in pos: judgement='positive'; reason=pos[rid]
  else: judgement='no_positive_mapping'; reason=f"This occurrence's title/snippet does not establish {rid} relevance or a defensible transfer: {WHY[eid]}"
  checks.append({'question':rid,'judgment':judgement,'reason':reason})
 items.append({'E_ID':eid,'stored_title':r['title'],'stage1':disposition,'primary_code':'advance/uncertain' if pos else 'X3','reason':('Advance as a bounded discovery/context lead only. '+ '; '.join(pos.values()) + ' Full text/identity/version/type/date/language remain unverified.') if pos else WHY[eid], 'R1-R6':checks,'positive_RIDs':list(pos),'source_type_proxy':'unverified; based only on export venue/type strings' if pos else 'not adjudicated; exclusion rests on semantic scope, not type','metadata_review':{'scholar_year_as_exported':r['publication_year'],'exact_date':'unverified/not supplied in Scholar export','language':'unverified/not supplied in Scholar export','version_identity':'unresolved; no merge/SID/DUP adjudication','original_duplicate_annotation_preserved':r['stage1_decision']=='DUP','raw_metadata_read':r['raw_record_metadata'],'full_text':'NOT RUN','claim_support':'UNASSESSED','methodological_confidence':'UNASSESSED'}})
out={'reviewer':'Luna AI; authored technical pass, not independent human review','date':'2026-10-26','protocol':'ERP-2026-10-25-v1.0','cutoff_inclusive':'2026-10-25','original_export_read':'All 38 stored original titles, complete Scholar snippets, metadata, URLs and original duplicate annotations actually read; snippets are not abstracts/full text. No network/full-text retrieval.','items':items}
open(os.path.join(ROOT,'primary_judgments.json'),'w').write(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
fields=['E_ID','stage1','primary_code','reason','positive_RIDs','source_type_proxy','R1-R6']
with open(os.path.join(ROOT,'item_checks.tsv'),'w',encoding='utf-8',newline='') as f:
 f.write('\t'.join(fields)+'\n')
 for x in items:
  vals=[x['E_ID'],x['stage1'],x['primary_code'],x['reason'],','.join(x['positive_RIDs']),x['source_type_proxy'],json.dumps(x['R1-R6'],ensure_ascii=False)]
  f.write('\t'.join(v.replace('\t',' ').replace('\n',' ') for v in vals)+'\n')
print('primary rows',len(items),'advance',sum(x['stage1']=='ADVANCE' for x in items),'X3',sum(x['stage1']=='X3' for x in items),'pending',sum(x['stage1']=='PENDING' for x in items))

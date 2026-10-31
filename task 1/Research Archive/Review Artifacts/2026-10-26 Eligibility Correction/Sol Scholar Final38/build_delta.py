"""Serialize Sol-authored decisions; no semantic inference from keywords or producer labels."""
import csv, json, hashlib, datetime
from pathlib import Path
ROOT = Path(__file__).parent
QUEUE = Path('task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv')
PROD = ROOT.parent / 'Scholar Batch7 Final38'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, obj): (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
# Each six-element tuple is independently authored R1..R6: + retain, ? unresolved lead, - not established.
# Type labels below are export proxies, never verified source types.
DATA = [
(1000,'X3','journal','marketing-construct',
 '-Antecedents in marketing do not operationalize browser timing.|-No capture or observation intervention stated.|-Correlates of business website outcomes do not establish workload/user transfer.|-Significant correlations are not repeat-run uncertainty methods.|-Correlation between antecedents and outcomes is not matched-method agreement.|-No fixture, corpus or browser evaluation design identified.',
 'Marketing antecedent associations are a different outcome construct; neither correlation significance nor uncertainty about associations supplies a transferable performance-measurement method.'),
(1001,'ADVANCE','preprint','network-workload',
 '-No metric definition supplied.|?Performance extension might involve measurement but capture mechanism is unstated.|+Lossy cellular conditions and domain sharding bound network and page-delivery transfer.|-Disagreement about h2 is not a sampling-uncertainty procedure.|-h1 versus h2 compares protocols, not reference conformance.|?Network intervention may inform controlled fixture factors, not established design.',
 'Retain network-condition/workload lead; test page and network equivalence before any browser transfer, and do not infer instrumentation overhead.'),
(1002,'ADVANCE','conference','cache-evaluation',
 '?Worst-case cache consistency is a construct distinct from browser timing; its exact definition is unavailable.|?Evaluation tool may expose cache state, but capture details absent.|+Distributed cache state can change delivered content and latency, bounding replay/live equivalence.|-Worst-case consistency uncertainty is not repeated-run precision.|-Cache consistency is not agreement between matched tools.|+Named caching evaluation tool is a fixture/evaluation-method lead; browser implementation remains unestablished.',
 'Retain cache-evaluation context for state/content equivalence; worst-case consistency must not be relabeled as timing confidence or reference agreement.'),
(1003,'PENDING','journal','marketing-construct',
 '?Website performance measurement is explicit but service-quality setting leaves business versus runtime construct unresolved.|-No capture mechanism.|-No workload or user coverage comparison.|-Ad hoc measurement is not a repeat-run uncertainty method.|-No matched reference procedure.|?Measurement-practice study could inform design only if technical operationalization is present.',
 'Producer R1 advance overstates a potentially marketing-only title: hold for construct clarification; snippet alone does not justify either browser mapping or confident exclusion.'),
(1004,'PENDING','journal','human-navigation',
 '-Telepresence is not a browser timing metric.|-No instrumentation intervention.|?Destination navigation and imagined travel might inform user-task coverage, but no synthetic-to-user performance bridge is supplied.|-No repeated-measure uncertainty design stated.|-No reference agreement.|-No browser fixture or profiler design.',
 'Prior human studies are allowed; this particular navigation/telepresence outcome needs a concrete task-coverage bridge, not automatic R3 relevance from human participation.'),
(1005,'X3','journal','ranking-visibility',
 '-Repository visibility/ranking is not runtime metric semantics.|-No observation mechanism.|-Institutional visibility does not establish browser workload coverage.|-No repeat-performance statistical method.|-Web ranking is not matched-tool agreement.|-No corpus sampling or profiler evaluation method stated.',
 'Institutional repository visibility is the target; ranking recommendations provide no browser-measurement or transferable method mechanism in this export.'),
(1006,'PENDING','conference','standards-topics',
 '?Web Performance WG specifications are mentioned but no normative metric statement supplied.|-No instrumentation capture or perturbation method.|-Topic frequencies are not workload coverage.|-Low-count topic noise is not repeated-performance uncertainty.|-No reference conformance procedure.|?W3C topic mapping is a standards-discovery lead, not yet a closest technical solution or evaluation design.',
 'Retain unresolved standards-discovery context without treating topic analysis as normative semantics or a validated R6 design. Exact 2026 date unverified.'),
(1007,'PENDING','journal','tool-mention',
 '-Land-allocation uncertainty is not browser metric semantics.|?Pylot system-wide testing is explicit; could indicate a web measurement component, but its role is truncated.|-Spatial allocation is not itself web workload coverage.|-Unbounded awareness uncertainty is not repeat-run precision.|-No matched-tool agreement.|?Tool evaluation might be a methods lead if tied to the actual study rather than incidental material.',
 'Reject confident exclusion: Pylot is an explicit testing-tool lead, but its role is unresolved. Do not infer browser validation from the mention or adopt spatial uncertainty as performance statistics.'),
(1008,'X3','journal','physical-measurement',
 '-Spider orb-web mechanics are not browser metric constructs.|-Digitization error lacks a stated observation-perturbation mechanism transferable to execution.|-Prey speed is not a web workload/user distribution.|-Digitization error magnitude alone provides no repeated-measure estimator or dependence method.|-Three biomechanical models are not matched-tool reference agreement.|-No transferable fixture/corpus or execution evaluation procedure specified.',
 'Biological mechanics is not excluded merely for domain: inspected digitization error and model testing, but neither supplies a stated transferable uncertainty/agreement/capture procedure in this snippet.'),
(1009,'ADVANCE','journal','platform-workload',
 '?Web technology speed is named but metric operationalization absent.|-No capture/off-on evaluation.|+Platform and hardware architecture explicitly bound performance generalization.|-No repeat-run estimator supplied.|-Platform comparison is not reference conformance.|?Cross-platform factors could inform a crossed design; no actual randomization established.',
 'Retain hardware/platform transfer context; platform/version and workload matching must be checked before applying any result.'),
(1010,'PENDING','conference','standards-topics',
 '?W3C performance specifications are mentioned without metric definitions.|-No runtime capture method stated.|-Topic counts do not establish workload transfer.|-Feature-count uncertainty is not performance repetition uncertainty.|-No conformance procedure.|?Standards-topic study may locate standards but does not establish closest implementation overlap.',
 'This occurrence remains separate despite matching strings. Standards-discovery potential is unresolved, not proof of normative semantics or R6 technical-design relevance.'),
(1011,'ADVANCE','preprint','network-workload',
 '-No explicit metric semantics.|?Web performance extension is not enough to establish capture changes.|+Cellular packet-loss context and sharding identify a network-condition transfer boundary.|-Protocol disagreement is not repeated-measure uncertainty.|-h1/h2 comparison is not reference-tool agreement.|?Protocol intervention may supply controlled conditions if design details are established.',
 'Retain a separately tracked occurrence for transport/workload relevance; no merge, overhead inference or conformance interpretation.'),
(1012,'PENDING','book','method-volume',
 '-No specific browser metric definition identified.|-No identified runtime capture mechanism.|?Internet/Web performance data-mining application might address workloads, but chapter identity is absent.|?Statistical analysis/KEEL could be methodological context; no estimator is identifiable.|-No method-agreement procedure.|?Broad volume may contain an original method chapter; relevant contribution cannot be located from fragmented snippet.',
 'A broad volume and disconnected fragments warrant a finite chapter/identity clarification, not confident X3 or a blanket source-type exclusion.'),
(1013,'PENDING','journal','detector-noise',
 '-Radio energy is not browser metric semantics.|?Noise-sensitive detector observability could transfer to missing-event detection only if a threshold/noise mechanism is established.|-Radio traffic is not evidence of browser workload coverage.|?Noise uncertainty may be systematic rather than repeated-sample variation; estimator transfer unresolved.|-No matched reference agreement shown.|-No browser fixture or profiler design.',
 'The web-performance phrase appears biographical, but detector noise and signal-correlation assumptions deserve methodological clarification; no radio model is adopted as browser evidence.'),
(1014,'ADVANCE','conference','online-experiment',
 '-No browser metric definition.|-No capture perturbation.|-No stated lab/field population transfer test.|+Tail significance and sample-size reasoning are explicit precision/design leads; independence and estimand must be checked.|-No matched-tool agreement.|+Website experimentation rules are a design-method lead, not automatic browser protocol prescriptions.',
 'Retain statistical-tail and online experiment-design leads. Do not import the quoted thousands rule into nested browser repetitions without population and dependence justification.'),
(1015,'ADVANCE','conference','cache-evaluation',
 '?Consistency metric may clarify a non-timing construct, not browser timing semantics.|?Tool observability details not in snippet.|+Distributed caching affects state and content delivery, bounding live/replay equivalence.|-Worst-case consistency is not repeated-run uncertainty.|-Consistency is not reference-tool agreement.|+Evaluation-tool precedent may inform cache fixture design, subject to scope checks.',
 'Keep occurrence separate. Transfer concerns cache state and evaluation setup, not unverified consistency-to-timing equivalence.'),
(1016,'ADVANCE','conference','workload-model',
 '-No browser metric operationalization.|-No instrumentation intervention.|+Markovian workload characterization identifies time-evolving workload assumptions relevant to coverage and scenario generalization.|?Future-evolution uncertainty is not automatically sampling precision; temporal dependence may be a method lead.|-QoS prediction is not matched-reference agreement.|?Workload model may guide fixture factors if model assumptions fit browser workloads.',
 'Retain temporally structured workload analogue; cloud resource prediction is not browser validation and future prediction error is not a confidence interval on repeated means.'),
(1017,'ADVANCE','conference','runtime-instrumentation',
 '+Settled first-view in 3D tiles versus general page metrics is an explicit operationalization lead.|+AOP runtime instrumentation and time-to-first-view capture directly address observability; perturbation remains untested.|?Cesium/3D tiles bound a workload family, not universal page coverage.|+Uncertainty for means, excluded runs and outliers explicitly concern repeated-reporting decisions.|-No matched reference agreement stated.|+Named instrumentation framework is a closest-evaluation/design lead; independent expected effects remain unchecked.',
 'Broaden producer R2-only mapping to R1/R4/R6. Check settling criterion, run exclusion and uncertainty assumptions; no dates, findings or overhead claims verified.'),
(1018,'ADVANCE','chapter','cache-model',
 '-No browser timing definition supplied.|-No runtime observation mechanism.|+Cache state and end-user latency link workload/state to delivered performance.|-Rough-set uncertainty is not a repeated-run sampling method.|-No reference-tool agreement.|?Rough cache model may inform fixture states, but methodological originality/type unresolved.',
 'Retain cache-state context; rough-set granularity must not be treated as a sampling interval or evidence about measurement perturbation.'),
(1019,'PENDING','journal','marketing-construct',
 '?Technical accessibility may include performance constructs, but operationalization absent.|-No capture mechanism.|?Content/accessibility and traffic might bound site populations only if technical workload selection is actually analyzed.|-Associations do not establish repeat-run uncertainty.|-No reference agreement.|-No stated fixture or profiler design.',
 'Technical accessibility is not automatically browser performance. Hold the business-traffic association for a specific construct/workload bridge rather than inherit producer R3.'),
(1020,'X3','thesis-proxy','marketing-analytics',
 '-Internet-marketing evaluation is not browser metric semantics.|-Third-party traffic data uncertainty is not execution-observer perturbation.|-Alexa/social traffic rankings are not an explicit synthetic-workload coverage method.|-No estimator for repeated performance observations specified.|-Ranking-source uncertainty does not establish matched-metric agreement.|-No fixture or profiler evaluation procedure.',
 'Explicit marketing evaluation and traffic rankings target a different construct. Uncertainty in those ranks alone supplies no transferable sampling, capture or agreement method.'),
(1021,'ADVANCE','conference','online-experiment',
 '-No metric semantics supplied.|-No capture intervention.|?Bing experiments imply a field context but synthetic representativeness is unstated.|?Experiment interactions may create dependence; no repeated-run estimator given.|-Controlled comparison is not reference agreement.|+Explicit interactions between online experiments are a transferable interference/design issue; browser-run interaction mechanism must be specified.',
 'Retain design/interference precedent. Controlled experimentation is not itself R4 or R5; Bing field estimates and browser-run estimands are not interchangeable.'),
(1022,'PENDING','journal','marketing-analytics',
 '?Session duration versus performance metrics may expose construct non-equivalence; exact browser metric is unspecified.|-No instrumentation mechanism.|-E-commerce conversion association does not establish workload coverage.|-A test statistic is not a repeated-performance uncertainty method.|-Session/performance association is not matched-metric agreement.|-No browser fixture/design method stated.',
 'Possible construct contrast only; avoid positive R1 assignment until actual performance metrics are known. Conversion and session duration alone do not validate browser timing.'),
(1023,'ADVANCE','journal','technical-optimization',
 '?Technical web optimization may operationalize performance but metrics are absent.|-No capture/off-on intervention.|?Industrial setting may bound workload/user context, not established synthetic transfer.|-Logistical uncertainty is not repeated-measure uncertainty.|-No reference agreement.|+Automation and technical optimization intervention is a candidate closest applied evaluation; isolate technical effects from operational outcomes.',
 'Uncertain advance for explicit technical web optimization and possible solution overlap; not mere marketing benefits, but no effect attribution or browser-specific design is verified.'),
(1024,'ADVANCE','journal','human-navigation',
 '-Usability/search behavior is distinct from browser timing.|?Eye movement is a capture modality, but no execution-observer effect established.|+Older adults with/without impairment provide an explicit task/population coverage boundary for agents lacking gaze/cognitive behavior.|-Cognitive information uncertainty is not a repeated-run precision method.|-Group differences are not matched-tool agreement.|?Task/population stratification may inform corpus inference, not a prescription for new human collection.',
 'Retain prior-human task-coverage analogue, bounded to search/eye-movement behavior; no new human study or equivalence with browser speed is implied.'),
(1025,'ADVANCE','journal','workload-model',
 '?Two performance metrics are mentioned but not defined.|-No capture perturbation.|+Server workload prediction explicitly supplies temporal load-context assumptions to test before page-workload transfer.|-Fuzzy membership uncertainty is not repeated-measure confidence.|-Prediction does not constitute reference-tool agreement.|?Fuzzy Markov model could motivate workload fixtures only if assumptions fit.',
 'Retain temporal workload context, not a validated browser estimator or a sampling-uncertainty method.'),
(1026,'X3','journal','export-contamination',
 '-Geological fossils do not define browser metrics; snippet web phrases conflict with title.|-No recoverable capture mechanism.|-Miocene fauna do not establish web workload/user coverage.|-Geological age uncertainty gives no transferable repeated-performance estimator.|-No matched-method agreement procedure.|-No coherent browser fixture/design contribution can be attributed.',
 'Title and venue identify paleontology while snippet contains unrelated web text: exclude this exported occurrence as no attributable R1–R6 contribution, not as verified irrelevance of an identified web source. Underlying snippet association remains unresolved.'),
(1027,'ADVANCE','journal','human-navigation',
 '-Navigation performance need not mean browser timing.|-No execution capture perturbation.|+Deaf users, textual content and practice identify user-task coverage limits that synthetic navigation may omit.|-Pearson correlations do not establish repeated-measure precision.|-Correlation with language scores is not reference agreement.|?Information structure/practice could inform task stratification; actual fixture design unverified.',
 'Retain prior-human task/population boundary; do not treat user navigation scores as runtime timing or Pearson correlation as conformance.'),
(1028,'PENDING','conference','security-index',
 '?Lighthouse/W3C performance evaluations are explicit but their relation to the security index is truncated.|?Potential use of Lighthouse capture is unresolved, not demonstrated overhead analysis.|-No workload transfer statement.|-Fuzzy uncertainty is not repeated-run precision.|-No paired reference agreement.|?Composite security index could be adjacent evaluation design; technical performance contribution unestablished.',
 'Reject X3 certainty because named performance-evaluation references may be substantive. Hold for index/metric-role clarification; no relevance inferred solely from Lighthouse keywords and no 2026 cutoff assumption.'),
(1029,'PENDING','conference','system-consolidation',
 '-Reporting statistics are not browser metric definitions.|-No runtime capture mechanism.|?Database consolidation explicitly affects web performance/reliability; could bound server-load conditions, but measured workload is unknown.|-Ad hoc statistical reporting does not establish run uncertainty.|-No matched-tool agreement.|?Consolidation comparison might be an intervention fixture, but evaluation details absent.',
 'System-consolidation performance concern warrants clarification rather than X3 based on application domain. Need an actual load/evaluation mechanism before positive mapping.'),
(1030,'PENDING','conference','lagged-statistical-model',
 '-SEO visibility is not runtime metric semantics.|-No capture perturbation.|-Search traffic is not synthetic workload coverage evidence.|?Explicit ARDL short/long-term modeling could inform temporal dependence/drift treatment only after estimand and stationarity assumptions are checked.|-Model comparison is not reference agreement.|-No browser fixture or profiler evaluation.',
 'Marketing application is not itself relevant, but explicit lagged statistical modeling is a bounded methodological candidate. Hold for original-method/assumption clarification; do not automatically exclude native statistics or adopt this application as a method.'),
(1031,'PENDING','journal-proxy','warehouse-system',
 '-Warehouse outcomes are not browser metric definitions.|-No observation mechanism.|?Query-generation and web-performance relation could bound a technical workload, but fragment gives no measured phenomenon.|-Demand uncertainty is not repeated-run measurement uncertainty.|-No agreement procedure.|?Web/mobile application evaluation may contain a workload fixture; not established here.',
 'Application domain does not ban a technical evaluation. Hold the explicit query/performance lead; demand uncertainty itself is not a transferable browser statistical method.'),
(1032,'PENDING','journal','self-healing',
 '-Recovery behavior is not browser metric semantics.|?Self-healing may observe state, but instrumentation target and observer effects are unstated.|-No workload/user coverage design shown.|-Correlation-method comparison does not establish repeated-run uncertainty.|-Pearson/Kendall comparison is not conformance or agreement.|?Adaptive recovery framework might overlap intervention/evaluation work; performance component unresolved.',
 'Reject confident exclusion until framework observation/evaluation role is clear. Mere correlation and recovery uncertainty do not earn R4/R5; retain only unresolved capture/solution-overlap leads.'),
(1033,'ADVANCE','conference','trimmed-statistical-model',
 '?CPU load construct may contrast with timing but exact metric absent.|?Load evaluation may require instrumentation; no overhead assessment supplied.|-No user/workload transfer study stated.|+Explicit trim(10%) and uncertainty reduction is an estimator/tail-handling lead; estimand shift, dependence and omitted tails require checking.|-Comparing two methods is not matched-reference agreement.|?Code structures/scripts can be fixture factors, but design unverified.',
 'Retain statistical load-measurement analogue; trimming is not automatically appropriate for browser tails and claimed uncertainty reduction is not verified. Exact 2026 date unresolved.'),
(1034,'X3','journal','ranking-visibility',
 '-Stakeholder institutional ranking perceptions are not browser timing semantics.|-No capture intervention.|-Institutional stakeholders do not establish workload/agent coverage.|-Generic uncertainty has no repeat-performance estimator.|-Ranking perceptions are not reference-tool agreement.|-No technical corpus or profiler design.',
 'Institutional visibility/knowledge-sharing constructs, not technical web measurements. Human participation is not the reason for exclusion; no bounded performance-method transfer is specified.'),
(1035,'ADVANCE','thesis-proxy','probability-simulation',
 '-No browser metric semantics specified.|-No runtime observation intervention.|?Web planning/simulation might model workload probabilities, but target is unresolved.|+Explicit confidence interval for p(i) and distinction between uncertain values and discrete structure is a methodological lead for separating sampling and model uncertainty.|-No matched reference agreement.|?Simulation planning could inform probabilistic fixture assumptions, not an established browser design.',
 'Reject X3: CI-versus-model uncertainty distinction is a bounded statistical transfer lead. Check what p(i) estimates, data-generating assumptions and originality; book label/ProQuest dissertation URL is not verified source type.'),
(1036,'X3','thesis-proxy','marketing-construct',
 '-Export-marketing web capabilities are business constructs, not browser timing.|-No capture mechanism.|-Export outcomes do not specify workload/user transfer.|-Statistical questions in apparent acknowledgments give no method.|-No reference agreement.|-No fixture or profiler evaluation method.',
 'Export-marketing thesis topic and apparent acknowledgment fragments identify no transferable technical/statistical contribution. Not excluded for thesis type or inaccessible full text.'),
(1037,'ADVANCE','conference','resource-workload',
 '?Functioning efficiency may be a different construct; no browser metric definition yet.|-No capture intervention.|+Request complexity, data volume and hardware explicitly identify context factors relevant to workload transfer.|?Resource-model uncertainty is not necessarily repeated sampling; no estimator stated.|-No matched-reference agreement.|+Request/data/hardware factors are candidate controlled-fixture factors, with causal and design assumptions unverified.',
 'Retain explicit workload/resource factor model; do not equate its efficiency construct or uncertainty with browser timing precision.'),
]

def primary():
    freeze=json.loads((ROOT/'target_freeze.json').read_text())
    assert digest(QUEUE)==freeze['source_sha256']
    assert all(digest(Path(p))==h for p,h in freeze['producer_files'].items())
    with QUEUE.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f); fields=reader.fieldnames; rows={r['occurrence_E_ID']:r for r in reader if r['occurrence_E_ID'] in freeze['ordered_target_EIDs']}
    producer={x['E_ID']:x for x in json.loads((PROD/'primary_judgments.json').read_text())['items']}
    checks=[]
    for n,status,typ,method,six,why in DATA:
        eid=f'E-{n}'; r=rows[eid]; parts=six.split('|'); assert len(parts)==6
        q={f'R{i+1}':{'judgment':{'+':'retain','?':'unresolved','-':'not_established'}[s[0]],'reason':s[1:]} for i,s in enumerate(parts)}
        checks.append({'target_E_ID':eid,'event_E_ID':f'E-{4400+n-1000}','stage1':status,'primary_code':'X3' if status=='X3' else 'advance/uncertain' if status=='ADVANCE' else 'PENDING','R1_R6':q,'positive_RIDs':[k for k,v in q.items() if v['judgment']=='retain'],'candidate_RIDs':[k for k,v in q.items() if v['judgment']=='unresolved'],'reason':why,'type_proxy':typ,'method_proxy':method,'producer_stage1':producer[eid]['stage1'],'producer_X3_adjudication':('retained' if status=='X3' else 'rejected') if producer[eid]['stage1']=='X3' else 'not producer X3','title_as_exported':r['title'],'complete_Scholar_snippet_as_exported':r['abstract_or_snippet'],'authors_metadata_as_exported':r['raw_record_metadata'],'year_as_exported':r['publication_year'],'record_url_as_exported':r['record_url'],'metadata_limits':'Date/version/cutoff, language/authorized translation, type/originality and identity UNVERIFIED; type/method labels are export proxies; no DUP/SID adjudication.','claim_support':'UNASSESSED','methodological_confidence':'UNASSESSED','fulltext':'NOT RUN','citation':'NOT RUN','actual_primary_read':'Complete stored title, entire Scholar snippet (not abstract), author/venue/year/URL/record metadata read.'})
        save('primary_checks.json',{'reviewer':'Sol AI separate-pass technical QA, not independent human review','protocol':'ERP-2026-10-25-v1.0','items':checks,'checked':len(checks),'unreviewed':38-len(checks)})
    added=['effective_event_E_ID','effective_stage1','effective_primary_code','effective_positive_RIDs','effective_candidate_RIDs','effective_R1_R6_json','effective_reason','effective_type_proxy','effective_method_proxy','effective_claim_support','effective_methodological_confidence','effective_fulltext','effective_citation','effective_metadata_limits']
    with (ROOT/'overlay.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields+added);w.writeheader()
        for c in checks:
            r=dict(rows[c['target_E_ID']]); vals=[c['event_E_ID'],c['stage1'],c['primary_code'],','.join(c['positive_RIDs']),','.join(c['candidate_RIDs']),json.dumps(c['R1_R6'],ensure_ascii=False),c['reason'],c['type_proxy'],c['method_proxy'],'UNASSESSED','UNASSESSED','NOT RUN','NOT RUN',c['metadata_limits']];r.update(dict(zip(added,vals)));w.writerow(r)
    with (ROOT/'events.csv').open('w',newline='',encoding='utf-8') as f:
        names=['event_E_ID','target_E_ID','stage1','primary_code','producer_stage1','producer_X3_adjudication','reason'];w=csv.DictWriter(f,fieldnames=names,extrasaction='ignore');w.writeheader();w.writerows(checks)
    print('Primary persisted:',len(checks))

if __name__=='__main__': primary()

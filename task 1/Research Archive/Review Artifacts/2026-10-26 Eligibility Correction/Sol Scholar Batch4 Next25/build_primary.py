import csv
import json
from datetime import datetime, timezone
from freeze import HERE, ROOT, QUEUE, PRODUCER, sha

# Authored after reading the complete stored snippets and exported metadata.
# Each tuple: type proxy (not verified type), R5 reason, R4 judgment, positive R4.
CASES = {
725: ('context_review', 'Imaging reliability text explicitly names closeness of agreement and Bland–Altman graphical comparison. Transfer: distinguish replicate precision from paired profiler/reference agreement; no imaging validity or tolerances transfer.', 'Replicates alone do not establish an uncertainty procedure or hierarchy; no positive R4 assignment.', False),
726: ('methodological_lead', 'The snippet explicitly extends classical limits of agreement to replicate measurements. Transfer: assess whether repeated profiler/reference pairs require replicate-aware LoA rather than treating repeats as independent. Generic journal title leaves exact work identity unresolved.', 'Extension to replicate data is a lead, but uncertainty estimand/nesting is not stated; no separate positive R4 assignment.', False),
727: ('empirical_application', 'Lithium assay snippet explicitly uses paired sample-level observations and says correlation alone does not assess agreement. Transfer: preserve profiler/reference pairing and do not use correlation as agreement; chemical performance does not validate browser metrics.', 'Two replicates and a paired observation are stated, not an uncertainty model; no positive R4 assignment.', False),
728: ('empirical_application', 'Plethysmographic techniques are explicitly assessed for agreement, not merely compared. Transfer: separate within-technique repeat differences from between-tool differences; lung-volume results do not transfer.', 'POSITIVE bounded R4: SD of differences between two replicates supplies an explicit repeat-variation summary. Examine its unit and assumptions before adapting a browser-run precision summary.', True),
729: ('software_method', 'Extended biasplot explicitly targets bias, precision and agreement. Transfer: inspect agreement visualization for paired tool outputs, not generic ranking or tool superiority.', 'POSITIVE bounded R4: indexed replicates and the stated absence of a CB around percentage agreement raise explicit uncertainty-reporting/design issues; no confidence-band formula is verified.', True),
730: ('context_review', 'Bland–Altman review explicitly discusses calculating/evaluating agreement limits. Transfer: contextual guide to paired-output analysis and locating original methods; veterinary thresholds are not browser thresholds and review is not primary proof.', 'Replicate characterization is truncated; uncertainty procedure is not exposed. No positive R4 assignment.', False),
731: ('empirical_application', 'Neuromuscular-measure interchangeability title plus replicate differences and limits of agreement support an R5 lead. Transfer: distinguish repeat precision and paired agreement before claiming interchangeability; no clinical result transfers.', 'The trailing “95%” is incomplete; do not infer confidence-interval methods. No separate positive R4 assignment.', False),
732: ('empirical_application', 'Snippet explicitly assesses agreement of new and predicate cell-count methods. Transfer: distinguish within-platform precision from cross-platform agreement; no biological/device thresholds transfer.', 'POSITIVE bounded R4: CV of replicate measurements is an explicit repeat-variation summary. Site and replicate dependence must be resolved before any browser-run CV use.', True),
733: ('empirical_application', 'Analyzer/manual-reference agreement estimates and missing manual replicates are explicit. Transfer: scrutinize asymmetric reference precision in profiler/reference agreement; no analyzer validity is imported.', 'POSITIVE bounded R4 design limitation: missing reference replicates prevent direct assessment of that component of repeat variation; this is not positive repeatability evidence.', True),
734: ('software_method', 'Biasplot implements statistical methodology and warns that agreement can mislead. Transfer: inspect bias/precision plots for matched profiler/reference outputs; implementation and estimator assumptions remain unread.', 'No replicate hierarchy or uncertainty treatment is stated; no positive R4 assignment.', False),
735: ('empirical_application', 'Three dental-model methods, delayed replicate readings and an agreement-method reference justify uncertain R5 routing, not verified analysis. Transfer: inspect how same-object pairing and delayed reads were handled; no dental accuracy result transfers.', 'POSITIVE bounded R4: one-week separation gives an explicit repeat-time design feature. Separate temporal/session variability from immediate repetition; do not adopt a one-week browser schedule.', True),
736: ('empirical_application', 'Assay snippet explicitly reports method comparison and agreement. Transfer: inspect how replicate stability and paired assay comparison are separated; no drug assay finding transfers.', 'POSITIVE bounded R4: stability of replicate measurements over time is explicit, but “10-” is truncated. Do not invent duration, drift model or stopping rule.', True),
737: ('empirical_application', 'Automated SAA assay snippet states method agreement plus replicate-pool CV. Transfer: distinguish pooled within-assay precision from between-tool agreement; species and assay acceptability do not transfer.', 'POSITIVE bounded R4: replicate serum-pool CV explicitly summarizes variation; browser unit/nesting and appropriate scale must be justified independently.', True),
738: ('context_review', 'Clinical-measurement assessment explicitly addresses limits of agreement with replicates/multiple observers. Transfer: contextual lead to replicate-aware profiler/reference agreement methods, not primary empirical validation.', 'Observers and replicates are named without an uncertainty procedure; no separate positive R4 assignment.', False),
739: ('context_review', 'Review of methodological reviews explicitly concerns Bland–Altman reporting. Transfer: inspect agreement-reporting requirements and locate originals; the quoted 50-subject/three-repeat rule is not a browser sample-size prescription.', 'Replication count alone is not an uncertainty justification; no separate positive R4 assignment.', False),
740: ('methodological_lead', 'Title proposes copula-based agreement for heteroscedastic measurements; snippet discusses replicate-data models. Transfer: investigate magnitude-dependent profiler/reference disagreement; no copula suitability or estimator is verified.', 'POSITIVE bounded R4: heteroscedastic replicated-measurement modeling is explicit in title/snippet. Map run hierarchy and changing variance before adapting; assumptions unread.', True),
741: ('software_measurement_unclear', 'UNCLEAR, not positive R5: quoted “agreement” is within replicate-measurement terminology under the same procedure/location, not demonstrated between-method or reference agreement. The producer R5 reason also asserts R6 while its own R6 field denies a mapping.', 'UNCLEAR: same-procedure/location replication could inform fixture repeatability, but the truncated definition does not show an uncertainty method. PENDING targeted relevance/identity inspection, not X3.', False),
742: ('identity_ambiguous', 'Explicit LoA and failure to account for replicates give a potential R5 limitation/context lead. However “K O’Brien / Lancet / 1986” conflicts with the BerlinRUG/20151217/MCSwithR-Berlin2015 URL; PENDING exact work/version and source-role clarification, not exclusion.', 'Missing replicate handling is a limitation lead, but cannot attribute an uncertainty method to this unresolved work; no positive R4 assignment.', False),
743: ('methodological_lead', 'Title explicitly proposes agreement models for quantitative data with heterogeneous random raters and replicates. Snippet is apparently reference-list material, not method evidence. Transfer: investigate rater/run variance in paired-tool agreement; no model details verified or duplicate merged.', 'POSITIVE bounded R4 from title only: heterogeneous random raters and replicate measurements identify a hierarchy/variance modeling lead. Tool/run factors must be mapped, not equated to human raters.', True),
744: ('methodological_lead', 'Pavement-friction snippet explicitly says poor device repeatability limits attainable agreement. Transfer: reference and profiler repeat error can constrain achievable agreement; pavement thresholds/results are irrelevant to browser tolerances.', 'POSITIVE bounded R4: explicit repeatability constraint motivates separating each device’s repeat variation from between-device differences; no variance formula verified.', True),
745: ('context_review', 'Clinical-measurement snippet explicitly requires defining acceptable agreement a priori. Transfer: prespecify justified browser tolerances rather than selecting them after observing results; clinical tolerances do not transfer.', 'POSITIVE bounded R4: replicates from each subject explicitly identify nested observations. Browser page/session/run mapping and dependence must be justified, not assumed.', True),
746: ('empirical_application', 'Manual/automatic bladder measurement snippet explicitly targets repeatability and agreement. Transfer: separate within-technique variability from matched-method agreement; the reported smaller variation is not evidence about profilers.', 'POSITIVE bounded R4: variation between replicate readings is explicitly compared. Unit, operator and device nesting remain unread; no browser precision conclusion.', True),
747: ('reporting_statement', 'COMPARE title and snippet explicitly concern LoA against prespecified thresholds. Transfer: examine reporting/analysis rules for paired profiler/reference outputs, not cardiac-output tolerance adoption or statement-as-experiment evidence.', 'POSITIVE bounded R4: accounting for replicate measurements per subject is explicit. The handling procedure and mapping to nested browser runs require full text.', True),
748: ('methodological_lead', 'TSD/FWD title specifies LoA; snippet explicitly discusses device agreement with repeated observations. Transfer: investigate replicate-aware profiler/reference agreement; references in snippet do not verify the paper’s implemented method.', 'POSITIVE bounded R4: multiple observations per individual explicitly raise nested dependence. Do not treat browser repetitions as independent individuals or import pavement variance estimates.', True),
749: ('empirical_application', 'Handheld/reference comparison uses a single ADVIA reading versus a mean of 2–3 HC readings and explicitly addresses agreement. Transfer: paired agreement depends on asymmetric aggregation; cat hemoglobin results do not transfer.', 'POSITIVE bounded R4: one-versus-mean-of-2–3 replication is an explicit aggregation/unit distinction. Map uncertainty of averages versus single runs; do not infer a variance-reduction guarantee.', True),
}

def write_json(name, obj):
    with (HERE / name).open('x') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')

if __name__ == '__main__':
    freeze = json.loads((HERE/'target_freeze.json').read_text())
    # Only the immutable queue and completed first25 producer inputs are used.
    for p in [QUEUE, PRODUCER/'overlay_first25.csv', PRODUCER/'authored_judgments_first25.json']:
        assert sha(p) == freeze['inputs'][str(p.relative_to(ROOT))]
    with QUEUE.open() as f:
        reader = csv.DictReader(f)
        original_columns = reader.fieldnames
        rows = {r['occurrence_E_ID']:r for r in reader if r['occurrence_E_ID'] in freeze['target_ids']}
    with (PRODUCER/'overlay_first25.csv').open() as f:
        producer = {r['occurrence_E_ID']:r for r in csv.DictReader(f)}
    authored = {r['occurrence_E_ID']:r for r in json.loads((PRODUCER/'authored_judgments_first25.json').read_text())}
    assert set(rows) == set(producer) == set(authored) == set(freeze['target_ids'])
    judgments, overlay = [], []
    for i, eid in enumerate(freeze['target_ids']):
        n = int(eid[2:]); row=rows[eid]; old=authored[eid]; p=producer[eid]
        assert row['title']==old['title'] and row['abstract_or_snippet']==old['entire_original_snippet'] and row['raw_record_metadata']==old['raw_metadata']
        proxy, r5, r4, positive4 = CASES[n]
        pending = n in (741,742)
        positive = (['R4'] if positive4 else []) + ([] if pending else ['R5'])
        q = {
            'R1':'NO POSITIVE MAPPING: this title/snippet does not define browser metric constructs, scope, units or absent-versus-zero semantics.',
            'R2':'NO POSITIVE MAPPING: measurement automation alone does not demonstrate capture limitations, observer perturbation or instrumentation overhead.',
            'R3':'NO POSITIVE MAPPING: clinical/device populations and repeated objects are not evidence of synthetic-to-user workload transfer.',
            'R4':r4, 'R5':r5,
            'R6':'NO POSITIVE MAPPING: no explicit fixture ground truth, randomized/block design, corpus inference or closest browser solution is established; general experimentation is insufficient.'}
        disposition = 'PENDING' if pending else 'ADVANCE'
        reason = r5 + ' ' + r4
        correction = 'Retain bounded R5 routing; replace vague R4 hints with explicit positive/no-positive judgments. R6 requires design evidence, not only absence of a browser solution.'
        if n==741:
            correction='Producer six-question inconsistency corrected: R5 field/reason claims R6/R4 while R6 field denies it. Repeatability definition is not between-method agreement. ADVANCE → PENDING; no positive RIDs until resolved.'
        if n==742:
            correction='ADVANCE → PENDING because exported identity cues conflict; retain possible R5 context lead without attributing Lancet-1986 authorship to a 2015-named slide export.'
        j=dict(occurrence_E_ID=eid,effective_event_E_ID=f'E-{3800+i}',effective_producer_event_E_ID=p['new_event_E_ID'],
               effective_disposition=disposition,effective_primary_code='',effective_RIDs=positive,
               effective_question_judgments=q,effective_reason=reason,effective_producer_comparison=correction,
               effective_type_proxy=proxy,effective_type_proxy_status='exported title/metadata cue only; NOT verified source type',
               effective_reviewer='Sol separate-pass AI validation; not independent human/scientific review',
               effective_reviewed_utc=datetime.now(timezone.utc).isoformat(),
               effective_date_status='PENDING exact publication/version date against 2026-10-25 inclusive; year alone not verified',
               effective_language_status='PENDING full-text language/authorized translation',
               effective_source_type_status='PENDING original/contextual evidence-role verification',
               effective_identity_status='ID-PENDING; historical duplicate candidates preserved, no merges or SID allocation',
               effective_claim_support='UNASSESSED',effective_methodological_confidence='UNASSESSED',
               effective_fulltext_pass='NOT RUN',effective_citation_pass='NOT RUN',
               effective_original_record_sha256=__import__('hashlib').sha256(json.dumps(row,sort_keys=True,ensure_ascii=False).encode()).hexdigest())
        judgments.append(j)
        out=dict(row)
        for k,v in j.items():
            if k!='occurrence_E_ID': out[k]=json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v
        out['effective_producer_history_json']=json.dumps(p,ensure_ascii=False)
        out['effective_producer_authored_history_json']=json.dumps(old,ensure_ascii=False)
        overlay.append(out)
    write_json('judgments.json',judgments)
    with (HERE/'delta_overlay25.csv').open('x') as f:
        writer=csv.DictWriter(f,fieldnames=list(overlay[0]));writer.writeheader();writer.writerows(overlay)
    with (HERE/'item_checks.tsv').open('x') as f:
        writer=csv.writer(f,delimiter='\t');writer.writerow(['occurrence_E_ID','original_title','complete_original_Scholar_snippet','raw_metadata','record_url','all_six_questions_read','producer_judgments_compared','effective_event_E_ID','effective_disposition','effective_RIDs','effective_reason'])
        for j in judgments:
            r=rows[j['occurrence_E_ID']]
            writer.writerow([r['occurrence_E_ID'],r['title'],r['abstract_or_snippet'],r['raw_record_metadata'],r['record_url'],'YES','YES',j['effective_event_E_ID'],j['effective_disposition'],';'.join(j['effective_RIDs']),j['effective_reason']])
    groups={}
    for j in judgments:
        for rid in j['effective_RIDs']:
            groups.setdefault(rid+' / '+j['effective_type_proxy'],[]).append(j['occurrence_E_ID'])
        if not j['effective_RIDs']:
            groups.setdefault('PENDING / '+j['effective_type_proxy'],[]).append(j['occurrence_E_ID'])
    exclusions=[j['occurrence_E_ID'] for j in judgments if j['effective_disposition']=='X3']
    selected=sorted(set(exclusions+[min(m) for m in groups.values()]))
    write_json('qa_freeze.json',dict(created_utc=datetime.now(timezone.utc).isoformat(),phase='before secondary stored-original rereads',
        primary_sha256=sha(HERE/'judgments.json'),overlay_sha256=sha(HERE/'delta_overlay25.csv'),
        all_proposed_exclusions=exclusions,rule='all exclusions plus lexicographically first EID per explicit positive R/type-proxy group; also each no-positive pending type proxy',
        groups={k:dict(members=v,selected=min(v),nonselected_count=len(v)-1) for k,v in sorted(groups.items())},
        selected_ids=selected,selected_count=len(selected),status='PLANNED; not checked by manifest creation',
        type_boundary='Proxies are exported-title/metadata cues, not verified source types',
        original_columns=original_columns))
    print(json.dumps(dict(primary_count=len(judgments),qa_selected=selected),indent=2))

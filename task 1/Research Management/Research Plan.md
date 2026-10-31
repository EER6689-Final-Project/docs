# Research Plan

**Working title:** RELIABILITY OF DELAYED WEBSITE OR WEB APPLICATION PERFORMANCE DIAGNOSIS.

**Status:** literature review and research proposal. The research direction was selected by the researcher on 2026-10-31. The objective-by-objective methodology below is a proposed study design. Implementation and the pilot remain future work; the pilot will establish feasibility and inform a separate protocol and analysis freeze before the main study. Selection does not establish novelty or experimental findings.

## Problem and rationale

A lightweight browser monitor can detect an unusual page load or interaction without retaining enough detail to explain it. A common response is to run the page again with richer profiling. The follow-up execution may have a different cache state, content, server response or script path. Its diagnosis can therefore be correct for the follow-up visit while failing to explain the original alert.

The research investigates this evidence gap for persistent and intermittent website performance regressions. Website-specific histories help establish comparable conditions and detect changes; their existence is not the novelty claim. The possible contribution is a measured boundary on the reliability and cost of delayed diagnosis, supported by independently verified faults and visit-specific evidence.

The [novelty comparison](<Monitoring Novelty Cross Reference.md>) connects this question to Paradyn, Vesper, WebREC, LMAT, Hindsight, WMF and existing monitoring tools. Adaptive instrumentation, historical baselines, trace retention and performance-fault testing already have substantial prior art. The report should distinguish the proposed browser-specific evaluation from those established techniques.

## Research question and aim

**Research question:** For projects that require accurate and reliable performance diagnosis at a limited monitoring cost, how does detailed follow-up profiling compare with evidence retained during the original visit in identifying the cause of an earlier website or web application regression under matched resource limits and the same diagnosis deadline?

**Aim:** assess original-cause attribution, diagnostic coverage and total monitoring cost for delayed browser profiling and retained original-visit evidence, then use those results to inform profiler design choices within the tested conditions.

**Application:** The results are intended to inform performance-monitoring and resource-use estimation systems that measure web application behavior while limiting collection and storage costs. The primary comparison concerns intermittent faults, for which the original cause may be absent at follow-up. The experiment evaluates evidence collection and diagnosis; it does not validate the outputs of a separate application.

## Hypotheses

**Research hypothesis (H₁):** For intermittent website performance regressions, retaining diagnostic evidence from the original browser visit leads to a higher proportion of correctly attributed regression episodes than detailed profiling during a follow-up visit, under matched monitoring budgets and the same diagnosis deadline.

**Null hypothesis (H₀):** Under the same conditions, retaining diagnostic evidence from the original visit does not increase the proportion of correctly attributed intermittent regression episodes.

Correct attribution means identifying the independently verified fault class responsible for the **original regression episode**. Missed alerts, failed follow-up visits, unavailable evidence and abstentions remain in the evaluation denominator. Total monitoring cost includes the original collection, retained evidence, confirmations and follow-up visits.

These are working hypotheses to test, not expected findings. Fault persistence is the main factor to investigate; follow-up delay and browser state are secondary factors within the study's resource limits. The statistical test, sample size and decision criteria remain to be specified.

## Objectives

1. **Define a repeatable measurement protocol** that records browser conditions, metric definitions and evidence provenance, and clearly separates original visits from diagnostic follow-up visits.
2. **Build a longitudinal, website-specific evaluation dataset** with stable periods, persistent and intermittent regressions, and different causes that produce similar symptoms. Use independently verified fault labels.
3. **Implement and compare feasible evidence-collection strategies**, including lightweight original-visit attribution, retained original-event evidence, detailed follow-up profiling and periodic detailed capture.
4. **Evaluate diagnostic effectiveness and total monitoring cost** by measuring correct original-cause attribution, missed episodes, misleading diagnoses, abstentions, diagnosis delay, instrumentation effects and capture failures.
5. **Identify when delayed diagnosis is reliable**, focusing on fault persistence and assessing the effects of follow-up delay and browser-state changes.

## Methodology by objective

### Overall research design

Use a **controlled longitudinal experiment**: observe the same website conditions over time, introduce known performance faults, and compare the evidence collected by different profiling strategies. The main unit of evaluation is an **original regression episode**, linked to its original visit and any diagnostic follow-up visits. A persistent fault may produce several affected visits; these belong to the same fault occurrence and must be identified as related observations.

Start with owned or authorized controlled websites and small test websites, called **fixtures**, on the bounded localhost Chromium setup. Use scheduled synthetic visits with fixed safe inputs. Here, ongoing monitoring means repeated scheduled observations, not observation of every real user or everything that happens between visits. An optional authorized live-site sample can test operational robustness, but unexplained live-site slowdowns cannot establish diagnostic accuracy.

| Objective | Main method | Expected output |
| --- | --- | --- |
| 1. Define a repeatable protocol | Specify conditions, metrics, provenance and conformance checks. | Versioned measurement protocol and data dictionary. |
| 2. Build the dataset | Collect site-specific histories and independently verified fault episodes. | Longitudinal episode dataset with separate evaluation labels. |
| 3. Compare strategies | Run controlled, randomized comparisons under complete resource budgets. | Comparable evidence and cost records for each strategy. |
| 4. Evaluate results | Measure original-cause attribution, coverage, failures and cost with uncertainty. | Outcome tables, effect estimates and cost–coverage plots. |
| 5. Identify reliability conditions | Compare persistent/intermittent faults, delays and browser states. | An evidence-based account of when delayed diagnosis works or loses evidence. |

The procedures below are proposed research choices. Exact targets, versions, run counts, thresholds, budgets and statistical procedures will be fixed after the pilot and before inspecting main-study results.

The [Study Source Map](<Study Source Map.md>) attributes metric definitions, methodological precedents and limitations to the selected papers and documents, using their Zotero keys. It separates source-supported principles from this study's operational choices, including the episode definition and primary attribution rate.

### Objective 1: Define a repeatable measurement protocol

**Method.** Write a measurement contract that explains what each visit measures and when it starts and ends. Keep original visits and follow-up visits separately identified, even when they use the same URL.

1. **Fix the environment.** Pin the Chromium, automation, profiler and metric-library versions. Record the host, operating system, viewport, CPU/network profile and background workload. A mobile viewport remains an emulated profile, not evidence from a physical mobile device.
2. **Define browser state and journeys.** Specify the navigation, safe input sequence, observation window, cache preparation, session data and service-worker policy. Record the state actually used. A new browser context alone must not be treated as proof that every relevant cache or server state was reset.
3. **Define metric contracts.** Begin with the smallest feasible metric/fault set. Candidate measures include LCP for loading, INP for qualifying scripted interactions, and CLS for eligible layout shifts. Specify when callbacks are finalized and exported, since a metric may become available only after an interaction or page-lifecycle change; see the [`web-vitals` usage documentation](https://raw.githubusercontent.com/GoogleChrome/web-vitals/main/README.md). Keep FCP, TBT, Speed Index and client-observed TTFB as separately defined diagnostics when collected. Missing or unsupported measurements receive a reason code, not a zero; TBT is not a replacement for INP. Do not combine incompatible visits into a website-wide average.
4. **Check measurement conformance.** Use simple fixtures to confirm that the intended event is recorded, its timestamp belongs to the correct visit and its output matches the pinned reference definition within a declared tolerance. This checks implementation consistency; agreement between two tools using the same browser API is not independent validation of the underlying construct.
5. **Check instrumentation effects.** Compare minimally observed and profiled runs in randomized blocks using external resource measurements where feasible. Measure whether collection changes timings, fault activity or failures. Keep these calibration runs separate from the main strategy comparison.

**Output.** A versioned protocol, metric dictionary, state/reset procedure, visit identifier scheme and conformance record. Failed conformance checks must be resolved or the affected output removed before the main study.

**Implementation reference.** [Playwright browser contexts](https://playwright.dev/docs/browser-contexts) provide isolated browser storage for repeatable tests. The protocol must still specify host and server state separately; browser isolation does not establish experimental independence.

**Methodological basis.** Vesper illustrates why metric meaning, instrumentation and differences between executions matter; its historical Ready Index is not current INP. See the [Vesper source note](<../Research Papers/T1.1 Metric Semantics/Papers/Netravali et al 2018 - Vesper Measuring Time-to-Interactivity.md>).

### Objective 2: Build a longitudinal, website-specific dataset

**Method.** Collect a chronological history for each site and measurement condition. Separate the data used to establish normal behavior from the data used to evaluate diagnosis.

1. **Choose the corpus.** Select a manageable set of fixtures with different loading and interaction patterns. Define the inclusion criteria and hold out distinct fixture templates or site instances before tuning. Begin with single-fault cases so the expected fault class is unambiguous; multi-fault cases are optional extensions.
2. **Collect stable histories.** Revisit each site under the declared conditions to establish normal variation. Use an early stable period for baseline training, a separate period for tuning, and later deployments for testing. Evaluate held-out fixtures using the frozen method; any site-specific calibration uses only their designated earlier stable history. Freeze baseline-update rules so a persistent regression is not silently absorbed as normal behavior.
3. **Create known fault episodes.** Introduce controlled changes with declared onset, duration and severity. Include the cases below. Pilot work will select effects large enough to establish a measurable regression without making all cases trivially obvious.

| Case | How to construct it | Why it is needed |
| --- | --- | --- |
| Stable control | No injected fault under the specified conditions. | Estimate normal variation and false alarms. |
| Persistent regression | Keep a verified fault active across the original and follow-up visits. | Test diagnosis when the cause remains available. |
| Intermittent or one-visit regression | Activate the fault for selected visits or a short interval. | Test whether follow-up profiling loses the original evidence. |
| Similar symptom, different cause | For example, delay an LCP resource in one case and delay its rendering with main-thread work in another, if the pilot confirms both effects. | Check whether a strategy identifies the cause rather than only the slow metric. |
| Nuisance change | Change a declared condition, such as cache state, without an injected software fault. | Test whether diagnosis confuses an environmental change with the target fault. |

4. **Verify the labels independently.** Keep an evaluator-only intervention manifest and an execution check, such as a server request-delay log or an instrumented handler entry/exit record. Check that the fault actually ran on each original and follow-up visit. Enabling a fault flag alone is insufficient. A rich trace is a reference observation, not ground truth. Use minimally observed pilot controls to establish the intended performance effect, and freeze the eligibility rule before testing. Record label uncertainty separately; do not relabel a difficult case to match the profiler's answer.
5. **Collect and preserve all attempts.** Keep successful visits, timeouts, missed triggers, collection failures and visits after a budget is exhausted. Store raw evidence separately from derived metrics and labels. Never provide hidden labels, fault schedules or revealing identifiers to the monitoring or diagnostic strategy.

**Episode eligibility.** Define eligible original opportunities from the planned, pilot-validated fault cases, independent execution checks and whether the journey/metric applies. Eligibility must not depend on a strategy alerting, producing a metric or observing a slow value. A missing metric or fault-induced timeout does not by itself make an opportunity ineligible. Keep fault-active but ineligible cases, uncertain labels and failed visits separately visible, using the same frozen rules for every strategy.

The dataset will use linked tables or equivalent structured records:

| Record | Minimum contents |
| --- | --- |
| Site and configuration | Site/template, page/journey, deployment, browser/tool versions, host, profile and intended state. |
| Visit | Visit ID, original/follow-up role, parent episode, timestamps, actual state, measurements, strategy and failure/missingness codes. |
| Episode and evaluator label | Fault occurrence ID, fault class, activity checks on each visit, persistence, severity, regression eligibility and label confidence/status. |
| Evidence and diagnosis | Evidence file references and hashes, capture window/loss, diagnosis time, predicted class or abstention, supporting evidence. |
| Resource cost | Collection and rerun time, CPU time, peak memory, bytes collected/retained/exported, follow-up count and budget remaining. |

**Output.** A longitudinal dataset with a data dictionary, collection manifest and reproducible fixture configurations. Preserve a complete attempt ledger; episodes with unverifiable labels remain visible in the accounting but cannot be scored as known-cause cases. Report their frequency and examine whether this missingness differs by strategy. Remove credentials and unnecessary page/user content from any shared dataset; define retention and release rules before collection.

**Methodological basis.** [Performance mutation testing](<../Research Papers/T1.5 Profiler Validation/Papers/Delgado-Perez et al. 2021 - Performance Mutation Testing.md>) provides a precedent for introducing known performance changes. Its C++ experiments do not validate browser fault labels or justify copying their repetition counts or statistical tests.

### Objective 3: Implement and compare profiling strategies

**Method.** Use the same lightweight measurements, baseline, alert rule, fault taxonomy and diagnosis deadline across the main comparisons. Change how diagnostic evidence is collected. Each strategy must diagnose the original episode using only the evidence it would legitimately possess.

“Lightweight” and “detailed” describe **capture contracts**, not fixed lists of metric names. Define each contract by its collectors, events/fields, version, observation window, attribution, buffering and export rules. Use the [source map's definitions and capture rationale](<Study Source Map.md#evidence-for-defining-lighter-and-deeper-capture>) to select candidate contracts, then verify their coverage and resource cost in the pilot. A metric can be available through more than one acquisition path; the label alone does not establish cost.

| Strategy | Collection procedure | Main comparison role |
| --- | --- | --- |
| A. Lightweight original-visit attribution | Collect metrics and supported existing attribution on every original visit. | A practical low-cost baseline using existing attribution. |
| B. Detailed follow-up profiling | Use the common alert to schedule a new richly profiled visit after a declared delay. Keep its evidence separate from the original visit. | Test delayed diagnosis of the original episode. |
| C. Bounded original-event capture | Collect a feasible, explicitly specified set of events during the original visit and retain the relevant evidence when alerted. | Test the value of evidence from the original execution. |
| D. Periodic detailed capture | Select rich original visits using a fixed schedule independent of hidden faults; randomize the schedule's starting position. | Compare a simple alternative that sometimes captures the original episode. |
| E. Always-rich reference | Collect detailed evidence on every visit within its separate resource allowance. | Describe diagnostic coverage and instrumentation cost; it is not a cause oracle or guaranteed upper bound. |

All arms retain the common lightweight record. First test C's API support, event coverage, buffer lifetime, event loss and resource cost. It must capture events before they are needed; an alert cannot reconstruct activity that was never recorded. If only a narrower evidence set is feasible, specify that set and narrow the comparison. If no useful original-event comparator is feasible, revisit H₁ before the main study rather than claim to have tested it.

For A, the [`web-vitals` attribution build](https://raw.githubusercontent.com/GoogleChrome/web-vitals/main/README.md) is a candidate source of existing diagnostic fields. These fields support diagnosis but do not independently prove the injected cause. Verify the supported fields and costs in the pinned version during the pilot; its current documentation is not a frozen study configuration.

**Fair allocation.** Run matched scenario blocks with the same site, fault class, persistence, severity and intended state. Each strategy receives its own original execution, with evidence from other arms withheld. Randomize strategy order within blocks, reset state as specified and record actual fault activity. Pairing controls the assigned scenario, not the exact nondeterministic execution. Follow-up visits remain later observations with their assigned delays. Prevent simultaneous runs from competing for the same host resources.

**Budget control.** Give the compared policies the same scheduled original-visit opportunities, diagnosis deadline and predefined resource caps. Count baseline construction, continuous collection, serialization, retention, confirmations, export, unsuccessful attempts and reruns. Record CPU time, elapsed time, memory and bytes separately; do not add incompatible units into an unexplained score. If a strategy reaches a cap, apply a predefined fallback or abstention rule and keep remaining episodes in the denominator. Use pilot costs to select feasible common budget levels, then report cost–coverage curves where exact resource matching is impossible.

Generate the scheduled workload and fault opportunities independently of policy budgets. If a policy cannot scan an assigned opportunity, the evaluator-only harness still verifies the workload and label; that eligible opportunity counts as no correct in-time diagnosis. Its evidence remains hidden from the policy. Report evaluator-only verification work as a separate experimental cost; include every measurement used by a policy, including common lightweight collection, in that policy's budget. Check verification overhead during calibration as well.

**Diagnosis rule.** Define a common fault-class vocabulary and a reproducible mapping from available evidence to a predicted class or **abstention**. Keep rules fixed after tuning and hide evaluator labels until predictions are recorded. Use a primary single-class decision; any ranked candidate lists are secondary. A manually reviewed subset can audit evidence quality, but a full human study or machine-learning classifier is not required.

**Output.** Versioned policy configurations, randomized allocation records, evidence available to each policy, prediction records and complete cost ledgers. Website-specific versus generic alert thresholds can be tested later as a separate **ablation study**; changing detection and capture together would obscure which change explains a result.

### Objective 4: Evaluate diagnostic effectiveness and total cost

**Method.** Score predictions against the independently verified original fault class. Evaluate intermittent faults first for H₁; use persistent faults and other conditions to explain the limits of the result.

**Primary outcome:**

> Original-cause attribution rate = verified original regression episodes correctly attributed within the deadline and budget / all verified original regression episodes assigned to the strategy.

Missed alerts, failed reruns, absent evidence, exhausted budgets, late answers and abstentions remain in this denominator. Do not score only episodes that triggered an alert or produced a usable trace. Diagnose against the original label even when a follow-up contains a different fault. Repeated alerts for the same original episode are deduplicated; a new affected scheduled original visit receives its own episode ID and retains its shared fault occurrence ID for dependent-data analysis.

| Secondary outcome | How it will be measured |
| --- | --- |
| Detection coverage and delay | Fraction of verified regression episodes alerted, and time from episode observation to alert. Also report fault-onset-to-detection time when onset is known. |
| Diagnostic coverage | Fraction of all verified regression episodes receiving an in-time, within-budget, non-abstaining cause claim. |
| Conditional diagnostic precision | Correct original-cause claims divided by all in-time, within-budget cause claims on verified regression episodes. Report with coverage; if there are no claims, precision is undefined. |
| Misleading diagnosis | Wrong original-cause claims divided by all verified regression episodes; provide a fault-class confusion matrix. |
| Abstention and operational failure | Counts/rates for no diagnosis, missing evidence, timeouts, failed follow-ups, unsupported outputs, buffer loss and exhausted budgets. Record overlapping reasons. |
| False alarms and unsupported diagnoses | Alert rates and cause-claim rates during stable controls and nuisance changes, reported separately per observation and monitoring time. |
| Diagnosis delay and recurrence | Time from original episode observation to diagnosis, plus whether the original fault actually recurred on follow-up. Show unresolved episodes separately from successful-diagnosis times. |
| Monitoring cost and perturbation | Total and per-scheduled-visit resources, instrumentation-induced changes and cost per correctly attributed episode; undefined when no episode is correctly attributed. |

**Analysis.** Report the difference in primary attribution rate between C and B for intermittent faults, with an uncertainty interval and a predefined minimum practically useful difference. Present A and D as additional comparisons and E as a reference. Show site-level results and a declared aggregate weighting so a site with many repeated visits does not silently dominate the conclusion.

Use pilot data to estimate variation across sites, fault occurrences, browser sessions and visits. Select run counts and a cluster-aware or hierarchical analysis that respects these dependencies; do not treat repeated visits as independent websites. A block- or cluster-based resampling method is a candidate, subject to sufficient independent clusters and method appraisal. With too few sites or clusters, narrow the conclusions and emphasize descriptive uncertainty rather than claim population-wide significance. Fix the confirmatory contrast, interval method, significance level if used, multiplicity handling and stopping rule before the main study. Do not stop when a favorable result first appears.

An inconclusive result does not establish equivalence. Report achieved precision, failures and unsupported labels alongside effect estimates. Summarize successful diagnosis times without hiding unresolved episodes. Conduct sensitivity analyses for uncertain labels and failure/missingness patterns; do not impute missing metrics as healthy values.

**Output.** An all-attempt accounting table, primary comparison with uncertainty, confusion matrices, site/condition breakdowns and cost–coverage plots. [Kalibera and Jones](<../Research Papers/T1.4 Statistical Measurement/Papers/Kalibera and Jones 2013 - Rigorous Benchmarking in Reasonable Time.md>) support estimating repetition needs at the actual experimental levels; their benchmark counts are not browser defaults. The [Heričko et al. note](<../Research Papers/T1.3 Synthetic Agents and External Validity/Papers/Hericko et al. 2021 - Towards Representative Web Performance Measurements.md>) likewise does not justify a universal five-run rule.

### Objective 5: Identify when delayed diagnosis is reliable

**Method.** Compare attribution and cost across a small, predefined set of conditions. Fault persistence is the main factor. Follow-up delay and browser-state changes are secondary factors, included only to the extent supported by the pilot budget.

1. **Vary persistence.** Compare faults that remain active with intermittent and one-visit faults. Verify actual recurrence; do not infer it from a repeated slow metric.
2. **Vary follow-up delay.** Choose a feasible short delay and longer operational delays after the pilot. Record both assigned and actual delay, including queueing and failed attempts. Keep the diagnosis deadline common within each comparison and report follow-ups that cannot finish in time.
3. **Vary browser state.** Compare explicitly prepared matched-state follow-ups with controlled cache/session/service-worker changes, one factor at a time where possible. Do not interpret uncontrolled state differences as an isolated cache effect.
4. **Challenge symptom matching.** Include cases where a similar slowdown appears on both visits but the verified cause changes. Check whether the strategy wrongly transfers the follow-up explanation to the original episode.
5. **Map the boundary.** Report attribution differences and uncertainty by condition. A simple condition-by-strategy table or heatmap can show where delayed profiling is adequate, loses evidence, or remains inconclusive. Define adequate reliability using the frozen practical criterion, not a threshold selected after seeing the results.

**Output.** A bounded validity statement and practical guidance on when to use follow-up profiling, retain original evidence or abstain. Limit claims to the tested sites, fault classes, browser versions and synthetic conditions. A controlled localhost result does not establish accuracy for arbitrary production websites or real-user workloads.

### Pilot and main-study sequence

1. **Feasibility pilot:** confirm metric contracts, a small set of independently verifiable faults, legitimate lightweight attribution and useful original-event capture. Inspect perturbation, failures, actual costs and dependence.
2. **Protocol freeze:** record the corpus, eligibility rules, fault taxonomy, split boundaries, randomization, schedules, state policy, delays, budgets, deadlines, run counts, outcome weighting, analysis and retention rules. Appraise the statistical methods actually selected. Keep pilot/tuning observations out of the confirmatory test set.
3. **Main collection:** run the frozen schedule, retain every attempt, and record deviations without silently changing the policy. Evaluate later deployments and the reserved fixture set.
4. **Analysis and reporting:** score locked predictions, report all-episode outcomes and complete costs, examine predefined conditions, and distinguish confirmatory comparisons from exploratory findings.

The [verification queue](<Zotero Verification Queue.md>) tracks the unresolved feasibility and analysis choices. The [Finite Pilot Protocol FP-0.1](<Finite Pilot Protocol.md>) now proposes bounded pilot counts and stopping rules. Its implementation/host checks and a justified main-study sample size remain open.

## Scope and deliverables

The scientific claim concerns synthetic browser measurement and diagnostic reliability. It does not require a human study, a universal anomaly detector or a production always-on service. Keep current CWV and diagnostic definitions distinct, report synthetic INP only when eligible inputs are exercised, label client-observed TTFB accurately, and retain scoped raw measurements alongside any diagnostic score. The recorded TTI omission remains in force.

Engineering duties remain the profiler service/API, seven performance surfaces, metric/network/main-thread/memory/timeline outputs, evaluation and unit tests for URL validation, timing calculations and score generation. The research endpoint can use a smaller metric/fault subset than the complete software feature list. Detailed allocation and prior scope decisions remain in the [archived scope record](<../Research Archive/Scope Resolution.md>).

Research outputs are the episode dataset and manifests, versioned capture configurations, conformance checks, comparison analysis and report. Implementation belongs outside this research-only repository.

## Report structure

**Current requested deliverable:** the [LaTeX research report](<../../docs/README.md>)
uses the requested preliminary pages followed by Introduction, Literature Review,
Research Methodology, Research Work Plan and Conclusion. The submission presents
the proposed study and its evidence base; neither pilot nor main-study results
are available. The six-chapter outline below is retained as an earlier option
for a later empirical report and does not govern the current `docs/main.tex` build.

1. **Introduction:** delayed-diagnosis problem, motivation, question, aim, objectives and contribution boundaries.
2. **Literature review:** metric semantics, instrumentation effects, repeated measurement and the closest diagnosis/monitoring systems; use the [source matrix](<Literature Review and Research Gap Matrix.md>) and [novelty comparison](<Monitoring Novelty Cross Reference.md>).
3. **Methodology:** observation contracts, episode oracle, corpus, capture arms, allocation, budgets, failures, holdouts and analysis assumptions.
4. **Profiler and dataset:** implemented collection pipeline, provenance, fixture verification and reproducibility details.
5. **Results:** detection, original-episode attribution, recurrence, failures, uncertainty and complete costs. Do not populate before experiments.
6. **Discussion and conclusion:** conditions where delayed diagnosis is reliable, unresolved cases, threats to validity and the supported answer to the question.

## Immediate work

The [decision-critical source review](<../Research Archive/Review Artifacts/2026-10-31 Decision-Critical Source Checks/README.md>) now records the five closest-work identities, named paper passage checks and original-visit evidence documentation. WMF's earlier access discrepancy is resolved. LMAT controller details and the unread Shahedi journal edition retain explicit holds; Paradyn is usable with an explicit manuscript citation. The comparison supports a candidate empirical question, not proof of novelty.

The [Finite Pilot Protocol FP-0.1](<Finite Pilot Protocol.md>) now translates the methodology into two fixtures, eight scenarios, 64 matched comparison blocks and explicit visit, time, resource and progression limits. Its numbers are proposed operational choices informed by a [review of Luna web searches](<../Research Archive/Review Artifacts/2026-10-31 Finite Pilot Protocol/README.md>), not established population sample sizes.

Next, complete and check the actual host, versions, fixtures, capture/diagnosis contracts and execution manifest, then address the remaining readiness items in the [verification queue](<Zotero Verification Queue.md>). Confirm useful original evidence before freezing H₁ or the main-study design. A full original trace or JS stack sampler is not assumed. Main-study endpoints, thresholds, budgets, sample size, uncertainty and stopping remain to be frozen separately. The [decision log](<Decision Log.md>) records the draft protocol without claiming pilot execution or gate closure.

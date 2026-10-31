# Finite Pilot Protocol

**Study:** Reliability of Delayed Browser Performance Diagnosis. **Version:** FP-0.1, 2026-10-31. **Status:** proposed protocol for feasibility work; no collection has been run. The software, host and capture manifests must be completed before execution. This document specifies the pilot's limits; it does not freeze the main study or pass G3–G7.

## 1. Purpose and basis

The pilot asks whether the proposed experiment can be carried out with trustworthy labels, useful original-visit evidence and manageable costs. It will check the measurement pipeline, expose failures and inform the main study's design. It will not test H₁ as a confirmatory hypothesis or establish that one strategy is generally superior.

Pilot guidance recommends feasibility objectives, a reason for the sample size and criteria for deciding whether to proceed or amend the study [1–3]. Systems benchmarking adds two important cautions: repetition needs depend on the actual system, and earlier trials can affect later trials [4–5]. Hindsight shows why retained evidence needs a finite capture horizon and explicit loss accounting [6]. These principles inform this protocol; **all numerical limits below are proposed project choices, not published browser standards**. The [review of the Luna searches](<../Research Archive/Review Artifacts/2026-10-31 Finite Pilot Protocol/README.md>) explains the evidence and its limits.

The pilot must answer five questions:

1. Can the harness verify which fault actually ran on each visit?
2. Can A, B and C supply the evidence they claim to collect, with correct visit identity and timing?
3. Does collection change the measured behavior or exceed the resource limits?
4. Can the scheduler, diagnosis rules and complete cost ledger work across persistent, transient and replaced faults?
5. What needs to change before designing the main experiment?

## 2. Fixed scope

Use **two owned localhost fixture templates**, one pinned headless Chromium build, one automation stack and one host. Use a desktop viewport of **1365 × 768**, device scale factor 1, no network throttling and CPU rate 1, except for the named nuisance condition. Mobile, live websites, multiple browsers, human participants, authentication and service workers are outside this pilot. Their omission narrows this feasibility exercise, not the complete engineering deliverables.

| Fixture | Required behavior |
| --- | --- |
| F1: image-led page | A designated image is normally the LCP candidate. It also has a safe button input. |
| F2: script-rendered page | A small script constructs the designated LCP content. It has a different DOM/loading structure and the same kind of safe input. |

Both fixtures must support the same two fault classes and have no external dependencies, cross-origin frames or background polling. Keep their URLs, element identifiers and returned content structure unchanged across fault conditions. Use opaque visit IDs that do not encode the scenario or fault. Do not put fault names in query strings, DOM attributes or policy-visible logs.

**R — delayed resource:** the server holds one designated critical response for an additional **500 ms**. Verify the hold with evaluator-only request ID and start/end logs.

**J — main-thread work:** a designated script performs approximately **500 ms** of work before the LCP content can paint. Verify actual entry/exit and elapsed work using a common evaluator probe. That probe is present in every arm and has its cost measured. Send its records over a separate evaluator channel to storage the policy process cannot read. Audit policy inputs and stored evidence for accidental label/marker leakage; a separate directory name alone is insufficient.

The purpose is to create similar loading symptoms through different mechanisms. Qualification must demonstrate this; the intervention flag alone is insufficient. If a fixture cannot support both mechanisms, apply the bounded repair rule in §9 rather than quietly substitute another site.

### Scenarios and observation unit

| Scenario | Original visit | B follow-up, if triggered |
| --- | --- | --- |
| S0: stable | No fault; CPU rate 1 | No fault; CPU rate 1 |
| S1: nuisance | No software fault; CPU rate 2 | Same declared CPU setting; no software fault |
| S2: persistent R | R | R |
| S3: persistent J | J | J |
| S4: transient R | R | No fault |
| S5: transient J | J | No fault |
| S6: replaced R | R | J |
| S7: replaced J | J | R |

Persistence here is controlled by visit role: each arm receives a separately reset copy of the assigned fault occurrence. This tests the pipeline under known conditions; it does not estimate natural production fault lifetimes. Verify follow-up activity separately. Repeated slow values cannot establish that the same cause recurred.

A **matched block** is one fixture × scenario × repetition, with five separately executed original visits, one per arm. Each original visit has its own episode ID. The five visits share a block ID, not an identical execution. Related observations retain fixture, scenario, occurrence, session and visit IDs.

## 3. Visit and capture contracts

The 30-second visit clock starts at the attempted browser-process launch. Start collection before fixture code executes. Observe each visit for **15 seconds from navigation start**. Attempt the safe button input at **5 seconds**; if unavailable, record an input failure. Freeze the loading endpoint according to the pinned LCP definition and input cutoff. Stop collectors at 15 seconds, flush while the page is available and finish export within the **30-second total visit limit**, including browser startup and cleanup. Failed navigation, export or input is a recorded outcome.

The primary symptom is **LCP**, in milliseconds, for this fixed journey. Record client-observed navigation/resource timings and available attribution. INP and CLS may be recorded to check availability and lifecycle handling, but are exploratory pipeline outputs in this pilot. Missing INP is not zero. TBT, a composite score, memory-growth diagnosis and a full performance-metric validation are outside the pilot endpoint.

| Contract / arm | Evidence and collection rule |
| --- | --- |
| M: minimally observed calibration | A minimal LCP observer, harness timing and the same hidden verification probe, without attribution or rich collectors. It has a nonzero measurement cost. Used for fault qualification and perturbation checks. |
| A: original lightweight attribution | Common metrics and all supported existing `web-vitals` attribution, including useful original-visit resource/LoAF fields when available. Serialize needed values before objects disappear. |
| B: rich follow-up | The same original record as A. Each common alert schedules **one** new rich visit. B can use its original attribution; escalation must not erase that evidence. |
| C: bounded original evidence | A plus an early-start record of supported Resource Timing, long-animation-frame and long-task entries. Keep at most **1,024 entries or 4 MiB of serialized record data**, whichever is reached first. Track eviction and drops with affected time ranges. At 15 seconds, stop and freeze the retained record before finalizing the alert. Export it within the visit deadline; send the audit export to a separate, access-logged store the diagnosis worker cannot read. Release the diagnostic copy only after the common alert. The collector may record before the alert, but the classifier must not read that record early. For this pilot export every C record for conformance auditing and charge every export, including unalerted visits. If required earlier evidence was evicted, the record is incomplete and cannot support that diagnosis. This is a scoped entry record, not a full trace. |
| D: periodic rich originals | A on every original; rich capture on every fourth assigned original for each fixture. Choose a random starting phase before the fault schedule is available to the policy. No extra visit. |
| E: always-rich reference | A plus rich capture on every original, under a separate reference allowance. It supplies neither oracle labels nor evidence to other arms. |

The candidate rich contract uses CDP Network metadata and a trace of main-thread, paint/layout and script execution, with a sampled CPU profile if the pinned build supports the chosen configuration. Omit response bodies, video and heap snapshots. Record the **exact event categories, APIs, sampling settings and buffer options** in the capture manifest; verify them before treating the contract as implemented. Reference `web-vitals` v5.1.0 is already documented in the source appraisal; the actual package version and checksum must be pinned for execution.

Observe browser/API loss signals and application-record drops. A warning-free trace is not proof of completeness. Qualification must include a known event that can be independently matched to the expected timestamp, resource or script. ChromeDriver documents buffer loss [7], but this pilot must test the actual CDP/automation path; it must not assume ChromeDriver's logging behavior applies unchanged.

### Common alert and diagnosis

For each fixture, train once on its first 20 stable A visits. Define:

> Alert threshold = median stable LCP + max(100 ms, 3 × unscaled median absolute deviation).

Use the next 20 stable visits for validation. This is a simple operational threshold, not a significance test or a field CWV threshold. After qualification, lock it for the comparison; do not update it during faults.

Use a small rule-based classifier, frozen after qualification. Begin with two discriminators: a critical-resource phase at least **200 ms above its stable median**, and at least **200 ms of attributable pre-paint main-thread work**. Check availability, overlap and ambiguity in the pinned outputs. If both explanations are supported, neither is supported or the evidence is incomplete, abstain. Record the final field/formula mapping in the manifest before comparison. A must retain any legitimate field that makes these rules possible; C is not entitled to an advantage.

For B, give supported original evidence priority. If only the follow-up supports a class, record that class as an **inferred original cause from a later visit**, so the evaluator can test that transfer. Conflicting original/follow-up evidence is flagged, not silently overwritten. All arms issue cause claims only after the common alert, keeping missed alerts in the denominator. All arms apply the same vocabulary: R, J or abstain; controls also permit “no supported target fault.”

For B, assign a target follow-up delay of **1 or 15 seconds after the original observation window ends**, balanced two/two across the four repetitions of each fixture/scenario. Record the actual delay, including startup and queueing. The assigned delay is a browser-launch target; actual delay to follow-up navigation includes startup and queueing. The common diagnosis deadline is **90 seconds after the original observation window ends**. A missing alert, unsuccessful visit, late diagnosis or abstention is not repaired by further diagnostic visits.

## 4. Finite schedule and sample-size rationale

| Stage | Fixed allocation | Maximum browser starts |
| --- | --- | ---: |
| Warm-up | 2 visits per fixture at the start of each of 3 sessions; retained but excluded from evaluation | 12 |
| Stable history | 2 fixtures × 40 A visits: first 20 train, next 20 validate | 80 |
| Qualification | 2 fixtures × 4 conditions (stable, nuisance, R, J) × 3 contracts (M, C including A, rich including A) × 5 development visits; plus 4 C fault-handling checks per fixture | 128 |
| Perturbation calibration | 2 fixtures × 6 blocks (4 stable, 1 R, 1 J) × 4 contracts (M, A, C, rich) | 48 |
| Frozen comparison originals | 2 fixtures × 8 scenarios × 4 repetitions × 5 arms | 320 |
| B follow-ups | At most one for each of B's 64 originals, including false alerts on controls | 64 |
| **Planned maximum** | Includes all warm-up, preparation and diagnostic visits | **652** |
| Bounded repair reserve | Pre-comparison qualification/calibration repairs only | **48** |
| **Absolute campaign cap** | No additional or replacement visits beyond this limit | **700** |

This gives **64 matched blocks**. Each arm receives 64 original opportunities: **48 assigned regression cases, 8 stable controls and 8 nuisance controls**. Transient cases contribute 16 originals per arm; replaced-cause cases contribute another 16. Counts are assignments, not guaranteed verified/completed observations.

The allocation covers the mechanisms, persistence changes, controls and all five strategies while keeping the work bounded. Four repetitions allow each delay to occur twice and split each cell across two comparison sessions. They do not establish a reliable population error rate. Only two fixture templates are represented; hundreds of visits do not become hundreds of independent websites. No published five-run or native-benchmark rule is used as a sample-size justification [4,8].

Use **three sessions**: preparation/calibration up to 3 hours, then two comparison sessions up to 2.5 hours each on different days. Put repetitions 1–2 in the first comparison session and 3–4 in the second. Complete the campaign within **7 consecutive calendar days from the first warm-up**. Active time includes startup, waits, resets, verification, capture and export. Gaps between sessions count toward the seven days, not the eight active hours.

Within each comparison session, shuffle fixture/scenario blocks and randomize arm order inside each block. Balance B's delay assignments across sessions. Generate D's periodic phase independently of the fault sequence. Save seeds and schedule hashes before comparison; do not expose the evaluator's schedule to policies. Run one browser workload at a time. These controls address order and carryover risks; they do not prove independence [5].

## 5. Resource limits and stopping point

RSS means resident set size: the memory resident in the browser/collector process tree. MiB and GiB are binary storage units. Enforce resource limits with the host watchdog and retain the observed peaks and termination reasons.

| Limit | Proposed cap / response |
| --- | --- |
| Total experiment | Stop at the first of 700 browser starts, 8 active hours, 7 calendar days, or 8 GiB of campaign artifacts. |
| Per visit | 30 seconds elapsed, 30 CPU-seconds for browser + policy collector, and 2 GiB peak process-tree RSS. Terminate the affected visit at a breach and retain the reason. |
| Rich export | 32 MiB per visit; mark truncation/loss rather than silently discard bytes. |
| C entry record | 1,024 entries / 4 MiB serialized data. Account separately for actual runtime memory; serialized size is not heap usage. The 2 GiB process-tree RSS stop is the enforced memory bound. |
| Policy comparison allowance | For each A–D: 3 charged hours, 120 CPU-minutes and 2 GiB cumulative exported evidence, plus the common per-visit limits. E has 3 hours, 120 CPU-minutes and 3 GiB as a reference allowance. |
| Diagnosis / retries | Deadline 90 seconds; at most one B follow-up. No comparison retry or visit-until-recurrence rule. |
| Repair | One documented repair cycle before comparison, at most 48 extra starts, inside every campaign cap. |

A–D receive the same allowance vector, not a claim that their actual costs are equal. During comparison, enforce these policy allowances after debiting each arm for the full shared stable-history cost. Charge original scans, dropped/evicted records, serialization, exports, waits and failed reruns. Qualification and perturbation calibration are development work outside the policy allowances, but inside the campaign caps and reported separately. Charge the full shared stable-history acquisition cost to each arm when reporting its standalone policy cost, while counting those physical visits only once in the campaign ledger. Show both ledgers; do not add CPU-seconds, MiB and elapsed time into a single unexplained score.

If a policy exhausts its allowance, it stops obtaining policy evidence. Remaining scheduled originals are still executed with the minimally observed evaluator harness, subject to the campaign cap. Their verified eligible regressions remain in that policy's denominator as no correct in-time diagnosis. Harness-only evidence stays hidden and is charged separately.

If a **global** cap or integrity stop ends the campaign, do not launch the remaining visits. Mark them not attempted and report the planned and observed counts separately. Do not invent verification labels for them or present a partial campaign as a completed comparison. Budget exhaustion and inconclusive results are legitimate stopping outcomes.

## 6. Qualification and progression criteria

Before comparison, require actual version/build hashes, host specifications and enough available capacity to enforce the caps. Use a new browser process and empty profile per visit, clear fixture/controller state, disable service workers and verify the declared CPU rate. Record host load and previous-run state; browser resets do not clear every host cache.

Qualification's four additional checks per fixture deliberately exercise **buffer overflow, export failure, a trigger delayed to 20 seconds, and absence of the qualifying input**. They test whether failure codes and loss handling work. Expected failures in these checks are reported separately from unexpected failures in ordinary visits. Do not count them as successful normal captures.

For perturbation calibration, randomize the six blocks and contract order inside each block. Give M, A, C and rich separate matched executions and full state resets. Use the four stable blocks per fixture for the stated LCP overhead summary; independently verify fault activity in the R/J blocks for all four contracts, including A. These small samples screen for obvious perturbation and do not establish a universal overhead bound.

Apply these project-defined criteria after qualification/calibration and again after comparison:

| Feasibility criterion | Proceed candidate (green) | Amend (amber) | Stop this version (red) |
| --- | --- | --- | --- |
| Oracle and provenance | Every known-cause score has independent activity verification and correct visit linkage; all assignments, including uncertain labels, remain in accounting; no label leakage. | An uncertain label is isolated and traceable, with a defined repair before comparison. | Wrong visit/source linkage, labels visible to a policy, or oracle cannot distinguish R from J. Stop immediately if discovered during comparison. |
| Fault applicability | For each fixture/class under M: all 5 injections execute; at least 4/5 exceed the alert threshold; median LCP increase is at least 200 ms versus M stable visits. Verify activity under C/rich separately as well. | One mechanism needs the allowed repair and repeat qualification. | Mechanism still fails after the repair or changes the intended endpoint/candidate. |
| Original evidence comparator C | Required resource/main-thread discriminators are present, correctly scoped and exportable in all ordinary C qualification cases; frozen rules distinguish each class in at least 4/5 per fixture. Rich fault cases separately check its discriminator mapping. | A capture configuration needs repair within the reserve. | C cannot record a useful original discriminator within its cap. Narrow the arm or revise the question in a new protocol. |
| Entry continuity | No loss of required records in ordinary C visits; injected overflow/export failures are detected. | Any signalled required-evidence loss, with a specific capture repair for the next version. The affected visit remains a failed diagnostic opportunity. | Silent loss, wrong linkage, or a collector that cannot identify incomplete records. End the campaign if shared record integrity is unreliable. |
| Operational completion | All cells attempted; each arm completes/export-valid evidence on at least 58/64 originals (≥90%); required cause labels verified on at least 46/48 assigned fault cases. | At least 48/64 operationally complete and 39/48 verified, with a specific feasible correction. | Lower counts, an unattempted design cell or no credible bounded repair. |
| A/C perturbation | Against M, stable median LCP increase is no more than max(25 ms, 10% of M median) for both fixtures; fault identity/activity unchanged. | Increase is above green but no more than max(60 ms, 25%), or unstable estimates need a redesigned calibration. | Larger change or instrumentation alters which mechanism executes. Rich-reference overhead is reported separately. |
| Resources and completion | Fixed schedule finishes inside caps; no undisclosed policy evidence or cost. | Cap exhaustion is understood and a smaller/larger-cost design can be justified prospectively. | Required comparison cannot fit the available resources, or records/costs cannot be reconstructed. |

These are engineering progression rules, not confidence bounds or statistical acceptance tests. Small counts and shared state can make a green result fragile. Signalled strategy-specific loss is a failed observation and does not itself invalidate the oracle or require cancelling other arms. Shared label leakage, wrong visit linkage or untrustworthy records are campaign-wide integrity stops. Any integrity red overrides other colors. Overall amber requires a specific amendment; **green means prepare the main-study protocol**, not automatic permission to collect main-study data. C outperforming B is not a progression requirement. If A already diagnoses all selected causes, retain that finding and reconsider whether richer collection adds value.

## 7. Outcomes and analysis

Keep a complete attempt ledger with stage, block/occurrence, fixture, arm, visit role, state, actual timings, fault verification, loss/missingness, evidence hashes, diagnosis and cost. Freeze predictions before joining hidden labels. Eligibility follows the prequalified fault case and independent execution/applicability checks, not an alert, observed slow value or successful trace. Keep uncertain labels visible but separate from known-cause scoring.

Report correct original-cause attribution over **all verified eligible original regression episodes**, including missed alerts, failed follow-ups, missing evidence, late answers, exhausted policies and abstentions. Also report coverage, wrong attribution, stable/nuisance false alarms, recurrence, actual follow-up delay and resources. Give both assigned counts and verified denominators so oracle failures cannot disappear. Also report an assignment-based sensitivity range: for each arm, divide known correct cases by all 48 assigned fault opportunities for the lower bound; for the upper bound add only cases whose eligibility/label is unresolved. Unattempted cases after a global stop are shown separately, and that campaign remains incomplete. Compare C and B under the corresponding worst/best combinations; these are descriptive missing-label bounds, not confidence intervals.

Present counts and rates by fixture, scenario, arm and session. Show the descriptive C–B difference for transient cases and separately for replacement cases; do not merge them without labelling. Summarize timings/costs with median, range and observed variation across blocks/sessions. Check ordering/drift plots. Do not conduct an efficacy significance test or a two-fixture cluster bootstrap and label it population uncertainty.

Use the pilot to list the observed dependence levels, plausible costs and a **range** of main-study sample-size scenarios. The main study still needs a practical effect/precision target, more defensible independent-unit coverage and a separately appraised interval/stopping method. Do not power it from a single favorable pilot effect estimate [2,4]. Pilot observations, including repairs, stay out of the main confirmatory dataset.

## 8. Evidence retention and pilot outputs

Keep raw policy evidence and evaluator labels in separate directories/access paths. Preserve all failures and an append-only manifest with hashes. Under the 8 GiB cap, retain raw pilot artifacts for **90 days after the pilot report is signed off**; retain the de-identified ledger, configurations, derived tables and hashes through project assessment. Record actual storage/deletion actions when due; this document does not schedule them. Do not delete evidence mid-campaign to make a failed cap appear satisfied.

Allow at most **6 analyst-hours within 2 calendar days of the collection stop** for the pilot readout. If the analysis cannot be completed within that limit, record it as incomplete and list the unresolved work; do not extend collection.

Deliver: the run/cost ledger; versioned fixture and capture manifests; conformance/loss checks; per-cell outcome tables; perturbation and cost summaries; deviations; and a signed **stop / amend / prepare main study** decision with reasons. Report source and implementation limits alongside results.

## 9. Change control and execution record

Before first collection, fill the execution record with the host/OS/RAM/CPU, browser and automation versions, package checksums, fixture commits, exact capture fields/categories, clock alignment, diagnosis mapping, seeds, storage location, start date and accountable researcher. Verify the existing evidence/contract/readiness requirements in the [queue](<Zotero Verification Queue.md>). No version or resource availability is inferred from writing this file.

One pre-comparison repair cycle is allowed. State the failure, change and affected cases; the only permitted severity increase is **500 to 1,000 ms** when qualification fails to produce the intended symptom. Recheck the affected cases within the 48-start reserve; count the original failed attempts. If repair needs a new fault class, fixture, detector, capture mechanism or larger budget, stop FP-0.1 and write FP-0.2 prospectively. Comparison results cannot be used to tune the same comparison. A shared integrity problem after comparison starts ends that version; preserve it as partial/incomplete. An honestly detected arm-specific timeout, overflow or missing record remains an outcome under the frozen rules; continue other scheduled work if shared integrity and campaign caps allow it.

## References

1. Eldridge et al. (2016). *CONSORT 2010 statement: extension to randomised pilot and feasibility trials*. Pilot and Feasibility Studies 2, 64. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC5154046/). Items 6c/7a and Comment: objectives, number rationale and progression. Clinical reporting guidance adapted here; no clinical sample sizes transferred.
2. Thabane et al. (2010; corrected 2023). *A tutorial on pilot studies: the what, why and how*. BMC Medical Research Methodology 10, 1. [Full text](https://link.springer.com/article/10.1186/1471-2288-10-1). Sample Size and Criteria for Success: purpose, stop/amend decisions and caution in using pilot estimates. No numerical example adopted.
3. Moore, Carter, Nietert and Stewart (2011). *Recommendations for Planning Pilot Studies in Clinical and Translational Research*. Clinical and Translational Science 4(5), 332–337. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3203750/). §3: align numbers with aims, practical cost and risks. Transfer is methodological only.
4. Kalibera and Jones (2013). *Rigorous Benchmarking in Reasonable Time*. [Local version/appraisal](<../Research Papers/T1.4 Statistical Measurement/Papers/Kalibera and Jones 2013 - Rigorous Benchmarking in Reasonable Time.md>); [author manuscript](https://kar.kent.ac.uk/33611/45/p63-kaliber.pdf). Locally checked typeset PDF §§9.3/12: dimensioning depends on the configuration; do not transfer repetition tables. No native-workload inference formula adopted here.
5. Duplyakin et al. (2023). *Avoiding the Ordering Trap in Systems Performance Measurement*. USENIX ATC, 373–386. [Paper](https://www.usenix.org/system/files/atc23-duplyakin.pdf). §3, PDF 4–5: ordering and reset procedure; no ordering-test algorithm or server effect size transferred.
6. Zhang et al. (2023). *The Benefit of Hindsight: Tracing Edge-Cases in Distributed Systems*. NSDI, 321–339. [Paper](https://www.usenix.org/system/files/nsdi23-zhang-lei.pdf). §§3–4/7.3: retention horizon, overwrite and loss. Distributed-system capacities are not browser buffer prescriptions.
7. Chromium authors. *ChromeDriver: Performance log*. [Official documentation](https://developer.chrome.com/docs/chromedriver/logging/performance-log), accessed 2026-10-31. Tracing/buffer warnings illustrate loss handling; actual pilot collector support must be tested.
8. Heričko, Šumak and Brdnik (2021). *Towards Representative Web Performance Measurements with Google Lighthouse*. StuCoSReC, 39–42. [Source note](<../Research Papers/T1.3 Synthetic Agents and External Validity/Papers/Hericko et al. 2021 - Towards Representative Web Performance Measurements.md>); [DOI](https://doi.org/10.18690/978-961-286-516-0.9). §§3–5 concern Lighthouse-score repetition in a small historical setup, not a universal five-run rule or diagnostic pilot size.

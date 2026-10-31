# Continuous Website Performance Monitoring Research Direction

**Prepared:** 2026-10-31. **Status:** revised candidate framing in response to the researcher's requested direction; question, algorithms and study parameters remain provisional.

The individual research can stand as a study of **website-specific performance baselines and diagnostic reliability**. Repeated browser measurements build a history of each tested website under declared conditions. That history helps identify unusual changes and decide when a more expensive diagnostic capture is justified. The scientific outcomes are detection reliability, diagnostic attribution, measurement perturbation and monitoring cost. The study's motivation and conclusions do not depend on any particular downstream application.

**Evidence-adjusted candidate:** the [local-paper and current-solution cross-reference](<../Research Management/Monitoring Novelty Cross Reference.md>) finds strong prior art for the broad adaptive loop. The strongest remaining question concerns whether a new detailed visit can faithfully diagnose an earlier intermittent regression, compared with legitimate original-visit attribution, bounded recorded evidence and budget-matched scheduled capture. The broader system design below is useful infrastructure; it is not itself an established novel method.

## Proposed title and research question

**Working title:** Reliability of Delayed Browser Performance Diagnosis.

**Primary question:** For persistent and intermittent website performance regressions, when does a detailed follow-up visit identify the independently verified cause of the original anomalous visit, compared with retaining original-visit evidence under matched total monitoring costs?

**Hypothesis to test:** The reliability of a fresh diagnostic visit depends on fault recurrence and state continuity; original-visit evidence may avoid incorrect links between an earlier symptom and a later cause, at a continuous collection cost. The study must permit no meaningful difference or superiority of a simple fixed-capture schedule. Building a monitoring dashboard or saving a history is an implementation contribution; the question above needs comparative experimental evidence.

## Revised options 1 and 2

| Option | Research focus | Contribution to investigate | Evidence needed |
| --- | --- | --- | --- |
| **1. Reliability of delayed diagnostic capture** | Use site/condition history for detection, then compare a fresh detailed visit with available evidence retained from the original visit. | A measured validity/coverage boundary and, if justified, an improved capture decision under total cost constraints. | Persistent/intermittent episodes, original/follow-up fault verification, existing lightweight attribution, feasibility-gated original-event buffers and budget-matched fixed/random capture. |
| **2. Longitudinal benchmark for diagnostic reliability** | Combine each site's measurement history with independently labelled controlled changes and evidence linked to each visit. | A reproducible dataset/protocol showing detection, original-episode attribution, recurrence, missing evidence and misleading follow-up diagnoses. | Stable periods, graded single-fault variants, same-symptom/different-cause cases, negative controls, distinct held-out deployments/templates and recorded failures. |

Option 1 is the provisional primary study. Option 2 supplies its evaluation foundation and can become the narrower primary contribution if a distinct adaptive policy cannot be justified. This is one coherent programme of work rather than a requirement to invent two algorithms.

## What continuous monitoring means

The feasible initial interpretation is a **bounded experimental campaign of scheduled and deployment-triggered synthetic testing of authorized live URLs**. Interval, duration, retention, worker infrastructure and target access remain feasibility choices; an always-on production service is not an existing allocation or a prerequisite to this study. Each observation executes a fixed navigation and defined safe inputs using a declared browser/profile/state. The result is an ongoing series of samples; activity between samples is unobserved. A permanently open page measures a different lifecycle and state from repeated fresh visits, so it must not be substituted silently.

Real-user monitoring would require a separate collection design and access to the site's user-side instrumentation. The existing navigation-plus-fixed-input study can proceed conceptually without it. “Live” describes the target, not representative coverage of all users, visits or interactions. A detected change can request a richer *new* run, but that rerun cannot reconstruct the precise activity of the earlier lightweight visit.

The candidate measurement loop is:

1. Execute a bounded lightweight scan using the declared journey/profile/state.
2. Compare the result with past measurements from the same comparable condition.
3. Classify the observation as comparable, unavailable, failed or changed; preserve its raw values and provenance.
4. When a predeclared trigger and resource budget permit, repeat or escalate to selective CDP/trace capture.
5. Produce a diagnosis with supporting evidence and record the total cost of the initial scan, confirmation runs and richer capture.

Controlled intervention labels establish which regressions the trigger missed. Scheduled reference captures among non-triggered cases can estimate missed diagnostic opportunities, but those captures can also fail and are not independent fault truth. Evaluating only escalated cases would hide missed changes and inflate apparent diagnostic quality.

## Dataset customized to each website

A website is not one homogeneous workload. The basic analysis unit should identify **site, URL or journey, deployment/version, browser build, device/network profile, browser state and observation window**. Cache state, viewport, interaction sequence or reference-version changes can require separate baseline strata or explicit context adjustment.

Customization need not mean training a separate machine-learning system for every website. A shared method with site/condition-specific baseline parameters is a simpler starting point. The dataset must support both website characterization and evaluation of the profiler's diagnostic reliability; those are different uses of the same measurements.

| Dataset component | Example fields | Purpose |
| --- | --- | --- |
| Identity and time | Site/page/journey ID, timestamp, deployment/content version, fixture lineage. | Distinguish a repeated observation from a new workload or deployment. |
| Conditions | Browser/profiler build, host, viewport, CPU/network settings, HTTP cache, service-worker/session state, safe-input script and observation window. | Identify comparable runs and condition changes. |
| Measurements | LCP, applicable synthetic INP, CLS, TTFB, transfer bytes, requests, main-thread/long-task activity, scoped memory/DOM values. | Characterize the observed workload using versioned output contracts. |
| Collection quality | Capture tier, availability/missingness reasons, intervention success, navigation/capture failures and retained run order. | Keep missing data and selective failure from looking like improvements. |
| Diagnostic labels | Stable control, deliberately introduced fault class/intensity, independently verified execution, nuisance-condition change; unknown where unverified. | Assess detection and attribution without using the profiler's own diagnosis as ground truth. |
| Resource cost | Wall-clock duration, browser-process time where defined, request/transfer load, trace size, retries and deep-capture frequency. | Compare complete monitoring policies fairly. |

Two connected datasets serve different roles. **Natural live-site histories** describe variation, data availability and operational robustness. **Controlled deployments or fixtures** provide verified fault labels and stable controls for correctness tests. Public-site changes observed in the wild remain unlabelled unless corroborated; a release marker or slow run alone does not establish its cause.

Candidate interventions include larger image payloads, a controlled expensive input handler, a delayed designated request, eligible delayed layout shifts and changes in request fan-out. Include same-payload/different-computation cases to test whether runtime diagnostics add information beyond transfer-size monitoring. Verify the injected mechanism and metric eligibility; an exact timing response is not known merely from the source change. Keep multiple-fault challenges distinct from single-fault calibration.

Website-specific history improves knowledge of what is usual for the tested condition. **It does not automatically establish what is acceptable, what caused a change, or whether the diagnosis is correct.** Keep absolute reference/quality thresholds alongside relative change signals so an already slow website is not treated as satisfactory because it is consistently slow.

## Comparative study and evaluation

Use a small primary metric/fault subset for the research endpoints while retaining the wider profiler outputs as engineering deliverables. Predeclare common fault opportunities, diagnostic labels, evidence thresholds and attribution scoring across all compared strategies.

| Comparison | Question isolated |
| --- | --- |
| Fixed thresholds with fixed lightweight capture | What does a simple, reproducible monitoring baseline achieve? |
| Website-specific history with the same lightweight capture | Does site-specific context improve change detection, independently of extra instrumentation? |
| Website-specific history plus triggered diagnostic capture | Does selective richer capture improve independently verified diagnosis for its added cost? |
| Periodic rich capture and always-rich capture | Does escalation allocate a limited capture budget better than a fixed schedule, and what diagnostic coverage does the tested rich configuration provide? |

Compare at equal total budgets where feasible and report the full cost/diagnostic frontier where they cannot be matched. Include startup/history-collection cost, failed attempts, confirmations and reruns. Detection delay is measured from the verified change onset in the controlled sequence; attribution is scored against the intervention class. False alarms require independently stable or labelled nuisance periods, and missed regressions require observation beyond the triggered subset. Report eligible-opportunity, all-attempt and elapsed-time denominators explicitly.

Evaluate chronologically: fit the baseline on earlier designated stable data, tune only in a development period, and test on later unseen deployments. Keep distinct fixture templates/instances held out before tuning and stratify by fault class. A random split of repeated visits to the same deployment leaks information. An additional held-out-site test can assess portability separately from personalization to a known site.

Do not let the baseline automatically absorb a persistent regression as a new healthy state. Specify update/freeze/reset rules, version changes and a cold-start fallback. Examine dependence, recurring variation and repeated testing across metrics and time before adopting an alarm threshold or confidence procedure. An isolated per-test p-value is not a guaranteed long-term false-alarm rate.

## Coverage of the existing six research topics

| Topic | Role in the revised question |
| --- | --- |
| T1.1 Metric semantics | Define comparable outputs, windows, attribution and missingness. |
| T1.2 Browser instrumentation | Choose lightweight/rich capture and quantify incremental effects. |
| T1.3 Synthetic agents and external validity | Specify journeys, state and profiles; bound transfer from synthetic observations. |
| T1.4 Statistical measurement | Estimate normal variation, repeated-measure uncertainty, drift and alarm behaviour. |
| T1.5 Profiler validation | Separate conformance, change detection and correct diagnostic attribution. |
| T1.6 Experimental design | Separate labelled interventions from live histories, control confounding and preserve held-out evaluation. |

## Existing solutions and remaining novelty test

Continuous monitoring, historical baselines and regression alerts are established capabilities. Sitespeed.io documents saved-baseline statistical regression comparison; SpeedCurve documents absolute and relative-change budgets, contextual filters and alert persistence; Calibre documents separate budgets for different test profiles. Lighthouse CI provides assertions, repeated audits and historical comparisons. These tools are direct comparisons, not evidence of an absent solution. [Sitespeed.io Compare](https://www.sitespeed.io/documentation/sitespeed.io/compare/), [SpeedCurve budgets](https://support.speedcurve.com/docs/performance-budgets-and-alerts), [Calibre budgets](https://calibreapp.com/docs/synthetic/budgets), [Lighthouse CI configuration](https://github.com/GoogleChrome/lighthouse-ci/blob/main/docs/configuration.md), accessed 2026-10-31.

The [expanded closest-work comparison](<../Research Management/Monitoring Novelty Cross Reference.md>) adds Paradyn, Vesper, WebREC, LMAT, Hindsight, WMF and trace-optimization research. Adaptive depth and original-event preservation are already established. The possible remaining contribution concerns **original-episode attribution when diagnosis is deferred to a separate browser visit**, compared with retaining available original evidence at matched cost. A full-cost empirical validity boundary is a plausible output even without a new adaptive algorithm; novelty remains provisional.

## Independent deliverables

The study would deliver the profiler service and required performance interfaces, a versioned website-history schema, reproducible controlled changes, a longitudinal dataset, evaluated monitoring policies and a report of supported conclusions and limits. A generic API exposes raw metrics, conditions, diagnosis evidence, uncertainty and collection costs for later reuse. No application-specific outcome is required to evaluate the research.

The current task refines a research direction. It does not start a monitoring service, collect user telemetry, alter target websites or freeze study parameters. Implementation remains outside the research-only repository. Existing evidence, requirements and historical decisions remain traceable through the [progress review](<Research Progress and Independent Contribution Review.md>), [source comparison table](<Research Source Comparison Table.md>) and [verification queue](<../Research Management/Zotero Verification Queue.md>).

# Phase 0 — Tier-1 Evidence Synthesis

**Status:** Active

**Updated:** 2026-10-08

**Scope:** Research management for the individual browser-performance profiler component. This file records evidence state and reasoning; it does not select the research gap, research question, hypothesis, final objectives, final methodology, architecture, statistic, or score.

## 1. Evidence status

The six Tier-1 Deep Research reports are present locally:

1. [[../Research Papers/T1.1 Metric Semantics/T1.1 Metric Semantics|T1.1 Metric Semantics]]
2. [[../Research Papers/T1.2 Browser Instrumentation/T1.2 Browser Instrumentation|T1.2 Browser Instrumentation]]
3. [[../Research Papers/T1.3 Synthetic Agents and External Validity/T1.3 Synthetic Agents and External Validity|T1.3 Synthetic Agents and External Validity]]
4. [[../Research Papers/T1.4 Statistical Measurement/T1.4 Statistical Measurement|T1.4 Statistical Measurement]]
5. [[../Research Papers/T1.5 Profiler Validation/T1.5 Profiler Validation|T1.5 Profiler Validation]]
6. [[../Research Papers/T1.6 Experimental Design/T1.6 Experimental Design|T1.6 Experimental Design]]

These reports are **secondary synthesis and discovery material**. Their embedded `cite...` markers are not thesis-ready citations. Zotero searches have confirmed the presence and metadata of several priority sources, but claim-level verification requires reading the original records or papers and recording what each source actually supports.

The project proposal and `My tasks.pdf` remain requirements/context documents, not literature evidence. The proposal governs group context; `My tasks.pdf` governs individual scope. Direct conflicts require explicit human resolution.

## 2. Cross-theme synthesis

### 2.1 Measurement is multidimensional, not one scalar construct

T1.1 establishes the strongest common foundation: a profiler observes specified browser events, counters, state, and derived algorithms under declared conditions. LCP, INP, CLS, FCP, TBT, Speed Index, TTFB, trace categories, memory values, DOM counts, and transfer-size fields are not interchangeable simply because several use milliseconds or are presented by the same tool.

The current taxonomy should remain separated into:

- user-facing outcome indicators;
- visual-loading/progression indicators;
- responsiveness and main-thread diagnostics;
- client-observed network measurements;
- browser/resource state measurements; and
- versioned derived scores or classifications.

The practical consequence is that every future measurement contract must state the construct, source, lifecycle boundary, aggregation, scope, and version. “Normalized” may mean unit/schema normalization; it must not erase semantic differences.

### 2.2 Instrumentation is a measurement condition

T1.2 shows that Web Performance APIs, PerformanceObserver, CDP, Chromium tracing, Puppeteer, and Lighthouse occupy different abstraction and observation planes. Puppeteer is primarily orchestration, while Lighthouse combines collection and post-hoc interpretation. A trace is richer but is not automatically more valid, and page-level observers or trace serialization can alter the workload.

The reports converge on a tiered principle rather than a final architecture:

- collect low-overhead standardized entries and selective CDP metadata broadly;
- reserve expensive traces, screenshots, heap snapshots, and detailed profiles for justified diagnostic or validation conditions;
- separate collection, workload modification, and post-processing;
- measure instrumentation tiers against a minimally instrumented condition; and
- attempt correction only if an out-of-sample model demonstrates transferable benefit.

There is no universal constant called “CDP overhead” or “trace overhead.” Workload, event rate, serialization, sampling, browser version, host, and enabled categories all matter.

### 2.3 Synthetic agents can be field-informed without becoming RUM

T1.3 resolves the terminology issue. A browser controlled by a script remains synthetic, even when its configuration is derived from RUM or when it visits a genuine production URL. Such a run can have production-system realism and controlled-condition realism without automatically having field-population representativeness.

The three realism dimensions should remain explicit:

1. controlled-condition realism;
2. real-network/server realism; and
3. field-user/population realism.

RUM-informed parameters can improve the first two dimensions' relevance, but independently selected p75 values can create combinations that do not occur jointly in the field. Profile-definition validity and profile-execution validity are different claims. Browser state must also be represented as a vector: HTTP cache, service workers, Cache Storage, cookies/storage, history/navigation state, connection state, and related conditions.

### 2.4 Repeated measurements should preserve distributions until the estimand is known

T1.4 treats the outcome as a conditional distribution \(F_C\), where the complete condition includes URL/version, browser, host, state, network, time, protocol, and measurement settings. This is a provisional statistical stance, not a final reporting choice.

The reports support the following guardrails:

- mean, median, percentiles, spread, skewness, and confidence intervals answer different questions;
- p95 is not a universal default and is information-poor at small run counts;
- fixed repetition counts should not be selected by convention;
- sequential stopping requires calibrated fixed-width procedures or confidence sequences, not naïve repeated CI peeking;
- cold observations must not be discarded automatically as warm-up;
- failures must be classified as valid operational outcomes, protocol failures, or profiler failures;
- dependence, drift, and state carryover must be diagnosed; and
- repeated runs within one site/condition are not independent websites.

The distribution-first position is adopted provisionally. The primary statistic remains open until the research question and estimand are approved.

### 2.5 Validation requires converging evidence

T1.5 distinguishes construct validity, same-artifact computational conformance, independent matched-run agreement, within-tool repeatability, reproducibility across legitimate environment changes, and sensitivity to known perturbations.

DevTools and Lighthouse are reference implementations, not automatic ground truth. They also share Chromium/CDP/tracing infrastructure with a custom profiler, so agreement is partly compatibility evidence rather than independent triangulation. Correlation may be descriptive but cannot establish agreement. A metric-specific measurement contract must precede numerical comparison.

Controlled fixtures with independently known perturbations can reduce dependence on the reference tool. Dose-response variants for payload, main-thread work, layout shifts, or DOM size can test directionality, sensitivity, and detector performance. These tests still do not establish a universal scalar truth.

### 2.6 Controlled fixtures and live URLs have different inferential roles

T1.6 provides methodological support for a hybrid evaluation candidate:

- controlled fixtures support causal sensitivity, attribution, calibration, and reproducibility;
- live URLs expose production infrastructure, third parties, real deployment complexity, and ecological failure modes.

The two corpora must not be pooled as if they support the same claim. Fixture baselines and perturbed variants support treatment/control language; a live page is normally an observational workload, not a control group. Website count and run count estimate different variance components. Site and agent are usually crossed factors, with runs nested inside site × agent × condition × time block.

Live-site categories such as “image-heavy,” “JavaScript-heavy,” and “poorly optimized” require independent operational definitions. The category must not be defined by the profiler and then used to validate the profiler.

## 3. Agreements across reports

The following are sufficiently supported as working principles, subject to original-source verification:

1. Same metric names do not guarantee same measurands across APIs, DevTools, Lighthouse, synthetic runs, and field aggregates.
2. Synthetic testing is not RUM; RUM-informed configuration remains synthetic.
3. Production targets provide system realism, not automatic user-population representativeness.
4. Instrumentation can perturb execution and must be minimized and characterized.
5. Repeated browser measurements are variable, potentially skewed, state-dependent, and dependent over time.
6. The estimand determines which summary statistic and uncertainty method are appropriate.
7. Correlation alone is not a method-agreement or validation criterion.
8. DevTools and Lighthouse are useful references but are not unquestionable truth sources.
9. Controlled perturbations provide evidence complementary to reference-tool comparison.
10. Raw runs, provenance, failed attempts, and exclusion reasons should be retained before aggregation.
11. Reproducibility requires browser, host, state, profile, target, timing, and tool-version metadata.
12. A universal composite score is not justified without a declared decision purpose, metric semantics, normalization, weights, and thresholds.

## 4. Persistent tensions and contradictions

These are not to be forced into consensus:

| Tension | Current interpretation | Decision deferred until |
| --- | --- | --- |
| Rich trace evidence vs observer effect | Rich tracing may improve attribution while reducing neutrality. | Metric requirements and overhead pilot |
| Production realism vs internal validity | Live URLs increase realism and nuisance variation simultaneously. | Approved inferential target and corpus design |
| Same trace vs independent runs | Same traces test computational conformance; independent runs test operational agreement. | Validation objectives |
| Headless vs headed | Unified Headless reduces architectural differences but does not prove metric equivalence or equal served content. | Target metric/mode pilot |
| Cold vs warm | Both can be legitimate states; “warm-up” is not a universal discard rule. | Estimand and state protocol |
| Percentile vs confidence interval | A percentile describes a distribution; a CI describes estimator uncertainty. | Estimand |
| Score requirement vs multidimensional performance | A transparent decision aid may be possible; a universal performance quantity is not assumed. | Stakeholder purpose and scoring evidence |
| Metric standardization vs construct validity | Standardized signals can be useful without fully representing QoE. | Claim scope and evaluation design |

## 5. Open gates — no final selections yet

The following remain deliberately unresolved:

- primary estimand and headline statistic;
- repetition count or stopping rule;
- serial-dependence treatment and warm-up/state protocol;
- comparable metric set and metric contracts;
- instrumentation tier(s) and overhead model;
- headless/headed condition;
- SPA lifecycle, interaction protocol, and soft-navigation scope;
- live-corpus frame, fixture set, category definitions, and sample sizes;
- agreement/tolerance criteria;
- score purpose, model, and whether a scalar is defensible;
- research gap, question, hypothesis, aim, objectives, final methodology, and architecture.

## 6. Phase 0 exit criteria

**T1.1 checkpoint (2026-10-08):** Phases A and B covered all 20 records in the `1. Metric definitions` collection, and Phase C compared four candidate problem areas in [[T1.1 Candidate Gap Assessment]]. This satisfies a *local comparative checkpoint*, not the Phase 0 exit gate: individual W3C specifications/current implementations, adjacent overlapping studies, T1.2–T1.6 sources and approval of requirements conflicts remain outstanding. No candidate was selected or established novel.

Phase 0 is not complete until:

1. Priority original sources have been read and claim-level support is recorded.
2. Report-derived claims are marked confirmed, qualified, contradicted, or unsupported.
3. T1.1–T1.6 evidence is represented in a source-level evidence map.
4. Multiple candidate problem areas have been evaluated without prematurely selecting one.
5. Any requirements/evidence conflict is recorded for approval rather than silently resolved.

## 7. Next actions

1. Read the P0 Zotero queue in order, beginning with metric specifications and tool semantics.
2. Record claim-level verification results in [[Zotero Verification Queue]].
3. Build the source-level evidence map from verified original records, not from report citation markers.
4. Reassess candidate problem areas only after the verification gate.
5. Keep implementation outside this research directory; this workspace records requirements and research reasoning only.

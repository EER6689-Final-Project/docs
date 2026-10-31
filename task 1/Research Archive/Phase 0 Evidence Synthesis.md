# Phase 0 — Tier-1 Evidence Synthesis

**Status:** Active

**Updated:** 2026-10-26 (T1.6 integration of 2026-10-25 source checks; scope acceptance handled separately)

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

Existing source notes and the [matrix](<../Research Management/Literature Review and Research Gap Matrix.md>) record bounded T1.1–T1.6 claim review, not metadata alone. T1.2 reports 35 processed parent records with access limits, not a fully-read total. T1.3: 24 records / 23 substantive sources / 21 new rows + two cross-references + one prompt. T1.4: 29 records / 22 works / 19 rows + three cross-references. T1.5: 32 records / 30 works / 22 rows + seven cross-references + implementation provenance. T1.6 integration: 16 seeds + four NIST documents + distinct Tranco service = 21 reviewed works, 16 new notes/rows + five canonical reuses/references, nine original PDFs, 27 claim/QC mappings. Its 24-parent collection resolves to 21 candidate identities, a different set from the reviewed portfolio; five additional documents remain target-check leads. Counts do not establish independent corroboration, whole-paper reading or uniform confidence. See [T1.6 inventory](<T1.6 Source Inventory.md>).

The T1.2 individual W3C specification, CDP-domain, Lighthouse variability/throttling and Mytkowicz 2007 notes supersede blanket “unread” labels; T1.5 VIM entries support terminology. Draft/API contracts and mutable engineering guidance are not observed accuracy/completeness or browser overhead results. Bland–Altman, Lin, Carstensen and Zou are located but abstract-limited. The initial 2026-10-25 reconciliation itself made no new rechecks; later same-day T1.6 sourcework did, now integrated with AI self-audit limits and no independent human scientific review.

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

T1.6's source-grounded integration qualifies the following hybrid evaluation candidate (C-006; atomic claims in queue); the corpus-role distinction is researcher inference from historical predecessors, not an already validated modern protocol:

- controlled fixtures support causal sensitivity, attribution, calibration, and reproducibility;
- live URLs expose production infrastructure, third parties, real deployment complexity, and ecological failure modes.

The provisional design implication is to keep the corpora's inferential roles separate. SPDY uses custom clients and modeled dependencies, Mahimahi's 500-page corpus differs from its 20×25 live comparison, and Polaris changes its completion endpoint. Jueckstock supplies a historical synchronized crossing with partial/fatal/complete-success distinctions; Zeber's selected privacy comparisons do not validate timing or representative users. NIST supplies restricted design terminology/guidance; canonical native/Java repetition methods warn about dependence and configuration transfer. A fixture contrast, live workload, crossing and nested repeats still require the actual estimand, independently known effects, units, allocation and uncertainty. No selected browser count/model follows.

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
- detailed lifecycle/window/frame and interaction contracts within approved navigation + fixed-input scope; soft-navigation metrics remain version-gated exploratory;
- live-corpus frame, fixture set, category definitions, and sample sizes;
- agreement/tolerance criteria;
- score model, weights/calibration, severity, missingness and evidence for the approved diagnostic-prioritization purpose; no universal UX/energy/carbon claim;
- research gap, question, hypothesis, aim, objectives, final methodology, and architecture.

## 6. Phase 0 exit criteria

**Historical T1.1 checkpoint (2026-10-08):** Phases A/B covered 20 records and Phase C compared four candidate areas in [[Candidate Gap Assessment#historical T1.1 comparison — 2026-10-08]]. This was a local checkpoint, not Phase 0 exit; later reviews and the fifth statistical candidate do not retroactively change it. A separate current five-candidate planning comparison is now recorded in [[Candidate Gap Assessment]]. Heričko/Hantke and Demir have bounded checked claims; T1.6 coverage is integrated and accepted with qualifications at Q-120. Scope is approved for bounded planning; versions, methods, budgets and permissions remain later conditions. Closest-solution, eligibility/identity and citation review remains open. No candidate is selected or established novel.

**Current gate snapshot (2026-10-26):** G0 is **satisfied procedurally** (PREP-003). G1 is **qualified/deferred: bounded source coverage accepted** after prospectively manifested V-T16-002/Q-120 rechecked 27/27 retained claims (20 pass/7 current-web-state-qualified; none blocking within those bounds). DEV-T16-001, lost raw audit captures, metadata uncertainties and unverified historical webpage state remain disclosed; no modern-protocol validity is inferred. G2 is **satisfied for bounded candidate planning** by actual user choices/ownership (APP-001), not unspecified methods/versions/budgets/site permissions. G3/G4 remain **open**: 838 discovery occurrences have unvalidated producer triage and incomplete canonical eligibility/identity/citation review; corrective batches are separate work, not completed screening by assertion. G5–G7 remain open; no contribution selection, contracts or pilot freeze. The [queue](<../Research Management/Zotero Verification Queue.md>) owns live states. Phase 0 remains active.

Phase 0 is not complete until:

1. Priority original sources have been read and claim-level support is recorded.
2. Report-derived claims are marked confirmed, qualified, contradicted, or unsupported.
3. T1.1–T1.6 evidence is represented in a source-level evidence map.
4. Multiple candidate problem areas have been evaluated without prematurely selecting one.
5. Any requirements/evidence conflict is recorded for approval rather than silently resolved.

## 7. Next actions

1. Maintain accepted [Evidence Review Protocol](<Evidence Review Protocol.md>) v1.0 and [Search and Screening Log](<Search and Screening Log.md>); G0 procedural acceptance is recorded in PREP-003. Log amendments before changed review work.
2. Maintain qualified G1 evidence and accepted G2 scope; preserve DEV-T16-001 and performed Q-120 receipts, reopen only affected claims when needed. Do not repeat completed sourcework as a blanket reading task.
3. Continue B-010 from **Accepted Snapshot 7: 574 advance / 112 X3 / 152 pending** occurrences (log §18). All **838/838 original-export semantic QA checks** are complete, with zero unread within the exported set; 70 OA/82 Scholar holds remain unresolved despite being read. The completed 130-member OA expansion assessed 151 affected mappings: 87 metadata-supported/44 unclear/20 outside that R, with four routing holds and no new exclusion. Inherited mappings, identities/date/language/type, source-role/content defects, coverage gaps and citation/full-text appraisal remain separate; no global all-pass or independent human review is inferred. All assigned subagents returned; do not restart completed metadata tasks.
4. Complete the protocol-required discovery, closest-solution and shortlisted-method checks supporting the five-candidate comparison; obtain actual contribution/scope approvals before contract/pilot/main-study freezes.
5. Keep implementation outside this research directory; this workspace records requirements and research reasoning only.

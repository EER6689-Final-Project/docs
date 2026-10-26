# Research Management Decision Log

**Updated:** 2026-10-26 (T1.6 integration and actual user scope decisions; historical decisions preserved)

This log records provisional governance decisions. It is not a final thesis design.

## Accepted decisions

| Date | Decision | Reason and boundary |
| --- | --- | --- |
| 2026-10-04 | Proposal governs group context; `My tasks.pdf` governs individual scope; direct conflicts require approval. | Prevents silent scope changes and respects both source documents. |
| 2026-10-04 | Phase 0 remains active. | All six reports are present, but original-source verification and claim-level evidence mapping are incomplete. |
| 2026-10-04 | Use “synthetic browser measurement” or “RUM-informed synthetic agents,” not RUM, for scripted browser runs. | RUM requires measurements from actual users/visits. |
| 2026-10-04 | Provisionally characterize the conditional run-performance distribution first. | Prevents premature selection of mean, median, p75, p90, or p95 before the estimand is known. |
| 2026-10-04 | Treat DevTools/Lighthouse as reference implementations, not automatic ground truth. | Shared Chromium infrastructure and different execution pipelines make agreement a layered validation problem. |
| 2026-10-04 | Keep same-artifact conformance and independent matched-run agreement conceptually separate. | They answer different validation questions. |
| 2026-10-04 | Treat instrumentation tier as an experimental factor and measure observer effects. | Overhead is workload- and configuration-dependent; universal correction is not assumed. |
| 2026-10-04 | Retain the controlled-fixture plus live-URL hybrid as a candidate evaluation design. | Fixtures support causal sensitivity; live URLs support production complexity. Neither replaces the other. |
| 2026-10-04 | Keep the performance-score requirement subject to an evidence gate. | Preserve component measurements; prohibit arbitrary weights or universal scalar claims. |
| 2026-10-04 | Do not implement the profiler in this directory. | This workspace is research-only; implementation belongs elsewhere if later authorized. |
| 2026-10-25; integrated 2026-10-26 | User is accountable researcher and project-scope authority; orchestrator coordinates AI technical checks, Luna extracts and Sol synthesizes. | Actual interactive answers, recorded in Scope Resolution §§5.1–5.2. No independent human reviewer, institutional authority or site permission is inferred. |
| 2026-10-25; integrated 2026-10-26 | Approve initial navigation plus fixed non-consequential inputs and conditional synthetic INP; soft-navigation metrics remain version-gated exploratory. Explicitly omit historical TTI by requirement amendment. | Preserve original REQ-006 wording/history and all other diagnostics, seven dashboards and unit-test duties. TBT and INP are distinct constructs, not equivalent TTI replacements. |
| 2026-10-25; integrated 2026-10-26 | Approve truthful CWV/diagnostic labels, client-observed TTFB and per-output version-matched DevTools/Lighthouse comparisons separating conformance from independent-run agreement. | Exact intervals, algorithms, releases, uncertainty methods and tolerances remain later evidence/contract choices; no isolated server-processing or absolute-accuracy claim. |
| 2026-10-25; integrated 2026-10-26 | Retain a versioned diagnostic-prioritization composite beside raw metrics and severity. | Purpose approved, not weights/calibration, universal UX/energy/carbon validity or a human study. |
| 2026-10-25; integrated 2026-10-26 | Bound feasibility planning to controlled local Chromium, required desktop/mobile/CPU/network profiles, four independently classified workload categories, fixtures plus authorized live targets; headed checks exploratory; no human study. | Supersedes the earlier candidate-only fixture/live scope boundary, not its inferential cautions. Exact builds, budgets, rubric, allowlist and actual permissions remain G5/G6 conditions; no scans authorized. Group cloud deployment remains a separate integration concern. |
| 2026-10-25; integrated 2026-10-26 | Individual owns profiler/API, all seven performance surfaces, evaluation and required unit tests; ZIP, carbon/AI, shared auth/storage and non-performance views are group dependencies. | User-approved responsibility boundary; actual team/interface agreement remains to obtain, not an assignment of other people by inference. |

## Explicitly not decided

- research gap, research question, hypothesis, aim, objectives, and final methodology;
- final profiler architecture or instrumentation tier;
- exact browser/reference builds and capture settings, cache/state/window contracts, corpus/rubric, sample sizes and repetition rule; bounded navigation/input and exploratory-SPA scope is now approved above;
- primary statistic, confidence procedure, agreement method, acceptance tolerance, or score formula.

## Historical approval issues — original questions and subsequent disposition

| Date | Requirement/evidence tension | Required decision | Evidence state |
| --- | --- | --- | --- |
| 2026-10-08 | `My tasks.pdf` lists FCP, TBT, Speed Index, historical TTI and “server response time” as Core Web Vitals, but official current CWV are LCP/INP/CLS; client TTFB is not isolated server processing. | Original question retained: labels, scripted INP, legacy TTI and client/server timing. | Resolved at scope level by actual user answers 2026-10-25: truthful labels, navigation + inputs/conditional INP, explicit TTI omission amendment and client TTFB. Exact contracts remain G5; see Scope Resolution A–E. |
| 2026-10-08 | Required DevTools/Lighthouse comparison has no automatic ground truth; version, collection artifact, browser state and score transformations can differ. | Original question retained: numerical conformance versus documented differences and agreement criteria. | User approved per-output version-matched references and separate conformance/independent-run agreement. Metric pairing, estimators/tolerances and shortlisted abstract-limited methods remain evidence/contract gates, not missing scope approval. |
| 2026-10-08 | Required transparent score may conflict with claim that one scalar measures universal web performance. | Original question retained: stakeholder purpose and multidimensional/severity reporting. | User approved developer diagnostic prioritization with versioned composite, raw metrics and severity. Weights/calibration/validity remain pending; historical Lighthouse v10 weights are not adopted. |

The four historical alternatives in [[Candidate Gap Assessment#historical T1.1 comparison — 2026-10-08]] (2026-10-08) remain unranked for novelty; a separately dated current five-candidate planning comparison is now recorded in [[Candidate Gap Assessment]]. Neither selects a contribution or establishes novelty. G3/G4 remain open under the queue; no accepted decision above selects a candidate.

## Initial decision/gate index — 2026-10-25 local

These stable IDs index current governance and **pending decision records**, not approvals. The earlier dated decisions/alternatives are preserved. Evidence comes from existing canonical notes and inventories only; this update is not a new source audit. The [queue](<Zotero Verification Queue.md>) owns C-001–C-008 claim families, B-001–B-009 blockers and minimum gate closure/reopening criteria. Review roles must be assigned; no personal owner or received approval is invented.

| Decision ID | Current decision or required resolution | Status / evidence boundary |
| --- | --- | --- |
| D-001 | Keep Phase 0 active and use the protocol/log plus reconciled tracker baseline | G0 procedurally satisfied 2026-10-25, PREP-003, ERP-2026-10-25-v1.0. Subsequent G1 qualified acceptance and G2 bounded scope approval are recorded below; G3–G7 remain open. G0 itself did not grant scientific, scope or experiment approval. |
| D-002 | Complete source-grounded T1.6 coverage before relying on new design claims | 2026-10-26: G1 qualified/deferred, bounded coverage accepted after prospective Q-120/V-T16-002 (27/27 checked; 20 pass/7 qualified, none blocking for retained assertions). Inventory accounts for 16 seeds/four NIST/service, 16 new rows/five references. Historical/current-web/transfer, metadata, retrospective-operation and lost-raw-capture limitations remain; no modern-design validation. |
| D-003 | Resolve requirements and decision rights explicitly | G2 satisfied for bounded candidate planning, orchestrator review 2026-10-26, APP-001; Scope Resolution records actual user answers and ownership. Specific technical/budget/site/ethics conditions remain later gates, not granted permissions. |
| D-004 | Resolve common/pre-selection evidence before final candidate selection | G3 open; Demir C-T1.6-051 now supplies bounded profile/count evidence, not completed novelty/closest-solution coverage. Reuse existing Heričko/Hantke and other canonical notes; soft-navigation release, current semantic/version checks and prescribed discovery/citation/contrary evidence remain. |
| D-005 | Complete protocol-required coverage supporting the five-candidate comparison, verify shortlisted method dependencies and seek contribution approval | G4 open; working comparison recorded, but eligibility/citation/closest-solution checks and shortlist methods remain. No selection/novelty finding. Abstract-only or inaccessible critical methods require authorized full text or a justified alternative/narrowing. |
| D-006 | Freeze versioned measurement contracts only after relevant scope/evidence resolution | G5 open; no output set, clock/scope/missingness contract or tolerance is approved here. |
| D-007 | Specify and approve a finite pilot before separately authorized collection | G6 open; requires G4/G5, parameters, allocation/failure/data-separation rules, scenario checks and actual permissions/approvals. No pilot run or implementation authorized here. |
| D-008 | Separate pilot exploration from a later main-study analysis freeze | G7 open; no main-study estimator, sample size, stopping or tolerance selected; approval cannot validate unsupported inference. |

Gate dependencies and deferrals follow the queue register: G1/G2 after G0, G3 after G1/G2, G4 after scope/common and shortlisted-method closure, G5 after relevant evidence/scope decisions, G6 after G4/G5, G7 after G6 and authorized pilot evidence. Contrary evidence, relevant version/scope/implementation changes or failed assumptions reopen affected decisions/gates. A critical unresolved blocker cannot pass merely by being deferred; any removal/narrowing needs an explicit bounded claim and required approval.

## T1.6 evidence integration decision record — 2026-10-26

Sol integrated sourcework dated 2026-10-25 under ERP-2026-10-25-v1.0; eligibility cutoff unchanged. Historical custom-client, own-server, replay, crossed-crawl and methodological evidence supplies qualified design considerations, not a mandate for a particular hybrid protocol. The user separately approved fixtures plus authorized live targets as the evaluation-scope boundary at APP-001; profiler architecture and sampling/analysis recipes remain unselected. No source is treated as proving our architecture, category thresholds, sample/repetition count, independence model, score weights, stopping/tolerance or novelty. [Inventory](<T1.6 Source Inventory.md>), atomic queue ledger and log preserve these boundaries; original report/PDF remain historical discovery material with a verification addendum.

G1 was accepted with explicit qualifications after performed V-T16-002/Q-120; its manifest preceded the new all-27-claim audit. Source-level support remains bounded; missing original operation clocks/ranks and lost raw audit captures cannot be retroactively repaired. Durable receipts disclose reconstruction from retained completed tool observations following restart. QC is AI technical self-audit, not independent human scientific review. G2 is separately satisfied for bounded candidate planning (APP-001); G3–G7 remain open, including unresolved discovery eligibility/identity and citation work. Future parameter/resource/site permissions remain distinct. No contracts, pilot, contribution assessment, library mutation, staging or commit is part of this integration.

## Change rule

Any future change to an item above must state the new evidence, identify which source class supports it, and preserve the prior alternative unless the user explicitly authorizes removing it.

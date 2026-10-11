# Research Management Decision Log

**Updated:** 2026-10-08

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

## Explicitly not decided

- research gap, research question, hypothesis, aim, objectives, and final methodology;
- final profiler architecture or instrumentation tier;
- browser mode, cache/state protocol, SPA/interaction scope, corpus, sample sizes, and repetition rule;
- primary statistic, confidence procedure, agreement method, acceptance tolerance, or score formula.

## Issues for approval — recorded, not decided

| Date | Requirement/evidence tension | Required decision | Evidence state |
| --- | --- | --- | --- |
| 2026-10-08 | `My tasks.pdf` lists FCP, TBT, Speed Index, historical TTI and “server response time” as Core Web Vitals, but official current CWV are LCP/INP/CLS; client TTFB is not isolated server processing. | Retain requested diagnostics with correct labels; approve whether INP scripted interactions and historical TTI reproduction are in individual scope, and how to label server/client timing. | Verified official taxonomy and CrUX timing guidance in [[Literature Review and Research Gap Matrix]]; scope clarification pending. |
| 2026-10-08 | Required DevTools/Lighthouse comparison has no automatic ground truth; version, collection artifact, browser state and score transformations can differ. | Select which outputs require numerical conformance versus documented differences, with later agreement criteria. | T1.1 originals support distinctions; T1.4/T1.5 source-level methods still pending. |
| 2026-10-08 | Required transparent score may conflict with claim that one scalar measures universal web performance. | Specify stakeholder purpose and whether a multi-dimensional/severity display alongside any composite meets the requirement. | Lighthouse v10 score mechanics read; current weights and score-validity evidence pending. |

The four alternatives in [[T1.1 Candidate Gap Assessment]] remain unranked for novelty and none changes an accepted decision above.

## Change rule

Any future change to an item above must state the new evidence, identify which source class supports it, and preserve the prior alternative unless the user explicitly authorizes removing it.

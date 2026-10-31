# Research Decisions

**Updated:** 2026-10-31. This is the current decision summary. Complete earlier decisions and alternatives are preserved in the [archived log](<../Research Archive/Decision Log before research selection.md>).

## Selected direction

| Date | Decision | Meaning |
| --- | --- | --- |
| 2026-10-31 | The researcher explicitly selected **Reliability of Delayed Browser Performance Diagnosis**: “We will go ahead with this idea.” | Proceed with report preparation around original-visit evidence versus a detailed follow-up visit for persistent/intermittent website regressions. The [Research Plan](<Research Plan.md>) is the working reference. |
| 2026-10-31 | Frame the study as independent browser performance measurement and diagnostic research. | Its title, question, objectives and evaluation stand independently of a particular consuming application. |
| 2026-10-31 | Treat website histories and adaptive profiling as supporting techniques with established prior art. | The possible contribution is a browser-specific empirical validity/coverage result, as explained in the [novelty comparison](<Monitoring Novelty Cross Reference.md>). Selection does not prove originality or superiority. |
| 2026-10-31 | Keep a longitudinal episode benchmark as the narrower fallback. | A new adaptive algorithm is optional; the study can characterize when delayed diagnosis loses or misattributes evidence. |
| 2026-10-31 | Reduce the working folder to six files and archive supporting/history material. | Full source matrix, novelty assessment and current decisions/checks remain accessible; older inventories, screening logs and audit artifacts are preserved in [Research Archive](<../Research Archive/README.md>). |
| 2026-10-31 | Document the research question, aim, hypotheses and five objectives in simpler language while retaining technical terms. | The [Research Plan](<Research Plan.md>) now states a directional H₁ and corresponding H₀ for intermittent regressions under matched budgets/deadlines. Correct attribution concerns the original verified fault class across all regression episodes. Statistical procedures and detailed protocol remain open. |
| 2026-10-31 | Document a proposed methodology for each of the five objectives. | Use a controlled longitudinal experiment, website-specific histories, independently verified episode labels and randomized scenario blocks. Compare legitimate lightweight attribution, fresh detailed follow-ups, feasible original-event capture and periodic capture under complete resource caps; retain always-rich profiling as a separate reference. Evaluate all-episode original-cause attribution, coverage, failures and cost, then examine persistence, delay and browser state. Pilot feasibility and a separate protocol/analysis freeze remain required. |

## Retained measurement and evaluation rules

- Independently verified interventions supply cause labels. A trace is a reference observation; a similar follow-up symptom is not proof that the original cause recurred.
- Keep original-visit and follow-up evidence separately identified. Include missed triggers, failures, unavailable data, exhausted budgets and abstentions in the all-episode evaluation.
- Freeze episode eligibility from planned, pilot-validated cases and independent execution/applicability checks, rather than alerts or an arm's observed slowdown. Keep scheduled opportunities independent of policy exhaustion; account for hidden evaluator-only verification separately from complete policy costs.
- Compare legitimate cheap attribution, feasible retained original evidence, fresh rich visits and fixed schedules using complete costs. Count continuous buffer capture and reruns, not only retained files.
- Preserve metric definitions, versions, windows, state and missingness. Synthetic runs remain synthetic; TBT is distinct from INP, client TTFB is not isolated server processing, and the recorded TTI omission remains in force.
- Engineering scope retains the service/API, seven performance surfaces, evaluation and three required unit-test families. The research endpoint may use a smaller output subset. The [scope record](<../Research Archive/Scope Resolution.md>) preserves the detailed allocation.
- Keep this repository research-only. Study implementation and collection require a specified finite protocol and appropriate target/resource access.

## Still to decide

Exact browser/reference versions; primary metric/fault subset; attribution taxonomy; original-evidence feasibility; target/corpus frame; state/reset and follow-up policy; thresholds, deadlines and budgets; campaign duration and run counts; uncertainty and repeated-testing procedures; holdout/allocation rules; retention and failure treatment; any score calibration.

The researcher has selected the direction. **The evidence and methodology are not thereby frozen:** G3/G4 evidence work and G5–G7 preparation remain open in the [verification queue](<Zotero Verification Queue.md>). Later approval or a passing gate must be recorded explicitly and must not be inferred from this summary.

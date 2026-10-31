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
| 2026-10-31 | Add the requested [Study Source Map](<Study Source Map.md>) and ground scan depth in capture contracts. | The map covers all 133 existing matrix rows plus 11 supplementary sources/references, giving Zotero keys, contributions and access/transfer limits. Metric definitions do not establish acquisition cost. Select candidate collectors from supported mechanisms and verify coverage/overhead in the pilot; episode definitions, thresholds and inference remain explicit study choices. The working folder now has seven files. |
| 2026-10-31 | Add 14 deduplicated parent records to Zotero's Final Project Research Papers collection (`FN3JMCGF`). | Seven supplementary research works/leads, four implementation documents and three existing sources without resolved paper records were imported and individually read back. Website Complexity is `9IN2U6Z2`, Tranco 2019 is `MWTY6KCS`, and Klotski is `JL4U756T`. The [receipt](<../Research Archive/Review Artifacts/2026-10-31 Study Source Map/README.md>) records keys, metadata and scope. The 133-row portfolio and source-appraisal/read limits are preserved; the map incorporates the newer decision-critical source checks. |

## Source-check consequences — 2026-10-31

- The [direct source checks](<../Research Archive/Review Artifacts/2026-10-31 Decision-Critical Source Checks/Source Appraisals.md>) support retaining the selected question as a **candidate browser episode-level evaluation**. The named works establish adaptive tracing, original-event retention, historical anomaly detection and selective sampling. Their inspected designs do not establish the full proposed delayed-visit comparison; this bounded inference is not novelty approval.
- WMF identity and the earlier direct-access discrepancy are resolved. Its controlled/synthetic anomaly-bin evaluation does not independently label each original visit's cause. Its tentative live-event explanations and manual-inspection treatment must not become this study's oracle or exclusion rules.
- LMAT's exact evaluated linger behavior remains unresolved because its indexed descriptions conflict. Use the qualified host-level precedent. Cite Shahedi's inspected 2024 preprint for its methods until the journal edition is read; cite Paradyn's manuscript for its rerun passage. Editions are not independent corroboration.
- Existing original-visit attribution is a mandatory baseline. Documentation checked at `web-vitals` v5.1.0 supplies a reference schema, not a selected runtime or demonstrated accuracy. Test supported entries and retention first; keep sampled stacks conditional on demonstrated need and build support.
- Do not adopt Mertz/Nunes's sample-release rule, Shahedi's regression test, a repetition count or a statistical threshold by analogy. Methods still require appraisal for the chosen episode hierarchy and estimand. No gate, collection permission or analysis freeze is recorded by this review.

## Finite pilot draft — 2026-10-31

The researcher requested Luna web searches, review and a Markdown protocol. [FP-0.1](<Finite Pilot Protocol.md>) is now the proposed feasibility design: two localhost fixtures, two fault classes, eight scenarios, five arms and 64 matched comparison blocks. The full schedule has 652 planned browser starts including preparation and maximum follow-ups, plus a 48-start repair reserve; stop at 700 starts, eight active hours, seven calendar days or the artifact/integrity cap, whichever applies first.

The [source review](<../Research Archive/Review Artifacts/2026-10-31 Finite Pilot Protocol/README.md>) supports feasibility-led sizing, explicit progression and attention to repetition/order/retention limits. All numerical caps and green/amber/red criteria are project choices. B retains original cheap attribution; C audit exports are gated; signalled capture failures remain outcomes; uncertain labels receive assignment-based sensitivity bounds. No superiority or favorable p-value is required to complete the pilot.

This records a **proposed protocol**, not research results, hardware availability, acceptance of numerical parameters or G6/G7 passage. Actual builds/capture mappings and execution checks remain open. Pilot data will remain separate from the main confirmatory dataset. The pilot's narrow loading/fault subset does not cancel the broader engineering duties.

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

## Report-writing plan — 2026-10-31

The researcher requested a comprehensive LaTeX plan in [docs](<../../docs/README.md>)
with 13 specified components: cover, title, declaration, abstract/keywords,
contents, figures and tables lists when applicable, abbreviations, Introduction,
Literature Review, Research Methodology, Work Plan and Conclusion. References
follow the conclusion. The current build uses five chapters and no results
chapter; the earlier empirical-report outline remains a later option.

Luna agents explore sources and draft sections; Sol agents synthesize, perform
a separate final content review, and then build/inspect the document in a
different agent. Zotero parent keys provide citation traceability, and the
extracted Hindsight illustration records its source page and file hash. The
declaration is an unsigned draft because the supplied formatting checklist has
no official declaration wording. Font and administrative limits are explicit
in the document and build review. This writing/production work establishes no
experimental result, novelty approval, source-hold resolution or study gate.

## Submission manuscript revision — 1 November 2026

The earlier report-plan and front-matter revisions were committed and pushed
as `fabf6f9` and `f2bb81f`. The requested validation and editorial passes then
converted the active `docs/` sources into a proposed-study submission manuscript.
Source, method and report-coherence discrepancies were corrected; internal
writing instructions were removed. The supplied two-page checklist remains
unchanged in the declaration position, and project-group/department lines
remain omitted from the identity pages.

The format checklist and two fresh-proof reviews record actual 12 pt Times
New Roman body text with 15 pt baselines, 18 pt reference/list baselines and
exact preservation of the original checklist pages. The final cleanup also
corrected cited publication identities and distinguished unknown publication
dates from access dates. Remaining online metadata checks are listed in the
[verification queue](<Zotero Verification Queue.md>). Final artifact generation
and page-dependent checks are recorded separately under `docs/review/`.

These revisions prepare the report, not the experiment. FP-0.1 and the main
study remain unrun; capture feasibility, main-study analysis decisions,
source-edition limits and the provisional contribution are unchanged.

# Sol Scholar Batch4 Next25 — completed bounded validation

**Exact scope:** E-0725–E-0749, 25 completed producer judgments only. ERP-2026-10-25-v1.0; cutoff 2026-10-25 inclusive; approved scope unchanged. Events **E-3800–E-3824**, in occurrence order. Producer E-3700–E-3724 is retained as history.

## Actual outcome

- Actually read all 25 original stored titles, **complete exported Scholar snippets** (not abstracts/full text), author/year/venue/URL metadata, and producer six-question judgments. Item-specific judgments and transfer boundaries are in `judgments.json` and `item_checks.tsv`.
- **23 ADVANCE / 2 PENDING / 0 X3.** E-0741 is pending because repeatability terminology does not establish between-method agreement or a repeated-measure uncertainty method; producer R5/R6 statements are internally inconsistent. E-0742 is pending because Lancet/1986 metadata conflicts with BerlinRUG/2015 URL cues; its possible R5 contextual relevance is not rejected.
- Positive R4 assignments identify specific SD/CV, temporal stability, heteroscedasticity, nesting, missing-reference-replicate, repeatability or aggregation issues. Experimentation or replication alone is not the assignment rule. R5 requires explicit agreement/bias/precision evidence, not general comparison. No positive R1/R2/R3/R6 was established. Statistical, human/native and non-browser methodological analogues remain eligible within explicit transfer limits.
- ADVANCE means uncertain stage-1 discovery/context routing, **not confirmed eligibility**. Dates (especially 2026 records), full-text language/authorized translation, source type and canonical identity remain pending for every item. Source-type proxies are title/metadata cues only. Reviews/statements/software papers do not replace originals for decision-driving claims. Source support/confidence **UNASSESSED**; full-text and citation passes **NOT RUN**. No online retrieval was needed or attempted; network availability is not an eligibility criterion.

## Prospective freeze and actual secondary QA

`target_freeze.json` froze the exact ordered 25 IDs, queue hash and completed producer hashes before Sol original reading. Producer handoff/author judgments were inspected first to establish actual scope and columns. Initial byte-hashing also incidentally covered a concurrently present `remaining50_freeze.json`; no remaining-50 content was semantically read or used.

After primary authoring, `qa_freeze.json` froze **all proposed exclusions (none)** and the first EID per each nonempty explicit positive R/type-proxy group, plus each no-positive pending type proxy: **10 distinct selected occurrences**. The selected originals were then actually reread from the immutable queue, against primary judgments. `qa_results.json` records **10 checked-no-discrepancy**, 0 corrected, 0 unresolved; `qa_group_results.json` distinguishes group selection from group-wide checking. **15 others have primary validation only**, not secondary QA. No secondary discrepancy triggered expansion. This is separate-pass AI self-audit, not independent human/scientific review; producer's earlier single selected QA check is not counted as whole-group QA.

## Preservation and integration boundary

`delta_overlay25.csv` preserves **every original queue column value unchanged**, including reviewer, stage1_reason, canonical_pending fields and historical DUP candidates. All added judgments/history fields begin `effective_`; consumers must deliberately select these derivative fields rather than treating preserved historical pending fields as current decisions. The completed first25 producer overlay and author judgments are embedded as history. No DUP merges, new SIDs, source/library mutation, original/shared tracker writes, staging or commits.

`verification.json` records exact target/event ordering, original-field equality checks and unchanged source/completed-producer hashes. `counts.json` is a **local delta only**; no aggregate was overwritten. `file_manifest.json` hashes deliverables except itself.

**E-0750–E-0799 remain entirely unreviewed by this task (50/50).** Producer activity elsewhere does not change this task's denominator. All 25 requested primary validations and all 10 selected secondary checks are actually complete; this is not a setup-only handoff. Canonical integration/acceptance belongs to the orchestrator. **G3/G4 remain OPEN**; broad-query, closest-solution/citation, method/full-text appraisal, identity and novelty deficits are not closed. No corpus-sufficiency, novelty or scientific approval claim follows.

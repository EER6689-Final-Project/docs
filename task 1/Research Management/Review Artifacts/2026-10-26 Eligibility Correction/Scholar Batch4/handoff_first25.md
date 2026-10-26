# Scholar Batch 4 — first 25 semantic review handoff

## Completed primary review

Reviewed records E-0700–E-0724 (25 items) from the prospectively frozen 100-ID set. Their original queue title, snippet field (treated as a search snippet, not abstract), and record metadata were printed and inspected directly. The additive `overlay_first25.csv` records producer review events E-3300–E-3324 with six separate, item-specific R1–R6 rationales and ADVANCE routing. No exclusion was proposed. Every ADVANCE decision reflects plausible bounded relevance to statistical repeated-measure/agreement methods; these are analogues, not browser validation.

The original DUP annotation was individually inspected but never used to dispose of an occurrence. Identity remains pending. Date, language, and source-type determinations remain pending; year 2026 alone did not cause a cutoff exclusion. No X2/X4 was applied. Full-text review and citation pass were not run; claim support and confidence are unassessed.

## Separate QA status

After primary review, `qa_freeze_first25.json` froze the exclusion and first-EID-per-R/source-type-proxy sample before secondary checks. There are no proposed exclusions to QA. The selected records were E-0700, E-0701, E-0709, E-0714, E-0716, E-0719, and E-0724. Checks were attempted and actual outcomes are in `qa_results_first25.csv`: Sage and MDPI returned 403; Springer returned a client challenge; the two PDFs failed because the fetch tool does not support `application/pdf`; Google Books returned only bibliographic/page-display information, not a substantive passage; arXiv returned abstract/metadata, not full text. Consequently **zero selected original full texts were checked**. These are access/tool blockers, not completed QC. No status is represented as checked-no-discrepancy.

## Counts and handoff boundary

- Actual stage-1 semantic checks: **25** (E-0700–E-0724).
- Frozen targets not reviewed: **75** (E-0725–E-0799).
- Primary exclusions proposed: 0; exclusion QA: not applicable.
- Secondary QA original-text checks complete: 0/7 selected; seven remain unreviewed for QC.
- Full-text claims/citation pass: none; support/confidence remain unassessed.
- Canonical promotion: **not authorized; Sol QA remains pending**.

`overlay.csv` and the prior general handoff are preserved as historical all-pending administrative artifacts; `overlay_first25.csv` is the additive reviewed overlay. No shared tracker, source library, original queue, or stage file was modified.

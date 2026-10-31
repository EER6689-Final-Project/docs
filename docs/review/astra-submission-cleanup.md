# Final submission editorial cleanup

**Date:** 1 November 2026. **Scope:** the active report sources and citation copy after the manuscript revision and the two 44-page proof reviews. This record is outside the submitted PDF. No experiment, compile, PDF rename, commit or push was performed during this pass.

## Changes

- Removed the obsolete report-writing-plan comment, unused `ReportPlaceholder`, `PlanCheck` and `PlanSource` macros, and editing prompts in metadata comments. Retained technical comments, source attribution, export provenance and historical review records.
- Verified that five placeholder-only files were not in the input tree, then removed them: `chapters/04-profiler-and-dataset.tex`, `chapters/05-results.tex`, `chapters/06-discussion-and-conclusion.tex`, `frontmatter/acknowledgements.tex` and `appendices/a-supplementary-material.tex`. These files contained authoring instructions, not completed research content.
- Removed internal appraisal, verification and workflow commentary from every cited bibliography note. Remaining notes identify a source version, publication status or associated author preprint. “Working Draft” and “Candidate Recommendation Draft” remain where they describe actual standards editions.
- Tightened a small number of literature-review sentences and the Hindsight lead-in. Kept the reproduced figure's attribution and the distinction between distributed-system prior art and the proposed browser study. Preserved substantive source limitations and the absence of experimental results.
- Restricted the Performance Timeline edition statement to the cited 21 May 2025 Candidate Recommendation Draft. The unlinked 26 October 2026 editor's-draft mention was removed; the report does not attribute editor's-draft-only content to the Candidate Recommendation. Finite, entry-specific buffering and the need to verify runtime support remain explicit.

## Citation corrections and checks

All 49 cited keys resolve. All cited scholarly records now have an author and publication year. Corrections affect `docs/references.bib`, not the Zotero library.

| Key | Correction and evidence |
| --- | --- |
| `DJI5ULJD` | Replaced the incomplete ResearchGate wrapper identity with Tjaša Heričko, Boštjan Šumak and Saša Brdnik (2021), *Towards Representative Web Performance Measurements with Google Lighthouse*, StuCoSReC 2021, pp. 39–42, University of Maribor Press, DOI `10.18690/978-961-286-516-0.9`. Evidence: the existing T1.3 paper note's PDF first-page and official-proceedings reconciliation. The old ResearchGate retrieval date was removed when the URL changed to the DOI; no new access date was invented. |
| `6WVYFE8R` | Pinned the LCP Working Draft to 26 August 2026, its dated W3C URL and corporate authorship, with the actual 31 October verification date. Evidence: `edition-date-verification.json`. |
| `REP5RHB6` | Pinned Performance Timeline to the 21 May 2025 Candidate Recommendation Draft, its dated W3C URL and corporate authorship, with the actual 31 October verification date. Evidence: the same receipt. |
| `84ZFNR74`, `JJWRMF5Z` | Preserved the earlier verified corrections to Paint Timing (2 October 2026) and Navigation Timing Level 2 (1 September 2026), including fixed URLs and 31 October access dates. |
| `HS3PKWFL` | Supplied the NSDI 2018 proceedings title and USENIX Association publisher from the exported venue identity and existing Vesper source note. Removed the duplicate event-title field. Authors, year and pp. 217–231 are unchanged. |
| `IX2DU87B` | Kept the 2024 arXiv v1 identity; reduced the note to “Preprint, version 1, 26 November 2024.” The body retains the unverified-final-journal-text limitation. |
| `WE8HHCA8` | Kept the verified JSS identity and made the associated author-preprint link version-specific (`2305.01039v1`, 1 May 2023). The body now explicitly states that the adaptive-sampling comparison concerns this preprint and does not establish journal-text equivalence. |
| `63QKVL86`, `N33VTKAN`, `SSS4NSXC`, `KE53ZLW3`, `TIIDVPV8`, `UMVA36NP` | Removed appraisal directions and project-specific interpretation from notes. Retained tip-of-tree status, web-vitals v5.1.0, Paradyn's manuscript type and the JS Self-Profiling source's draft identity where applicable. Technical limitations remain in the body. |

The bibliography style now selects publication `date`/`year`, otherwise `nodate`, for its author–year label. It no longer substitutes `urldate` as a publication year. Actual access dates remain available in reference entries. The final build must verify the rendered `n.d.` labels and disambiguation suffixes.

### Source metadata still unknown in the citation copy

No publication date was fabricated for these 23 cited online records: `4MGN3SYQ`, `63QKVL86`, `6SJEG5G9`, `92RRK4LT`, `9T8ACIJ8`, `9V33RJH6`, `9WMJW57H`, `A8GDSSI7`, `AAW3TPVK`, `B8XNKSHY`, `FBTV2ICM`, `GYN22PP7`, `I8L7FN9V`, `KEJFZJHV`, `N33VTKAN`, `NXHCE5SV`, `QF52VUCU`, `QHUCFVBF`, `R2U9EAFA`, `SSS4NSXC`, `UKNA4QJZ`, `UMVA36NP`, `VMWYVJKL`. These use `n.d.` unless a publication date is subsequently verified.

The existing copy also has no author/editor field for these 19 online records: `4MGN3SYQ`, `6SJEG5G9`, `92RRK4LT`, `9T8ACIJ8`, `9V33RJH6`, `9WMJW57H`, `A8GDSSI7`, `AAW3TPVK`, `B8XNKSHY`, `FBTV2ICM`, `GYN22PP7`, `I8L7FN9V`, `KEJFZJHV`, `NXHCE5SV`, `QF52VUCU`, `QHUCFVBF`, `R2U9EAFA`, `UKNA4QJZ`, `VMWYVJKL`. Titles, source URLs and existing source/site fields identify these documents; the configured style falls back to title where needed. Corporate or personal authorship has not been guessed from a URL. These are metadata-verification items, not evidence of missing cited documents.

## Preserved scientific and production constraints

The pilot and main study remain unrun. The report retains future/conditional procedures and contribution claims, independent activity verification, the all-verified-eligible failure denominator, strong A attribution and B's retention of A, all-original C audit exports with charged cost and gated diagnostic access, E's separate reference allowance, FP-0.1 allocations and caps, and a separately unfrozen main study. No experimental result, independent causal validation or final novelty claim was introduced.

The exact supplied `format.pdf`, its inclusion wrapper and preservation/build scripts were not edited in this pass. The fixed 27 October 2026 report date, author/course/registration details, Faculty of Engineering Technology, omitted department/group lines, strict Times New Roman selection, 12/15 pt normal body setting and 12/18 pt reference/list settings were retained.

## Static verification and final-build handoff

- The resolved input tree contains 13 files; all input targets exist.
- All 49 cited keys and 11 cross-reference targets resolve.
- Active TeX, stylesheet and bibliography braces balance; `git diff --check` passes.
- Active sources contain no `ReportPlaceholder`, `PlanCheck`, `PlanSource`, “To write,” “Completion check,” agent labels or report-writing-plan identity.
- Every retained cited bibliography note was inspected. It now states only version/status or author-preprint identity.
- The previous 44-page proof is superseded for page-dependent checks. Rebuild with Biber and the prescribed original-page preservation step; inspect every page, bibliography sorting and `n.d.` labels, line spacing, fonts, resolved references and exact original pages 3–4 before delivering the named final PDF.

The final build/render remains the only production hold from this pass. Scientific limitations concerning source-edition equivalence, LMAT controller behavior, runtime capture feasibility and the main-study design remain explicit; editorial cleanup does not resolve them.

## Access-date reconciliation after cleanup

The client date advanced to 1 November during the root source checks. The LCP
and Performance Timeline fixed-edition URLs were retrieved on 1 November;
Paint Timing and Navigation Timing were retrieved on 31 October. The edition
receipt records the two batches, and the final build corrects those two access
dates without changing publication dates, source versions or scientific claims.

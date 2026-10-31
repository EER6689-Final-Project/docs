# Final submission build and PDF verification

**Date:** 1 November 2026. **Artifact:** [`EEY6189_N.W.L.U.R.D.Nanayakkara_321424374_Final Report.pdf`](../EEY6189_N.W.L.U.R.D.Nanayakkara_321424374_Final%20Report.pdf). **SHA-256:** `d63e7f84081a821a7070e4da304f80d7abf1d4d2b24b71b272f0251a78dda1ec`. **Size:** 636,866 bytes. **Length:** 44 physical pages. The named file is byte identical to the final post-processed `main.pdf`. The active input fingerprint is `e5b700d7185c8d8a2fd372271be0fc2865e2080b5983dd04232fe537a83dddc7`; its included paths and machine-readable checks are in `final-submission-build.json`.

`bash docs/tools/build-report.sh` completed XeLaTeX, Biber, XeLaTeX, XeLaTeX and original-page preservation. The build used TeX Live 2026 XeTeX `3.141592653-2.6-0.999998`, Biber `2.22`, pypdf `6.10.0` and Poppler `26.01.0`. The final XeLaTeX/Biber logs have no errors, unresolved citations or cross-references, missing characters, or overfull boxes. Narrow table cells and URLs yield underfull ragged-wrap warnings; page render review found no clipping or overlap. `git diff --check` passes.

## Structure and format checklist

The final disposition of the IDs in `format-structure-checklist.md` is:

| IDs | Result | Fresh-PDF evidence |
| --- | --- | --- |
| S01–S04 | PASS | Cover/title are physical pp. 1–2; supplied pages 3–4; abstract 5; contents 6–7; figure list 8; table list 9; symbols 10; five chapters start 11, 15, 21, 34 and 38; references start 39. Both caption lists appear in the ToC at correct Roman folios. No acknowledgements or appendices are included. |
| F01–F06 | PASS | No authored logo, border, running header or footer text; only permitted folios. Source margins are 1.5/1/1.5/1 inches; authored pages are A4. Title is Roman `i`, abstract `iv`, chapter 1 Arabic `1`, references start `29`, final page `34`. Chapter openings and symbols list were inspected. Genuine embedded Times New Roman is used for body text. |
| I01–I03 | PASS | Cover and title pages show prescribed sizes/weights, author, course, faculty, university, fixed date, registration and supervisors; no department or group line. |
| C01–C03 | PASS | ToC pp. 6–7 have correct linked component/section folios. The full, unshortened captions of both figures and all eight tables appear in their lists, with no optional short-caption source. |
| R01–R02 | PASS | Pages 39–44 contain 49 consecutive `[n]` reference labels for 49 cited keys, alphabetically sorted under `nyt`, with author–year citations. Online entries show `[Online]`, URLs and access dates. Unknown online publication dates remain `n.d.` rather than being replaced by retrieval years. The two newly checked W3C pages have 1 November 2026 access dates; the other fixed editions retain their verified 31 October dates. |
| A01 | N/A | No appendix is included. |
| Q01–Q02 | PASS | PDF text scan found no placeholder macro text, AI-agent labels, authoring prompts or source-verification workflow notes. The final source and artifact hashes, page count, font and spacing measurements, build logs, and page renders are recorded here and in the JSON receipt. |

The supplied `format.pdf` remains SHA-256 `04f2a570203133ed4360dfbfb07ae50a37a1961fc1e3ec12d8cd7addc7dea774`. Its pages occur at physical pp. 3–4 with their 612 × 792 point Letter MediaBoxes. Extracted text and decoded content streams match the source; final-report and source renders are **pixel identical at 120 dpi**. All blanks, boxes and signature/date lines remain unfilled, without an authored overlay or folio.

Normal body characters measure 11.9552 PDF points, equivalent to 12 TeX points. Successive prose lines on physical pp. 11, 18, 26 and 34 measure 14.9–15.0 PDF points after coordinate rounding, matching a 15 TeX-point baseline (`14.94396` PDF points). Figure/table lists on pp. 8–9 and multiline references on pp. 39–40 and 44 measure 17.9–18.0 PDF points, matching an 18 TeX-point baseline (`17.93275` PDF points). The 72 dpi contact sheet covers all 44 final pages; pp. 1–2, 6–9, 20, 26, 35, 37, 39, 43–44 were examined at larger scale. Temporary renders are under `/tmp/eei6689-final-submission-qa/`.

The report accurately presents a proposed study: neither pilot nor main experiment has been executed, so no measured research result or institutional approval is implied. Unknown authorship/publication dates for some online source records remain verification items outside the submitted PDF.

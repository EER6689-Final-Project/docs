# Structure, front matter, captions and references audit

**Proof inspected:** 31 October 2026, 44-page fresh build  
**PDF SHA-256:** `e050b7f4b8a71ae8469cddd5613e5eb238d00962dab4cee5f349dfe3be328d1b`  
**Authority:** `docs/review/format-structure-checklist.md` and supplied `docs/format.pdf`  
**Method:** active LaTeX route/source review, `pdfinfo`, PDF text/page-size checks, full-page 72 dpi contact sheet, selected-page visual inspection, and 120 dpi source-versus-inserted-page pixel comparisons. Temp renders are in `/tmp/eei6689-submission-qa/final/`.

## Checklist results

| ID | Result | Evidence and physical PDF pages |
|---|---|---|
| S01 | PASS | `main.tex` selects cover, title, two supplied guide pages, abstract, ToC, LoF, LoT, symbols/abbreviations, Chapters 1–5, then references. Fresh PDF confirms: cover/title 1–2; guide 3–4; abstract 5; ToC 6–7; LoF 8; LoT 9; symbols 10; Chapters 1–5 begin 11, 15, 21, 34, 38; references begin 39. |
| S02 | PASS | `frontmatter/declaration.tex`, `main.tex`, build script and preservation script use the supplied `format.pdf` in order. Physical PDF pp. 3–4 are each 612 × 792 pt, text matches source, and their 120 dpi renders are pixel-identical to source pp. 1–2. |
| S03 | PASS | Physical PDF pp. 3–4 retain the supplied blank checkboxes, registration/study-stream blanks, and candidate signature/date area. No overlay is visible; source and report renders match pixel for pixel. |
| S04 | PASS | No acknowledgements or appendices are input by `main.tex`; neither appears in the PDF or ToC. This follows the explicit 13-component sequence and omission. |
| F01 | PASS | Full contact sheet and selected pages show no OUSL logo, borders, running headers, or authored footer text. Folios are the only authored footer content. The two supplied pages remain unchanged. |
| F02 | PASS | `report-format.sty` sets left/right/top/bottom margins to 1.5/1/1.5/1 in. Authored pages are A4; source and PDF geometry confirm the inserted pages alone remain Letter. Selected body/table pages fit the authored text area. |
| F03 | PASS | Printed folios: title i; inserted pages have no new folios; abstract iv; ToC v–vi; LoF vii; LoT viii; abbreviations ix; Chapter 1 starts at Arabic 1. Subsequent chapter and reference folios are Arabic. Cover has no visible folio. |
| F04 | PASS | Source chapter formatter and physical PDF chapter openings p. 11, 15, 21, 34, 38 show numbered uppercase headings (`01.` through `05.`), left aligned, without underlining or a blank line above. |
| F05 | PASS | Typesetting review verified the required genuine Times New Roman faces, 12 pt body size, 15 pt running-line baseline, and 18 pt list/reference baselines in this proof. Authored body text uses embedded subset Times New Roman; original guide-page fonts are confined to pp. 3–4. |
| F06 | PASS | Symbols/abbreviations list is present on physical p. 10. All 22 listed entries are used in active chapters; table is readable at page scale. |
| I01 | PASS | `cover.tex` uses 18/27 pt uppercase title, 14 pt bold “By” and course, 16 pt bold author, 14 pt faculty/university and bold month/year. Physical p. 1 fits; department and group lines are absent. |
| I02 | PASS | `title.tex` uses 18/27 pt uppercase title, 14 pt bold “By”, registration, course and date, 16 pt bold author, 14 pt supervisors/faculty/university. Physical p. 2 fits; department and project-group lines are absent. |
| I03 | PASS | Physical pp. 1–2 contain no project-group or department line; faculty and university are retained. |
| C01 | PASS | Physical pp. 6–7 show bold chapter title/page-number lines and numbered section hierarchy. ToC includes all routed components and references; linked folios agree with the PDF (e.g. Chapter 1 p. 1, Chapter 5 p. 28, References p. 29). No stale chapter entries. |
| C02 | PASS | Physical p. 8 lists both figures with full caption wording and folios (10 and 16); active figures have no shortened optional captions. |
| C03 | PASS | Physical p. 9 lists all eight tables with full caption wording and folios (8, 13–19, 24, 27); active tables have no shortened optional captions. Continuation on p. 35 has a repeated table header and readable cells. |
| R01 | HOLD — format passes; cleanup pending | Physical pp. 39–44 contain 49 consecutively numbered references, matching 49 cited keys; no uncited records render. Biber uses author–year sorting/citations and the output uses numeric bracket labels. Alphabetical order is consistent with the configured `nyt` sort. Source-verification note commentary is emitted in entries; see Q01. |
| R02 | PASS | All cited `@online` records include URL and access date in the source and rendered bibliography. Online entries visibly use an online medium and “Available at” URL. DOI/URL-bearing scholarly papers remain publication records, not website entries. |
| A01 | N/A | No appendix is included. |
| Q01 | FAIL — cleanup pending | Active body/front matter contain no emitted draft prompts, AI-role labels, or editorial placeholders. The bibliography does emit internal source-verification notes, including physical p. 39, reference [8] (printed folio 29), p. 40 [15] (folio 30), and p. 44 [48] (folio 34). The final cleanup/rebuild must remove or rewrite those notes before submission. |
| Q02 | PASS for this proof | The inspected 44-page PDF is the fresh post-processing build with the guide-page preservation step. SHA-256 and page count are recorded above. The current log has no unresolved citations/references; the previously reported Chapter 4 longtable overfull was corrected in the final proof. |

## Build and visual observations

- All 44 pages are non-empty. There are 42 authored A4 pages and the two exact Letter guide pages.
- The ToC and generated lists contain the active content; figures precede tables, and the abbreviations list follows both.
- The Chapter 4 work-sequence longtable breaks cleanly, repeats its header, and has no clipped text. The risk table on physical p. 37 is readable.
- The two figure placements and selected methodology tables are legible and unclipped. References wrap within the text area.
- This audit describes the current proof. Re-run page-dependent checks after the pending bibliography cleanup changes and final build.

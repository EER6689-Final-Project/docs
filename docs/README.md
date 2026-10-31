# Research report

Start with `main.tex`. The LaTeX report **Reliability of Delayed Browser
Performance Diagnosis** presents the research question, literature review,
proposed methodology, research work plan and conclusion. Neither the feasibility
pilot nor the main study has been executed; the report does not present
experimental findings.

## Document structure

1. Cover page
2. Title page
3. Both original pages of `format.pdf` in the declaration position
4. Abstract and keywords
5. Table of contents
6. List of figures
7. List of tables
8. Symbols and abbreviations
9. Introduction
10. Literature review
11. Research methodology
12. Research work plan
13. Conclusion

References follow the conclusion. The requested order and the removal of
project-group and department lines take precedence over the generic checklist.
Faculty of Engineering Technology is verified from the original proposal.
The author, course, supervisors and fixed report date are retained in
`config/metadata.tex`.

## Sources

The study protocol and source appraisals remain in
`../task 1/Research Management/`. `references.bib` uses Zotero parent item keys
as citation keys, for example `\parencite{HS3PKWFL}`. Only cited records are
printed. The broader collection export is documented in
`zotero-export-manifest.json`; it is not a count of independent empirical studies.
The focal readback and citation-copy corrections are recorded in
`source-manifest.json` and the review records. The four dated W3C edition URLs
and their verified retrieval dates are recorded in
`review/edition-date-verification.json`.

The Hindsight illustration is an attributed crop of the original Figure 2,
physical PDF page 6 / printed page 325. Its source hash and crop are recorded
in `figures/provenance.json`. The evidence-flow diagram is native TikZ and
represents the proposed design. Source illustrations are not experimental
outcomes from this study.

## Build

Run from the repository root:

```sh
bash docs/tools/build-report.sh
```

XeLaTeX, Biber, Times New Roman and Python with `pypdf` are required. The script
uses tools on PATH, or the existing TeX Live 2026 installation under
`~/.local/texlive/2026/bin/x86_64-linux/`. A temporary XeLaTeX format is generated
when the installation has no prebuilt format. XeLaTeX, Biber and two further
XeLaTeX passes are run directly. The local bundled Python runtime is used if
the system Python has no `pypdf` installation. The compiled preview is `main.pdf`.

The original two checklist pages are preserved by
`tools/preserve-format-pages.py` after compilation. This step copies the source
PDF's content streams, resources and Letter page geometry into the reserved
pages without changing the report's page destinations. No heading, folio or
other overlay is added. Authored pages use A4. The source PDF is unchanged.

The final submission filename is:

`EEY6189_N.W.L.U.R.D.Nanayakkara_321424374_Final Report.pdf`

## Format verification

The main source of formatting requirements is `format.pdf`; the requirement
matrix is `review/format-structure-checklist.md`. Normal paragraph text is
12 pt Times New Roman with a 15 pt baseline. Figure/table lists and references
use 18 pt baselines. Margins are 1.5 inches on the left/top and 1 inch on the
right/bottom. Chapter headings are 22 pt uppercase; subheadings are 14 pt.
Page numbers are placed at the bottom right, with Roman preliminary pages and
Arabic chapter pages. The unchanged inserted checklist pages have no added
folios. Harvard author-year citations are paired with alphabetically sorted,
numbered references to follow the checklist's mixed examples.

The four genuine Times New Roman faces were installed locally and verified;
font binaries are not distributed in this repository. Installation/source
hashes are recorded in `review/font-verification.json`. Build and validation
records are kept under `review/`; earlier records describe their historical
snapshots. No review or document build establishes study execution or
institutional approval.

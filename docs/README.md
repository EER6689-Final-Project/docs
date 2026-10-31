# Final report LaTeX project

Start with `main.tex`. This is a writing scaffold based on `format.pdf`, with
chapter topics taken from the current research plan. It contains drafting
prompts, not a completed report or experimental findings.

## Identity and editing

Edit `config/metadata.tex` for the report identity. It currently contains:

- **Title:** Reliability of Delayed Repeatable Website Performance Diagnosis
- **Author:** N. W. L. U. R. D. Nanayakkara
- **Student registration number:** 321424374
- **Contact:** s92064374@ousl.lk
- **Subject:** EEY6189 Research Methodology and Project Identification (Software)
- **Supervisors:** Prof. Uditha Ratnayake and Ms. Tharini Abeyrathne
- **Date:** 27 October 2026, four days before 31 October 2026

The cover shows October 2026; the title page shows the full fixed date. Fill in
the project group, department and faculty placeholders before
submission. The course code supplied for this report is retained even though
the repository uses EEI6689 in its name.

Write in `chapters/`, edit preliminary pages in `frontmatter/`, put figures in
`figures/`, and add supplementary material in `appendices/`. All visible
`\ReportPlaceholder{...}` prompts and bracketed administrative placeholders
must be replaced or removed before submission. The chapter outline follows
the working plan; it does not freeze the protocol or establish any findings.

Working sources remain under `../task 1/Research Management/`, especially the
research plan, literature matrix and novelty cross-reference. Resolve uncertain
source details in the existing Zotero Verification Queue before citing them.

## Formatting implemented

| Guide requirement | Project setting |
| --- | --- |
| Arrangement | Cover, title, abstract, acknowledgements, contents, tables, figures, symbols/abbreviations, chapters, references, appendices |
| No OUSL logo, borders or running text | No logo, border or running header/footer text; page number only |
| Margins | Left/top 1.5 in; right/bottom 1 in |
| Body | Times New Roman, 12 pt, 15 pt baseline, left aligned with ragged right edge |
| Chapter headings | 22 pt, uppercase, left aligned, no underline or extra space above; `01. INTRODUCTION` style |
| Subheadings | 14 pt, left aligned; write their titles in Title Case |
| Cover/title heading | 18 pt uppercase, 27 pt baseline (1.5 line spacing) |
| By / author / course | 14 pt bold / 16 pt bold / 14 pt bold |
| Administrative lines | 14 pt; registration and dates bold |
| Contents | Chapter entries and page numbers 12 pt bold; section hierarchy `1.1`, `1.1.1`, `1.1.1.1` |
| Tables/figures lists | 12 pt with 18 pt baseline; use full captions without optional short captions |
| Pagination | Cover unnumbered; title starts at `i`; chapters start at `1`; bottom right |
| Appendices | `A1`, `A2`, ...; each new appendix resets to `B1`, `C1`, ... |
| References | Author-year citations, alphabetically sorted numbered entries, left aligned at 1.5 line spacing |

The guide does not explicitly set a paper size. **A4 is the project default**;
change `a4paper` in `main.tex` if the department requires another size. The
checklist PDF itself uses US Letter, but does not say the report must use it.
The guide's "leftJustified" is interpreted as left aligned rather than fully
justified. Normal section numbers retain the standard hierarchy; only chapter
headings have the leading zero shown in the guide's example.

## Citations and references

Add checked BibLaTeX records to `references.bib`. Use `\textcite{key}` for
Author (Year) or `\parencite{key}` for (Author, Year). Only cited records appear
in the bibliography. Remove its visible drafting prompt when records are added.

The guide combines "Harvard style" with numbered `[n]` examples. This project
uses BibLaTeX author-year citations and adds numbered labels to the alphabetical
reference list to accommodate both instructions. Books support publication
place, publisher and edition; omit the edition for a first edition. Online
records support `[Online]`, "Available at:" URLs and bracketed access dates;
supply `urldate` explicitly. Harvard punctuation varies, so compare the first
populated bibliography against the checklist during the deferred visual review.

## Build later

**Compilation and rendered layout checks are intentionally deferred** while
LaTeX is being installed. No TeX engine, Biber or latexmk has been run for this
project. Source review does not establish that the project compiles or that
the rendered report meets every layout requirement.

Use **XeLaTeX**, **Biber** and the actual **Times New Roman** font family
(regular, bold, italic and bold italic). The project deliberately does not
substitute another font. The current system font lookup resolved Times New
Roman to Liberation Serif, so confirm/install the required font before building.
The needed packages are listed in `config/report-format.sty`; a full TeX Live
installation normally supplies them. `latexmk` is optional but convenient.

Run from `docs/` after installation:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively, use these passes from the same directory:

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
biber main
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

The empty starter bibliography can produce an empty-bibliography warning.
The generated `main.pdf` and intermediate files are ignored locally; the two
supplied PDFs remain untouched. To clean intermediates after a build:

```sh
latexmk -c main.tex
```

## Deferred review checklist

- Confirm Times New Roman is actually loaded and all four font faces work.
- Inspect both identity pages for long-line wrapping and single-page fit.
- Check margin distances, the 12/15 body baseline and 22/14 pt headings.
- Check that the title page is `i`, Chapter 1 starts at `1`, and appendix pages
  reset correctly across at least two appendices, with unique PDF links.
- Inspect the contents, full-caption lists and a populated alphabetical
  bibliography, including a book and an online record with an access date.
- Resolve citations/references and inspect figures, tables and page breaks.
- Remove every drafting prompt and administrative placeholder before submission.

# Research report-writing plan

Open `main.tex`. This LaTeX project is a detailed plan for writing **Reliability
of Delayed Browser Performance Diagnosis**, with proposed study text, evidence
requirements, drafting tasks, production roles and completion checks. It is not
a report of completed experiments. FP-0.1 is proposed feasibility work; no pilot
or main-study result is asserted.

## Requested document sequence

| Order | Component | Source / generation |
| --- | --- | --- |
| 1 | Cover page | `frontmatter/cover.tex` |
| 2 | Title page | `frontmatter/title.tex` |
| 3 | Declaration page | `frontmatter/declaration.tex` |
| 4 | Abstract and keywords | `frontmatter/abstract.tex` |
| 5 | Table of contents | Generated from headings |
| 6 | List of figures | Generated from the included figure captions |
| 7 | List of tables | Generated from the included table captions |
| 8 | Abbreviations | `frontmatter/symbols-and-abbreviations.tex` |
| 9 | Introduction | `chapters/01-introduction.tex` |
| 10 | Literature review | `chapters/02-literature-review.tex` |
| 11 | Research methodology | `chapters/03-methodology.tex` |
| 12 | Work plan | `chapters/04-work-plan.tex` |
| 13 | Conclusion | `chapters/05-conclusion.tex` |

References follow the conclusion. Figures and tables are actually included,
so both caption lists are present; remove the corresponding list if all items
of that type are removed later. The user's requested order governs this plan
where the supplied checklist has a different sequence. The older unreferenced
scaffold files for results, a separate profiler chapter, acknowledgements and
appendices are retained but are not part of this build.

## Identity and declaration

`config/metadata.tex` retains the supplied author, registration number, contact,
course and supervisors. The title is consistent throughout this project.
The cover identifies this as a **Detailed Report-Writing Plan** prepared on
31 October 2026. The existing report date, 27 October 2026, is retained and
explicitly marked for confirmation; it is not represented as an actual study
completion date. Project group, department and faculty remain administrative
fields to confirm. Do not guess them.

`format.pdf` contains formatting instructions and a checklist signature, but
no prescribed authorship declaration. The declaration page therefore provides
a visibly labelled draft and completion instructions. It is unsigned and must
be replaced with approved wording before submission.

## Evidence and source handling

The source of truth for the study is `../task 1/Research Management/`, including
the Research Plan, Study Source Map, Literature Review and Research Gap Matrix,
Monitoring Novelty Cross Reference, Finite Pilot Protocol and verification
queue. The plan distinguishes documentary support, researcher choices and
runtime checks. It does not allocate metrics to light/deep scans solely by name.

`references.bib` preserves the broader Zotero collection export already present
during this task. `zotero-export-manifest.json` records that export's scope.
Only cited entries appear in the PDF; library records, aliases and topic reuse
are not counts of independent empirical studies. `source-manifest.json` records
23 focal items individually read from the live local Zotero API for this plan.
Zotero parent keys are deliberately used as BibLaTeX keys, for example
`\parencite{HS3PKWFL}`. Citation-copy corrections and source-version choices
are recorded in that manifest; the Zotero library was not changed. Abstracts,
local attachment paths and organization tags are omitted from the citation copy.

The Hindsight diagram is a local vector crop, not a redrawn result. Its source,
parent key, original Figure 2, physical PDF page 6 / printed page 325, crop and
source hash are in `figures/provenance.json`. Re-extract with
`python3 tools/extract-reference-figure.py` when `pypdf` is available. The
original study evidence-flow diagram is native LaTeX/TikZ. Both illustrations
are labelled by purpose; neither is a measured study outcome. Confirm permitted
reuse before external republication of the source illustration.

## Build and visual review

Use XeLaTeX and Biber. Run from `docs/`:

```sh
bash tools/build-report.sh
```

The script uses installed tools on PATH, or the existing TeX Live 2026 binaries
under `~/.local/texlive/2026/bin/x86_64-linux/`. It does not install dependencies
or use the network. It runs XeLaTeX, Biber and two further XeLaTeX passes
directly; this avoids a `latexmk` dependency on missing system Perl modules.
If the TeX Live install lacks a prebuilt XeLaTeX format, the script generates
one in `/tmp` for that build. The output is `main.pdf`; intermediates and that
compiled preview are ignored by Git. The LaTeX sources, bibliography, source
assets and review records are the editable deliverables.

`format.pdf` requires Times New Roman. The style uses that font when installed;
otherwise it emits an explicit warning and uses **TeX Gyre Termes for the draft
proof**, with a notice on the cover. A fallback build is not exact font
compliance. Install/verify the genuine required family and rebuild before
submission. A4 is the project default; the guide does not prescribe paper size.
The other settings follow the supplied checklist: 12 pt / 15 pt body,
left/top 1.5-inch margins, right/bottom 1-inch margins, 22 pt uppercase chapter
headings, 14 pt subheadings, bottom-right page numbers and no logo or running
text. Harvard author-year citations have an alphabetically sorted numbered
bibliography to accommodate the guide's mixed examples.

The final content and build agents record their checks in `review/`. Compilation
must resolve citations and cross-references; visual review must inspect page
sequence, identity-page fit, diagrams, multi-page tables, captions and references.
Actual build status and remaining limitations belong in the build review,
not an assumed success statement here. Content review by an AI agent is not
independent scientific or institutional approval.

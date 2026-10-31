# Final build and visual review — report-writing plan

**Reviewed:** 31 October 2026. **Status:** PDF built and visually checked as a draft proof. This is a production review following the separate passed content review, not scientific, institutional, or submission approval.

## Artifact and build

| Check | Result |
| --- | --- |
| Command | `bash docs/tools/build-report.sh` from the repository root; completed with exit code 0 without external `PATH`, downloads, or network access |
| Engine | XeTeX 3.141592653-2.6-0.999998, TeX Live 2026; Biber 2.22 |
| Route | XeLaTeX → Biber → XeLaTeX → XeLaTeX |
| Output | `docs/main.pdf`, 40 A4 pages, 382,395 bytes, SHA-256 `0a8f52c7b6033eca90038a5a25be37f7045788ab7809aaacc834c222cee70d65` |
| References | 180 retained BibLaTeX entries; Biber processed 46 cited parent keys and generated 46 numbered, alphabetically sorted references |
| Diagnostics | Zero unresolved citations or cross-references, zero overfull boxes, zero Biber errors/warnings. `git diff --check` passed. Benign underfull boxes remain in narrow table cells. |

The local TeX Live installation has no prebuilt `xelatex.fmt`; its `mktexfmt` and `latexmk` fail because the system Perl lacks core modules (`File::Find` and `File::Copy`). The build script now generates a temporary XeLaTeX format directly with `xetex -ini` when needed and runs the three XeLaTeX passes plus Biber directly. The format and page renders are in `/tmp`, outside the repository. A fresh invocation of the script succeeded without session environment variables.

## Visual and structural checks

All 40 final pages were rendered at 90 dpi and inspected in four contact sheets; selected pages were inspected at 160 dpi, including cover, title, declaration, contents, caption lists, the source figure, the original TikZ diagram, the multi-page prior-work table, the work-plan tables, and references. Temporary renders are at `/tmp/eei6689-report-plan-qa/`. No clipped text, overlapping cells or boxes, empty figure/table lists, broken glyphs, or misordered major components remain. The repaired diagram's evaluator and cost-ledger boxes have a visible gap and connect to the locked-score path without crossing text.

The cover is unnumbered; the title through abbreviations use Roman pages i–vii; Introduction starts Arabic page 1. The contents fit one page and the required order is cover, title, declaration, abstract/keywords, contents, figures, tables, abbreviations, Introduction, Literature Review, Research Methodology, Work Plan, Conclusion, then References. The lists contain two captioned figures and eight captioned tables with page references. The References section begins on Arabic page 27 and ends on page 32. The PDF title explicitly includes “Detailed Report-Writing Plan.”

## Technical reconciliation after the content gate

- `docs/references.bib`: removed two malformed residual abstract fragments from uncited records `9WT3HAHJ` and `L59HPN96`; no entry, cited key, or source metadata field was replaced. Biber now parses all 180 entries. Final SHA-256: `4e9ec95a2c5043684982f437fb5afa7ee8c2a0848f9676a407d5c6c5af16d4cb`.
- `docs/config/report-format.sty`: loads the installed TeX Gyre Termes OTF files by filename, makes URL breaks flexible, prevents overfull ragged-right lines, tightens contents spacing, specifies Biber's effective `uniquename=init`, and identifies the plan in PDF metadata. Final SHA-256: `568108d092e17ae1737f7da2db27b23a71e4d8b1e1489d1690c5088c6f3090dc`.
- `docs/figures/episode-evidence-chain.tex`: used relative TikZ node placement, wider boxes, and a gap between side boxes to remove collisions; diagram labels retain the same design meaning. Final SHA-256: `a2a13637a513054659d2f0f81b400baa420be194c51fb850490b052c27391a6f`.
- `docs/chapters/03-methodology.tex` and `docs/chapters/04-work-plan.tex`: adjusted table cell padding and changed slash-separated table labels to equivalent prose so columns wrap; no study design, threshold, count, or claim changed. Final SHA-256 values: `f74eb0400f94db683239cb423578f991dec0fd7ea6ccefb8a2b208f82d5321bf` and `ecbe2a096bb12798c882252dc2c03e797412e54301455d83ea3b392992b40030`.
- `docs/tools/build-report.sh` and `docs/README.md`: documented and implemented the reproducible local build fallback. Script SHA-256: `b964e56fa9ec21c4543066b99acfb6e818fa2e72834b5a66328f6652fefc4dfa`.

## Remaining submission checks

The only final compiler warning is intentional: **TeX Gyre Termes is embedded as a draft proof fallback because Times New Roman is unavailable here**. The cover states this plainly; exact font compliance requires a genuine Times New Roman installation and rebuild. The declaration remains unsigned and its wording requires institutional approval. Project group, department, faculty, and the retained 27 October 2026 report date require researcher confirmation. These are visible document fields, not build failures. No pilot or main-study work was executed for this review.

# Final content review — report-writing plan

**Reviewed:** 31 October 2026. **Reviewer:** separate Sol content pass after Luna drafting and Sol synthesis. **Status:** passed for separate build and visual review after the three focused corrections below were applied and rechecked. This review checks the editable plan's scientific claims and internal consistency. It is not independent human scientific or institutional approval, and it does not report a TeX build or study execution.

## Snapshot reviewed

The active build route in `docs/main.tex` is cover, title, declaration, abstract/keywords, contents, list of figures, list of tables, abbreviations, Introduction, Literature Review, Research Methodology, Work Plan, Conclusion, then References. The old results/profiler/acknowledgements/appendix scaffolds are not input by `main.tex`. Source comparison used `task 1/Research Management/{Research Plan,Finite Pilot Protocol,Study Source Map,Zotero Verification Queue}.md`, the decision-critical Source Appraisals, and `docs/format.pdf`.

| Reviewed file | SHA-256 |
| --- | --- |
| `docs/main.tex` | `02e076d7d34072b3bdf8d25c119d13c7008c65935cd9e8e714ecbacc1b6d1494` |
| `docs/config/metadata.tex` | `a565c7bc9614af820b7f5df30e64e45f170e1f7291ffb80507c91735f692177b` |
| `docs/config/report-format.sty` | `60067e0b3c2d7ff039e67902b99a300555d83956ba25913683d311040515ee71` |
| `docs/frontmatter/cover.tex` | `966179f15ba7024780947e2aaa6da78b63ca8cbc8d35f9496364bfd58c2a2f4c` |
| `docs/frontmatter/title.tex` | `06eb76b51db315bdb99c054b617b631f91918c79b747e90e80f66d838b274e7c` |
| `docs/frontmatter/declaration.tex` | `889028110a2053c110964754763ab3980a7aaea6c7f6245ddf933ebffa75975c` |
| `docs/frontmatter/abstract.tex` | `9e2b1c8e6fe89776beef9501f1f718097a20235d7c022709e6f5668047486d82` |
| `docs/frontmatter/symbols-and-abbreviations.tex` | `775e703ea8458cd581b43f26ce1e4efbf01a686d73506b91236e4c9bb338fc69` |
| `docs/chapters/01-introduction.tex` | `a2acad8b24e500b26d37990e4cf83ea1ee0a0684c51829195eeb78c9045d9d` |
| `docs/chapters/02-literature-review.tex` | `88222c66d62a32e2cdce6a778c9beee0ef553d43d9ba57e5cd4ab41c97e591b0` (corrected snapshot) |
| `docs/chapters/03-methodology.tex` | `73b63ca5c727d48ca5da0c7ca50656c33a8fad4f7ca4ef0a8d379be041d8aaf5` |
| `docs/chapters/04-work-plan.tex` | `5bfe9687d9147cfabf5744849c751e8f535804b488a95f0a8924d0483dcd53fc` |
| `docs/chapters/05-conclusion.tex` | `2aa3f399f454b78cce49f35f064996373663a3b5f3bcc20ac20c993040d84bc1` |
| `docs/references.bib` | `812d984c413f9c41d653091539d42d3ca7f5de91856f4dfdb242e5f7772fa7b5` |
| `docs/figures/episode-evidence-chain.tex` | `110de16a1ba4f46234fbc8ce01c152e645b80e932adbf369abbd872032c6d60c` |
| `docs/figures/hindsight-trace-lifecycle.pdf` | `8a408186f1eee92459dffdbdb738028a23cb330d05ac9711a8dd8f323b46d621` |
| `docs/figures/provenance.json` | `c613228feb854d9acb3ac69a0b34bbc94a5e57dd5b5c325c54dcbabb35674494` |
| `docs/source-manifest.json` | `9b5e5ab8aea62f7f814199ab8183d2d631bd9ea9bfdab8f9d023959b45014306` |
| `docs/zotero-export-manifest.json` | `4e157f13065915fdb57cefa3039682e55d4e569ca476468e0c2a68a4445ae46c` |

## Corrections resolved before build

1. **Layout Instability citation corrected.** The Event Timing/Layout Instability sentence now cites `I8L7FN9V,R2U9EAFA`; `KEJFZJHV` remains on the separate Long Tasks sentence.
2. **Reference release qualified.** The attribution sentence now says “documented web-vitals v5.1.0 attribution build,” preserving the source appraisal's reference-release boundary.
3. **Pilot choices distinguished from open decisions.** The paragraph now states FP-0.1's proposed LCP endpoint and median + max(100 ms, 3 × unscaled MAD) rule, requires qualification and locking, and leaves runtime mapping/finalization and main-study thresholds/aggregation open.

## Findings supporting the content gate

- The question, aim, H1/H0, five objectives, C-minus-B intermittent contrast, original-episode unit and all verified eligible denominator match the Research Plan. The methodology keeps missed alerts, failures, abstentions, late claims and exhausted policies in that denominator. It separately accounts for unresolved labels and unattempted cases after a global stop.
- The independent intervention/execution checks are hidden from strategy inputs; a rich trace is not used as the cause oracle. A retains legitimate original attribution and B retains A evidence. C starts capture before the event, charges every pilot audit export and records bounded loss; E has a separate allowance and is neither oracle nor assumed upper bound.
- FP-0.1's two fixtures, eight scenarios, 64 blocks, 652 planned and 700 maximum starts, visit/deadline/resource limits, conditional repair and descriptive-only analysis are represented as proposed pilot choices. No pilot or main-study result, confirmatory estimator, powered sample size or analysis freeze is invented.
- The closest-work account respects the checked source versions: Vesper includes its contrary tested-corpus observation; WMF's endpoint is anomaly-bin detection; Hindsight is distributed-system original-event retention; WebREC distinguishes replay from analysis of recorded execution; LMAT, Shahedi and Paradyn retain their three bounded source holds. The gap remains conditional.
- The guide has no official declaration wording. The draft is visibly unsigned; project group, department and faculty remain unresolved. The retained 27 October report date is labelled for confirmation beside the 31 October plan-preparation date. TeX Gyre Termes is explicitly a draft proof fallback, not Times New Roman compliance.
- Read-only citation inventory found **46 distinct cited parent keys**, all present in the **180-entry** retained Zotero bibliography. The 23 individually read focal records and the broader export are separately described. The Hindsight source-file SHA-256 matches `figures/provenance.json`; its single included crop is attributed to original Figure 2, PDF page 6 / printed page 325. The original TikZ flow is identified as proposed design, not observed data.

## Recheck and handoff

The corrected paragraph was re-read against FP-0.1 and source appraisal SC-C09, its citation keys were checked against the bibliography, and `git diff --check` reported no whitespace error for the modified chapter. This content gate is passed for a separate Sol build and visual-review pass. Any scientific wording added during build should return for content review. The builder must verify citations, figure provenance and formatting in the compiled PDF, including the unresolved font and administrative fields; compilation cannot establish submission or scientific approval.

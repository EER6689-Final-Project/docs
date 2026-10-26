# Reproducibility and Replicability of Web Measurement Studies

## Identity and access

- **S-0011**, R3/R4/R6. Nurullah Demir, Matteo Große-Kampmann, Tobias Urban, Christian Wressnegger, Thorsten Holz, Norbert Pohlmann. WWW 2022, published pp. 533–544; DOI **10.1145/3485447.3512214** (visible on PDF p. 1).
- Zotero My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), work **RB93JMBB**, attachment **IHAL8PAA**. Existing legitimate attachment copied to `Demir 2022.pdf`; computed SHA-256 `8ff093073f7bfcf2fd765fd0df13facdb1447be0929e6d3f674238039bac466f` (corrects malformed handoff transcription).
- Original attachment has **12 PDF pages including appendices**, checked with `pdfinfo`; PDF p. 12 is Appendix C. Main text lacks printed numeric page footers. Cite **PDF pages and sections** below; published-page correspondence is not visually verified. Do not infer the page count from text form-feed splitting: embedded control characters produced spurious page segments in preliminary extraction. Official author URL supplied by Luna: <https://intellisec.de/pubs/2022-www.pdf> (not newly fetched here).
- Sol, 2026-10-25, `ERP-2026-10-25-v1.0`: actual text rechecks PDF pp. 1, 5–6; p. 6 visually inspected. Attempted text inspection p. 8 was incomplete/garbled and is not used for retained findings. Luna previously read pp. 1–12; neither pass is a whole-paper independent scientific review.

## Claim-to-source extraction

### C-T1.6-051 — Visits across profiles are not unique pages

**Proposed claim:** Demir's roughly 4.5M successful page visits are aggregated across browser profiles, not 4.5M unique pages. The paper separately reports 178,452 pages satisfying its cross-profile inclusion threshold.

**Exact original anchors:** §4.2.2, PDF p. 6: “Across all profiles, we successfully visited 4.5M pages on 8,883 sites.” The preceding sentence reports 10k distinct sites and 182,586 subpages including landing pages. The subsequent paragraph says only pages with at least 17 successful crawls across 24 profiles are considered, followed by “178,452 (92%) of the analyzed pages fall into this category.”

**Denominator interpretation:** “Across all profiles,” the per-profile mean in that paragraph, and the much smaller corpus make repeated profile-visit instances the defensible interpretation of 4.5M. The original wording is “pages”; do not quote it as “unique pages.” Do not reconstruct or silently repair the reported 92% denominator from the 182,586 count: the retained claim uses the absolute analyzed-page count and threshold, not that percentage as a recomputed fraction.

**Methods context:** §4.1, PDF pp. 5–6: four browser modes, three regions, two interaction conditions; text starts with “25 different setups” but continues with 24 and the described crossing yields 24. Tranco top-10k frame, first 25 subpages if possible, coordinated VM visits. Landing-page starts are coordinated but later page visits are not synchronized. Units are sites, URLs and repeated profile observations, not independent human participants.

**Construct/comparator:** §4.2.1 p. 6 concerns tracker/request and CSP sets; cross-profile pairwise Jaccard similarities are averaged per page. No timing-profiler conformance or general performance effect size is established. Exact formulas and figures are not transcribed/used here.

**Support: qualified** (explicit count/threshold confirmed; repeated-instance interpretation contextualized; internal percentage/setup wording retained as caveats). **Methodological confidence: limited**: selected ranked frame, profile-dependent missingness and asynchronous live visits constrain causal and population inference. Dependency group `DG-Demir-profiles`: same URLs/infrastructure across profiles; Tranco upstream frame links S-0010/S-0021. These are dependent comparisons, not independent replications.

**Conditional project inference:** If approved, document URL-level inclusion and every profile's failures separately; do not use visit totals as unique workload counts or transfer tracker differences into profiler timing effect sizes.

## Design-specific appraisal

- Identity/access **adequate**: original author/citation page and attachment hash checked.
- Sampling/missingness **concern**: ranked sites, heuristic subpages and success threshold select the analysis corpus.
- Time/content equivalence **concern**: p. 6 states subpage visits are not synchronized; live content may vary.
- Construct definition **adequate** for observed request/CSP comparisons; **concern** for extrapolation to timing/memory correctness.
- Unit/dependence **concern**: repeated observations share sites, profile infrastructure and time; independence is not established by arm count.
- Estimator uncertainty **unclear** for broader proposed profiler inference; not evaluated or reproduced in this bounded read.

## Passage QC — QC-051

Sol, 2026-10-25, original PDF text plus visual p. 6; separate passage pass after Luna, **not independent human/scientific review**. **checked-corrected**: removed unique-4.5M-pages implication and unverified printed-page anchors; disclosed manuscript pagination and “25”/24 wording. Recomputed attachment hash corrects malformed handoff transcription; a pre-copy hash assertion caught the typo before any PDF was written. Source-wide finite retained set rechecked: C-T1.6-051 only. Other numerical results from Luna are not promoted. No scope or gate approval.

## Copy receipt

Source: `/home/mendydias/Zotero/storage/IHAL8PAA/Demir et al. - 2022 - Reproducibility and Replicability of Web Measurement Studies.pdf`; new target `Demir 2022.pdf`, 611,152 bytes. Exact bytes preserved; source/target SHA-256 checked, no existing target overwritten.

Final pagination self-audit corrected a draft 15-segment/12-page confusion: `pdfinfo` reports 12 actual pages; page-bounded extraction confirms retained §4.1 on PDF p. 5 and §4.2.2 on PDF p. 6. It also inspected actual PDF p. 12 solely to identify appendix pagination, not to promote extra methods claims. The finite expansion C-T1.6-050–053 revalidated each retained supporting-PDF anchor (see Tranco QC receipt). This correction is part of QC-051's **checked-corrected** self-audit, not independent review.

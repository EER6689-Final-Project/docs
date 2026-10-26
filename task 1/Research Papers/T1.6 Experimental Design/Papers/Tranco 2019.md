# Tranco: A Research-Oriented Top Sites Ranking Hardened Against Manipulation

## Identity and access

- **S-0010**, R3/R6. Victor Le Pochat, Tom Van Goethem, Samaneh Tajalizadehkhoob, Maciej Korczyński, Wouter Joosen; NDSS 2019. DOI **10.14722/ndss.2019.23386**, printed on original PDF p. 1.
- Original: <https://tranco-list.eu/assets/tranco-ndss19.pdf>. Local deliverable: `Tranco 2019.pdf` (**15 PDF pages**, checked with `pdfinfo`). SHA-256: `98db36f5d41fe44b67fdb4c41146c3d3f8343b58ec5d323f2a364c8c5df3b095`.
- Work has no paper-record key independently resolved in this pass. **A3AT7C2E is the separate live webpage S-0021**, not an alias of this paper.
- Sol, 2026-10-25, `ERP-2026-10-25-v1.0`: reopened original text pp. 1, 12–13; visually checked p. 1. Keyword navigation elsewhere is not full-paper review. Luna's earlier extraction is provenance, not independent human review.

## Claim-to-source extraction

### C-T1.6-050 — Permanent configuration-specific ranking references

**Proposed claim:** The 2019 paper describes preserving the exact domain list and its configuration through a permanent short link; this supports reproducible ranked-domain frame identification, not an all-web probability sample.

**Original assertion:** §VI.B.3, “Reproducibility,” printed/PDF p. 13: “Once a list has been created, a permanent short link and a preformatted citation template are generated for inclusion in a paper.” The following sentences say the link provides the exact domain set, configuration and component-ranking methods. §VI.B opening, p. 12, explicitly describes configurable lists and permanent records. Abstract/introduction p. 1 identify the historical provider rankings and their potential biases.

**Interpretation/transfer:** If a ranked-domain corpus is approved, preserve list ID, date, provider/filter configuration, actual selected URLs and exclusions. Frozen domains do not freeze page content or make origins/pages/users interchangeable sampling units. This is a conditional design inference, not a paper-prescribed browser-profiler design.

**Design/context:** Ranking construction and empirical ranking assessment; upstream commercial/provider data, not randomized browser trials. Unit for this retained claim is the archived domain list/configuration. Browser version, timing estimator and run-level replication are not applicable to the archival-mechanism claim. No numerical ranking-effect estimate is retained here.

**Support:** **qualified** (archival mechanism confirmed; population inference is explicitly bounded). **Methodological confidence: higher** for the described mechanism, **limited** for transfer to browser evaluation. Dependency group `DG-Tranco`: shares authors/service with S-0021; not independent corroboration. Demir S-0011 also uses a Tranco frame, not an independent all-web sample.

## Design-specific appraisal

- Identity/version **adequate**: paper title/authors/DOI visible; fresh official retrieval matched the scratch hash.
- Sampling/generalization **concern**: popularity-ranking selection and opaque upstream panels do not establish all-web coverage.
- Archival definition **adequate**: exact list and configuration explicitly described; actual service implementation not tested here.
- Historical/current equivalence **concern**: S-0021 describes changed providers; do not import current service composition into 2019 results.
- Uncertainty/independent replication **not applicable** to the narrow mechanism description; no empirical result independently reproduced.

## Passage QC — QC-050

Sol original-passage recheck, 2026-10-25; separate agent passage pass after Luna, **not independent scientific/human review**. **checked-corrected**: separated S-0010 paper from S-0021 webpage and corrected handoff's swapped PDF hash labels. Finite source-wide retained set checked: C-T1.6-050 only. No gate, broad search, novelty or scope approval follows.

## Copy receipt

Source: `/tmp/opencode/eei6689-t16-supporting/tranco-paper.pdf`; new target `Tranco 2019.pdf`, 650,399 bytes. Exact bytes preserved; source/target SHA-256 checked, no existing target overwritten. Sol's fresh official download `/tmp/opencode/eei6689-t16-supporting/tranco-official-sol.pdf` has the same hash, independently confirming the corrected hash-to-work association (not independent scientific review).

Final editorial/pagination self-audit corrected a draft page-count error using `pdfinfo`. Because text segmentation could affect PDF anchors, the check expanded to all four supporting-PDF claims C-T1.6-050–053: page-bounded original extraction explicitly revalidated Tranco pp. 12–13, Demir pp. 5–6, Klotski pp. 3/10 and Polaris pp. 8/11. All retained anchors remained valid; no inferred text-segment page count is used.

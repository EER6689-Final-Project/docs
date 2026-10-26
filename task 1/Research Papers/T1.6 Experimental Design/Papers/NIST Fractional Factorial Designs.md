# NIST/SEMATECH — Fractional factorial designs

## Identity and access

- **S-0020**, R4/R6. NIST/SEMATECH e-Handbook §**5.3.3.4**; My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), webpage **GYIRB4X5**.
- <https://www.itl.nist.gov/div898/handbook/pri/section3/pri334.htm>, live official full returned text re-opened by Sol **2026-10-25**, no immutable revision/hash captured. Prior Luna raw extraction: `/tmp/opencode/eei6689-t16-supporting/raw/nist-fractional-factorial.json`. No original PDF attachment in prior metadata; no substitute produced.
- `ERP-2026-10-25-v1.0`; read bounds: this introductory page only, not linked fraction selection, resolution or aliasing sections. No formulas or numerical examples used.

## Claim-to-source extraction

### C-T1.6-059 — Deliberately selected fraction, not arbitrary dropped cells

**Claim:** The handbook describes fractional factorial designs as adequately chosen subsets of full-factorial treatment combinations; the introduction alone does not establish a specific alias structure or justify arbitrary missing cells.

**Original anchors:** **Full factorial experiments can require many runs** quotes the ASQC (1983) glossary definition: “A factorial experiment in which only an adequately chosen fraction of the treatment combinations required for the complete factorial experiment is selected to be run.” This is NIST's attributed quotation; ASQC original not independently inspected. **Later sections will show how to choose the ‘right’ fraction…** says selection requires strategies suited to purpose, and properly chosen two-level fractions can be balanced and orthogonal. **2-Level fractional factorial designs emphasized** bounds the page's emphasis.

**Methods/assumptions:** Statistical design guidance, not browser observations. No alias-resolution guarantee, treatment-interaction identifiability, repeated-measure estimator or missing-run rule is extracted. Do not treat accidental crawl failures as a designed fraction or orthogonality as independence of browser observations.

**Conditional inference:** If a reduced design is approved, choose/disclose estimands, fraction, defining relation/resolution, alias tradeoffs and handling of missing runs before collecting. This page supports the need for purposeful selection, not a chosen project fraction's validity; additional original methods would be required.

**Support: confirmed** for the handbook's introductory definition; **qualified** for browser transfer. **Methodological confidence: higher** for attributed definition, **indeterminate** for any specific unchosen browser fraction. Dependency group `DG-NIST-design`, same upstream handbook as S-0017–S-0019, not independent browser validation.

## Appraisal and QC

- Definition/scope **adequate**: deliberate selection and two-level emphasis explicit; original ASQC version **unclear** beyond NIST attribution.
- Alias/model/interaction assumptions **unclear** for a concrete design: not established on this introduction.
- Dependence/missingness **concern** for automatic browser transfer; dropped cells are not automatically a valid fraction.
- Normative/version scope **adequate** as attributed handbook guidance; immutable revision **unclear**.
- Browser empirical validity **not applicable**: no browser experiment.
- **QC-059**, Sol, 2026-10-25: **checked-no-discrepancy** for C-T1.6-059; original definition and selection/scope paragraphs reopened. No numeric examples or uninspected alias claims retained. Separate pass after Luna, **not independent human/scientific review**. No gate or scope approval.

# Tranco — live ranking service

## Separate identity and access

- **S-0021 (auxiliary)**, R3/R6. **Substantively different document from S-0010**, the 2019 NDSS paper. My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), webpage **A3AT7C2E**, <https://tranco-list.eu/>. It links the paper but is not its published text or a paper-record alias.
- Sol re-opened full official home page **2026-10-25**. Mutable current-service documentation; no immutable revision/hash captured, no list generated/downloaded, no ranking API behavior validated. Luna's previous reading is provenance only. No original webpage PDF attachment identified; none fabricated.
- `ERP-2026-10-25-v1.0`; retained evidence: opening provider-update notice, **Access the Tranco ranking**, **Updates**, and **About this service**. No linked methodology/code audit.

## Claim-to-source extraction

### C-T1.6-060 — Current service is not fixed 2019 provider composition

**Claim:** The live service offers permanent references to exact configured lists, but its documented upstream composition has changed since the 2019 paper. A citation to “Tranco” alone does not identify a unique sampling frame.

**Original anchors:** Opening notice says CrUX and Cloudflare Radar were integrated from the daily list of **August 1, 2023**, and Alexa removed because unavailable. **Access the Tranco ranking** offers standard, subdomain, historical and configurable lists and permanent IDs. **About this service**: “We archive all generated rankings and supply a permanent link to a page with additional information on the methodology behind the ranking and the ability to download the exact same list as was used in the study.”

**Important boundary:** The page advertises averaging four rankings for its standard list while attribution names five providers and Farsight's default-list restriction. This pass does not resolve all composition details or infer any selected list's inputs from a generic headline. Preserve the list-specific configuration if a corpus is approved. The currently served webpage cannot retrospectively prove historical inputs beyond its stated update history.

**Design/unit/metric:** Service documentation of ranked-domain lists, not a browser load experiment or probability sample of all pages/users. Permanent list retrieval is a reproducibility mechanism, not evidence that selected page content stays constant. No benchmark estimate, effect size or uncertainty inferred.

**Support: qualified** (service archive/update statements confirmed; precise selected-list composition requires its configuration). **Methodological confidence: higher** for current documented availability/history, **limited** for implementation and historical/all-web inference. Dependency group `DG-Tranco`: shared authors/service with S-0010, not independent corroboration.

## Appraisal and QC

- Work identity **adequate**: clearly separate live page and linked paper.
- Version/configuration **concern**: mutable page, changing providers, headline/attribution not a complete list-specific recipe.
- Archival definition **adequate**: permanent exact-list mechanism stated; actual retrieval fidelity **unclear**, not tested.
- Sampling/generalization **concern**: domains selected by upstream popularity data are not pages/users sampled with known probabilities.
- Causal allocation/uncertainty **not applicable** to current documentation.
- **QC-060**, Sol, 2026-10-25: **checked-corrected**, source-wide retained set C-T1.6-060 re-opened; separated work identity from S-0010 and retained provider-history caveat rather than claiming immutable 2019 composition. Separate original-page pass after Luna, **not independent human/scientific review**. No scope/gate approval.

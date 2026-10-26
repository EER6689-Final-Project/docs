# HTTP Archive — Web Almanac 2025 Methodology

## Identity and access

- **S-0016**, R3/R6. Official Web Almanac 2025 methodology: <https://almanac.httparchive.org/en/2025/methodology>.
- My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), work/webpage key **BCIWQ2PK**. This correct eight-character key is supplied by the orchestrator's **Q110 census**; Sol did not repeat that census. Luna's handoff invented `BCIWZQ2PK` (nine characters) and then reported a mismatch. **There is no real library-key issue established by that failed lookup.** No library mutation performed.
- Sol re-opened official full webpage 2026-10-25, especially **About the dataset**, **Websites**, and **Lighthouse**. Edition 2025, default dataset July 2025; mutable webpage without captured immutable revision/hash. No BigQuery data, chapter-specific queries, linked sources or ebook PDF independently analyzed. No substitute PDF created.
- Extractor Sol, `ERP-2026-10-25-v1.0`; Luna's earlier extraction is not independent human review.

## Claim-to-source extraction

### C-T1.6-055 — Website count and lab-frame boundary

**Claim:** The 2025 methodology reports **16,213,084 websites**, not that many unique pages, in a CrUX-derived dataset, with overlapping desktop/mobile subsets and chapter-specific page-selection differences. Its lab crawl does not directly represent field-user experiences.

**Original anchors:** **Websites** starts “There are 16,213,084 websites in the dataset” and says most are in both desktop/mobile subsets. It says URLs are sourced from the Chrome UX Report. Subsequent paragraphs identify recent secondary-page inclusion and say some chapters use only home pages. Final paragraph: “All pages are tested with an empty cache in a logged out state, which may not reflect how real users would access them.” Same paragraph calls HTTP Archive a lab testing tool operating from a datacenter, not real-world user-experience collection. **About the dataset** identifies the July 2025 crawl unless a chapter states otherwise. **Metrics** separately identifies CrUX use for real-world experience metrics: do not erase that distinct field-data component when describing the lab crawl.

**Construct/unit/design:** Descriptive crawl/corpus methodology; site-level count versus page-level measurements. Desktop/mobile overlap prevents summing subsets as unique sites. CrUX eligibility and selected URLs restrict the frame; page-selection policy is chapter-dependent. No random allocation or causal optimization evaluation. **Lighthouse** describes a distinct test and July 2025 version **12.8.0**; this does not establish every HTTP Archive metric came from Lighthouse.

**Support: confirmed** for documentation/count and lab conditions; **qualified** for all-web representativeness. **Methodological confidence: higher** for explicit documented frame/conditions, **limited** for broader population inference. Dependency group `DG-HA2025-CrUX`: chapters/crawl/CrUX-derived selection share upstream infrastructure; the methodology is not an independent validation of those tools.

**Conditional inference:** If a corpus is approved, freeze the exact dated dataset/query and distinguish origins, selected pages, visits and field distributions. Do not choose a sample size from the headline website count alone.

## Appraisal and QC

- Version/definition **adequate**: year, default crawl and explicit site count; immutable webpage revision **unclear**.
- Sampling/generalization **concern**: CrUX-derived frame, page selection varies, datacenter/logged-out/empty-cache conditions.
- Metric provenance **adequate** as documented distinction between tools and separate field source; implementation fidelity **unclear**, not rerun.
- Causal allocation/independent replication **not applicable** to descriptive documentation; shared upstream dependence disclosed.
- **QC-055**, Sol, 2026-10-25: **checked-corrected**. Rechecked all retained C-T1.6-055 numeric/scope statements at original headings, corrected count noun and handoff-only key-mismatch story. Key correction relies on orchestrator census Q110, not a new Sol library observation. Separate original-page pass, **not independent human/scientific review**. No gate or scope promotion.

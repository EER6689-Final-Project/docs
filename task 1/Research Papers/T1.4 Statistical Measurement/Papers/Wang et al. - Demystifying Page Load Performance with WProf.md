# Wang et al. 2013 - Demystifying Page Load Performance with WProf

- **Citation:** Xiao Sophia Wang, Aruna Balasubramanian, Arvind Krishnamurthy, and David Wetherall. “Demystifying Page Load Performance with WProf.” In *Proceedings of the 10th USENIX Symposium on Networked Systems Design and Implementation (NSDI ’13)*, 473–485. USENIX Association, 2013.
- **Zotero keys:** `D568X6SQ` and `JNNJZS5L` (duplicate records for the same source; one note and one PDF retained).
- **Provenance:** Both Zotero records list the same title/authors/abstract and provide the same named PDF. The PDF identifies the USENIX NSDI ’13 paper. The journalArticle type in Zotero does not match the venue shown in the source.
- **Source access:** Read the attached Zotero PDF via `zotero_get_item_fulltext` and the methods/conclusions pages with `zotero_read_pdf_pages`. Text extraction can garble tables and plots; quantitative findings below are limited to clear prose and the abstract.

## Abstract and scope

WProf is an in-browser profiler that builds a dependency graph across network, HTML parsing, JavaScript/CSS evaluation, and rendering work. The authors use critical-path analysis to investigate page-load bottlenecks and compare caching, SPDY, and mod_pagespeed settings.

## Outline Summary

- **Approach and sample:** WProf models dependency constraints among browser activities and instruments page loads for critical-path analysis. The study covers 350 Web pages and controlled settings, including end-host cache state, network RTT/bandwidth, SPDY, and mod_pagespeed. Some experiments use top Alexa pages; controlled server experiments download embedded objects to avoid third-party changes, and dynamically generated objects are handled with HTTP 404 responses (Sections 3–5).
- **Results:** Computation accounts for as much as 35% of the critical path in the studied pages, and synchronous JavaScript can block parsing. Cached-object count does not directly predict page-load improvement because many object loads are off the critical path. In their tests, SPDY helped at high RTTs but not low RTTs; mod_pagespeed provided little average benefit in the evaluated setup (abstract and Section 5).
- **Limitations:** Results are tied to a 2013 browser/toolchain, 350-page sample, and controlled network/server conditions. The handling of dynamically generated requests and locally hosted objects constrains realism for those experiments. The paper evaluates causal structure and optimization behavior; it is not a study of repeated-run uncertainty or a validation of current browser timing APIs.
- **Author-stated caveats:** The model abstracts browser activity dependencies, and optional SPDY features requiring page-specific knowledge are excluded. The authors say improving SPDY and leveraging those optional techniques are future work (Section 5.4.1).
- **Relationship to T1.4:** Provides browser-specific context that page-load observations combine network and computation on a dependency graph; a measurement should retain the browser, network, page set, and cache settings that condition its result. It does not prescribe a statistical estimator or repetition count.
- **Concise takeaway:** Page-load time depends on the critical path through network and browser computation, so summary metrics and comparisons are conditional on pages and experimental settings.

## T1.4 Evidence Check

- **Paper-supported:** The WProf dependency model, 350-page study, tested settings, and conditional findings are explicit in the source.
- **Not established:** Generalization to today’s browsers/sites or adequate statistical precision from any stated repetition count.
- **Researcher inference:** Preserve page-set and browser/network/cache conditions as analysis dimensions and assess repeated-measure uncertainty separately.

## T1.6 reuse check - 2026-10-25

**Extraction:** Sol (AI), 2026-10-25; `ERP-2026-10-25-v1.0`; `S-0001`; R3/R4/R6. This appended, claim-bounded check preserves the historical summary. Local NSDI PDF, `Wang et al. - Demystifying Page Load Performance with WProf.pdf`; existing Zotero aliases `D568X6SQ` / `JNNJZS5L` were not re-resolved against a live library.

- **C-T1.6-090 / QC-090:** In §5.1, printed p. 479 / PDF p. 7, the authors report the minimum PLT from five runs and results from 150 complete-run websites among the top 200 Alexa sites, excluding sites affected by reported Selenium hangs. This is the study's aggregation and completion rule, **not** a universal adequate repetition count. Its per-experiment denominator must not be replaced by the historical overall study count. **Support outcome: confirmed** for this bounded methods description; **methodological confidence: limited** for browser-design reuse because minimum selection does not characterize run-to-run uncertainty and complete-case selection restricts the observed page population.
- **C-T1.6-091 / QC-091:** §5.4.1, printed p. 482 / PDF p. 10, describes controlled SPDY experiments on the authors' own server using downloaded page objects; its footnote says unavailable dynamically generated objects receive HTTP 404 responses. §5.4.2 uses that setup for mod_pagespeed; §5.5, printed p. 483 / PDF p. 11, describes alternate settings. **Support outcome: confirmed** for the setup, not for equivalence to live browsing; **methodological confidence: limited**, because hosting and missing dynamic objects change the workload being evaluated.

**Design-specific appraisal:** setup/cache/network description **adequate** for identifying the reported conditions (cold cache, shaped network, Selenium and instrumented/default Chrome; §5.1); sampling/missingness **concern**, because completion exclusions are not representative-user sampling; uncertainty/independent repetitions **concern**, because reporting a minimum does not establish precision or independence; allocation/order **unclear** in the checked passages; contemporary browser transfer **concern**, because these are the paper's historical toolchain and pages, not a current-browser validation. Formula/table numerical results **not applicable** to these claims: none reused.

**Dependency and transfer:** `DEP-WPROF-LOCAL` groups this note, both record aliases, and the same WProf experiments; cross-topic reuse is not replication. Reviewer interpretation: preserve distinct live/controlled workload provenance, completion rules and aggregation in any T1.6 comparison. The source does not establish a project sample size, causal fixture ground truth, or representative user distribution; no design or gate choice is made here.

**Read bounds and QC:** Local `pdftotext -layout` extraction at 2026-10-25T23:22:04.650888–23:22:04.768639+05:30 covered PDF pp. 7–11 (printed 479–483), not the whole paper. SHA-256 computed from the actual local PDF: `6cc992a610a4c40d2c00844e64f70cb64d645bb5aea57c55b91af4b4a3325c9c`. PDF p. 7 was also rendered and visually checked for the sample/minimum wording and printed mapping. In a separate local reread at 23:22:39.898833–23:22:40.214158+05:30, Sol rechecked PDF pp. 7 and 10 against both new claims. `QC-090`/`QC-091`: **checked-no-discrepancy**. This is AI self-audit, not independent human review. The orchestrator-reported Kalibera guessed-pagination discrepancy expanded this check to all new reuse claims in the five canonical notes (`C-T1.6-090`–`099`); no historical access time or discovery-query ID is inferred.

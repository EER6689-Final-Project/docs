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

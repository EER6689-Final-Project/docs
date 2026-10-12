# Kalibera and Jones 2013 - Rigorous Benchmarking in Reasonable Time

- **Citation:** Tomas Kalibera and Richard Jones. “Rigorous Benchmarking in Reasonable Time.” *ACM SIGPLAN Notices* 48, no. 11 (2013): 63–74. The two Zotero records list conflicting DOIs: `GJMALCNF` lists `10.1145/2555670.2464160`; `TWKB9CAY`’s accepted manuscript gives `10.1145/2464157.2464160`. Treat the DOI/venue mapping as unresolved pending record verification.
- **Zotero keys:** `GJMALCNF` (ACM typeset/published-version PDF; journalArticle record) and `TWKB9CAY` (Kent Academic Repository author-accepted manuscript; conferencePaper record).
- **Record/version note:** The two Zotero records represent versions of the same paper, rather than independent studies. `TWKB9CAY`’s PDF identifies itself as the accepted manuscript and gives the ISMM ’13 record DOI `10.1145/2464157.2464160`; `GJMALCNF`’s typeset PDF has the same title, authors, abstract, substantive sections, and findings, but its metadata lists DOI `10.1145/2555670.2464160`. That DOI conflicts with the ACM/ISMM citation shown on the accepted manuscript and should be verified in Zotero. The two non-identical PDFs are retained separately to preserve the available versions.
- **Source access:** Read both PDFs with `zotero_get_item_fulltext` and sampled their title, methods, and conclusion pages with `zotero_read_pdf_pages`. The repository manuscript has an additional repository/version cover page; the main article text and findings are materially the same in the extracted sections.

## Abstract and scope

The paper develops a cost-aware methodology for deciding how many repetitions to use at different levels—iterations, process/VM executions, and builds—and for reporting uncertainty and effect sizes. Its examples use throughput measurements of DaCapo and SPEC CPU benchmarks on specified Java/VM and processor configurations.

## Outline Summary

- **Approach:** The authors model experimentation cost and variation at nested levels, estimate variance components, then allocate repetitions to achieve a chosen confidence-interval precision within an experiment budget. They distinguish dependent iterations within a VM execution from independent means across executions, and recommend effect-size confidence intervals for comparisons (Sections 3, 8–10).
- **Sample and conditions:** Case studies include DaCapo Java benchmarks and SPEC CPU benchmarks on several named platforms. The reported repetition counts are tied to specific benchmark, VM, platform, and compiler configurations, including OpenJDK/DaCapo and SPEC CPU with a layout-randomizing compiler; they are presented as examples to be recalculated for a new system, not universal defaults (Section 11).
- **Results:** Repetition needs vary substantially across benchmarks and platforms. The authors recommend determining repetition counts at the levels where uncertainty arises, reporting confidence intervals, and measuring each system configuration rather than adopting another study’s counts. They find that within-run iteration times can be autocorrelated and may not represent independent steady-state samples (Sections 9–12).
- **Limitations:** The examples concern execution-time benchmarking of managed-runtime and SPEC workloads on older named platforms, not browser page-load outcomes. The method requires a potentially expensive one-off variance/dimensioning study per system configuration. Manual identification of independence is described as feasible but accurate automation is left open (Section 12).
- **Author-stated caveats:** Repetition counts depend on the platform, VM, and benchmark; the authors specifically warn against using their measured counts at face value for other systems. They also note that automatic steady-state heuristics may select dependent iterations and create errors of tens of percent (Section 12).
- **Relationship to T1.4:** Provides a methodological basis for estimating required repetitions from observed variability at the correct experimental levels and reporting uncertainty for performance differences. Its numeric repetition tables cannot be transferred directly to browser profiling.
- **Concise takeaway:** Choose repetitions from a variance model fitted to the actual benchmark and platform, and report uncertainty around the effect; do not treat repetitions as interchangeable across nested levels.

## T1.4 Evidence Check

- **Paper-supported:** Nested repetition levels, uncertainty allocation, dependence concerns, effect-size confidence intervals, and the configuration-specific nature of repetition counts are explicit in the paper.
- **Not established:** A universal number of page loads or browser launches for the project’s target metric.
- **Researcher inference:** Pilot the project’s measurement pipeline, estimate variation across the levels it actually has (for example, browser process, page load, and within-load sample), and use those estimates to set repetition targets.

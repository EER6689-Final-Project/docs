# Netravali et al. 2018 - Vesper: Measuring Time-to-Interactivity for Web Pages

- **Citation:** Ravi Netravali, Vikram Nathan, James Mickens, and Hari Balakrishnan. “Vesper: Measuring Time-to-Interactivity for Web Pages.” In *Proceedings of the 15th USENIX Symposium on Networked Systems Design and Implementation (NSDI ’18)*, 217–231. USENIX Association, 2018. https://www.usenix.org/conference/nsdi18/presentation/netravali-vesper.
- **Zotero keys:** `DQUYYQXB` and `LXFQBXE3` (duplicate metadata records for the same NSDI paper; one note and one PDF retained). This is the same source as T1.1 record `HS3PKWFL`; see its existing matrix row rather than adding a duplicate row.
- **Provenance:** Both Zotero records have the same title, first/second/fourth authors and abstract, and separately attach the same named paper. The PDF and USENIX proceedings record identify James Mickens as the third author; Zotero’s creator list omits him. The venue, date, and pages below follow the paper and USENIX record.
- **Source access:** Read the attached PDF via `zotero_get_item_fulltext` and methods/results pages with `zotero_read_pdf_pages`. The PDF was published in the 2018 NSDI proceedings.

## Abstract and scope

Vesper defines page readiness around above-the-fold content being both visible and functional. Its Ready Index (RI) is a progressive measure of the fraction of that state that is interactive; Ready Time (RT) is the time until all of the above-the-fold state is interactive. The tool rewrites page HTML and JavaScript to infer the state supporting interactivity.

## Outline Summary

- **Approach and sample:** Vesper uses two page loads: a heavily instrumented first load identifies visible DOM elements and JavaScript state supporting interaction; a second, lightly instrumented load measures readiness with lower timing distortion. The evaluation compares RI/RT with page-load time (PLT), above-the-fold time (AFT), and Speed Index on a corpus of 350 popular websites under multiple emulated network conditions, including 12 Mbit/s links and varying RTTs (Sections 3–5).
- **Results:** In the tested corpus and conditions, conventional metrics could underestimate or overestimate the paper’s interactivity measure by 24%–64%. At a 100 ms emulated RTT, PLT differed from RT by about 2.2 seconds at the median; visible content could precede functional event-handling state. The separate optimization tool reduced median time to interactivity by 29%–32% in the tested cases (abstract and Section 5).
- **Limitations:** RI/RT operationalize interactivity as visibility plus functional JavaScript event handling for above-the-fold content; they do not measure every aspect of perceived usability or below-the-fold behavior. Vesper rewrites page code and uses two loads, so results depend on instrumentation coverage and page behavior across those loads. The evaluation is bounded to its 350-page corpus, tool/browser implementation, and network profiles; it is not a current universal estimate for all sites.
- **Author-stated caveats:** The design balances coverage, low overhead, and browser agnosticism. The authors use page rewriting and two-phase instrumentation because fully tracking state is heavyweight and can distort timings (Section 4). They also distinguish visible progress from functionality progress and note the potential for visible but nonfunctional controls (Section 5).
- **Relationship to T1.4:** Directly relevant to choosing and validating a browser performance outcome: visible completion and functional readiness can diverge. The paper supports making the construct explicit, but does not prove RI or RT is the right endpoint for every study population or research question.
- **Concise takeaway:** A page-load metric can disagree substantially with readiness when visible elements are not yet interactive; define the target outcome before comparing timing measurements.

## T1.4 Evidence Check

- **Paper-supported:** The RI/RT definitions, two-phase rewriting approach, 350-page corpus, emulated 12 Mbit/s conditions, and reported comparisons are described in the source.
- **Not established:** That the reported 24%–64% discrepancy or optimization gains hold for current browsers, different site samples, or the project’s target user population.
- **Researcher inference:** If the project’s construct concerns user interaction, consider a separately validated functional-readiness outcome and compare it with available visible/page-load metrics under the same page and network conditions.

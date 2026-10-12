# Georges et al. 2007 - Statistically Rigorous Java Performance Evaluation

- **Citation:** Andy Georges, Dries Buytaert, and Lieven Eeckhout. “Statistically Rigorous Java Performance Evaluation.” *ACM SIGPLAN Notices* 42, no. 10 (2007): 57–76. OOPSLA ’07. https://doi.org/10.1145/1297027.1297033.
- **Zotero keys:** `P94EL9KH` (canonical proceedings paper) and `DS3SS83A` (malformed ResearchGate scrape of the same DOI; its attached PDF extraction contains only two damaged pages and is not used).
- **Provenance:** The canonical Zotero record and attached PDF identify OOPSLA ’07. The PDF pagination is reported as 57–76, but Zotero omits pages; confirm the proceedings citation before relying on the page range.
- **Source access:** Read the attached PDF with `zotero_get_item_fulltext` and selected method, setup, and findings pages with `zotero_read_pdf_pages`. The available extraction covers only the first ten pages of the 20-page PDF; this note draws on those pages and the Zotero abstract.

## Abstract and scope

The authors compare common Java benchmarking practices and show how non-determinism, JIT compilation, garbage collection, and nested repeated iterations can make naïve summaries misleading. They propose separate procedures for startup and steady-state performance and provide JavaStats to collect repetitions and confidence intervals.

## Outline Summary

- **Approach:** The paper surveys and evaluates existing Java performance evaluation methods, contrasting summaries such as best-run or within-process iteration means with methods that quantify uncertainty. For steady state, it collects several iterations within each VM invocation, then computes confidence intervals across means from multiple VM invocations, treating those invocation-level means as the independent units. It also proposes measuring startup performance over repeated single-iteration VM invocations (Sections 3–4).
- **Sample and conditions:** The case study uses Jikes Research VM and Java workloads from SPECjvm98 and DaCapo, comparing garbage-collection strategies on specified hardware platforms. These conditions are Java-specific and from 2007; the available extraction does not justify transferring its exact sample sizes or convergence thresholds to browsers (Sections 4–5).
- **Results:** Method choices can yield misleading performance conclusions when they ignore warmup, dependence, or variation. The paper advocates reporting confidence intervals and distinguishes startup from steady-state measurements. JavaStats automates collecting data across VM invocations and reporting intervals; its estimates can remain imprecise if the available number of runs is small (Sections 3–4).
- **Limitations:** The work focuses on managed Java runtimes, selected GC strategies, and older benchmark suites/platforms. Its method quantifies random variation but does not itself remove systematic confounding or control non-determinism. The authors note that statistically rigorous collection can be time-consuming and that limited measurements necessarily produce wider intervals (Section 4.3).
- **Author-stated caveats:** Within-invocation iterations are not independent, so inference should be based on independent VM invocation means. The authors also describe their methods as applicable with a design that controls non-determinism, not a substitute for such design (Sections 4.2–4.3).
- **Relationship to T1.4:** Provides foundational support for matching the statistical unit to the dependence structure and for distinguishing startup/cold behavior from warmed behavior. It does not specify a browser-specific startup/steady-state boundary.
- **Concise takeaway:** Repeated timings within one process are not automatically independent; summarize at the level where independent executions occur and report uncertainty.

## T1.4 Evidence Check

- **Paper-supported:** The proposed startup and steady-state procedures, JavaStats behavior, nested Java measurement setup, and caution about correlated iterations are described in the paper.
- **Not established:** That browser load samples within one browser process have the same dependence structure as Java benchmark iterations.
- **Researcher inference:** Determine the project’s independent unit empirically and distinguish fresh-process measurements from repeated loads in an existing process before calculating confidence intervals.

# Vesper: Measuring Time-to-Interactivity for Web Pages

- **Citation:** Netravali, R., Nathan, V., Mickens, J., & Balakrishnan, H. (2018). Vesper: Measuring time-to-interactivity for web pages. *15th USENIX Symposium on Networked Systems Design and Implementation (NSDI '18)*, 217–231. https://www.usenix.org/conference/nsdi18/presentation/netravali-vesper
- **Zotero key:** `HS3PKWFL`.
- **Source:** Original 16-page PDF (cover + printed pp. 217–231); printed page numbers below.

## Abstract

> Everyone agrees that web pages should load more quickly. However, a good definition for “page load time” is elusive. We argue that, for pages that care about user interaction, load times should be defined with respect to interactivity: a page is “loaded” when above-the-fold content is visible, and the associated JavaScript event handling state is functional. We define a new load time metric, called Ready Index, which explicitly captures our proposed notion of load time. Defining the metric is straightforward, but actually measuring it is not, since web developers do not explicitly annotate the JavaScript state and the DOM elements which support interactivity. To solve this problem, we introduce Vesper, a tool that rewrites a page’s JavaScript and HTML to automatically discover the page’s interactive state. Armed with Vesper, we compare Ready Index to prior load time metrics like Speed Index; across a variety of network conditions, prior metrics underestimate or overestimate the true load time for a page by 24%–64%. We introduce a tool that optimizes a page for Ready Index, decreasing the median time to page interactivity by 29%–32%.

- **Abstract transcription:** Printed p. 217, with PDF line-break hyphenation normalized. “True load time” is the authors' defined *visibility-plus-functionality* target, not universal objective ground truth.

## Outline Summary

- **Central idea**
  - A visible search box may not work until its event handlers and dependent JavaScript/DOM state are ready; loading metrics based on paint alone miss that.
  - The authors define Ready Time (completion of above-the-fold readiness) and Ready Index (progressive visibility + functionality), then build Vesper to measure them.
- **Research problem and objectives**
  - Determine a testable functional definition of page readiness and automate measurement without grossly perturbing the page; compare it with PLT, above-the-fold time (AFT), and Speed Index; test an RI-directed scheduler (pp. 217–218).
  - No formally enumerated research questions.
- **Approach and experimental setup**
  - 350 sites selected from Alexa US Top 500 after filtering pages not rewriteable by Scout or measurable by Speedline; therefore not an unfiltered top-500 census (p. 224).
  - Mahimahi capture/replay; Chrome 53; mostly Ubuntu 14.04 EC2, cold cache; 12 Mbit/s, RTTs 25/50/100/200 ms; five repeated loads per trial under equal Phase-2 instrumentation; warm cache, Nexus 5, and Opera comparisons (pp. 224–226, 230–231).
  - Two-phase source rewriting: heavyweight first run discovers interactive elements and state by synthetic event dispatch; lighter second run observes when the known state appears and when it paints. Phase 1 increased load time by median 4.5%, Phase 2 by 1.9% (pp. 221–223).
  - Study 1: 73 people judged perceived rendering for 15 sites; Study 2: 85 people attempted tasks on five sites and selected the fastest variant (pp. 227–228).
- **Metrics, algorithms and results**
  - Ready Time ends when viewport elements are *both* visible and their relevant handler/DOM/JS state is available; RI integrates area-weighted readiness progress; the metric assigns equal weights to visibility and functionality (pp. 220–221).
  - Against *this operational definition*, PLT typically overestimates and AFT/SI underestimate readiness; comparisons vary with RTT and cache (pp. 224–226).
  - OPT-RI decreased median RI by 29% and Ready Time by 32% compared with ordinary loads; 83% of the task-study participants preferred OPT-RI (pp. 227–228).
- **Limitations**
  - **Author-acknowledged:** equal visibility/functionality weighting is an assumption; rewriting third-party source requires replay; synthetic event firing does not cover all paths/interleavings; nondeterministic state can differ across first/second loads (pp. 221, 223–224).
  - **Our assessment:** a handler being registered with traced state is not proof it functions correctly for every user task; filtered sites and a fixed 30-second state-discovery horizon constrain generalization; Chrome 53-era TTI and browser behavior should not be treated as 2026 definitions.
- **Author-stated future work**
  - Future empirical research may establish better visibility/functionality weights (p. 221); plugin/native implementation could reduce instrumentation overhead or combine phases; symbolic execution might improve event-path coverage (pp. 223–224).
- **Relationship to our profiler**
  - Directly relevant to *semantic validity*, versioned metric contracts, instrumentation overhead and controlled-fixture user-interaction tests; demonstrates a task-relevant construct that neither paint nor onLoad alone captures.
  - Do not conflate its Ready Index with current Web Vitals INP, or its use of the word “true” with universal ground truth.
- **Important quotations**
  - “A web page is not usable until its above-the-fold content is both visible and functional.” — p. 228.
  - “The use of equal weights reflects our assumption that functionality and visibility are equally important.” — p. 221, footnote 3.
- **Concise takeaway**
  - Specify *which* interactivity construct is measured; the required instrumentation and validation depend on that definition and can change the page itself.

## T1.1 Claim Check

- **Qualified:** The report's 24–64% disagreement applies to Vesper's defined interactive readiness in its selected/replayed corpus and experimental conditions, not to an independent universal truth or to INP.

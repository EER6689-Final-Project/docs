# Optimize along the way: An industrial case study on web performance

- **Citation:** van Riet, J., Malavolta, I., & Ghaleb, T. A. (2023). Optimize along the way: An industrial case study on web performance. *Journal of Systems and Software, 198*, 111593. https://doi.org/10.1016/j.jss.2022.111593
- **Zotero key:** `9WT3HAHJ`.
- **Source:** Original open-access PDF, 24 pages. References use PDF pages.

## Abstract

> Context: Fast loading web apps can be a key success factor in terms of user experience. However, improving the performance of a web app is not trivial, since it requires a deep understanding of both the browser engine and the specific usage scenarios of the web app under consideration.
>
> Aims: In this paper, we present an industrial case study at 30 MHz, an agricultural technology company, in which we target a large web-based dashboard, where its performance was improved via 13 distinct interventions over a four-month period. Moreover, we conduct a user study to analyse whether web performance metrics correlate with the user perceived page load time in optimization scenarios.
>
> Methods: First, we design a replicable performance engineering plan, where the technical realization of each intervention is reported in detail along with its development effort. Second, we develop a benchmarking tool that supports 11 widely used web performance metrics. Finally, we use the benchmarking tool to quantitatively evaluate the performance of the target web app and measure the effect of 13 interventions on both desktop and mobile devices. For the user study, we record six videos of different page loads and ask participants about their opinion about the time a web page is considered ready. We calculate the correlation of the user perceived data with each web performance metric.
>
> Results: We observe a considerable performance improvement over the course of the 13 interventions. Among others, we achieve 98.37% and 97.56% time reductions on desktop and mobile, respectively, for the First Contentful Paint metric. In addition, we achieve 48.25% and 19.85% improvements for the Speed Index (SI) metric on desktop and mobile, respectively. Our user study shows that the Lowest Time to Widget metric, a product-specific web performance metric, is perfectly correlated with perceived performance during the optimization process.
>
> Conclusion: This study shows the importance of a continuous focus on performance engineering in the context of large-scale web apps to improve user browsing experience. We recommend developers to carefully plan their performance engineering activities, since different interventions might require different efforts and can have different effects on the overall performance of the web application.

- **Abstract transcription:** Complete author-labelled abstract from PDF p. 1, checked against the local PDF's layout-preserving extraction; line-break hyphenation normalized. Zotero's `abstractNote` omits its Context and Aims.

## Outline Summary

- **Central idea**
  - A repeatable browser benchmark with multiple outcome metrics can guide a sequence of real product changes; a *product-specific* metric may track what this product's users actually notice better than generic metrics.
- **Explicit research questions**
  - RQ1: “How can the performance of a web application be improved iteratively?” (p. 3).
  - RQ2: “To what extent do quantitative performance metrics correlate with user-perceived performance improvements of web apps?” (p. 3).
- **Approach, dataset and setup**
  - One 30 MHz Angular dashboard, 13 cumulative interventions over four months; desktop Intel i7/Windows 10 and Samsung Galaxy S10e/Android 10, testing Chrome 80 on final replayed versions; staging with production-like CloudFront and fixed dashboard (pp. 3–7).
  - Benchmark runs each state 30 times with Lighthouse-based automation plus User Timing hooks, CPU ×4 and slow-4G settings; persistent cookies/cache because reset was deliberately disabled. Median, Cliff's delta, Mann–Whitney U and Benjamini–Hochberg adjust comparisons (pp. 6–7).
  - 11 metrics: FCP, historical First Meaningful Paint/First CPU Idle/TTI, SI, TBT, Estimated Input Latency, network-request count, DOM nodes, and product-specific Lowest/Median Time to Widget (pp. 4–6). These names/definitions are *historical* and not all are current recommended metrics.
  - Perception study: 19 employees watched six videos made from three dashboard compositions with/without browser loading indicator and pressed space when they thought each page finished (pp. 7–8).
- **Key results**
  - End-to-end FCP reductions 98.37% desktop/97.56% mobile; SI reductions 48.25%/19.85%, respectively; an intermediate chart-library switch improved runtime interaction frame rate but worsened SI by ~20% desktop/15% mobile (pp. 15, 17).
  - Only Lowest Time to Widget achieved a statistically confirmed correlation with median perceived completion in the tiny video set (p. 18). The abstract's “perfectly correlated” is about *this specific six-video, three-page product study*, not general web QoE.
  - Device-specific metric changes frequently diverged; one optimization reduced DOM size drastically while worsening page-load SI (pp. 15, 17–20).
- **Limitations and future work**
  - **Authors' threats:** one Angular app, Chrome-only, possible environmental confounds controlled by later remeasurement, limited perception sample/pages, and need for more independent industrial studies (pp. 20–23).
  - **Our assessment:** cumulative interventions confound isolated causal contributions; 19 employees are familiar insiders; six videos/three layouts are few independent workloads; persistent cache differs from cold conditions; very high FCP percentage reductions do not guarantee comparable gains in other constructs.
  - **Author-stated future:** analyze cross-device rendering paths, more browsers/pages/industrial cases, new objective/perceived metrics and framework/language effects (pp. 19, 21, 23).
- **Relationship to our profiler**
  - Reuse fixed workload, versioned runs, repeated measurements, raw distributions and explicit stakeholder-specific diagnostic milestones.
  - Treat the reported perfect correlation as a warning about *small-sample single-product associations*; not a basis for globally weighting “Time to Widget” or generic Web Vitals.
  - This is important for our individual task's transparent score: optimize for an explicit decision purpose and retain individual metrics.
- **Important quotations**
  - “there is no single metric that can be considered the best representative of web performance.” — PDF p. 20.
  - “future research should further expand our analyses using more pages to investigate whether our observations hold in terms of correlations and their statistical significance.” — PDF p. 21.
- **Concise takeaway**
  - A product-specific loading milestone can be useful in a well-defined workload; don't extrapolate a correlation from a handful of videos to every URL.

## T1.1 Claim Check

- **Qualified:** Supports the usefulness of task-/product-specific measures but only within one SPA and its tiny insider user study. Its own historical FMP/FCI/TTI definitions should not be adopted as current metric semantics.

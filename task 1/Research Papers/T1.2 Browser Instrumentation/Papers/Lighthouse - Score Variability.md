# Lighthouse Score Variability

- **Citation:** GoogleChrome/Lighthouse contributors. *Score Variability* (docs/variability.md), mutable main branch, accessed 12 October 2026. https://github.com/GoogleChrome/lighthouse/blob/main/docs/variability.md
- **Zotero key:** CWHHFA55 (LighthouseDocsVariabilitymd).
- **Source:** Repository documentation/guidance, not a research paper. The Zotero snapshot is a captured version; this note checks live main content as accessed on the date above.

## Summary

- **Purpose and content**
  - Explains that Lighthouse performance scores vary even without code changes and describes page, network, server, hardware, resource contention, and browser sources of variability.
  - Compares how simulated throttling, DevTools throttling, and no throttling mitigate those sources. Page nondeterminism is not solved by throttling; other mitigations are partial.
  - Recommends adequate and consistent hardware, isolating external influences, avoiding concurrent Lighthouse runs on the same machine, and collecting repeated runs. It suggests aggregate summaries such as the median or 90th percentile instead of treating one report as decisive. The document says the median of five runs is twice as stable as one run.
- **Research questions and evidence type**
  - N/A — practical Lighthouse guidance. It is not a reported controlled experiment or peer-reviewed study; quantitative stability statements link to a separate variability/accuracy analysis.
- **Dataset, setup, metrics, and methods**
  - N/A for an original study. The page provides qualitative source classifications, environment recommendations, and repeated-run guidance, but no newly collected dataset or reproducible statistical protocol in this document.
- **Limitations and interpretation**
  - Mutable main content may change. The guidance distinguishes environments and throttling methods but does not establish universal variance magnitudes or a sample size adequate for every site/metric.
  - Treat the five-run statement as guidance and trace its linked analysis before using it as a formal sample-size justification.
- **Relationship to our profiler**
  - **Preliminary inference:** report run distributions and environment/throttling configuration, and avoid conclusions based on an unexplained single run. This source does not prescribe our replicate count or summary statistic.
- **Important section anchors**
  - Paraphrase anchors: “Summary,” “Sources of Variability,” “Effect of Throttling Strategies,” and “Strategies for Dealing With Variance” including “Run Lighthouse Multiple Times.” No page numbers.

## T1.2 Evidence Check

- **Qualified:** Mutable engineering guidance that summarizes variability mechanisms and recommended practices; it is not independent empirical validation of Lighthouse or another profiler.
- **Preliminary inference:** Repeated-run distributions and environment records are candidates for later protocol review; their adequacy remains to be established.

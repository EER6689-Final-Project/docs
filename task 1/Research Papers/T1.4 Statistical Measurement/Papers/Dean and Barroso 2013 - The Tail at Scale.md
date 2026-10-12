# Dean and Barroso 2013 - The Tail at Scale

- **Citation:** Jeffrey Dean and Luiz André Barroso. “The Tail at Scale.” *Communications of the ACM* 56, no. 2 (2013): 74–80. https://doi.org/10.1145/2408776.2408794.
- **Zotero key:** `6H3HKLL4`.
- **Provenance:** Zotero provides a Google Research publication-page capture as an HTML attachment; it does not provide a PDF. The Google Research page identifies the authors, journal, volume, year, and pages.
- **Source access:** Read the attached Google Research HTML through `zotero_get_item_fulltext`. The Zotero record lacks journal, volume, issue, pages, and DOI fields; only the Google publication page was used to supply the journal citation.

## Abstract and scope

This article discusses latency tails in large interactive online services. It describes how transient high-latency episodes can dominate system-level responsiveness as service scale and utilization increase, and outlines tail-tolerance techniques such as redundancy and hedging to reduce their impact.

## Outline Summary

- **Approach:** The authors synthesize design principles and examples from large online services; the article is not a controlled experiment with a sampled dataset or browser benchmark methodology.
- **Claims:** Tail latency can dominate user-facing responsiveness in large distributed services even when typical component behavior is fast. The paper explains techniques for mitigating latency tails and argues these can permit higher utilization without proportionally lengthening service-level latency tails.
- **Limitations:** The article addresses distributed online-service latency, not browser page-load timing or statistical inference for repeated measurements. It does not provide a general sample-size prescription or empirical estimate applicable to the project’s field measurement.
- **Author-stated caveats:** The Google Research page frames the techniques around large online services and their distributed workloads. The article’s examples and recommendations should be read in that systems context.
- **Relationship to T1.4:** Useful background for why tail behavior can matter when the project outcome is user-facing latency. It does not establish which percentile or confidence procedure should be used for a browser metric.
- **Concise takeaway:** For interactive systems, rare slow events can matter to overall responsiveness; a central tendency alone may miss that behavior.

## T1.4 Evidence Check

- **Paper-supported:** The role of high-latency episodes in large services and the described tail-tolerance techniques are stated by the authors.
- **Not established:** The browser-level frequency or impact of tail events for the project’s population.
- **Researcher inference:** If tail responsiveness is part of the research question, specify a tail estimand in advance and gather enough observations to estimate it with stated uncertainty.

# Lighthouse — Total Blocking Time Documentation

- **Citation:** Chrome for Developers. “Total Blocking Time.” [Lighthouse documentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-total-blocking-time).
- **Zotero key:** `QHUCFVBF` (webpage; imported HTML snapshot attached as `lighthouse-total-blocking-time.html`).
- **Source access:** Current online page and saved Zotero snapshot checked 13 October 2026.

## Outline Summary

- **Operational definition:** Lighthouse documentation defines TBT as the sum of the blocking portions of long tasks between First Contentful Paint and Time to Interactive. For each task longer than 50 ms, the portion beyond 50 ms contributes to the sum.
- **Comparability:** This is a derived quantity with an explicit interval and threshold; a raw long-task duration/count or a different observation window is not the same metric.
- **Limit:** The documentation describes Lighthouse’s metric; it does not validate a custom implementation or make TTI a current recommended headline metric. The page is mutable and version-dependent.

## T1.5 Evidence Check

- **Source-supported:** TBT’s stated interval and blocking-time computation.
- **Researcher inference:** Validate an implementation against identical task boundaries and FCP/TTI endpoints before interpreting numerical agreement.

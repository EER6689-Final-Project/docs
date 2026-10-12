# Lighthouse — Time to Interactive Documentation

- **Citation:** Chrome for Developers. “Time to Interactive.” [Lighthouse documentation](https://developer.chrome.com/docs/lighthouse/performance/interactive).
- **Zotero key:** `9T8ACIJ8` (webpage; imported HTML snapshot attached as `interactive.html`).
- **Source access:** Official page and Zotero snapshot checked 13 October 2026.

## Outline Summary

- **Status and caveat:** The page states that TTI was removed as a Lighthouse metric in Lighthouse 10 because it was overly sensitive to outlier network requests and long tasks, producing high variability. It presents LCP, TBT, and INP as alternatives.
- **Historical definition:** The page describes TTI in terms of useful content, event-handler availability, and response within 50 ms; this describes the retired metric’s historical meaning.
- **Project relevance:** A historical Lighthouse output should be versioned and kept distinct from current metrics; historical TTI should not be assumed to be a current Lighthouse score component.
- **Limit:** Documentation of a retired metric does not establish current tool behavior or a custom profiler’s validity.

## T1.5 Evidence Check

- **Source-supported:** The stated removal, variability concern, and historical definition.
- **Researcher inference:** Exclude TTI from claims of current Lighthouse score comparability unless a versioned legacy target is explicitly intended.

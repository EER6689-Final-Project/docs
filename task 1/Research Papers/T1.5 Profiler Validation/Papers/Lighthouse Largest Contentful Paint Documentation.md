# Lighthouse — Largest Contentful Paint Documentation

- **Citation:** Chrome for Developers. “Largest Contentful Paint.” [Lighthouse documentation](https://developer.chrome.com/docs/lighthouse/performance/lighthouse-largest-contentful-paint).
- **Zotero key:** `QF52VUCU` (webpage; no child attachment).
- **Source access:** Current official documentation checked 13 October 2026.

## Outline Summary

- **Operational scope:** The page says Lighthouse extracts LCP data from Chrome tracing and reports it in seconds. It describes LCP as the time when the largest content element in the viewport is rendered.
- **Interpretation:** The documentation distinguishes timing from the score category and shows different lab thresholds for mobile and desktop on the page reviewed. The Web Vitals thresholds it cites use the mobile thresholds across devices.
- **Project relevance:** A custom trace-derived LCP can be compared to Lighthouse only after aligning navigation, frame, candidate selection, trace interpretation, and execution mode. A threshold label or score transformation is not itself a raw timing.
- **Limit:** Mutable Lighthouse documentation; the page does not validate an independent profiler or establish identical observed and simulated run values. The underlying LCP concept is separately documented by W3C (`6WVYFE8R`, T1.1).

## T1.5 Evidence Check

- **Source-supported:** The trace extraction statement, visible-element timing description, and displayed score thresholds at review time.
- **Researcher inference:** Keep raw LCP timing, threshold category, and overall Lighthouse score as separate outputs.

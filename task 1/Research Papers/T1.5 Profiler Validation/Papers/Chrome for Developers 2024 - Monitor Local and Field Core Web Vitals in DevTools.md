# Chrome for Developers (2024) — Monitor Local and Field Core Web Vitals in DevTools

- **Citation:** Rick Viscomi. “Monitor your local and real-user Core Web Vitals performance in DevTools.” Chrome for Developers, 17 September 2024. [Article](https://developer.chrome.com/blog/devtools-realtime-cwv).
- **Zotero key:** `FNWVG4JH` (webpage; no child attachment).
- **Source access:** Official Chrome for Developers article checked 13 October 2026.

## Outline Summary

- **Scope:** Describes DevTools Performance-panel features for viewing local Core Web Vitals and comparing them with field data.
- **Field-data basis:** The page describes CrUX data as a 28-day aggregation of real-user experiences for a URL or origin, subject to eligibility. Data can be separated by device type when enough data exist; otherwise DevTools may show all-device aggregation.
- **Interpretation:** Local and field values are contextual comparisons, not paired measurements of the same page execution. Eligibility, aggregation window, URL/origin, and device bucket affect what field value is displayed.
- **Limit:** Product feature announcement, not a controlled validation study. It does not establish that local conditions reproduce a population or that two metrics are interchangeable.

## T1.5 Evidence Check

- **Source-supported:** Feature description and stated CrUX aggregation/eligibility behavior.
- **Researcher inference:** Treat the panel as a useful reference workflow, while keeping its local run and aggregated field distribution distinct.

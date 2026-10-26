# Long Animation Frames API

- **Citation:** World Wide Web Consortium (W3C). *Long Animation Frames API*. First Public Working Draft, 28 April 2026. https://www.w3.org/TR/long-animation-frames/
- **Zotero key:** `6SJEG5G9`.
- **Source:** W3C draft specification, cited by section. Zotero snapshot and the published draft are dated 28 April 2026.

## Abstract

This draft defines a browser API for observing long animation frames that can occupy the UI thread and delay other work. This summary describes normative design material; it is not an empirical overhead or coverage study.

## Outline Summary

- **Central idea**
  - Expose long frame periods and related rendering and script timing context through `PerformanceLongAnimationFrameTiming` and `PerformanceScriptTiming` entries.
- **Problem and objective**
  - Define observable long-frame entries and attribution information for investigating main-thread congestion. The specification contrasts long animation frames with long tasks because frame entries can include a rendering phase and expose frame-level context (§1.2).
- **Approach and scope**
  - Specifies entry interfaces, processing and reporting algorithms, observer exposure, and security and privacy considerations (§§2–5). It is a Working Draft, not an experiment; dataset, participants, and experimental setup are N/A.
- **Signal and rules**
  - A long animation frame qualifies when the relevant period exceeds 50 ms (§2). Entries can expose fields such as `renderStart`, `styleAndLayoutStart`, `blockingDuration`, and script attribution.
  - The draft says implementations should advertise `long-animation-frame` through `PerformanceObserver.supportedEntryTypes` (§3). Observers can request buffered entries, but target-browser support and realized behavior must be checked.
- **Limitations and interpretation**
  - Timing is coarsened; cross-origin and opaque-script attribution is limited by the privacy model (§5). Some exposed timing details, including forced style/layout duration, are implementation-defined (§2.2). The draft supplies no measured observer cost, completeness result, or cross-browser validation.
- **Author-stated future work**
  - Not established from the reviewed specification.
- **Relationship to the T1.2 instrumentation review**
  - Provides a candidate browser-native signal for frame-level congestion and script context. Whether it is supported, complete enough, and low-cost in the selected Chromium build requires measurement.
- **Important section references**
  - Long animation frames versus long tasks (§1.2); entry fields and threshold (§2); processing and support exposure (§3); security and privacy (§5).
- **Concise takeaway**
  - The draft defines a frame-level signal and attribution fields, but does not demonstrate their realized coverage or measurement cost.

## T1.2 Evidence Check

- **Normative claim:** The draft defines the greater-than-50-ms qualification and the long-frame entry model.
- **Preliminary inference:** Check target-version support, available fields, attribution, and collection cost before using these entries as profiler evidence.

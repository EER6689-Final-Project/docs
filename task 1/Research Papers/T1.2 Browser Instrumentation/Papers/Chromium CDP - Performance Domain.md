# Chrome DevTools Protocol: Performance Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — Performance domain*, protocol documentation endpoint `tot`. https://chromedevtools.github.io/devtools-protocol/tot/Performance/
- **Zotero key:** `SU8DH5XW`.
- **Source:** Zotero snapshot saved 29 August 2026. The `tot` endpoint is mutable; pin the Chromium and protocol versions for any implementation study. The collection record describes protocol version 1.3.

## Abstract and scope

This protocol documentation defines methods and events for enabling performance metric reporting and retrieving metric name/value pairs. It does not report empirical measurement accuracy or observer cost.

## Outline Summary

- **Central idea**
  - A CDP client can enable metric reporting, request a set of current metrics, and receive metric updates through the Performance domain.
- **Problem and objectives**
  - Document protocol operations and the available time-domain configuration for performance metrics. Research questions, dataset, participants, and experimental setup are N/A for protocol documentation.
- **Approach and scope**
  - `enable` starts reporting; `getMetrics` returns name/value pairs; the `metrics` event reports updates. A `timeDomain` option can select `timeTicks` or `threadTicks` where supported.
- **Methods and interpretation**
  - Treat metric names and units as part of the result schema. Record the selected time domain and the browser/protocol version with captured values.
- **Limitations and interpretation**
  - Metric availability can vary by implementation/version. `setTimeDomain` is experimental/deprecated in the documented surface, so it should not silently become a core dependency. The protocol reference does not quantify collection cost, validity, or completeness.
- **Author-stated future work**
  - N/A; no future-work programme is established by this API reference.
- **Relationship to the T1.2 instrumentation review**
  - This is a possible source for browser metric collection. Semantics, availability, and observer overhead need separate validation for the selected Chromium build.
- **Important source references**
  - Performance domain methods and events: `enable`, `getMetrics`, `metrics`, and `setTimeDomain`; no page numbers apply.
- **Concise takeaway**
  - CDP provides a metric reporting interface, but callers must preserve metric identity and time-domain context and measure its behavior in the target version.

## T1.2 Evidence Check

- **Protocol claim:** The domain defines reporting and retrieval operations and documents time-domain options.
- **Preliminary inference:** Log returned metric names and the chosen clock domain, and validate availability and observer cost before using the values comparatively.

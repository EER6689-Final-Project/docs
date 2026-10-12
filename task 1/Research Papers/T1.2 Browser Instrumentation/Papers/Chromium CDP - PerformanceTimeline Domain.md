# Chrome DevTools Protocol: PerformanceTimeline Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — PerformanceTimeline domain*, protocol documentation endpoint `tot`. https://chromedevtools.github.io/devtools-protocol/tot/PerformanceTimeline/
- **Zotero key:** `QW7AGAGB`.
- **Source:** Zotero snapshot saved 29 August 2026. This `tot` documentation endpoint is mutable; record the Chromium and protocol versions used in any implementation study. The collection record describes protocol version 1.3.

## Abstract and scope

This protocol documentation describes a programmatic domain for enabling selected Performance Timeline event types and receiving timeline events. It defines an interface, not measured collection accuracy or overhead.

## Outline Summary

- **Central idea**
  - The domain provides a CDP path for requesting selected timeline event types and receiving `timelineEventAdded` notifications.
- **Problem and objectives**
  - Define how a protocol client subscribes to timeline events and obtains the domain’s supported event payloads. Research questions, dataset, participants, and experimental setup are N/A for protocol documentation.
- **Approach and scope**
  - `PerformanceTimeline.enable({eventTypes})` selects requested event types. The documentation describes buffered entries being reported before `enable` returns, followed by live `timelineEventAdded` events.
  - Payloads can include timeline information such as LCP and layout-shift details where supported by the protocol surface.
- **Methods and interpretation**
  - Configure event types explicitly, collect the initial buffered entries, then process subsequent events. Reconcile the boundary between buffered and live events in the client implementation.
- **Limitations and interpretation**
  - The domain is marked experimental in the protocol documentation. Its supported event types do not guarantee exposure of every web performance entry type. The `tot` endpoint changes over time, and the documentation gives no empirical completeness, accuracy, or observer-cost estimates.
- **Author-stated future work**
  - N/A; no future-work programme is established by this API reference.
- **Relationship to the T1.2 instrumentation review**
  - This is a candidate collection interface. Event coverage, ordering, buffered/live reconciliation, and overhead must be checked against a pinned Chromium/protocol version.
- **Important source references**
  - PerformanceTimeline domain methods and events, especially `enable` and `timelineEventAdded`; no page numbers apply.
- **Concise takeaway**
  - CDP specifies a subscription and event-delivery surface, while leaving realized coverage and collection cost to empirical validation.

## T1.2 Evidence Check

- **Protocol claim:** The documented domain exposes event-type selection and timeline event delivery, including buffered data as described by `enable`.
- **Preliminary inference:** Pin and report versions, specify subscriptions, and test coverage and buffered/live ordering before relying on the stream.

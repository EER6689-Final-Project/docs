# Life of a Frame

- **Citation:** Chromium authors. *Life of a frame*. Chromium source documentation, mutable `HEAD`, accessed 12 October 2026. https://chromium.googlesource.com/chromium/src/+/HEAD/docs/life_of_a_frame.md.
- **Zotero key:** `JZ6S53CX` (snapshot version 1463; Zotero access date 29 August 2026).
- **Source version:** The URL follows `HEAD`, not a pinned Chromium commit or release. Section references below were checked on 12 October 2026; record the actual Chromium revision alongside any later experimental use.

## Abstract and scope

This implementation document outlines Chromium's compositor-frame path, from BeginFrame and main-thread updates through raster, activation, compositor submission, GPU work, swap, and presentation. It explains stage dependencies and when stale content may be submitted. It does not report a controlled timing study or validate that internal timestamps equal user-visible latency.

## Outline Summary

- **Central idea:** A displayed frame passes through multiple dependent browser, display-compositor, and GPU stages; stage timestamps must be interpreted in the context of this pipeline.
- **Problem and objectives:** Explain the major steps involved in producing and presenting a Chromium frame.
- **Research questions:** N/A — implementation documentation.
- **Approach:** Descriptive account of the compositor and presentation pipeline, including BeginFrame, compositor updates, BeginMainFrame, main-thread updates, commit, raster wait, activation, submission, surface aggregation, draw, swap, and presentation.
- **Dataset and setup:** N/A. The document describes Chromium's implementation, not a measured dataset or experimental configuration.
- **Metrics and methods:** No evaluated metrics or analysis method. The document describes deadlines and stage transitions, and notes that if work misses the activation deadline, Chromium may submit the existing active tree, a possible source of a dropped frame. Presentation time may be exact on some platforms and estimated on others.
- **Limitations:** Mutable `HEAD` documentation; implementation details can change. Internal stage completion is not the same as pixels becoming visible. The page states that exact presentation timestamps are unavailable on every platform and that Chrome makes best-effort estimates (steps 16–17).
- **Author-stated future work:** Not stated in the reviewed document.
- **Relationship to the T1.2 instrumentation review:** Provides a stage map for assigning trace events and distinguishing compositor progress from actual presentation. It does not establish the cost or accuracy of probes attached to those stages.
- **Important source references:** [Steps 1–9](https://chromium.googlesource.com/chromium/src/+/HEAD/docs/life_of_a_frame.md) cover BeginFrame through submission; steps 10–17 cover display aggregation, GPU draw, swap, and presentation. Checked 12 October 2026.
- **Concise takeaway:** Frame-production timestamps describe distinct stages; user-visible presentation is later and may only be estimated, depending on platform.

## T1.2 Claim Check

- **Source-described behavior:** Missed deadlines can lead to submission of the prior active tree, and presentation timestamp availability varies by platform.
- **Preliminary inference:** A browser measurement contract should name the stage represented by each timestamp and preserve timestamp provenance. That inference needs validation against the target Chromium build and platform.
- **Phase 0 scope:** This document supplies implementation context; it does not select a presentation metric, timestamp tolerance, or research gap.

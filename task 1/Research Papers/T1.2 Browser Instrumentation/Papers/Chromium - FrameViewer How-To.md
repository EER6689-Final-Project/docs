# FrameViewer How-To

- **Citation:** Chromium authors. *FrameViewer How-To*. Mutable Chromium project documentation, accessed 12 October 2026. https://www.chromium.org/developers/how-tos/trace-event-profiling-tool/using-frameviewer/.
- **Zotero key:** `47DZSUKL` (snapshot version 1463; Zotero access date 29 August 2026).
- **Source version:** The page is not pinned to a release or commit. The page says FrameViewer requires the latest Chrome rendering architecture and may be buggy; follow its current trace-category and command-line guidance for the target build. Sections cited below were checked on 12 October 2026.

## Abstract and scope

This how-to explains how to capture and inspect Chromium frame-viewer traces. It describes per-frame layer-tree state, invalidations, and SkPictures alongside ordinary trace timing. It is an implementation and debugging guide, not an experiment measuring FrameViewer's accuracy, collection cost, or effect on a page.

## Outline Summary

- **Central idea:** Pair trace-event timing with a frame-by-frame view of rendered state to help diagnose where rendering work occurs.
- **Problem and objectives:** Help Chromium developers inspect rendering changes across frames and relate trace events to layers and invalidations.
- **Research questions:** N/A — technical how-to documentation.
- **Approach:** Describes prerequisite trace capture, version-sensitive flags/categories, the rendering pipeline, process/thread timelines, and frame-viewer interaction. The tool can expose layer trees, invalidations, and rasterized SkPicture contents for selected frames.
- **Dataset and setup:** N/A as an empirical study. The instructions use a Chromium trace with non-default categories; some features depend on impl-side painting and Skia benchmarking flags in the recording/viewing builds.
- **Metrics and results:** No evaluated performance metric or empirical result is reported. The guide describes available visual and trace context, including event duration, thread duration where available, self-time, occurrences, and frame state.
- **Limitations:** The page warns that the tool targets Chromium internals and recent rendering architecture, requires version-specific setup, can be buggy, and should not be used alone to infer whether an operation is cheap or expensive. Timing fields are not available for all events or platforms (overview and trace navigation sections).
- **Author-stated future work:** Not stated in the reviewed page.
- **Relationship to the T1.2 instrumentation review:** Useful for qualitative trace interpretation and locating candidate rendering stages. Any suspected measurement overhead or operation cost must be quantified in controlled browser runs.
- **Important source references:** Prerequisites and interpretation caveat: [overview](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool/using-frameviewer/) lines 19–49. Trace fields and per-frame layer data: same page, sections on basic trace navigation and Frame Viewer mode (lines 139–159 in the accessed page). No direct quotation is included.
- **Concise takeaway:** FrameViewer supplies diagnostic context for Chromium rendering traces; its visualizations do not themselves validate timing accuracy or instrumentation overhead.

## T1.2 Claim Check

- **Source-described capability:** With the required trace configuration, the guide describes inspecting page layer trees, invalidations, and SkPicture content by frame alongside trace events.
- **Preliminary inference:** Use the tool to localize candidate rendering work, then measure the suspected stage independently. This is a proposed review practice, not an experimental result from the guide.
- **Phase 0 scope:** Record the Chromium build, capture flags/categories, and viewer build when using this material. No profiler design or final gap is selected.

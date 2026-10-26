# Chromium - Adding Traces to Chromium/WebKit/JavaScript

- **Citation:** Chromium authors. *Adding Traces to Chromium/WebKit/JavaScript*. Undated instrumentation guide. https://www.chromium.org/developers/how-tos/trace-event-profiling-tool/tracing-event-instrumentation/
- **Zotero key:** `HUJR8W9W`.
- **Duplicate:** Zotero record `P82GMMCM` is consolidated with this note and is not counted separately.
- **Source:** Mutable, undated guide; accessed 12 October 2026. The guide contains an obsolete `code.google` link.

## Abstract and scope

This guide explains how to add trace events and JavaScript timing calls. It describes event categories and scopes, counters, IDs, and asynchronous events across threads or processes. It also makes rough enabled/disabled clock-cycle cost assertions, without specifying a controlled benchmark behind them.

## Outline Summary

- **Central idea:** Add categorized trace events around code and use event identifiers and scopes to represent synchronous, asynchronous, and counter data.
- **Problem and objectives:** Explain trace instrumentation conventions; formal research questions, dataset, participants, and empirical setup are N/A.
- **Approach:** The guide describes trace macros, categories, scoped events, IDs, counters, asynchronous events, and JavaScript `console.time`. It says macro arguments are evaluated only when tracing is enabled.
- **Cost claims:** The guide characterizes disabled trace macros as costing a few dozen clock cycles and enabled macros as costing a few thousand. It gives no hardware, workload, uncertainty, or measurement method for these approximate figures; they are documentation assertions, not a controlled result for this project.
- **Results:** N/A. No experiment is reported in the guide.
- **Limitations:** Undated and mutable; an external link is obsolete. The rough cost figures lack conditions and cannot be treated as current Chromium measurements.
- **Author-stated future work:** Not stated.
- **Relationship to T1.2:** Direct implementation guidance for trace event structure and a reason to measure trace emission cost under the target Chromium version and workload.
- **Important source references:** [Trace event instrumentation guide](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool/tracing-event-instrumentation/), including event macro and JavaScript timing sections. No page numbers.
- **Concise takeaway:** The guide documents trace instrumentation patterns and rough cost assertions; it does not provide a controlled current estimate of browser tracing overhead.

## T1.2 Evidence Check

- **Documentation claims:** Event categories/scopes, IDs, asynchronous events, argument evaluation behavior, and approximate enabled/disabled costs are stated by the guide.
- **Not established:** Cost under a specified device, Chromium revision, event rate, or workload.
- **Preliminary inference:** Preserve event scope/category and enabled state, then measure overhead in the intended environment.

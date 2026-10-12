# Chromium CDP - Memory Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — Memory domain*, `tot` documentation. https://chromedevtools.github.io/devtools-protocol/tot/Memory/
- **Zotero key:** `H6CJZ69R`.
- **Source:** Zotero snapshot version 1473, saved 29 August 2026; `tot` endpoint is mutable. Pin the Chromium build and protocol revision for implementation work.

## Abstract and scope

The Memory domain documents memory-related observations and controls, including DOM counters, allocation sampling, simulated memory pressure, and preparation for leak detection. It is experimental protocol documentation. It does not report empirical accuracy or overhead measurements.

## Outline Summary

- **Central idea:** CDP exposes several memory-related commands, some of which observe state and some of which actively change it.
- **Problem and objectives:** Define protocol operations and returned data for memory inspection and control. Research questions, participants, datasets, and experimental setup are N/A for this documentation.
- **Methods and observations:** `getDOMCounters` reports document, JavaScript event-listener, and node counts. Sampling controls configure and query allocation sampling. The domain also documents memory pressure operations.
- **Active state changes:** `prepareForLeakDetection` may terminate workers, stop spellcheckers, drop caches, and run garbage collection before leak-related counters are collected. These operations can affect the state being examined; the documentation does not quantify those effects.
- **Results:** N/A. This protocol reference specifies operations and does not provide experimental outcomes.
- **Limitations:** The domain is experimental and mutable. The reference does not establish counter accuracy, representativeness, or collection cost. Preparation and pressure commands are interventions, not passive observations.
- **Author-stated future work:** Not stated.
- **Relationship to T1.2:** Candidate memory observation and control surface. Record exact commands, sampling settings, process or renderer scope, and whether cleanup or pressure operations ran.
- **Important source references:** [`getDOMCounters`](https://chromedevtools.github.io/devtools-protocol/tot/Memory/#method-getDOMCounters), [`prepareForLeakDetection`](https://chromedevtools.github.io/devtools-protocol/tot/Memory/#method-prepareForLeakDetection), and the [Memory domain](https://chromedevtools.github.io/devtools-protocol/tot/Memory/). No page numbers.
- **Concise takeaway:** The protocol offers memory counters and controls, but active preparation can change browser state and the reference gives no cost or validity evaluation.

## T1.2 Evidence Check

- **Protocol claim:** The listed commands and their documented behavior are defined by the Memory domain reference.
- **Not established:** Realized accuracy, coverage, and observer cost for a target Chromium build.
- **Preliminary inference:** Evaluate observation and intervention commands separately and measure whether they alter the workload or reported memory state.

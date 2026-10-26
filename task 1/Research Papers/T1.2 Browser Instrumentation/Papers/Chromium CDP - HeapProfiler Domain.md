# Chromium CDP - HeapProfiler Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — HeapProfiler domain*, protocol documentation endpoint tot. https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/
- **Zotero key:** I9Z9RWE2.
- **Source:** Zotero snapshot saved 29 August 2026 (item version 1473); current tot page checked 12 October 2026. The endpoint is mutable; pin the Chromium build and protocol revision.

## Abstract and scope

The HeapProfiler domain defines heap sampling, snapshots, object tracking, and related events. These modes yield different views of heap activity/state; the reference gives no empirical overhead or error estimates.

## Outline Summary

- **Central idea:** CDP offers allocation sampling, heap-object tracking, and heap snapshots as distinct ways to inspect JavaScript heap behavior.
- **Problem and objectives:** Specify operations and data structures for heap observation. Research questions, datasets, participants, and experimental setup are N/A for protocol documentation.
- **Approach:** startSampling uses Poisson allocation sampling; documented defaults are a 32,768-byte interval and maximum stack depth 128. By default, returned samples focus on objects still alive; options can include objects collected by major or minor GC. Tracking and snapshots are separate procedures.
- **Methods and interpretation:** Record interval, stack depth, GC-retention options, and mode. A sampled profile is not an exhaustive allocation census; distinguish it from tracked object IDs and snapshot data.
- **Limitations:** The protocol does not quantify sampling error, coverage, or collection overhead. Modes expose different data and may have different operational effects.
- **Author-stated future work:** N/A; protocol documentation.
- **Relationship to T1.2:** Candidate memory observation surface. Record mode, sampling parameters, and object-retention rule; evaluate effects for target browser workloads.
- **Important source references:** [startSampling](https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/#method-startSampling), [SamplingHeapProfile](https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/#type-SamplingHeapProfile), [stopSampling](https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/#method-stopSampling), [takeHeapSnapshot](https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/#method-takeHeapSnapshot), and [startTrackingHeapObjects](https://chromedevtools.github.io/devtools-protocol/tot/HeapProfiler/#method-startTrackingHeapObjects). No page numbers.
- **Concise takeaway:** HeapProfiler offers sampled, tracked, and snapshot views; none should be presented as a complete, cost-free memory census based on the protocol page alone.

## T1.2 Evidence Check

- **Protocol claim:** Sampling defaults and collection operations are defined by the protocol documentation.
- **Preliminary inference:** Report mode/parameters and measure workload-specific effects; the API reference gives no overhead or sampling-error result.

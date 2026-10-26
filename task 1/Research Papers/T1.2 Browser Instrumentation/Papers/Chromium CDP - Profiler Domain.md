# Chromium CDP - Profiler Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — Profiler domain*, protocol documentation endpoint tot. https://chromedevtools.github.io/devtools-protocol/tot/Profiler/
- **Zotero key:** GC9EIJZR.
- **Source:** Zotero snapshot saved 29 August 2026 (item version 1473); current tot page checked 12 October 2026. The endpoint is mutable; pin the Chromium build and protocol revision.

## Abstract and scope

The Profiler domain defines CPU profile collection and JavaScript coverage operations. It documents profile data and commands, not empirical sampling accuracy or profiler overhead.

## Outline Summary

- **Central idea:** A CDP client can configure CPU sampling, start/stop profiling, and retrieve a structured profile. Precise coverage is a separate mode.
- **Problem and objectives:** Specify profiler controls and output types. Research questions, datasets, participants, and experimental setup are N/A for protocol documentation.
- **Approach:** setSamplingInterval configures sampling and must be called before recording. start/stop delimit CPU profiling. Profile contains nodes, timestamps, samples, and time deltas; timestamps are in microseconds. Precise coverage has separate start/take/stop operations.
- **Methods and interpretation:** Record sampling interval and mode. Treat CPU sampling and precise coverage as different procedures with different effects.
- **Limitations:** The docs do not quantify overhead, accuracy, or workload effects. Precise coverage prevents optimized code and resets execution counters, so it may alter the program being observed.
- **Author-stated future work:** N/A; protocol documentation.
- **Relationship to T1.2:** Primary candidate CPU sampling surface. Measure mode-specific observer effects and interaction with optimization in the target Chromium build.
- **Important source references:** [setSamplingInterval](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/#method-setSamplingInterval), [start](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/#method-start), [stop](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/#method-stop), [Profile](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/#type-Profile), [startPreciseCoverage](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/#method-startPreciseCoverage), and [takePreciseCoverage](https://chromedevtools.github.io/devtools-protocol/tot/Profiler/#method-takePreciseCoverage). No page numbers.
- **Concise takeaway:** CDP Profiler defines CPU sampling and coverage output, but its data contract does not show that either mode has negligible cost or preserves optimized execution.

## T1.2 Evidence Check

- **Protocol claim:** Methods, profile fields, and precise-coverage behavior are documented protocol behavior.
- **Preliminary inference:** Compare each mode with an unprofiled baseline and report sampling interval/mode.

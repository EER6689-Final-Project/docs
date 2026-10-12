# Lighthouse Throttling Documentation

- **Citation:** GoogleChrome/Lighthouse contributors. *Network Throttling* and CPU throttling sections (docs/throttling.md), mutable main branch, accessed 12 October 2026. https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md
- **Zotero key:** MI895PBZ (LighthouseDocsThrottlingmd).
- **Source:** Lighthouse implementation guidance, not a research paper. This note checks live main content as accessed on the date above; the Zotero URL's tracking parameter is omitted.

## Summary

- **Purpose and content**
  - Describes Lighthouse's default mobile network profile (150 ms latency, 1.6 Mbps down, 750 Kbps up, no packet loss) and four common levels of network throttling: simulated, request/DevTools, proxy, and packet level.
  - Simulated throttling is the Lighthouse default: it simulates a page load from the initial unthrottled load. The guide describes it as fast and deterministic while warning that alternate execution paths create inaccuracy and edge cases.
  - Request-level DevTools throttling is an approximation and does not model packet-level effects directly; packet-level shaping can be more realistic but may introduce more variance. CPU throttling is also described in simulated and DevTools forms. The page documents a default CPU slowdown multiplier of 4× and gives calibration guidance based on host benchmark power.
- **Research questions and evidence type**
  - N/A — technical documentation describing Lighthouse settings and trade-offs; no new empirical comparison is reported here.
- **Dataset, setup, metrics, and methods**
  - N/A for an original study. The page lists default configuration values, CLI controls, and qualitative method trade-offs. Linked accuracy analyses and external tools are separate sources.
- **Limitations and interpretation**
  - Mutable main documentation and implementation constants can change; capture Lighthouse version and explicit configuration.
  - Simulated measurements may diverge when an alternate network/CPU execution path occurs. Network and CPU throttling methods model different mechanisms and are not interchangeable conditions.
  - The default profile is a tool convention, not a universal target population or proof that a run represents a real device/network.
- **Relationship to our profiler**
  - **Preliminary inference:** preserve throttling method (simulated, DevTools, packet shaping), its parameters, and Lighthouse/browser versions. This source does not choose our research setup.
- **Important section anchors**
  - Paraphrase anchors: “The mobile network throttling preset,” “Types of network throttling,” “CPU Throttling,” “Calibrating the CPU slowdown,” and “Types of CPU Throttling.” No page numbers.

## T1.2 Evidence Check

- **Qualified:** Defaults and trade-offs are as documented on Lighthouse main on 12 October 2026; the page itself is not a controlled accuracy or overhead evaluation.
- **Preliminary inference:** Treat throttling method and parameters as experimental setup fields and interpret them in relation to the intended estimand.

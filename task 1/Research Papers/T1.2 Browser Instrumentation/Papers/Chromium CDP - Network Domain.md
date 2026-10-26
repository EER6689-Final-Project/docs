# Chromium CDP - Network Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — Network domain*, protocol documentation endpoint tot. https://chromedevtools.github.io/devtools-protocol/tot/Network/
- **Zotero key:** 92RRK4LT.
- **Source:** Zotero snapshot saved 29 August 2026 (item version 1473); current tot page checked 12 October 2026. The endpoint is mutable; record the Chromium build and protocol revision used.

## Abstract and scope

The Network domain defines protocol commands, events, and types for observing network activity. It is a protocol contract, not an empirical study of request coverage, timing accuracy, or collection overhead.

## Outline Summary

- **Central idea:** A CDP client can enable network event delivery and observe request lifecycle, response, data, completion, and failure events.
- **Problem and objectives:** Specify operations and fields for network requests and resource timing. Research questions, participants, datasets, and experimental setup are N/A for protocol documentation.
- **Approach:** Network.enable starts event delivery and accepts buffer-related configuration. Events include requestWillBeSent, responseReceived, dataReceived, loadingFinished, and loadingFailed.
- **Methods and interpretation:** Request IDs connect lifecycle events. dataLength and encodedDataLength describe different byte quantities. ResourceTiming defines requestTime as a seconds baseline and phase values as millisecond offsets; preserve units and event relationships.
- **Limitations:** The reference does not guarantee complete or uniform timing traces across cache, service-worker, and other paths; it does not quantify accuracy or observer overhead.
- **Author-stated future work:** N/A; protocol documentation.
- **Relationship to T1.2:** Candidate network event/timing acquisition surface. Validate completeness and perturbation in the chosen Chromium build/workload before treating derived values as validated.
- **Important source references:** [Network.enable](https://chromedevtools.github.io/devtools-protocol/tot/Network/#method-enable); [requestWillBeSent](https://chromedevtools.github.io/devtools-protocol/tot/Network/#event-requestWillBeSent), [responseReceived](https://chromedevtools.github.io/devtools-protocol/tot/Network/#event-responseReceived), [dataReceived](https://chromedevtools.github.io/devtools-protocol/tot/Network/#event-dataReceived), [loadingFinished](https://chromedevtools.github.io/devtools-protocol/tot/Network/#event-loadingFinished), [loadingFailed](https://chromedevtools.github.io/devtools-protocol/tot/Network/#event-loadingFailed), and [ResourceTiming](https://chromedevtools.github.io/devtools-protocol/tot/Network/#type-ResourceTiming). No page numbers.
- **Concise takeaway:** CDP Network defines request lifecycle and timing fields; the documentation alone does not establish complete capture or low-cost observation.

## T1.2 Evidence Check

- **Protocol claim:** Event/field names, units, and operations are documented behavior.
- **Preliminary inference:** Validate coverage for cache and service-worker conditions and measure collection effects for the selected browser build.

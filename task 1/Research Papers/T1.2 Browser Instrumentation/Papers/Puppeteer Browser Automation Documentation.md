# Puppeteer Browser Automation Documentation

- **Citation:** Puppeteer project. *Puppeteer Documentation*, version 25.13.0 (Zotero snapshot retrieved 29 August 2026). https://pptr.dev/
- **Zotero key:** `WYGSHWFH`.
- **Source:** Official Puppeteer documentation and API reference. This is software documentation, not a controlled empirical study; cite the selected API pages and pinned package/browser versions when describing an implementation.

## Abstract and scope

Puppeteer documents browser automation through page, browser, and protocol APIs. The relevant surfaces for this review include CDP sessions, page metrics, tracing, screenshots, and CPU/network emulation.

## Outline Summary

- **Central idea**
  - Puppeteer provides automation and browser-control APIs that can set up workloads and collect browser data.
- **Problem and objectives**
  - Document the supported automation interfaces and protocol-dependent behavior. Research questions, dataset, participants, and experimental setup are N/A for API documentation.
- **Approach and scope**
  - A page can create a CDP session with `Page.createCDPSession`; `CDPSession.send` sends protocol commands and its event interface receives protocol events. Relevant Page APIs include metrics, tracing, screenshots, and emulation controls.
  - Chrome uses CDP by default; Firefox uses WebDriver BiDi by default. The documentation notes that `Page.metrics` and tracing are unavailable over BiDi and that only one trace can run per browser at a time.
- **Methods and interpretation**
  - Pin Puppeteer and browser versions; state the protocol and emulation configuration; preserve the command/event sequence and serialize tracing where required by the single-trace constraint.
- **Limitations and interpretation**
  - API availability and behavior depend on the browser/protocol combination. Documentation does not establish automation overhead, measurement accuracy, or the effect of emulation on any particular workload.
- **Author-stated future work**
  - N/A; no research future-work programme is established by the API documentation.
- **Relationship to the T1.2 instrumentation review**
  - Puppeteer is a candidate workload-control and data-collection layer. Its own cost and protocol effects must be measured as part of the experimental setup.
- **Important source references**
  - API pages for `Page.createCDPSession`, CDPSession commands/events, `Page.metrics`, tracing, screenshots, and emulation; no page numbers apply. The documentation is versioned and may move as releases change.
- **Concise takeaway**
  - Puppeteer supplies useful automation controls, but protocol choice, version, emulation, and tracing constraints belong in a reproducible measurement setup.

## T1.2 Evidence Check

- **Documentation claim:** The listed automation surfaces and protocol-dependent availability are documented API behavior, not measured performance results.
- **Preliminary inference:** Include automation configuration and its measured overhead in later Chromium experiments; this does not select an architecture or method.

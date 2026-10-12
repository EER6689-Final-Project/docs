# Grigorik 2013 - HTTP: Primer on Web Performance

- **Citation:** Ilya Grigorik. “Primer on Web Performance.” Chapter 10 in *High Performance Browser Networking*. O’Reilly Media, 2013. Online chapter: https://hpbn.co/primer-on-web-performance/.
- **Zotero key:** `9V33RJH6`.
- **Source type:** Book chapter, available as an author-hosted online text.
- **Provenance/access:** Zotero records the canonical chapter URL under the site title “High Performance Browser Networking,” but omits creator and date. The live chapter identifies itself as Chapter 10 of the O’Reilly book and names Ilya Grigorik as author in the book’s surrounding site. Consulted 12 October 2026; no Zotero snapshot is attached.

## Abstract and scope

Introduces end-to-end web performance, the roles of latency, bandwidth, transport, HTTP, application behavior, and browser constraints. The chapter explicitly discusses synthetic and real-user measurement as complementary methods.

## Outline Summary

- **Source findings:** Synthetic tests use a controlled environment and can provide stable baselines for detecting regressions or isolating components. Their results may fail to represent real users because of differences in navigation scenarios, cache state, intermediaries, hardware, browsers, bandwidth, and latency. The chapter recommends augmenting synthetic tests with RUM and notes that Navigation Timing, Resource Timing, and User Timing expose different timing scopes (section “Synthetic and Real-User Performance Measurement”).
- **Limitations:** This is a 2013 technical book chapter, not a recent validation study. Browser API support, tooling, and web architecture described at publication may have changed. It provides no current performance distributions or accuracy bounds for device/network emulation.
- **Relationship to T1.3:** Foundational distinction between controlled repeatability and real-world diversity; useful for explaining why a synthetic browser visiting a production URL still cannot sample actual user devices or behavior.
- **Important anchors:** Performance pillars, section “Performance Pillars: Computing, Rendering, Networking”; measurement tradeoffs and sources of mismatch, “Synthetic and Real-User Performance Measurement” (online lines 169–200); resource waterfalls, lines 107–110. No PDF page numbering on the web chapter.
- **Concise takeaway:** Synthetic and RUM evidence complement each other because controlled tests isolate causes while field observations capture user diversity.

## T1.3 Evidence Check

- **Source-supported:** Definitions and listed mismatch factors are stated in the chapter.
- **Not established:** Current browser API support or accuracy of present-day emulators.
- **Researcher inference:** Use this chapter for conceptual framing; rely on current platform documentation and empirical validation for implementation claims.

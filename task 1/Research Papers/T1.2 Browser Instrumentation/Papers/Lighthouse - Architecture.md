# Lighthouse Architecture

- **Citation:** GoogleChrome/Lighthouse contributors. *Architecture*. Mutable `main` branch documentation, accessed 12 October 2026. https://github.com/GoogleChrome/lighthouse/blob/main/docs/architecture.md.
- **Zotero key:** `I2QWB27Y` (snapshot version 1463; Zotero access date 29 August 2026).
- **Source version:** The page is on mutable `main`; the document labels its content “Some incomplete notes.” It is not pinned to a commit. Sections cited below were checked on 12 October 2026.

## Abstract and scope

The document sketches Lighthouse's architecture and terminology. A Driver interfaces with Puppeteer and Chrome DevTools Protocol (CDP); Gatherers collect artifacts such as traces and DevTools logs; audits and computed artifacts process those inputs into a Lighthouse Result (LHR); the report UI renders the result. It also notes protocol-event ordering concerns. This is incomplete architecture documentation, not a validation study of timing accuracy or observer effects.

## Outline Summary

- **Central idea:** Separate browser control and artifact gathering from audit computation and presentation, while retaining intermediate artifacts for downstream analysis.
- **Problem and objectives:** Describe the modules and data flow used by Lighthouse; no formal research questions are stated.
- **Approach:** Architecture documentation organized around components, terminology, and protocol behavior.
- **Dataset and setup:** N/A. No empirical dataset or experiment is reported. The described collection uses a Puppeteer/CDP Driver, Gatherers, artifacts including `trace.json` and `devtoolslog.json`, audits, computed artifacts, an LHR, and a client-side report.
- **Metrics and results:** The architecture page does not evaluate performance metrics or report empirical results. It documents that some CDP domains must be enabled to receive events and that listeners should be attached before `Domain.enable()` resolves because enabling may flush pending events.
- **Limitations:** The source itself calls the notes incomplete and is on mutable `main`. It does not establish collection overhead, timestamp accuracy, artifact completeness, or stability of the described architecture.
- **Author-stated future work:** Not stated in the reviewed document.
- **Relationship to the T1.2 instrumentation review:** Offers a useful separation of collection, transformation, audit, and report stages. A research profiler could track artifact provenance and CDP state/order, but the source does not validate that approach or its cost.
- **Important source references:** [Components & Terminology](https://github.com/GoogleChrome/lighthouse/blob/main/docs/architecture.md#components--terminology), especially Driver/Gatherers/Audit/Report; [Protocol](https://github.com/GoogleChrome/lighthouse/blob/main/docs/architecture.md#protocol), especially event binding and domain enable ordering. Checked 12 October 2026. No direct quotation is included.
- **Concise takeaway:** Lighthouse documents a staged browser-data pipeline and a CDP event-ordering concern, while leaving completeness, overhead, and timing validity unmeasured.

## T1.2 Claim Check

- **Source-described architecture:** Gatherers produce artifacts, audits consume them, and computed artifacts can derive additional shared information; report UI consumes the LHR.
- **Preliminary inference:** A research instrument should make these stages and protocol setup observable so collection and interpretation can be evaluated separately. This remains a candidate design principle, not a selected architecture.
- **Phase 0 scope:** The mutable, explicitly incomplete document is an architecture reference. It does not validate the profiler or determine a final research gap.

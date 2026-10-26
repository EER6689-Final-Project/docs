# Speedometer 3.1

## Identity and access

- **S-0015**, R1/R3/R6; official benchmark documentation, release **3.1**. My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), webpage **VGT3AWRS**, no attached original PDF in Luna's metadata read.
- Sol re-opened <https://browserbench.org/Speedometer3.1/>, <https://browserbench.org/Speedometer3.1/about.html> and <https://browserbench.org/Speedometer3.1/instructions.html>, 2026-10-25. Heading text says “About Speedometer 3” and “Speedometer 3 General Instructions”; URL and displayed release are 3.1. Live documents, no immutable revision/hash recorded. This is not an executed benchmark. No generated substitute PDF is provided.
- `ERP-2026-10-25-v1.0`. Original full text of these three short pages re-opened by Sol; no linked workload code, scoring implementation or engine implementation audit. Luna's prior web reading is a separate extraction, not independent human review.

## Claim-to-source extraction

### C-T1.6-054 — Simulated responsiveness has explicit limits

**Claim:** Speedometer 3.1 times simulated interactions in fixed demo workloads and does not measure concurrent asynchronous work; its documentation says it should not be used to compare JavaScript frameworks. It is not a live-origin sample or universal browser-performance ground truth.

**Original anchors:** About page opening: “measures Web application responsiveness by timing simulated user interactions on various workloads.” Journey list covers todo lists, rich-text editing, charts and a news site. Under **Notes about methodology**: “Speedometer does not attempt to measure concurrent asynchronous work (e.g. in Web Workers)” and “Speedometer should not be used as a way to compare the performance of different JavaScript frameworks.” Final bullet says workloads must not depend on server infrastructure and are built as static files. These are benchmark-owner scope statements, not a Web standard or evidence that every implementation conforms.

**Operational context:** Instructions prefer a separate clean profile, focus, latest stable browser, no background programs, browser restart/other-tab closure and possible cooling between runs. These are source recommendations, not an approved project collection protocol. Home-page warning/result-template text in fetched HTML does not establish successful execution, score or durations.

**Construct/unit/comparator:** Demo journey operations in a benchmark harness, not independent sites/users. This pass does not inspect aggregate-score formula, repetition defaults or uncertainty; no score arithmetic or figure/table is used. Comparing framework scores conflicts with the explicit owner warning.

**Support: confirmed** for stated scope/warning; **qualified** for proposed external-validity interpretation. **Methodological confidence: higher** for documentation scope, **limited** for claimed real-user representativeness without additional validation. Dependency group `DG-Speedometer31`: home/About/instructions describe one benchmark and are not three independent studies.

**Conditional inference:** If approved, use a pinned release as a bounded synthetic interaction workload; retain lifecycle/network/memory checks separately, and do not designate it an independent correctness oracle merely because it is an established benchmark.

## Appraisal and QC

- Definition/version **adequate**: release-specific URLs and explicit workload/scope text; immutable commit **unclear** (not captured).
- Normative force **adequate**: owner instructions distinguished from standards and project requirements.
- Representativeness **concern**: fixed demos and JavaScript simulation, explicit worker exclusion.
- Implementation fidelity **unclear**: no code audit or valid benchmark run; uncertainty **not applicable** to documentation-only claims.
- **QC-054**, Sol, 2026-10-25: **checked-no-discrepancy** for all retained claim C-T1.6-054, including methodology warning and instructions context. Two initially guessed `/resources/` document URLs returned 404; correct links were followed from the home page. Separate passage recheck after Luna, **not independent human/scientific review**. No scope, novelty or gate approval.

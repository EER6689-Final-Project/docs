# Zotero Verification Queue

**Status:** Active

**Updated:** 2026-10-12 (T1.3 Zotero source review)

This queue converts the six Deep Research source lists into a verification workflow. “Located” means Zotero returned a record or metadata for the item. It does **not** mean that the item's full text has been read or that every report claim is supported. Record claim-level outcomes as **confirmed**, **qualified**, **contradicted**, or **unsupported** after reading.

## Verification protocol

For each source:

1. confirm title, authors, year, venue, DOI/URL, and source type;
2. read the relevant methods, results, limitations, and definitions;
3. identify the exact claim(s) for which the source is being used;
4. record the population, browser/tool, conditions, repetitions, metrics, and analysis;
5. compare the source claim with the Deep Research report;
6. record the outcome and any qualification; and
7. do not promote a report claim to thesis evidence merely because metadata exists.

## P0 — definitions, tool semantics, and measurement validity

| Source | Zotero record | Verification question | Status |
| --- | --- | --- | --- |
| W3C/WHATWG Paint Timing, LCP, Event Timing, Navigation Timing, Resource Timing, Performance Timeline, Long Tasks | `REP5RHB6`, `6WVYFE8R`, `I8L7FN9V`, `JJWRMF5Z`, `NXHCE5SV` and related records | Do the report's metric semantics, lifecycle boundaries, units, and direct/derived distinctions match the current specifications? | Located; claim reading pending |
| Chrome UX Report methodology and metrics | `3KVANYXJ`, `DP9EINBS` | What population, eligibility, aggregation, navigation types, percentiles, and field/lab distinctions are actually documented? | **Qualified for T1.1:** original live methodology/metrics read. Eligible Chrome users/page-origin filtering, URL normalization, iframe/SPA attribution and full-load-only TTFB differ from a synthetic page run. CrUX methodology contains conflicting sentences about user+origin eligible but page-ineligible experiences in origin aggregates; do not quote this rule without resolution. Other T1.3 claims still pending. |
| Chrome DevTools Protocol | `GC9EIJZR` | Which CDP domains/events/counters and throttling controls are documented, and what are their timestamp and scope semantics? | Located; claim reading pending |
| Chrome DevTools timeline event reference | `BL8XCEDY` | How are trace categories and event names defined, and what does the UI aggregate versus merely display? | **Qualified for T1.1:** original reference lists 2015-era scripting/rendering/painting UI event names and common properties; it is **not** a current trace schema/CDP contract. Modern implementation checks still pending. |
| Lighthouse performance scoring | `WB6JZEUA` | What current score components, distributions, weights, and version caveats apply? | **Qualified for T1.1:** read original scoring page; weighted log-normal score construction confirmed; 10/10/25/30/25 table is labelled *Lighthouse 10*, **not verified as current 2026 weights**. Current release/config check pending. |
| Lighthouse variability documentation | `CWHHFA55` | What sources of run-to-run variation and recommended repetition practices are documented? | Located; claim reading pending |
| Lighthouse throttling documentation | `MI895PBZ` | How do simulated, request-level, proxy, and packet-level throttling differ? | Located; claim reading pending |
| VIM / International Vocabulary of Metrology | Search Zotero by exact title | Are accuracy, precision, repeatability, reproducibility, and bias being used correctly? | Search/read pending |

## P0 — browser measurement and controlled evaluation

| Source | Zotero record | Verification question | Status |
| --- | --- | --- | --- |
| Wang et al., *Demystifying Page Load Performance with WProf* | Not located by exact-title search; search by authors/NSDI 2013 | Does WProf support the report's claims about browser/network decomposition, corpus, and cold/warm/hot loads? | Not located; priority search |
| Netravali et al., *Vesper: Measuring Time-to-Interactivity for Web Pages* | `HS3PKWFL` | What was measured, under which cache/browser/network conditions, and how did distributional effects support the report's claims? | **Qualified** for T1.1: original NSDI '18 paper read; 350 *filtered* sites, Chrome 53/Mahimahi, cold-cache default and 25–200 ms RTT. Its 24–64% mismatch refers to *its own visibility-plus-functionality readiness construct*, not a universal ground truth or modern INP. [[../Research Papers/T1.1 Metric Semantics/Papers/Netravali et al 2018 - Vesper Measuring Time-to-Interactivity|Source note]]; other T1.2/T1.6 claims still require their own checks. |
| Netravali et al., *Mahimahi: Accurate Record-and-Replay for Web Applications* | Search exact title/USENIX ATC 2015 | Does the paper support record/replay as a bridge between live realism and controlled execution? | Search/read pending |
| Wang et al., *How Speedy is SPDY?* | Search exact title/NSDI 2014 | Does the staged synthetic-to-real design support the proposed fixture/live distinction? | Search/read pending |
| Butkiewicz et al., *Understanding Website Complexity* | Search exact title/IMC 2011 | Which measurable content/service features support independent workload categories? | Search/read pending |
| Zeber et al., automated crawls versus human browsing | Search exact title/WWW 2020 | What differences between stateless crawls and stateful human browsing were observed, and what limitations apply? | Search/read pending |

## P0 — statistical measurement and agreement

| Source | Zotero record | Verification question | Status |
| --- | --- | --- | --- |
| Mytkowicz et al., *Producing Wrong Data Without Doing Anything Obviously Wrong!* | `IWCIN2C5`; DOI `10.1145/1508244.1508275` | Does the source support setup randomization and the claimed risk of measurement bias? | Metadata/abstract located; full-text reading pending |
| Mytkowicz et al., *Understanding Measurement Perturbation in Trace-based Data* | `EVB9FDNG`; DOI `10.1109/IPDPS.2007.370515` | What trace perturbation mechanisms and evidence are actually reported? | Metadata/abstract located; full-text reading pending |
| Curtsinger & Berger, *STABILIZER* | `5NNCRU98`; DOI `10.1145/2451116.2451141` | What assumptions and results support randomization/statistical soundness, and what transfers to browsers? | Metadata/abstract located; full-text reading pending |
| Kalibera & Jones, *Rigorous Benchmarking in Reasonable Time* | Not located by current title search | Does it justify hierarchical variance analysis and repetition allocation? | Search/read pending |
| Georges, Buytaert & Eeckhout, *Statistically Rigorous Java Performance Evaluation* | Not located by current title search | Does it justify precision-driven or adaptive repetition? | Search/read pending |
| Chen & Revels, *Robust Benchmarking in Noisy Environments* | Not located by current title search | Does it establish heavy-tailed/non-IID timing concerns relevant here? | Search/read pending |
| Frachtenberg et al., *The Distribution Is the Performance* | Not located by current title search | Does it support distribution-first performance reporting, and with what scope? | Search/read pending |
| Singham & Schruben, *Finite-Sample Performance of Absolute Precision Stopping Rules* | Search exact title | Does naïve CI-width stopping lose coverage, and what calibrated alternatives are supplied? | Search/read pending |
| Howard & Ramdas, sequential quantile estimation | Search exact title | What IID assumptions and coverage guarantees apply to quantile confidence sequences? | Search/read pending |
| Bland & Altman, method-comparison agreement papers | Not located by current query; search by exact titles/year | What agreement and limits-of-agreement claims are justified, especially with replicate measurements? | Search/read pending |
| Carstensen, Simpson & Gurrin; Zou, replicate agreement | Search exact titles | How should repeated browser runs be handled without pseudoreplication? | Search/read pending |

## P1 — external validity, agents, and operational threats

| Source | Zotero record | Verification question | Status |
| --- | --- | --- | --- |
| Kelton et al., *Improving User Perceived Page Load Times Using Gaze* | `WUUGBCG4` | Which conventional metrics failed to capture attention/perceived completion, and what was the study's scope? | **Qualified:** original NSDI '17 paper read; uPLT–OnLoad/SI correlation ≈0.46/0.44 across 45 sampled pages, video-based human completion under specified network/browser conditions. Not a universal failure of synthetic metrics. [[../Research Papers/T1.1 Metric Semantics/Papers/Kelton et al 2017 - Improving User Perceived Page Load Times Using Gaze|Source note]]. |
| Kelton et al., *Modeling User-Centered Page Load Time for Smartphones* | `GJ9PAHK3`; DOI `10.1145/3379503.3403565` | Does mobile scrolling/user behavior justify separating initial viewport load from user-centered load? | **Qualified:** original MobileHCI '20 paper read; early scrolling and multiple viewports under simulated video/scroll conditions support the distinction. “Ground truth” muPLT is operationalized from scroll pauses; do not generalize to all mobile tasks. [[../Research Papers/T1.1 Metric Semantics/Papers/Kelton et al 2020 - Modeling User-Centered Page Load Time for Smartphones|Source note]]. |
| Wehner et al., *A Vital Improvement?* | `2LYVIL8I`; DOI `10.1109/QoMEX55416.2022.9900881` | What design and limitations support the claim that CWV are not a complete QoE model? | **Qualified:** original QoMEX '22 paper read; synthetic preloaded pages, load-rating task and 2022 LCP/FID/CLS set. Not evidence about present-day INP or all field QoE. [[../Research Papers/T1.1 Metric Semantics/Papers/Wehner et al 2022 - A Vital Improvement|Source note]]. |
| Wehner et al., *Do you agree?* | `22HAD6YA`; DOI `10.1007/s41233-023-00058-3` | How do cookie banners, tasks, and controlled QoE manipulation affect the reported conclusion? | **Qualified:** original 2023 article read; controlled banner stimuli can alter LCP candidate and delay content clicks, but mandatory interaction and synthetic pages constrain transfer; the same 2022-era FID definition applies. [[../Research Papers/T1.1 Metric Semantics/Papers/Wehner et al 2023 - Do You Agree|Source note]]. |
| Gundelach, Mühlhauser & Herrmann, *Detecting Bot Detection* | `9TZCJ36B`; DOI `10.48550/arXiv.2606.14525` | Is the headless soft-block finding reproducible and how should its preprint status limit claims? | Metadata/abstract located; full-text reading pending |
| Chrome, field-informed DevTools performance debugging | Search exact title | What is documented about host CPU calibration, real-device comparison, and field-informed lab conditions? | Search/read pending |
| Chrome DevTools Protocol Emulation and Network domains | Search/get exact records | What does each control actually change, and what is not emulated? | Search/read pending |
| RFC 9111 and W3C Service Workers | Search exact standards | Are HTTP cache and Cache Storage/service-worker state distinct as stated? | Search/read pending |

## T1.1 scholarly-paper batch — remaining claim-level checks

| Paper | T1.1/report claim tested | Outcome and boundary |
| --- | --- | --- |
| Gao et al. (2017), `6EFLN7PR` | Above-the-fold visual completion and people's speed judgement differ. | **Qualified:** 160 matched retail-video pairs; onLoad 55% and original SI 53% agreement with majority vote; the higher-performing TTC-truncated variant uses observed human decision time. [[../Research Papers/T1.1 Metric Semantics/Papers/Gao et al 2017 - Perceived Performance of Top Retail Webpages|Source note]]. |
| Hoßfeld et al. (2018), `9A8CMSAY` | Speed Index directly predicts individuals' QoE. | **Unsupported as stated:** authors report no significant correlation at the individual-rating level; stronger model fit uses *ByteIndex-ATF* with aggregated MOS, not SI predicting each person. Their data section/conclusion disagree on page count (12 vs 25). [[../Research Papers/T1.1 Metric Semantics/Papers/Hossfeld et al 2018 - Speed Index and Web QoE|Source note]]. |
| van Riet et al. (2023), `9WT3HAHJ` | Task-/product-specific measures can track perceived load better than generic ones. | **Qualified:** 19 employees, six videos representing three dashboard compositions; product-specific Lowest Time to Widget correlated in this case only. Historical Chrome 80 and retired metrics cannot be promoted to present-day defaults. [[../Research Papers/T1.1 Metric Semantics/Papers/van Riet et al 2023 - Optimize Along the Way|Source note]]. |

These outcomes apply only to the **listed T1.1 claims**. The twelve non-paper records from the same collection are checked below; individual W3C specifications and further P0 tool records remain pending. This does not complete verification for T1.2–T1.6.

## T1.1 Phase B — twelve non-paper records in `VEYKC53A`

| Record(s) | Original-page claim check | Outcome / boundary |
| --- | --- | --- |
| `R2U9EAFA`, `GYN22PP7` — WICG Layout Instability API + Chrome CLS guide | Are `layout-shift` entries, lifetime sum and current CLS equivalent? | **Confirmed distinct:** WICG's per-frame API and non-normative lifetime sum are not Google's maximum-session-window CWV aggregation (<1 s gap, ≤5 s). Cross-frame access and page lifetime matter. |
| `NJYH4V45` — WICG memory proposal | Does “page memory” identify one exact cross-browser number? | **Contradicted:** proposed estimate may be incomplete and implementation-specific, requires cross-origin isolation; JS heap is a different scope. |
| `XFCVZVBE` — W3C publication catalogue | Does this catalogue itself define LCP/FCP/Resource Timing? | **Unsupported:** it lists status and links to actual dated specifications; each original specification remains to read for exact semantics. |
| `UN6NKBQX`, `VWHJLGV3` — Web Vitals guide + INP change announcement | Current CWV set and date FID was replaced? | **Confirmed:** LCP/INP/CLS; INP became CWV 12 March 2024. Google's metric lifecycle and W3C specification maturity are separate. |
| `B8XNKSHY` — INP guide | Is TBT equivalent to INP without interaction? | **Contradicted:** INP needs qualifying clicks/taps/keys; TBT may aid lab diagnosis, not substitute for observed INP. |
| `3KVANYXJ`, `DP9EINBS` — CrUX methodology/metrics | Can lab output or independently aggregated p75 subparts be read as a per-visit CrUX decomposition? | **Contradicted:** eligibility/denominators differ; image-LCP p75 subparts need not sum to overall p75. TTFB collected on full loads only; wording on one origin-eligibility condition needs reconciliation. |
| `WB6JZEUA`, `A8GDSSI7` — Lighthouse score/SI guides | Is score a raw timing and is SI a functional-readiness event? | **Contradicted:** score is weighted transformed metrics; SI video/Speedline visual progression. **Qualified:** score table explicitly v10; SI page from 2019; neither establishes current source-code formula or subjective validity. |
| `BL8XCEDY` — DevTools timeline event reference | Are named UI categories portable browser-standard JS/layout/paint totals? | **Unsupported:** page lists Chrome/DevTools event categories and properties, dated 2015; it is not a current CDP trace-event specification. |

All twelve have [matrix rows](<Literature Review and Research Gap Matrix.md>) with original URLs/sections. Outcomes are for the stated T1.1 claims only. This batch does **not** finish the P0 W3C individual-specification, CDP, Lighthouse-variability/throttling or broader T1.2–T1.6 queue.

## T1.3 — synthetic agents and external validity

| Source | Zotero record | Verification question | Status |
| --- | --- | --- | --- |
| Sengupta et al., “Through the Lens of Google CrUX” | `9IDW7B5Y`; attached arXiv v2 and IFIP Networking 2024 proceedings record | Which author list should be used in the formal bibliography? | **Claim review complete; bibliographic follow-up open:** the attached preprint lists five authors including Dinh Nguyen, while the conference contents lists four. The matrix cites the proceedings and retains the discrepancy in its source note until the final proceedings PDF/DOI metadata is reconciled. |
| Heričko, Šumak & Brdnik, “Towards Representative Web Performance Measurements with Google Lighthouse” | `DJI5ULJD`; attached PDF `PCW9E8SN` | Does the Zotero record metadata match the paper? | **Resolved from attached PDF and proceedings record:** cite Heričko, Šumak & Brdnik (2021), *StuCoSReC 2021*, pp. 39–42, DOI `10.18690/978-961-286-516-0.9`; Zotero's ResearchGate-style item title/authorship fields were incomplete. |
| CDP Network and Lighthouse throttling documentation | `YLRND2GP`, `JT3PXZLG` | Are these independent sources from the T1.2 records? | **Resolved as duplicates:** same documentation as T1.2 `92RRK4LT` and `MI895PBZ`, respectively; T1.3 notes retained for collection traceability and matrix rows are not duplicated. |
| Other 21 T1.3 evidence sources | Collection `B2NRLIE9`; source notes in T1.3 Papers | Do source-specific methods, scope, and limitations support the matrix claims? | **Reviewed for the claims recorded in the T1.3 matrix.** Outcomes are bounded to each source note; mutable documentation and aggregate observational data do not establish synthetic-agent fidelity. |

## Known Zotero search limitations

- Exact-title item searches sometimes return semantically related items instead of the intended paper; a returned result is not proof of identity.
- Semantic search is useful for discovery but must not replace exact bibliographic verification.
- Some expected sources may exist under a different title, duplicate record, author spelling, or collection.
- No source should be marked claim-verified from an abstract alone when the report makes methodological or quantitative claims.

## Verification outcome vocabulary

- **Confirmed:** the original source directly supports the stated claim under matching conditions.
- **Qualified:** the source supports a narrower claim, with population, version, method, or limitation recorded.
- **Contradicted:** the original source conflicts with the report claim.
- **Unsupported:** the source is relevant but does not provide evidence for the stated claim.
- **Not located:** source identity/metadata still requires resolution; do not treat absence from a search as evidence that the source does not exist.

# Initial Evidence Map

**Status:** Phase 0 working map; not a verified bibliography

**Updated:** 2026-10-08 (T1.1 Phases A–C)

This map records the current relationship between the six Tier-1 reports, the claims they contribute, and the status of original-source verification. It deliberately distinguishes **report synthesis**, **project requirement**, **Zotero metadata**, and **claim-level primary evidence**.

## Evidence classes

| Class | Meaning | Permitted use |
| --- | --- | --- |
| **Requirement** | Statement from the project proposal or `My tasks.pdf`. | Defines scope or acceptance needs; does not establish literature novelty or methodological truth. |
| **Deep Research synthesis** | Claim in a local T1 report. | Discovery, hypothesis generation, and queue construction; not final primary evidence. |
| **Zotero metadata** | Bibliographic record, abstract, DOI, or URL found in Zotero. | Confirms source identity provisionally; does not verify detailed claims. |
| **Primary/authoritative evidence** | Original paper, specification, or official technical document read for the exact claim. | Thesis evidence, subject to scope and limitations recorded. |
| **Researcher inference** | Design implication derived from evidence. | Must remain labelled as inference and cannot be presented as source fact. |

## Current claim map

| Theme | Current synthesis claim | Local source | Evidence currently available | Original-source status | Current disposition |
| --- | --- | --- | --- | --- | --- |
| Metric semantics | Current Core Web Vitals taxonomy must be distinguished from supporting/diagnostic metrics; same-name values can have different semantics. | T1.1 | `UN6NKBQX`, `VWHJLGV3`, `B8XNKSHY`, `GYN22PP7`, `R2U9EAFA` original pages read. | **Confirmed** current LCP/INP/CLS and FID retirement as Google metric taxonomy; **qualified** CLS API primitive versus Google session-window score. Individual W3C LCP/Event Timing/Paint specs remain pending. | Promote only the named taxonomy/CLS-aggregation claims to original documentation evidence, not every metric's full normative semantics. |
| Metric semantics | Client-observed TTFB, Resource Timing byte fields, memory values, DOM counts, and trace categories have narrower scopes than informal labels imply. | T1.1 | Deep Research synthesis; relevant API/CDP records located. | Claim reading pending. | Working principle; verify definitions and version. |
| Instrumentation | Web APIs, PerformanceObserver, CDP, tracing, Puppeteer, and Lighthouse observe different planes; Puppeteer is primarily orchestration. | T1.2 | Deep Research synthesis; CDP/Lighthouse records located. | Claim reading pending. | Candidate measurement-contract requirement. |
| Observer effect | Instrumentation overhead is configuration- and workload-dependent; no universal constant is justified. | T1.2 | Deep Research synthesis; Mytkowicz records `EVB9FDNG` and `IWCIN2C5` located; STABILIZER `5NNCRU98` located. | Full-text claim reading pending. | Candidate experimental factor; correction not assumed. |
| Synthetic validity | RUM-informed scripted agents remain synthetic; production targets provide system realism but not automatic population representativeness. | T1.3 | CrUX methodology/metrics `3KVANYXJ`, `DP9EINBS` read for T1.1; Zeber source still to locate. | **Qualified** support for field population/denominator distinctions; claims about agent behavior, field representativeness and T1.3 empirical evidence remain pending. | Avoid treating matched names or an RUM-derived synthetic profile as field population samples. |
| Synthetic validity | CPU throttling, network shaping, geography, and browser state have different fidelity limits and must be specified separately. | T1.3 | Deep Research synthesis; related Chrome/CDP records partly located. | Claim reading pending. | Preserve as separate agent dimensions. |
| Statistical measurement | The conditional run-performance distribution is the provisional statistical object; the headline statistic remains estimand-dependent. | T1.4 | Deep Research synthesis; key methodology papers not yet reliably located. | Verification pending. | Provisional statistical stance adopted. |
| Statistical measurement | p95 is operationally meaningful in some studies but unstable/information-poor at small repetition counts; repetition should be precision-driven. | T1.4 | Deep Research synthesis; exact source reading pending. | Verification pending. | Do not select p95 or fixed run count. |
| Statistical measurement | Cold, warm, and sequential states may be distinct target conditions; failures and outliers require provenance-based classification. | T1.4/T1.6 | Deep Research synthesis; WProf/Vesper/standards still pending full reading. | Verification pending. | State vector and failure classes remain open design gates. |
| Validation | DevTools and Lighthouse are reference implementations, not automatic ground truth; correlation alone cannot establish agreement. | T1.5 | Deep Research synthesis; Lighthouse/DevTools records located; agreement sources pending. | Claim reading pending. | Use layered validation vocabulary. |
| Validation | Same-artifact conformance, matched independent-run agreement, repeatability, robustness, and controlled-defect sensitivity answer different questions. | T1.5 | Deep Research synthesis. | Original-method verification pending. | Preserve as separate candidate evidence layers. |
| Experimental design | Controlled fixtures support causal sensitivity; live URLs support production complexity; their inferential roles must remain separate. | T1.6 | Deep Research synthesis; WProf/SPDY/Mahimahi records still to resolve. | Verification pending. | Hybrid design retained as candidate only. |
| Experimental design | Site and agent are generally crossed; repeated runs are nested in condition cells; website count and run count estimate different variance components. | T1.6 | Deep Research synthesis; Kalibera/Jones source not yet located. | Verification pending. | Do not set sample size by convention. |
| Scoring | A project-required score is not automatically a valid universal performance quantity; underlying component data must be preserved. | Stage 1/T1.1/T1.5 | Requirement plus original Lighthouse scoring `WB6JZEUA` read. | **Qualified:** official page confirms a weighted log-normal metric transformation with versioned v10 weights; cannot infer a universally valid UX scalar or current v2026 weights. | Requirement with evidence gate; preserve versioned raw components. |

## Source-level status summary

### T1.1 official documents and repository (original pages read 2026-10-08)

| Original records | Verified proposition and limitation |
| --- | --- |
| WICG `R2U9EAFA` + Google `GYN22PP7` | LayoutShift entries are per-frame primitives; WICG lifetime sums are non-normative; current CWV CLS uses the maximum unexpected-shift session window and can include iframe experience absent from a top-page JS observer. |
| WICG memory proposal `NJYH4V45` | `measureUserAgentSpecificMemory` is an estimate, scope- and isolation-dependent; non-goals explicitly exclude precise, complete and cross-browser comparable totals. |
| W3C index `XFCVZVBE` | Lists dated publication maturities, not normative algorithms. Direct Paint/LCP/Event/Navigation/Resource/etc. spec reading remains pending. |
| Google `UN6NKBQX`, `VWHJLGV3`, `B8XNKSHY` | Stable CWV are LCP/INP/CLS; FID retired 12 Mar 2024; navigation-only Lighthouse cannot observe INP; interaction workload and page lifetime govern its scope. |
| CrUX `3KVANYXJ`, `DP9EINBS` | Eligible Chrome field population and per-metric navigation denominators are not equivalent to synthetic runs; independently aggregated p75 subparts are not a per-visit additive decomposition. One methodology eligibility sentence is internally inconsistent and flagged. |
| Lighthouse `WB6JZEUA`, `A8GDSSI7` | Score is a weighted mapping of metric scores; SI is video/Speedline visual progression; v10 weighting table and older SI guide do not prove current release formula. |
| DevTools `BL8XCEDY` | 2015 UI event reference distinguishes categories and self/CPU/wall properties; not a present-day interoperable trace schema. |

Each of the twelve parent Zotero keys has an [individual matrix row](<Literature Review and Research Gap Matrix.md>) with direct section links. Four cross-source candidate areas are *researcher inferences* in that matrix, **not confirmed novel gaps**. Individual specifications, current tool source code and T1.2–T1.6 sources still require their own claim checks.

### Phase C comparative assessment

[[T1.1 Candidate Gap Assessment]] compares four *not selected* areas against all 20 T1.1 records, the individual task allocation, and a limited adjacent-literature discovery scan. Potential overlap includes repeated Lighthouse measurements `DJI5ULJD`, reproducibility study `RB93JMBB`, WebREC `MAYMCK7L`, and Chrome soft-navigation documentation `486KI7NN`. Those four are **leads**, not fully verified entries in the T1.1 matrix; Phase C does not promote their method/result claims to final thesis evidence. It records an unresolved requirements conflict: `My tasks.pdf` groups historical or diagnostic metrics under “Core Web Vitals” and calls client-observed response latency “server response time.”

### T1.1 original scholarly papers read for the specific claims below (2026-10-08)

| Original source | Original-source finding relevant to T1.1 | Report claim status / qualifier | Researcher inference (not author finding) |
| --- | --- | --- | --- |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Kelton et al 2017 - Improving User Perceived Page Load Times Using Gaze|Kelton et al. 2017]] `WUUGBCG4` | Median human uPLT and OnLoad/SI correspond weakly in 45 pages under recorded, shaped loads (NSDI '17, pp. 547–549). | **Qualified:** supports limited attention/perceived-completion caution; not a general benchmark for every modern metric. | Synthetic profiler should label output as browser-observed, not perceived completion. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Gao et al 2017 - Perceived Performance of Top Retail Webpages|Gao et al. 2017]] `6EFLN7PR` | Retail-video majority A/B choices matched onLoad 55%, original SI 53%; TTC-truncated visual metric uses human decision time (Internet QoE '17, pp. 16–18). | **Qualified:** different metric endpoints change agreement with this judgement task. | No unattended metric should inherit the TTC-assisted accuracy without separate validation. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Hossfeld et al 2018 - Speed Index and Web QoE|Hoßfeld et al. 2018]] `9A8CMSAY` | No significant individual-rating correlation; binned MOS fits used ByteIndex-ATF; dataset page count contradicts itself (QoMEX '18, pp. 4–6). | **Unsupported** if asserted as individual-level SI→QoE validation. | Keep aggregation and metric-substitution provenance in outputs. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Netravali et al 2018 - Vesper Measuring Time-to-Interactivity|Netravali et al. 2018]] `HS3PKWFL` | Vesper operationalizes visibility *plus* functional state; prior metrics can differ substantially under controlled Chrome 53/record-and-replay (NSDI '18, pp. 217–228). | **Qualified:** 24–64% disagreement is relative to Vesper's definition, not universal ground truth or INP. | An interactivity claim requires an explicit task/construct and instrumentation checks. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Kelton et al 2020 - Modeling User-Centered Page Load Time for Smartphones|Kelton et al. 2020]] `GJ9PAHK3` | Early mobile scrolling/multiple viewports affect a scroll-pause-defined muPLT under replay (MobileHCI '20, pp. 5–10). | **Qualified:** initial viewport need not represent this mobile browsing journey; pause-derived muPLT is a proxy. | Distinguish navigation-only mobile load from scripted multi-viewport tasks. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Wehner et al 2022 - A Vital Improvement|Wehner et al. 2022]] `2LYVIL8I` | Controlled loading ratings and custom pages show less CWV response within fixed load duration (QoMEX '22, paper pp. 3–6). | **Qualified:** 2022 LCP/FID/CLS and load-rating task, not current INP or field outcomes. | Keep metric version and validation task together. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/Wehner et al 2023 - Do You Agree|Wehner et al. 2023]] `22HAD6YA` | Banner context affects measured candidates, clicks and ratings in artificial fixtures (Q&UE 2023, PDF pp. 9–16). | **Qualified:** not a universal repudiation of CWV; partly extends same group's 2022 work, not independent replication. | A metric can measure a real overlay while missing task-relevant content. |
| [[../Research Papers/T1.1 Metric Semantics/Papers/van Riet et al 2023 - Optimize Along the Way|van Riet et al. 2023]] `9WT3HAHJ` | One dashboard's product-specific widget milestone tracks the perceived completion response of 19 insiders over six videos (JSS 2023, PDF pp. 7–8, 18–21). | **Qualified:** useful single-product demonstration, not universal metric preference. | Define intended decision purpose and retain individual diagnostics rather than presuppose a scalar. |

See [[Literature Review and Research Gap Matrix]] for methods, page-specific quotations, author limitations and candidate gaps. The **T1.1 official specifications/documentation batch is still unread**; no normative metric or Lighthouse claim above has been promoted on the strength of these papers.

### Located in Zotero with usable metadata

- `IWCIN2C5` — Mytkowicz et al., *Producing wrong data without doing anything obviously wrong!*, DOI `10.1145/1508244.1508275`.
- `EVB9FDNG` — Mytkowicz et al., *Understanding Measurement Perturbation in Trace-based Data*, DOI `10.1109/IPDPS.2007.370515`.
- `5NNCRU98` — Curtsinger & Berger, *STABILIZER*, DOI `10.1145/2451116.2451141`.
- `HS3PKWFL` — Netravali et al., *Vesper: Measuring Time-to-Interactivity for Web Pages*.
- `GJ9PAHK3` — Kelton et al., *Modeling User-Centered Page Load Time for Smartphones*, DOI `10.1145/3379503.3403565`.
- `WUUGBCG4` — Kelton et al., *Improving User Perceived Page Load Times Using Gaze*.
- `2LYVIL8I` — Wehner et al., *A Vital Improvement?*, DOI `10.1109/QoMEX55416.2022.9900881`.
- `22HAD6YA` — Wehner et al., *Do you agree?*, DOI `10.1007/s41233-023-00058-3`.
- `9TZCJ36B` — Gundelach et al., *Detecting Bot Detection*, DOI `10.48550/arXiv.2606.14525`; preprint status applies.
- `3KVANYXJ`, `DP9EINBS` — Chrome UX Report methodology/metrics.
- `GC9EIJZR`, `BL8XCEDY` — Chrome DevTools Protocol and DevTools timeline documentation.
- `WB6JZEUA`, `CWHHFA55`, `MI895PBZ` — Lighthouse scoring, variability, and throttling documentation.

### Not yet reliably resolved by current exact-title searches

- WProf, Kalibera & Jones, Georges et al., Chen & Revels, Frachtenberg et al., Bland & Altman, Mahimahi, SPDY, Butkiewicz et al., Zeber et al., and several standards/methodology sources.

This is a search-status statement, not evidence that the sources are absent from Zotero.

## Promotion rule

A row may be promoted from “Deep Research synthesis” to “Primary/authoritative evidence” only after the original source is read and the claim, conditions, limitations, and bibliographic identity are recorded in the verification queue.

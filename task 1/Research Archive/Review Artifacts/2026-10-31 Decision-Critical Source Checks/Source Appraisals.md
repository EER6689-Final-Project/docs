# Decision-Critical Source Appraisals

**Review:** `SC-2026-10-31`, 2026-10-31, Asia/Colombo. **Extractor/checker:** Codex assistant, separate-pass self-audit. **Scientific reviewer:** unassigned. All judgments below concern the stated claim, not the quality of an entire paper. Unless specified otherwise, numerical effects and implementation reproduction are outside the read/adoption scope. Local PDF hashes and inspected sections are in the [receipt](<source-access-receipt.json>).

## SC-C01 — LMAT: identity resolved; mechanism qualified

**Identity:** Kasra Darvishi, Morteza Noferesti, Yuvraj Sehgal and Naser Ezzati-Jivan. *LMAT: An adaptive tracing approach based on efficient system behavior analysis using language models*. Journal of Systems and Software 238 (2026), 112890. [DOI](https://doi.org/10.1016/j.jss.2026.112890). The [author artifact](https://github.com/kasra-darvishi/adaptive_tracer#citation) separately cites the ICSE-NIER 2024 predecessor, *Toward Adaptive Tracing: Efficient System Behavior Analysis using Language Models*, DOI 10.1145/3639476.3639778, without Sehgal. They are related publications, not interchangeable citations or independent corroboration of the journal experiment.

**Passages/access:** publisher-indexed §§3/3.1, 5.4, 6 (intermittent/rare errors) and 7; [author publication record](https://threadslab.org/research-publications/papers/lmat-adaptive-tracing-language-models/), Method, Limitations and citation. Direct publisher access returned 403. Minimal kernel-event monitoring, deviation-driven richer recording and error-vector fault classification are supported for the Apache/Sock Shop host setting. Indexed controller text describes linger, whereas the prototype discussion says it has neither pre-trigger buffering nor post-trigger linger. Exact tested controller behavior is unresolved.

**Appraisal:** mechanism **adequate** for broad overlap; implementation/version consistency **concern**; browser transfer **unclear**. **Support: qualified; confidence: limited.** Do not claim every rare event requires repetition, or adopt a measured loss/accuracy/overhead value. Dependency `DEP-SC-LMAT` includes the predecessor, article, author summary and repository. **QC: unresolved** for controller details; broad host-level overlap rechecked without discrepancy. Hold `SC-B01`.

## SC-C02 — Hindsight: original-event retention confirmed

**Identity:** Lei Zhang, Zhiqiang Xie, Vaastav Anand, Ymir Vigfusson and Jonathan Mace. *The Benefit of Hindsight: Tracing Edge-Cases in Distributed Systems*. NSDI 2023, 321–339. [Venue citation](https://www.usenix.org/conference/nsdi23/presentation/zhang-lei); [inspected PDF](<Sources/Hindsight - NSDI 2023.pdf>).

**Passages:** §§3–4.3, printed 324–326 / PDF 5–7: record every request locally, retrieve after a symptom trigger, evict untriggered data, and limit recovery by the event horizon. §6, printed 328 / PDF 9 identifies distributed-service workloads and head/tail sampling comparators. This retains evidence of the original execution; it does not reexecute the request.

**Appraisal:** capture/retention distinction **adequate**; late-trigger and overload loss **concern**; browser lifecycle transfer **unclear**. **Support: confirmed; confidence: higher** for architecture, limited for browser effectiveness. Count generation, memory management and export, not only saved traces. Dependency `DEP-SC-HINDSIGHT`: same framework/workloads across comparisons. **QC: checked-no-discrepancy**, including visual inspection of PDF 6. No browser performance effect is inferred.

## SC-C03 — WMF: direct access discrepancy resolved

**Identity:** Giulio Grassi, Renata Teixeira, Chadi Barakat and Mark Crovella, in the PDF's author order. *Leveraging Website Popularity Differences to Identify Performance Anomalies*. IEEE INFOCOM 2021. [DOI](https://doi.org/10.1109/INFOCOM42981.2021.9488832); [author PDF](https://www.cs.bu.edu/fac/crovella/paper-archive/infocom21-website-anomalies.pdf); [preserved copy](<Sources/WMF - INFOCOM 2021 author paper.pdf>). An author publication list uses a different author order; use the original paper.

**Passages:** §§III–IV, PDF 3–5: passive Navigation Timing histories, hourly website/metric summaries and low-rank reconstruction. §V, PDF 5–6: controlled network-delay injections and synthetic matrix anomalies; detection precision/recall/F1 concern anomalous bins. §V.C acknowledges incomplete truth and separately reports manual-inspection treatment. §VII.B, PDF 8–9 contains tentative explanations of live events, not independently verified visit causes.

**Appraisal:** history/detection overlap **adequate**; natural-event truth and selection **concern**; diagnostic-cause endpoint equivalence **not applicable**. **Support: confirmed; confidence: higher** for the endpoint distinction, limited for reuse of the method. The earlier root access failure is superseded by this direct download/read and PDF 6 visual check. Dependency `DEP-SC-WMF`: controlled-site calibration, synthetic injections and observational analysis reuse the study pipeline. **QC: checked-no-discrepancy** for retained claims. Do not transfer its bin size, thresholds or apparent accuracy.

## SC-C04 — Shahedi: preprint/journal association resolved; editions kept separate

**Identity:** Kaveh Shahedi, Heng Li, Maxime Lamothe and Foutse Khomh. *Tracing Optimization for Performance Modeling and Regression Detection*. Inspected [arXiv:2411.17548v1](https://arxiv.org/abs/2411.17548v1), submitted 26 November 2024, 23-page manuscript; [local PDF](<Sources/Shahedi - Tracing Optimization arXiv v1.pdf>). The [coauthor's publication record](https://www.hengli.org/publications/) explicitly links this title/authorship to TOSEM DOI [10.1145/3749839](https://doi.org/10.1145/3749839), labelled accepted in 2025. Publisher landing/PDF access returned 403. Final publication pagination, text changes and experimental equivalence are not verified here; acceptance year is not silently used as final issue year.

**Passages:** preprint §3.1, PDF 6: selected native C/C++ benchmarks and function tracing. §§3.4.2–3.4.3, PDF 13 and §4.4, PDF 18: injected single-function delays, fresh program versions/inputs and model-based regression detection. §5, PDF 19–20 limits input/workload generalization.

**Appraisal:** selective tracing precedent **adequate**; version correspondence **unclear**; transfer to browser-episode attribution **concern**. **Support: qualified; confidence: limited.** Comparing versions is not a demonstrated recovery of an earlier transient browser cause. No test threshold is adopted. Dependency `DEP-SC-SHAHEDI` groups editions and replication data. **QC: checked-no-discrepancy** for preprint claims; final edition remains `SC-B02`.

## SC-C05 — Mertz/Nunes: DOI linkage and adaptive-sampling scope confirmed

**Identity:** Jhonny Mertz and Ingrid Nunes. *Software runtime monitoring with adaptive sampling rate to collect representative samples of execution traces*. Journal of Systems and Software 202 (2023), 111708. [DOI](https://doi.org/10.1016/j.jss.2023.111708). The [arXiv record](https://arxiv.org/abs/2305.01039v1) explicitly supplies the related journal DOI. Inspected [14-page v1 manuscript](<Sources/Mertz and Nunes - Adaptive Sampling arXiv v1.pdf>), 1 May 2023; journal text equivalence is not asserted.

**Passages:** §§3–3.4, especially PDF 7, adapt request sampling and evaluate sample release; §4.1, PDF 8 evaluates selected Java/DaCapo applications against uniform, inverse-throughput, full and no monitoring. Its representativeness endpoint uses memory-usage error. §§4.4–4.5, PDF 12 discuss workload/GC limitations and weakening confidence with cycle time.

**Appraisal:** adaptive sampling precedent **adequate**; surrogate-to-diagnosis transfer **concern**; statistical guarantee for this project **unclear**. **Support: confirmed; confidence: higher** for the narrow scope distinction, limited for method adoption. Do not treat a nonsignificant mean comparison as demonstrated equivalence, or copy its release/stopping procedure. Dependency `DEP-SC-MERTZ` includes manuscript/journal and shared benchmark executions. **QC: checked-no-discrepancy** for retained scope claims.

## SC-C06 — Paradyn: manuscript-to-work association confirmed, edition equivalence unverified

**Identity:** Barton P. Miller and seven coauthors, *The Paradyn Parallel Performance Measurement Tools*, [23-page project manuscript](<Sources/Paradyn - project manuscript.pdf>). The [lead author's bibliography](https://pages.cs.wisc.edu/~bart/includes/publications.html), 1995 entry, links this manuscript path to Computer 28(11), 37–46. Its title wording differs from the journal citation *The Paradyn Parallel Performance Tools*, DOI [10.1109/2.471178](https://doi.org/10.1109/2.471178); DOI retrieval failed. This establishes an author-supplied association, not identical edited text or pagination.

**Passages:** manuscript abstract and §1.2, physical PDF/printed 4–5 explicitly discuss limited-cost dynamic instrumentation, short executions ending before diagnosis, and saving search state for a rerun. Cite that manuscript for those passages.

**Appraisal:** adaptive/rerun precedent **adequate**; journal passage equivalence **unclear**; browser transfer **concern**. **Support: qualified; confidence: higher** for manuscript wording. Dependency `DEP-SC-PARADYN` includes the existing `TIIDVPV8` alias and author/journal records. **QC: checked-no-discrepancy** for the manuscript claims. Journal-only claims stay out of the report until `SC-B03` is resolved.

## SC-C07 — Vesper: cross-load caveat confirmed with contrary context

**Identity:** Ravi Netravali, Vikram Nathan, James Mickens and Hari Balakrishnan. *Vesper: Measuring Time-to-Interactivity for Web Pages*. NSDI 2018, 217–231. Existing canonical alias `HS3PKWFL`; T1.4 reuse is not another study. [Venue](https://www.usenix.org/conference/nsdi18/presentation/netravali-vesper).

**Passages:** existing local PDF 8–9 / printed 223–224, §4.3: heavy discovery/light measurement, possible different state across loads and incomplete event-path coverage. The same discussion says their tested corpus did **not** exhibit nondeterminism producing different functional state. §5.1 describes filtered, replayed pages under a historical browser setup.

**Appraisal:** conditional caveat **adequate**; generalizing rerun failure frequency **concern**. **Support: confirmed; confidence: higher** for the conditional claim. This supports testing equivalence, not assuming reruns usually fail or equating Ready Index with INP. Dependency `DEP-SC-VESPER` includes all topic aliases and replayed corpus. **QC: checked-no-discrepancy** on the two original pages. No quantitative metric or overhead result is newly adopted.

## SC-C08 — WebREC: final proceedings passages checked

**Identity:** Florian Hantke, Peter Snyder, Hamed Haddadi and Ben Stock. *Web Execution Bundles: Reproducible, Accurate, and Archivable Web Measurements*. USENIX Security 2025, 8235–8253. [Final venue](https://www.usenix.org/conference/usenixsecurity25/presentation/hantke), [final PDF](https://www.usenix.org/system/files/usenixsecurity25-hantke.pdf). Existing `ZZSL9IPU` attachment is arXiv:2501.15911v4; final PDF has a cover and 20 physical pages, versus 19 preprint pages.

**Passages:** final §2.3.2, printed 8239 / PDF 6; §§3.2–3.3, printed 8240–8241 / PDF 7–8; §6.1, printed 8247 / PDF 14: response replay and analysis of recorded runtime behavior are different. Final §5, PDF 14 retains Chromium/outside-page-context limits. These specific final passages corroborate the previously inspected preprint distinction; whole-version equivalence is not claimed.

**Appraisal:** archive/reexecution distinction **adequate**; coverage of the project's performance endpoints **unclear**. **Support: confirmed; confidence: higher** for architecture, limited for browser diagnostic effectiveness. Dependency `DEP-WEBREC-PAGEGRAPH` is retained. **QC: checked-no-discrepancy** for those targeted final/preprint claims. No universal completeness or cost claim follows.

## SC-C09 — Existing original-visit attribution: versioned documentation check

**Source:** GoogleChrome [`web-vitals` v5.1.0 README](https://github.com/GoogleChrome/web-vitals/blob/v5.1.0/README.md#attribution), Attribution / `INPAttribution`, `CLSAttribution`, `LCPAttribution`, Limitations. This is a deliberately named reference release, not a claim that v5.1.0 is latest or the selected study build.

Supported diagnostic fields include the interacted element, latency components and, when supported, intersecting long-animation-frame entries and a longest-script summary. CLS identifies shifted elements; an affected element is not necessarily its causal culprit. LCP splits loading/rendering components. **Researcher implication:** existing evidence may already distinguish easy fixtures; richer capture must demonstrate added value. Empty optional fields and missing eligible interactions require explicit outcomes.

**Appraisal:** documented schema **adequate**; implementation/fixture conformance **unclear**; cost advantage **unmeasured**. **Support: qualified; confidence: limited** until the exact runtime is tested. Dependency `DEP-SC-BROWSER-APIS`: library attribution shares upstream browser APIs with observer-based arms. **QC: checked-no-discrepancy** for named documentation fields; individual source-file URLs returned cache misses, so no code execution or implementation audit is claimed.

## SC-C10 — Performance Timeline buffering: finite, type-specific evidence

**Source:** W3C [Performance Timeline editor's draft, 26 October 2026](https://w3c.github.io/performance-timeline/), §§2, 4.1–4.2 and 5.6. `buffered` exposes available earlier entries of a supported type; storage limits and dropped-entry handling are explicit. This is a mutable work-in-progress specification, not verified support in a chosen Chromium build.

**Researcher implication:** a bounded application record can retain selected observed entries, but cannot be called a complete retrospective trace. Feature detection, observer start/flush, frame scope, limits, eviction and export failures need conformance checks. Do not assume all implementations expose the draft's loss counter.

**Appraisal:** specification boundary **adequate**; deployed conformance **unclear**. **Support: qualified; confidence: limited** for implementation. Shares `DEP-SC-BROWSER-APIS`; neither this draft nor library documentation independently validates experimental accuracy. **QC: checked-no-discrepancy** for the stated draft behavior.

## SC-C11 — JS Self-Profiling: candidate sampled evidence, not a full trace

**Source:** WICG [JS Self-Profiling API draft](https://wicg.github.io/js-self-profiling/), accessed 2026-10-31, Profiling Sessions / Sampling / Document Policy. It samples execution stacks, allows the actual sampling rate to differ from the requested interval, and describes stopping when the sample buffer is full. The current draft's `js-profiling-mode` policy wording must not be assumed to match an older implementation's configuration.

**Researcher implication:** profile recording must cover the original interval to supply original samples; enabling it after the episode does not recover unrecorded stacks. This is not a rolling full-browser event recorder or proof of network/layout coverage. Chromium build support, policy headers, cross-origin filtering, source resolution and lifecycle/export behavior remain empirical checks.

**Appraisal:** sampled-recording boundary **adequate**; browser conformance and diagnostic sufficiency **unclear**. **Support: qualified; confidence: limited**. Shares `DEP-SC-BROWSER-APIS`. **QC: checked-no-discrepancy** for the inspected draft; no sampler implementation is adopted.

## Supplementary closest-work leads and search boundary

The [Argus original paper](https://www.usenix.org/system/files/atc21-weng.pdf), Weng, Huang, Nieh and Yang, USENIX ATC 2021, 193–207, introduction/§2 (PDF 2–3), includes causal diagnosis of a Chrome/macOS responsiveness issue. It strengthens the warning against claiming browser diagnosis itself as new. Evaluation and complete-cost equivalence were not appraised; keep it as a lead for the final related-work pass, not a verified equivalent or a new matrix study row.

Existing discovery occurrence `E-0633` / `Q-208`, *Prediction of performance anomalies in web-applications based-on software aging scenarios*, remains a historical-data prediction lead. The 2010 publisher URL and snippet do not establish a method comparison; no frozen occurrence disposition or identity merge is changed. Irrelevant search results and secondary retellings were not adopted as technical evidence.

The supplementary search did not establish an exact equivalent. Its queries, incomplete coverage, access errors and version boundaries cannot support an absence claim or close G3/G4. A finite citation/overlap pass and appraisal of any adopted statistical method remain separate work. In particular, neither Mertz's sample-release rule nor Shahedi's regression test selects valid inference for clustered browser episodes.

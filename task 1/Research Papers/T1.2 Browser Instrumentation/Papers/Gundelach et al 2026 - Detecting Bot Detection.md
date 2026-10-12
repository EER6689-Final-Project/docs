# Detecting Bot Detection: Prevalence, Techniques, and Implications for Web Measurement Research

- **Citation:** Gundelach, R., Mühlhauser, M., & Herrmann, D. (2026). *Detecting bot detection: Prevalence, techniques, and implications for web measurement research* (arXiv:2606.14525v1 [cs.CR]). https://doi.org/10.48550/arXiv.2606.14525
- **Zotero key:** 9TZCJ36B (gundelachDetectingBotDetection2026).
- **Source:** Zotero contains a preprint PDF child (7UUIVQHT) at https://arxiv.org/pdf/2606.14525v1 and a snapshot. This outline is for arXiv v1, submitted 12 June 2026.

## Abstract

The authors examine whether bot detection causes automated browser crawls to lose samples or receive blocked responses. A literature survey and a four-condition crawl of the Tranco Top 10K find that headless Chromium is blocked more often than other tested configurations, with many blocks attributed to bot detection. They also identify browser and header signals used by detection systems. This is a paraphrase of the v1 abstract.

## Outline Summary

- **Central idea**
  - Automated web measurement can be biased when browser runs are blocked or served differently, while papers often fail to report detection conditions and exclusions.
  - Distinguish explicit block outcomes from probing evidence, and vendor-confirmed attribution from inference based on cross-condition behavior.
- **Research problem and objectives**
  - Measure reporting of bot detection in web-measurement research, blocking prevalence across browser configurations, and techniques/sites involved (§§3, 5).
  - The work studies blocking-induced sample loss; downstream effects on individual measurement outcomes remain unmeasured (§6).
- **Approach and experimental setup**
  - Surveyed 132 papers across seven venues and retained 81 eligible automated-browser crawling studies (2020–2025). Two authors independently coded a stratified subset of 20 papers and report Cohen's κ = 0.90 (§3).
  - Scanned 10,000 Tranco homepages using Chromium headless/headed and Firefox headless/headed, for 40,000 planned visits (§5.1). Infrastructure failures and timeouts are reported separately.
  - Classified HTTP 403, 429, and 503 as soft blocks; examined response bodies and paired browser conditions; used vendor evidence and a header-spoofing experiment to assess attribution (§§5.1–5.3).
  - Instrumented page JavaScript to observe automation-related property/function probes. Detection prevalence and blocking prevalence are distinct outcomes.
- **Metrics and methods**
  - Paper coding criteria for reproducibility and bot-detection awareness; site-level success, soft-block, timeout, and infrastructure-failure rates; vendor-confirmed and inferred attribution; detection-probe prevalence (§§3, 5).
  - Paired browser-condition comparisons, header-spoofing intervention, and provider-level descriptive analysis (§5).
- **Key results**
  - In the v1 Top 10K scan, soft-block rates were 15.2% for Chromium headless, 7.2% for Chromium headed, and 6.8% for each Firefox condition (§5.3).
  - The authors attribute 82% of observed blocks to bot detection: 59% vendor-confirmed and 23% inferred from condition-dependent blocking. The abstract reports that 75% of Chromium-headless-only blocks were attributable to header-level signals in the spoofing experiment (§5.3).
  - The literature survey found 83% of the 81 eligible studies omitted discussion of bot-detection blocking (§3.2). This describes the reviewed corpus and coding criteria, not all web measurement research.
- **Limitations and interpretation**
  - Single European datacenter vantage point and scan period; Top 10K homepages only; HTTP 200 content degradation is not detected; headed automation is not equivalent to human browsing (§6 limitations).
  - Browser/version, site selection, and explicit HTTP-status definitions condition the prevalence estimates. Downstream effects on specific measurement outcomes remain future work (§6).
- **Author-stated future work**
  - Measure downstream effects of bot-detection blocking on particular web measurement outcomes; the limitations also motivate broader vantage points and coverage beyond homepages (§6).
- **Gap identified by us**
  - **Preliminary inference:** report attempted, successful, blocked, and failed navigations by browser mode, retaining browser/version and response evidence. Whether this is needed in this project's protocol remains open.
- **Relationship to our profiler**
  - This study identifies a threat to validity and representativeness of automated browser measurements. It does not evaluate profiler instrumentation overhead or establish that this project will encounter the same rates.
- **Important quotations and page numbers**
  - No direct quotation transcribed. Anchors: study selection/coding §§3.1–3.2; scan method §5.1; prevalence and header-spoofing results §5.3; limitations and implications §6. arXiv HTML/PDF v1; page numbers not transcribed.
- **Concise takeaway**
  - Headless mode can change which sites enter an automated measurement sample; report blocking and failures instead of silently dropping them.

## T1.2 Evidence Check

- **Qualified:** Rates refer to a single-vantage, single-period Tranco Top 10K scan and the v1 definitions; they are not universal rates for Chromium automation.
- **Preliminary inference:** An explicit navigation outcome/failure record is a candidate protocol safeguard. No final method or research question is selected.

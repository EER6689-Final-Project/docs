# A Vital Improvement? Relating Google's Core Web Vitals to Actual Web QoE

- **Citation:** Wehner, N., Amir, M., Seufert, M., Schatz, R., & Hoßfeld, T. (2022). A vital improvement? Relating Google's Core Web Vitals to actual web QoE. *2022 14th International Conference on Quality of Multimedia Experience (QoMEX)*, 1–6. https://doi.org/10.1109/QoMEX55416.2022.9900881
- **Zotero key:** `2LYVIL8I`.
- **Source:** Original paper is PDF pp. 2–7 after a publisher-repository cover page; references below use paper pp. 1–6 (PDF page = paper page + 1).

## Abstract

> Providing sophisticated web Quality of Experience (QoE) has become paramount for web service providers and network operators alike. Due to advances in web technologies (HTML5, responsive design, etc.), traditional web QoE models focusing mainly on loading times have to be refined and improved. In this work, we relate Google’s Core Web Vitals, a set of metrics for improving user experience, to the loading time aspects of web QoE. To this end, we first perform objective measurements in the web using Google’s Lighthouse. To close the gap between metrics and experience, we complement these objective measurements with subjective assessment by performing multiple crowdsourcing QoE studies. In these studies, we use CWeQS, a customized framework to emulate the entire web page loading process, and ask users for their experience while controlling the Core Web Vitals. Our results suggest that the Core Web Vitals have less predictive value for web QoE than expected and that page loading times remain the main influence factor in this context.

- **Abstract transcription:** From paper p. 1, typography and PDF line-break hyphenation normalized.

## Outline Summary

- **Central idea**
  - When the experiment asks for *a rating of a page load*, overall load duration may dominate even if the experiment changes individual Web Vitals.
  - This is not a test that Core Web Vitals are universally invalid; it tests particular ratings under custom controlled stimuli.
- **Research question and objectives**
  - Explicit: “To which extent do the CWV metrics correlate with the end-user’s web QoE?” (paper p. 1).
  - Measure network sensitivity on real sites; then independently manipulate loading, input delay and layout shift on three synthetic pages and collect subjective scores.
- **Approach, participants and setup**
  - ≥30 Lighthouse runs per site/condition for 50 Tranco sites, desktop/mobile emulation; Docker/`tc` delays, packet loss and bandwidth (paper pp. 1–2).
  - CWeQS uses preloaded assets and scheduled DOM-element appearance for news, shopping and blog pages; manipulated overall PLT 2/5/10 s and LCP/FID/CLS stimulus parameters; ratings on a five-point ACR scale (pp. 3–4).
  - After filtering: 183 people/1,098 LCP ratings, 140/840 FID ratings and 207/1,014 CLS ratings; article also states 323 valid participants overall, indicating study-specific counts are not necessarily distinct people (p. 5).
- **Metrics and results**
  - LCP and SI were network-sensitive in Lighthouse; FID/CLS less so for this corpus and configuration (p. 3).
  - Under fixed 2/5/10 s load settings, variation in each manipulated CWV did not significantly change these subjective load-experience MOS values; PLT and SI had Spearman correlations −0.74 and −0.70 with individual ratings (pp. 5–6).
  - Page-load-time MOS model uses *only three fixed PLT levels*, so its R² close to one is not evidence for a universally linear QoE law (p. 5).
- **Limitations and context**
  - **Author-stated:** inability to abandon a crowdsourcing trial differs from field engagement; CWV influences may have gone undetected due to the experimental design (p. 6).
  - **Our assessment:** controlled DOM timers and preloaded assets suppress production/network dynamics; tasks and user-rating prompt privilege loading; first-input-delay FID was a CWV **in 2022** but was replaced by INP in 2024. Lighthouse navigation audits do not themselves create real first-input interactions, so treat reported Lighthouse FID as requiring protocol-level scrutiny, not as a current metric.
- **Author-stated future work**
  - Modify CWeQS/studies to include user engagement and directly compare with field-focused Google findings (p. 6).
- **Relationship to our profiler**
  - Reuse paired objective/subjective layers and controlled metric perturbations, but never claim that this study tests current INP or that a load-only synthetic rating represents field engagement.
  - Candidate issue from us: validation depends on the outcome/question and stimulus, not merely on whether a metric has a good/poor threshold.
- **Important quotations**
  - “To which extent do the CWV metrics correlate with the end-user’s web QoE?” — paper p. 1 (PDF p. 2).
  - “we cannot rule out a potential influence of the CVW on the MOS, that we might have not been able to detect due to our study design.” — paper p. 6 (PDF p. 7; typo `CVW` in source).
- **Concise takeaway**
  - Distinguish a CWV definition from its validity for a *particular subjective task*; preserve metric vintage (FID versus INP).

## T1.1 Claim Check

- **Qualified:** T1.1's claim that this study questions CWV as a complete QoE model is defensible; its conclusion is conditional on three custom pages, a load-rating task, and the 2022 LCP/FID/CLS set. This paper cannot settle current INP's validity.

# Do you agree? Contrasting Google’s Core Web Vitals and the impact of cookie consent banners with actual web QoE

- **Citation:** Wehner, N., Seufert, M., Schatz, R., & Hoßfeld, T. (2023). Do you agree? Contrasting Google’s Core Web Vitals and the impact of cookie consent banners with actual web QoE. *Quality and User Experience, 8*, article 5. https://doi.org/10.1007/s41233-023-00058-3
- **Zotero key:** `22HAD6YA`.
- **Source:** Original open-access article, PDF pp. 1–18; references use PDF pages and section titles.

## Abstract

> Providing sophisticated web Quality of Experience (QoE) has become paramount for web service providers and network operators alike. Due to advances in web technologies (HTML5, responsive design, etc.), traditional web QoE models focusing mainly on loading times have to be refined and improved. In this work, we relate Google’s Core Web Vitals, a set of metrics for improving user experience, to the loading time aspects of web QoE, and investigate whether the Core Web Vitals and web QoE agree on the perceived experience. To this end, we first perform objective measurements in the web using Google’s Lighthouse. To close the gap between metrics and experience, we complement these objective measurements with subjective assessment by performing multiple crowdsourcing QoE studies. For this purpose, we developed CWeQS, a customized framework to emulate the entire web page loading process, and ask users for their experience while controlling the Core Web Vitals, which is available to the public. To properly configure CWeQS for the planned QoE study and the crowdsourcing setup, we conduct pre-studies, in which we evaluate the importance of the loading strategy of a web page and the importance of the user task. The obtained insights allow us to conduct the desired QoE studies for each of the Core Web Vitals. Furthermore, we assess the impact of cookie consent banners, which have become ubiquitous due to regulatory demands, on the Core Web Vitals and investigate their influence on web QoE. Our results suggest that the Core Web Vitals are much less predictive for web QoE than expected and that page loading times remain the main metric and influence factor in this context. We further observe that unobtrusive and acentric cookie consent banners are preferred by end-users and that additional delays caused by interacting with consent banners in order to agree to or reject cookies should be accounted along with the actual page load time to reduce waiting times and thus to improve web QoE.

- **Abstract transcription:** Author abstract from PDF p. 1, line-break hyphenation normalized; no paraphrase inside the block quote.

## Outline Summary

- **Central idea**
  - Extends [[Wehner et al 2022 - A Vital Improvement]] with pre-studies of experimental design and an intervention on consent banners, which can change both Web Vital readings and users' ability to interact with content.
  - A metric reading is not the same thing as a task-specific judgement or the time until useful content can be accessed.
- **Research question and objectives**
  - Explicit: “To which extent do the CWV metrics correlate with the end-user’s web QoE?” (p. 2).
  - Test robustness of subjective-task design; compare three 2022-era CWV with ratings; examine banner type, appearance, annoyance and extra time to content interaction.
- **Approach and setup**
  - ≥30 Lighthouse runs on 50 Tranco URLs under network shaping, desktop/mobile; separate CWeQS study manipulates timed DOM appearance on three *preloaded, custom* pages rather than varying real network requests (pp. 4–6).
  - Pre-studies: 92 unique participants/951 ratings for element loading order; 137/979 for image-vs-link validation task (pp. 7–8).
  - Main CWV study: after filters, LCP 183 participants/1,098 ratings, FID 140/840, CLS 207/1,014; study also says 323 valid participants in total, so three cohort sizes must not be summed as distinct persons (p. 10).
  - Consent-banner study: 87 participants/455 rated stimuli; 27 combinations of three banner types, three arrival times and three PLTs (pp. 11–12).
- **Metrics, analyses and results**
  - Historic LCP/FID/CLS, SI, PLT, five-point ACR/MOS; compare controlled doses, Spearman correlations, Mann–Whitney U, and 95% CIs (pp. 8–11).
  - Changing historic CWV stimuli within fixed PLT groups did not materially change reported load-experience MOS; overall PLT/SI correlated −0.74/−0.70 with subjective ratings in the loading study (pp. 10–11).
  - Banner interactions delayed first *content* interaction by median 3.1 s versus a different no-banner study group; this is context-specific and not a universal banner delay (p. 14).
  - Banner appearance could become the LCP candidate; overlay banners in their fixture yielded no layout shift, while a header could shift the page. The measurement may describe the banner rather than the user's primary content (p. 15).
- **Author-stated limitations**
  - Participants cannot abandon trials as real users might; imposed task may dominate ratings; *three* PLT values constrain conclusions about linear QoE response (p. 16).
  - Consent fixtures were simplified; no third-party consent systems; everyone was required to click the banner before proceeding even though many real sites do not require this; restricted combinations (p. 16).
- **Methodology weaknesses identified by us**
  - Many subjective ratings per person and fixed stimuli are not independent page samples; artificial element timing and preloaded assets differ from live production network/browser dynamics; consent/no-consent cohorts are not a within-person randomized comparison; historic FID is not current INP.
- **Author-stated future work**
  - Compare engagement-based and ratings-based studies directly; use explainable AI; broaden consent treatments; test other browsers/page conditions as applicable (pp. 16–17).
- **Relationship to our profiler**
  - Track whether a measured LCP relates to meaningful page content or to an overlay; separate browser metric validity from task outcome and banner-induced delay.
  - Reuse dose-controlled fixtures and an explicit interaction protocol but do not borrow its 2022 FID threshold as current CWV semantics.
- **Important quotations**
  - “To which extent do the CWV metrics correlate with the end-user’s web QoE?” — PDF p. 2.
  - “we cannot rule out a potential influence of the CWV on the MOS, that we might have not been able to detect due to our study design.” — PDF p. 16.
- **Concise takeaway**
  - A site can present a technically valid Web Vital value whose selected element or observation window tells little about the user's next task; report context and limitations.

## T1.1 Claim Check

- **Qualified:** Supports claim of limited predictive value for these historic CWV under these rating and banner fixtures; *not* proof that all CWV fail for all field populations or that current INP was tested.

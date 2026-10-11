# Modeling User-Centered Page Load Time for Smartphones

- **Citation:** Kelton, C., Ryoo, J., Balasubramanian, A., Bi, X., & Das, S. R. (2020). Modeling user-centered page load time for smartphones. *MobileHCI '20*, 1–12. https://doi.org/10.1145/3379503.3403565
- **Zotero key:** `GJ9PAHK3`.
- **Source:** Original PDF, 12 pages; citations use PDF pagination.

## Abstract

> Page Load Time (PLT) is critical in measuring web page load performance. However, the existing PLT metrics are designed to measure the Web page load performance on desktops/laptops and do not consider user interactions on mobile browsers. As a result, they are ill-suited to measure mobile page load performance from the perspective of the user. In this work, we present the Mobile User-Centered Page Load Time Estimator (muPLTest), a model that estimates the PLT of users on Web pages for mobile browsers. We show that traditional methods to measure user PLT for desktops are unsuited to mobiles because they only consider the initial viewport, which is the part of the screen that is in the user’s view when they first begin to load the page. However, mobile users view multiple viewports during the page load process since they start to scroll even before the page is loaded. We thus construct the muPLTest to account for page load activities across viewports. We train our model with crowdsourced scrolling behavior from live users. We show that muPLTest predicts ground truth user-centered PLT, or the muPLT, obtained from live users with an error of 10-15% across 50 Web pages. Comparatively, traditional PLT metrics perform within 44-90% of the muPLT. Finally, we show how developers can use the muPLTest to scalably estimate changes in user experience when applying different Web optimizations.

- **Abstract transcription:** Author abstract, PDF p. 1; notation `muPLTest` represents the paper's `muPLT` with subscript `est`, and line breaks were normalized.

## Outline Summary

- **Central idea**
  - People on phones may scroll before the initial viewport finishes loading; a single above-the-fold measurement may describe the wrong part of their experience.
  - The authors infer an implicit mobile user-perceived completion time from scroll pauses, then predict it using metrics from several viewports.
- **Research problem, objectives and question**
  - Explicit question: “do these traditional page load metrics measure user-centered load time?” (p. 1).
  - Characterize early scrolling, obtain human-centered mobile muPLT, and estimate it automatically without a new user study for every optimization (pp. 1–3).
- **Approach and participants**
  - 50 pages sampled across Alexa Top 500 categories; synchronized recorded viewport videos permit simulated scrolling while standardizing page loads (pp. 4–5).
  - 200 free-browsing participants across four device/network conditions (50 each); 50 in targeted search and 50 in the separate push-optimization validation; initial qualitative replay check had 30 (pp. 4–5, 10). The introduction says “300 users”; do not sum cohorts as unique people without checking overlap.
  - Recorded on Nexus 5/Pixel XL and Ubuntu desktop, Chrome 61/67; emulated 3G, 4G and desktop broadband conditions; Microworkers respondents across 22 countries (p. 5).
- **Methods and metrics**
  - muPLT is the time of an individual's first scroll pause longer than a page/condition-specific Tukey outlier threshold computed from users' inter-scroll intervals; this is a *proxy for engagement*, not direct access to someone's thoughts (pp. 6–7).
  - Multiple SpeedIndex averages SpeedIndex across recorded viewports with equal viewport weights; use multi-viewport FCP plus OnLoad/ordinary SI in a LASSO model; evaluate by ten-fold, leave-five-out cross-validation (pp. 8–9).
  - Evaluate server-push alternatives on ten pages using a new 50-person validation study (p. 10).
- **Key results**
  - For the median mobile page, users view roughly three viewports before reporting load; desktop users usually stay in the first; on many pages >70% of Nexus users visit multiple viewports (pp. 5–6).
  - Traditional metrics differed from defined muPLT by about 42–70% on median pages under studied networks, while the fitted estimator reported median prediction error 10–15% for the 50-page cross-validation; push-case median absolute error 7.8% on ten studied pages (pp. 7–10).
  - Explicit-feedback/muPLT Pearson correlations 0.91 (4G) and 0.84 (3G); correlation alone does not establish agreement (p. 7).
- **Limitations**
  - **Author-described:** standardized replay sometimes looked blurry or stale (30-person qualitative check), and scrolling-caused load changes were tested but results not shown (p. 4). Interaction focus deliberately excludes tapping/pinching (pp. 3–4).
  - **Our assessment:** a long pause can reflect reading, distraction or an unfinished interaction; equal viewport weights ignore actual gaze/time in viewport; page-level cross-validation within the same corpus is not independent out-of-domain validation; aged Chrome and HTTP/2 push limit transfer.
- **Author-stated future work**
  - No distinct future-work programme is explicitly set out in the paper's conclusion; do not attribute our suggested extensions to the authors.
- **Relationship to our profiler**
  - Mobile emulation changes the *workload and lifecycle*, not just viewport width. Include the scripted interaction and measured viewports in any synthetic claim.
  - A distribution of controlled navigation-only runs cannot automatically represent the browsing experience measured by a scrolling-person study.
- **Important quotations**
  - “The critical question is: do these traditional page load metrics measure user-centered load time?” — p. 1.
  - “we define the long pause as the first outlier in the empirical distribution of all users’ inter-scroll times” — p. 7.
- **Concise takeaway**
  - Decide whether the target construct is first-viewport load or a particular multi-viewport user journey; the answer determines the metric.

## T1.1 Claim Check

- **Qualified:** Supports a substantial mobile initial-viewport limitation under the studied page, replay and scrolling conditions; its “ground truth” is a defined scroll-pause proxy, not independent universal ground truth for perceived load.

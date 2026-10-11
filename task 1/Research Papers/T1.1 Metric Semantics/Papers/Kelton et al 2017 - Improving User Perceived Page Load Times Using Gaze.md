# Improving User Perceived Page Load Times Using Gaze

- **Citation:** Kelton, C., Ryoo, J., Balasubramanian, A., & Das, S. R. (2017). Improving user perceived page load times using gaze. *14th USENIX Symposium on Networked Systems Design and Implementation (NSDI '17)*, 545–559. https://www.usenix.org/conference/nsdi17/technical-sessions/presentation/kelton
- **Zotero key:** `WUUGBCG4`.
- **Source:** Original 17-page PDF (first page is a cover; printed pp. 545–559 correspond to PDF pp. 2–16). Read the original PDF; citations below use printed pages.

## Abstract

> We take a fresh look at Web page load performance from the point of view of user experience. Our user study shows that perceptual performance, defined as user-perceived page load time (uPLT) poorly correlates with traditional page load time (PLT) metrics. However, most page load optimizations are designed to improve the traditional PLT metrics, rendering their impact on user experience uncertain. Instead, we present WebGaze, a system that specifically optimizes for the uPLT metric. The key insight in WebGaze is that user attention and interest can be captured using a user’s eye gaze and can in turn be used to improve uPLT. We collect eye gaze data from 50 users across 45 Web pages and find that there is commonality in user attention across users. Specifically, users are drawn to certain regions on the page, that we call regions of high collective fixation. WebGaze prioritizes loading objects that exhibit a high degree of collective fixation to improve user-perceived latencies. We compare WebGaze with three alternate strategies, one of which is the state-of-the-art system that also uses prioritization to improve user experience. Our evaluation based on a user study shows that WebGaze improves median uPLT for 73% of the Web pages compared to all three alternate strategies.

- **Abstract transcription:** From printed p. 545; normalized extraction line breaks and split words (the PDF title on its first page uses the singular “Time” whereas Zotero and the cover use “Times”).

## Outline Summary

- **Central idea**
  - A browser's load event or pixel-based Speed Index may disagree with when a person thinks a page has finished loading.
  - The authors measure perceived completion with people, observe where they look, then prioritize resources in visually important regions.
- **Research problem and objectives**
  - Existing load-time optimizers generally target browser milestones, leaving their effect on actual perceived completion uncertain (pp. 545–546).
  - Define user-perceived page-load time (uPLT), measure its correspondence with OnLoad and Speed Index, test whether gaze reveals shared interest, and evaluate whether WebGaze reduces uPLT.
  - No formal research-question list is stated; these are the study's stated aims, not quotations of formal questions.
- **Approach**
  - **Perceptual study:** Ask viewers to press a key when a recording *looks loaded*; adjust for calibrated response time and reject responses before first paint or after final visual change (p. 547).
  - **Page corpus:** 45 pages, three from each of 15 Alexa categories, spanning popularity bands. Additional network-condition study uses 23 pages and 30 users (p. 547).
  - **Participants:** 50 lab and 50 online participants for uPLT comparison; webcam gaze captured from 50 lab users, with a 23-person higher-end eye-tracker comparison. Evaluation of WebGaze used separate sets of 100 people for each of three pairwise comparisons (pp. 547, 549, 553).
  - **Browser/workload:** Chrome 52, 1920×1080 page-load recordings at 10 fps; primary DSL profile 50 ms RTT, 1.3 Mbps down, 384 Kbps up; additional WiFi-like and 3G-like profiles (p. 547).
  - **Optimization:** Split viewport into visual regions; collective fixation is the proportion of gaze tracks visiting a region. At a 0.7 fixation threshold, map DOM objects and WProf dependencies to priority resources and serve with HTTP/2 Server Push (pp. 550–552).
  - **Comparison:** WebGaze versus default loading, push-all and Klotski; local Apache serves captured resources, while some nondeterministic remote resources remain (p. 553).
- **Metrics and analysis**
  - uPLT is time from page request until *the person perceives completion*, not a browser API metric (p. 546).
  - Compare medians across users with OnLoad, DOMContentLoaded and Speed Index, and correlate these across pages; also analyze gaze collective fixation and per-page improvements (pp. 548, 550, 553–554).
- **Key results**
  - Across 45 pages, median uPLT correlations were about 0.46 with OnLoad, 0.44 with Speed Index and 0.21 with DOMContentLoaded; Speed Index was about 3.5 s *below* uPLT for more than 87% of pages (p. 548).
  - The relationship varied with network conditions: OnLoad–uPLT correlation about 0.55 under 3G-like conditions and about 0.74 under WiFi-like conditions (pp. 548–549).
  - Some regions receive disproportionate attention: at least 20% of regions had fixation from ≥90% of viewers, while about 25% were viewed by fewer than 30% (p. 550).
  - WebGaze beat each of the three alternatives in median uPLT on 33/45 pages (73%); it also *lost* on some pages due to excessive pushing, demonstrating that optimization can help one metric while harming another (pp. 553–555).
- **Interpretation**
  - Loading all resources or painting many pixels early is not the same thing as loading *what viewers care about*. This supports a narrow construct-validity warning, not a claim that all synthetic metrics are useless.
  - The paper optimizes *a user-defined perceptual outcome* rather than validating a custom CDP profiler against DevTools or Lighthouse.
- **Limitations and methodology weaknesses**
  - **Discussed by authors:** server-push bandwidth contention and two pathological pages; gaze order depends on rendering order; mobile gaze accuracy/energy, changing content, and security/privacy concerns (pp. 552, 554, 556).
  - **Our assessment:** recorded videos constrain variance but cannot represent interactive browsing/scrolling; Chrome 52, HTTP/2 Server Push and local consolidation limit direct transfer to present-day live profiling; collective user gaze need not represent every individual's goal.
- **Author-stated future work**
  - Explore fixation duration and order (p. 550), prioritize considering object sizes (p. 553), collect gaze under different load orders and develop more deployable/secure gaze support (p. 556).
- **Relationship to our profiler**
  - Reuse the separation of browser measurements from human-perceived outcomes, explicit experimental network profiles, and multi-page sampling.
  - Candidate question *from us*: under what stated conditions can a synthetic metric responsibly be presented as a diagnostic rather than as user-perceived completion? This paper does not establish that no one has answered it.
- **Important quotations**
  - “uPLT is the time between the page request until the time the user ‘perceives’ that the page is loaded.” — p. 546.
  - “Speed Index ... is about 3.5 seconds lower than uPLT for over 87% of the Web pages.” — p. 548.
- **Concise takeaway**
  - Do not call a low synthetic loading number proof of good user experience; specify the measured construct, workload and intended inference.

## T1.1 Claim Check

- **Qualified:** The report's assertion that conventional load metrics poorly represent user-perceived completion is supported *for these pages, users and conditions*. It does not prove they fail on every site or network.
- **Confirmed:** The paper directly compares uPLT against OnLoad, Speed Index and DOMContentLoaded; the 73% improvement refers to median uPLT over *all three* alternatives on 33 of 45 pages.

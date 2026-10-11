# Perceived Performance of Top Retail Webpages In the Wild: Insights from Large-scale Crowdsourcing of Above-the-Fold QoE

- **Citation:** Gao, Q., Dey, P., & Ahammad, P. (2017). Perceived performance of top retail webpages in the wild: Insights from large-scale crowdsourcing of above-the-fold QoE. *Proceedings of Internet QoE '17*, 13–18. https://doi.org/10.1145/3098603.3098606
- **Zotero key:** `6EFLN7PR`.
- **Source:** Six-page original paper, PDF pp. 1–6 = printed pp. 13–18; page references below use printed pagination.

## Abstract

> Clearly, no one likes webpages with poor quality of experience (QoE). Being perceived as slow or fast is a key element in the overall perceived QoE of web applications. While extensive effort has been put into optimizing web applications (both in industry and academia), not a lot of work exists in characterizing what aspects of webpage loading process truly influence human end-user's perception of the Speed of a page. In this paper we present SpeedPerception, a large-scale web performance crowdsourcing framework focused on understanding the perceived loading performance of above-the-fold (ATF) webpage content. Our end goal is to create free open-source benchmarking datasets to advance the systematic analysis of how humans perceive webpage loading process. In Phase-1 of our SpeedPerception study using Internet Retailer Top 500 (IR 500) websites, we found that commonly used navigation metrics such as onLoad and Time To First Byte (TTFB) fail (less than 60% match) to represent majority human perception when comparing the speed of two webpages. We present a simple 3-variable-based machine learning model that explains the majority end-user choices better (with 87 ± 2% accuracy). In addition, our results suggest that the time needed by end-users to evaluate relative perceived speed of webpage is far less than the time of its visualComplete event.

- **Abstract transcription:** Author abstract, printed p. 13, with footnote numerals and PDF line-break hyphenation removed; wording otherwise preserved.

## Outline Summary

- **Central idea**
  - SpeedPerception asks people to compare videos of two pages loading and evaluates whether browser and visual metrics predict which one they perceive as faster.
  - Visual progress *before the person decides* may describe this choice better than waiting for full visual completion.
- **Research problem and objectives**
  - Existing browser metrics lack large, reproducible human-judgement benchmarks for perceived above-the-fold loading speed (pp. 13–14).
  - Build a crowdsourcing framework and dataset, quantify agreement of single metrics with majority votes, and train a metric-based choice predictor.
  - **Explicit study question:** “How does one evaluate end-user perception of webpage speed?” (p. 15).
  - **Three explicit hypotheses:** no single current metric exceeds 90% agreement; visual metrics outperform nonvisual metrics; people decide before Visual Complete (p. 15).
- **Approach and setup**
  - Collect HARs, metrics and recorded viewport videos with WebPageTest from Internet Retailer Top 500 URLs: Chrome 50, 10/5 Mbps cable, Northern California, ten tests per URL (p. 15).
  - Construct 160 video pairs from 115 unique pages, matching Visual Complete within 5% and stratifying on Speed Index (SI) and Perceptual Speed Index (PSI) differences (pp. 15–16).
  - Crowdsourced users view simultaneous side-by-side videos and select Left, Right or About the same; 16 test pairs and five known-answer honeypots per session (p. 16).
  - >5,400 sessions in two months, 51% accepted, >40,000 valid votes, >250 per pair. **The paper does not state a count of distinct participants:** sessions are not independent people (p. 16).
- **Metrics and methods**
  - Compare nonvisual TTFB/DCLend/onLoad with first paint, render, SI, PSI and Visual Complete; record Time to Click (TTC), i.e. when the participant chooses (pp. 14, 16).
  - SI uses histogram-based visual progress; PSI uses structural similarity to account for visual changes; variants truncate the integration at onLoad or TTC (pp. 14–15).
  - Encode each metric as a three-way synthetic vote under a ±5% relative-difference rule; compare with majority human votes using matching rates, Cramér's V and chi-square; train Random Forest/Gradient Boosting models with ten-fold cross-validation (pp. 16–17).
- **Key results**
  - onLoad matches 55% and original SI 53% of majority choices; TTC-truncated SI matches around 84%, and a three-visual-variable model approaches 87–90% cross-validated accuracy in this data (p. 17).
  - Median TTC is 5,746 ms; most respondents chose after render but before Visual Complete (pp. 16–17).
  - Perceived relative speed and the timing endpoint chosen for SI/PSI are different constructs from the browser load event.
- **Interpretation and caveats**
  - TTC-truncated metrics use *the user's actual decision time*. Their impressive result cannot simply be transferred to an automated profiler without an independently estimated TTC/end point (p. 18).
  - Predicting a majority choice about two recorded above-the-fold videos is not predicting an individual's interactive or field experience.
- **Limitations**
  - **Author-stated:** pop-ups/jitter not isolated, no demographics, one page per judgement rather than browsing sequences, device-specific human response-time variability, and difficult-to-interpret predictors (pp. 17–18).
  - **Our assessment:** self-selected respondents, retail-only pages, Visual-Complete-matched pair sampling, many votes per page, and potential cross-validation leakage if pairs derived from the same page are split across folds (the paper does not establish a page-grouped holdout).
- **Author-stated future work**
  - Model TTC or another metric endpoint; isolate visual jitter; compare retail with Alexa and desktop with mobile; test browsing sequences and demographic/device effects; build interpretable models (p. 18).
- **Relationship to our profiler**
  - Reuse its clear separation of human labels from synthetic features, repeated page runs, pair matching and data-quality checks *if* we later study perceptual validity.
  - Candidate gap *from us*: whether a deployable, purely browser-observable end point can substitute for human TTC; this is a hypothesis for later literature checking, not a final thesis gap.
- **Important quotations**
  - “How does one evaluate end-user perception of webpage speed?” — p. 15.
  - “While onLoad only matches 55% of the majority vote, original SI ... is even worse (53% match).” — p. 17.
- **Concise takeaway**
  - Define what outcome is predicted, how human ground truth is gathered, and whether a synthetic metric's endpoint is actually observable in deployment.

## T1.1 Claim Check

- **Qualified:** The paper's relative-speed comparisons support a limited construct-validity challenge to onLoad/TTFB and original SI on this sampled retail corpus, not a universal claim about all Web Vitals or sites.
- **Confirmed:** The reported three-variable model's approximate 87 ± 2% performance is in the abstract; TTC-based inputs are *not* independently derived from an automated browser run.

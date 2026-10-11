# Speed Index: Relating the Industrial Standard for User Perceived Web Performance to Web QoE

- **Citation:** Hoßfeld, T., Metzger, F., & Rossi, D. (2018). Speed Index: Relating the industrial standard for user perceived web performance to web QoE. *2018 Tenth International Conference on Quality of Multimedia Experience (QoMEX)*, 1–6. https://doi.org/10.1109/QoMEX.2018.8463430
- **Zotero key:** `9A8CMSAY`.
- **Source:** Six-page original PDF. PDF/printed pages 1–6.

## Abstract

> In 2012, Google introduced the Speed Index (SI) metric to quantify the speed of the Web page visual completeness for the actually displayed above-the-fold (ATF) portion of a Web page. In Web browsing a page might appear to the user to be already fully rendered, even though further content may still be retrieved, resulting in the Page Load Time (PLT). This happens due to the browser progressively rendering all objects, part of which can also be located below the browser window’s current viewport. The SI metric (and variants) thereof have since established themselves as a de facto standard in Web page and browser testing. While SI is a step in the direction of including the user experience into Web metrics, the actual meaning of the metric and especially its relationship between Speed Index and Web QoE is however far from being clear. The contributions of this paper are thus to first develop an understanding of the SI based on a theoretical analysis and second, to analyze the interdependency between SI and MOS values from an existing public dataset. Specifically, our analysis is based on two well established models that map the user waiting time to a user ACR-rating of the QoE. The analysis show that ATF-based metrics are more appropriate than pure PLT as input to Web QoE models.

- **Abstract transcription:** PDF p. 1 with formatting and line-break hyphenation normalized; Zotero's `abstractNote` stops midway and is insufficient on its own.

## Outline Summary

- **Central idea**
  - Speed Index and related *integrals of incomplete progress* distinguish a gradually rendered page from a blank page that suddenly appears at the end.
  - When modeling users' quality ratings, the study's above-the-fold byte-index proxy fits aggregated ratings better than full page-load time; it does **not** establish that individual users' ratings are predictable.
- **Research problem, objectives, questions**
  - The mathematical meaning of SI and its relationship to subjective Web QoE were unclear (pp. 1–2).
  - Derive properties of SI, investigate time-discrete measurement bias, and fit IQX/WQL waiting-time–QoE models using existing user ratings.
  - No formal research questions; the authors ask whether WQL or IQX can apply when SI approximates perceived waiting time (p. 4).
- **Approach and dataset**
  - Theoretical examples vary when and how visual progress occurs; derivation models sampling every Δt and obtains Δt/2 absolute bias for smooth linear progress (pp. 3–4; equations/figures should be visually checked before mathematical quotation).
  - Reanalysis of public Web QoE dataset: 8,687 browsing sessions rated by 241 volunteers in Chrome on 12 non-landing pages from Alexa top 100 (p. 4).
  - **Internal inconsistency:** conclusions say “only 25 pages are considered” (p. 6), while data description says twelve (p. 4). Preserve both counts and resolve against the underlying dataset before reuse.
  - Five-level Absolute Category Rating; aggregate subjective ratings by equal-count bins to estimate Mean Opinion Score (MOS) (pp. 4–5).
- **Metrics, models and results**
  - PLT, above-the-fold time, visual Speed Index, ObjectIndex, and ByteIndex; distinguish SI from BI: **the MOS fitting shown here primarily uses ByteIndex (ATF), not direct SI** (pp. 4–6).
  - Fit IQX exponential and WQL logarithmic models to aggregate MOS. No significant correlation between *individual ratings* and the reported timings/indices; stronger relationship appears after aggregating (p. 5).
  - Table II reports BI-ATF WQL MSE 0.053 versus PLT WQL MSE 0.168 for its binned fits; the authors say edge ratings are sparse so relative suitability of IQX/WQL is unresolved (p. 5).
- **Limitations and future work**
  - **Author-stated:** sparse observations at rating extremes, limited website diversity, and inconsistent reported page count; call for richer dataset, website-class-specific fits and task-weighted ByteIndex (pp. 5–6).
  - **Our assessment:** refitting and evaluating models on binned data can hide individual errors; reused dataset and assumptions are not independently validated here; avoiding session/task behavior limits external validity. Qualify any claim that SI itself was validated against QoE.
- **Relationship to our profiler**
  - Reuse definition of progressive visual metrics and explicit sampling-interval discussion; preserve whether a score uses pixels, bytes, objects, or subjective judgements.
  - Candidate issue *from us*: metric substitutions/aggregations can yield apparently strong QoE fits despite weak individual correspondence; do not present a diagnostic aggregate as subjective ground truth.
- **Important quotations**
  - “The first observation is that no significant correlation between the individual user ratings and the different time instants as well as the Speed Index can be observed in the data.” — p. 5.
  - “for the ByteIndex all bytes are born equal” — p. 6.
- **Concise takeaway**
  - A visual-progress index has a clear algorithm, but its validity for individual experience needs separate evidence; this study's strongest empirical fit is for *ByteIndex on aggregate MOS*.

## T1.1 Claim Check

- **Qualified:** The report's general statement about imperfect correspondence of SI and perception is compatible with this paper, but the model-fit result must be attributed to BI-ATF on aggregated ratings, not direct individual SI prediction.
- **Open bibliographic/method issue:** Twelve versus 25 study pages requires resolution before quoting a definitive page count outside this note.

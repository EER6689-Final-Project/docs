# How the Core Web Vitals Metrics Thresholds Were Defined

- **Citation:** McQuade, B., & Pollard, B. (2020, May 21; updated 2025, May 7). How the Core Web Vitals metrics thresholds were defined. *web.dev*. https://web.dev/articles/defining-core-web-vitals-thresholds
- **Zotero key:** `T3FHMMCH`.
- **Source:** Zotero-attached saved HTML, preserved as [McQuade and Pollard 2020 - How Core Web Vitals Thresholds Were Defined.html](McQuade%20and%20Pollard%202020%20-%20How%20Core%20Web%20Vitals%20Thresholds%20Were%20Defined.html); live article was also checked. This is an explanatory web article, not a peer-reviewed empirical study.

## Research question and approach

The authors explain the rationale for selecting Core Web Vitals thresholds and for classifying page/site performance using the 75th percentile of visits. They balance high-quality user experience, achievability for existing sites, and percentile robustness to outliers. For achievability, the article reports CrUX origin data from April 2020 and comparisons among top-performing sites; the current article page was last updated May 7, 2025 (article sections “Criteria” and “Choice of percentile”).

## Findings from the source

- The article lists p75 classification thresholds of LCP ≤2.5 s as good and >4 s as poor; INP ≤200 ms as good and >500 ms as poor; and CLS ≤0.1 as good and >0.25 as poor (article threshold table).
- It explains that the 75th percentile was selected to ensure that a majority of visits meet the target while limiting sensitivity to outliers. The authors illustrate that, for 100 visits, five unusually slow observations can affect a p95, which motivates avoiding a higher site-classification percentile (article “Choice of percentile”).
- The article says one threshold is applied to both desktop and mobile for simplicity and shared experience goals, while achievability is mostly based on mobile because of device constraints; it recognizes there is no single perfect threshold and presents the values as broad web-wide targets (article “Criteria”).

## Relevance and limits

This source documents the rationale behind a field-level, visit-weighted p75 classification convention. Its threshold-achievability evidence is tied to CrUX origin data as of April 2020 and the article’s stated comparison criteria. It does not validate p75 as the right summary for repeated controlled browser-agent runs, establish a confidence interval method, or show that the CWV thresholds are appropriate for this project’s research outcome.

**Researcher inference:** The p75 rationale is a useful example of aligning a percentile with an explicit population-level classification goal. The chosen percentile should still follow the profiler’s target population and decision rather than be copied by default.

## Provenance and version note

Zotero omits creators and date, but the saved article names Bryan McQuade and Barry Pollard and states original publication on May 21, 2020, with last update May 7, 2025. The repository copy is the Zotero-saved HTML version; the live article was checked for its current update date and threshold table.

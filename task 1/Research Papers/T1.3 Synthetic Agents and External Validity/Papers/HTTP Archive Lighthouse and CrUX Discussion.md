# Correlating Lighthouse scores to page-level CrUX data

- **Source type:** Community analysis / discussion; not peer-reviewed research or a controlled validation study.
- **Zotero key:** `NW3PJGSZ`.
- **Provenance:** Zotero URL and attached HTML snapshot `2CBZYFPH`: https://discuss.httparchive.org/t/correlating-lighthouse-scores-to-page-level-crux-data/2164. Original post by Rick Viscomi, 8 June 2021; HTTP Archive “Analysis” category.

## Source-supported details

The post joins URL-level CrUX data embedded in HTTP Archive page records with Lighthouse lab scores and reports weak-to-medium correlations for Core Web Vitals, including a negative Pearson correlation for FID in the initial analysis. The thread then identifies important interpretation issues: Lighthouse’s composite score is not a direct proxy for each individual field metric; its version-specific metric weights matter; Pearson correlation may be inappropriate for nonlinear score transformations; and TBT is only a lab proxy for FID (opening post and replies by Paul Irish, 9 June 2021).

## Use and limits

This is a worked example and useful methodological caution about comparing a composite lab score to individual field metrics. The result is tied to Lighthouse v7 scoring, one HTTP Archive dataset sample/query, and forum analysis; it should not be generalized as a current Lighthouse-to-CrUX calibration. Replies revise the initial interpretation, so cite the whole discussion and specify which analysis is being used.

**Researcher inference:** This source helps frame external validation: align the construct, version, and field metric before interpreting a lab/field association. It does not establish a stable predictive relationship.

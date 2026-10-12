# Lantern — Lighthouse documentation

- **Source type:** Official, version-controlled software documentation / model evaluation.
- **Zotero key:** `4XWMB3XH`.
- **Provenance:** Zotero URL https://github.com/GoogleChrome/lighthouse/blob/main/docs/lantern.md; attached HTML snapshot `69BWGC5Y`. Current source: https://github.com/GoogleChrome/lighthouse/blob/main/docs/lantern.md.

## Source-supported details

The document describes Lantern as a model that uses page activity to simulate browser execution. Its reported accuracy study sampled 300 URLs from Alexa Top 1000, HTTP Archive, and ad landing pages; it compares medians from nine runs in two environments. Reported rank correlations and mean absolute percentage errors vary by metric and comparison. The document concludes that Lantern has systematic error relative to DevTools throttling and emphasizes that user-centric metrics vary across runs (sections Accuracy, Lantern Accuracy Stats, Conclusions).

## Use and limits

The source’s own evaluation shows that a simulation can preserve useful rank information while still differing materially in absolute estimates. Its URL sample, metrics, environments, and Lighthouse implementation define the scope of those numbers. The document is on mutable `main`, and its sample includes older named sources such as Alexa rankings.

**Researcher inference:** Use Lantern’s calibration results to support separating rank validity from absolute-value validity. Recheck the pinned Lighthouse version before carrying its numerical accuracy estimates into a current study.

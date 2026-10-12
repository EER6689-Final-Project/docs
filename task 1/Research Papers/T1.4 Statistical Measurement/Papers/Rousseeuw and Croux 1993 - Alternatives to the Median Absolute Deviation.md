# Alternatives to the Median Absolute Deviation

- **Citation:** Rousseeuw, P. J., & Croux, C. (1993). Alternatives to the median absolute deviation. *Journal of the American Statistical Association, 88*(424), 1273–1283. https://doi.org/10.1080/01621459.1993.10476408
- **Zotero key:** `X7ZXVUQY`.
- **Source:** Zotero has no attachment. A primary author-hosted [11-page PDF](https://wis.kuleuven.be/stat/robust/papers/publications-1993/rousseeuwcroux-alternativestomedianad-jasa-1993.pdf) is available, but its text could not be extracted in the current review. This note is limited to the Zotero abstract and the bibliographic record; it does not claim details from unseen sections, tables, or experiments.

## Research question and approach

The abstract frames the problem as constructing explicit, 50%-breakdown scale estimators that improve on the normalized median absolute deviation (MAD) in Gaussian efficiency and applicability beyond symmetric distributions. It names two statistics: (S_n=1.1926\,\mathrm{med}_i\,\mathrm{med}_j|x_i-x_j|) and (Q_n), based on the first quartile of pairwise distances. The abstract states that neither requires a location estimate and that both can be computed in (O(n\log n)) time and (O(n)) storage.

## Findings from the source

- The abstract reports Gaussian efficiencies of 58% for (S_n) and 82% for (Q_n), compared with 37% for the normalized MAD.
- The authors state that the study examines influence functions, bias under implosion and explosion, finite-sample performance, and non-Gaussian models including a negative exponential model. The abstract reports lower gross-error sensitivity than MAD for (S_n) at that non-Gaussian model.

## Relevance and limits

This source provides candidate robust scale summaries for noisy, potentially asymmetric data and shows why the normalized MAD may not be the only relevant scale estimator. The numerical properties above are abstract-level claims; because the accessible PDF could not be read in this review, this note does not specify the finite-sample design, precise calibration conditions, comparative results beyond the abstract, or limitations in the paper’s experiments. It does not establish that either statistic is suitable for browser latency data.

**Researcher inference:** Robust scale summaries could be considered alongside quantiles when describing dispersion in the presence of outliers. Selecting one for this project requires checking its finite-sample behavior and defining the target distribution and measurement conditions.

## Provenance and metadata note

Zotero records the 1993 JASA article, pages 1273–1283, and DOI `10.1080/01621459.1993.10476408`. No Zotero child attachment is present. The author-hosted PDF is 11 pages, but its body text was not available to verify beyond the abstract-level details above.

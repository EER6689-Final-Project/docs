# Robust Analogs to the Coefficient of Variation

- **Citation:** Arachchige, C. N. P. G., Prendergast, L. A., & Staudte, R. G. (2022). Robust analogs to the coefficient of variation. *Journal of Applied Statistics, 49*(2), 268–290. https://doi.org/10.1080/02664763.2020.1808599
- **Zotero key:** `L59HPN96`.
- **Source:** Full article in [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9196089/). Zotero has a linked HTML child (`K6AH5QZI`) but no local attachment path and no PDF child; the article was read from the PMC full text.

## Research question and approach

The authors develop two quantile-based relative-spread measures as alternatives to the coefficient of variation (CV): (0.75\times\mathrm{IQR}/\mathrm{median}) and (1.4826\times\mathrm{MAD}/\mathrm{median}). They derive influence and asymptotic variance results and compare confidence intervals using simulations (PMC full-text §§2–5). The simulation used 10,000 trials across normal, lognormal, exponential, chi-square, and Pareto distributions, with sample sizes 50, 100, 200, 500, and 1,000. Two illustrations use 2002 Health and Retirement Study doctor-visit data (3,066 people in the AHEAD cohort subsample) and Melbourne house prices from January 2016 (source §§5.1–5.2).

## Findings from the source

- In their distribution comparisons, the MAD-based relative spread estimator had smaller or equal relative asymptotic standard deviation than the IQR-based measure; the robust alternatives compared more favorably with the CV for the selected skewed lognormal and Pareto cases. For some Pareto parameter values, the CV’s asymptotic comparison was undefined because the required fourth moment did not exist (source §3.3, Table 3).
- In the reported simulations, the MAD-based asymptotic interval and BCa interval had coverage near the nominal 95% level across the selected distributions, including at (n=50); the IQR-based interval was slightly conservative in those simulations. Conventional CV intervals often fell below nominal coverage for selected skewed distributions (source §5.1, Tables 4–5).
- In the doctor-visit example, a single large female-group observation (750 visits) substantially widened the CV interval; the quantile-based intervals were little changed when the authors removed that observation for an illustrative comparison (source §5.2.1, Tables 6–7).

## Relevance and limits

This paper provides candidate robust relative-dispersion summaries and interval methods for skewed positive data. Its theoretical setup assumes IID observations from a positive distribution, and its simulation results are bounded to the stated families and sample sizes. The examples concern doctor visits and housing prices, not browser timing. These measures also describe relative spread; they do not replace a latency quantile or a confidence interval for that quantile.

**Researcher inference:** If the project needs a scale-adjusted stability statistic, these measures merit consideration alongside IQR/MAD in original units. Their stated IID assumptions would need checking before applying their interval methods to temporally ordered page loads.

## Provenance and metadata note

The PMC full text verifies authors, 2020 online publication date, collection date 2022, journal, volume, issue, pages, DOI, PMCID, and PMID. Zotero contains those bibliographic fields, but its linked HTML attachment is unresolved locally and no PDF is attached. PMC exposes an article PDF link, but no local PDF was retrieved; the note relies on the readable PMC full text.

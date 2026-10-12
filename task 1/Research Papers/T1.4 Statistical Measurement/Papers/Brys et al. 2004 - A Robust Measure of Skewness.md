# A Robust Measure of Skewness

- **Citation:** Brys, G., Hubert, M., & Struyf, A. (2004). A robust measure of skewness. *Journal of Computational and Graphical Statistics, 13*(4), 996–1017. https://doi.org/10.1198/106186004X12632
- **Zotero key:** `ZNCYRKP4`.
- **Source:** Zotero has no attachment. The authors’ 27-page [KU Leuven manuscript](https://wis.kuleuven.be/statdatascience/robust/papers/2004/medcouple.pdf) was read. The PDF identifies itself as a 1 September 2003 manuscript; the journal citation in Zotero is the 2004 publication. Page references below refer to the manuscript PDF.

## Research question and approach

The authors introduce the medcouple (MC), a robust skewness measure for univariate continuous distributions, and compare it with octile skewness (OS) and quartile skewness (QS). The paper derives robustness properties, provides an (O(n\log n)) algorithm, and studies finite-sample behavior through simulated distributions and real data (PDF pp. 1–2, 10–13, 15–20).

## Findings from the source

- The paper proves a 25% breakdown value and bounded influence function for the medcouple. It also describes location and positive-scale invariance and zero value for symmetric distributions (PDF pp. 1, 4, 8–9).
- For finite-sample variance comparisons under standard Gaussian and (G_{0.5}) distributions, the study draws 10,000 samples for each sample size from 10 to 200. The authors report that the finite-sample variances converge fairly well to their asymptotic values (PDF pp. 9–10).
- In simulations of right-skewed (g)-distributions, 1,000 samples at sizes 50, 100, 500, and 1,000 are used to compare how often each measure is positive. OS detects small positive skewness most often, followed by MC, then QS (PDF pp. 13–14).
- The authors’ discussion concludes that all three measures perform well for symmetric uncontaminated distributions; OS detects small positive skewness most effectively; QS is most insensitive to outliers, followed by MC; and OS shows excessive bias when contamination exceeds 12.5% in their study (PDF pp. 19–20).

## Relevance and limits

This source supplies a robust alternative to moment-based skewness for univariate continuous data and reports its finite-sample and contamination behavior against two quantile-based skewness measures. The numerical comparisons are bounded to the distributions, sample sizes, and contamination setups studied in the manuscript. The paper’s simulation and real-data examples do not validate the medcouple for page-load traces or dependent time series.

**Researcher inference:** If skewness of a browser measurement distribution is substantively useful, the medcouple offers a robust candidate alongside conventional skewness. Its behavior would still need to be checked on the project’s metric, sample size, ties, and dependence structure.

## Provenance and metadata note

The Zotero record supplies the journal citation and DOI but no PDF. The KU Leuven-hosted preprint carries a September 2003 manuscript date; the final journal record is 2004, volume 13(4), pages 996–1017. Findings above are read from the manuscript and retain its stated study conditions.

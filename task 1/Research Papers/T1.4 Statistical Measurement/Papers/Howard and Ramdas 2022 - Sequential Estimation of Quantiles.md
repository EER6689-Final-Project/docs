# Sequential estimation of quantiles with applications to A/B testing and best-arm identification

- **Citation:** Howard, S. R., & Ramdas, A. (2022). Sequential estimation of quantiles with applications to A/B testing and best-arm identification. *Bernoulli, 28*(3), 1704–1728. https://doi.org/10.3150/21-BEJ1388
- **Zotero key:** `GANI6MKK`.
- **Source:** Zotero-attached 25-page PDF, preserved as [Howard and Ramdas 2022 - Sequential Estimation of Quantiles.pdf](Howard%20and%20Ramdas%202022%20-%20Sequential%20Estimation%20of%20Quantiles.pdf). Page references below use the PDF’s printed journal pagination where shown.

## Research question and approach

The authors construct confidence sequences for quantiles from a stream of IID observations on a complete, fully ordered set. They provide intervals for tracking one fixed quantile and for tracking all quantiles simultaneously, along with a time-uniform concentration inequality for the empirical distribution function. They also derive QLUCB, a procedure for choosing an approximately best quantile arm in a multi-armed bandit setting (PDF pp. 1704–1706).

## Findings from the source

- The quantile intervals shrink at the paper’s stated (t^{-1/2}sqrt{\log\log t}) order, up to constants, while maintaining nonasymptotic coverage uniformly over time under the IID condition (PDF pp. 1704–1706).
- The empirical-distribution bound extends the Dvoretzky–Kiefer–Wolfowitz inequality to uniform-in-time use. The paper also provides a sample-complexity result for approximate best-quantile arm selection (PDF pp. 1704–1706, 1715–1720).
- In the authors’ simulations, QLUCB uses five to fifty times fewer samples than the comparison methods reported in the abstract (PDF p. 1704; simulation results in the paper).

## Relevance and limits

This is direct methodological evidence for sequential quantile estimation, including tail quantiles, when observations are IID and the outcome space is fully ordered. The guarantees should not be transferred to dependent page-load observations or a drifting website workload without satisfying or adapting the assumptions. Its bandit example concerns selection among arms, not a browser profiling study.

**Researcher inference:** A quantile-based page-load estimand could be paired with time-uniform uncertainty only after the unit of observation, dependence structure, and stationarity conditions are made explicit. The paper supplies candidate statistical machinery, not validation of a particular browser measurement protocol.

## Provenance and metadata note

The Zotero PDF is the attached journal article (25 pages); its citation agrees with Zotero’s *Bernoulli* 28(3), pages 1704–1728, DOI metadata. No second source note is created for this paper in this assignment.

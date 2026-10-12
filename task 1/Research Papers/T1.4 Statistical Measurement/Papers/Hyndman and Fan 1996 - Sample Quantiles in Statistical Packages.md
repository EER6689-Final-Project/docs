# Sample Quantiles in Statistical Packages

- **Citation:** Hyndman, R. J., & Fan, Y. (1996). Sample quantiles in statistical packages. *The American Statistician, 50*(4), 361–365. https://doi.org/10.1080/00031305.1996.10473566
- **Zotero key:** `E2A63QR8`.
- **Source:** Zotero has no attachment. The author-maintained [paper page and errata](https://fpp.robjhyndman.com/publications/quantiles/index.html) and [author-hosted five-page PDF](https://robjhyndman.com/papers/sample_quantiles.pdf) are available. The bibliographic abstract is available in Zotero; the PDF text could not be reliably extracted for this note, so the paper summary is bounded to the abstract and the author’s errata page.

## Research question and approach

The article compares commonly implemented sample-quantile definitions, expressing them in a common notation and examining their motivation and properties. The authors argue for a standard definition across software packages and within a package, and recommend a median-unbiased estimator (the definition now commonly called Hyndman–Fan Type 8). The available abstract does not support a fuller account of the comparison design or all properties considered.

## Findings from the source

- The authors’ abstract says that software packages have used different sample-quantile definitions, sometimes even for different outputs within one package, and recommends the median-unbiased estimator because it has many desirable quantile-estimator properties and is distribution-independent.
- The author-maintained errata page lists corrections to the paper’s property statements and frequency expressions, including corrections dated 8 May 2007, 27 April 2022, and 3 October 2026. It states that the frequency expressions on pp. 362–363 assume distinct observations; with ties, property P3 can fail for every definition (the page gives (x=(1,2,2)), (p=0.5) as an example).

## Relevance and limits

This source establishes that “sample quantile” is not a software-neutral operation unless its interpolation/definition convention is specified. The recommendation is a comparison among definitions in the article; the abstract alone does not show that Type 8 is optimal for every project estimand or software environment. The errata materially qualifies use of the paper’s frequency-property claims, especially when data contain ties.

**Researcher inference:** Any reported browser-performance quantile should identify the software and quantile algorithm, so repeated calculations are reproducible. Choosing a definition for the project requires matching the estimator to the intended interpretation and validating behavior for the sample sizes and ties at hand.

## Provenance and metadata note

The author page links the publication and lists its corrections. The Zotero record identifies the journal, volume, issue, and page range but gives JSTOR DOI `10.2307/2684934`; the author’s citation block gives DOI `10.1080/00031305.1996.10473566`. Both DOI values point to this article. The note cites the author’s current errata, including the 3 October 2026 correction to Definition 3/P3.

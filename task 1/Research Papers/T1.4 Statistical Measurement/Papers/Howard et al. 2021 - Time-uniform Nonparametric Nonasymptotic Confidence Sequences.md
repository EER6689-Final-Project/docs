# Time-uniform, nonparametric, nonasymptotic confidence sequences

- **Citation:** Howard, S. R., Ramdas, A., McAuliffe, J., & Sekhon, J. (2021). Time-uniform, nonparametric, nonasymptotic confidence sequences. *The Annals of Statistics, 49*(2), 1055–1080. https://doi.org/10.1214/20-AOS1991
- **Zotero keys:** `TNLWEEU7` and `NIWWJJIZ` (duplicate records for the same DOI and work).
- **Source:** Zotero PDFs under both records are duplicate copies of the arXiv v9 preprint, dated 6 August 2022; one copy is preserved as [Howard et al. 2021 - Time-uniform Nonparametric Nonasymptotic Confidence Sequences.pdf](Howard%20et%20al.%202021%20-%20Time-uniform%20Nonparametric%20Nonasymptotic%20Confidence%20Sequences.pdf). The paper’s journal citation remains the 2021 *Annals of Statistics* article. Page references below refer to the 48-page Zotero PDF, whose front matter identifies it as arXiv:1810.08240v9 (Aug. 2022).

## Research question and approach

The paper develops confidence sequences: intervals that cover a target uniformly over an unbounded sequence of observation times. It builds time-uniform concentration methods from nonnegative supermartingale bounds, including sub-Gaussian and Bernstein conditions, self-normalized processes, and matrix martingales. Its examples include mean and covariance estimation and a sample-average treatment effect; it is a general sequential-inference paper rather than a quantile-specific method (PDF pp. 1–3).

## Findings from the source

- The stated guarantees are nonasymptotic and uniform over time, for all sample sizes, under the paper’s respective assumptions. The method allows an experimenter to stop at an arbitrary time without invalidating those guarantees (PDF p. 2).
- The paper gives shrinking confidence sequences with width on the order of (t^{-1/2}) up to iterated-logarithm factors in its sub-Gaussian mean example. In one Rademacher illustration, the authors compare pointwise intervals and time-uniform sequences using one 100,000-draw run and 10,000 replications for the miscoverage plot (PDF pp. 2–3).
- The authors state that this flexibility costs interval width: their illustrated discrete-mixture bound stays within a factor of two of fixed-sample asymptotic CLT intervals across five orders of magnitude in time (PDF p. 2, as described by the authors).

## Relevance and limits

This source supports principled inference when a measurement stream is monitored continuously or stopped adaptively. Its guarantees rely on the assumptions attached to each bound; the paper does not establish that repeated page-load observations satisfy those assumptions. It does not itself provide quantile-specific intervals for arbitrary browser latency distributions. Howard and Ramdas’s later quantile paper (Zotero key `GANI6MKK`) is the direct source for sequential quantile estimation.

**Researcher inference:** This paper is useful for motivating time-uniform uncertainty reporting when the stopping time may depend on observed data. Applying its bounds to page-load measurements would require identifying a suitable observation model and verifying the required conditions.

## Provenance and metadata note

Both Zotero records share DOI `10.1214/20-AOS1991` and journal metadata; the PDFs are duplicate copies, so only one is included here. The local PDF is the 48-page arXiv v9 file dated August 2022, not the typeset journal version. The journal record lists 2021; this note uses the PDF’s own version date only to identify the preserved file.

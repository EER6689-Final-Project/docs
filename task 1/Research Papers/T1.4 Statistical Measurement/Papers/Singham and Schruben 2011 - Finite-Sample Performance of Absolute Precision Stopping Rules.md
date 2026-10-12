# Finite-Sample Performance of Absolute Precision Stopping Rules

- **Citation:** Singham, D. I., & Schruben, L. W. (2011; issue publication 2012). Finite-sample performance of absolute precision stopping rules. *INFORMS Journal on Computing, 24*(4), 624–635. https://doi.org/10.1287/ijoc.1110.0471
- **Zotero key:** `XX924A92`.
- **Source:** Zotero stores the publisher’s HTML record only; the publisher page and abstract are available at [INFORMS PubsOnline](https://pubsonline.informs.org/doi/10.1287/ijoc.1110.0471). This note is bounded to that record and abstract; the full article PDF was not read.

## Research question and approach

The article examines finite-sample coverage when sequential simulation experiments stop after an interval reaches a specified absolute precision. The authors introduce coverage contours to describe the trade-offs among interval coverage, stopping time, and precision. For independent, identically distributed normal simulation data, they report an analytic calculation of these contours. The available publisher abstract does not state the study’s other model conditions, simulation design, or numerical sample sizes.

## Findings from the source

- The publisher abstract reports that a basic absolute-precision stopping rule can bias coverage even when its supporting assumptions hold.
- The authors define optimal stopping rules that achieve nominal coverage with the smallest expected number of observations. In their finite-sample analysis, increasing the confidence coefficient used by the stopping rule can achieve nominal coverage; this differs from an asymptotic result that would reduce the precision of the rule.
- Under the stated IID normal model, the authors report an analytically determined rule that is insensitive to data variance and provides at least nominal coverage at any precision value.

## Relevance and limits

This source directly cautions that repeatedly sampling until a nominal precision target is met does not by itself guarantee nominal interval coverage. The result is about sequential simulation confidence intervals and an IID normal analytic case; the abstract does not establish performance for skewed, dependent, drifting, or web-page load observations. It also does not provide enough accessible detail here to assess the proposed rule’s implementation or empirical operating characteristics.

**Researcher inference:** A measurement protocol that stops on observed precision should specify its stopping rule and justify coverage under the data-generating conditions. Whether these rules suit repeated browser measurements remains an open transfer question.

## Provenance and metadata note

Zotero’s record omits creators, date, DOI, and page range. The INFORMS publisher page identifies Singham and Schruben, gives the DOI, and reports online publication on 25 August 2011; it cites the issue as *INFORMS Journal on Computing* 24(4), 624–635, in Fall 2012. The note uses the online year and explicitly records the issue year distinction. The local Zotero child is HTML, not a PDF.

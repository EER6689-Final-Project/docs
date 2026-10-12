# A new biometrical procedure for testing the equality of measurements from two different analytical methods

- **Citation:** Passing, H., & Bablok, W. (1983). A new biometrical procedure for testing the equality of measurements from two different analytical methods: Application of linear regression procedures for method comparison studies in clinical chemistry, Part I. *Journal of Clinical Chemistry and Clinical Biochemistry, 21*(11), 709–720. https://doi.org/10.1515/cclm.1983.21.11.709
- **Zotero key:** `8FNYPXJD`
- **Source:** [Passing & Bablok 1983.pdf](Passing%20%26%20Bablok%201983.pdf), 12-page source PDF attached in Zotero (Zotero attachment key `8B3ZGT7J`).

## Research problem and contribution

The authors address method-comparison settings where both methods have measurement error and standard regression assumptions may be implausible. They propose a regression procedure intended to avoid special distributional assumptions about sample values and measurement errors and to be invariant to which method is assigned to X or Y. The method tests linearity, estimates slope and intercept, and uses confidence limits to assess departures from slope 1 and intercept 0.

## Methods and evidence

The article describes method comparisons for analytical chemistry measurements, with concentration values measured on paired samples. It uses rank-based pairwise slopes and a median-based estimate, with a cusum test for linearity and confidence limits for slope and intercept. Its simulation appendix varies sample size from 40 to 90, concentration range, coefficients of variation, and error distributions; 500 datasets are generated per parameter/distribution setting. The reported simulation result says the slope estimator is unbiased under the null in the studied settings when coefficients of variation are below 7%. The paper also gives clinical-chemistry examples.

## Relevance to profiler validation

This is a candidate errors-in-variables method for checking proportional and constant departures between two profilers when both produce noisy measurements. It can assess a linear relationship and whether it is consistent with the identity line; it does not itself quantify the distribution or practical size of individual differences.

## Limitations and evidence boundary

The authors' simulation findings are conditional on their specified designs and do not establish performance for browser metrics, larger variability, or arbitrary data-generating processes. The paper explicitly cautions that regression comparison alone cannot compare all method properties and that accuracy, imprecision, sensitivity, specificity, and usable range require additional experiments and statistics. The abstract's broad “no special assumptions” wording should not be read as assumption-free: the article states assumptions about a linear structural relationship, continuous sampling values, and proportional error variances.

## Zotero metadata check

Zotero's creator metadata records “Passing, H.; Bablok, null.” The attached paper identifies the authors as H. Passing and W. Bablok. The corrected citation above follows the PDF; the Zotero creator field needs verification/correction.

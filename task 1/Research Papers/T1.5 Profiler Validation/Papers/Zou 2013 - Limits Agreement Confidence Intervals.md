# Confidence interval estimation for the Bland-Altman limits of agreement with multiple observations per individual

- **Citation:** Zou, G. Y. (2013). Confidence interval estimation for the Bland–Altman limits of agreement with multiple observations per individual. *Statistical Methods in Medical Research, 22*(6), 630–642. https://doi.org/10.1177/0962280211402548
- **Zotero key:** `7CBVI4EG`
- **Source available in Zotero:** PubMed record only; no paper PDF attached. This note is based on the Zotero bibliographic record and abstract.

## Scope and contribution

Zou develops confidence-interval procedures for limits of agreement when each individual has multiple measurements. The abstract distinguishes cases where the underlying true value is assumed to change from cases where it is assumed stable. It says a fixed number of replicates per individual is not required, and that the procedures use standard-normal and chi-square quantiles. The abstract reports worked examples, simulation results described as performing well, and a publisher-hosted SAS macro.

## Relevance to profiler validation

This source addresses uncertainty in agreement limits under repeated measurements. It is relevant where a page/environment is measured repeatedly and the target estimand depends on whether the underlying performance value is treated as stable or changing across runs.

## Evidence boundary and limitations

The available abstract does not specify simulation scenarios, sample sizes, missingness patterns, empirical example details, or numerical coverage results. “Perform well” is therefore the authors' abstract-level characterization, not independently assessed evidence for this project. The model choice between stable and changing underlying values must be justified for the profiler protocol, and the method has not been evaluated here on browser measurements.

## Project use

Consider for confidence intervals around limits of agreement after checking the paper's assumptions and simulation conditions against the planned repeated-run design.

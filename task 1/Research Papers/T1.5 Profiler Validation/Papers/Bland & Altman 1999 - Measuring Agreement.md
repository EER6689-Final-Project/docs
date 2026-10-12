# Measuring agreement in method comparison studies

- **Citation:** Bland, J. M., & Altman, D. G. (1999). Measuring agreement in method comparison studies. *Statistical Methods in Medical Research, 8*(2), 135–160. https://doi.org/10.1177/096228029900800204
- **Zotero key:** `X4BEQVFF`
- **Source available in Zotero:** PubMed record only; no paper PDF attached. This note is based on the Zotero bibliographic record and abstract.

## Scope and contribution

This methodological article describes agreement analysis for paired measurements from two methods. Its abstract presents the mean difference and 95% limits of agreement (mean difference ± 1.96 SD of paired differences) and discusses graphical checks, confidence intervals, proportional differences, repeatability, replicated measurements, and a nonparametric method.

## Relevance to profiler validation

The paper supports analyzing paired differences in the measurement units that matter instead of treating correlation as agreement. It also flags that a simple constant-difference limits-of-agreement model may not suit data where differences vary with magnitude, and that replicate runs need a method appropriate to their dependence structure.

## Evidence boundary and limitations

The available abstract does not report a study sample, empirical dataset, implementation details, or numerical performance results; this is a methods paper, not direct evidence that any browser profiler is valid. The classical limits described rely on the distribution and variance assumptions being checked for the target data. Consult the full article before relying on particular formulae for replicated or magnitude-dependent measurements.

## Project use

Use as a foundational rationale for paired-difference agreement analysis. For repeated browser runs, pair it with replicate-specific methods such as Carstensen et al. (2008) and Zou (2013), whose own details are summarized in separate notes.

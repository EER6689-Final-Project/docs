# NIST Dataplot — ROC Curve Reference

- **Citation:** National Institute of Standards and Technology, Statistical Engineering Division. “ROC CURVE.” [Dataplot reference manual](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/roccurve.htm).
- **Zotero key:** `N5YHCXI3` (webpage; saved HTML attachment `roccurve.html`).
- **Source access:** NIST reference page and Zotero snapshot checked 13 October 2026.

## Outline Summary

- **Scope:** The Dataplot command plots sensitivity against false-positive rate across test thresholds, with examples for multiple settings of one instrument or multiple instruments. The page says upper-left points indicate high accuracy and that the no-discrimination line runs from (0,0) to (1,1).
- **AUC caveat:** The page warns that area under the curve is meaningful for different settings of the same instrument; comparisons across multiple vendors/instruments need separate interpretation.
- **Project relevance:** If controlled defects are used to test whether a profiler detects known differences, threshold/sensitivity analysis may describe detection behavior. It does not test measurement agreement in the Bland–Altman sense.
- **Limit:** This is software-method documentation, not an evaluation of browser profiling tools or a validation design for continuous performance measurements.

## T1.5 Evidence Check

- **Source-supported:** ROC variables, operating-point interpretation, and the stated AUC caveat.
- **Researcher inference:** Use only for a clearly defined defect-detection classification task, not as a replacement for agreement analysis.

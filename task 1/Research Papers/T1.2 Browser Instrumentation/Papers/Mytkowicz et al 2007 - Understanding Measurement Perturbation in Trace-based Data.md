# Understanding Measurement Perturbation in Trace-based Data

- **Citation:** Mytkowicz, T., Diwan, A., Hauswirth, M., & Sweeney, P. F. (2007). “Understanding Measurement Perturbation in Trace-based Data.” *IEEE International Parallel and Distributed Processing Symposium (IPDPS)*, 1–6. https://doi.org/10.1109/IPDPS.2007.370515
- **Zotero key:** `EVB9FDNG`.
- **Source:** Zotero-attached full PDF; page references below refer to the paper's printed pages.

## Abstract and scope

This paper examines whether trace instrumentation changes the relationships among measured program signals, and whether the amount of added instrumentation predicts the resulting measurement distortion. The evidence is from native software workloads and hardware-counter traces, not browser instrumentation.

## Outline Summary

- **Central idea**
  - Small added instruction counts do not guarantee that the relationships observed among trace signals remain stable.
- **Research problem and objectives**
  - Assess measurement perturbation in trace-based data and examine whether added instrumentation cost predicts it.
  - The supplied source review does not establish formally enumerated research questions.
- **Approach and experimental setup**
  - Compare instrumented traces with a hardware-counter-only baseline treated as minimally perturbing.
  - Instrumentation used CIL, PAPI hardware counters, global increments for software events, and Linux `setitimer` sampling at 10–200 ms.
  - The evaluation covered approximately 700 traces from bzip, mcf, sjeng, and sim-outorder, with approximately 3,000 records per trace.
- **Metrics, algorithms and results**
  - Compared added instructions and Spearman correlations between hardware metric pairs in baseline and instrumented runs.
  - Used dynamic time warping to align traces before comparing correlations between signal time series.
  - Sjeng's L1D/L2 miss correlation fell from about 0.8 to below 0.5 with about 2.25% extra instructions. Sim-outorder's branch-misprediction outer correlation fell from above 0.9 to 0.3 with about 0.2% extra instructions. Bzip remained stable at 2.5%; adding software metrics sometimes reduced perturbation (pp. 2, 4–6).
- **Limitations**
  - Four native workloads and a hardware-metric correlation proxy limit generalization. The minimally perturbing baseline is an assumption. Other relationships, including software/software and software/hardware signals, may also be affected. The study does not establish a universal reliable metric subset or threshold (pp. 2, 4–6).
- **Author-stated future work**
  - Not established by the reviewed evidence.
- **Relationship to the T1.2 instrumentation review**
  - Provides a general observer-effect precedent and motivates checking signal relationships as well as added cost. It does not set browser-specific thresholds, establish Chromium-specific effects, or select a profiler design.
- **Important page references**
  - Perturbation setup and baseline: pp. 2, 4–6. No direct quotations are included because exact wording has not been checked against the PDF.
- **Concise takeaway**
  - Added instruction overhead alone is not sufficient evidence that trace measurements remain valid.

## T1.2 Claim Check

- **Preliminary inference:** Browser instrumentation should be evaluated with workload-specific validity checks that examine relationships among signals alongside added cost. This is a transfer question for later work, not a browser result or selected methodology.

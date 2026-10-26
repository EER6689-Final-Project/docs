# Curtsinger and Berger 2013 - STABILIZER Statistically Sound Performance Evaluation

- **Citation:** Curtsinger, C., & Berger, E. D. (2013). “STABILIZER: Statistically Sound Performance Evaluation.” *ASPLOS ’13*, 219–228. https://doi.org/10.1145/2451116.2451141
- **Zotero key:** 5NNCRU98.
- **Source:** Full-text PDF attached in Zotero as 5PBKK4PN; extracted text reviewed. PDF pp. 5–6 have no extractable text layer; details found only there need visual verification.

## Abstract and scope

STABILIZER is a compiler transformation and runtime system intended to reduce layout-related bias in native program performance comparisons. It randomizes code, stack, and heap placement so repeated runs sample different layouts. The authors evaluate it on SPEC CPU2006 and use the resulting distributions to assess LLVM optimization levels. It is not a study of Chrome, CDP, or browser instrumentation.

## Outline Summary

- **Central idea:** Repeated runs of one binary do not necessarily sample different layouts. STABILIZER re-randomizes layout to account for layout effects.
- **Problem and objectives:** Code, stack, and heap placement can affect caches and branch predictors. The authors aim to control this variation and enable statistically interpretable comparisons.
- **Research question:** Paraphrase: can runtime layout randomization improve execution-time distributions and support sound comparisons of program changes?
- **Approach and setup:** An LLVM transformation/runtime randomizes function placement, stack-frame spacing, and heap layout. Re-randomization defaults to 500 ms. Evaluation used 18 SPEC CPU2006 benchmarks and 30 runs per configuration; some C++ benchmarks were excluded due to unsupported exception handling, and some Fortran benchmarks failed to build.
- **Metrics and analysis:** Execution-time distributions, normality, overhead, and optimization effects; pairwise comparisons and suite-level ANOVA.
- **Key results:** Four of five previously non-normal benchmark distributions became normally distributed; cactusADM remained non-normal and hmmer was anomalous. Median overhead was 6.7%; four workloads exceeded 30%, none exceeded 40%. Pairwise tests found significant differences for 17/18 benchmarks for -O2/-O1 and 9/18 for -O3/-O2. Suite-level ANOVA found -O2 significant at 90%, not 95% (p=.0898), and -O3/-O2 not significant (p=.264). The suite-level result does not imply no individual benchmark effects.
- **Limitations:** Native SPEC CPU2006 and older toolchain; workload/language exclusions limit generalization. No direct estimate of CDP/browser-profiler overhead. Results do not establish that its method or assumptions apply to browser workloads.
- **Author-stated future work:** Section 8 proposes finer-grained basic-block randomization and use of performance counters to identify layout-related performance problems (PDF p. 9).
- **Relationship to T1.2:** Methodological precedent for repeated runs, distribution checks, and separating workload-level from suite-level inference. Whether similar controls isolate browser instrumentation effects remains untested.
- **Important source references:** PDF pp. 1–4, §§1–3 (motivation/system); p. 7, §5 (distribution/overhead); p. 8, §6 (optimization/ANOVA); p. 9, §8 (future work). No verbatim quotation used. Check pp. 5–6 visually before relying on details located only there.
- **Concise takeaway:** STABILIZER demonstrates a native-code method for sampling layout variation and analyzing repeated results. Its overhead and findings cannot be transferred to Chromium instrumentation.

## T1.2 Evidence Check

- **Empirical claims:** Benchmark counts, overhead, and optimization results are author-reported in the cited sections.
- **Preliminary inference:** Repeated runs and workload-specific distributions are useful design considerations for later browser experiments; this paper does not prescribe a browser profiler or establish its cost.

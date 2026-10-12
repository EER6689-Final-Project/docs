# Producing Wrong Data Without Doing Anything Obviously Wrong!

- **Citation:** Mytkowicz, T., Diwan, A., Hauswirth, M., & Sweeney, P. F. (2009). “Producing Wrong Data Without Doing Anything Obviously Wrong!” In *Proceedings of the 14th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS XIV)*, 265–276. https://doi.org/10.1145/1508244.1508275
- **Zotero key:** `IWCIN2C5`.
- **Source:** Zotero-attached full PDF; page references below refer to the PDF's printed pages.

## Abstract and scope

The paper studies measurement bias caused by seemingly incidental choices in experimental setup. Its experiments vary UNIX environment size and link order, which affect memory layout, while comparing compiler optimization levels on SPEC CPU2006 C programs. It reports effects across older native systems and one simulator. It does not study browsers or instrumentation overhead directly.

## Outline Summary

- **Central idea:** A performance comparison can be precise and repeatable within one setup yet misleading because the setup itself interacts with the systems being compared.
- **Research problem and objectives:** Examine whether UNIX environment size and executable link order change reported optimization speedups, and use causal analysis and setup randomization to investigate and reduce bias. The questions are a summary of the experiments, not quoted formal research questions.
- **Approach and experimental setup:** Compare GCC O3 and O2 on 12 single-threaded SPEC CPU2006 CINT/CFP benchmarks using train inputs. The authors report 5,940 runs per benchmark across the setup variations, on Pentium 4 and Core 2 Linux systems and an m5 O3CPU simulator; selected comparisons also use Intel's C compiler. Some analyses use smaller targeted repetition counts, including five runs for the micro-kernel and three runs for each of 484 perlbench setup combinations. PAPI measurements are collected through an `LD_PRELOAD` interposer.
- **Metrics, methods and results:** The principal outcome is execution time and the O2/O3 speedup ratio, with selected hardware performance counters used to investigate mechanisms. Changing environment size or link order can shift speedups and can reverse a comparison; these effects are reported across the tested processors, compilers, and most benchmarks. Fixing stack placement is used as a causal probe for one proposed mechanism, but the authors do not confirm every low-level explanation on physical hardware. Setup randomization samples multiple configurations and compares resulting distributions; causal analysis intervenes on a proposed cause to check whether the outcome changes as predicted (pp. 3–12).
- **Limitations:** The study varies two setup dimensions on older hardware, operating systems, compilers, and workloads. Its findings establish that such bias occurred in these tested conditions, not its magnitude in current browsers. Some proposed hardware-level mechanisms remain unconfirmed. Randomization cannot cover setup factors that were not varied, and causal probes provide evidence rather than proof (pp. 3–12).
- **Author-stated future work:** Not established from the reviewed paper.
- **Relationship to the T1.2 instrumentation review:** This is empirical evidence that nuisance setup variables can distort systems comparisons. It motivates recording and controlling browser launch environment, binary/build, runtime configuration, and run order, while leaving the size and presence of analogous Chromium effects to be tested.
- **Important page references:** Experimental design and platform details: pp. 3–4. Results and analysis: pp. 5–8. Randomization and causal analysis: pp. 9–12. No direct quotation is included because exact wording has not been verified against the page image.
- **Concise takeaway:** Repeated runs under one fixed setup do not rule out setup-induced bias; the paper's remedy is to vary relevant setup factors and probe proposed causes.

## T1.2 Claim Check

- **Source-reported result:** Link order and UNIX environment size affected speedup comparisons in the evaluated compiler, benchmark, and platform settings.
- **Preliminary inference:** A browser instrumentation study could record and, where justified, vary launch environment, build/layout, browser configuration, and run order. This is a transfer question, not a claim that these factors have already been shown to bias Chromium measurements.
- **Phase 0 scope:** This note records a methods precedent; it does not choose a browser experiment, nuisance-factor set, statistical test, or thesis gap.

# Curtsinger and Berger 2013 - STABILIZER: Statistically Sound Performance Evaluation

- **Citation:** Charlie Curtsinger and Emery D. Berger. “STABILIZER: Statistically Sound Performance Evaluation.” In *Proceedings of the 18th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS ’13)*, 219–228. ACM, 2013. https://doi.org/10.1145/2451116.2451141.
- **Zotero key:** `3HI3DY8W`. This is the same work as T1.2 record `5NNCRU98`; see its existing matrix row rather than adding a duplicate row.
- **Provenance:** Zotero identifies the ASPLOS ’13 conference paper and provides one attached PDF. The paper is about runtime and compiler layout effects in native program benchmarking.
- **Source access:** Read the attached PDF through `zotero_get_item_fulltext` and method/results sections with `zotero_read_pdf_pages`. The extraction is page-limited; conclusions below are bounded to the paper’s abstract and readable extracted sections.

## Abstract and scope

The authors argue that repeated runs of one binary do not sample code, stack, and heap layouts, even though modern processors can be sensitive to those layouts. STABILIZER repeatedly re-randomizes layouts at runtime to sample that source of variability and support statistical tests.

## Outline Summary

- **Approach:** STABILIZER modifies execution to repeatedly randomize code, stack, and heap object locations, with the goal of sampling memory configurations and making layout effects approximately Gaussian so techniques such as ANOVA can be used. The evaluation measures its overhead and uses it to compare LLVM optimization levels on SPEC CPU2006 (abstract and evaluation sections).
- **Sample and conditions:** The performance experiment covers SPEC CPU2006 workloads and the authors’ LLVM/compiler/runtime setup. Results concern native program layout variation on the tested x86 systems, not browser runtime layout or page loads.
- **Results:** The paper reports median overhead below 7%. With layout randomization, -O2 is significantly faster than -O1, while the measured difference between -O3 and -O2 is indistinguishable from random noise in the tested suite and setup (abstract).
- **Limitations:** STABILIZER is a specialized tool and its conclusions depend on its randomization model, supported binary/runtime assumptions, and benchmark suite. It does not show that layout randomization is practical or appropriate for general browser performance measurement.
- **Author-stated caveats:** A single binary is only one sample of the program-layout space, irrespective of run count; this is the motivation for randomization. Results are presented for the implementation and workload set evaluated, rather than as a universal overhead or optimization ranking.
- **Relationship to T1.4:** Reinforces the distinction between repeated execution of a fixed artifact and repetition that samples a relevant source of variation. The project can use this distinction when deciding whether browser/process/build variants belong in its measurement design.
- **Concise takeaway:** More runs of one fixed configuration do not cover variation that only changes across configurations or layouts.

## T1.4 Evidence Check

- **Paper-supported:** STABILIZER’s layout re-randomization mechanism, measured overhead, and SPEC CPU2006 optimization comparison are stated in the paper.
- **Not established:** That the project’s browser performance differences are caused by layout variation or that STABILIZER-like randomization would improve browser measurement.
- **Researcher inference:** Identify whether the project’s target estimand includes variation across process/build/layout configurations; if it does, collect those as explicit experimental levels rather than assuming repeated loads sample them.

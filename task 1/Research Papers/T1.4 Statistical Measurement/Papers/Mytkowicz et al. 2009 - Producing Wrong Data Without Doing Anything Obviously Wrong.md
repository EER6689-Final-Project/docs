# Mytkowicz et al. 2009 - Producing Wrong Data Without Doing Anything Obviously Wrong

- **Citation:** Todd Mytkowicz, Amer Diwan, Matthias Hauswirth, and Peter F. Sweeney. “Producing Wrong Data Without Doing Anything Obviously Wrong!” In *Proceedings of the 14th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS ’09)*, 265–276. ACM SIGPLAN Notices 44, no. 3 (2009). https://doi.org/10.1145/1508244.1508275.
- **Cross-reference:** This is the same work as T1.2 Zotero record `IWCIN2C5`; see its existing matrix row rather than creating a duplicate matrix entry.
- **Zotero key:** `2TY5A3XC`.
- **Provenance:** Zotero catalogs the record as a journal article in *ACM SIGPLAN Notices* 44(3), while the attached PDF identifies the ASPLOS ’09 conference and same title/authors. I cite both the conference and series details shown in the available metadata/source. No newer version was identified in this item.
- **Source access:** Read the Zotero PDF through `zotero_get_item_fulltext` and the final pages with `zotero_read_pdf_pages`. The extracted text exposes the experimental procedures and discussion, but some table/figure text is garbled; numeric claims below rely on explicit prose or legible text.

## Abstract and scope

The paper demonstrates that apparently innocuous setup choices can bias systems measurements enough to overstate or reverse conclusions. It studies two mechanisms—UNIX environment size and link order—and proposes setup randomization to expose layout-related variation and causal analysis to check conclusions.

## Outline Summary

- **Approach:** The authors vary experimental setup factors while comparing compiler optimization results for SPEC CPU2006 programs. The study includes Pentium 4, Core 2, and simulated m5 O3CPU configurations, and gcc and Intel compilers. They examine how environment size can shift stack placement and how link order changes memory layout; the paper also reviews 133 papers from ASPLOS, PACT, PLDI, and CGO (Sections 3–6).
- **Results:** The authors report that these setup changes can materially affect reported speedups and lead to incorrect conclusions across the architectures, compilers, and most of the SPEC CPU2006 C programs they tested. Their examples include an apparent O3 benefit that disappeared when an intervention fixed stack placement. They propose randomizing setups and using causal interventions to test whether a proposed cause produces the expected effect (Sections 4 and 7).
- **Limitations:** The experiments examine specific setup factors and a finite set of older processors, compiler versions, and SPEC CPU2006 C workloads. They do not quantify all possible sources of measurement bias or establish prevalence across current browser workloads. The paper explicitly says setup randomization may fail to cover the full space of setups and causal analysis increases confidence without guaranteeing correctness (Section 7).
- **Author-stated caveats:** Diverse benchmarks and careful statistics may factor out some bias, but benchmark suites themselves can be unrepresentative; neither of the proposed techniques is perfect. The authors call for systems and hardware support to make these methods easier to use (Sections 6–8).
- **Relationship to T1.4:** Supports treating environment/setup variation as a possible measurement bias and varying or controlling setup factors when checking performance conclusions. It does not directly validate repeated browser measurements, browser timing APIs, or any particular sample-size rule.
- **Concise takeaway:** A repeatable timing procedure can still yield a biased comparison if setup changes performance; test causal explanations and sample setup variation explicitly.

## T1.4 Evidence Check

- **Paper-supported:** The specific tested setup factors, processor/compiler families, benchmark suite, and the authors’ methods for detecting and avoiding bias are reported in the paper.
- **Not established:** That the same bias magnitude occurs in modern browsers or the project’s target field measurements.
- **Researcher inference:** For a browser study, record and deliberately vary plausible setup factors (such as process state and page/environment configuration) before interpreting small effects; select factors from the actual measurement system rather than copying this paper’s setup list.

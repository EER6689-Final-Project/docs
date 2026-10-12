# Bulej et al. 2020 - Duet Benchmarking: Improving Measurement Accuracy in the Cloud

- **Citation:** Lubomír Bulej, Vojtěch Horký, Petr Tůma, François Farquet, and Aleksandar Prokopec. “Duet Benchmarking: Improving Measurement Accuracy in the Cloud.” In *Proceedings of the 2020 ACM/SPEC International Conference on Performance Engineering (ICPE ’20)*, 2020, 8 pp. https://doi.org/10.1145/3358960.3379132.
- **Zotero keys:** `B39WMA9T` and `YEM9ZMRR` (duplicate metadata records for this source; one note and one PDF retained).
- **Provenance:** Both Zotero records have the same title, authors, venue, DOI, abstract, and independently attached copies of the paper. The citation and PDF front matter identify the ICPE ’20 proceedings paper.
- **Source access:** Read the attached PDF with `zotero_get_item_fulltext`, then inspected experimental setup, research questions, and conclusion passages. The authors refer readers to an online appendix for detailed environment information.

## Abstract and scope

The paper evaluates “duet” performance comparisons, in which two versions/workloads run concurrently and their relative execution times are compared. The design aims to cancel synchronized interference on shared machines, especially cloud VMs. This is a performance-regression benchmarking method, not a browser measurement study.

## Outline Summary

- **Approach and sample:** The authors compare duet with standard independent/interleaved measurement and use A/A experiments plus 99% confidence-interval widths to assess accuracy. Environments include Amazon EC2 instance types t3.medium, t3a.medium, m5.large, and m5a.large; Travis CI on unspecified Google Compute Engine instances; GitLab CI on DigitalOcean instances; a Proxmox private cloud; and bare metal. Workloads include 23 SPEC CPU 2017 rate workloads and 20 ScalaBench/DaCapo workloads that ran successfully. Java tests use OpenJDK 1.8.0 with fixed heap and disabled GC ergonomics. Detailed platform/run information is deferred to the cited online appendix (Section 4).
- **Results:** In their tested configurations, duet narrows confidence intervals relative to the standard method by 2.3×–12.5× (5.03× average) for ScalaBench/DaCapo and 23.8×–82.4× (37.4× average) for SPEC CPU 2017. The experiments attribute the improvement to synchronized interference under shared resources. Uneven resource use when paired workloads differ in duration can bias the estimated execution-time ratio (Sections 4.1–4.4).
- **Limitations:** Findings are bounded to the listed cloud/CI platforms and benchmark workloads. Travis CI’s underlying instance type is unspecified in the paper. The paper frames cloud use as viable for detecting regression changes; it does not establish that duet yields unbiased absolute timing or applies to browser page-load comparisons. The conclusion leaves its effectiveness in CI/CD without dedicated instances as future work.
- **Author-stated caveats:** Duet depends on platform/workload properties that cloud users cannot fully control. Accuracy improvements are associated with shared-resource synchronized interference; uneven utilization can underestimate execution-time ratios, and detection of a change may be separated from estimating its magnitude in a controlled environment (Sections 1, 4.3–4.4, 6).
- **Relationship to T1.4:** Relevant as evidence that paired measurements can reduce shared-host noise under tested performance-regression conditions. It does not justify paired browser runs unless the project tests the assumption that both runs experience comparable synchronized interference.
- **Concise takeaway:** Pairing can improve comparison precision on shared hosts in the tested benchmark settings, but the result depends on the interference and resource-sharing conditions.

## T1.4 Evidence Check

- **Paper-supported:** The listed environments, workloads, 99% interval comparison, reported accuracy ranges, synchronized-interference explanation, and workload-duration caveat are described in the paper.
- **Not established:** Equivalent gains for browser pages, page-load metrics, or a different cloud host.
- **Researcher inference:** Treat paired browser runs as a candidate design only after an A/A check on the intended host and workload demonstrates lower uncertainty without meaningful ratio bias.

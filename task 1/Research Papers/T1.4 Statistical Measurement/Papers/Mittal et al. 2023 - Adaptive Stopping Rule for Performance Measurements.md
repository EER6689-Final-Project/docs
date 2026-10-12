# Adaptive Stopping Rule for Performance Measurements

- **Citation:** Mittal, V., Bruel, P., Milojicic, D., & Frachtenberg, E. (2023). Adaptive stopping rule for performance measurements. In *Proceedings of the SC ’23 Workshops: Performance Modeling, Benchmarking and Simulation of High Performance Computer Systems (PMBS ’23)* (pp. 1288–1297). ACM. https://doi.org/10.1145/3624062.3624202
- **Zotero key:** `SKLNC8DZ`.
- **Source:** Zotero contains the SC23 workshop metadata page only. The authors’ 10-page PDF is available at [Frachtenberg’s publication page](https://frachtenberg.org/eitan/pubs/papers/mittal23:adaptive.pdf) and was read for this note; PDF page references refer to that author-hosted copy.

## Research question and approach

The paper asks how to decide when enough performance samples have been collected when the distribution is not known in advance. The proposed meta-heuristic learns from the stream, classifies its distribution using a decision tree, and selects a distribution-specific stopping criterion. To evaluate distribution fidelity, the authors use 1,000 runs of each benchmark as an empirical reference distribution, determine a minimum sample size under a distance threshold, and compare the stopping heuristic’s sample distribution with that reference (PDF pp. 1–3).

## Findings from the source

- On synthetic distributions, the prototype closely matches the reference distribution and stops near the authors’ desired distance threshold (PDF pp. 1, 4–7).
- For actual benchmarks, results are mixed: the heuristic is too conservative for some applications and too lax for others, especially GPU applications, although it generally captures the overall distribution shape (PDF pp. 1, 8–9).
- The authors identify limitations in the simple classifier, the size and breadth of the tested application set, and the computational cost of repeatedly fitting models to the full sample set. They propose more training data and more capable models as future work (PDF pp. 8–9).

## Relevance and limits

This is directly about adaptive stopping for performance measurement and explicitly treats the observed distribution as the target. Its evaluation is a prototype using synthetic distributions and a set of single-node Rodinia CPU/GPU benchmarks; the authors say it did not test networked, large-scale HPC workloads (PDF pp. 5–9). It does not establish accuracy for browser page-load metrics, and its heuristic’s mixed results on real benchmarks limit any claim that adaptive stopping is uniformly efficient or accurate.

**Researcher inference:** The work supports considering distribution-level stopping criteria when a point estimate could hide meaningful variation. A browser-focused implementation would need separate validation with the target metrics and workload, especially because the paper reports both over- and under-sampling on actual benchmarks.

## Provenance and metadata note

The Zotero webpage record has no creators or publication fields beyond title and URL. The author-hosted PDF identifies the four authors, PMBS ’23, 13 November 2023, DOI `10.1145/3624062.3624202`, and a 10-page conference version. Its experimental evaluation and limitations are read from that full PDF. Zotero’s workshop page and the ACM PDF use slightly different workshop numbering in their descriptions; the note follows the title and DOI of the ACM proceedings citation.

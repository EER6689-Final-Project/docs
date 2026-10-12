# Virtual Machine Warmup Blows Hot and Cold

- **Citation:** Barrett, E., Bolz-Tereick, C. F., Killick, R., Mount, S., & Tratt, L. (2017). Virtual machine warmup blows hot and cold. *Proceedings of the ACM on Programming Languages, 1*(OOPSLA), Article 52, 1–27. https://doi.org/10.1145/3133876
- **Zotero key:** `ISZ9TU75`.
- **Source:** Zotero’s 40-page attachment is arXiv:1602.00602v6, dated 6 October 2017. It is preserved as [Barrett et al. 2017 - Virtual Machine Warmup Blows Hot and Cold.pdf](Barrett%20et%20al.%202017%20-%20Virtual%20Machine%20Warmup%20Blows%20Hot%20and%20Cold.pdf). The Zotero citation refers to the later 27-page PACMPL OOPSLA article; page references below use the attached arXiv PDF’s numbered manuscript pages.

## Research question and approach

The authors test whether small, deterministic programs running on virtual machines reliably reach a steady state of peak performance after warmup. They use six microbenchmarks (five from the Computer Language Benchmarks Game plus Richards), implemented in C, Java, JavaScript, Python, Lua, PHP, and Ruby, across eight language implementations and three machines: two Debian Linux systems with different CPUs and one OpenBSD system on the second CPU. Each benchmark execution has 2,000 in-process iterations and is repeated across 30 process executions (PDF pp. 5–7).

They detect outliers with a sliding-window rule, then use PELT changepoint analysis for changes in both mean and variance. The authors classify a run as flat, warmup, slowdown, or no steady state; a steady state requires the final 500 iterations to be equivalent to the final segment under their chosen tolerance (PDF pp. 10–12).

## Findings from the source

- The experiment covers 3,660 process executions and 7,320,000 in-process iterations. The authors’ abstract reports that at most 43.5% of `<VM, benchmark>` pairs consistently reach a steady state of peak performance. In the results, they separately report “good” warmup categories (flat, warmup, or good inconsistency): these account for 43.4% of pairs on one Linux machine, while the share of individual process executions classified as good is higher. These are distinct outcomes under the paper’s definitions (PDF pp. 12–13).
- Their analysis finds both warmup and slowdown patterns, as well as runs that do not reach a stable classification by the end of the 2,000 iterations. Thus discarding a fixed initial warmup period would not reliably isolate a peak-performance steady state in these tested configurations (PDF pp. 11–13).

## Relevance and limits

This source shows how a time series of repeated measurements can contain warmup, changepoints, slowdown, and unstable behavior, and it demonstrates a concrete changepoint-based classification protocol. The sample is a deliberately controlled set of small deterministic language microbenchmarks and historical VM versions, not browser navigation or field measurements. Its operational definition of steady state (including the 500-iteration window and 0.001-second tolerance) is specific to the authors’ setup and should not be treated as a general threshold.

**Researcher inference:** For browser performance experiments, the paper motivates inspecting within-run trajectories and validating any warmup exclusion rule against the metric and runtime being measured. It does not show that this particular PELT configuration transfers directly to page-load data.

## Provenance and metadata note

The attachment is the arXiv v6 manuscript, with draft-style front matter and 40 PDF pages, while the Zotero record identifies the published PACMPL article (2017, volume 1, OOPSLA, pages 1–27; DOI `10.1145/3133876`). The methods, sample, and findings in this note are read from the attached v6 manuscript and its own page sequence.

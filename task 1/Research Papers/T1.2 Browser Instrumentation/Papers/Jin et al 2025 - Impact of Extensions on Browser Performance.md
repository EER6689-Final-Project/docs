# Impact of Extensions on Browser Performance: An Empirical Study on Google Chrome

- **Citation:** Jin, B., Li, H., & Zou, Y. (2025). Impact of extensions on browser performance: An empirical study on Google Chrome. *Empirical Software Engineering, 30*, Article 103. https://doi.org/10.1007/s10664-025-10633-1
- **Zotero key:** MF3Z7MCZ (jinImpactExtensionsBrowser2025).
- **Source access:** Zotero has no PDF attachment. This outline uses the authors' arXiv v1 preprint, submitted 10 April 2024, as supporting full text for the 2025 journal citation: https://arxiv.org/abs/2404.06827 (HTML: https://arxiv.org/html/2404.06827). Claims below are grounded in v1 and were not cross-checked against the final journal typeset version.

## Abstract

The authors study how Chrome extensions affect page-load time and energy use, including cases where extensions are not logged in, lack access to a page, are used on non-designated sites, or are inactive. Their study reports performance impacts across selected extensions and identifies extension characteristics associated with those impacts. This is a paraphrase, not a transcription.

## Outline Summary

- **Central idea**
  - Evaluate ordinary and unintended extension usage because an installed extension may affect browser performance when a user does not actively use it as intended.
  - Relate observed impacts to extension attributes, including code structure, privacy practices, and activation mode; associations do not establish causal explanations.
- **Research problem and objectives**
  - Ask how extensions affect Chrome page-load time and energy, how activation modes alter the effect, and which characteristics are associated with impact (§§2–3, arXiv v1).
  - The target is desktop Chrome. Browser instrumentation and profiler overhead are not the study's primary questions.
- **Approach and experimental setup**
  - Collected 110,240 extensions from 11 Chrome Web Store categories, then clustered and selected representatives; the performance study covers 72 extensions (§§2.1–2.2).
  - Constructed site and interaction scenarios for expected use and four partial/inactive modes: no permission grant, no login, non-designated website, and fully inactive (§2.3).
  - Ran each extension's designated site scenario ten times with and without that extension; other extensions were removed. Measurements are normalized against extension-free measurements (§§2.5–2.6, §3).
  - Measures are page-load time, system energy during page load, and energy during a fixed post-load period (§2.4). The study does not establish results for other browsers or mobile Chrome.
- **Metrics and methods**
  - Page-load time, page-load energy, stabilized energy; extension attributes include code metrics, file characteristics, privacy-practice indicators, category, user/rating factors, and usage scenarios (§§2.4, 3.3).
  - Statistical comparisons examine effects across repeated runs and activation modes. Elastic-net models explore factor associations; the authors caution that correlation does not establish causation (§3.3, §4).
- **Key results**
  - Partial or inactive modes could still change at least one measured metric in tested cases (§3.2).
  - In no-login mode, 12 of 17 tested extensions increased page-load energy by an average of 18% among the reported increases; seven had a significant page-load-time effect, with an average 33% increase among those reported increases. These are subgroup results, not average effects for all extensions or browsing (§3.2).
  - The authors report significant associations between some extension characteristics, privacy practices, and outcomes; the models do not show that any one characteristic causes the effects (§3.3–§4).
- **Limitations and interpretation**
  - The sample is a selected, clustered subset; the authors note possible sampling bias and screening/metadata constraints (§4).
  - Only Chrome is studied. Network instability, background processes, assumed user behavior, and limited scenarios affect construct and external validity (§4).
  - The study is evidence that extensions can be a browser-performance context factor; it does not quantify proposed-profiler overhead or specify a universal extension-control policy.
- **Author-stated future work**
  - The conclusion recommends testing and optimizing extensions under unintended usage scenarios and considering privacy practices and code complexity (§6). A distinct future-work programme was not established from reviewed v1 sections.
- **Relationship to our profiler**
  - **Preliminary inference:** extension inventory, enabled state, permission/login state, and site compatibility may be relevant run-context fields. Whether those factors are in scope remains for later synthesis.
  - This is contextual empirical evidence about Chrome performance variation, not a validation of browser instrumentation.
- **Important quotations and page numbers**
  - No direct quotation transcribed. Anchors: experiment design §§2.1–2.6; results and activation modes §§3.1–3.3; threats to validity §4; conclusion §6 of arXiv v1. Printed page references were not verified against the journal PDF.
- **Concise takeaway**
  - Chrome extensions may affect timing and energy outside their intended active state. Impact depends on the extension, scenario, and setup.

## T1.2 Evidence Check

- **Qualified:** Results come from the authors' 2024 arXiv v1 study and selected desktop Chrome scenarios. Zotero has no PDF; the arXiv full text was accessible, but the final journal version was not compared section by section.
- **Preliminary inference:** Treat extension state as a candidate confound or context variable for later protocol review. This does not select a setup or research gap.

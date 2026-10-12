# Web Execution Bundles: Reproducible, Accurate, and Archivable Web Measurements

- **Citation:** Hantke, F., Snyder, P., Haddadi, H., & Stock, B. (2025). Web execution bundles: Reproducible, accurate, and archivable web measurements. *34th USENIX Security Symposium (USENIX Security 25)*, 8235–8253. USENIX Association. https://www.usenix.org/conference/usenixsecurity25/presentation/hantke
- **Zotero key:** `ZZSL9IPU`.
- **Source:** Zotero-attached 19-page PDF is the arXiv v4 preprint, arXiv:2501.15911 (4 June 2025); final proceedings record and pagination verified on USENIX. PDF page anchors below refer to the attached preprint.

## Research question and approach

The paper argues that web measurement tools and archives often fail to capture browser behavior comprehensively, which can make measurements inaccurate and hard to reproduce. It introduces WebREC, a Chromium-integrated measurement tool, and `.web`, an archive format that records browser execution behavior. The authors compare the approach with existing tools and archives through experiments, replications, and a survey of prior measurement papers (PDF §§1–2, pp. 1–5; §4, pp. 7–12; §5, pp. 12–13).

## Findings from the source

- The authors report that WebREC captures browser events that conventional instrumentation can miss, including script execution and event-listener behavior (PDF §§2.2–2.3, pp. 3–6).
- In a request-count comparison over 8,544 successfully crawled origins, the `.web` behavior records contained 776,229 requests against 778,500 filtered HAR requests, a difference below 0.3%. The paper explains that HAR includes requests outside page context while `.web` records page activity; each format therefore answers a somewhat different measurement question (PDF §4.5.2, pp. 11–12).
- The authors say 70% of studies in their selected web-crawling survey could be conducted with WebREC as-is, and 48% could use `.web` archives without new crawling (abstract; §5, pp. 12–13).

## Relevance and limits

This is direct evidence that browser-based measurement agents and their archives have an observation boundary: the recorded activity depends on the tool’s integration level and on the event definition. Its “accuracy” claims are comparisons against specified baselines and tasks, not proof that a synthetic browser run represents the distribution of real user experiences. The request comparison also depends on explicit filtering and attribution rules; race conditions and page-internal requests remain sources of disagreement (PDF §4.5.2, pp. 11–12).

**Researcher inference:** For an external-validity argument, cite this paper to distinguish measurement completeness and reproducibility from representativeness of users, networks, devices, or browsing intent. It does not validate Lighthouse scores against field outcomes.

## Provenance and verification

Zotero metadata supplied arXiv:2501.15911 and the attached PDF; the paper’s first pages identify the authors and title. USENIX’s proceedings page confirms final venue, page range, publisher, and the final paper link. The Zotero item date is the preprint date, not the final conference publication date.

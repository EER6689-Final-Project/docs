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

## T1.6 reuse check - 2026-10-25

**Extraction:** Sol (AI), 2026-10-25; `ERP-2026-10-25-v1.0`; `S-0012`; R2/R3/R6. Checked local file: `Hantke et al. 2025 - Web Execution Bundles Reproducible, Accurate, and Archivable Web Measurements.pdf`, the arXiv v4 version identified in this note, not the final proceedings PDF. Existing Zotero alias `ZZSL9IPU` and version metadata were not re-resolved in a live library. Anchors below are preprint PDF pages, not proceedings pagination.

- **C-T1.6-098 / QC-098:** §2.3 (PDF p. 5) explains that replaying resource archives may change execution because of non-determinism and differences in browser/environment. §§3.1–3.2 (PDF p. 6) instead describe `.web` as recording observed execution and WebREC as Chromium-dependent; §6.1 (PDF p. 13) describes reanalysis of recorded activity without rerunning responses. **Support outcome: confirmed** for this architectural distinction; **methodological confidence: higher** for the narrow distinction, not a claim of complete capture or user representativeness. Reviewer interpretation: archived-execution reproducibility and representative real-user performance are separate evidentiary questions.
- **C-T1.6-099 / QC-099:** The evaluation has explicit limits: §4.2 (PDF p. 8) reports quirks-mode effects, missed `srcdoc` iframe executions and recording races in its comparison pipeline; §4.4.2 (PDF p. 10) reports a PageGraph SVG-event-handler limitation addressed in a newer version. The discussion on PDF p. 13 excludes some outside-page-context studies and other browser engines. **Support outcome: confirmed** for these bounded limitations; **methodological confidence: limited** for transfer to a browser-performance corpus, because task-specific capture and baseline/replay behavior do not establish a representative device/network/user distribution or independent category ground truth. Pipeline-specific limitations must not be presented as unavoidable defects of every WebREC deployment.

**Design-specific appraisal:** recording-versus-reexecution distinction **adequate**, clearly specified; baseline construct equivalence **concern**, since JS hooks and deeper browser recording have different observation boundaries (§§4.3–4.4, PDF pp. 8–10); fidelity/missingness **concern**, with reported pipeline and implementation limits; sampling/user representativeness **unclear**, not established by task comparisons; cross-browser transfer **concern**, explicitly Chromium-dependent; quantitative accuracy/table claims **not applicable** to this reuse block, none imported. An accurate statement of the architecture does not upgrade the methodological confidence of a population-transfer claim.

**Dependency and transfer:** `DEP-WEBREC-PAGEGRAPH` groups WebREC, its PageGraph infrastructure, the same crawl/replay pipeline and version reuse; they are not independent replications. Reanalysis of a captured execution shares that execution's selection and observation boundaries. A resource replay, an archived behavior graph and a new live visit must not silently become interchangeable experimental units. No corpus, scope, novelty or gate choice is made here.

**Read bounds and QC:** Actual local `pdftotext -layout` extraction at 2026-10-25T23:22:05.298100–23:22:05.463710+05:30 covered PDF pp. 3, 5–6, 8–10 and 13 only. Computed local SHA-256: `5a0b2dc6d9c2f69212d2c6fee140f65bef6d0cd08bcf6a99bca86ac2f0c1df4c`. Separate original-PDF reread at 23:22:39.898833–23:22:40.214158+05:30 checked pp. 5–6, 8, 10 and 13 for both new claims. `QC-098`/`QC-099`: **checked-no-discrepancy**. Sol, 2026-10-25, AI self-audit, not independent human review. Both claims belong to the expanded check `C-T1.6-090`–`099` prompted by the Kalibera exploratory pagination discrepancy. The final version, unread pages and historical access times are not silently verified; no discovery query occurred.

## Decision-critical final-version check — 2026-10-31

`SC-C08` in the [source appraisal](<../../../Research Archive/Review Artifacts/2026-10-31 Decision-Critical Source Checks/Source Appraisals.md#sc-c08--webrec-final-proceedings-passages-checked>) adds targeted checks in the final 20-page USENIX PDF, preserving the existing 19-page arXiv v4 attachment. Final §2.3.2, printed 8239 / PDF 6; §§3.2–3.3, printed 8240–8241 / PDF 7–8; and §6.1, printed 8247 / PDF 14 support the same recorded-execution versus response-replay distinction. This supersedes the earlier final-version-unread status only for those passages. It does not establish whole-version equivalence, complete performance-event capture or measured cost for this project. `DEP-WEBREC-PAGEGRAPH` remains one dependent source family. Separate-pass AI self-audit, not independent human review.

# Mahimahi: Accurate Record-and-Replay for HTTP

## Identity, artifact and review boundary

- **S-0003:** Ravi Netravali, Anirudh Sivaraman, Somak Das, Ameesh Goyal, Keith Winstein, James Mickens and Hari Balakrishnan (2015), USENIX ATC '15. https://www.usenix.org/conference/atc15/technical-session/presentation/netravali.
- Zotero work `6UGAU5X4`, attachment `HR25KWHX`; numeric library identity/type not independently resolved in this pass.
- Source: `/home/mendydias/Zotero/storage/HR25KWHX/Netravali et al. - 2015 - Mahimahi Accurate Record-and-Replay for HTTP.pdf`.
- Preserved copy: `task 1/Research Papers/T1.6 Experimental Design/Papers/Netravali et al 2015 - Mahimahi Accurate Record-and-Replay for HTTP.pdf`.
- SHA-256 (source and copy): `67b2d0330898b72200c9b66662ad01b3d0f9305f3045678e5792942bf92ec3cb`.
- Version: proceedings PDF, 14 PDF pages including cover. PDF p. 6 carries manuscript p. 5 / proceedings p. 421; PDF p. 1 is a venue cover, not an abstract.
- Extractor GPT-6.1 Sol, 2026-10-25, time unknown; `ERP-2026-10-25-v1.0`, G0 accepted. Updated Luna handoff used as aid. Original PDF pp. 1-2, 4-7 re-opened for identity, framework, fidelity and limits; no claim of this agent rereading all 14 pages. Handoff's full-source review is distinct from this critical-passage pass.

## C-T1.6-003 / S-0003 / R3, R5, R6

**Exact proposed claim:** The paper reports multi-server loading in 98% of Alexa US Top-500 pages and evaluates protocols on a 500-site corpus, but the direct live-versus-replay fidelity comparison covers only 20 pages loaded 25 times each. These are distinct quantities and designs.

**Original passages:** Abstract, PDF p. 2: “multi-server nature of Web applications, present in 98% of the Alexa US Top 500 Web pages” and, separately, protocol evaluation “on a corpus of 500 sites.” §4.1, PDF p. 6: “Only 9 of the 500 Web pages (1.8%) we consider use a single server.” This is compatible with the abstract's rounded 98%, not 98% replay accuracy. The same section specifies “Google Chrome loading 20 Web pages from the Alexa US Top 500, 25 times each,” under a 5 Mbit/s LinkShell and minimum RTT 100 ms.

### Population, procedure and comparisons

- Historical Alexa US frame, not a probability sample of all pages/users. Footnote 3, PDF p. 6: the 20 live-comparison sites were all CDN-hosted nearby, ping less than 5 ms; minimum emulated RTT was chosen to equalize delays. This selection boundary is material to fidelity.
- Browser automated with Selenium/Google Chrome; exact Chrome build, cache reset and randomized live/replay order are not established by the checked fidelity passage. RecordShell and web-page-replay record immediately after Internet measurements to limit changing-content mismatch, not simultaneously from the same execution.
- Each recorded page replayed 25 times using multi-server ReplayShell, modified single-server ReplayShell, and web-page-replay at matched stated link/RTT settings. Experimental observations are executions nested within pages, not 25 independent sites per page.
- Separate broader experiment in §4.1 loads recorded Alexa US Top-500 pages under nine link/RTT configurations, using both multi-server and single-server ReplayShell; it is not live validation of all 500. EC2 m3.large, US-east-1a, Ubuntu 13.10. The abstract's broader protocol evaluation is another use of the corpus, not a substitute live benchmark.

### Metrics, analysis and contrary evidence

§4.1, PDF p. 6 defines per-site error as the absolute percent difference between mean PLTs over 25 runs in replay and on the Internet. Median errors across sites: **12.4%** multi-server ReplayShell, **36.7%** web-page-replay, **20.5%** single-server ReplayShell. These are descriptive errors, not confidence bounds, universal tolerances or exact equality. No inferential interval is reconstructed here. Footnote 4 explicitly says “We are not certain why single-server ReplayShell is so much more accurate than web-page-replay.” Thus not all performance differences are explained by multi-server preservation.

§3, PDF pp. 4-5: recorded request/response pairs are replayed; matching uses a heuristic when client state changes the request. §2.2, PDF p. 4 limits topology to one physical client connected to servers, not arbitrary network topology. Namespace isolation (§4.2, PDF p. 6) addresses network cross-traffic interference, not every CPU/shared-host or server-behavior confound. Failure/coverage of arbitrary dynamic workflows is not quantified by this extraction. Recorded responses cannot establish fidelity to all mutable backend behavior.

### Support and appraisal

**Support: confirmed** for the differentiated corpus/design statement; **qualified** for replay-fidelity transfer. **Methodological confidence: higher** for the documented sample and comparison structure, **limited** for a general claim of accurate replay across contemporary sites or workflows.

| Domain | Judgment and reason |
| --- | --- |
| Construct/pairing | adequate for comparison of stated PLTs; concern because captures follow live runs and are not identical live executions |
| Sampling/coverage | concern: 20 nearby-CDN pages are a narrow live comparison; 500 replayed pages do not repair that boundary |
| Manipulation/fidelity | adequate for testing preserved versus collapsed server structure; concern for dynamic responses and topology generalization |
| Allocation/state | unclear: exact browser build, cache/order controls not established by checked passage |
| Uncertainty/reference | concern: mean-based absolute error with descriptive median is not an agreement tolerance or uncertainty analysis |

Dependency group **DG-T16-MAHIMAHI**: 500-page analyses, replay variants and later protocol experiments share framework/captures; count as one source family, not independent corroborations. Related S-0002 illustrates server consolidation's consequences; different study goals/artifacts preclude treating disagreement as a replication failure. Later Mahimahi-based systems reuse this infrastructure and require dependency checking by their note owner.

**Research inference - candidate only:** Replay is a possible intermediate corpus, with explicit fidelity checks and preserved server structure; it is not evidence that live evaluation can be dropped, modern browsers are validated, the proposed profiler works, or the project is novel.

## Separate-pass AI self-audit

**QC-003**, GPT-6.1 Sol, 2026-10-25, time unknown; **checked-corrected**. Reopened PDF p. 2 abstract and p. 6 §4.1 including footnotes; rechecked 98%/9-of-500, 500-site corpus versus 20 × 25, 5 Mbit/s/100 ms, nine configurations, error denominator and all three median errors. Handoff's pp. 4-5 location was corrected to PDF p. 6. Its abstract-location wording was corrected to PDF p. 2. Expanded check covers all retained numerical claims in C-T1.6-003. PDF pp. 4-5 additionally checked for replay matching/topology limits.

This note-local event awaits canonical log integration; no tracker/gate status is set. Separate-pass same-AI self-audit only; human independent review **not done**. No novelty search/citation pass or current-browser validation was performed.

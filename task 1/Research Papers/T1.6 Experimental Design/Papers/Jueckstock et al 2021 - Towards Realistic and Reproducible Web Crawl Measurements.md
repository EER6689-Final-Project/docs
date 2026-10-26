# Towards Realistic and Reproducible Web Crawl Measurements

## Identity, artifact and read boundary

- **S-0005:** Jordan Jueckstock, Shaown Sarker, Peter Snyder, Aiden Beggs, Panagiotis Papadopoulos, Matteo Varvello, Benjamin Livshits and Alexandros Kapravelos (2021), WWW '21. DOI: https://doi.org/10.1145/3442381.3450050. Title-page spelling is Aiden Beggs.
- Zotero canonical work `B9FIJAKE`, duplicate alias `TAZSGXJH` supplied by integration owner; attachment `39R54V6I`. Alias equivalence not independently re-queried; numeric library identity/type unresolved in this pass. Records/versions are not independent studies.
- Source: `/home/mendydias/Zotero/storage/39R54V6I/Jueckstock et al. - 2021 - Towards Realistic and ReproducibleWeb Crawl Measurements.pdf`.
- Preserved copy: `task 1/Research Papers/T1.6 Experimental Design/Papers/Jueckstock et al 2021 - Towards Realistic and Reproducible Web Crawl Measurements.pdf`.
- SHA-256 (source and copy): `cb934751dad035c16f761e05639ab3fde62a49abfc879d008714488660d0ce7f`.
- Version: conference-layout PDF, 12 pages; carries small manuscript-style page counters and proceedings numbers. Use PDF page + section throughout, not an unverified “printed p. 2” from the handoff. Visual p. 3 shows counters 3 and 82; the corresponding design passage is PDF p. 3 regardless of mapping.
- Extractor GPT-6.1 Sol, 2026-10-25, time unknown; `ERP-2026-10-25-v1.0`, G0 accepted. Luna handoff used as aid. Original PDF text pp. 1-5, 10-11 re-opened and p. 3 visually checked; title identity checked from original. This is a critical-passage reread, not a claim of a second cover-to-cover 12-page review.

## C-T1.6-005 / S-0005 / R3, R4, R6

**Exact proposed claim:** The study synchronized visits to each target URL across three vantage points and two browser configurations, targeting landing pages from frozen Tranco top-25,000 snapshot 77PX in three independently randomized crawl rounds. Its coverage must retain the difference between queued visits, nonfatal completion and complete success; the design is not direct observation of representative human browsing.

**Literal design anchor:** §2.2.3, **PDF p. 3**: “Each of our page sets comprises 6 synchronized parallel visits to the same URL, one for each combination of our 3 network VPs and 2 BCs representing a range of relative realism levels.” §2.4, same PDF page: top **25,000** domains, snapshot **77PX**, domain landing page only, itinerary visited **3** times. The handoff's printed-page references are not reused.

### Population, allocation, browsers and controls

§§2.2.1-2.2.2, PDF pp. 2-3: research-university network, nearby residential ISP and AWS, with a single endpoint per class; naive/headless stock Puppeteer versus stealth/non-headless Puppeteer controlling **Chromium 80**. Each page set is the synchronized six-cell comparison, not six independent sites or a random sample of human users. “Realism” is relative to chosen configurations; stealth/residential is an operational comparison reference, not empirical human ground truth.

§2.3, PDF p. 3: clean user profile for every visit, common workflow/timeouts, Cloudflare DNS, deterministic alternatives to JavaScript entropy APIs, and bandwidth/latency throttling to harmonize conditions. These controls aim to reduce nuisance variability, not establish identical server responses. Target is third-party/privacy/security behavior rather than performance metrics or user journeys. Study period is **30 April-9 May 2020** (§2.6.1, PDF p. 5). Randomized-round scheduling is documented in §2.4.1, PDF p. 4; the critical claim does not assume randomized human assignment.

### Counts, metrics, analysis and contrary findings

§2.6.1, **PDF p. 5**: **450,000** queued visits; **449,936 (99.99%)** completed without fatal error. “Of these completed pages, **375,246 (83.40%)** were completely successful” and **74,690 (16.60%)** had some level of failure. The success percentage is reported in the context of nonfatal completed visits; it is not 83.4% of unique domains, nor proof all 25K targets succeeded. Some failure labels include late teardown aborts after content collection; “fatal error,” “non-aborted navigation,” “complete success,” and “useful data” are not interchangeable. §2.3.1 allows successful non-aborted navigation even without the official load event.

§2.7, PDF p. 5: aggregate additive metrics by entity/configuration, compare rounded log2 differences, independently score rounds, intersect entities across the three rounds and take median scores. This consistency filter omits ephemeral differences; it does not provide a confidence interval for all web behavior or make every request an independent replicate. Quantitative abstract-level 19%/10% summaries are not promoted in this design-focused claim.

§4.2, **PDF p. 11**: one endpoint per class is “too small to generalize results across all cloud or residential endpoints”; stealth does not perfectly approximate human visitors and the measured bias is presented as a lower bound. §§4.1.2-4.1.3 recommendations against headless/cloud conditions are authors' historically conditioned recommendations, not normative browser conformance rules. Some content differences can reflect geography; controlling client entropy does not eliminate backend or geotargeting variation.

**Support: confirmed** for the synchronized crossed design and target frame; **qualified** for coverage and generalization. **Methodological confidence: higher** for documented allocation/control structure, **limited** for broad human or endpoint-class representativeness.

| Domain | Judgment and reason |
| --- | --- |
| Factor/control fidelity | adequate: literal six-cell structure and explicit nuisance controls; concern because BC bundles multiple changes |
| Population/vantage coverage | concern: top-list landing pages and one endpoint per class |
| Missingness | concern: partial/fatal/complete-success differences and intersection filtering restrict analyzed observations |
| Time/content equivalence | adequate for synchronized matching; concern for uncontrolled backend/geographic content differences |
| Construct/reference | concern: relative realism is not human-ground-truth validation or profiler accuracy |
| Uncertainty | concern: repeated consistency scores are not population effect confidence intervals |

Dependency group **DG-T16-JUECKSTOCK-CRAWL**: all rounds/configurations share the same snapshot, workflow and tooling; not six independent replications. The VisibleV8 author/tool lineage overlaps related instrumentation notes. S-0006 is explicitly discussed as related work, with shared measurement concerns but a different cohort/design; citation is not replication or proof of independent datasets.

**Research inference - candidate only:** Cross agent settings with sites and synchronize/block comparisons where appropriate; retain failure categories and frozen frames. This neither validates modern headless behavior nor proves the proposed profiler/design is novel or approved.

## Separate-pass AI self-audit

**QC-005**, GPT-6.1 Sol, 2026-10-25, time unknown; **checked-corrected**. Original §2.2.3/§2.4 PDF p. 3 text and rendered image confirm literal 3 × 2, 25K, 77PX and three rounds; §2.4.1 PDF p. 4 confirms independent randomized crawls. Original §2.6.1 PDF p. 5 confirms counts, percentage context, period and failure nuance; §4.2 PDF p. 11 confirms endpoint limitation. Handoff had selection at PDF p. 4, counts at p. 6 and limitations at p. 12; corrected here. Expanded check covers the full retained claim, not only the mismatched page label.

This is separate-pass **AI self-audit**, not independent review; human independent review **not done**. Note-local QC awaits canonical log integration. No tracker/gate completion, new search/citation pass, novelty finding or Zotero mutation asserted.

# The Representativeness of Automated Web Crawls as a Surrogate for Human Browsing

## Identity, artifact and read boundary

- **S-0006:** David Zeber, Sarah Bird, Camila Oliveira, Walter Rudametkin, Ilana Segall, Fredrik Wollsén and Martin Lopatka (2020), WWW '20. DOI: https://doi.org/10.1145/3366423.3380104.
- Zotero canonical work `U2NAEPYI`, duplicate alias `QYN69APX` supplied by integration owner; attachment `T4T3H4YS`. Alias equivalence not independently queried; numeric library identity/type unresolved here. Duplicates are not independent evidence.
- Source: `/home/mendydias/Zotero/storage/T4T3H4YS/Zeber et al. - 2020 - The Representativeness of Automated Web Crawls as a Surrogate for Human Browsing.pdf`.
- Preserved copy: `task 1/Research Papers/T1.6 Experimental Design/Papers/Zeber et al 2020 - The Representativeness of Automated Web Crawls as a Surrogate for Human Browsing.pdf`.
- SHA-256 (source and copy): `4dd4268452b8de87ad233dbbdc7b681252f3c7521d360d7f0cb84b1f4c5a0a66`.
- Version: 12-page conference-layout PDF. Use PDF page + section; PDF p. 3 shows proceedings p. 169, but no general printed-page mapping is needed for the anchors below.
- Extractor GPT-6.1 Sol, 2026-10-25, time unknown; `ERP-2026-10-25-v1.0`, G0 accepted. Original PDF pp. 1, 3-4, 8-10 re-opened for abstract, cohort/methods, contrast and discussion; no new cover-to-cover claim. Luna handoff is an aid, not original evidence.

## C-T1.6-006 / S-0006 / R3, R4, R6

**Exact proposed claim:** The authors compared automated crawl measurements with observed browsing from an opt-in sample of over 50,000 Firefox users, not 50,000 visits. Their selected metrics show crawl-versus-user differences, including more third-party activity in crawls, but state, sampling and observational confounding prevent a universal causal claim about all crawls or users.

**Original passage:** Abstract, PDF p. 1: “actual browsing behaviour measured from an opt-in sample of over 50,000 users of the Firefox Web browser”; it contrasts “stateless crawling infrastructure and generally stateful human browsing” and says crawlers tend to see more third-party activity. §3.4.1, **PDF p. 4** specifies approximately **52,000** opt-in participants using **Firefox 67 or 68**, en-US locale; this elaborates rather than contradicts the rounded abstract.

### Population, browser, allocation and instrumentation

- §3.4.1, PDF p. 4: existing opt-in cohort of at least six months' membership; not newly randomized human recruitment or a probability sample of all browser users. Two seven-day recording periods separated by a seven-day pause; final data span **July 16-August 13, 2019**, **30 million site visits** across **640,000 unique domains**. Counts describe distinct levels: people, visits, domains. Only summaries/selected code can be public because raw user data are sensitive.
- §3.1, PDF p. 3: OpenWPM in crawl and WebExtension instrumentation; captures navigation, requests/responses/redirects and selected fingerprinting-related JavaScript calls. Per-navigation recording stops at **500 KiB**, **10 seconds** or **1,000 events**, whichever comes first. These are observation limits, not assurance of complete page/user-session capture.
- §3.3, PDF p. 4: crawl-to-crawl work uses Alexa Top-1K, July-October 2019, **10-second dwell**. Baseline simultaneous Firefox 69 crawls, timed Firefox 68 crawls, and Firefox 69 cloud/residential and OS contrasts have different configurations; do not collapse them into one treatment. §3.4.2 describes the companion crawl launched **July 31, 2019**, Google cloud, 10-second dwell, with a hybrid top-list methodology. A top-list seed is not the actual frequency distribution of user visits.
- Units: navigation events grouped into intentional site visits, often aggregated by domain (§3.2); visits within users/sites share dependence. Crawls control selected factors but human browsing is observational, not randomized to stateless/stateful conditions. Neither identical user URLs nor identical page content is guaranteed merely by matching a domain.

### Metrics, results, analysis and contrary evidence

§3.2, PDF p. 3 defines third party by differing eTLD+1, which can classify common-owner domains as third party. Outcomes are counts of unique domains/URLs and Jaccard similarities for third-party/tracking/fingerprinting content, not PLT, interaction quality or profiler accuracy. §4.3, PDF p. 8 compares distributions of per-domain visit averages, with equal-domain and popularity-weighted views; selected-site examples show crawler counts in the upper tail of user values. The qualitative direction is retained; no additional effect-size number is needed for the claim.

Contrary/qualifying findings: §4.3, PDF p. 9 finds close agreement on fingerprinting prevalence while the identities of serving domains differ. §5, PDF p. 10 explicitly says causal mechanisms could not be directly studied from observational client sessions; differential treatment of bots may play a relatively minor role in their crawl contrasts. Cookie syncing, evolving tracker blocking, profile history, authentication, geography and users seeing different site portions remain plausible explanations, not experimentally isolated causes. The authors also warn that fewer third parties per user visit need not mean fewer cumulatively when different visits contact different parties. Thus do not infer that automated crawling always overcounts every privacy metric or that statelessness alone caused the discrepancy.

**Support: confirmed** for cohort identity and existence of the reported selected-metric divergence; **qualified** for generalization or causal interpretation. **Methodological confidence: higher** for the explicit cohort/method description, **limited** for broad user representativeness or causal attribution.

| Domain | Judgment and reason |
| --- | --- |
| Sampling/frame | concern: opt-in en-US Firefox users and top-list crawl frame differ from all users/pages |
| Measurement comparability | adequate: shared OpenWPM basis and explicit definitions; concern: caps, browser versions and state/content differences |
| Allocation/confounding | concern: human-to-crawl comparison is observational, not randomized state manipulation |
| Dependence/analysis | concern: user/site/visit hierarchy and domain aggregation cannot be interpreted as independent raw events |
| Missingness/reference | concern: capture limits and sensitive nonpublic raw data constrain complete independent reproduction |
| Outcome scope | adequate for the named privacy/content metrics; not applicable as direct performance-profiler validation |

Dependency group **DG-T16-ZEBER-OPENWPM**: shared cohort/instrumentation and companion crawl underpin several metrics, not separate human-validation replications. S-0005 cites this work but has different instrumentation/comparison endpoints and no equivalent human cohort; do not count its relative realism comparator as replication of this user sample. Shared upstream top lists/tooling can induce dependencies even across papers; sample independence is not assumed.

**Research inference - candidate only:** Label synthetic configurations as agent profiles, not representative humans, and delimit conclusions by observed metrics and state. This does not validate the proposed profiler, modern Firefox/Chromium, or a novelty claim.

## Separate-pass AI self-audit

**QC-006**, GPT-6.1 Sol, 2026-10-25, time unknown; **checked-no-discrepancy** for the bounded cohort claim. Reopened original abstract PDF p. 1 and §3.4.1 PDF p. 4: >50K users is consistent with approximately 52K; it is distinct from 30 million visits and 640K domains. Original §3.1 PDF p. 3 checked all three capture limits; §3.3-3.4 PDF p. 4 checked browser/version/dwell/cohort dates. §§4.3/5 PDF pp. 8-10 checked selected-metric divergence, fingerprinting counterexample and noncausal/stateful qualifications. No unverified table-effect numbers retained.

Separate-pass **AI self-audit**, not independent scientific review; human independent review **not done**. QC is note-local pending canonical log integration; no tracker/gate change or Zotero mutation. Novelty/citation passes **not run**.

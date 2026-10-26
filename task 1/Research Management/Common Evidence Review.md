# Common Evidence Review

**Prepared:** 2026-10-26, Sol (AI synthesis/secondary passage check).
**Status:** bounded step-4 preparation, **not G3 closure**; G3/G4 remain **OPEN**.
**Protocol:** [Evidence Review Protocol](<Evidence Review Protocol.md>), `ERP-2026-10-25-v1.0`; eligibility cutoff 2026-10-25 inclusive, unchanged.

## 1. Authority, provenance and limits

- Governing approval: [Scope Resolution](<Scope Resolution.md>), §§5.1–5.2 and 6, records actual user decisions received 2026-10-25, integrated 2026-10-26. This memo does not infer approvals from older pending tracker text.
- D-003-B/E approve initial navigation plus fixed non-consequential inputs, with conditional synthetic INP; SPA soft-navigation metrics are version-gated exploratory, **not promised capability**.
- D-003-F approves per-output version-matched references and separates same-artifact conformance from independent-run agreement; exact reference versions/methods remain open.
- D-003-G approves a versioned developer diagnostic-prioritization composite alongside raw metrics/severity, **not weights, calibration or universal UX validity**.
- Scientific-choice/accountable researcher and project-scope owner: **user**. Orchestrator is an **AI technical-check coordinator**, not site/institutional/ethics authority; those external authorities remain unassigned. No independent human scientific review is claimed.
- Input: Luna's 43-line `/tmp/opencode/eei6689-common-evidence/handoff.md`, inspected 2026-10-26; reported source accesses also 2026-10-26, exact times not captured. This is a handoff, not an immutable historical webpage archive.
- Sol reopened the four original URLs below on **2026-10-26** through read-only `webfetch`; exact clock times were not captured. These are additional accesses, not reconstructed Luna times or 2026-10-25 snapshots.
- All these live-page reads are **after cutoff**. Displayed publication/revision/footer dates are metadata, not proof of the exact historical page state. No retrospective eligibility or gate promotion follows; orchestrator must disposition later-access evidence under ERP before promotion.
- Passage checks are **AI secondary-pass self-audit**, not independent human review or a completed ERP §9 gate-wide QC manifest. Documentation supports what it says, not independently demonstrated browser behavior.
- Existing parent keys below remain identity pointers under families **C-001/C-003/C-008**, decisions **D-003/D-004**, and blocker **B-004**; these are not new atomic claim IDs. No new S/Q/QC IDs are assigned before the all-topic identity crosswalk/owner reconciliation.
- The T1.6 inventory's **21 reviewed portfolio works** remain unchanged; this memo adds no portfolio works, matrix rows, collection census or independent studies.

## 2. CrUX origin/page eligibility and metric denominators

**Identity/anchors:** methodology parent `3KVANYXJ`, [CrUX methodology](https://developer.chrome.com/docs/crux/methodology), exact headings **“Eligibility”**, **“Origin”**, **“Page”**, **“User”**; metrics parent `DP9EINBS`, [Metrics](https://developer.chrome.com/docs/crux/methodology/metrics), **“Navigation types”**, **“Time to First Byte”** and **“Experimental soft navigation core web vitals metrics”**. Families C-001/C-003/C-008; B-004; D-003-B/D/E/F.

**Luna read boundary:** methodology live page, 2026-10-26; no dated 2026-10-08 capture located/retrieved. The handoff names the metrics key but does not document a separate metrics-page read; do not invent one. Sol read both returned pages on 2026-10-26, limited here to the headings above and their immediate context.

**Source wording:** “Eligibility” requires User, Origin and Page for page-level data in PageSpeed Insights and the CrUX API, then says:

> Experiences which meet the User and Origin criteria but not Page aren't included in the origin-level data available in all CrUX data sources.

Under “Origin”, after discoverability/popularity requirements, it instead says:

> If an origin is determined to be publicly discoverable, eligible user experiences on all of that origin's pages are aggregated at the origin-level, regardless of individual page discoverability.

**Disposition:** the current official text retains an **apparent origin/page eligibility conflict**. The quotations' different tool/aggregation scopes matter; neither the handoff nor this memo authorizes choosing one edge rule as correct. Exact 2026-10-08 wording remains **needs retrieval**, not disproved or replaced by today's text.

**Metric context:** “Time to First Byte” explicitly limits CrUX TTFB to full page loads, unlike LCP coverage of bfcache/prerender, and warns its smaller sample need not be directly comparable. “Navigation types” distinguishes those navigation classes. This is a metric-specific denominator warning, not a synthetic-run correction formula. The experimental soft-navigation section describes separate experimental metrics including full loads and soft navigations; it does not resolve origin eligibility or independently verify rollout.

**Appraisal:** documentation authority **adequate** for attributed wording; version/historical-state and capture-boundary domains **concern** because the live page is mutable and internally ambiguous. Methodological confidence **limited** for an exact inclusion-rule claim. Field/synthetic transfer remains qualified; no population equivalence is established. Both pages share upstream Chrome documentation, not independent replication.

**Recommendation under approved scope:** retain CrUX as a contextual field reference with explicit user/eligibility/aggregation/metric-denominator differences, not synthetic ground truth. The approved synthetic navigation-plus-input study **does not depend on this disputed origin edge rule**. That non-dependence is a scoped research appraisal/recommendation, not a factual resolution or blanket B-004 closure; retain the caveat wherever that edge is discussed.

## 3. Soft-navigation documentation versus actual shipping/build support

**Identity/anchors:** parent `486KI7NN`, [Measuring soft navigations](https://developer.chrome.com/docs/web-platform/soft-navigations), exact headings **“How do I enable soft navigations in Chrome?”**, **“What are the implications of enabling soft navigations in Chrome?”**, **“Feature detecting Soft Navigations API support”**, **“How will soft navigations be reported in CrUX?”**. Families C-001/C-003/C-008; B-004; D-003-B/E/I/F.

**Luna read boundary:** 2026-10-26 live page; historical T1.1 note reports a 2026-10-08 retrieval, not an archived page supplied here. Luna's one official-release-site search returned no results and retrieved no release note/version history; that is **not evidence of non-release**. Sol reopened the page, not release evidence or a browser executable, on 2026-10-26.

**Source wording**, under “How do I enable soft navigations in Chrome?”:

> The soft navigations feature is enabled by default from Chrome 151.

The implications section warns that support differs for other browsers/Chrome before 151, and some users may report CWV without soft-navigation-based metrics. The CrUX heading describes experimental metrics and a **plan** to graduate them in May 2027; a plan is not observed implementation or guaranteed delivery.

**Disposition:** retained **qualified documentation assertion** about version 151, not confirmed Chrome 151 Stable shipping by cutoff/access, actual rollout, or support in the project's as-yet-unpinned target build. Those implementation/release facts remain **needs retrieval/verification**. Do not convert a support badge, sidebar category or mutable prose into a Stable-release receipt.

**Appraisal:** source authority **adequate** for documentation wording; release/build conformance **unclear**, historical version boundary **concern**. Methodological confidence **limited** for implementation availability. CrUX and soft-navigation pages are dependent official documentation, not independent corroboration of shipping.

**Recommendation under approved scope:** keep soft-navigation measures exploratory/version-gated; there is no implicit stable-feature promise. Required initial navigation plus fixed qualifying inputs/conditional synthetic INP is not contingent on stable soft-navigation APIs. If a candidate makes route-level metrics essential, pin build/channel/flags and verify API/metric behavior before G5/G6; unsupported exploratory outputs must be disclosed, not silently fabricated.

## 4. Lighthouse historical scoring versus a chosen reference configuration

**Identity/anchors:** parent `WB6JZEUA`, [Lighthouse performance scoring](https://developer.chrome.com/docs/lighthouse/performance/performance-scoring), exact headings **“How the Performance score is weighted”**, **“Lighthouse 10”**, **“How metric scores are determined”**, **“How desktop versus mobile is handled”**. Families C-001/C-008; B-004; D-003-F/G.

**Luna read boundary:** returned live page, 2026-10-26, historical v10 table/transformation prose; not a release/config/source audit. Sol reopened the same URL/retained headings on 2026-10-26; no calculator run, package inspection or browser comparison was performed.

**Source wording:** the weighting heading calls the Performance score a “weighted average” of **metric scores**, not raw timings; “How metric scores are determined” describes transformation using a “log-normal distribution”. The page explicitly says weightings have changed over time.

**Version-labelled table:** under **“Lighthouse 10”**, FCP **10%**, Speed Index **10%**, LCP **25%**, TBT **30%**, CLS **25%**. This is the table's attribution, not a current-2026 release claim or a selected custom score. Desktop/mobile scoring context further rules out assuming every configuration interchangeable.

**Disposition:** retain **qualified historical/version-labelled definition/example** of weighted metric-score composition and the documented log-normal transformation. Current-release formula, weights, control points and actual comparison configuration remain **needs retrieval** when a reference is chosen at G5. The source does not validate project weights, statistical estimators, a universal UX scalar or carbon/energy validity.

**Appraisal:** documentation authority **adequate** for attributed mechanics/table; currency/configuration **concern** and actual implementation correspondence **unclear**. Methodological confidence **limited** for current/custom-score transfer. No independent implementation check or score-validity study is supplied by this passage.

**Recommendation under approved scope:** preserve D-003-G's approved diagnostic purpose, raw components and severity alongside a versioned composite. Leave transformations, missingness, weighting/calibration and severity thresholds open. Inspect the exact release artifact/configuration only for the actual reference selected; a broad all-version history sweep is not required by this memo.

## 5. Additional recheck receipts and metadata corrections

Each row is one successful Sol `webfetch` return on **2026-10-26**, no exact clock captured; original URLs are linked in §§2–4. These are passage-level receipts, not immutable archived captures, new discovery searches or formal QC-ID allocations.

| Original page / parent | Observed revision metadata and retained finding |
| --- | --- |
| CrUX methodology / `3KVANYXJ` | Footer **2024-06-20 UTC**; both conflicting passages persist. Footer does not establish the October 8 or 25 historical state. |
| CrUX Metrics / `DP9EINBS` | Published **2022-06-23**, updated/footer **2026-10-13**; TTFB denominator qualification and experimental soft-navigation heading read. This separate Sol read was not evidenced as a separate Luna read. |
| Measuring soft navigations / `486KI7NN` | Published **2023-02-01**; displayed introduction says updated **2026-09-20**, footer says **2026-10-20 UTC**. Preserve both, rather than collapsing Luna's introduction date into a unique revision. Exact quote uses plural **“soft navigations feature”**, correcting the handoff's singular transcription; meaning unchanged. No shipping evidence retrieved. |
| Lighthouse performance scoring / `WB6JZEUA` | Footer **2019-09-19 UTC** despite explicit v10/v8 tables; treat footer as displayed metadata, not proof that v10 content existed in 2019. Historical attribution and transformed-score distinction retained. |

## 6. Coverage deficit and finite next actions

[Discovery preservation README](<Review Artifacts/2026-10-26 Discovery/README.md>), §§1–3/5, records **838 occurrences**, all **STAGE1-PENDING**: automatic triage is unvalidated, with a critical unresolved ERP §§7/9 deviation. Its 144 X3 and three metadata-language X2 labels are not validated exclusions; duplicate candidates and the all-topic work crosswalk remain unresolved. The expanded corrective list covers **all 838**, not a reassuring sample. Coverage/access/rank gaps remain explicit. This memo neither validates those decisions nor allocates source IDs from them.

**Subsequent accepted correction snapshot:** log §13 and [Eligibility Correction](<Review Artifacts/2026-10-26 Eligibility Correction/README.md>) supersede the initial all-pending state through additive events: **94 advance / 44 X3 / 700 pending**. All 173 proposed OA exclusions and 22 additional sample sources received semantic QA; 105 other OA rows and all 538 Scholar mappings remain unfinished. Final regroup QC and canonical identities/citation/full-text work are still open. Original discovery files retain their historical values; advances are not verified source findings or full-text inclusions.

**Later accepted snapshot 3:** [combined receipt](<Review Artifacts/2026-10-26 Eligibility Correction/Accepted Snapshot 3/README.md>) and log §14 supersede those earlier counts: **208 advance / 46 X3 / 584 pending**. All 300 OA original-export semantic checks are now complete, with 66 mappings unresolved; first-25 Scholar QA is accepted, leaving 513 Scholar without accepted semantic QA. Global regroup/identity/citation/full-text requirements remain open. This replaces neither immutable history nor source-level caveats.

**Current accepted snapshot 7:** [combined receipt](<Review Artifacts/2026-10-26 Eligibility Correction/Accepted Snapshot 7/README.md>) and log §18 record **574 advance / 112 X3 / 152 pending** occurrences. All 838 original-export semantic checks are complete (300 OA/538 Scholar), but 152 reviewed holds remain unresolved. The completed 130-member OA expansion assessed 151 affected memberships: 87 metadata-supported/44 unclear/20 outside that R, not a global pass or new exclusions. Inherited mappings, identity/date/language/type, content/coverage gaps, citations and full texts remain separate; no new source rows, source confidence or novelty inference follow. All assigned metadata-review subagents have returned.

New-discovery citation and full-text/method passes are **NOT RUN**; this memo runs none. Inaccessible/abstract-limited classic statistical sources remain at their recorded access boundaries: unknown methods/formulas are **not verified** by documentation review, citation presence or scope approval. Other retained semantic claims and closest-solution/contrary evidence still need protocol checks. **G3/G4 and B-004 remain OPEN despite common-scope narrowing**; no G1/G2 acceptance is declared here.

| Common claim retained, qualified | Trigger and finite check before dependence/promotion | Accountable owner / timing |
| --- | --- | --- |
| CrUX is contextual field evidence; disputed origin/page rule remains caveated. Approved synthetic scope need not rely on it. | If inclusion edge drives a candidate/denominator claim, retrieve the exact 2026-10-08 snapshot and reconcile both passages with authoritative clarification; if unavailable, retain blocker or explicitly bound/remove that claim. | User scientific owner; orchestrator coordinates AI checks before affected G3/G5 promotion. |
| Official docs assert enablement from 151; shipping and target build remain unverified. | If soft-navigation support becomes essential, obtain official release/channel evidence and verify pinned target build/flags, feature detection and metric attribution. Otherwise preserve exploratory label. | User; AI technical checks before affected G5/G6. |
| Lighthouse v10 is a historical weighted/transformed-score example, not current/custom weights. | On actual reference selection, pin release/artifact/profile/config/source; check selected output's formula/weights and distinguish raw metrics from transformed score. Justify custom parameters separately. | User; AI technical checks at G5 before numerical adoption. |
| Narrowing dependence does not establish sufficient evidence or novelty. | Continue from snapshot 7 (574/112/152); resolve prioritized holds/inherited mappings, canonical identities/source roles and coverage dispositions before citation/full-text claims. Do not repeat completed metadata batches. | User scientific accountability; orchestrator integration before G3/G4 passage. |

No contribution is selected; no metric contract, score weights, estimator, tolerance, pilot budget or protocol is frozen. No implementation, scans, collection, human study, library mutation, shared-tracker/log edit, staging or commit is authorized/performed by this memo.

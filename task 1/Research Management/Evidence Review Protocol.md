# Evidence Review Protocol

**Version:** 1.0 — frozen rules, not a completed review
**Freeze identifier:** `ERP-2026-10-25-v1.0`
**Frozen:** 2026-10-25 (+05:30; local system date checked during preparation)
**Scope:** bounded, systematic evidence-led phase-zero review for T1.1–T1.6; not a formal systematic literature review or an exhaustive search.
**At freeze:** no new searches, screening, extraction, or passage verification had been performed under these rules. Actual execution is recorded in the Search and Screening Log.
**G0:** orchestrator review accepted on 2026-10-25; the queue is the canonical live gate register. This is procedural acceptance, not scientific verification or scope approval.

## 1. Purpose and review questions

These questions constrain evidence gathering before selecting a thesis contribution. They are not the final thesis question.
Prior syntheses and generated citations are discovery aids, not verified evidence. Historical reviews retain their actual dates and access limits.

| ID | Bounded question | Relevant population/phenomenon | Comparators and outcomes sought |
| --- | --- | --- | --- |
| R1 | What do proposed browser metrics actually measure? | Browser timing, lifecycle, interaction, memory and derived scores | Specification versus implementation/reference version; units, scope, aggregation, absent versus zero, construct non-equivalence |
| R2 | What can instrumentation capture, and how can observation alter execution? | Browser APIs, CDP, traces, automation; native instrumentation only for transferable mechanisms | Profiling off/on, tier/sham, alternative capture; observability, missing events, perturbation, bias and overhead |
| R3 | To which workloads and users can synthetic observations transfer? | Live/replayed pages, automated agents, field populations and benchmark workloads | Headless/headful, stateful/stateless, vantage point, lab/field; content equivalence, coverage and selection bias |
| R4 | How should repeated performance measurements represent uncertainty? | Nested browser runs and methodological analogues | Repetitions within/across sites, sessions and blocks; dependence, drift, variance, tails, precision and stopping validity |
| R5 | What constitutes reference-tool conformance or agreement? | Matched browser metrics and method-comparison procedures | Same artifact versus independent runs; bias, agreement, repeatability, tolerances and uncertainty, not correlation alone |
| R6 | What design and closest prior work bound a defensible contribution? | Fixtures, replay/live corpora and browser profiler evaluations | Randomization/blocking, crossed/nested factors, classification, independent expected effects, corpus inference and solution overlap |

## 2. Eligibility and boundaries

- Include primary empirical browser/web-performance studies, original statistical/methodological papers, standards, official tool documentation/code, benchmark/corpus methods, and authorized preprints.
- Include non-browser methods only when the exact transferable assumption or mechanism is stated; never treat analogy as browser validation.
- Include positive, null, contradictory and failure findings. Relevance is to a question/claim, not agreement with the proposed architecture.
- Reviews and tutorials may identify originals or contextualize terminology; they do not replace an available original for decision-driving claims.
- Date window: database inception through **2026-10-25 inclusive**; no lower bound because foundational measurement/agreement methods predate browser APIs.
- Mutable documentation: capture access date, page revision/release and implementation version; an undated live page is not proof of historical behavior.
- Language: English full texts, or an original accompanied by an authorized English translation. This is a resource limitation, not a quality criterion; log language exclusions and possible bias.
- An English abstract with inaccessible/non-English body remains abstract-limited. Do not infer full-text methods or numerical findings.
- Exclude unrelated performance domains without an explicit transfer rationale, marketing-only assertions and non-original retellings as primary evidence. Unresolved identities remain pending.
- No full text is an access disposition, not evidence of irrelevance. Retain unresolved critical sources with a blocker; do not silently exclude them.
- No publication venue, citation count, open-access status or result direction is an automatic quality threshold.

## 3. Identity, ownership and records

Allocate IDs monotonically; never recycle or renumber after sorting. Existing prose IDs remain aliases until reconciled by the canonical owner.
Before allocating, check the relevant owner for an existing ID. Simultaneous editors reserve disjoint ranges with the orchestrator.

| ID / entity | Convention | Canonical owner |
| --- | --- | --- |
| Claim | `C-T1.1-001` through topic-specific sequences; cross-topic claim keeps its first ID. Existing `C-001`–`C-008` remain coarse claim-family aliases, not substitutes for atomic passage-level claims | Zotero Verification Queue: exact wording, support disposition, access state and blockers |
| Decision | `D-001`; retain historical decision label as alias | Decision Log: alternatives, rationale, dependencies, scientific/approval status |
| Blocker | `B-001`; one blocker can affect several claims/decisions | Zotero Verification Queue: gate/blocker register and gate states |
| Source/work | `S-0001`; independent of topic, collection and mutable metadata | Source inventory: canonical work, versions, records and aliases; reuse existing canonical topic inventory |
| Search operation | `Q-001`; screening event `E-0001`; QC event `QC-001` | Search and Screening Log: execution, counts, screening and recheck events |

Source notes own extraction and design-specific appraisal, not competing workflow statuses.
The matrix synthesizes checked claims; Evidence Map summarizes decision relevance. Both point to queue IDs rather than declaring independent completion.
Phase-zero summaries and memory are dated mirrors, not alternative status owners. This file defines rules, not live gate status.

Each S-ID maps to Zotero **library type/ID + item key**, all duplicate keys, DOI/other persistent ID, title/authors/year, canonical note and inventory.
If Zotero is unavailable, assign a provisional S-ID with local path/DOI and an identity-resolution task; missing local PDF does not establish library absence.
Never use an attachment key as the work identity. Record attachments, checksums where available, version dates, pagination and access separately.
Merge duplicate records through an alias crosswalk, without deleting records. Related but substantively different works retain separate S-IDs.
Preprint/accepted/published versions normally share a work ID; preserve differing results/passages and do not count versions as independent studies.
Corrections/retractions take precedence for affected claims; log the relationship and reopen decisions as necessary. No library mutation is authorized here.

## 4. Seed audit versus collection census

The T1.6 report's **16 priority works** form a bounded seed audit, not a census of a Zotero collection or a verified source count.
Before processing, transcribe the 16 labels and resolve identities in the T1.6 inventory; retain ambiguous references as unresolved, not invented works.
Identify its NIST references separately, then deduplicate against canonical WProf, Kalibera–Jones, Mytkowicz, Georges and Hantke notes.
Prioritize SPDY, Mahimahi, Butkiewicz, Jueckstock and Zeber for critical design claims, without assuming their contents are verified.
For an actual collection census, first discover library and collection ID, enumerate every page, and preserve raw item keys, retrieval time and count.
Report collection records, attachments, duplicate records and distinct works separately. An incomplete/paginated listing is a partial enumeration.
Local inventories may guide reconciliation but cannot substitute for a current observed Zotero census. Log any actual discovery as its own operation.

## 5. Prescribed discovery searches

All searches below are **NOT RUN** at freeze. Record the exact submitted string, platform URL/API parameters, timestamp, filters, sort and inspected window.
Use Google Scholar (`https://scholar.google.com/`) and OpenAlex works API (`https://api.openalex.org/works`) as complementary discovery platforms.
Scholar: enter the literal expression below, relevance sort, no lower year, custom upper year 2026; screen out post-cutoff records explicitly.
Inspect first 50 displayed records per expression or all if fewer; disable patents and citation-only records. Log displayed estimates separately from retrieved records.
OpenAlex: use the corresponding plain-text `search` value below, `filter=to_publication_date:2026-10-25`, `sort=relevance_score:desc`, `per-page=50`, `page=1`.
URL-encode parameter values without changing their text; preserve request URL/response metadata. No API language filter; apply language eligibility during screening.

| R | Google Scholar exact expression | OpenAlex exact `search` value |
| --- | --- | --- |
| R1 | `"web performance" "metrics" "semantics"` | `web performance metrics semantics` |
| R2 | `"browser" "instrumentation" "overhead"` | `browser instrumentation overhead` |
| R3 | `"web performance" "synthetic" "representative"` | `web performance synthetic representative` |
| R4 | `"benchmarking" "repeated measurements" "uncertainty"` | `benchmarking repeated measurements uncertainty` |
| R5 | `"method comparison" "agreement" "replicate measurements"` | `method comparison agreement replicate measurements` |
| R6 | `"web performance" "experimental design"` | `web performance experimental design` |

Run the following six official-document discovery queries in Google Web Search (`https://www.google.com/search`), literal strings, no language/date UI filter, first 20 organic results each.
Exclude advertisements; preserve ranked URLs and actual retrieval count. Apply cutoff/version checks during screening, not by assuming current search ranking proves currency.

| R | Exact Google Web Search query |
| --- | --- |
| R1 | `site:w3.org/TR/ "timing" "PerformanceEntry"` |
| R2 | `site:chromedevtools.github.io/devtools-protocol/ "Tracing"` |
| R3 | `site:developer.chrome.com "CrUX" "methodology"` |
| R4 | `site:usenix.org "benchmarking" "variance"` |
| R5 | `site:developer.chrome.com "Lighthouse" "variability"` |
| R6 | `site:itl.nist.gov/div898/handbook/ "randomized block"` |

For closest-solution/disconfirming discovery, run these five additional Scholar expressions with the same 50-record rules before G4:

1. `"browser" "profiler" "conformance"`
2. `"web performance" "interaction" "lifecycle"`
3. `"web performance" "diagnostics" "scoring"`
4. `"Lighthouse" "repeatability" "comparison"`
5. `"web performance" "statistical" "uncertainty"`

Each yields an explicit comparison against the corresponding candidate, including closest solution, remaining difference and possible falsifier.
These narrow queries have known vocabulary/ranking bias. Add synonyms only through a logged amendment; bounded completion is not proof of novelty.

## 6. Retrieval, citations, stopping and access failure

Discovery identifies candidates; retrieval obtains a known work/version. Keep these operation types and their counts distinct.
For each seed or retained decision-critical missing text: search Zotero exact title, then DOI, then author/year; verify identity manually despite semantic matches.
Try the publisher/DOI landing page, then official venue or author/institution repository. Maximum three retrieval routes per work per round; log URLs, errors and versions.
An authorized alternate manuscript is usable only within its checked boundaries. Request an export/attachment if unavailable; never invent a successful read.
Do not bypass access controls. After the three routes, open an access blocker with next owner/date; repeat only when access or identity information changes.

Citation pass is finite and performed once after initial screening:

1. Freeze the pass-anchor list: included seed works plus at most the first S-ID-sorted decision-critical new work per R1–R6 (maximum six additions).
2. Backward: inspect the complete reference list for each anchor; record reference count, screened entries and exclusions. Unreadable lists remain access-limited.
3. Forward: Scholar “Cited by” for each anchor, relevance sort, first 50 records or all if fewer, upper year 2026 and manual cutoff check.
4. Screen newly found records, deduplicate, and retrieve eligible critical texts; do not recursively citation-chain those new works in v1.
5. If Scholar citations are unavailable, use OpenAlex `filter=cites:<anchor OpenAlex ID>,to_publication_date:2026-10-25`, `sort=cited_by_count:desc`, `per-page=50`, `page=1`; record changed ranking/coverage.

For other unavailable Scholar searches, use OpenAlex with the same plain terms (remove quotation marks only), above date filter and first 50 rule; label a substitute, not an equivalent replication.
If OpenAlex is unavailable, use Scholar with the exact corresponding plain terms, above filters/window; retain the failed operation separately.
If Google Web Search is unavailable, use Bing (`https://www.bing.com/search`) with the same literal query and 20 organic result limit.
Attempt one retry on a later recorded date for transient failures; do not loop indefinitely. If both primary and fallback fail, record an access/resource stop and affected R/claims.
For an unknown forward-citation identity, log identity unresolved rather than submitting a guessed OpenAlex ID.

Stop when all prescribed operations and the single citation pass have dispositions, and every retained critical claim has support/appraisal/QC or a finite blocker.
Also stop at a documented platform/access/resource limit with actual inspected counts and a coverage deficit. Reaching a cap or limit does not establish sufficiency.
Unresolved critical deficits block relevant gates; they cannot be converted to “no competing work found.” A second pass or expanded window requires amendment.

## 7. Screening, exclusions and count reconciliation

Deduplicate each batch against the work crosswalk before screening; retain every occurrence's search/rank/record ID and version linkage.
Stage 1: title/abstract/metadata screen against R1–R6 and eligibility. If uncertain, advance; record reviewer, date and reason.
Stage 2: inspect full text for relevance, source type, design and usable claim boundaries. Record include, exclude, or awaiting text/identity.
An included abstract-limited record is discovery/context only unless its exact limited statement is all that is claimed; it cannot close a methods blocker.
Retain screening history when decisions change; record old/new reason and affected IDs. Reviewer conflicts go to the scientific reviewer, unresolved items stay pending.

| Code | Primary exclusion reason (one per excluded work; apply first applicable) |
| --- | --- |
| X1 | Outside date window |
| X2 | Ineligible full-text language/translation |
| X3 | Outside all six questions/no defensible transfer |
| X4 | Ineligible source type/non-original retelling for primary-evidence purpose |
| X5 | Full text does not address the target phenomenon/claim |

Duplicates are `DUP`, not exclusions; unresolved identity is `ID-PENDING`, unavailable text is `FT-PENDING`, not X5.
Log one stage-specific primary code plus a plain-language explanation; preserve secondary reasons as notes.
Counts per batch: retrieved occurrences = duplicate occurrences + newly registered unique works (including unresolved provisional identities).
Unique works = stage-1 excluded + stage-1 pending + advanced; advanced = stage-2 excluded + stage-2 pending + included.
Count an included work once across topics/queries; report version/record/attachment counts separately. Any identity merge requires a dated count correction.
Unknown/not-run counts are `NR` or `unknown`, never zero. A genuine zero needs an executed query and captured result evidence.

## 8. Extraction and design-specific appraisal

Use one claim-to-source extraction block in the canonical note; link it from the queue and matrix:

> C-ID / S-ID / R-ID / extractor/date / freeze ID; exact proposed claim; original assertion versus reviewer interpretation; Zotero library/item and version/access; exact quotation or faithful passage; printed page + PDF page/section/table/figure or versioned URL heading; population/frame/sample and exclusions; browser/tool/version/hardware/network/cache/lifecycle; design, unit and repetitions; comparator/allocation; construct/metric/units/aggregation/missingness; estimator/uncertainty/assumptions; positive/null/contrary results; limitations and project transfer boundary; dependence links; support outcome; appraisal rationale; QC-event link.

Appraise the claim's design, not the paper's reputation. Use domain judgments `adequate`, `concern`, `unclear`, `not applicable`, with reasons; do not total them.

| Evidence design | Required appraisal prompts |
| --- | --- |
| Specification/documentation/code | Normative versus informative? Version/release and conformance scope? Definition versus actual supported implementation? Capture boundary or missingness ambiguity? |
| Controlled performance experiment | Independent experimental unit? Manipulation/sham fidelity? Randomization, blocking, order/cache confounding? Instrumentation effects? Uncertainty and alternative causes? |
| Observational crawl/field study | Sampling frame/selection, content equivalence, agent/user mismatch, time/vantage confounding, missingness, dependence and generalization boundary? |
| Repeated-measure/statistical method | Estimand and hierarchy? IID/exchangeability/model assumptions? Dependence/drift, optional stopping, finite-sample uncertainty and browser transfer? |
| Agreement/validation | Same construct/units and pairing? Shared artifact versus independent execution? Replicates/heteroscedasticity, reference error, justified tolerance; correlation not agreement? |
| Benchmark/replay/corpus design | Category ground truth independent of measured output? Replay fidelity, archival drift, workload overlap and representativeness? Fixture causality versus live external validity? |

Separately report methodological confidence for this claim as `higher`, `limited`, or `indeterminate`, with domain-specific rationale and transfer limits; no universal score.
Support outcome is independently **confirmed**, **qualified**, **contradicted**, or **unsupported**, following the queue vocabulary.
Before passage reading use `unassessed`; inability to access is not “unsupported.” A confirmed quotation can still have limited methodological confidence.
Ask whether sources share authors, cohort/sites/time window, dataset, code/tool infrastructure, replay capture or upstream documentation.
Record explicit dependency-group labels and links; distinguish replication from reanalysis/version reuse. Unknown independence is not corroboration.

## 9. Passage rechecks and deterministic quality control

Recheck **all decision-driving quantitative and normative claims** against the original passage, methods context and version before promotion to a gate.
Check numbers/denominators, units, comparison, qualifications, normative force and transfer; exact citation presence alone is insufficient.
Lower-priority sample: at each gate snapshot, group retained noncritical claims by topic and source type; cover each nonempty group with one source using the deterministic rule below.
Operationally, for each topic/type group select the lexicographically first S-ID and its first C-ID; if that source is already critically checked, count that check and record the link rather than silently resampling.
Freeze the sample manifest before rechecking; record group membership, selected IDs and nonselected count so another reviewer can reproduce selection.
Log checker/date, independent versus self-audit, original anchor, discrepancy, correction and resolution. Agent participation alone is not independent review.
If no independent checker is available, disclose a separate-pass self-audit and its limitation; never fill an independent-review field by inference.
Any substantive discrepancy expands checking to all claims sharing the source or extraction pattern at that snapshot; log the finite expanded list.
Distinguish `planned`, `checked-no-discrepancy`, `checked-corrected`, and `unresolved`. Only actual checked records satisfy QC requirements.

## 10. Decision rights, blockers and dependency-aware gates

Scientific owner: researcher responsible for claim/design justification; scientific reviewer checks reasoning and evidence. Record names when assigned, otherwise `unassigned`.
Approval owner: supervisor/project authority for scope, resources, permissions and ethics. Approval cannot validate unsupported science or establish novelty.
Orchestrator reconciles cross-document status/IDs and records review acceptance; authorship of these files is not evidence of that acceptance.
Queue register fields: B-ID, gate, affected C-/D-IDs, common versus candidate-specific, scientific owner, approval owner, minimum evidence, next action/date, state, closure rationale/evidence, reopening trigger.
Allowed gate states: `open`, `satisfied`, `qualified/deferred`, `approval-pending`. A draft deliverable is not a passed gate.
Deferral passes only when the affected claim is bounded, replaced or removed with an authorized scope decision; active decision-critical blockers never pass.
New contrary evidence, scope change, relevant source/tool version change or unresolved QC discrepancy reopens affected gates and dependent decisions.

| Gate | Dependencies | Required checklist before canonical owner can record passage |
| --- | --- | --- |
| G0 review-ready | None | [ ] Frozen rules/templates; [ ] baseline counts/statuses reconcile across named trackers/memory; [ ] finite register/owners; [ ] editorial checks; [ ] orchestrator review recorded |
| G1 coverage-ready | G0 | [ ] All 16 T1.6 seeds and NIST references dispositioned; [ ] retained critical design claims anchored/appraised/QC checked; [ ] source/record/row counts reconcile; [ ] no active critical design blockers |
| G2 scope-ready | G0; may run alongside G1 | [ ] Requirements/ownership mapped; [ ] candidate-selection scope resolved or explicitly bounded; [ ] required scope/resource approvals recorded, not inferred |
| G3 common-evidence-ready | G1, G2 | [ ] Common/pre-selection blockers closed or bounded; [ ] contrary/overlap searches logged; [ ] candidate-specific checks finite and assigned; [ ] critical passages rechecked |
| G4 contribution-ready | G2, G3 and shortlisted-method checks | [ ] Five candidates compared; [ ] prescribed discovery/citation passes dispositioned; [ ] closest work/falsifiers checked; [ ] requirement→claim→appraisal→decision→evaluation links; [ ] contribution approval recorded |
| G5 contracts-ready | Relevant G1–G4 evidence/scope decisions | [ ] Each approved output has versioned semantic contract or approved exclusion; [ ] units/windows/missingness/reference non-equivalences reviewed; [ ] no critical semantic blocker |
| G6 pilot-ready | G4, G5 | [ ] Parameters/allocation/failures/analysis/resource stops frozen; [ ] fixture/live/partial walkthroughs recorded; [ ] scientific review and permissions/approvals complete before collection |
| G7 main-study-ready | G6 and reviewed pilot findings | [ ] Main estimand/population/uncertainty/sample-size/stopping/exclusions/tolerances frozen; [ ] pilot separation/reuse justified; [ ] unsupported endpoints exploratory; [ ] scientific review and approval recorded |

All checklist items here are **requirements, not checked achievements**. Live states belong only in the queue. No pilot collection is authorized by this protocol.

## 11. Amendments and editorial verification

Freeze v1.0 before new evidence processing; G0 acceptance remains a separate prerequisite to downstream work.
Before changing queries, windows, eligibility, sample selection or appraisal/gate rules, append a log amendment with old/new rule, reason, author/date and affected operations/claims/gates.
Issue v1.1+ with a new freeze ID; preserve prior rule text in the amendment record or a precise diff reference. Never backdate a rule to fit obtained findings.
Urgent deviations are logged when encountered and reviewed before promotion; label retrospective changes explicitly and rerun affected work or retain the limitation.
Scientific changes require scientific review; scope/resource changes require the appropriate approval owner too. Unreviewed amendments remain proposed.
After each step inspect `git status --short --untracked-files=all`, `git diff --ignore-space-at-eol -- "task 1"`, and `git diff --check -- "task 1"`; manually read new files.
Separate pre-existing edits/line-ending issues from introduced defects. Editorial checks do not validate searches, science or gate completion.

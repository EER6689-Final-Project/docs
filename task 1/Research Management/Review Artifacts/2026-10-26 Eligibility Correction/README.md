# Sol synthesis and metadata-eligibility technical QA — 2026-10-26

**Outcome: tentative Luna totals are NOT promoted.** The conservative effective occurrence state is **94 ADVANCE / 44 X3 / 700 PENDING** across the immutable 838 rows. Only 300 OpenAlex corrective events are applied. Scholar's 538 occurrences remain pending: its semantic RQ mapping **FAILED/not completed**, its prospective freeze was missed, and exclusion/group QC was not performed.

This is **Sol AI metadata-eligibility technical QA after Luna AI**, not independent human scientific review, publisher/full-text appraisal, verified source claims, a completed evidence review or method adoption. Existing animal/human studies, native instrumentation and original statistical methods remain eligible analogues when the exact bounded transfer is identified. The current no-human-study scope restricts new collection, not the prior literature. No protocol amendment is made: this corrects semantic-filter overclaims under **ERP-2026-10-25-v1.0** and the current approved candidate-planning scope.

## Exact coverage and counts

| Cohort | Advance | X3 | Pending | Total |
| --- | ---: | ---: | ---: | ---: |
| Luna OA1 durable producer history, unchanged | 49 | 91 | 10 | 150 |
| Luna OA2 preserved producer history | 55 | 82 | 13 | 150 |
| Tentative producer OA total, not accepted | 104 | 173 | 23 | 300 |
| Sol effective OA1 | 33 | 33 | 84 | 150 |
| Sol effective OA2 | 61 | 11 | 78 | 150 |
| **Sol effective OA** | **94** | **44** | **162** | **300** |
| Scholar, semantic mapping unfinished | 0 | 0 | 538 | 538 |
| **Sol effective all occurrences** | **94** | **44** | **700** | **838** |

- **173/173 proposed X3 targets actually rechecked** against original title, the entire supplied exported abstract (or its absence/defect), date/language/type/venue metadata. Not checked only against Luna's generic explanation. **44 exclusions stand; 129 rejected: 72 advance, 57 pending. No exclusion targets left unchecked.** Each has an authored domain/transfer rationale in `Sol_item_checks.tsv` and `Sol_X3_adjudications.csv`.
- **22 additional distinct frozen sample sources** had the same original-export check; all advance (20 retain producer advance, 2 change pending to advance).
- **195/300 OA rows** therefore have actual original-export semantic QA: 64 retain their producer disposition and 131 change. These are disposition counts, not claims that every retained R mapping was unchanged.
- The **other 105 OA rows** received bounded title/date/language/type/abstract-availability and producer-map inspection, **not original-abstract semantic QA**. They stay pending; 84 producer advances are held pending rather than silently promoted, and 21 producer pendings remain pending. Exact EIDs and prior statuses are in `Sol_OA_unvalidated_semantic_QA.csv` and `Sol_QA_counts.json`. This finite expanded 300-row semantic QA is **not complete**. Pending is a QA hold, not an assertion those clearly relevant titles are irrelevant; e.g. original agreement models and rigorous software benchmarking deserve the next bounded pass.
- Counts are **occurrences, not unique works**. Identity/crosswalk, date/version, original source type and full-text language/authorized translation remain pending. An advance is stage-1 routing only, never full-text inclusion. No X1/X2/X4/X5, DUP adjudication, S-ID allocation or work merge was made.
- **All source-claim support, methodological confidence and passage-level QC remain UNASSESSED.** Metadata eligibility rationale is not source-paper validation. No new retrieval, broad query, citation pass, method selection or library operation occurred.

## Freeze, QC and deviations

`Sol_frozen_QA_manifest.json` was written **before Sol's original-text recheck**. It freezes all 173 producer X3 occurrence IDs, original input hash, producer-file hashes, and 35 provisional R/type group memberships with an exact first-occurrence-EID sample of 22 distinct sources. SHA-256: `a9c628b6f9ff72a0100fa7315fa528518f057386f7d5a1cae6b154bc2f23209f`.

The deterministic sample is **E-0203, E-0204, E-0218, E-0220, E-0240, E-0241, E-0251, E-0252, E-0254, E-0267, E-0278, E-0287, E-0310, E-0328, E-0349, E-0367, E-0397, E-0407, E-0412, E-0427, E-0432, E-0484**. Groups use explicit R tokens in producer mapping and exported source type, not retrieval-query membership. Missing producer R assignments and broad/range-like mapping are not validated by this grouping.

All 22 sample texts were actually checked; **8 of 35 producer group mappings need correction**. `Sol_frozen_group_QA_results.json` links the original-source reasoning. Occurrence EIDs and metadata types are proxies, **not** protocol section 9's canonical S-ID/C-ID claim groups. Those identities/claims do not yet exist for these occurrences. No claim QC or independent-review requirement is represented as satisfied.

After substantive exclusion discrepancies, `Sol_expansion_freeze.json` froze a **finite expansion to every OA occurrence E-0200–E-0499 (300 rows)** before further checking. Completed/uncompleted targets are separately recorded, not hidden. The corrected mapped snapshot has 42 groups in `Sol_final_group_snapshot_PLANNED.json`; its exact next sample is frozen as **PLANNED ONLY**. **Final regrouped QC remains OPEN/not performed**, and unmapped pending rows prevent claims of complete final group coverage. Earlier source checks are not falsely labeled prospective rechecks of this later snapshot.

Historical limits are preserved: OA1's earlier prospective receipt existed only in scratch, and its durable correction manifest was later prospective for its correction pass, not a retroactive receipt for the first screen. The superseded **42/105/3** OA1 preliminary observations remain history, not final counts; no old log was deleted or overwritten. OA2's manifest/handoff claims are preserved as producer observations, not independently proven freeze chronology. Scholar's manifest is explicitly retrospective; its displayed 538 snippets were not 538 completed semantic judgments. No retroactive freeze or protocol success is asserted.

## Scientific/technical overreach caught

- **Generic all-R denial was not evidence.** OA2's first two exclusions illustrate different problems: E-0350 explicitly discusses observer backaction and a score hiding leakage; E-0351 distinguishes uncertainty estimands but needs transfer clarification. They now advance and remain pending respectively, with different item-specific reasons.
- **Direct/analogous material was excluded.** Examples: WebUI corpus composition/noise (E-0201); repeated Tor crawls (E-0221); instrumentation/coverage in browser security (E-0275, E-0280, E-0282); original repeated-data uncertainty (E-0368, E-0378, E-0393); clinical repeatability/agreement (E-0425, E-0444); web response distributions and controlled overhead evaluation (E-0468, E-0483); CSS/browser animation evaluation (E-0491). These are discovery-level transfer hypotheses, not adopted methods or verified findings.
- **Export field labels overstated content.** Acknowledgements/prefaces (E-0210, E-0224, E-0238, E-0257), an error page (E-0250), proceedings/award metadata (E-0306, E-0315), contaminated HTML/text (E-0324), a contents list (E-0407), and long garbled reconstruction (E-0439) cannot support confident source-method judgments. Missing abstracts were not fabricated. E-0439's entire long supplied field was read, but no publisher full text was retrieved/appraised.
- **Correlation, aggregate similarity and reference agreement are not accuracy.** Item reasons distinguish constructs, event/object-level from aggregate agreement, common-artifact from independent execution, uncertainty from point error, and systematic from independent error. Clinical/nuclear/chemical thresholds, sample counts and numerical results are not imported into browser protocols.
- Language metadata never supplies X2. English snippets/abstracts do not prove English bodies. Export dates are not original-version verification. Source/platform IDs remain provisional identity anchors; no normalized-title merges or independent-study counts are inferred.

## Durable files and interpretation

- `OA1/` — already durable producer manifest/overlay/QC/handoff; **not overwritten**.
- `OA2/` — all five supplied actual scratch files copied durably: `overlay.csv`, `frozen_EID_manifest.csv`, `qc.json`, `qc_exclusions.json`, `handoff.md`.
- `Scholar/` — all four supplied actual scratch files copied durably: `overlay.csv`, `manifest.json`, `qc_counts.json`, `handoff.md`. No nonexistent exclusion/group-QC files fabricated.
- `Sol_item_checks.tsv` — 195 authored per-source original-export decisions/rationales. Script joins never make semantic decisions.
- `Sol_OA_corrective_events.csv` — exactly 300 events **E-2000–E-2299**, allocated in immutable OA input order to targets E-0200–E-0499. Producer events E-1100–E-1399 remain history, never reused as new checks. Administrative pending events explicitly say semantic QA unreviewed.
- `Sol_effective_state_838.csv` — every immutable original field preserved, plus separate **`effective_*`** columns. Use those columns for this conservative snapshot; original `stage1_*`, `canonical_*` and other fields remain history, not competing current decisions. Only validated OA decisions and explicit unresolved holds are applied; Scholar producer R1–R6 boilerplate is not inherited as semantic mapping.
- `Sol_X3_adjudications.csv`, `Sol_OA_unvalidated_semantic_QA.csv`, `Sol_QA_counts.json` — exact checked/rejected/held cohorts and reconciliation.
- Freeze/group/expansion receipts — selection and actual-vs-planned QA boundaries above.
- `Sol_file_manifest.json` — SHA-256, bytes and exact declared row-count basis for **each actual file** in this subtree except its self-referential manifest. CSV counts exclude headers; JSON object counts/text line counts are not source/work counts.
- `freeze_sol.py` and `build_sol_artifacts.py` — audit/reproduction helpers confined to this subtree. Do not rerun the freeze over existing receipts. The builder validates joins/IDs/hashes/counts and preserves original fields; it does not establish scientific validity.

Original queue SHA-256 remains `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`. Source discovery artifacts, notes/PDFs, shared trackers, library, staging and commits were not changed by this task. Existing changes by other sessions are not reverted. **Common B-010, G3 and G4 remain OPEN** because canonical identity, citation and full-text requirements are still pending; no gate file was edited.

Mechanical verification passed: source/durable byte equality for all nine copied receipts; frozen producer hashes; 300 target joins and ordered corrective IDs; all original field values in 838 effective rows; 538 Scholar pending rows with no inherited semantic RIDs or corrective IDs; UNASSESSED support/confidence throughout; every manifested file hash; authored text whitespace. Repository-wide `git diff --check -- "task 1"` also reports existing trailing-whitespace/line-ending issues in other sessions' research notes outside this subtree; those files were not repaired or changed here. Mechanical integrity does not establish scientific validity.

## Orchestrator integration paragraph

Sol's 2026-10-26 AI metadata technical QA supersedes tentative Luna OA eligibility totals only within this additive artifact snapshot: all 173 proposed X3 occurrences were checked against original exported text, 44 retained and 129 rejected (72 stage-1 advances, 57 pending); 22 frozen sample sources also advance. With 105 other OA occurrences held pending for unfinished semantic QA and all 538 Scholar occurrences still pending after failed itemwise mapping/missed freeze, the 838-occurrence effective state is **94 advance / 44 X3 / 700 pending**. Preserve producer history and use corrective events E-2000–E-2299; do not present 300 OA or 538 Scholar as fully validated semantic reviews, 42 final groups as QC-passed, AI coordination as independent human review, or advances as verified works/full-text inclusions. Support/confidence remain UNASSESSED and B-010/G3/G4 stay OPEN. Next work is the finite 105-row OA original-text QA, clarification of 57 rejected exclusions, final regroup QC, and genuine Scholar itemwise semantic review, without implying authorization for new broad queries, citations, method adoption or library mutations.

# Sol OA completion — 2026-10-26

## Outcome and integration boundary

**105/105 actual original-export semantic checks completed; none unreviewed. Accepted: 95 ADVANCE / 1 X3 / 9 PENDING.** These are occurrence-level stage-1 dispositions, not unique works or full-text inclusions. The new conservative `effective_state_838.csv` is **189 ADVANCE / 45 X3 / 604 PENDING**, using only the immutable root Sol baseline plus this disjoint 105-row correction. **Scholar's 538 occurrences are still pending here.** No later Scholar overlay is integrated; the orchestrator owns any combination with other sessions.

| Scope | Advance | X3 | Pending | Total |
| --- | ---: | ---: | ---: | ---: |
| Immutable root baseline | 94 | 44 | 700 | 838 |
| This cohort before completion | 0 | 0 | 105 | 105 |
| This cohort after actual checking | 95 | 1 | 9 | 105 |
| Delta to baseline | +95 | +1 | -96 | 0 |
| New conservative snapshot | 189 | 45 | 604 | 838 |
| OA subset in new snapshot | 189 | 45 | 66 | 300 |
| Scholar, untouched | 0 | 0 | 538 | 538 |

The remaining 604 pending occurrences are **57 earlier OA unresolved + 9 completion OA unresolved + 538 Scholar**, disjoint cohorts. All original 44 X3 and all 195 earlier OA effective decisions are unchanged. This task has no authority to re-adjudicate that earlier batch.

## What was actually checked

Sol read every target's original title, entire exported abstract/snippet field (including absence/defect), date/language/type/venue and associated metadata, and compared Luna's disposition, R mapping and rationale. `item_checks.tsv` supplies 105 individually authored semantic rationales. `original_export_targets.csv` preserves those exact 105 original queue rows; `overlay.csv` links each original row, producer judgment and new decision. Scripts perform joins/counts, not semantic decisions.

Luna's 91 advance / 14 pending / 0 X3 becomes 95 / 9 / 1: **87 advance retained; 8 pending→advance; 5 pending retained; 4 advance→pending; 1 pending→X3**. Thirteen dispositions change; every rationale is item-specific, including cases where the disposition or explicit token remains the same. Token-level mapping changes are enumerated separately in `counts.json`; a changed token set is not automatically a producer error (some add justified secondary questions).

- Pending→advance: E-0261, E-0296, E-0313, E-0322, E-0329, E-0332, E-0347, E-0455. Direct title-level profiling/measurement/workload leads are routed without inventing abstracts. Synthetic benchmark methods and the animal-study design assistant have explicitly bounded methodological transfer. Reviews are context/original-source discovery, not substitutes for primary evidence.
- Advance→pending: E-0359, E-0389, E-0392, E-0433. Their absent abstracts and application-specific titles do not identify an exact reusable uncertainty/agreement mechanism. This is not a blanket clinical/native/physical-domain exclusion.
- Pending→X3: E-0452, the UHPC/concrete box-beam study. Structural web reinforcement is not Web execution, and the supplied title/metadata identify no methodological transfer to any R1–R6. This proposed exclusion was frozen before its actual second-pass adjudication. It is title/metadata stage 1 only, not an inferred full-text exclusion.
- R6 replaces vague R3/R4 routing for phase-aware browser power-management factors (E-0296), benchmark-repository design (E-0388: R3/R6) and WRF environment comparisons (E-0396). Original agreement models retain R5 with explicit replicate/dependence R4 assignments where justified; neither correlation nor mean-model similarity is treated as individual agreement.
- E-0416 is a course announcement, E-0421/0422/0423 methodological discussion/context, not automatically original models. E-0329's entire exported abstract is a life quotation; only its explicit workload-design title supports routing. E-0398 is a degree-submission statement and stays pending. E-0408's contradictory interchangeability wording, E-0411's pairing/truncated-coordinate ambiguity and E-0430's date/version discrepancy remain unresolved source checks, not silently corrected facts.

## Immutable chronology and prospective QA

1. Read repository instructions, frozen protocol, correction README and Luna receipts. No root history rewritten.
2. Wrote `target_freeze.json` **before Sol's original-text recheck**, freezing the exact 105 targets in source order, original queue hash, root baseline hash, every supplied Luna receipt hash and reserved events **E-2600–E-2704**. Original Luna E-2300–E-2404 remain history.
3. Completed the 105 itemwise checks and persisted `item_checks.tsv`.
4. Wrote `group_exclusion_freeze.json` **before the second-pass checks**, freezing the authored TSV hash, explicit R tokens, exported metadata type memberships, first lexicographic target EID per group, all nine unmapped pending rows and the sole proposed exclusion E-0452. No generic R range is parsed as membership.
5. Actually re-read the complete supplied fields for **15 distinct group sample occurrences covering all 18 nonempty mapped R/type groups**, plus **E-0452**, after that freeze. Persisted observations in `second_pass_checks.tsv`; all 18 selected group checks and the one exclusion check are `checked-no-discrepancy` against the corrected snapshot. Actual checks are not inferred from first-pass completion. Exact groups/members/selected IDs and actual-versus-planned results are linked in `group_exclusion_QA_results.json`.
6. Built a new overlay and effective snapshot, verified input hashes and original-field preservation, and persisted counts/integrity/hash receipts.

The 15 frozen group sample EIDs were **E-0255, E-0256, E-0268, E-0285, E-0288, E-0296, E-0300, E-0313, E-0329, E-0357, E-0361, E-0373, E-0395, E-0420, E-0486**. These are metadata-eligibility proxy groups only: no canonical S-IDs/C-IDs exist here. **Not claim-level QC, not independent human review, and not global 300-row group-QC completion.** The earlier 195 were not regrouped/rechecked, the earlier 57 unmapped pending remain, and nine additional unmapped pending persist here. The old root planned-group snapshot is unchanged. Luna's misparsed generic-range group manifest remains invalid history; this new corrected prospective pass does not retroactively repair its chronology.

Pending completion EIDs: **E-0262, E-0276, E-0309, E-0359, E-0380, E-0389, E-0392, E-0398, E-0433**. They were checked, not left unread; relevance/transfer remains unresolved. They do not belong to fabricated R/type groups.

## Integrity, limits and next owner

Original queue SHA-256: `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`. The root baseline and all producer/freeze files remain unchanged. Every original queue field is preserved in all 838 new effective rows. Non-target effective fields are unchanged; target histories nest baseline links, Luna events and new Sol events in `completion_history_json`. Use `effective_*` columns for current decisions; original screening columns are history. `file_manifest.json` hashes every deliverable in this new subtree except itself, with counts explicitly labeled as file rows/lines rather than works.

**Claim support, methodological confidence and source-claim QC remain UNASSESSED.** Identity/crosswalk, original-source date/version/type and full-text language/authorized translation remain pending. Full text and citations are **NOT RUN**. No X2, new SID/work, merge, broad search, retrieval, library mutation, method adoption, novelty judgment, shared-tracker change, staging or commit occurred. This is Sol AI technical separate-pass self-audit after Luna AI, not independent human scientific review. **B-010/G3/G4 remain OPEN.**

The orchestrator may integrate only these accepted 105 corrections, preserve this conservative Scholar state until separately authorized reconciliation, and report partial metadata group coverage. Next bounded work is resolving the 66 OA pending mappings and a valid global grouping snapshot/recheck, alongside identity/source/passage requirements; this handoff does not authorize new discovery or gate closure.

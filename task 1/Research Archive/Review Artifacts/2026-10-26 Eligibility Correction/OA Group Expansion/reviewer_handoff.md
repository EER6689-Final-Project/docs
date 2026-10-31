# OA affected-group expansion — completed delta, unresolved leads retained

## Outcome and actual bounds

**Sol AI technical review, not independent human review.** All **130/130** frozen targets were actually read from the immutable Discovery `REVIEWQUEUE.csv`: exported original title, entire supplied abstract field or recorded absence, abstract status, bibliographic metadata, dates/language/type and identifiers. This includes the entire long malformed E-0439 field and the incomplete E-0468 field, without repairing or completing either. No primary target is unreviewed.

There are **151 affected positive R/type memberships**, not 151 distinct papers. Final mapping results after secondary correction are **87 supported / 44 unclear / 20 outside the affected question**. “Supported” means a bounded abstract/export-level relevance or explicitly stated methodological analogue, never a verified source claim, full-text method, performance number or browser validation. “Outside” is a mapping-specific result, **not X3**.

The 130 corrective events are **E-3500–E-3629 in the exact existing expansion-freeze target order**. No new mapping, S-ID, duplicate merge, exclusion or X3 proposal was created. Other mappings are explicitly **inherited/unrevalidated**, not silently reauthored as six negative judgments.

## Deliverables and import boundary

- **Import candidate:** `overlay_130_final.csv` — one delta row per target, corrected explicit positive RIDs, separate supported/unclear/outside affected RIDs, preserved inherited mappings, routing, authored reasoning, read receipt and original-record digest.
- `overlay_130.csv` and `primary_results_freeze.json` preserve the original frozen primary output. They intentionally show the pre-QA 88/43/20 results and are **not** the final import candidate.
- `secondary_corrections.json` records **E-0483/R4: supported → unclear**. ANCOVA without specified covariates, replicate units, dependence assumptions or uncertainty output was an overpermissive transfer. Inherited R6 and ADVANCE remain; the lead is not excluded.
- `final_counts.json`, `final_group_results.json`, `secondary_QA_results.csv`, `completion_checkpoint.json` and `output_manifest.json` give final counts, exact memberships, actual QC, durable checkpoint and hashes.
- `authored_primary_*.json`, `authored_secondary_*.json`, `authored_pattern_QA.json` contain actual authored checks. Read receipts retain complete emitted source fields and timestamps. Emission timestamps are not semantic-reading durations or live source-access/publication times.

**Nothing was promoted or merged.** The frozen input remains Snapshot 3. The user reports Snapshot 5 now incorporates disjoint Scholar work (375 ADVANCE / 59 X3 / 404 PENDING); this agent did not read, edit or independently validate Snapshot 5 or Scholar QA. The orchestrator must validate row preconditions against its current OA rows and apply this as a 130-row delta, never replace current state with Snapshot 3.

Within these 130 targets, proposed routing changes **110 ADVANCE / 20 PENDING → 106 ADVANCE / 24 PENDING**. The four ADVANCE → PENDING targets are **E-0267, E-0271, E-0357, E-0377**: their only existing positive mappings became unclear. They are retained retrieval leads, not excluded. All prior PENDING statuses stay PENDING even where a mapping is supported.

## Prospective secondary QA: planned versus actually done

After primary completion, `secondary_freeze.json` prospectively selected **63 targets**: every one of the **55 changed positive-mapping sets**, plus first EID per nonempty corrected affected R/type group. No new exclusions existed to add. All **63/63** were actually reread and separately authored: **22 checked-no-discrepancy / 1 checked-corrected / 40 unresolved**. “Unresolved” here is an executed source check that still cannot resolve a mapping, not an unread target.

The E-0483 discrepancy then triggered `secondary_pattern_expansion_freeze.json`, persisted **before** two additional R4-only rereads. **E-0361 and E-0458 were both actually checked (2/2)**: the former explicitly identifies repetition levels; the latter explicitly contrasts all erratically varying observations with a selected 90% subset. These have concrete hierarchy/selection mechanisms, unlike merely naming an adjustment model. E-0352 and E-0469 had already been secondarily checked, so this covers the complete remaining positive R4/conference-paper group without repeating their completed reads. E-0483's removal does not change that group's first positive EID, E-0352.

Total secondary unique targets: **65**. The other **65** targets have primary checks only, not invented secondary passes. There are **zero unreviewed targets in either frozen secondary list**. The finite conference-R4 pattern check is complete; this is **not** proof that every positive mapping in other groups, inherited mapping or whole OA population has passed QC.

## Final affected groups

| R | Raw type proxy | Supported | Unclear | Outside |
| --- | --- | ---: | ---: | ---: |
| R1 | conference-paper | 4 | 6 | 3 |
| R1 | dissertation | 3 | 0 | 1 |
| R2 | book-chapter | 0 | 0 | 1 |
| R2 | conference-paper | 15 | 3 | 3 |
| R2 | preprint | 4 | 1 | 1 |
| R4 | article | 41 | 17 | 3 |
| R4 | conference-paper | 4 | 4 | 1 |
| R4 | dataset | 0 | 1 | 0 |
| R4 | preprint | 3 | 4 | 5 |
| R5 | conference-paper | 1 | 2 | 1 |
| R6 | book-chapter | 0 | 1 | 0 |
| R6 | preprint | 12 | 5 | 1 |
| **Total** | | **87** | **44** | **20** |

These are **raw metadata grouping proxies**, not verified source-type eligibility. Missing language/venue metadata is explicit in the overlay; any inference dependent on unknown metadata remains unclear. Original identity, date/version/cutoff, full-text language/translation and source-type/primary-evidence fit remain **PENDING for every record**.

## Remaining limits and actions

1. Retain all **44 unclear affected mappings** as explicit unresolved questions; retrieve originals rather than treat missing abstracts as irrelevance. `final_counts.json` supplies the exact target-to-R list.
2. Preserve the prior global **42 groups: 30 supported / 12 held** as historical results. Do not rewrite them to all-pass. This expansion does not revalidate all 300 OA rows, earlier exclusions, unselected positive mappings or the broader inherited-transfer pattern. Examples of inherited mappings still needing their own prospective treatment include E-0308/R3/R6, E-0382/R1, E-0419/R5 and E-0439/R1/R5; they were not silently corrected here.
3. Apply the reviewer's schema recommendation **only in a new orchestrator-owned snapshot**: replace the six unauthored `NOT MAPPED IN THIS SNAPSHOT` placeholders with an explicit unavailable/not-separately-recorded representation pointing to the existing mappings/rationale. Do not invent six authored judgments or edit immutable old CSVs. This subtree makes no schema edit to shared data.
4. Full-text and citation passes are **NOT RUN**. Source-claim support and methodological confidence are **UNASSESSED** throughout, including apparently familiar statistical papers. All G3/G4 gates remain **OPEN**. No library, original file, accepted CSV, shared tracker, stage or commit was changed by this agent.

## Integrity and interruption record

- Queue SHA-256: `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`.
- Snapshot 3 SHA-256: `089dad4d37ae783362d376c9d20d3daff2f63eebcf8f009a020cdeb96e60e536`.
- Existing prospective freeze SHA-256: `9952da137a1d5fafa32f22c5a198e7ace0cb2bad24daf9b16d935e4dc4206dc3`.
- The existing expansion freeze and all frozen primary-output hashes were checked unchanged; exact hashes and final artifact digests are in the manifest/checkpoints.
- Direct whitespace checks found no trailing whitespace in owned text artifacts. Repository-wide `git diff --check` reports existing findings outside this subtree; they were not repaired. `editorial_summary.json` records actual commands and outcomes, without copying unrelated research diffs into this deliverable.
- The user reported earlier network issues. **No network call was needed or made for these checks, and no network/tool interruption was observed in this agent's actual execution.** No unavailable failure time, cause or duration is invented. On continuation, completed primary reads and the first ten completed secondary reads were retained, not repeated; work resumed at secondary index 10.

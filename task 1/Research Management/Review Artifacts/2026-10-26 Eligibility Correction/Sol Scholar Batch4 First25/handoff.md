# Sol Scholar Batch 4 — first 25 metadata QA

## Outcome and integration boundary

**25 original exports checked; 25 ADVANCE / 0 PENDING / 0 X3.** This is a newly authored stage-1 routing assessment, not inheritance of producer advances. Every occurrence has six question judgments and its own bounded transfer rationale. All 25 have a specific R5 agreement-method lead; 21 also have positive R4 methodological/design-limitation leads. R4 is not positively assigned to E-0705, E-0713, E-0717 or E-0718. No positive R1/R2/R3/R6 mapping is inferred from general comparison, measurement, experimental-design words or query membership.

Apply only `effective_*` fields in `delta_overlay25.csv`, joining `occurrence_E_ID`. It preserves every original queue field verbatim plus producer history and corrective events **E-3400–E-3424**, in input E-0700–E-0724 order. Original discovery/canonical columns remain history, not alternative effective outcomes. Producer **E-3300–E-3324** is not rewritten. No disposition changes versus the producer, but rationales and question boundaries are corrected. Counts are occurrences, not unique works. The other **75 Batch 4 targets E-0725–E-0799 remain unreviewed by this task**; no combined aggregate was produced.

Protocol `ERP-2026-10-25-v1.0`; cutoff **2026-10-25 inclusive**, unchanged. Date/version, language, identity and source type are unverified/pending for all 25. Proxies are sampling labels, not validated publication categories. No SID, DUP adjudication, merge, source claim, method selection or gate conclusion is supplied. **Support/confidence UNASSESSED; full text/citations NOT RUN.** Reviews/books/tutorials/course-like sources advance as discovery/context only, not substitutes for available original decision-driving evidence. Existing human/clinical studies are not excluded by the prohibition on new human data collection.

## Actual reads and prospective freezes

1. `target_freeze.json` records the exact 25 IDs, original queue hash and producer overlay hash **before Sol's original-export reread**. Producer overlay and handoff were inspected before that freeze, not misrepresented as original-source checks. Original queue SHA-256: `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`; producer overlay SHA-256: `1d47ab4a385e67fcfa85bc2ca7e942f4583a4f3570352220dfb06ca28e8a824b`.
2. All 25 stored original titles, **entire stored snippets**, year/date/language fields, raw metadata, labels, URLs and original duplicate annotations were printed and read. All snippets exist and are explicitly Scholar snippets, not abstracts or full text. There are **zero missing/unreadable original exports** here. Producer HTTP 403/client challenges/PDF failures do not affect their readability or establish ineligibility. This task made no online retrievals.
3. After primary assessment, `qa_freeze.json` froze all proposed exclusions (none), the completed primary overlay/judgment hashes, and **18 actual explicit R/type-proxy groups** before separate secondary rereads. First-EID selection yields **9 distinct occurrences: E-0700, E-0701, E-0708, E-0709, E-0714, E-0715, E-0716, E-0719, E-0720**. All nine original stored exports were actually reread against the corrected judgments. All 18 group selections are represented in `qa_group_results.json`.
4. `qa_expansion_freeze.json` prospectively froze a finite risk expansion for producer reference-list/fragment interpretation patterns: **E-0704, E-0705, E-0711, E-0713, E-0717, E-0718, E-0724**. All seven additional original stored exports were then actually reread. This is a documented precaution after primary producer-rationale corrections, not an invented discrepancy in the corrected primary sample.
5. `qa_results.csv` gives **16 actual separate-pass original-export checks**, all `checked-no-discrepancy` relative to the corrected primary. The other nine received primary checks only; their exact IDs are in `counts.json`. No claim of all-25 secondary QA is made. No final-positive group membership changed in secondary QA, so no unperformed regroup check is implied.

This is Sol AI technical review followed by Sol separate-pass **self-audit**, not independent human/scientific review. Metadata group coverage is not protocol section 9 canonical S-ID/C-ID claim/passage QC.

## Important producer-rationale corrections

- **E-0704/E-0720:** snippet contains MethComp/R references, not model exposition. Advance is based on the specific heterogeneous-rater/replicate agreement title alone. The two occurrences remain separate unresolved identities, not corroboration.
- **E-0705:** proposed agreement index/graphs support R5; repeated design and a specific limits-of-agreement alternative are not exported.
- **E-0716:** criterion method and replicates are stated as absent; limitation-based transfer is distinct from positive repeatability evidence. The missing prespecified clause and exact 2026 date are not reconstructed.
- **E-0717:** asymmetric parent-report/direct-measurement comparator and explicit bias are a bounded uncertain R5 lead; no repeat structure is invented.
- **E-0718:** plot differences against means versus a standard is the specific R5 lead; no R4 design is established.
- **E-0724:** the truncated correlation statement establishes neither endorsement nor warning. Advance rests on replicate-comparison designs and an open agreement/correlation question. The URL directory does not verify publication date.

## Files and verification

- `delta_overlay25.csv`: integration delta, 25 rows, original fields plus effective judgments/history.
- `item_checks.tsv`, `judgments.json`: 25 primary item checks and authored positive/limited-transfer judgments; the CSV/TSV contain all 150 R judgments.
- `target_freeze.json`, `qa_freeze.json`, `qa_expansion_freeze.json`: prospective input, group and finite expansion receipts.
- `qa_judgments.json`, `qa_results.csv`, `qa_group_results.json`: authored 16-item secondary results and 18 group-result links.
- `counts.json`, `verification.json`: exact coverage and mechanical checks, distinct from scientific validity.
- `freeze.py`, `build_primary.py`, `freeze_expansion.py`, `finalize.py`: local construction/verification helpers. Exclusive creation intentionally prevents overwriting frozen receipts; do not rerun them over existing outputs.
- `file_manifest.json`: SHA-256, bytes and declared row-count basis for every actual deliverable/helper other than the self-referential manifest.

Only this new subtree was written. No shared/root/other-batch/library files, Git staging or commits were changed. The orchestrator owns later reconciliation; no gate completion or permission for broader queries/citations is implied.

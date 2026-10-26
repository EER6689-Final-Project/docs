# Scholar Batch 4 remaining 75 — updated handoff

Protocol `ERP-2026-10-25-v1.0`, cutoff 2026-10-25 inclusive. The original 75 EID/input freeze in `target_freeze.json` and the first authored overlay for E-0725–E-0749 remain immutable history. New target selection E-0750–E-0799 was separately frozen in `remaining50_freeze.json` before the new semantic judgments. All 75 stored original titles, complete Scholar snippets (not abstracts), and exported metadata were read.

## Authored stage-1 routing

- E-0725–E-0749: **25 ADVANCE / 0 PENDING / 0 X3**, in the original first overlay. Not repeated.
- E-0750–E-0799: **41 ADVANCE / 8 PENDING / 1 X3**, authored occurrence-by-occurrence in two persisted 25-record JSON chunks and additive `overlay_remaining50.csv`.
- Across the frozen 75: **66 ADVANCE / 8 PENDING / 1 X3**. These are metadata-stage routing judgments, not source/full-text eligibility or gate findings.

Each new item has six explicit R1–R6 judgments, a bounded case-specific rationale, and original queue values retained under `producer_*` columns. ADVANCE mappings are selective: workload/network/design analogues are not called browser validation; agreement alone is not repeatability or accuracy. E-0769's tentative X3 is specifically a higher-education learning review with no stated R1–R6 transfer. Eight queue-annotated duplicate occurrences in E-0750–E-0799 remain PENDING identity, not adjudicated DUPs or merged; no identity or eligibility is inherited.

For every item, exact publication date/version, language/full-text translation and source type remain unverified; support/confidence are UNASSESSED; full text and citations NOT RUN. No online source retrieval occurred. All human/clinical studies are treated as prior literature, not new participant collection.

## Secondary QA

`secondary_remaining50_freeze.json` records the proposed X3 plus first EID from each explicit positive R-question group before the corresponding rereads; no source-type proxy group was selected because exported Scholar metadata does not adjudicate type. Five selected original stored exports were actually reread and recorded in `secondary_remaining50_results.json`, all checked-no-discrepancy. This is AI separate-pass self-audit, not independent human/scientific review or canonical S-ID/C-ID passage QC. No substantive discrepancy triggered expansion.

## Durable files

- `remaining50_freeze.json`: frozen E-0750–E-0799 inputs and IDs.
- `authored_remaining_750_774.json`, `authored_remaining_775_799.json`: incrementally persisted case-by-case judgments.
- `overlay_remaining50.csv`: additive 50-row decision overlay with all immutable original queue columns copied to `producer_*`.
- `secondary_remaining50_freeze.json`, `secondary_remaining50_results.json`: selected QA freeze and actual original-export rereads.
- `remaining50_counts.json`, `file_manifest.json`: reconciliation and file hashes.

No original/shared queue, other batch, library, stage or commit was modified. This cohort review does not establish whole-Scholar completion, gate closure, novelty, or authorization for broader search/citation work.

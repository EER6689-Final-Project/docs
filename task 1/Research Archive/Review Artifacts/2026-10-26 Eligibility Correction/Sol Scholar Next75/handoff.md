# Sol Scholar Next75 — bounded validation handoff

**Completed:** all 75 original E-0525–E-0599 title/Scholar-snippet/metadata records read and given six explicit R1–R6 judgments plus case reasoning. Events E-3100–E-3174 retain Luna E-2900–E-2974 as history. Rules: ERP-2026-10-25-v1.0; cutoff 2026-10-25 inclusive. Input hashes and ordered IDs were frozen before Sol's original-record read.

## Delta, not aggregate acceptance

- Producer: 50 ADVANCE / 25 PENDING / 0 EXCLUDE. Sol: **50 ADVANCE / 20 PENDING / 5 X3 EXCLUDE** (occurrences, not unique works).
- 21 disposition changes: 8 ADVANCE→PENDING, 8 PENDING→ADVANCE, 5 PENDING→EXCLUDE. All 75 received newly authored reasons and question-specific judgments; 75 have R-status changes. See `counts.json` and the producer/Sol fields in `overlay75.csv`.
- Removed unsupported semantics→metric, experiment/overhead→R4, protocol/tool comparison→R5, and generic intervention/instrumentation→R6 transfers. Retained exact native mechanisms: plan-loading setup cost (E-0568), dynamic probes (E-0585), live/compiler-inserted hooks (E-0591/E-0594), sampled-memory capture/cost (E-0595), and time/space perturbation (E-0599). These are bounded analogues, not browser validation.
- X3 E-0526: semantic question answering/search; E-0530: replication/object semantics with web performance in biography; E-0538 and E-0544: semantic ontology mapping; E-0547: semantic digital-library architecture. Each was reread against all six questions; no actual measurement/observer/statistical/workload-transfer mechanism is visible. No exclusion is based on access, venue, language metadata, or the word survey. Heuristic duplicate E-0544 remains a separate occurrence, not a second verified work.

## Actually executed QC

`qc_freeze.json` froze every proposed exclusion, all eight nonempty explicit positive-R/exported-type-proxy groups and their first EIDs, plus the expanded full list of 75 **before** secondary rereads. R4/R5 have no positive groups; no generic R-range extraction was used. Unclear fields are not positive memberships; all records were checked through expansion anyway.

After the freeze, all 75 original titles, snippets and metadata/identity fields were reread against the frozen Sol judgments. `secondary_notes.tsv` contains new case-specific reread notes; `actual_checks.csv` records executed checks and original anchors. Five exclusions, eight group representatives and all 75 expanded records are checked; no additional discrepancy against the Sol primary overlay was found. The immutable primary overlay remains unchanged. Primary unreviewed: **0**. Secondary unreviewed: **0**. Pending **eligibility/source-role** cases: **20**, enumerated in `counts.json`; pending is not unfinished screening or exclusion.

Luna's planned secondary QC remains **NOT RUN** in its unchanged artifact. This Sol pass is a separate-pass AI self-audit, **not independent human scientific review**. It applies only to these 75 occurrences, not the whole Scholar corpus or another batch.

## Limits and next owner

These are stage-1 routing decisions only; no abstracts, full texts, methods passages or findings were read, and snippet numbers are not verified source claims. All records had snippets, so no missing-snippet abstract fallback was required. Date/cutoff (especially year-only 2026 and arXiv 2610.22697), version, full-text language/authorized translation, source type/originality, canonical identity and duplicate relationships remain **PENDING for all 75**, including excluded occurrence metadata. Claim support and methodological confidence remain **UNASSESSED**; full-text and citation passes **NOT RUN**. No SID assignment, work merge, library operation, novelty/coverage/gate claim, commit or staging.

The orchestrator may combine this disjoint delta only after acceptance, preserving its finite scope and pending blockers. No parallel OA-completion/Scholar-Batch-3 active outputs were read or combined, and no aggregate snapshot was authored. `preservation_receipt.json` verifies unchanged queue/producer inputs; `file_manifest.json` hashes every deliverable except itself (self-hashing is not possible).

# Scholar Batch 6 — itemwise semantic stage-1 review

Protocol ERP-2026-10-25-v1.0; cutoff 2026-10-25 inclusive. Review date 2026-10-26. Exact explicit targets E-0900–E-0999 (100 occurrences) are frozen in `target_freeze.json` against REVIEWQUEUE SHA-256 `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`.

## Scope/index discrepancy

The instruction paired E-0900–E-0999 with positions 401–500. In the immutable source queue these EIDs are positions 701–800; positions 401–500 are E-0600–E-0699. To avoid overlap and honor the explicit ID scope, this batch reviewed only E-0900–E-0999.

## Results

Disposition: **11 ADVANCE / 6 PENDING / 83 X3**. Every target received itemwise title, complete stored Scholar snippet (not an abstract), supplied author/venue/year/URL/metadata reading; six independent R1–R6 judgments and a case-specific rationale are in `overlay.csv`. Positive routing is provisional; “ADVANCE” is not an eligibility/full-text inclusion. Prior human/statistical analogues are retained only with bounded transfer reasoning (not browser validation); experimental relevance is not conflated with R4 repeated-measure uncertainty, and generic comparison is not treated as R5 agreement. The six pending items are not exclusions.

The overlay carries all original REVIEWQUEUE fields unchanged and adds only `producer_*` columns. Original duplicate flags remain annotations only: no DUP disposition, S-ID, merge, or inherited eligibility was created.

## Secondary check

Before QA, `secondary_QA_freeze.json` froze all 83 proposed X3 targets and 17 explicit positive R/type-proxy groups. Their first occurrence selections were reread from the original stored exports, not online full texts. **97 unique occurrences were actually reread; all were checked-no-discrepancy** (83 proposed X3 plus 14 unique positive-group representatives, including supplemental E-0985). The original freeze’s helper nonselected-count values are invalid and not used; see `secondary_QA_freeze_errata.json`. The E-0985 accessibility-audit group was separately frozen before its reread. This is the same AI reviewer’s separate-pass self-audit, not independent human scientific review.

## Limits

Exact 2026 cutoff dates remain unresolved for year-only records; language metadata is not full-text language; source type, version and identity remain unverified. No X2 from metadata language. No full texts, citations, methods/results or claim passages were checked; claim support and methodological confidence remain **UNASSESSED**. No search, network request, canonical/library edit, shared tracker, gate, novelty claim or cross-topic reconciliation occurred.

Files and SHA-256/byte counts are in `manifest.json`; `original_stored_exports.jsonl` preserves the actual selected source rows.

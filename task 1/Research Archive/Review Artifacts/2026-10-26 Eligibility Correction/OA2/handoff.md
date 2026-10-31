# OpenAlex semantic Stage 1 handoff — DEV-DISC-001

- Input: immutable `REVIEWQUEUE.csv` (SHA-256 `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`).
- Frozen selection: OpenAlex original rows 151–300, `E-0350`–`E-0499`; manifest `frozen_EID_manifest.csv` (SHA-256 `0d8e1ac8a8ced9f0d9a3072fbd240dc2f716c3c8b790891bbb8447a40f24c692`), frozen 2026-10-26 09:46:31 +05:30.
- Review: all 150 records' title, exported abstract (including empty records), and exported metadata were read itemwise. Reviewer: GPT-6 Luna; this is an AI self-review, not independent human review.
- Overlay: `overlay.csv`; new event range E-1250–E-1399 in input order. Counts: {'X3': 82, 'PENDING': 13, 'ADVANCE': 55}.
- All 82 proposed exclusions underwent separate-pass self-audit; details `qc_exclusions.json`. First-EID-per-R/type advance self-audit is in `qc.json`. Mechanical QC preserved input hash, order and platform-ID joins.
- Full text NOT INSPECTED; citation/gate closure NOT RUN. Date, source-type, full-text language/translation and identity may remain pending. No canonical DUP merge, source IDs or work counts.
- Candidate relevance/priority is a review aid only; no G3/G4 claim.

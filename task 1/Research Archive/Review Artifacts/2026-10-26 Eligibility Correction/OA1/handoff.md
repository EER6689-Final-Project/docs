# OA1 — Luna stage-1 eligibility exploration receipt

Updated: 2026-10-26T10:51:44+05:30 local (+05:30). Protocol freeze: ERP-2026-10-25-v1.0.

## Frozen selection and provenance

Selected the first 150 OpenAlex rows by actual `source_platform` field and original REVIEWQUEUE order, target occurrence EIDs E-0200–E-0349. Review-event IDs E-1100–E-1249 preserve that order. The pre-interruption manifest existed only in scratch and is not claimed as durable. This folder's `manifest.json` is a new prospective manifest, frozen at 2026-10-26T10:48:49+05:30 before the correction pass; its SHA-256 is `2a0f9cfeea58c282c6bd7a5d7b3039880e2f73dbc206a5fb9e3aee0d19bee6d2`. It does not retroactively establish a durable pre-screen receipt for the earlier pass. Input REVIEWQUEUE SHA-256: `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`.

The first-pass itemwise title/abstract/metadata observations were retained in session context and scratch. This continuation did not reread all 150. The correction pass repaired mismatched row rationales/dispositions found during durable-overlay validation, then performed a separate exclusion check and deterministic R/type group check on retained source observations. Source exports were not modified.

## Current occurrence-level result

| Outcome | Count |
|---|---:|
| Advance | 49 |
| X3 semantic scope exclusion | 91 |
| Pending clarification | 10 |
| Total reviewed occurrences | 150 |

These are occurrence counts only; unique-work counts are not known. Original provisional decisions in these same rows were {'X3': 83, 'ADVANCE': 65, 'X2': 1, 'DUP': 1}; these are preserved, not inherited. All 150 rows retain original fields and add explicit `target_occurrence_EID`, reviewer/time/freeze, disposition, itemwise rationale, R IDs, transfer boundary and uncertainty fields.

No X1, X2 or X4 assigned. All export publication dates are on/before the cutoff; this is metadata-only and source/version dates remain unchecked. Metadata languages: en 135, es 1, blank 14; no full-text language or authorized translation checked, and metadata language was not used as X2. Source types are unverified export metadata; no X4. Any source claims, methods, confidence/support and passage QC remain unassessed. No full text was read.

## Actual QC and limits

- Separate-pass semantic recheck: A separate pass checked 92 proposed exclusions against R1–R6 using each exported title and actual abstract/status; one was promoted to contextual advance after review, leaving 91 X3 exclusions. Not a keyword filter. Row-level corrections and reasons are in `overlay.csv`; changes do not imply source-paper validation.
- Deterministic group check: `group-qc.json` records the first new EID per each of 22 final nonempty R1–R6 × exported source-type advance/pending groups, selected and checked in a separate metadata-stage pass. Self-audit only; not independent review.
- Language/source type/date verification from full text, canonical identity crosswalk, citation/broad query, full-text appraisal, and independent scientific review: not done. Uncertain records remain pending. All identity links remain provisional; no SIDs/work counts or duplicate inheritance.
- Non-browser methods are advanced only with an explicit, bounded rationale; none is treated as browser validation. Optional candidate A–E mapping is unassigned. Direct/analogue priority is in overlay for later full-text triage, not an instruction to retrieve all 615 other occurrences.

## Files and handoff

- `manifest.json` — prospective selection manifest.
- `overlay.csv` — 150-row occurrence overlay; SHA-256 `7d3b3560ce33a54c1fc7e0932750ca1e4548552b83aeedbf9a2093bf5fb73892`.
- `group-qc.json` — group sample manifest and actual-check records; SHA-256 `ceccf92e521f62447004557081b4654b316edf278113d1f4cb33ba7a870b3c2f`.
- `qc.json` — current counts, checks and blockers.

These are Luna exploration receipts only. Sol should review/synthesize canonical statuses later. No novelty claim, gate closure, repository/library mutation beyond these authorized additive receipts, staging or commit is asserted.

# Accepted eligibility snapshot 5 — 2026-10-26

**375 ADVANCE / 59 X3 / 404 PENDING** across the same 838 immutable occurrences. Current routing is in `effective_state_838.csv`; historical producer columns do not replace `effective_*` decisions. These are not independent works, full-text inclusions or verified source claims. B-010/G3/G4 remain open.

| Cohort | Advance | X3 | Pending | Accepted original-export semantic QA |
| --- | ---: | ---: | ---: | ---: |
| OpenAlex | 189 | 45 | 66 | 300/300 |
| Scholar | 186 | 14 | 338 | 225/538 |
| Total | 375 | 59 | 404 | 525/838 |

Pending comprises **66 reviewed-but-unresolved OA + 25 reviewed-but-unresolved Scholar + 313 Scholar without accepted semantic QA**. Having been read does not resolve exact dates/versions, languages, source roles, identity or all transfer questions. No new S-ID, duplicate merge, full-text appraisal, citation pass or method selection occurs.

## Disjoint accepted changes

Starting from [snapshot 4](../Accepted%20Snapshot%204/README.md), only two completed Sol corrections are added:

- [Scholar Batch 3](../Sol%20Scholar%20Batch3/handoff.md), E-0600–E-0699 / corrective events E-3200–E-3299: **92 provisional advance / eight X3**. All 100 original exports reviewed; 54 secondary rereads cover every proposed exclusion and all 34 frozen R/type proxy groups. Of 31 producer exclusions, 24 are rejected and seven retained. All ten producer DUP candidates receive individual relevance review: nine advance and E-0636 X3, with **zero identity merges**. No raw DUP label supplies exclusion or unique-work counts.
- [Scholar Batch4 First25](../Sol%20Scholar%20Batch4%20First25/handoff.md), E-0700–E-0724 / E-3400–E-3424: **25 advance**. All 25 original stored exports reviewed, with completed nine frozen group selections and seven prospectively frozen risk checks. Online full texts are not required or claimed for this metadata check. The other 75 originally frozen Batch4 targets remain unreviewed.

The delta from snapshot 4 is **+117 advance / +8 X3 / −125 pending**. Earlier accepted decisions, original fields and authored question judgments are preserved. The pending OA 130-member mapping-expansion task is **not included**. The global proxy-group result remains 30 supported/12 held, not an all-pass.

## Caught and repaired history-column problem

The Batch 3 Sol overlay reused **17 original column names** for its own administrative/semantic judgments. Some columns differ on all 100 rows; `stage1_decision` differs on 17 rows. Its protected title/snippet/raw metadata/URL/platform/date fields match the original, so this is a provenance/schema issue, not new source-text corruption. Nevertheless, treating those columns as preserved discovery history would be wrong.

`batch3_overlay_original_fields_restored.csv` is a **new derivative**: every original queue value is restored, and each overwritten Sol value is retained under `sol_authored_<original_column_name>`. The original Sol overlay, its manifest and immutable discovery files are untouched. Main snapshot integration starts from accepted snapshot 4, imports only explicitly identified corrective values into `effective_*`, and verifies **every original field/value/order in all 838 rows**. New rationale comes from the Sol-authored reason, not from relabeling original discovery reasons. No new reads or routing changes arise from this mechanical provenance repair. The receipt lists all 17 affected column names and input hashes.

Snapshot 4's explicit unknown/unauthored-question schema clarification remains intact; real authored judgments are not replaced with generic placeholders. Candidate/analogue assignments remain stage-1 routing leads, not source support or methodological confidence. All support/confidence remain **UNASSESSED**, full-text/citation passes **NOT RUN**, and date/language/type/identity holds remain. This is AI technical QA/self-audit, not independent human scientific review. No library mutation, staging or commit.

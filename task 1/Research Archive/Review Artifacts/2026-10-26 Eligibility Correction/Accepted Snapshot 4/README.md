# Accepted eligibility snapshot 4 — 2026-10-26

**258 ADVANCE / 51 X3 / 529 PENDING**, combining snapshot 3 with only Sol's completed next-75 Scholar QA (E-0525–E-0599, events E-3100–E-3174). The accepted delta is +50 advance / +5 X3 / −55 pending. Earlier snapshots and original/producer fields remain unchanged.

| Cohort | Advance | X3 | Pending | Original-export semantic QA |
| --- | ---: | ---: | ---: | ---: |
| OpenAlex | 189 | 45 | 66 | 300/300 |
| Scholar | 69 | 6 | 463 | 100/538 |
| All occurrences | 258 | 51 | 529 | 400/838 |

Sol actually completed all 75 primary checks and all 75 prospectively frozen secondary checks. Its overlay has 21 disposition changes from Luna: eight advance→pending, eight pending→advance and five pending→X3. All 75 question maps were separately authored/corrected. Five exclusions were specifically checked against all six questions; producer duplicate annotations are not inherited as work merges. Source-specific reasoning and input/QC chronology belong to [Sol Scholar Next75](../Sol%20Scholar%20Next75/handoff.md).

## Explicit schema clarification

On untouched rows, snapshot 3's six `effective_R*_judgment` placeholders said `NOT MAPPED IN THIS SNAPSHOT` even when `effective_RIDs` existed. This snapshot explicitly changes unauthored placeholders to **not separately recorded; consult existing mapping/rationale; unknown per-question judgment, not negative relevance**. This is a representation correction with **zero routing changes** of its own. Original fields, existing mapping/rationale and genuinely authored first-25 Scholar judgments remain preserved. The next-75 authored judgments are then applied. The receipt records 4,878 placeholder cells renamed before applying that overlay, not 4,878 semantic judgments.

`candidate:` in the next-75 question fields identifies a bounded stage-1 routing lead, not source-support confidence or verified methodology. `effective_RIDs` includes only those explicit candidate assignments for this cohort. Existing OA mappings remain subject to the global check's **30 supported / 12 held** result and its frozen 130-member expansion; that expansion is not included here. No generic R-range parsing or query-based relevance inference is used.

`effective_state_838.csv` preserves every original queue field/value/order, earlier accepted decisions, and histories. The receipt fixes input hashes and cohorts; the manifest fixes this snapshot's delivered files. Mechanical verification included all 14 files in the next-75 manifest and original-field/target/event/support boundaries. Metadata counts are occurrences, not unique works or full-text inclusions. Canonical identity/date/language/type, full texts/citations and global grouping remain open; support/confidence remain UNASSESSED. AI technical review/self-audit, not independent human review. B-010/G3/G4 stay open. Later active batches are not implicitly merged.

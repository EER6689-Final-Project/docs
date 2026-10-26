# Accepted eligibility snapshot 3 — 2026-10-26

**208 ADVANCE / 46 X3 / 584 PENDING** across 838 occurrences, not independent works or full-text inclusions. This is the current accepted administrative merge, superseding snapshot 2's counts without overwriting it. B-010/G3/G4 remain open.

| Cohort | Advance | X3 | Pending | Original-export semantic QA completed |
| --- | ---: | ---: | ---: | ---: |
| OpenAlex | 189 | 45 | 66 | 300/300 |
| Scholar | 19 | 1 | 518 | 25/538 |
| Total | 208 | 46 | 584 | 325/838 |

Completion means itemwise original-export metadata eligibility QA, **not eligibility fully resolved**: 66 OA mappings remain pending despite having been read. Full-text/source validation and identity/date/language/type verification are different stages. Scholar still has 513 occurrences without accepted semantic QA plus five reviewed-but-pending first-batch occurrences.

## Accepted inputs

1. [Snapshot 2](../Accepted%20Snapshot%202/README.md) contains the root accepted state plus Sol's first-25 Scholar correction.
2. [Sol OA Completion](../Sol%20OA%20Completion/handoff.md) supplies **105 disjoint** corrections, E-2600–E-2704: 95 advance / 1 X3 / 9 pending. Only those targets are copied; its untouched Scholar/root baseline is **not** merged over the accepted Scholar decisions.

The OA delta from snapshot 2 is +95 advance, +1 X3, −96 pending. Earlier 195 OA decisions, their 44 exclusions and all 25 accepted Scholar corrections are unchanged. Luna's 105-row producer proposal is superseded by Sol's 13 disposition changes and 67 explicit mapping-token changes; original producer/history files remain immutable. E-0452's metadata-level X3 was prospectively frozen and second-pass checked, not silently inferred from a missing abstract.

Sol's new OA secondary QA checked 18 nonempty explicit R/type proxy groups through 15 distinct sample sources, plus the sole proposed exclusion. **Global regrouped QC across all 300 OA rows remains unfinished**. Source-type proxies/occurrence IDs are not canonical S-ID/C-ID groups. Neither local group QA nor prior source reading certifies full-text methods or independent human scientific review.

## Files and limits

- `effective_state_838.csv`: original queue fields/order preserved; current routing uses `effective_*` fields. OA completion provenance is in `completion_history_json`; six first-25 Scholar judgments from snapshot 2 remain intact. Unmapped judgments are explicitly unavailable, not inferred from query membership.
- `receipt.json`: frozen input hashes, 105 applied target IDs, cohort/count reconciliation and exact read-coverage boundary. `manifest.json` records delivered bytes/hashes, excluding itself.
- Earlier provenance handles retain their source-file context; the receipt and stable target/event IDs identify authoritative underlying rows. Do not confuse producer columns with current states or apply the same delta twice.
- All source-claim support/confidence remain **UNASSESSED**; full-text/citation passes **NOT RUN**. Canonical identity, original dates/versions, full-text language and source-type roles remain unresolved. No S-IDs, work merges, novelty claims or gate passage are created.
- Parallel later Scholar producer/QA batches are **not included** until separately accepted. Any later snapshot must preserve this one and reconcile nonoverlapping target cohorts.

Orchestrator verified the OA completion's 15 manifested files, all original values across the 838-row merge, preservation of source-support boundaries, and independent status counts. These mechanical checks support receipt integrity, not source validity. No library mutation, staging or commit occurred.

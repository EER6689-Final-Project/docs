# Scholar Batch 7 Final 38 — actual semantic stage-1 handoff

## Outcome

Completed an actual itemwise semantic stage-1 review of exactly **38** frozen Google Scholar occurrences E-1000–E-1037 from the immutable discovery queue. Results: **22 ADVANCE / 0 PENDING / 16 X3**. Each occurrence has six separate R1–R6 judgments and an item-specific transfer/exclusion rationale in `primary_judgments.json` / `author_checks.tsv`. The complete stored title, Scholar snippet and available metadata were read for all 38; every snippet is marked and treated as a Scholar snippet, never as an abstract/full text.

ADVANCE means retain for bounded discovery/context review only; it is not inclusion, source validation, evidence support, or methods adoption. Exact date/cutoff, language/translation, source type, identity/version, SID and canonical crosswalk remain unverified. Full-text and citation checks were NOT RUN. Claim support and methodological confidence remain UNASSESSED. No gate, project-wide conclusion, or proposal acceptance follows.

## Freeze and actual QA

`target_freeze.json` prospectively froze the exact ordered 38 IDs and original queue SHA-256 `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad` before original-target reading. After itemwise assessment, `secondary_freeze.json` froze all 16 proposed X3 and first EID per each actual positive question group (R1/R2/R3/R4/R6; none for R5), before secondary reread. Four distinct selected occurrences plus the 16 proposed exclusions (20 distinct total) were then actually reread from stored original export fields; all 20 secondary checks found no discrepancy relative to the final primary judgments. No source-type groups were invented because source types are unverified. This is a separate-pass Luna AI self-audit, not independent human/scientific review.

A corrective refinement moved E-1003, E-1004, E-1023 from exclusion to bounded ADVANCE based on their explicit website measurement, human navigation, and technical web optimization/user-experience subjects. The final QA freeze and reread were repeated after that revision; the earlier interim freeze is superseded in the final receipt.

## Boundaries

- No generic R1–R6 parsing, rank-based decisions, blanket R assignments, or keyword-only exclusion. General comparison did not trigger R5; no R5 positive assigned.
- Existing human studies and non-browser methodological analogues are not automatically excluded; any transfer is bounded and explicitly stated.
- Original producer DUP labels/annotations remain verbatim in original columns. No DUP disposition, identity merge, SID allocation, or source-work identity decision was made.
- No X1 or X2 assigned; year-only Scholar metadata cannot establish exact cutoff eligibility, and no metadata language field establishes full-text language eligibility.
- No network retrieval, full text, citations, library mutation, shared/root/other-batch write, stage commit, or gate claim.

## Files

- `target_freeze.json`: prospective exact target list/source hash.
- `primary_judgments.json`: 38 occurrence-specific judgments, 228 R-question judgments, metadata limitations.
- `overlay.csv`: original queue fields preserved plus separate `producer_*` judgment columns.
- `author_checks.tsv`, `item_checks.tsv`: itemwise authors-as-exported and rationale audit.
- `secondary_freeze.json`, `secondary_reread_originals.txt`, `secondary_checks.json`: prospective secondary set and actual reread receipts.
- `counts.json`, `file_manifest.json`: counts and checksums.

Only this new `Scholar Batch7 Final38/` subtree was written. No proposal/G3 closing, whole-Scholar disposition, source identity reconciliation, or gate completion is implied.

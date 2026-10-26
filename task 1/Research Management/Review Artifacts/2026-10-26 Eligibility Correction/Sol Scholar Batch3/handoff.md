# Sol Scholar Batch3 — additive semantic correction

## Outcome and scope

Protocol **ERP-2026-10-25-v1.0**, unchanged cutoff **2026-10-25 inclusive**. Exactly **100 original occurrences E-0600–E-0699**, in frozen target order, receive additive corrective events **E-3200–E-3299**. Preserve Luna's ordered **E-3000–E-3099** history and producer files. The predecessor event labels follow the caller's reserved ordering; the producer overlay itself does not contain an event-ID column. This subtree is a proposed disjoint overlay for orchestrator combination, not acceptance or a shared-register update.

**Actual corrected occurrence routing: 92 ADVANCE, 8 X3, 0 semantic-pending, 0 accepted DUP dispositions/merges.** All 100 original complete supplied titles, Scholar snippets (**not abstracts**) and raw author/venue/year/URL/identity metadata were read. Six-question checks and source-specific reasons/transfer limits are recorded for each. Advancement includes uncertain methodological analogues and context/original-tracing sources; it does not establish primary-evidence eligibility.

Producer routing was 59 ADVANCE / 31 X3 / 10 DUP. Of the 31 proposed X3 exclusions, **24 are rejected** and **7 retained**. All 59 producer advances remain provisional advances. All 10 producer DUP rows receive independent semantic routing: **9 advance; E-0636 receives X3**.

Rejected producer exclusions, each now provisional ADVANCE:

E-0608, E-0630, E-0640, E-0649, E-0650, E-0659, E-0664, E-0672, E-0673, E-0674, E-0675, E-0676, E-0677, E-0679, E-0680, E-0681, E-0683, E-0684, E-0685, E-0688, E-0689, E-0691, E-0692, E-0696.

Retained producer X3: **E-0617, E-0624, E-0646, E-0665, E-0682, E-0686, E-0697**. Additional semantic X3: **E-0636**, formerly producer DUP. These eight have explicit R1–R6 reasons and an explicit no-defensible-transfer rationale; neither animal subject matter nor non-browser origin is itself an exclusion. Experimental language is not an R4 assignment; protocol/algorithm comparison and ranking correlation are not R5 agreement. In particular E-0669 is routed R6 rather than the producer's R4/R5; E-0695 is R6 rather than R4.

## Identity is separate

All **10 heuristic duplicate candidates remain UNADJUDICATED** with their original candidate target and factual occurrence flag preserved. No author/edition/DOI reconciliation, canonical linkage, work merge, new S-ID or independent-work count is authorized or asserted. All **100 canonical identities remain unverified**. E-0636's X3 is its own semantic decision, not inheritance from E-0617. The 100 rows are occurrences, not 100 distinct studies. Raw title/year/author/venue/URL fields are preserved as factual discovery metadata, not certified bibliographic facts.

## Actual review and QA

1. `input_freeze.json` froze all 100 exact target IDs, event IDs and input hashes before original semantic reads. Original queue SHA-256: `92b984c89cf89ecdd8fe5970108e668e67f36cbfcbe4db08900af6d8032c10ad`.
2. `author_checks.psv` contains 100 hand-authored mappings, source-type proxies, source-specific reasons and bounded transfers. `primary_itemwise_checks.json` records the original full supplied text, producer reason and six-question primary checks. No keyword filter generated the decisions.
3. Only after primary checks persisted, `secondary_QA_freeze.json` froze the union of **31 producer exclusions + 8 Sol exclusions = 32 distinct critical occurrences**, plus lexicographically first E-ID in each of **34 explicit corrected R/type-proxy groups**. Explicit tag lists are used, not range parsing. Outside-all-six/type groups are also represented.
4. **54 distinct original records were actually reread** after that freeze. `secondary_author_checks.psv` records the separate-pass reasoning, including explicit six-question reassessment for all producer/Sol exclusion candidates. `qc_results.json` links each checked record and all 34 selected groups. **0 additional substantive discrepancies** were observed against Sol's primary decisions; no additional pattern expansion was required or claimed. The producer errors were already covered by the critical list. **46 other records had primary review but were not selected for secondary reread**; this is not a 100-row secondary audit.
5. `overlay.primary.csv` preserves the exact pre-secondary overlay bytes hashed in the freeze. `overlay.csv` is the final 100-row delta with secondary-status annotations. `preservation_receipt.json` verifies all frozen producer/protocol/queue hashes unchanged and all 100 raw occurrence field sets preserved. `qc_counts.json` owns the exact local count reconciliation. Scripts serialize the authored judgments and perform structural checks, not scientific validation; do not rerun them over frozen results.

This is **Sol AI technical review after Luna AI, followed by Sol separate-pass self-audit**, not independent human/scientific review. Every exclusion candidate was critically reread, but no claim passage was checked.

## Unfinished work and limits

- **Full-text and citation passes: NOT RUN. Claim support and methodological confidence: UNASSESSED.** Full-text inclusion and independent-work totals are not adjudicated.
- Exact publication date/cutoff eligibility, full-text English/authorized translation, source type/originality and identity/version remain **unverified for all 100**. No X1/X2/X4 is inferred from metadata. Source-type labels are grouping proxies only.
- Many restored candidates are deliberately uncertain. For example E-0673's sensitivity cause and E-0696's yearly-versus-repeat distinction are truncated; advancement requests inspection rather than asserting a validated transfer. Context sources cannot substitute for available originals in decision-driving claims.
- Next owner: orchestrator for acceptance/combination; scientific reviewer for unresolved relevance/design judgments; identity/full-text reviewers for bibliographic, language, date and source-type checks. No date or named human reviewer is invented.
- No library mutations, canonical merges, shared/root tracker edits, gate/novelty conclusions, study adoption, staging or commits. No parallel `Sol Scholar Next75/` or OA output content was read or written. Only this new subtree was written.

`file_manifest.json` hashes every other file in this subtree; it intentionally cannot hash itself. Input preservation is separately checked against the prospective freeze.

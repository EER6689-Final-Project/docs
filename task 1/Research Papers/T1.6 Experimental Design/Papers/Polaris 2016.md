# Polaris: Faster Page Loads Using Fine-grained Dependency Tracking

## Identity and access

- **S-0014**, R2/R3/R6. **Ravi Netravali, Ameesh Goyal, James Mickens, Hari Balakrishnan**. NSDI 2016. James Mickens is visible on the original cover; missing library creator metadata must not remove him from citations. No DOI guessed.
- My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), work **HA26TRBU**, attachment **HMSDHLG8**. Original <https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-netravali.pdf>. Local `Polaris 2016.pdf`, 15 PDF pages including cover; SHA-256 `a606465fd9ffeead1494ff02cf88fea2d07404b399e7e980f38a13a55b37b055`.
- Sol, 2026-10-25, `ERP-2026-10-25-v1.0`: reopened cover, PDF pp. 8, 10–11 and 13 in text; visual p. 11. Retained extraction below deliberately limited to pp. 8 and 11. Luna's prior pp. 1–15 read is not a Sol whole-paper review or independent human QC.

## Claim-to-source extraction

### C-T1.6-053 — Replay subset and non-equivalent lifecycle endpoint

**Proposed claim:** Polaris compares rewritten and baseline pages under replay, but cannot use ordinary `loadEventEnd` as the rewritten page's completion marker. Its operational endpoint is the time to fetch the baseline object set. Its selected corpus cannot establish general browser metric conformance.

**Exact anchors:** §3.5, proceedings p. **129**, internal p. **7**, PDF p. **8**: Mahimahi records “200 sites in the Alexa Top 500 list”; five mobile-optimized sites are included; pages using `eval()` or `with()` are excluded because the prototype does not support them. §5.1, proceedings p. **132**, internal p. **10**, PDF p. **11**: “All experiments used Firefox v40.0. Unless otherwise specified, all experiments used cold browser caches and DNS caches.” Same section, right column: “loadEventEnd is inaccurate for Polaris pages, since the event only indicates that the scheduler stub has been loaded”; baseline objects fetched between navigationStart and loadEventEnd are captured with tcpdump, and Polaris completion is the time needed to fetch those objects.

**Design/comparator/construct:** Controlled Mahimahi capture/replay with network emulation; baseline original capture versus scheduler-stub rewrite. Units are captured sites/pages and their loads, not field-user sessions. Endpoint is matched object fetching, not proof that lifecycle event semantics are equivalent. Exact repetition count/randomization and full uncertainty treatment were not established by these retained passages; no graph/table-derived improvement estimate is used.

**Interpretation:** A benchmark can legitimately change its endpoint to fit an intervention, but that endpoint must be named and cannot silently substitute for a standardized metric in a profiler-conformance claim. If profiler scope is approved, pair semantically identical metrics and preserve intervention-specific endpoints separately. This is conditional researcher inference, not a new evaluation authorization.

**Support: qualified**: endpoint and sample description confirmed; generic profiler validity unsupported by these passages. **Methodological confidence: limited** for transfer, given exclusions, historical implementation, replay and intervention-specific endpoint. Dependency group `DG-Polaris-replay`: shared corpus/capture across baseline/treatment, not independent replications. Uses Mahimahi upstream infrastructure; discusses WProf/Klotski in §3.4 (same PDF p. 8), not proof of novelty against all later tools.

## Design-specific appraisal

- Manipulation/comparator **adequate** for captured-page scheduling comparison; not a sham-instrumentation comparison.
- Selection/replay fidelity **concern**: Alexa-derived, unsupported-code exclusions, frozen capture and specialized rewrites.
- Construct/endpoint **adequate** when explicitly named; **concern** if mislabeled loadEventEnd equivalence.
- Cache **adequate** for explicit default cold-cache declaration; full state-reset fidelity not independently tested.
- Order/independent unit/uncertainty **unclear** in bounded retained read; shared capture implies dependence.
- Field transfer **concern**: neither replay nor chosen sites represent all field users.

## Passage QC — QC-053

Sol original-passage recheck, 2026-10-25, text and visual endpoint passage; separate pass after Luna, **not independent human/scientific review**. **checked-corrected**: restored original author list; precise proceedings/internal/PDF page anchors added. Retained set checked source-wide: C-T1.6-053 only; no headline numerical speedups promoted. No DOI or gate completion inferred.

## Copy receipt

Source: `/tmp/opencode/eei6689-t16-supporting/Netravali et al. - Polaris Faster Page Loads Using Fine-grained Dependency Tracking.pdf`; new target `Polaris 2016.pdf`, 777,281 bytes. Scratch original and existing `/home/mendydias/Zotero/storage/HMSDHLG8/Netravali et al. - Polaris Faster Page Loads Using Fine-grained Dependency Tracking.pdf` matched byte hashes in Sol's final check. Exact bytes preserved; source/target SHA-256 checked, no existing target overwritten.

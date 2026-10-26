# Common-evidence discovery handoff

**Review status:** bounded, read-only preparation under frozen `ERP-2026-10-25-v1.0`. G0 accepted; G1 evidence integration and G2 scope/approval work may proceed in parallel. This handoff is not G3/G4 closure or a scientific gate decision. No repository, Git, or Zotero mutations were made.

**Local execution window:** 2026-10-25T23:41:21.452669+05:30 through 2026-10-26T00:16:08.809339+05:30. Current local date is 2026-10-26. The protocol cutoff remains 2026-10-25 inclusive; no amendment was made. Exact per-request local/UTC times, URLs, HTTP status, retrieved/inspected counts, and response SHA-256 are in `operation_receipts.json` and adjacent `*.json` receipts.

## Query and Q-ID crosswalk

The Q-ID mappings below are proposed in scratch for canonical Search Log reconciliation only; the repository log was not edited. Each ID has exact request URLs/parameters in the receipt index. Q-229–Q-239 are diagnostic Scholar retrieval attempts, not part of the final prescribed windows.

| Q-ID | Operation | Exact submitted search string | Result / screening disposition |
|---|---|---|---|
| Q-200 | OpenAlex R1 | `web performance metrics semantics` | 50 fetched; OpenAlex total=92124; S1 {'X3': 41, 'ADVANCE': 8, 'X2': 1} |
| Q-201 | OpenAlex R2 | `browser instrumentation overhead` | 50 fetched; OpenAlex total=4853; S1 {'ADVANCE': 44, 'X3': 6} |
| Q-202 | OpenAlex R3 | `web performance synthetic representative` | 50 fetched; OpenAlex total=155154; S1 {'ADVANCE': 13, 'DUP': 1, 'X3': 36} |
| Q-203 | OpenAlex R4 | `benchmarking repeated measurements uncertainty` | 50 fetched; OpenAlex total=129993; S1 {'ADVANCE': 29, 'X3': 20, 'DUP': 1} |
| Q-204 | OpenAlex R5 | `method comparison agreement replicate measurements` | 50 fetched; OpenAlex total=544573; S1 {'ADVANCE': 39, 'X3': 11} |
| Q-205 | OpenAlex R6 | `web performance experimental design` | 50 fetched; OpenAlex total=1259487; S1 {'ADVANCE': 17, 'X3': 30, 'DUP': 1, 'X2': 2} |
| Q-206 | Scholar R1 | `"web performance" "metrics" "semantics"` | 50 screened from fixed first-50 window; S1 {'ADVANCE': 43, 'DUP': 7} |
| Q-207 | Scholar R2 | `"browser" "instrumentation" "overhead"` | 50 screened from fixed first-50 window; S1 {'ADVANCE': 39, 'DUP': 11} |
| Q-208 | Scholar R3 | `"web performance" "synthetic" "representative"` | 50 screened from fixed first-50 window; S1 {'ADVANCE': 40, 'DUP': 10} |
| Q-209 | Scholar R4 | `"benchmarking" "repeated measurements" "uncertainty"` | 50 screened from fixed first-50 window; S1 {'ADVANCE': 50} |
| Q-210 | Scholar R5 | `"method comparison" "agreement" "replicate measurements"` | 50 screened from fixed first-50 window; S1 {'ADVANCE': 50} |
| Q-211 | Scholar R6 | `"web performance" "experimental design"` | 50 screened from fixed first-50 window; S1 {'ADVANCE': 50} |
| Q-212 | Google Web R1 | `site:w3.org/TR/ "timing" "PerformanceEntry"` | Google returned HTTP 200 JavaScript/enable-JavaScript shell; organic results unparsed/unknown; no record-level screening. |
| Q-213 | Google Web R2 | `site:chromedevtools.github.io/devtools-protocol/ "Tracing"` | Google returned HTTP 200 JavaScript/enable-JavaScript shell; organic results unparsed/unknown; no record-level screening. |
| Q-214 | Google Web R3 | `site:developer.chrome.com "CrUX" "methodology"` | Google returned HTTP 200 JavaScript/enable-JavaScript shell; organic results unparsed/unknown; no record-level screening. |
| Q-215 | Google Web R4 | `site:usenix.org "benchmarking" "variance"` | Google returned HTTP 200 JavaScript/enable-JavaScript shell; organic results unparsed/unknown; no record-level screening. |
| Q-216 | Google Web R5 | `site:developer.chrome.com "Lighthouse" "variability"` | Google returned HTTP 200 JavaScript/enable-JavaScript shell; organic results unparsed/unknown; no record-level screening. |
| Q-217 | Google Web R6 | `site:itl.nist.gov/div898/handbook/ "randomized block"` | Google returned HTTP 200 JavaScript/enable-JavaScript shell; organic results unparsed/unknown; no record-level screening. |
| Q-218 | Bing fallback R1 | `site:w3.org/TR/ "timing" "PerformanceEntry"` | Bing HTTP 200; captured page explicitly says “There are no results”; 0 organic records retrieved (this is a query outcome, not evidence of source absence). |
| Q-219 | Bing fallback R2 | `site:chromedevtools.github.io/devtools-protocol/ "Tracing"` | Bing HTTP 200; captured page explicitly says “There are no results”; 0 organic records retrieved (this is a query outcome, not evidence of source absence). |
| Q-220 | Bing fallback R3 | `site:developer.chrome.com "CrUX" "methodology"` | Bing HTTP 200; captured page explicitly says “There are no results”; 0 organic records retrieved (this is a query outcome, not evidence of source absence). |
| Q-221 | Bing fallback R4 | `site:usenix.org "benchmarking" "variance"` | Bing HTTP 200; captured page explicitly says “There are no results”; 0 organic records retrieved (this is a query outcome, not evidence of source absence). |
| Q-222 | Bing fallback R5 | `site:developer.chrome.com "Lighthouse" "variability"` | Bing HTTP 200; captured page explicitly says “There are no results”; 0 organic records retrieved (this is a query outcome, not evidence of source absence). |
| Q-223 | Bing fallback R6 | `site:itl.nist.gov/div898/handbook/ "randomized block"` | Bing HTTP 200; captured page explicitly says “There are no results”; 0 organic records retrieved (this is a query outcome, not evidence of source absence). |
| Q-224 | Scholar candidate C1 | `"browser" "profiler" "conformance"` | 50 screened (C3 short/partial); S1 {'ADVANCE': 43, 'DUP': 7} |
| Q-225 | Scholar candidate C2 | `"web performance" "interaction" "lifecycle"` | 50 screened (C3 short/partial); S1 {'ADVANCE': 40, 'DUP': 10} |
| Q-226 | Scholar candidate C3 | `"web performance" "diagnostics" "scoring"` | 38 screened (C3 short/partial); S1 {'ADVANCE': 28, 'DUP': 10} |
| Q-227 | Scholar candidate C4 | `"Lighthouse" "repeatability" "comparison"` | 50 screened (C3 short/partial); S1 {'ADVANCE': 50} |
| Q-228 | Scholar candidate C5 | `"web performance" "statistical" "uncertainty"` | 50 screened (C3 short/partial); S1 {'ADVANCE': 42, 'DUP': 8} |

### OpenAlex execution details

Q-200–Q-205 used the exact plain-text values shown above at `https://api.openalex.org/works`, with `filter=to_publication_date:2026-10-25`, `sort=relevance_score:desc`, `per-page=50`, `page=1`. All six returned HTTP 200 and 50 works. The table reports the API `meta.count` separately from retrieved/screened count. The stage-1 export includes all 300 titles, publication date/year, type, language, authors, DOI, venue, OpenAlex ID, landing URL, and abstract when supplied. Abstract text reconstructed from `abstract_inverted_index` is expressly labelled reconstructed; absent abstracts are marked.

### Google Scholar execution details

Q-206–Q-211 are the six prescribed R1–R6 literal Scholar expressions; Q-224–Q-228 are the five prescribed candidate expressions. Requests included `as_yhi=2026`, `as_vis=1` (exclude citation-only records), and `as_sdt=0,5`; no lower-year limit was applied. Scholar served 20 records per HTTP page despite `num=50`; starts 0, 20, and 40 were captured. R1–R6 and C1, C2, C4, C5 each yielded 50 inspected records. C3 yielded only 38 record cards across the three pages (18 + 16 + 4); page estimates varied from 18 to 44 and page returns were short, so Q-226 is **partial**, not “all fewer than 50.” The CSV records 38 platform IDs/URLs and requested-offset-derived ordinals (1–18, 21–36, 41–44); gaps and the rest of the nominal 50 window remain unresolved. These ordinals reflect request offsets, not an independently verified stable ranking. No further retries were made in this handoff.

The returned HTML does not independently confirm the patent toggle state. The `as_sdt=0,5` parameter was submitted, but patent exclusion cannot be certified from these responses; this is a filter-compliance limitation retained for orchestrator review. The final Scholar windows are the `ScholarFinal_*` requests. Earlier first-10/20 and pagination requests Q-229–Q-239 are preserved as diagnostics and excluded from the final-window screening counts. Displayed estimate text is retained per page receipt; it varied across pages and is not a retrieved-record count. Scholar records have title/author-year metadata and search snippets, **not inspected abstracts or full text**.

### Official-document Google Web searches and fallback

Q-212–Q-217 submitted the six exact official-site Google Web queries, no language/date UI filters, requesting 20 organic results. Each Google response was HTTP 200 but contained an enable-JavaScript/retry shell rather than parsed organic results. This is **unparsed/inaccessible result content**, not a zero-result search. Q-218–Q-223 then submitted the same six exact strings to Bing (`count=20`); each HTTP 200 page explicitly displayed “There are no results,” with zero organic result records. Bing’s observed empty-query pages do not establish absence of relevant sources. No extra OpenAlex substitute was run because the Bing fallback returned an accessible result page. The raw Google and Bing bodies are preserved separately.

## Stage-1 screening and identity

- Final screening file: **838 result occurrences**: 300 OpenAlex records and 538 Scholar records (six R queries × 50; four candidate queries × 50; C3 × 38). Per-occurrence dispositions: {'X3': 144, 'ADVANCE': 613, 'X2': 3, 'DUP': 78}. This includes duplicate occurrences; it is not a count of independent works.
- Stage-1 decisions were made from all retrieved OpenAlex title/abstract/metadata, reconstructed abstracts clearly marked, and Scholar title/metadata/snippet only. `ADVANCE` includes uncertain records; X3 is title/abstract discovery triage, not full-text exclusion. X2 is only where OpenAlex explicitly supplied non-English metadata. The stage CSV contains the exact Q-ID, rank, platform record ID, record URL, DOI/metadata, title, abstract/snippet, stage-1 code and reason.
- Stage 2 was not performed for any newly advanced work. All advanced, nonduplicate occurrences remain `FT-PENDING`; duplicates inherit/point to their first occurrence or existing canonical work. No methods/results/full-text claims or X5 dispositions are made. Exact-day eligibility for year-only 2026 Scholar records is unresolved; they were not passed as verified within the Oct 25 cutoff.
- Local T1.6 portfolio identity crosswalk found two existing works and retained their canonical IDs: (1) Q-206 rank 6, Mahimahi, Scholar result ID `3Kk_0JiZLo4J`, to S-0003 by title; (2) Q-203 rank 12, OpenAlex `W2013901208`, DOI `10.1145/2464157.2464160`, to S-0007 (the canonical note records accepted/proceedings and published-version DOI relationship). They are marked `DUP` in the screening export; no new S-ID is created.
- Other result-level DOI/normalized-title duplicates among this export are retained as `DUP`; aggregate disposition is 78 duplicate occurrences, of which two map to existing S-0003/S-0007 and 76 are duplicate occurrences within retrieved batches. Remaining identities have **not** been reconciled against all topic inventories/context sources or a live Zotero library. The five context documents/IDs 0022–0026 were not assigned to any candidate in this pass. No S-0100+ IDs have been allocated; use those only after canonical crosswalk confirms genuinely new works.
- No exact novelty, no-overlap, source-absence, or corpus-sufficiency claim follows from ranking, hit counts, snippets, or these bounded windows.

## Explicit remaining coverage and gate limits

- Q-226 (candidate C3) remains a partial first-50 window: 38 returned/screened record cards at requested offsets 0/20/40; the output has requested-offset-derived ordinals 1–18, 21–36, and 41–44, with missing positions and no verified stable ranking. Pagination totals were inconsistent. No additional request was made. A later bounded retry, if Sol judges necessary, must be separately timestamped and retain the original operation.
- Google Web result bodies were not parsable; the Bing fallbacks were accessible but yielded observed “no results” pages. This is the documented coverage deficit for official-document web ranking.
- Patent exclusion in Scholar is not certified from returned HTML. Scholar date UI is year-level (upper year 2026), and exact Oct 25 date eligibility for year-only records remains unresolved.
- Citation pass **NOT RUN**: no anchor list frozen; backward references and forward-cited-by searches not attempted. No citation Q-ID or fake zero count.
- No Zotero census, seed audit, full-text retrieval, source extraction, passage QC, scientific-review determination, or scope approval was performed in this discovery pass. G1 integration and G2 approval baselines remain with the orchestrator; G3/G4 are not closed.

## Scratch artifacts

| File | Use |
|---|---|
| `operation_receipts.json` | All per-request Q-ID crosswalk, exact URLs, parameters, local/UTC timestamps, status, retrieved/inspected counts, displayed totals, raw SHA-256. |
| `stage1_screening.csv` | 838 occurrence-level screening rows with Q, rank, platform document ID/URL, DOI/full raw metadata, abstract/snippet, disposition and canonical S-0003/S-0007 crosswalk. |
| `stage1_summary.json` | Disposition counts by Q-ID and overall. |
| `scholar_final_first50.csv` | Final Scholar result records; 50 each except partial C3 (38). |
| `screening_records.csv` | OpenAlex records and initial diagnostic Scholar records. |
| `artifact_manifest.json` | Byte counts and SHA-256 for scratch artifacts. |
| `GoogleWeb_R1.raw` | Example preserved Google JS-shell body; corresponding six query bodies retained. |
| `BingWeb_R1.raw` | Example preserved Bing “no results” page; corresponding six fallback bodies retained. |
| `OpenAlex_R1.raw` | Example raw OpenAlex JSON; corresponding six query responses retained. |

Every raw response is retained as a named `*.raw` file with its adjacent request receipt. The combined receipts list all 95 HTTP request records, including diagnostic pagination and final windows; repeated diagnostic requests are not double-counted as screened results.

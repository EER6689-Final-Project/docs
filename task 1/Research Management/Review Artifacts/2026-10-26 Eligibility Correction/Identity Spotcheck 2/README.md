# Two existing-work identity links — 2026-10-26

This narrow read-only metadata check addresses two already annotated links, **not** the remaining all-topic identity crosswalk. No new S-ID, source row, independent-work count, occurrence exclusion or library merge is created. Accepted snapshot 3 remains unchanged; this memo supplies more precise identity provenance for later integration.

## Actual operations

`zotero-cli --json config` succeeded with local mode and library selector `*`. Three subsequent `get metadata` calls succeeded on 2026-10-26; exact request clocks were not captured. The following observed fields are transcribed from the completed tool responses, not claimed as exact-byte raw JSON preservation.

| Operation | Exact command | Observed record/version |
| --- | --- | --- |
| Q-340 | `zotero-cli --json get metadata 6UGAU5X4` | Mahimahi, conferencePaper, Ravi Netravali/Anirudh Sivaraman/Somak Das/Ameesh Goyal/Keith Winstein/James Mickens/Hari Balakrishnan, 2015 USENIX ATC, pp. 417–429, version 1923. |
| Q-341 | `zotero-cli --json get metadata GJMALCNF` | Rigorous benchmarking in reasonable time, Tomas Kalibera/Richard Jones, journalArticle, DOI `10.1145/2555670.2464160`, SIGPLAN Notices 48(11), pp. 63–74, displayed date June 20 2013, version 1858. Metadata conflicts/edition issues are not settled by repeating this record. |
| Q-342 | `zotero-cli --json get metadata TWKB9CAY` | Same title/authors, conferencePaper, DOI `10.1145/2464157.2464160`, ISMM 2013, 2013-06-20, pp. 63–74, version 1883. |

The CLI responses identify `library.name=My Library`, `type=user`, `id=0`. This is the CLI interface's returned library identifier, **not** independently established as a global Zotero user ID or the same identifier namespace as the MCP/local database `libraryID=1` observed at Q-111. Keep those interface-specific observations separate; neither selector `*` nor CLI `id=0` overwrites the previously observed local database ID. No switch or write occurred.

## Reconciliation

- **E-0505 → existing S-0003, record 6UGAU5X4:** original exported title/year, supplied Netravali/Sivaraman/Das/Goyal authors and exact venue URL match the existing Mahimahi record. Both URLs are `https://www.usenix.org/conference/atc15/technical-session/presentation/netravali`. This supports the already annotated existing-work link; it does not imply a second independent study, verify an unseen Scholar-hosted file or justify skipping its eligibility review. The accepted first-25 review already assessed this occurrence separately.
- **E-0361 → existing S-0007, specifically conference record TWKB9CAY:** original OpenAlex DOI `10.1145/2464157.2464160`, title, Kalibera/Jones authors and date 2013-06-20 match that record. Do **not** replace its DOI with the distinct journal DOI from GJMALCNF. The inventory's existing work-level relationship is retained with these record/version distinctions; journal metadata/pagination/version issues remain visible. This is not a publisher-level validation of the journal record or proof two attachments are byte-identical.

Original export identity fields came from immutable `2026-10-26 Discovery/REVIEWQUEUE.csv`; E-0361's OpenAlex ID is `W2013901208`. Other 836 occurrences and 76 heuristic duplicate candidates were **not** reconciled in this pass. No publication-date, language, source-support, confidence, full-text or citation clearance follows. B-010/G3/G4 remain open. AI metadata identity check, not independent human scientific review.

## Later bounded DOI follow-up — Q-343

A mechanical scan of **citation cells only** in the 133-row matrix found 21 distinct DOI strings and two matching exported occurrence DOI/URL candidates. This is not a complete all-topic identity search: many sources/versions have no DOI in that particular field, so missing matches prove nothing. No language/relevance filtering or new work count followed.

- **E-0553 → existing T1.2 record 3TNGADXQ:** its VisibleV8 title and DOI-bearing ACM URL `10.1145/3355369.3355599` match the canonical note and a new actual local metadata read. Q-343 command `zotero-cli --json get metadata 3TNGADXQ` returned Jordan Jueckstock/Alexandros Kapravelos, *VisibleV8: In-browser Monitoring of JavaScript in the Wild*, October 21 2019, record version 1453, that DOI and exact ACM URL. Actual start/end clocks and exact-byte response hash are preserved in `Q-343-receipt.json` and `Q-343-VisibleV8-metadata.json`. This supports the existing-work/record link, not independent corroboration, current Chromium validity or an unseen Scholar attachment's version.
- **E-0501 → existing portfolio S-0004:** exported title and ACM DOI-bearing URL `10.1145/2068816.2068846` match the existing Butkiewicz source row/note. That bounded original-work link is recorded without inventing a Zotero parent key. No new library search or attachment-level identity check was performed; the existing legitimate author-copy provenance and unresolved library key remain as documented in the source note.

These additional links do not alter accepted snapshot routing, settle all cross-topic/edition identities, clear remaining heuristic DUP annotations, or allocate new S-IDs. No paper methods were reread in this metadata check. Other identity/date/language/type/full-text/citation requirements remain open; source support/confidence are unchanged.

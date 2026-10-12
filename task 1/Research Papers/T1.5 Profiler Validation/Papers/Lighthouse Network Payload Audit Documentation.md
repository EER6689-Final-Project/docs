# Lighthouse — Avoid Enormous Network Payloads

- **Citation:** Chrome for Developers. “Avoid enormous network payloads.” [Lighthouse documentation](https://developer.chrome.com/docs/lighthouse/performance/total-byte-weight).
- **Zotero key:** `AIFQRE7Y` (webpage; imported HTML snapshot attached as `total-byte-weight.html`).
- **Source access:** Current online page and saved Zotero snapshot checked 13 October 2026.

## Outline Summary

- **Operational scope:** The page says the audit reports the total size, in KiB, of resources requested by the page, with the largest requests listed first. It cites HTTP Archive data for a median payload range and states a 5,000 KiB flag threshold on the reviewed page.
- **Comparability:** “Requested resource size” must not be conflated with transferred bytes, encoded body bytes, or decoded resource sizes unless the exact collection rule is matched.
- **Limit:** This is mutable audit documentation with thresholds and reference data that may change. It is an optimization audit, not a validation result for a profiler’s byte accounting.

## T1.5 Evidence Check

- **Source-supported:** The audit’s stated units, scope, flag threshold, and rationale as displayed at review time.
- **Researcher inference:** Treat it as a separate derived audit output; do not assume a CDP network total is equivalent without reconciling request inclusion and size fields.

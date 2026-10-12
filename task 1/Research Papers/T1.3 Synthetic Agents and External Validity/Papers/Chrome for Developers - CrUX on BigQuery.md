# Chrome for Developers - CrUX on BigQuery

- **Citation:** Chrome for Developers. “CrUX on BigQuery.” Chrome UX Report documentation, current live documentation, accessed 12 October 2026. https://developer.chrome.com/docs/crux/bigquery.
- **Zotero key:** `VDGPNUWI`.
- **Source type:** Official dataset schema and access documentation.
- **Provenance/access:** Zotero stores an imported HTML snapshot (`2QA3W4VP`) and canonical URL. The live Google documentation was consulted; schema is mutable and the Zotero record provides no fixed documentation version.

## Abstract and scope

Documents the CrUX BigQuery datasets, table structures, and aggregation levels. This is primary documentation for accessing field data and understanding what dimensions remain available for population-level profile summaries.

## Outline Summary

- **Source findings:** The documentation describes summary tables by month and origin, plus `device_summary` by month/origin/device and `country_summary` by month/origin/device/country. `origin_summary` lists included origins and is updated monthly. Experimental country/global tables provide a `yyyymm` field for multi-month queries (sections for summary tables and experimental dataset, lines 126–133, 174–185).
- **Limitations:** Dataset presence and aggregation schema do not establish representativeness of all users, nor do aggregate histogram tables expose each user’s complete environment. The schema and monthly tables can change; record table date and query when analysis is performed.
- **Relationship to T1.3:** Provides a practical source for deriving distributions by time, origin, device, and country, while reinforcing that individual browser profiles cannot be reconstructed from aggregate summaries alone.
- **Important anchors:** Dataset access, lines 57–66; summary tables, 126–133; `origin_summary`, 174–176; experimental country/global tables, 177–185. No page numbers.
- **Concise takeaway:** BigQuery exposes useful aggregated profile dimensions, but aggregates cannot be mistaken for complete individual user configurations.

## T1.3 Evidence Check

- **Documentation-supported:** Table names, described grouping dimensions, monthly refresh, and experimental table schema.
- **Not established:** Population coverage, query-level data quality, or profile validity.
- **Researcher inference:** Preserve query text, month, and filtering choices so profile distributions are reproducible.

# CrUX API | Chrome UX Report

- **Source type:** Official data/API documentation.
- **Zotero key:** `DFUNZS6W`.
- **Provenance:** Zotero record URL https://developer.chrome.com/docs/crux/api; no child snapshot was present. Current official API documentation and methodology are available at https://developer.chrome.com/docs/crux/api and https://developer.chrome.com/docs/crux/methodology/tools.

## Source-supported details

The API provides aggregated real-user experience metrics by URL/page or origin and can filter by form factor and metric. The current API documentation describes the CrUX API as field data; the current tools documentation says the API supplies a daily updated rolling 28-day window and a subset of metrics. CrUX page inclusion requires user, origin, and page eligibility, including sufficient popularity; experiences failing page eligibility may still contribute to origin-level aggregates (Chrome for Developers, “CrUX API,” “CrUX Tools,” and “CrUX methodology”).

## Use and limits

CrUX is a field-data source for eligible Chrome user experiences, not a complete census of all browsers or visitors. API values are aggregated and time-windowed, so they are not matched observations for an individual synthetic run. Availability varies by URL eligibility and the documented metric/dimension support.

**Researcher inference:** A comparison with synthetic measurements needs aligned URL, form factor, metric definition, and time window; even then, association is population-level rather than a per-session causal comparison.

# Lighthouse — User Timing Marks and Measures

- **Citation:** Chrome for Developers. “User Timing marks and measures.” [Lighthouse documentation](https://developer.chrome.com/docs/lighthouse/performance/user-timings).
- **Zotero key:** `U9PHTV9S` (webpage; imported HTML snapshot attached as `user-timings.html`).
- **Source access:** Official page and Zotero snapshot checked 13 October 2026; page identifies its last update as 2 May 2019.

## Outline Summary

- **Scope:** Describes application-inserted User Timing marks and measures, and says Lighthouse extracts these from Chrome trace events for display in its report.
- **Meaning:** A mark is a timestamp and a measure is elapsed time between marks; these values depend on the application-defined instrumentation.
- **Limit:** The audit is informational rather than pass/fail. The page is dated 2019 and should not be treated as a current Lighthouse score definition without checking current implementation/version.

## T1.5 Evidence Check

- **Source-supported:** Description of user-defined marks/measures and the documented trace extraction path.
- **Researcher inference:** Use these as application-defined diagnostics, not as a standardized substitute for browser lifecycle metrics.

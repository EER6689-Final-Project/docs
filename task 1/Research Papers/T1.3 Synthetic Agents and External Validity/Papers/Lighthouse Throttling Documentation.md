# Lighthouse throttling documentation

- **Source type:** Official, version-controlled software documentation.
- **Zotero key:** `JT3PXZLG`.
- **Provenance:** Zotero URL https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md; attached HTML snapshot `JQICUSGQ`. Current source: https://github.com/GoogleChrome/lighthouse/blob/main/docs/throttling.md.

## Source-supported details

The documentation describes simulated throttling (the default in the current docs) as estimating a throttled page load from an initially unthrottled observation, and DevTools throttling as applying CPU throttling during execution. It says simulation is fast but can be inaccurate when alternate execution paths are predicted poorly; for deeper investigation it recommends actual DevTools CPU throttling. Lighthouse’s separate variability guidance reports that throttling only partly mitigates several sources of variation (Lighthouse docs, “Types of CPU Throttling” and variability table).

## Use and limits

These behaviors are implementation and version specific. Simulated conditions are estimates based on observed activity, while actual network and device variation remain relevant. The current `main` documentation can change; a study should pin a Lighthouse release or commit.

**Researcher inference:** A Lighthouse result should identify its throttling method. Simulated throttling supports a standardized lab profile, but it does not on its own establish that the profile predicts users’ field performance.

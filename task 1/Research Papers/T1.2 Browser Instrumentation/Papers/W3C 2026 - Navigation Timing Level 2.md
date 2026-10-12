# Navigation Timing Level 2

- **Citation:** World Wide Web Consortium (W3C). *Navigation Timing Level 2*. Working Draft, 1 September 2026. https://www.w3.org/TR/navigation-timing-2/
- **Zotero key:** `JJWRMF5Z`.
- **Source:** Zotero snapshot dated 25 February 2026 (Working Draft); current reviewed edition dated 1 September 2026.

## Document scope

This normative specification defines navigation lifecycle and network phase timestamps. It is not an empirical readiness study and reports no instrumentation overhead.

## Outline Summary

- **Central idea**
  - `PerformanceNavigationTiming` exposes navigation type and lifecycle/network phase timing attributes under specified visibility and connection conditions.
- **Purpose and questions**
  - Standardizes observable navigation lifecycle and network phases. Research questions and empirical objectives are not applicable to this normative specification.
- **Approach and setup**
  - Normative definitions for navigation timing entries; no experimental participants, dataset, or setup.
- **Timing behavior and results**
  - Defines redirect, fetch, DNS, connection, TLS, request, response, readiness, and load phase timestamps.
  - Cross-origin redirects and unload conditions can hide or zero fields. Cache and connection reuse can collapse DNS or connection phases. There is no `requestEnd`; `domLoading` should not be treated as a meaningful metric. These are specified semantics, not empirical results.
- **Limitations and conditions**
  - Cross-origin visibility restrictions and connection reuse affect interpretation of zero or absent phase values. Navigation phases alone do not validate perceived readiness or quantify instrumentation cost.
- **Author-stated future work**
  - Not stated in the reviewed specification.
- **Relationship to the T1.2 instrumentation review**
  - Provides navigation timing baselines and interpretive constraints. Analyses should preserve navigation type and relevant visibility, cache, and connection context.
- **Important sections**
  - `PerformanceNavigationTiming` definitions: https://www.w3.org/TR/navigation-timing-2/
- **Concise takeaway**
  - Treat absent, zero, and collapsed phases in light of visibility and connection context.

## T1.2 Claim Check

- **Specification claim:** The document defines observable navigation timing fields; those fields do not establish user-perceived readiness.

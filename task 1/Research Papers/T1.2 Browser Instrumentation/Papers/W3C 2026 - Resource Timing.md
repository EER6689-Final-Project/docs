# Resource Timing

- **Citation:** World Wide Web Consortium (W3C). *Resource Timing*. Candidate Recommendation Draft, 1 September 2026. https://www.w3.org/TR/resource-timing/
- **Zotero key:** `NXHCE5SV`.
- **Source:** Zotero snapshot dated 20 April 2026 (Candidate Recommendation Draft); current reviewed edition dated 1 September 2026.

## Document scope

This normative specification defines resource fetch timing and privacy controls. It does not provide a quantitative collection-cost or completeness study.

## Outline Summary

- **Central idea**
  - Resource Timing exposes per-fetch initiator and timing-phase information subject to buffering, cross-origin permissions, and timestamp precision rules.
- **Purpose and questions**
  - Standardizes resource fetch timing while protecting cross-origin information. Research questions and empirical objectives are not applicable to this normative specification.
- **Approach and setup**
  - Normative resource timing, buffering, and timing-allowance definitions; no experimental participants, dataset, or setup.
- **Entry behavior and results**
  - Defines per-fetch resource phases and initiator information, configurable bounded buffers, and clearing, overflow, and dropped-entry handling.
  - Without applicable `Timing-Allow-Origin`, cross-origin timing fields are masked. High Resolution Time coarsening applies; repeated URLs may share a fetch/entry. These are specified behaviors, not measured results.
- **Limitations and conditions**
  - Browser and cache behavior, cross-origin masking, timestamp coarsening, and buffer loss constrain visible detail. Entries represent fetches, not DOM element counts, and do not guarantee complete phase visibility. No experimental overhead estimate is supplied.
- **Author-stated future work**
  - Not stated in the reviewed specification.
- **Relationship to the T1.2 instrumentation review**
  - Defines resource observations and their visibility conditions. Resource-level analyses should account for initiators, timing permissions, and buffer loss before interpreting entry counts or phase distributions.
- **Important sections**
  - Buffer, timing allowance, and fetch definitions: https://www.w3.org/TR/resource-timing/
- **Concise takeaway**
  - Treat resource entries as conditional observations of fetches, with explicit coverage limits.

## T1.2 Claim Check

- **Specification claim:** Resource Timing defines entry and privacy behavior; it does not establish complete fetch visibility or quantify profiler overhead.

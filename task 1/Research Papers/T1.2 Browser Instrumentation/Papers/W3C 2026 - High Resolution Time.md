# High Resolution Time

- **Citation:** World Wide Web Consortium (W3C). *High Resolution Time*. Working Draft, 1 September 2026. https://www.w3.org/TR/hr-time-3/
- **Zotero key:** `CU4HMS98`.
- **Source:** Zotero snapshot dated 24 March 2026 (Working Draft); current reviewed edition dated 1 September 2026.

## Document scope

This normative specification defines monotonic, origin-relative time and precision protections. It does not report empirical timer accuracy, throughput, or instrumentation overhead.

## Outline Summary

- **Central idea**
  - `performance.now()` provides monotonic timestamps in milliseconds relative to a context's `timeOrigin`, subject to precision coarsening and security constraints.
- **Purpose and questions**
  - Defines elapsed-time clock behavior while limiting risks from high precision. Research questions and empirical objectives are not applicable to this normative specification.
- **Approach and setup**
  - Normative clock and precision definitions (§§4, 7, 9); no experimental participants, dataset, or setup.
- **Clock behavior and results**
  - Defines origin-relative monotonic timestamps and precision coarsening. Specified targets are at least 100 μs generally and at least 5 μs in cross-origin-isolated contexts; implementation behavior may vary (§§4, 7, 9).
  - These are specified constraints, not measured accuracy or overhead results.
- **Limitations and conditions**
  - Coarsening and possible jitter constrain interpretation of short intervals. Cross-context comparisons require handling distinct time origins and context conditions. The specification does not measure realized timer error or collection throughput.
- **Author-stated future work**
  - Not stated in the reviewed specification.
- **Relationship to the T1.2 instrumentation review**
  - Defines the clock basis for browser timing data. Timer precision and origin compatibility are relevant when interpreting small differences or joining observations across contexts.
- **Important sections**
  - §§4, 7, 9: https://www.w3.org/TR/hr-time-3/
- **Concise takeaway**
  - Interpret browser timestamps with their time origin and precision conditions.

## T1.2 Claim Check

- **Specification claim:** The document defines clock semantics and coarsening constraints; it does not establish a target browser's realized timing error or profiler throughput.

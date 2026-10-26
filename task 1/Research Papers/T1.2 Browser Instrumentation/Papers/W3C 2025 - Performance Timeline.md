# Performance Timeline

- **Citation:** World Wide Web Consortium (W3C). *Performance Timeline*. Candidate Recommendation Draft, 21 May 2025. https://www.w3.org/TR/performance-timeline/
- **Zotero key:** `REP5RHB6`.
- **Source:** Zotero-saved specification snapshot; reviewed edition matches the live W3C edition.

## Document scope

This normative specification defines common performance entry and observer interfaces. It is an API contract, not an empirical study, and supplies no measured observer overhead or capture-completeness result.

## Outline Summary

- **Central idea**
  - A shared `PerformanceEntry` model and `PerformanceObserver` interface expose timestamped browser performance entries.
- **Purpose and questions**
  - Defines common entry and observer behavior. Research questions and empirical objectives are not applicable to this normative specification.
- **Approach and setup**
  - Normative API definitions and algorithms (§§1, 3–6); no experimental participants, dataset, or setup.
- **Interfaces, behavior and results**
  - Defines entry names, types, timestamps and durations, observer registration and delivery, and buffer behavior.
  - Observer callback timing is user-agent chosen; supported entry types vary; buffers are bounded and dropped entries can be reported (§§3–6). These are specified behaviors, not empirical findings.
  - Section 5 recommends narrow subscriptions and disconnecting observers to limit observation work; it does not quantify the cost.
- **Limitations and conditions**
  - Entry support and callback timing can vary by user agent, and bounded buffers can lose entries. The specification does not measure callback latency, completeness, or collection cost.
- **Author-stated future work**
  - Not stated in the reviewed specification.
- **Relationship to the T1.2 instrumentation review**
  - Defines an observation interface and its coverage conditions. It can inform support checks and lost-entry accounting, but does not validate a profiler's accuracy or overhead.
- **Important sections**
  - §§1, 3–6, especially §5: https://www.w3.org/TR/performance-timeline/
- **Concise takeaway**
  - Record entry support and buffer loss when interpreting what an observer did or did not capture.

## T1.2 Claim Check

- **Specification claim:** The document defines browser API behavior. Any claim about realized callback cost or capture completeness requires separate empirical evidence.

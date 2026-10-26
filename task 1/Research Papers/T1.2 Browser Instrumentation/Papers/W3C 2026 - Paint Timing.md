# Paint Timing

- **Citation:** World Wide Web Consortium (W3C). *Paint Timing*. Working Draft, 2 October 2026. https://www.w3.org/TR/paint-timing/
- **Zotero key:** `84ZFNR74`.
- **Source:** Current W3C draft, cited by section because it is a normative specification and has no study page numbers.

## Abstract

This specification defines browser performance entries for First Paint (FP) and First Contentful Paint (FCP), including when user agents record and expose those events. This is a brief description of the specification, not a transcribed abstract; the document is normative API material, not an empirical study.

## Outline Summary

- **Central idea**
  - Define interoperable browser timing entries for early paint milestones and specify how those entries are recorded and exposed.
- **Problem and objective**
  - Provide a shared API model for FP and FCP observations. These definitions do not establish how accurately either milestone represents user-perceived visual readiness (§§1.1–1.2, 2–5.3).
- **Approach and scope**
  - Normative definitions of paintable/contentful content, entry fields, timestamps, recording algorithms, and reporting (§§2–5.3).
  - The specification is not an experiment; dataset, participants, and experimental setup are N/A.
- **Signals and rules**
  - FP is optional for user agents; implementations should at minimum mark FCP (§1.1).
  - Paint timing is tied to a rendering update. A presentation timestamp may be implementation-defined when available (§§1.1–1.2, 3–5).
  - “Paintable” does not necessarily mean perceptually visible. Reporting for nested frames may also be limited (§§1.1–1.2, 2, 5.2–5.3).
- **Limitations and interpretation**
  - This draft specifies API behavior and contains no empirical overhead, measurement-completeness, or user-perception results.
  - FP availability, the distinction between paintability and perceived visibility, presentation-time implementation details, and nested-frame reporting bound interpretation.
- **Author-stated future work**
  - Not stated in the reviewed sections.
- **Relationship to our profiler**
  - Defines possible early-paint signals and their browser reporting rules.
  - Preliminary inference: a profiler should name the milestone it reports and its frame scope; FCP should not be described as proof of visual readiness.
  - This interpretation does not select a final research gap or metric set.
- **Important quotations and section references**
  - No direct quotation transcribed. Relevant sections: §§1.1–1.2, 2–5.3.
- **Concise takeaway**
  - Record whether an observation is FP or FCP and preserve the specification’s frame and visibility limits when explaining it.

## T1.2 Evidence Check

- **Normative claim:** The note describes specified API behavior, not observed behavior across browser implementations.
- **Preliminary inference:** Paint milestones need explicit labels and scope before they are used as readiness claims.

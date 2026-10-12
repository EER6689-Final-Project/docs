# Event Timing API

- **Citation:** World Wide Web Consortium (W3C). *Event Timing API*. Working Draft, 19 March 2026. https://www.w3.org/TR/event-timing/
- **Zotero key:** `I8L7FN9V`.
- **Source:** Current W3C draft, cited by section because it is a normative specification and has no study page numbers.

## Abstract

This specification defines performance entries for selected discrete user events, measuring from the event timestamp through the next rendering update. It also defines event inclusion, duration precision, and reporting thresholds. This is a short description, not a transcribed abstract; the draft is normative API material, not an empirical study.

## Outline Summary

- **Central idea**
  - Expose timing information for selected discrete interactions to support analysis of event processing and presentation latency (§§1.4–1.5, 2.1).
- **Problem and objective**
  - Standardize which event timing entries are exposed and how their duration is calculated and reported. This API definition does not itself establish a complete distribution of interactive experience.
- **Approach and scope**
  - Normative definitions of entry fields, event processing, duration rounding, reporting threshold configuration, and privacy rationale (§§2.1, 3.6–3.9, 4).
  - The specification is not an experiment; dataset, participants, and experimental setup are N/A.
- **Signal and rules**
  - A selected event is timed from its event timestamp to the next rendering update (§§1.4–1.5).
  - Duration is rounded to 8 ms. The default reporting threshold is 104 ms; a configured threshold cannot be lower than 16 ms (§§3.6–3.9).
  - Continuous events such as pointer movement, wheel, and drag are excluded (§§1.4–1.5, 3.6).
- **Limitations and interpretation**
  - Thresholding means entries do not represent every event. Rounding limits precision, and excluded continuous events constrain interaction coverage (§§1.4–1.5, 3.6–3.9).
  - The specification provides no empirical overhead or user-perception result.
- **Author-stated future work**
  - Not stated in the reviewed sections.
- **Relationship to our profiler**
  - Defines an available signal for selected discrete interactions and its threshold and precision bounds.
  - Preliminary inference: disclose the configured threshold, rounding, and event classes covered before interpreting collected entries as interaction responsiveness.
  - This interpretation does not select a final gap, architecture, event set, or tolerance.
- **Important quotations and section references**
  - No direct quotation transcribed. Relevant sections: §§1.4–1.5, 2.1, 3.6–3.9, 4.
- **Concise takeaway**
  - Event Timing reports a thresholded and rounded subset of discrete interactions; entry presence and duration need that context.

## T1.2 Evidence Check

- **Normative claim:** Event selection, timing, threshold, and rounding are specified behavior, not measured coverage or accuracy across sites.
- **Preliminary inference:** Report threshold and event-class coverage when using this API to characterize interaction timing.

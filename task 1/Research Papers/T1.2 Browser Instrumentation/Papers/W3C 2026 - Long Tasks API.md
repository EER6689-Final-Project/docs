# Long Tasks API

- **Citation:** World Wide Web Consortium (W3C). *Long Tasks API*. Working Draft, 19 March 2026. https://www.w3.org/TR/longtasks-1/
- **Zotero key:** `KEJFZJHV`.
- **Source:** Current W3C draft, cited by section because it is a normative specification and has no study page numbers.

## Abstract

This specification defines entries for qualifying long tasks on the UI thread and limited attribution to a culprit browsing context. It sets the reporting threshold and describes the work included in a task’s duration. This is a short description, not a transcribed abstract; the draft is normative API material, not an empirical study.

## Outline Summary

- **Central idea**
  - Expose periods of qualifying long UI-thread work as browser performance entries, with limited context about the responsible browsing context (§§2–4.1).
- **Problem and objective**
  - Define a browser API for identifying tasks that exceed a specified duration and expose an attribution model. This API can flag a long period but does not uniquely identify its root cause.
- **Approach and scope**
  - Normative definitions for task terminology, entry and attribution interfaces, reporting algorithm, observer exposure, and privacy scenarios (§§2–5.2).
  - The specification is not an experiment; dataset, participants, and experimental setup are N/A.
- **Signal and rules**
  - A qualifying long task exceeds 50 ms. The measured task includes the following microtask checkpoint, rendering updates, and specified pauses (§§2, 4.1).
  - Entry duration has 1 ms granularity. Attribution to a culprit browsing context is limited (§§3, 4.1).
- **Limitations and interpretation**
  - A long-task entry identifies a qualifying period, not a unique source-level cause. Limited attribution and 1 ms granularity constrain interpretation (§§3–4.1).
  - The draft describes privacy risks and possible mitigations (§§5.1–5.2) but supplies no empirical overhead or causal diagnosis result.
- **Author-stated future work**
  - Not stated in the reviewed sections.
- **Relationship to our profiler**
  - Defines a candidate signal for long UI-thread periods that may be useful alongside other timing and task context.
  - Preliminary inference: present long tasks as periods requiring investigation and combine them with complementary context; do not label an entry as a unique root cause.
  - This interpretation does not select a final gap, architecture, method, or threshold.
- **Important quotations and section references**
  - No direct quotation transcribed. Relevant sections: §2, §3, §4.1, §§5.1–5.2.
- **Concise takeaway**
  - A Long Task entry flags a long UI-thread period with limited attribution; it is a diagnostic cue, not a causal explanation.

## T1.2 Evidence Check

- **Normative claim:** The 50 ms criterion, duration treatment, and attribution are defined by the draft; it does not establish cause or user impact for any particular task.
- **Preliminary inference:** Pair long-task timing with complementary context and state the limits of attribution.

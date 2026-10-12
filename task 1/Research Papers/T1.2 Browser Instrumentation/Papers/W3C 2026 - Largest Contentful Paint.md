# Largest Contentful Paint

- **Citation:** World Wide Web Consortium (W3C). *Largest Contentful Paint*. Working Draft, 26 August 2026. https://www.w3.org/TR/largest-contentful-paint/
- **Zotero key:** `6WVYFE8R`.
- **Source:** Current W3C draft, cited by section because it is a normative specification and has no study page numbers.

## Abstract

This specification defines a Largest Contentful Paint (LCP) performance entry and the rules for selecting and reporting eligible painted text and image candidates. This is a short description, not a transcribed abstract; the draft is normative API material, not an empirical study.

## Outline Summary

- **Central idea**
  - Report a selected large-content paint candidate as a page-load signal, using specified eligibility, sizing, and reporting rules (§§1, 3.1, 4.2–4.4).
- **Problem and objective**
  - The draft’s goals include reflecting meaningful page-load rendering better than FP/FCP, remaining understandable, and being harder to game (§1). These are specification goals, not empirical findings that LCP predicts user perception.
- **Approach and scope**
  - Normative entry definitions and candidate-selection, effective-visual-size, and entry-creation algorithms (§§3.1, 4.2–4.4).
  - The specification is not an experiment; dataset, participants, and experimental setup are N/A.
- **Signal and rules**
  - Candidates come from eligible painted text and images; the entry records the selected candidate and its timing/context fields (§3.1, §§4.2–4.4).
  - Candidate reporting stops after trusted scroll or input events (§4.2).
- **Limitations and interpretation**
  - LCP is a selected candidate under the API’s eligibility and interaction rules. It does not establish that all page content is ready or that a person has perceived the content.
  - The draft provides no empirical overhead or perceptual-validity evaluation.
- **Author-stated future work**
  - Not stated in the reviewed sections.
- **Relationship to our profiler**
  - Defines a browser-provided candidate signal and the context needed to interpret it.
  - Preliminary inference: preserve the selected candidate and interaction context in any profiler output; do not treat LCP as proof that all content is ready.
  - This interpretation does not select a final gap, architecture, or metric set.
- **Important quotations and section references**
  - No direct quotation transcribed. Relevant sections: §1, §3.1, §§4.2–4.4.
- **Concise takeaway**
  - LCP reports a rule-selected candidate, so interpret the candidate and the event cutoff alongside its timestamp.

## T1.2 Evidence Check

- **Normative claim:** Candidate eligibility, selection, and stop conditions are specified API behavior; the draft does not validate their relation to user-perceived readiness.
- **Preliminary inference:** A profiler should retain candidate and interaction context when presenting LCP.

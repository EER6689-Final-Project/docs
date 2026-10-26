# Chromium CDP - DOMSnapshot Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — DOMSnapshot domain*, `tot` documentation. https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/
- **Zotero key:** `66QX7WHN`.
- **Source:** Zotero snapshot version 1473, saved 29 August 2026; `tot` endpoint is mutable. Pin the Chromium build and protocol revision for implementation work.

## Abstract and scope

The DOMSnapshot domain documents commands for capturing DOM and layout state. `captureSnapshot` returns a flattened tree and layout data, with optional computed styles and other fields. The documentation describes the protocol surface; it does not measure capture fidelity, temporal consistency, or performance cost.

## Outline Summary

- **Central idea:** CDP can return a structured snapshot of DOM and layout information, including content from frames and shadow trees.
- **Problem and objectives:** Define the command and data representation for DOM/layout capture. Research questions, participants, datasets, and experimental setup are N/A for protocol documentation.
- **Approach:** `captureSnapshot` accepts requested computed styles and optional fields. The documented flattened DOM includes iframe, template, imported-document, and shadow-DOM content; layout data may include rectangles, paint order, and blended colors. `getSnapshot` is deprecated.
- **Results:** N/A. The reference documents API behavior rather than empirical results.
- **Limitations:** The domain is experimental and mutable. The page provides no evaluation of capture accuracy, timing, output consistency on a changing page, or resource cost.
- **Author-stated future work:** Not stated.
- **Relationship to T1.2:** Candidate structural observation channel for correlating DOM and layout state with timing or trace events. Record requested styles, optional fields, protocol revision, and capture point.
- **Important source references:** [`captureSnapshot`](https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/#method-captureSnapshot), [`getSnapshot`](https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/#method-getSnapshot), and the [DOMSnapshot domain](https://chromedevtools.github.io/devtools-protocol/tot/DOMSnapshot/). No page numbers.
- **Concise takeaway:** The command provides broad structural output, but the protocol reference does not establish snapshot cost, accuracy, or temporal consistency.

## T1.2 Evidence Check

- **Protocol claim:** `captureSnapshot` and the described result fields are documented by the DOMSnapshot domain.
- **Not established:** How fully or consistently a snapshot represents a dynamic page, or how much it perturbs that page.
- **Preliminary inference:** Test capture cost and state consistency under defined dynamic workloads; these are open evaluation questions, not findings of the protocol page.

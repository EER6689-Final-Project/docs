# web.dev - How To Think About Speed Tools

- **Citation:** “How To Think About Speed Tools.” web.dev, Google Chrome/web.dev guidance; publication or update date and named author are not provided in the inspected page. https://web.dev/articles/speed-tools.
- **Zotero key:** `99DTPUKH`.
- **Source type:** Practitioner infographic/guidance page.
- **Provenance/access:** Zotero metadata contains title, web.dev site, and canonical URL but no creator/date or child snapshot. The live canonical page was consulted on 12 October 2026; its text and downloadable infographic were available.

## Abstract and scope

Consolidates Google performance-tool guidance and explains the distinct strengths and limits of lab and field data. It is a conceptual source for deciding which evidence informs profile choices and which evidence measures actual user outcomes.

## Outline Summary

- **Source findings:** The page cautions against assuming a single metric or “representative user” captures experience. Lab testing offers controlled, repeatable debugging and deeper visibility, but may miss real-world bottlenecks. Field data captures actual user experiences and can support KPI correlation, but has a restricted metric set and limited debugging capability. It maps Lighthouse and WebPageTest to lab workflows and CrUX/PageSpeed Insights to field data (sections “Common myths,” “Understanding lab vs. field data,” and “What are the different performance tools?”).
- **Limitations:** The page is a high-level infographic and product guide; it does not report a study sample, methods, or performance comparison. Its tools and recommendations may change over time; the inspected page supplies no publication date.
- **Relationship to T1.3:** Supports combining synthetic tests with field evidence while being explicit about what each can observe. It argues against representing a broad user population with one hard-coded profile.
- **Important anchors:** Myths 1–3, lines 42–60; lab strengths/limitations, 62–83; field strengths/limitations, 84–105; tool roles, 107–153. No page numbers.
- **Concise takeaway:** Use lab data to reproduce and diagnose; use field data to understand the distribution of real experiences.

## T1.3 Evidence Check

- **Source-supported:** The stated definitions, strengths, limitations, and tool categories appear on the page.
- **Not established:** Quantitative accuracy, representativeness, or equivalence between named tools.
- **Researcher inference:** Treat the source as framing guidance, not validation evidence for the proposed profiler.

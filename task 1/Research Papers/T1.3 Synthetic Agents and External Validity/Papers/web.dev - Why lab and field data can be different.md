# web.dev - Why lab and field data can be different

- **Citation:** Philip Walton. “Why lab and field data can be different (and what to do about it).” web.dev, last updated 18 July 2022. https://web.dev/articles/lab-and-field-data-differences.
- **Zotero key:** `JHEC6VHJ`.
- **Source type:** Practitioner guidance article, not an empirical comparison study.
- **Provenance/access:** Zotero stores an imported HTML snapshot (`NZRZ7M7A`) and the live canonical URL. The current web.dev page was consulted on 12 October 2026. The live page identifies Walton and its update date.

## Abstract and scope

Explains why controlled lab measurements and real-user field measurements can disagree, using Core Web Vitals examples. The page is useful for defining the claims a synthetic test can support and for interpreting field data as a distribution rather than a single canonical value.

## Outline Summary

- **Source findings:** Lab data is collected under predefined device/network settings, supporting repeatability and debugging. Field data captures actual user devices, network conditions, geography, behavior, and a distribution of visits. Lab tests generally represent a single device, network, and location; field values also reflect caching, bfcache, personalization, user interaction, and other optimizations. The article recommends using field data to prioritize user impact while using lab data to investigate and reproduce issues (sections “Lab data versus field data,” “Why lab and field data are different,” and “What to do when the results are different”).
- **Limitations of the source:** Guidance focuses on Core Web Vitals and browser tooling; examples are explanatory rather than a controlled validation study. It does not quantify how accurate any specific emulator is. Page content is dated 2022 and may not reflect subsequent metric or product changes.
- **Relationship to T1.3:** Direct support for distinguishing synthetic results from RUM and for documenting representativeness limits. Real production URLs do not make controlled browser runs into RUM, because the users, devices, and behaviors remain simulated or fixed.
- **Important anchors:** Lab definition and repeatability, lines 66–72; field definition/distribution, 73–82; factors that differ, 95–108; interpretation, 199–205. No page numbers.
- **Concise takeaway:** Lab and field measurements answer related but different questions; reporting should preserve that distinction.

## T1.3 Evidence Check

- **Source-supported:** The distinction, examples of sources of variation, and suggested complementary uses are stated in the article.
- **Not established:** Error bounds or empirical fidelity of synthetic profiles against real users.
- **Researcher inference:** Use paired lab and field summaries to select profile dimensions, then validate profile timing distributions separately.

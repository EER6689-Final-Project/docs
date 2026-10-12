# Chrome for Developers - Navigation types now available in CrUX

- **Citation:** Chrome for Developers. “Navigation types now available in CrUX.” Chrome Developers Blog, current live page, accessed 12 October 2026. https://developer.chrome.com/blog/crux-navigation-types.
- **Zotero key:** `MDWB2TDG`.
- **Source type:** Official dataset feature announcement and query guidance.
- **Provenance/access:** Zotero stores an imported HTML snapshot (`37HLB7TB`) and canonical URL. The live Chrome Developers page was consulted; Zotero metadata omits publication date and named author, so the item should be pinned to the snapshot for formal citation.

## Abstract and scope

Describes the CrUX `navigation_types` metric and shows how navigation categories can help explain performance distributions. Relevant to profile scenarios because navigation mode and cache state change user experience independently of device/network profile.

## Outline Summary

- **Source findings:** The page demonstrates aggregating fractions for `navigate`, `navigate_cache`, `reload`, `restore`, `back_forward`, `back_forward_cache`, and `prerender`. It warns that not all origins provide `navigation_types` and recommends guarding calculations with `SAFE_DIVIDE` (query example, lines 127–146; feature explanation earlier on page).
- **Limitations:** This is a product announcement and SQL example, not an evaluation of the metric’s completeness or a browser cache experiment. Coverage varies by origin, and the post does not establish that these categories correspond to a single deterministic synthetic cache state.
- **Relationship to T1.3:** Supports treating navigation and cache conditions as explicit scenario dimensions; do not collapse initial navigation, reload, restoration, and prerender behavior into one profile result.
- **Important anchors:** Navigation type definitions and availability, page section around lines 80–127; aggregation/query example, lines 127–146. No page numbers.
- **Concise takeaway:** CrUX navigation type data can distinguish different visit modes, but its coverage is incomplete and it does not by itself specify a reproducible browser cache setup.

## T1.3 Evidence Check

- **Documentation-supported:** Named navigation categories and coverage caveat.
- **Not established:** A direct mapping from categories to controlled synthetic browser states or causal performance effects.
- **Researcher inference:** Define cache and navigation state separately in agent configuration and report them alongside measured timing.

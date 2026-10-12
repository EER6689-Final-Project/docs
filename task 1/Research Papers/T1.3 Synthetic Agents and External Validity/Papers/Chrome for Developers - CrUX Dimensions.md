# Chrome for Developers - CrUX Dimensions

- **Citation:** Chrome for Developers. “Dimensions.” Chrome UX Report documentation, current live documentation, accessed 12 October 2026. https://developer.chrome.com/docs/crux/methodology/dimensions.
- **Zotero key:** `JRR4K3ST`.
- **Source type:** Official dataset methodology documentation.
- **Provenance/access:** Zotero stores an imported HTML snapshot (`HZCHTL6S`) and canonical URL; the live Google Chrome for Developers documentation was consulted. The page is mutable and provides no fixed version in the item metadata.

## Abstract and scope

Defines current dimensions used to segment CrUX data, including form factor and effective connection type (ECT). This is operational documentation for understanding the categories that a RUM-informed profile could draw from.

## Outline Summary

- **Source findings:** Current form-factor values are `phone`, `tablet`, and `desktop`, inferred from the device User-Agent string. The documentation describes ECT as an optional dimension and explains that NULL can represent all connection types; data availability depends on eligibility criteria (sections “Current dimensions,” “Form factor,” and “Optional dimensions”).
- **Limitations:** This page documents schema/category semantics, not the validity of the classifications as physical hardware or network measurements. ECT must not be read as literal access technology. Current documentation may evolve; Zotero metadata contains no snapshot date.
- **Relationship to T1.3:** Helps map CrUX segments to profile labels while warning that dimensions represent classifications, not full device/network configurations.
- **Important anchors:** Current dimensions and eligibility, lines 47–51; form factor, lines 53–61; optional dimensions and NULL semantics, lines 68–72. No page numbers.
- **Concise takeaway:** CrUX form factor and ECT are useful segmentation labels, but they do not specify a reproducible physical device or network path.

## T1.3 Evidence Check

- **Documentation-supported:** Category values and their described semantics.
- **Not established:** Classification accuracy, population coverage, or profile fidelity.
- **Researcher inference:** Preserve raw CrUX dimensions when deriving profile distributions and separately define browser, hardware, and network settings.

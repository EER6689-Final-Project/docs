# Steiner and Gao 2016 - What slows you down? Your network or your device?

- **Citation:** Moritz Steiner and Ruomei Gao. “What slows you down? Your network or your device?” arXiv:1603.02293 [cs.NI], version 1, 7 March 2016. https://doi.org/10.48550/arXiv.1603.02293.
- **Zotero key:** `Q2T3R76T`.
- **Provenance:** Zotero record is a preprint and links to arXiv; attached PDF is 12 pages and identifies itself as arXiv v1. The arXiv record confirms title, authors, and submission date. No journal or conference publication is identified in the record or PDF examined.
- **Source access:** Read the attached Zotero PDF with `zotero_get_item_fulltext` and pages 8–12 with `zotero_read_pdf_pages`. PDF text extraction garbles some figures and Table 2; quantitative chart interpretation is therefore limited to values stated in the prose and legible table entries. The article itself notes that user-agent-based identification of iPhone hardware was unavailable.

## Abstract and scope

The study asks how device capability and network type affect mobile web page load time (PLT), using real-user measurements rather than isolated object-transfer logs. It is directly relevant to profile construction because it shows why an observed page timing cannot be attributed to a device or network without controlling the other factors and the page.

## Outline Summary

- **Approach:** Akamai inserted JavaScript into a small random sample (typically under 1% to 5%) of customer websites and collected Navigation Timing load events, browser/user-agent, IP-derived geography, and inferred network and device information. The March 2015 dataset contained about 2.5 billion entries. For comparisons, the authors selected one mobile e-commerce URL and controlled URL, network, or device as appropriate (Sections 2–5, pp. 2–10).
- **Results:** On the selected page, successive Android phone generations often had 18–30% lower median PLT; iOS-version comparisons showed up to 56% median reduction, but hardware and software contributions could not be separated. Comparing four U.S. mobile networks on one URL and iOS 8.1 device, the fastest cellular network had a 14% lower median PLT than the slowest. A fiber connection with Wi-Fi was 18% faster than the fastest and 28% faster than the slowest cellular network. In France, a DSL-plus-Wi-Fi median was 19% slower than the fastest cellular network (Sections 4–5, pp. 6–10).
- **Limitations:** The dataset comes from one CDN provider and participating customer sites, with selective sampling; it is observational and does not isolate causality. User-agent data could not identify iPhone hardware, so iOS-version differences combine hardware and software. Safari did not implement Navigation Timing in the comparison, making Safari and Chrome timings not directly comparable. The device analysis is constrained to one selected URL and does not compare smartphones with laptops/tablets because page variants differ. Site, audience, network, and device composition can confound broader comparisons (Sections 2–6, pp. 2, 5–11).
- **Author-stated implications:** Compare a factor only after holding the other factors constant; Navigation Timing offers page-level events while Resource Timing can expose individual resource timings (Section 6, p. 11).
- **Relationship to T1.3:** Strong rationale for treating device/network profiles as separate configurable dimensions and using RUM distributions to ground profile choices. The paper does not validate synthetic emulation or establish that a throttled desktop reproduces a real mobile device.
- **Important source anchors:** Data collection and scope, §2–3 (pp. 2–5); device comparison, §4 (pp. 5–9); network comparison, §5 (pp. 9–10); discussion, §6 (p. 11); conclusion, §8 (p. 12).
- **Concise takeaway:** Real-user PLT reflects the joint effects of device, network, and page; comparisons become interpretable only when the remaining factors are controlled.

## T1.3 Evidence Check

- **Paper-supported:** The dataset, instrumentation, selected comparisons, reported percentages, and stated measurement constraints above are described in the attached PDF.
- **Not established:** That any fixed synthetic profile represents a population, that CPU/network throttling reproduces physical devices or live paths, or that the 2015 sample generalizes to current web workloads.
- **Researcher inference:** Use the results as design evidence for stratifying profiles and controlling factors, not as contemporary device targets or a validation result for the proposed profiler.

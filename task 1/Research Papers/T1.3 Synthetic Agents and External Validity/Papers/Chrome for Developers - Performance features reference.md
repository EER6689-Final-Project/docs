# Chrome for Developers - Performance features reference

- **Citation:** Chrome for Developers. “Performance features reference.” Chrome DevTools documentation, current live documentation, accessed 12 October 2026. https://developer.chrome.com/docs/devtools/performance/reference.
- **Zotero key:** `WU62T7AT`.
- **Source type:** Official browser developer-tool reference.
- **Provenance/access:** Zotero stores an imported HTML snapshot (`AXAKKINJ`) and canonical URL. The live reference page was consulted; no fixed version or document date is recorded in Zotero.

## Abstract and scope

Documents Chrome DevTools Performance panel controls and interpretation features, including CPU throttling and calibration. It specifies product behavior rather than experimentally establishing how well emulation represents a physical phone.

## Outline Summary

- **Source findings:** The reference instructs users to choose a CPU throttling level in capture settings and points to calibrated custom presets for better matching of low- and mid-tier mobile devices (section “Throttle the CPU while recording,” lines 183–189).
- **Limitations:** A control description does not provide population device benchmarks, cross-machine invariance, or a fidelity evaluation. The documentation changes with Chrome releases; the Zotero record does not pin a Chrome version.
- **Relationship to T1.3:** Supports implementing and recording CPU-throttling settings and calibration version. Read together with the DevTools calibration article, it should not be treated as proof of full device emulation.
- **Important anchors:** CPU throttling and calibration, lines 183–189. No page numbers.
- **Concise takeaway:** DevTools offers calibrated CPU presets as a practical approximation; the reference alone does not validate broader device equivalence.

## T1.3 Evidence Check

- **Documentation-supported:** Setting CPU throttling and calibrating custom presets are documented features.
- **Not established:** Performance equivalence across physical devices or simulation of non-CPU hardware.
- **Researcher inference:** Record Chrome version, calibration state, and preset with each synthetic run.

# Emulation - Chrome DevTools Protocol

- **Source type:** Official protocol documentation / tool interface.
- **Zotero key:** `UKNA4QJZ`.
- **Provenance:** Zotero URL https://chromedevtools.github.io/devtools-protocol/#/Emulation; attached HTML snapshot `ZA82K2H3`. Current protocol page: https://chromedevtools.github.io/devtools-protocol/tot/Emulation/.

## Source-supported details

The Emulation domain defines commands for overriding device metrics, touch behavior, user-agent metadata, CPU throttling, geolocation, and other browser-visible conditions. For example, `Emulation.setDeviceMetricsOverride` accepts viewport dimensions, device scale factor, and a mobile flag (protocol documentation, method definitions).

## Use and limits

This documents browser-side emulation controls. It does not establish that an emulated viewport, user agent, CPU rate, or touch mode is equivalent to physical hardware or real users. The protocol’s “tot” documentation is explicitly mutable and does not guarantee backward compatibility; record browser and protocol versions for reproducibility.

**Researcher inference:** Treat protocol commands as controllable inputs to a synthetic agent. Validate the resulting behavior against real devices when claims concern device-level external validity.

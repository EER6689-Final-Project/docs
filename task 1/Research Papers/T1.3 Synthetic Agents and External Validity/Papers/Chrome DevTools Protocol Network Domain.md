# Network - Chrome DevTools Protocol

- **Source type:** Official protocol documentation / tool interface.
- **Zotero key:** `YLRND2GP`.
- **Provenance:** Zotero URL https://chromedevtools.github.io/devtools-protocol/#/Network; attached HTML snapshot `L3QJ4HDI`. Current protocol page: https://chromedevtools.github.io/devtools-protocol/tot/Network/.

## Source-supported details

The Network domain exposes browser network events and controls, including request interception and network-condition emulation. Current documentation marks `Network.emulateNetworkConditions` deprecated in favor of `emulateNetworkConditionsByRule` together with `overrideNetworkState`; the newer command can apply conditions by URL pattern (Network domain, method definitions).

## Use and limits

This is a browser control and observation interface. A configured latency or throughput cap is a synthetic condition; it does not recreate all properties of a carrier network, such as radio variability, handovers, DNS behavior, congestion, or shared access. The “tot” protocol schema changes over time.

**Researcher inference:** Report the exact emulation method and browser version, and avoid describing DevTools network shaping as a real mobile-network sample without validation.

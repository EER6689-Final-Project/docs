# tc-netem(8) — Linux Network Emulator

- **Source type:** Operating-system manual / network emulation documentation.
- **Zotero key:** `EPH3DPP2`.
- **Provenance:** Zotero URL https://man7.org/linux/man-pages/man8/tc-netem.8.html; attached snapshot `99H8YC2E`. Current Linux man-pages page: https://www.man7.org/linux/man-pages/man8/netem.8.html.

## Source-supported details

`netem` is a queue discipline for testing protocols by emulating packet-level network properties. The manual documents delay, jitter and delay distributions, random/state/burst loss, corruption, duplication, reordering, rate limits, and reproducible random seeds. It also warns of limitations from kernel timer granularity and queue placement; realistic TCP testing may require applying netem at the receiver’s ingress (manual sections DESCRIPTION, OPTIONS, LIMITATIONS).

## Use and limits

This is a capability reference for controlled network experiments, not evidence that a chosen impairment profile represents a specific population’s network. Interactions among impairments, kernel behavior, and placement affect results.

**Researcher inference:** For external validity, a reproducible netem profile should be justified from observed target-network data; it cannot substitute for observing mobile access variability by itself.

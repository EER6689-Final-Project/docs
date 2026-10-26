# Klotski: Reprioritizing Web Content to Improve User Experience on Mobile Devices

## Identity and access

- **S-0013**, R3/R6. Michael Butkiewicz, Daimeng Wang, Zhe Wu, Harsha V. Madhyastha, Vyas Sekar. USENIX NSDI 2015, pp. 439–453.
- Official venue: <https://www.usenix.org/conference/nsdi15/technical-sessions/presentation/butkiewicz>; PDF: <https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-butkiewicz.pdf>.
- `Klotski 2015.pdf`, **16 PDF pages including cover**; SHA-256 **9bf3778acc403cc8bef03f2acdc5260b735316dbf05a3a932302c05aa5580ec1**. Copied from Luna's original official-venue scratch download. Fresh Sol retrieval returned HTTP 403, not a new successful download; existing cover identifies venue and work. No Zotero work key resolved here; no assertion of library absence. No verified DOI is asserted; the handoff's 10.5555 catalog identifier is omitted.
- Sol, 2026-10-25, `ERP-2026-10-25-v1.0`: reopened cover, PDF pp. 3 and 10; p. 10 visually checked. Keyword hits elsewhere were navigation, not systematic full-paper review.

## Claim-to-source extraction

### C-T1.6-052 — Two distinct sample definitions

**Proposed claim:** Most Klotski system experiments use landing pages of 50 randomly chosen Alexa top-200 websites; a separate motivation comparison uses 100 randomly chosen top-2000 websites. They must not be conflated.

**Exact original:** §8.1, printed proceedings p. **447**, paper internal p. **9**, PDF p. **10**: “For most of our experiments, we use the landing pages of 50 websites chosen at random from Alexa's top 200 websites.” §2, printed proceedings p. **440**, internal p. **2**, PDF p. **3**, paragraph “Limitations of performance optimizations”: “we pick the landing pages of 100 websites chosen at random from the top 2000 websites” to compare existing optimizations. The preceding paragraph describes initial top-200 measurements, a third distinct context.

**Setup/comparison:** §8.1 p. 447/PDF 10 reports HTC Sensation, Android 4.0.3, Chrome 34.0.1847.116, WiFi hotspot via Mac Mini/T-Mobile 4G dongle, EC2 US West front end. §8.2 on the same page says the client loads first without optimization, then via Klotski; comparator is an unmodified proxy. This is stated order, not randomized arm order. Outcome is delivery of user-valued resources within a time budget, not generic instrumentation conformance.

**Units/analysis boundary:** Page loads within sites/device/proxy context; site-level utility distributions, not independent user experience for the entire web. Replication counts for the primary system evaluation are not established by this bounded read; do not reuse the five-load motivation statement as its replication count. No figure-derived effect sizes retained.

**Support: confirmed** for the two original sample descriptions, **qualified** for any browser-design transfer. **Methodological confidence: higher** for identity/count extraction; **limited** for generalized causal/browser-profiler inference. Dependency group `DG-Klotski`: same paper/proxy/device/site frame; not independent samples of all web usage. Related to Polaris S-0014 through method comparison, not an independent replication of Polaris.

**Conditional inference:** If a live-page study is approved, distinguish frame, selection and analysis subset, and counterbalance/reset paired conditions rather than copying this source's fixed order.

## Design-specific appraisal

- Frame/unit **adequate** for stated ranked subset; **concern** for broad web/user inference.
- Comparator **adequate**: explicit vanilla-proxy comparison, but proxy/device context is specialized.
- Allocation/order/cache **concern**: stated baseline-then-treatment order; cache/state randomization not established in checked passages.
- Construct **adequate** for defined utility objective; **concern** for treating utility or proxy optimization as timing-tool accuracy.
- Uncertainty/replication **unclear** for main evaluation from the retained passages; plots not used as uncertainty evidence here.

## Passage QC — QC-052

Sol original-passage recheck, 2026-10-25; **not independent human/scientific review**. **checked-corrected**: handoff's PDF page anchors were offset by cover inclusion, and its hash label was swapped with Tranco. Expanded finite retained set: C-T1.6-052 in both §2 and §8.1 contexts, plus comparator/order context in §8.2. Neither 100-of-2000 nor initial top-200 is the primary system sample. No novel-work absence or gate conclusion.

## Copy receipt

Source: `/tmp/opencode/eei6689-t16-supporting/klotski-paper.pdf`; new target `Klotski 2015.pdf`, 1,360,188 bytes. Exact bytes preserved; source/target SHA-256 checked, no existing target overwritten. Original official-venue provenance is Luna's retrieval plus Sol cover/identity review; the failed fresh HTTP 403 does not replace that receipt with a new successful retrieval claim.

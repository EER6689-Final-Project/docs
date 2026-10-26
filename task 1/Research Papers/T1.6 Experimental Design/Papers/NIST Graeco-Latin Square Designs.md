# NIST/SEMATECH — Graeco-Latin square designs

## Identity and access

- **S-0018**, R4/R6. NIST/SEMATECH e-Handbook §**5.3.3.2.2**; My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), webpage **T2YDS3PP**.
- <https://www.itl.nist.gov/div898/handbook/pri/section3/pri3322.htm>, live official full returned text re-opened by Sol **2026-10-25**; no immutable revision/hash. Prior Luna raw extraction: `/tmp/opencode/eei6689-t16-supporting/raw/nist-graeco-latin.json`. No original PDF attachment identified in prior metadata; no substitute PDF generated.
- `ERP-2026-10-25-v1.0`. Bounds: **opening two prose sections only for retained evidence**, not validation of displayed matrices, level labels or linked literature. No formulas/tables or run counts used.

## Claim-to-source extraction

### C-T1.6-057 — Restricted design, not a generic browser recipe

**Claim:** NIST describes Graeco-Latin squares for one treatment factor with three nuisance factors, restricted to equal numbers of levels, and recommends randomization only as far as the design allows.

**Exact original anchors:** **These designs handle 3 nuisance factors**: “efficient designs to study the effect of one treatment factor in the presence of 3 nuisance factors”; next sentence restricts all factors to the same number of levels. **Randomize as much as design allows**: “be sure to randomize the treatment units and trial order, as much as the design allows.” Following sentence suggests randomly selecting a square from those available, then randomizing run order.

**Design/unit/assumptions:** Structured treatment/block allocation guidance, not an empirical browser study. No browser metric, cache policy, missingness repair or repeated-measure uncertainty estimator is supplied. This opening prose does not establish estimability under arbitrary interactions or missing runs; no such claim is retained. Printed PDF pagination **not applicable**; named web headings are exact anchors.

**Conditional interpretation:** Only consider this design after approval and after checking factor-level compatibility, interaction assumptions, units, state/carryover and feasible allocation. It is not automatically suitable because a browser experiment happens to have several nuisance factors.

**Support: confirmed** for restricted scope and recommendation; **qualified** for browser adaptation. **Methodological confidence: higher** for documented scope; **limited** for browser use without a model/allocation justification. Dependency group `DG-NIST-design`, shared handbook with S-0017/S-0019/S-0020, not independent empirical corroboration.

## Appraisal and QC

- Stated design scope **adequate**: treatment/nuisance roles and equal-level restriction explicit in prose.
- Model/interaction/missingness transfer **concern**: not justified by the opening guidance for arbitrary browser settings.
- Version **unclear**: live page, no revision captured; normative force **adequate** as attributed handbook advice, not browser conformance.
- Browser empirical validity/uncertainty **not applicable**: not tested here.
- **QC-057**, Sol, 2026-10-25: **checked-no-discrepancy**, full retained set C-T1.6-057 rechecked against both original prose sections. No displayed design validated or copied. Separate passage pass after Luna, **not independent human/scientific review**. No gate or scope approval.

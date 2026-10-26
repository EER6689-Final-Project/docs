# NIST/SEMATECH — Randomized block designs

## Identity and access

- **S-0017**, R4/R6. NIST/SEMATECH e-Handbook §**5.3.3.2**. My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), webpage **FBTV2ICM**; no original PDF attachment in Luna's metadata reading.
- <https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm>, live official page re-opened by Sol **2026-10-25**, full returned text. No revision/date/hash captured; no linked section audit. Luna raw prior extraction: `/tmp/opencode/eei6689-t16-supporting/raw/nist-block.json`.
- `ERP-2026-10-25-v1.0`; methodological analogue, **not browser validation**. No formulas, run matrices, numerical worked examples or effect estimators are adopted; those displays have not received a visual mathematics check in this pass.

## Claim-to-source extraction

### C-T1.6-056 — Blocking and residual randomization

**Claim:** The handbook recommends holding controllable nuisance conditions constant in homogeneous blocks while varying the treatment within blocks, and randomizing remaining nuisance influences. This does not by itself make browser runs independent or remove state/carryover.

**Original anchors:** **Blocking used for nuisance factors that can be controlled**: “create homogeneous blocks in which the nuisance factors are held constant and the factor of interest is allowed to vary.” **Definition of blocking factors** says each primary-factor level occurs equally often with each nuisance-factor level. **Block for a few of the most important nuisance factors**: “Block what you can, randomize what you cannot.” Following sentence assigns randomization to remaining nuisance variables. This is handbook design guidance, not a requirement imposed by a browser specification.

**Methods context:** Process-improvement examples with one primary factor and nuisance factors. Browser treatment/unit hierarchy, cache resets and time drift are not defined here. The illustrative furnace randomization is not a universal instruction to randomize browser arm order identically. The displayed additive model is not adopted as a validated browser model.

**Interpretation/conditional transfer:** If scope is approved, declare treatment, experimental unit, block factors, allocation within blocks, state reset, nesting and remaining nuisance before running. Treat blocking as conditional nuisance control, not proof against arbitrary interactions/unmeasured drift. Replication and uncertainty require a separate design justification.

**Support: confirmed** for handbook guidance, **qualified** for browser transfer. **Methodological confidence: higher** for the stated guidance; **limited** for untested browser adaptation. Dependency group `DG-NIST-design`: S-0017–S-0020 share one handbook, not four independent browser studies.

## Appraisal and QC

- Method/estimand **adequate** for the declared primary-vs-nuisance distinction; browser estimand/unit **unclear** until specified.
- Exchangeability/dependence **concern** for automatic browser transfer: nuisance balance is not independence or carryover removal.
- Normative/version scope **adequate** for attributed guidance, **unclear** for historical revision (not captured).
- Browser implementation/empirical effect **not applicable**: source offers neither browser results nor a validated browser run count.
- **QC-056**, Sol, 2026-10-25: **checked-no-discrepancy**, C-T1.6-056 original prose re-opened including balance/randomization context; no tabular/formula claims retained. Separate pass after Luna, **not independent human/scientific review**. No scope or gate approval.

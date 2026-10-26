# NIST/SEMATECH — Full factorial designs

## Identity and access

- **S-0019**, R4/R6. NIST/SEMATECH e-Handbook §**5.3.3.3**; My Library (personal; local libraryID 1, orchestrator MCP check 2026-10-26), webpage **V8C28N5J**.
- <https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm>, live official page, full returned text re-opened by Sol **2026-10-25**; immutable revision/hash not captured. Luna's previous raw extraction: `/tmp/opencode/eei6689-t16-supporting/raw/nist-full-factorial.json`. No original attached PDF in prior metadata; none fabricated.
- `ERP-2026-10-25-v1.0`. Retained evidence is definitional prose only. Displayed run-count table/exponent formula and linked guideline table are **not used** or independently visually validated here.

## Claim-to-source extraction

### C-T1.6-058 — Complete factor crossing

**Claim:** NIST defines a full factorial design by inclusion of every setting of every factor with every setting of the other factors. Complete crossing alone does not specify browser replication, allocation order, or independence.

**Exact original anchor:** opening italic definition under **Full factorial designs in two levels**: “A design in which every setting of every factor appears with every setting of every other factor is a full factorial design.” Following paragraph names all possible high/low combinations for two-level inputs. This is design terminology, not evidence that any particular browser factor set is sufficient.

**Context/boundary:** The page also recommends smaller designs when full crossing becomes costly; that resource advice is not adopted here as a numerical threshold or mandatory factor limit. No run-count formula/table is required for this retained claim. Units, estimand, repetitions, nuisance drift and uncertainty remain project choices.

**Conditional inference:** If a crossed profiler/browser/network design is approved, specify each factor and level, primary interactions, experimental unit, repetitions and order/state controls. A factorial cell is not an independent replication and does not on its own remove site/time dependence.

**Support: confirmed** for definition; **qualified** for browser transfer. **Methodological confidence: higher** for terminology; **limited** for an unspecified browser design. Dependency group `DG-NIST-design`, same handbook as S-0017/S-0018/S-0020, not independent empirical evidence.

## Appraisal and QC

- Definition **adequate**: original prose explicit; model assumptions for browser inference **unclear** until chosen.
- Unit/dependence/drift **concern** for automatic transfer: crossing does not prescribe allocation or eliminate correlation.
- Version **unclear**: undated mutable page without pinned revision; normative force **adequate** as attributed definition, not project approval.
- Browser validation/uncertainty **not applicable** to definition-only source.
- **QC-058**, Sol, 2026-10-25: **checked-no-discrepancy** for C-T1.6-058, original opening prose and surrounding scope re-opened. No formula/table or numeric resource recommendation promoted. Separate pass after Luna, **not independent human/scientific review**. No gate or scope approval.

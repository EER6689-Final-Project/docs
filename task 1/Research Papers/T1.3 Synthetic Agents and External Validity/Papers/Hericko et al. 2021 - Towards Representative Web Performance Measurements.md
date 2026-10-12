# Towards Representative Web Performance Measurements with Google Lighthouse

- **Citation:** Heričko, T., Šumak, B., & Brdnik, S. (2021). Towards representative web performance measurements with Google Lighthouse. *Proceedings of the 2021 7th Student Computer Science Research Conference (StuCoSReC)*, 39–42. University of Maribor Press. https://doi.org/10.18690/978-961-286-516-0.9
- **Zotero key:** `DJI5ULJD`.
- **Source:** Zotero-attached 4-page PDF. PDF pages 1–4 correspond to printed pages 39–42. Citation details were reconciled against the University of Maribor Press proceedings record and its DOI; the Zotero record is incomplete and partly incorrect.

## Research question and approach

The authors examine how previous studies handled variability in Lighthouse performance measurements, then test repeated runs on ten websites. The experiment used Lighthouse 7.3.0, headless Chrome, macOS 10.15.7, desktop emulation, and broadband. Each website was measured with N=1, 5, 10, and 100 consecutive independent runs (PDF pp. 1–2, §§1–3).

## Findings from the source

- The literature search retrieved 134 studies and retained eight primary studies after screening. More than half of those retained studies used no stated strategy to address variability (PDF p. 2, §2).
- For most tested sites, scores varied across runs and occasional measurements were atypical. The authors report that the 5-, 10-, and 100-run median comparisons were not statistically different for the tested websites where Mood’s median test could be performed; they recommend five runs aggregated by median as a practical strategy in this experiment (PDF pp. 3–4, §§4–5, Tables 2–3).

## Relevance and limits

This is direct evidence that single Lighthouse runs can be unrepresentative of repeated measurements under a fixed test setup. Five runs are a result of this small experiment, not a universal sample-size guarantee. The test covered ten sites selected from the Alexa Top 500, one Lighthouse/Chrome/macOS configuration, and one short time window (PDF pp. 2–4, §3). Repeating a lab run addresses run-to-run noise; it does not by itself establish external validity against real-user field experience.

**Researcher inference:** If Lighthouse is used as an agent’s measurement instrument, repeated runs and a declared aggregation rule are justified, while representativeness still requires an independently defined target population and field comparison.

## Provenance and metadata correction

The PDF first page identifies Tjaša Heričko, Boštjan Šumak, and Saša Brdnik. The official proceedings metadata verifies StuCoSReC 2021 and pp. 39–42; the DOI is `10.18690/978-961-286-516-0.9`. Zotero currently has no author or year, calls the item “(PDF) …”, and incorrectly stores ResearchGate as “Proceedings Title”; its ISBN matches the volume. These are documented here without altering Zotero.

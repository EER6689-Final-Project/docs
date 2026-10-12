# Sengupta et al. 2024 - Through the Lens of Google CrUX

- **Citation:** Jayasree Sengupta, Tanya Shreedhar, Dinh Nguyen, Robert Kramer, and Vaibhav Bajpai. “Through the Lens of Google CrUX: Dissecting Web Browsing Experience Across Devices and Countries.” In *2024 IFIP Networking Conference (IFIP Networking)*, Thessaloniki, Greece, 3–6 June 2024, pp. 509–514. IEEE, 2024. https://doi.org/10.23919/IFIPNetworking62109.2024.10619890. The attached PDF is arXiv:2308.06409v2, dated 18 April 2024. The Zotero parent item is typed as a preprint and its date is the arXiv v2 date; cite the proceedings DOI for the published paper. The proceedings contents page lists four authors, while the attached PDF and arXiv record list five including Dinh Nguyen; the author record merits bibliographic follow-up.
- **Zotero key:** `9IDW7B5Y`.
- **Provenance:** Zotero preprint with attached 9-page PDF. The PDF notes acceptance at IFIP Networking 2024 in its attached Zotero note; the conference paper record verifies published venue and pages. The dataset is Google CrUX.
- **Source access:** Read the full attached PDF using Zotero full text and pages 6–9 for country results and limitations. Extraction garbles figures/table layout; prose and the legible country table were used. arXiv metadata and an indexed conference record were consulted to distinguish preprint from proceedings citation.

## Abstract and scope

The paper examines aggregated Chrome User Experience Report (CrUX) data across device types and nine European countries. It provides a concrete example of field distributions that may inform synthetic profile design, while also showing that the resulting evidence applies only to the eligible Chrome population and the dataset’s aggregation scheme.

## Outline Summary

- **Approach:** The authors analyze monthly CrUX data, describing four timing metrics (First Paint, First Contentful Paint, DOM Content Loaded, and Onload) and segmenting by effective connection type, device/form factor, country, and time. The paper considers three device classes and nine European countries (Germany, Great Britain, France, Italy, Spain, Sweden, Finland, Poland, Romania) (Sections II–III, pp. 2–7).
- **Results:** Desktop timing distributions generally outperform phones and tablets; tablets have the slowest timings despite high 4G share. For 4G connections, Sweden and Finland have the highest shares (85.99% and 81.41%). At the 75th percentile, Sweden and Finland are reported as 25–36% better than Italy across the studied metrics (Table I and §III, pp. 5–7).
- **Limitations:** CrUX metrics are aggregated by origin into normalized histograms, limiting origin-level temporal interpretation. The data represents Chrome users who opt in to usage reporting, not all browser or phone users; included origins are those known to Google’s crawler. The authors identify the need for finer connection-speed categories, origin-level segmentation, and validation with other browsers (Section IV, p. 7).
- **Author-stated future work:** Expand connection categories, study origin-specific and mobile-versus-desktop origins, validate with other browsers (including default mobile browsers), and investigate explanations for geographic differences (Section IV, p. 7).
- **Relationship to T1.3:** Shows how field distributions can guide dimensions and percentile targets for RUM-informed profiles. It does not provide individual device CPU specifications or validate a synthetic agent against CrUX; country/device associations remain observational and may include confounding.
- **Important source anchors:** Data and metric definitions, §II (pp. 2–4); device analysis, §III-A (pp. 4–5); country comparison and Table I, §III-B (pp. 5–7); limitations/future work, §IV (p. 7); conclusion, §VI (p. 9).
- **Concise takeaway:** CrUX can supply population-level timing distributions by broad dimensions, but its opt-in Chrome sample and origin aggregation constrain what a synthetic profile can claim to represent.

## T1.3 Evidence Check

- **Paper-supported:** Study dimensions, metric definitions, reported device/country patterns, and dataset limitations are described in the paper.
- **Not established:** Representative coverage of all web users, causal reasons for country/device differences, or mapping CrUX segments to specific synthetic hardware settings.
- **Researcher inference:** Profiles can be grounded in percentile distributions, provided they are labeled as design targets and tested for sensitivity to CrUX’s sampling and aggregation limits.

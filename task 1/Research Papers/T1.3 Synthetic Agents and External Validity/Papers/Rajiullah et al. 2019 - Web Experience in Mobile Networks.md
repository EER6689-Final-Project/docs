# Web Experience in Mobile Networks: Lessons from Two Million Page Visits

- **Citation:** Rajiullah, M., Lutu, A., Khatouni, A. S., Fida, M., Mellia, M., Alay, Ö., Brunstrom, A., Alfredsson, S., & Mancuso, V. (2019). Web experience in mobile networks: Lessons from two million page visits. *Proceedings of the 2019 World Wide Web Conference (WWW ’19)*, 1532–1543. ACM. https://doi.org/10.1145/3308558.3313606
- **Zotero key:** `H2BXWLHZ`.
- **Source:** Zotero-attached 12-page ACM paper; page references below are PDF pages, which correspond to the paper’s conference pagination beginning at p. 2367.

## Research question and approach

The study measures how access technology, mobility, browser, and protocol affect mobile-web performance. Its MONROE campaign used about 100 nodes in four European countries and eleven commercial mobile networks over two months, recording nearly two million page visits. The design varied Ethernet/3G/4G access, Chrome/Firefox, and HTTPS/HTTP/2/QUIC; 20 popular pages were selected (PDF pp. 1–4, §§1, 3.1).

The authors report three browser metrics: First Paint, Page Load Time, and RUMSpeedIndex. They explicitly caution that these metrics describe different aspects of page loading and should be compared within the same metric rather than treated as interchangeable (PDF p. 3, §3.2).

## Findings from the source

- Mobile broadband increased median page-load time by about one third relative to wired access; mobility added penalties, especially around handovers (PDF pp. 1–2, abstract and §1).
- In the measured in-the-wild conditions, HTTP/2 and QUIC showed marginal or inconsistent benefit over HTTPS, with no significant benefit in 55% of wired back-to-back comparisons; access technology, mobility context, webpage composition, and browser were significant factors in the analysis (PDF pp. 1–2, abstract and §1; see also §§5–7).
- The paper releases its dataset for validation and follow-on work (PDF pp. 1–2, abstract and §1).

## Relevance and limits

This is a useful empirical reminder that performance measurements depend on access network and mobility context, and that a controlled synthetic profile cannot stand in for these contexts without validation. Its own large-scale campaign is still bounded: four European countries, eleven providers, a selected set of 20 popular pages, two browsers from the study period, and a two-month window. The authors also state that even their controlled setup leaves the mobile web ecosystem difficult to disentangle (PDF pp. 1–3, §§1–2).

**Researcher inference:** This supports stratifying or recording network and device context when assessing synthetic agents, and limits broad claims from one emulated setup to all users or markets.

## Provenance and verification

Zotero metadata matches the paper’s PDF first-page ACM reference block: title, nine authors, WWW ’19, ACM, DOI, and ISBN. The attached PDF also confirms the MONROE design and metric definitions (PDF pp. 1–3).

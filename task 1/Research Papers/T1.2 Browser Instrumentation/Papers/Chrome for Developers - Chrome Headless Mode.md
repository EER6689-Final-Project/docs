# Chrome Headless Mode

- **Citation:** Bynens, M., & Kvitek, P. *Chrome Headless mode*. Chrome for Developers, accessed 12 October 2026. https://developer.chrome.com/docs/automation-and-testing/headless
- **Zotero key:** XV62BFGD (ChromeHeadlessMode).
- **Source:** Official Chrome for Developers documentation; page states last updated 21 October 2024.

## Summary

- **Purpose and content**
  - Explains running Chrome without a visible UI using the --headless flag and gives examples for command line, Puppeteer, and Selenium.
  - States that since Chrome 112, Headless creates platform windows without displaying them while sharing Chrome's code. Since Chrome 132.0.6793.0, the old separate Headless implementation is available only as the standalone chrome-headless-shell binary.
  - Puppeteer's examples distinguish headless: true (unified Chrome Headless), headless: 'shell' (Headless Shell), and headless: false (headful).
- **Research questions and evidence type**
  - N/A — product/automation documentation, not an empirical comparison of timing, accuracy, or headless/headful performance.
- **Experimental setup, dataset, and metrics**
  - N/A. The page gives launch instructions and implementation history, but no controlled workload, participants, benchmark metrics, or measured results.
- **Limitations and interpretation**
  - The page describes supported modes and commands; it does not prove that headless and headful runs are performance-equivalent, visually identical, or equally detectable by websites.
  - Mode names and implementations changed over time. Record the Chrome build and precise mode (headless, headless-shell, or headful) when describing a run.
- **Relationship to our profiler**
  - **Preliminary inference:** browser mode belongs in run provenance. This source can identify which implementation a command selects; it cannot establish observer effect or measurement validity.
- **Important section anchors**
  - Paraphrase anchors: introductory description and Chrome 112 behavior; “Use old Headless mode” and Chrome 132 note; Puppeteer mode options. No page numbers.

## T1.2 Evidence Check

- **Qualified:** Operational guidance, not an empirical paper and not evidence of headless/headful performance equivalence.
- **Preliminary inference:** Store selected Headless implementation and browser version in experiment metadata if these modes are used.

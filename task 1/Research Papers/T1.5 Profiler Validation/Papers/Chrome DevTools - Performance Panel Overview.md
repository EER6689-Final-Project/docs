# Chrome DevTools — Performance Panel Overview

- **Citation:** Chrome for Developers. “Performance panel: Analyze your website’s performance.” [Documentation](https://developer.chrome.com/docs/devtools/performance/overview).
- **Zotero key:** `VMWYVJKL` (webpage; imported HTML snapshot attached).
- **Source access:** Current official documentation checked 13 October 2026.

## Outline Summary

- **Scope:** The Performance panel records CPU profiles and supports capture-setting changes, report inspection, and analysis of runtime/load recordings.
- **Live metrics and capture effects:** The current page describes local LCP/CLS and interaction-derived INP, with CrUX field-data comparison. It also warns that advanced paint instrumentation and CSS selector statistics significantly hinder performance; disabling JavaScript samples reduces overhead.
- **Project relevance:** DevTools is a useful reference implementation and diagnostic interface, but optional capture settings can perturb the observed execution. Its local and field values have different data scopes.
- **Limit:** Mutable product documentation, not a fixed protocol or controlled validation experiment. UI behavior and metric support can change by Chrome version.

## T1.5 Evidence Check

- **Source-supported:** Documented panel capabilities and the explicit capture-setting overhead warnings.
- **Researcher inference:** Pin the Chrome version and settings when using panel output as a comparison target.

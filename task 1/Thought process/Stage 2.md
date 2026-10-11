# Stage 2 - High-Level Research Plan

## Purpose of this stage

Stage 2 defines what must be learned from existing research before selecting a research gap or designing the profiler experiment. It does not decide what the thesis will prove. The investigation must remain open to several possible conclusions rather than searching only for evidence that supports a preferred implementation.

The scope established in [[Stage 1]] remains the governing boundary:

> The profiler owns the live browser-performance measurement process and exposes a stable Application Programming Interface (API) through which other GreenCode modules provide inputs and consume results.

An API is a defined contract through which software components exchange data. Carbon estimation, artificial-intelligence recommendations, static analysis, authentication, and other subsystems are relevant only where they constrain this contract. The profiler should not need to understand how downstream modules calculate carbon or generate recommendations, and those modules should not need to understand the profiler's internal measurement process.

Stage 2 organizes the literature investigation around eight themes. The first five are essential because they are most likely to determine the final research problem. Scoring and test-corpus design are required but may remain supporting concerns. Instrumentation overhead is a potential threat that must be investigated.

## Research themes

### 1. Metric definitions and validity

A profiler is first a measurement system, so the research must establish exactly what each metric represents before deciding how to implement it. Candidate measurements include First Contentful Paint (FCP), Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), Total Blocking Time (TBT), Speed Index, Time to Interactive (TTI), server response time, network behaviour, main-thread activity, memory, and Document Object Model (DOM) size. The DOM is the browser's in-memory representation of a page's HTML structure.

For each important metric, the literature should determine:

- the phenomenon it is intended to represent;
- its formal definition and calculation;
- the browser events or observations it requires;
- whether it is observed directly or derived from several observations;
- whether it is intended for controlled laboratory tests, measurements from real users, or both;
- its known limitations and current relevance; and
- whether two tools can legitimately produce different values for it.

A direct measurement may be calculated from two timestamps:

$$
\text{request duration}=\text{response end}-\text{request start}
$$

Other metrics require interpretation. For example, a visual-loading metric may be calculated from a sequence of rendered frames rather than one timestamp. This distinction affects whether the custom profiler can reproduce a reference tool's result.

The expected output is a **metric definition matrix**:

| Metric | Meaning | Measurement source | Calculation | Limitations | Appropriate use |
| --- | --- | --- | --- | --- | --- |

Standards, browser specifications, authoritative documentation, peer-reviewed studies, and empirical metric research should supply this evidence.

### 2. Browser instrumentation

**Instrumentation** means adding or using mechanisms that observe a system's execution. Once the metrics are understood, the literature must determine where their underlying data can be obtained inside the browser.

The main candidate mechanisms are:

- **Browser Performance APIs:** JavaScript interfaces that expose navigation, resource, paint, and other performance entries.
- **Chrome DevTools Protocol (CDP):** a lower-level interface through which external software can control Chromium and access its Network, Runtime, Performance, Tracing, and Page facilities.
- **Chromium tracing:** detailed event-level records of JavaScript execution, rendering, style calculation, layout, painting, and task scheduling.
- **Puppeteer:** a browser-automation library that controls Chromium and can access CDP, but does not itself make every metric semantically equivalent.
- **Lighthouse:** an automated auditing system that gathers browser artifacts and derives metrics, audit results, and scores through its own processing pipeline.

The research must identify which metrics can be obtained directly from CDP or Performance APIs, which require trace processing or in-page scripts, and which are derived by Lighthouse. Similar names do not guarantee identical definitions or calculations:

```text
Custom CDP measurement != Lighthouse measurement by default
```

The investigation should also examine headless versus visible browser execution, abstractions introduced by Puppeteer, synchronization problems when combining data sources, and measurement overhead. The expected output is an instrumentation map connecting each metric to its browser phenomenon, available data source, candidate implementation, and known limitations.

### 3. Synthetic testing and real-user performance

The profiler launches a controlled browser to test a URL, which makes it a **synthetic performance-testing** system. Synthetic testing measures a website under deliberately defined browser, viewport, network, and Central Processing Unit (CPU) conditions.

**Real User Monitoring (RUM)** instead gathers performance observations from actual users with different devices, networks, locations, and browser states. The distinction limits what the profiler can claim. It can measure performance under a specified synthetic profile, but it cannot automatically claim to represent every user's real experience.

The literature should explain the strengths and weaknesses of both approaches, the relationship between laboratory and field measurements, and when synthetic results can be generalized. This establishes the study's **external validity**, meaning the extent to which findings from the experiment apply beyond its controlled environment. Emulating a mobile CPU or network does not necessarily reproduce every characteristic of a physical phone and real mobile connection.

### 4. Repeatability, variability, and reproducibility

Repeated tests of the same page can differ because of server response time, network conditions, caching, browser and operating-system scheduling, third-party scripts, dynamic content, nondeterministic JavaScript, garbage collection, CPU contention, browser startup state, content-delivery networks, advertisements, and service workers. A service worker is a background browser script that can intercept network requests and manage caches.

Three concepts must remain distinct:

- **Repeatability:** how similar measurements are when the same procedure is repeated under essentially the same conditions.
- **Reproducibility:** whether another researcher can recreate the procedure and obtain comparable results.
- **Accuracy:** how close a measurement is to a true value. This may be difficult to claim when no independent true value exists for a browser metric.

The literature must provide a methodological basis for the number of runs, warm-up and stabilization, cold or warm cache state, browser restart policy, outlier treatment, summary statistics, variability thresholds, confidence intervals, and environmental controls. A fixed number such as five runs should not be selected merely because it seems reasonable.

The expected output is a candidate repeatable-measurement protocol, not yet a final methodology.

### 5. Comparison with reference tools

The assignment requires comparison with Chrome DevTools or Lighthouse. Such evaluation must measure **agreement**, not rely only on correlation.

For example:

$$
\text{Reference}=[1,2,3,4,5]
$$

$$
\text{Profiler}=[2,4,6,8,10]
$$

These results are strongly correlated because they change together, but they do not agree because the profiler reports approximately twice the reference value. Correlation may therefore be supplementary, but it cannot establish equivalence.

The review should investigate absolute and relative error, Mean Absolute Error (MAE), percentage deviation, systematic bias, confidence intervals, and limits of agreement. MAE is the average absolute difference between paired values. **Bias** is a consistent tendency for one method to report higher or lower values than another. **Limits of agreement** estimate the range within which most differences between two methods fall.

Statistical comparison is only valid after confirming **semantic equivalence**: both values must represent the same phenomenon and use compatible start events, end events, units, test profiles, and conditions. Chrome DevTools and Lighthouse may be suitable references for different metrics rather than interchangeable references for all metrics.

The expected output is a framework stating what can be compared, which reference is appropriate, and which statistical methods are defensible.

### 6. Controlled browser, device, CPU, and network profiles

Desktop and mobile profiles, CPU throttling, and network throttling become experimental variables rather than simple configuration options.

- **Device and viewport emulation:** changing screen dimensions may also change responsive layouts and requested assets, so it can alter the workload itself.
- **CPU throttling:** intentionally reducing processing capacity can affect JavaScript execution, rendering, long tasks, and readiness for interaction, but browser throttling may not reproduce physical hardware exactly.
- **Network throttling:** a reproducible profile must specify latency, download and upload bandwidth, and any relevant packet behaviour. Labels such as “3G” are not precise enough by themselves.

The literature should determine how reliable browser emulation is, whether DevTools and Lighthouse use equivalent throttling strategies, whether their profiles are simulated or observed, how comparisons can use equivalent conditions, and which parameters must be reported for reproducibility.

### 7. Performance scoring and issue severity

The assignment requests a transparent performance score and severity classification, but combining unlike measurements can become methodologically arbitrary.

A **composite indicator** combines several variables into one result:

$$
S=w_1z_1+w_2z_2+\cdots+w_nz_n
$$

where $S$ is the overall score, $z_i$ is a normalized metric, and $w_i$ is its weight. Three decisions require evidence:

- **Normalization:** converting milliseconds, bytes, percentages, and counts to comparable scales.
- **Weighting:** justifying the relative importance assigned to each metric.
- **Thresholds:** defining what counts as good, moderate, poor, or critical.

The literature may support adapting an established score, developing a transparent custom model, or avoiding one overall score if aggregation would hide important differences. All three outcomes remain acceptable.

### 8. Test corpus and workload design

A **test corpus** is the collection of websites used in the experiment. The assignment requires static, image-heavy, JavaScript-heavy, and poorly optimized sites, but these categories and their representatives need a defensible selection method.

Real-world sites offer realism and complexity but change over time, depend on external services, and can be difficult to reproduce. Controlled benchmark sites are more deterministic and allow individual characteristics to be varied, but may not represent normal web complexity. A hybrid corpus may combine both strengths, but it is only a candidate strategy.

The literature should establish how studies select websites, define categories quantitatively, choose sample sizes, use local hosting, archive or freeze live sites, and manage dynamic content.

## Cross-cutting threat: instrumentation overhead

The profiler may alter the behaviour it measures. This is the **observer effect**: trace collection, event listeners, and data serialization consume resources and may change CPU or timing results.

```text
Normal run:       website -> browser workload
Instrumented run: website + tracing + listeners + serialization -> browser workload
```

The significance of this effect is not yet known. The literature should determine whether it needs to be measured, minimized, or reported as a limitation.

## Evidence strategy

Different questions require different evidence. The preferred hierarchy is:

1. **Standards and authoritative definitions:** World Wide Web Consortium (W3C) specifications, browser specifications, Chromium documentation, and official Lighthouse documentation for metric semantics and tool behaviour.
2. **Survey and review papers:** summaries of the field, common methods, debates, and known limitations.
3. **Peer-reviewed empirical studies:** evidence about browser behaviour, variability, benchmarking, reliability, and measurement validity.
4. **Tool-specific technical publications:** implementation details for Chrome, Puppeteer, Lighthouse, and Performance APIs.
5. **General web articles:** useful for discovering terminology, but insufficient as the main support for important thesis claims when stronger evidence exists.

Searches should be divided into literature families rather than one overly specific query:

- web-performance metrics and user-experience measurements;
- browser instrumentation, CDP, Chromium tracing, Puppeteer, and headless browsers;
- browser-benchmark repeatability, variability, and reproducibility;
- profiler validation and agreement between software measurement tools;
- systems-performance experimental design and repeated benchmarking; and
- composite scoring, normalization, weighting, and performance indices.

Broader systems-research literature may provide more mature experimental methods than web-specific publications.

## Requirements for a genuine research gap

A candidate gap must satisfy four conditions:

1. **Importance:** evidence must show that the underlying problem affects trustworthy performance measurement.
2. **Existing approaches:** the review must establish what researchers and tools already do about the problem.
3. **Demonstrated limitation:** empirical inconsistency, methodological criticism, contradictory findings, weak validation, or limited generalization must show that something remains unresolved.
4. **Fit and feasibility:** the unresolved issue must be investigable through the profiler and its evaluation, without requiring work outside the individual scope.

The useful region is therefore:

$$
\text{research significance}
\cap \text{unresolved evidence}
\cap \text{profiler scope}
\cap \text{project feasibility}
$$

Product novelty, such as building a particular dashboard combination for the first time, is not enough to establish a research gap.

## Evidence outputs

The literature review should produce more than paper summaries. For each important study, the evidence map should record:

| Field | Purpose |
| --- | --- |
| Research problem | Establish what was investigated |
| Measurement technique | Explain how data was collected |
| Browser, tool, and version | Assess reproducibility |
| Website corpus | Identify what was tested |
| Experimental environment | Record the conditions |
| Number of repetitions | Show how variability was handled |
| Metrics | Identify what was measured |
| Statistical method | Explain how conclusions were drawn |
| Findings | Record the available evidence |
| Limitations | Reveal possible unresolved problems |
| Relevance | Test whether the study applies to this profiler |

Together, the metric definition matrix, instrumentation map, candidate measurement protocol, reference-comparison framework, and study evidence map will support later gap identification and methodology design.

## Questions that must remain open

Chapter 3 methodology should not be finalized until the literature can justify decisions about:

- the Chromium version and whether to run headless or with a visible interface;
- how browser state, ordinary caches, and service-worker caches are reset;
- whether cold-cache, warm-cache, or both types of tests are required;
- whether a scan ends at the load event, after network inactivity, at another browser milestone, or after a fixed observation window;
- the number of runs, warm-up policy, and outlier treatment;
- exact network latency and bandwidth profiles;
- CPU throttling factors and their meaning across different hardware;
- website sample size, category definitions, hosting, and change control;
- whether DevTools, Lighthouse, or both are used, and which reference applies to each metric;
- acceptable agreement, systematic bias, uncertainty, and confidence intervals; and
- handling of missing metrics, failed requests, redirects, endless network polling, and pages that never become network-idle.

These behaviours are common in modern web applications and should not be dismissed as rare edge cases.

## Research questions versus implementation questions

The thesis must distinguish software-construction decisions from questions that can produce generalizable evidence.

| Implementation question | Related research question |
| --- | --- |
| How can CDP tracing events be collected? | Does trace-based instrumentation produce repeatable main-thread timing estimates under controlled conditions? |
| How should the JSON response be structured? | Which runtime measurements provide valid evidence for characterizing page performance? |

Implementation is necessary to build the artifact, but Chapter 2 should not become a technical manual. The research contribution must arise from a systematically investigated property of the profiler or its measurements.

## Profiler API boundary

The API remains a design constraint unless later evidence makes it part of the research problem.

```text
Input API
  - URL
  - device profile
  - network profile
  - scan configuration
        |
        v
Performance Profiling Engine
  - navigation and browser tracing
  - main-thread, network, and memory measurement
  - metric calculation, issue detection, and scoring
        |
        v
Output API
  - normalized measurements
  - raw or trace evidence where appropriate
  - issues and score
  - scan metadata
  - warnings and failure information
```

The stable result contract should let dashboards, storage, carbon analysis, and recommendation modules consume evidence without depending on the profiler's implementation details.

## Research priorities and workflow

The themes should be prioritized as follows:

| Priority | Themes |
| --- | --- |
| Essential | Metric definitions and validity; browser instrumentation; repeatability and reproducibility; reference-tool comparison; experimental control |
| Required but supporting | Performance scoring; test-corpus design |
| Potential threat | Instrumentation overhead |

Stage 3 research should follow this sequence:

```text
authoritative metric definitions
-> browser measurement mechanisms
-> variability and reproducibility
-> reference-tool comparison methods
-> controlled benchmarking methodology
-> scoring and corpus design
-> limitations and contradictory findings
-> evidence-supported candidate gaps
-> do not select the gap yet
```

Deep Research should identify several candidate opportunities and show the evidence for and against each one. The final gap must be judged from the original evidence rather than accepted from an automated report.

## Stage 2 outcome

Stage 2 is complete at the planning level. It establishes the literature landscape, research priorities, source hierarchy, expected evidence outputs, API boundary, and methodological questions that remain unresolved.

The investigation must eventually answer five questions:

1. What constitutes a valid browser-performance measurement?
2. What is the most defensible way to obtain such measurements programmatically?
3. How can repeated browser tests be made sufficiently controlled, repeatable, and reproducible?
4. How should a custom profiler be compared with recognized tools without making invalid claims about absolute accuracy?
5. What significant and unresolved limitation can be investigated feasibly through this profiler?

Only after the fifth question can be answered should the research gap, research question, and methodology be finalized.

The next stage is to construct a rigorous standalone Deep Research prompt. It should search foundational and recent literature, examine contradictory evidence, extract experimental details, distinguish authoritative definitions from empirical findings, and avoid treating implementation novelty as research novelty.

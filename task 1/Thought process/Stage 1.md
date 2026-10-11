# Stage 1 — Project and Individual Scope Realization

## Purpose of this stage

Stage 1 establishes the boundaries of the individual thesis within the wider GreenCode group project. It does not define a research gap, research question, objectives, or hypothesis. Those must be derived from evidence in the literature rather than designed retrospectively to justify an implementation that has already been proposed.

The central conclusion is:

> The group project concerns sustainable web software, but the individual thesis should focus on building and evaluating the browser-runtime performance measurement layer that supplies trustworthy evidence to the rest of the GreenCode system.

This distinction emerged by comparing the broad project proposal with the more precise individual task allocation.

## How the scope was narrowed

### 1. The group proposal defines a broad product

The proposed **Automated Web Application Carbon Emission Analyzer & Optimizer** is a Software as a Service (SaaS) platform, meaning software delivered online rather than installed and operated separately by each user. It aims to help developers measure and reduce the environmental impact of web applications.

The complete platform combines:

- runtime analysis of a deployed website supplied as a URL;
- static analysis, which examines source code without executing it, from a ZIP archive;
- conversion of measurements into estimated carbon emissions;
- historical reporting through a dashboard; and
- optimization or refactoring recommendations generated with a Large Language Model (LLM), an AI model trained to process and generate language and code.

Its overall pipeline can be summarized as:

```text
input → processing → asset/runtime analysis → carbon estimation → AI recommendations → dashboard
```

The group-level engineering problem is therefore how to provide developers with one tool that measures a web application's resource use, estimates its environmental effect, and recommends improvements. This is too broad to represent one member's thesis contribution.

### 2. The individual task allocation defines a measurement component

The individual task document assigns Member 1 the **Web Performance Profiling Engine**. A profiler is an instrument that records how a program uses resources and where it spends time. The assigned work covers the live-website path from URL validation to browser measurement, scoring, visualization, and integration.

The component must:

- validate a URL and control Chromium through Puppeteer or the Chrome DevTools Protocol (CDP);
- run desktop and mobile test profiles under controlled Central Processing Unit (CPU) and network conditions;
- collect loading metrics, browser lifecycle events, network activity, main-thread work, memory behaviour, and Document Object Model (DOM) information;
- identify performance issues and produce a transparent score;
- return structured results through an internal Application Programming Interface (API), a defined interface through which software components exchange data;
- provide performance views for timelines, network, CPU, memory, DOM, and issue details; and
- repeat measurements and compare them with Chrome DevTools or Lighthouse.

Puppeteer is a browser-automation library. CDP is the lower-level protocol used to communicate with Chromium and access debugging or performance data. The DOM is the browser's in-memory representation of the page's HTML structure.

This responsibility is substantially more complex than calculating a page's download size. It amounts to constructing a browser-performance measurement instrument.

### 3. The profiler supplies other modules rather than replacing them

The task document states that normalized profiler data must be sent to the carbon-analysis and recommendation modules. **Normalization** means converting measurements with different units or ranges into comparable forms. Because those modules consume the profiler's results, they are downstream dependencies rather than the primary subject of this thesis.

The resulting boundary is:

```text
                         INDIVIDUAL COMPONENT

URL
 │
 ▼
Validation
 │
 ▼
Controlled browser execution
 │
 ▼
Runtime instrumentation
 │
 ├── loading metrics and lifecycle timeline
 ├── network requests and transfer sizes
 ├── JavaScript and main-thread activity
 ├── memory behaviour
 └── DOM information
 │
 ▼
Normalization, issue detection, and scoring
 │
 ├──────────────► Performance dashboard
 │
 └──────────────► Structured internal API
                          │
                  ┌───────┴────────┐
                  ▼                ▼
             Carbon module   AI recommendation module
```

The individual scope therefore includes browser instrumentation, test profiles, repeated measurements, scoring, profiler APIs, performance visualizations, and comparative evaluation. It does not primarily include the carbon-emissions model, LLM recommendation method, static source-code analysis, authentication, or the complete history and portfolio system. These features matter only where they impose interface requirements on the profiler.

The available documents do not provide reliable task allocations for the other four members. They support a functional boundary between components, but not a person-by-person responsibility matrix. Missing allocations should not be invented.

## Engineering artifact and research contribution

The **engineering artifact** is the software that performs the following transformation:

```text
website → controlled browser run → instrumentation → measurements → normalized results → API and visualizations
```

Building this profiler is necessary, but building software alone does not establish an academic contribution. The research contribution must concern a property that can be investigated systematically.

The task allocation introduces several possible research properties:

- whether browser metrics can be collected consistently through a custom profiler;
- how repeatable the results are across multiple runs;
- how results correspond with Chrome DevTools or Lighthouse;
- why different instrumentation methods may disagree;
- how CPU, network, cache, browser, or website conditions affect measurements; and
- whether a multi-metric performance score can be justified transparently.

These remain research directions, not established research gaps. The literature must show what is already known and what remains unresolved.

## The provisional academic problem

Automated browser profiling measures a system that naturally varies between executions. For GreenCode to depend on the profiler, its measurements must be collected consistently, interpreted correctly, and shown to correspond meaningfully with an established reference tool.

This provisional problem has three layers.

### Measurement

The first layer asks whether the required information can be collected programmatically and what each value actually represents. Examples include when visible content appears, when the largest visible element is rendered, how long the browser's principal execution thread is blocked, how much data is transferred, how long network requests take, how much time JavaScript consumes, and how memory changes while a page loads.

This requires understanding the browser's execution pipeline:

```text
URL request → DNS and connection → HTTP response → HTML parsing → DOM construction
→ CSS processing → JavaScript execution → layout → paint → compositing → interactive page
```

Domain Name System (DNS) lookup translates a domain name into a network address. **Layout** calculates the position and size of page elements, **paint** draws their visual pixels, and **compositing** combines separately rendered layers into the final screen image.

### Reliability and repeatability

**Reliability** concerns whether repeated use of an instrument under the same conditions produces consistent results. **Repeatability** is the degree of consistency observed when the same page is tested repeatedly with the same procedure.

A page may produce different values across runs because of remote server response time, network variation, caching, browser scheduling, background processes, third-party resources, JavaScript behaviour, or garbage collection. Garbage collection is the automatic recovery of memory that is no longer in use.

Consequently, one run is unlikely to provide enough evidence. The methodology will eventually need justified rules for the number of runs, cache state, treatment of the first run, summary statistic, and handling of unusual values. Those rules should come from benchmarking and measurement literature rather than convenience.

### Validity and reference agreement

**Validity** concerns whether an instrument measures what it is intended to measure. A profiler can be highly repeatable but consistently different from the intended measurement; reliability therefore does not guarantee validity.

The assignment requires comparison with Chrome DevTools or Lighthouse, but neither should automatically be treated as unquestionable ground truth. They can serve as reference implementations. Until a true value can be justified, safer evaluation terms include **agreement**, **deviation**, **consistency**, or **correspondence with the reference tool**, rather than absolute accuracy.

Correlation alone is also insufficient. Two tools can produce values that rise and fall together while one remains systematically higher than the other. The literature review must therefore identify methods that assess both agreement and systematic bias, meaning a consistent tendency for one method to overestimate or underestimate another.

## Mathematical and experimental implications

Repeated measurements require descriptive statistics such as the mean, median, standard deviation, interquartile range, and confidence interval. These respectively describe the average, middle observation, typical spread, spread of the central half of observations, and uncertainty around an estimated value.

One candidate measure of relative variability is the **coefficient of variation**:

$$
CV = \frac{s}{\bar{x}}
$$

where $s$ is the sample standard deviation and $\bar{x}$ is the sample mean. It expresses variation relative to the size of the measurement, allowing variability in short and long timings to be compared more meaningfully. It is a possible method to investigate, not a method selected at this stage.

Comparison with a reference tool may begin with a difference:

$$
d_i = x_i-r_i
$$

where $x_i$ is the custom profiler's value, $r_i$ is the reference value, and $d_i$ is the difference for observation $i$. However, percentage difference or correlation alone may not adequately represent agreement, so an appropriate comparison method must be chosen from the literature.

The required performance score creates another problem. The profiler collects milliseconds, megabytes, request counts, DOM-node counts, and percentages. These values cannot be added directly because they have different meanings and units. They must first be normalized if they are to form a composite score.

A general weighted score could be represented as:

$$
S=\sum_{j=1}^{m}w_jz_j
$$

where $z_j$ is a normalized metric, $w_j$ is its assigned importance, and $m$ is the number of metrics. The equation is straightforward; justifying the normalization, thresholds, and weights is the difficult part. Arbitrary weights produce an arbitrary score. The literature must show whether established models exist, how their choices are justified, and whether preserving separate metrics would be more defensible than combining them.

The task also requires repeated tests on static, image-heavy, JavaScript-heavy, and poorly optimized sites. This suggests a repeated-measures design, in which the same websites are measured repeatedly under different CPU or network profiles and by both the custom and reference tools. Such a design supports within-site comparisons, but the website corpus, number of repetitions, statistical analysis, and acceptance criteria remain undecided.

## Technical foundations to investigate

Several computer-science areas must be understood before the methodology can be defended:

- **Browser architecture:** how networking, HTML and CSS processing, JavaScript, layout, painting, and compositing produce a page.
- **Main thread:** the browser's principal execution thread, on which JavaScript, style calculation, layout, and parts of rendering compete for CPU time. Long tasks on this thread can delay user interaction.
- **Measurement interfaces:** the differences among browser JavaScript Performance APIs, Puppeteer, CDP, Chromium tracing, Chrome DevTools, and Lighthouse. Similar metric names do not prove identical measurement procedures.
- **Networking:** DNS lookup, Transmission Control Protocol (TCP) connection, Transport Layer Security (TLS) setup, HTTP request and response timing, caching, compression, blocking, transfer size, and third-party requests.
- **Memory management:** allocation and garbage collection. An increase between two memory readings does not by itself prove a memory leak, which is memory retained unintentionally over time.
- **Benchmark reproducibility:** keeping relevant conditions consistent, including Chrome version, viewport, cache policy, throttling settings, hardware, test procedure, and the rule used to decide that a page has finished loading.

One terminology issue requires particular care. The task document groups First Contentful Paint (FCP), Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), Total Blocking Time (TBT), Speed Index, Time to Interactive, and server response time under “Core Web Vitals.” This classification should not be copied into the thesis without verification. **Core Web Vitals** is a specific industry-defined subset of user-experience metrics, and its current membership and definitions must be checked against authoritative sources.

Chrome DevTools and Lighthouse must also not be treated as interchangeable. DevTools provides browser inspection and performance-tracing capabilities, whereas Lighthouse performs an automated audit using its own workflow and scoring methodology. The literature review must determine which tool is an appropriate reference for each measurement; different metrics may require different references.

## Literature needed before defining a gap

The literature investigation should cover seven connected themes:

1. **Metric validity and semantics:** what each loading, responsiveness, network, memory, and main-thread metric means and how it is determined.
2. **Automated browser measurement:** how headless browsers, Puppeteer, CDP, Performance APIs, tracing, DevTools, and Lighthouse collect data.
3. **Repeatability and variation:** why repeated web tests differ and how researchers control or summarize that variation.
4. **Controlled benchmarking:** how CPU throttling, network profiles, cache state, browser version, mobile or desktop configuration, and page-load completion rules affect comparability.
5. **Profiler comparison:** how to evaluate bias, deviation, agreement, and repeatability between measurement instruments.
6. **Multi-metric scoring:** how metrics are normalized, weighted, and converted into thresholds or composite scores, and what information such scores may hide.
7. **Benchmark corpus design:** how to select or construct a reproducible set of static, image-heavy, JavaScript-heavy, and poorly optimized websites.

A defensible evidence chain is:

```text
authoritative metric definitions
→ existing tools and measurement methods
→ published evaluation practices
→ known variation, limitations, and disagreements
→ problems already solved
→ unresolved problems
→ fit with the individual scope
→ feasibility of testing
→ research gap
```

Potential gap categories include poor repeatability, disagreement among instrumentation approaches, insufficient validation of custom profilers, inadequate control of experimental conditions, opaque scoring, incomplete measurement coverage, or weak reproducibility reporting. None can be claimed yet. A genuine gap must be supported by multiple authoritative or peer-reviewed sources and must remain both inside the profiler's boundary and feasible to investigate.

The review should not treat product novelty as research novelty. Claims such as “no one has built this exact dashboard” or “this system combines several features” do not establish an academic gap. If the literature shows that the candidate problems have already been addressed adequately, the research direction should change rather than manufacture novelty.

## Requirements, assumptions, and unresolved claims

The project documents contain both confirmed requirements and claims that still need evidence.

| Statement | Current interpretation |
| --- | --- |
| Runtime measurements must feed the carbon and recommendation modules | Confirmed project requirement |
| A custom profiler must be built and evaluated | Confirmed individual requirement |
| Measurements must be repeated | Confirmed individual requirement |
| DevTools or Lighthouse must be used for comparison | Confirmed individual requirement, but the comparison method is unresolved |
| Existing carbon tools only analyze deployed sites | Unverified proposal claim |
| Existing tools generally lack actionable recommendations | Unverified proposal claim |
| Page weight directly determines environmental impact | Simplification requiring research |
| Carbon output can be reported as exact grams of CO₂ equivalent | Claim requiring substantial scrutiny |
| 0.35 g CO₂e per page view is a universal target | Claim requiring authoritative evidence |
| All profiler metrics should form one performance score | Engineering requirement with unresolved methodology |
| Difference from a reference tool represents accuracy | Methodological assumption requiring refinement |

The broad proposal also contains internal inconsistencies: one section describes four-week sprints while another describes three-week sprints; the database is identified as Supabase in one place and Firebase Cloud Firestore in another; and zero-cost infrastructure is treated as if it were a permanent technical property. More importantly, the proposal emphasizes page and asset weight, while the later individual allocation defines a much broader runtime profiler. Where the two differ, the individual task allocation is the more precise description of the current technical scope.

## Dependencies and integration boundaries

The profiler depends upstream on the overall application architecture for an invocation model such as:

```text
URL + test profile → profiler
```

Authentication, request formats, and deployment choices must be agreed by the group, but they are not necessarily individual research topics.

Downstream, the carbon and recommendation modules require a stable API contract containing structured evidence such as scan metadata, performance metrics, network activity, main-thread work, memory measurements, timeline events, detected issues, and any resulting score. The recommendation module will need underlying evidence rather than only a summary score; for example, a claim that JavaScript execution is expensive should be supported by the relevant task durations and affected resources.

Designing this output schema is part of profiler integration. Developing the carbon model or LLM itself remains outside the primary thesis scope.

## Outcome and next stages

Stage 1 has established a sufficiently clear working boundary:

> The thesis concerns the design and evaluation of a controlled browser-performance profiler whose measurements must be repeatable, interpretable, and meaningfully comparable with established tools. Its role in GreenCode is to provide trustworthy runtime evidence to performance, carbon-analysis, and recommendation interfaces.

The remaining process should be evidence-led:

1. Conduct broad foundational research across browser measurement, repeatability, experimental control, tool agreement, and scoring.
2. Build an evidence matrix recording each study's problem, method, browser or tool, metrics, environment, repetitions, website corpus, statistical analysis, findings, limitations, and relevance.
3. Synthesize the studies to identify an unresolved and feasible problem within the profiler boundary.
4. Derive the research question, and only add a hypothesis if the evidence supports a specific prediction.
5. Derive the aim and measurable objectives from that question.
6. Choose the browser configuration, website corpus, repetitions, cache policy, test profiles, reference tools, statistical methods, and validity controls in the methodology.

This sequence preserves traceability:

```text
literature → unresolved problem → research gap → research question
→ hypothesis if justified → aim → objectives → methodology
```

It also provides the likely foundation for the first three thesis chapters. Chapter 1 can introduce the evidence-supported problem, gap, question, scope, and significance. Chapter 2 can synthesize browser execution, metric semantics, automated profiling, controlled benchmarking, repeatability, profiler comparison, and scoring. Chapter 3 can then justify the profiler architecture, instrumentation, website corpus, repeated-run protocol, reference procedure, statistical analysis, reproducibility controls, and threats to validity.

The immediate next step is a broad Deep Research investigation. It should test competing possibilities rather than presuppose a gap, particularly around profiler validity, repeatability, controlled experimentation, reference-tool agreement, and composite scoring.

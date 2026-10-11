# Stage 3
## 1. Refine the monitoring model: RUM-informed synthetic profiling

I agree with the direction, but I would avoid calling it **Real User Monitoring (RUM)** itself.

Real User Monitoring means collecting telemetry from actual users interacting with a production application. What you are proposing is closer to:

> **RUM-informed synthetic monitoring using configurable user-condition agents.**

That is actually a useful research design because we can deliberately balance **internal validity** and **external validity**.

We can think of the profiler as having two related modes:

```text
                    Synthetic Profiler Agents
                              │
             ┌────────────────┴────────────────┐
             │                                 │
             ▼                                 ▼
   Controlled-condition testing       Live-path testing
   ────────────────────────────       ─────────────────
   Fixed CPU profile                  Real remote server
   Fixed network profile              Real Internet path
   Fixed viewport/device              Real CDN behaviour
   Fixed cache state                  Real server load
   Repeatable environment             Real third-party assets

        Higher internal validity       Higher external validity
```

The same agent concept can support both.

An agent might represent, for example:

```text
Profile A
Desktop
Fast CPU
Broadband network
1920 × 1080 viewport

Profile B
Mid-range mobile
Reduced CPU capacity
Higher-latency network
390 × 844 viewport

Profile C
Low-resource mobile
Strong CPU constraint
Constrained network
360 × 800 viewport
```

The profiler is still synthetic because we intentionally construct those conditions.

However, because the target is an actual live URL served by the real site's infrastructure, the test retains important real-world components:

- genuine server response;
    
- Content Delivery Network (CDN) behaviour;
    
- third-party services;
    
- actual deployed JavaScript;
    
- actual resource dependencies;
    
- real network path characteristics where they are not deliberately overridden.
    

This gives us a potentially useful distinction later:

> **controlled user-condition realism** versus **uncontrolled production-environment realism**.

We should make the Deep Research work determine how defensible that distinction is and how synthetic conditions should be selected.

---

# 2. Your measurement-distribution idea is promising, but there is one important correction

I strongly agree with the broader idea:

> **Do not reduce repeated profiler measurements immediately to one arithmetic mean. Preserve and analyse the distribution.**

But a **95% confidence interval**, a **95th percentile**, the **coefficient of variation**, and the **mean** answer different statistical questions.

They are not alternatives to one another.

Consider 100 repeated Largest Contentful Paint measurements.

That gives us an **empirical distribution**:

```text
                   repeated measurements
                           │
                           ▼
                    DISTRIBUTION
                           │
           ┌───────────────┼─────────────────┐
           ▼               ▼                 ▼
       Location          Spread             Shape
     ───────────      ────────────       ────────────
       mean             variance           skewness
       median           IQR                tails
       p50              CV                 multimodality
       p95
```

Then confidence intervals address another question:

> **How uncertain are we about an estimated property of that distribution?**

For example, we could construct:

- a 95% confidence interval around the mean;
    
- a 95% confidence interval around the median;
    
- a 95% confidence interval around the 95th percentile.
    

So:

$$\text{95th percentile} \neq \text{95\% confidence interval}$$

### What each quantity tells us

| Quantity                      | What it tells us                                              |
| ----------------------------- | ------------------------------------------------------------- |
| Mean                          | Average/expected measurement                                  |
| Median / p50                  | Typical central measurement, more resistant to extreme values |
| p95                           | A high-tail measurement: 95% of runs fall at or below it      |
| Variance / standard deviation | Absolute spread                                               |
| Coefficient of Variation (CV) | Spread relative to the mean                                   |
| Interquartile Range (IQR)     | Spread of the middle 50%                                      |
| Skewness                      | Degree of distributional asymmetry                            |
| Confidence interval           | Uncertainty in an estimated parameter                         |

One other correction: **CV does not measure skewness**.

If

$$CV=s\bar{x},CV=\frac{s}{\bar{x}}$$, then $s$ is the sample standard deviation and $\bar{x}$ is the sample mean.

It tells us how large the variability is relative to the measurement magnitude. It does not tell us whether that variation lies primarily above or below the centre.

---

# 3. I think the eventual measurement model could be considerably stronger than a simple mean

Without selecting it prematurely, a promising structure for us to investigate is:

```text
Repeated runs
      │
      ▼
Empirical distribution
      │
      ├── p50 / median       → typical behaviour
      ├── p95                → poor-tail behaviour
      ├── IQR / variance     → absolute variability
      ├── CV                 → relative variability
      ├── skewness           → distribution shape
      └── confidence interval→ uncertainty of estimators
```

For performance measurements, the tail can be especially meaningful.

Imagine:

```text
Most runs:        1.8–2.2 s
Occasional runs:  5–7 s
```

The mean can partially hide what is happening.

A percentile-based description makes the tail visible.

However, we **cannot yet say p95 is the correct statistic**. That needs research.

There is a practical mathematical issue too: estimating a high percentile reliably usually requires substantially more observations than estimating a mean or median.

With only 5 runs, for example, there is essentially no meaningful empirical p95 estimate.

Even with 20 runs, the p95 is heavily influenced by the largest observation.

So one particularly interesting research direction is:

> **Can profiler execution continue adaptively until the uncertainty of the required measurement statistic falls below a specified threshold?**

Conceptually:

```text
Run profiler
     ↓
Update sample distribution
     ↓
Estimate statistic + uncertainty
     ↓
Is uncertainty sufficiently small?
     │
   No│         Yes
     ▼          ▼
Run again    Stop and report
```

That would be much more principled than saying:

> “Every website is run exactly five times.”

It could potentially become a mathematical or algorithmic contribution—but only if the literature supports such an approach and it is feasible.

---

# 4. "More accurate than the mean" should be reframed

I would avoid saying that a confidence-interval or percentile approach is inherently **more accurate** than a mean.

Accuracy depends on what quantity we are trying to estimate.

If the scientific question is:

> What is the expected loading time?

then the mean is directly relevant.

If the question is:

> What does a typical execution look like?

the median may be more meaningful.

If the question is:

> How bad are unusually slow executions?

p95 may be more meaningful.

So before selecting the statistic, we need to identify the **estimand**.

An estimand is simply:

> **the quantity that our experiment is actually trying to estimate.**

That concept should become part of the statistical Deep Research prompt.

---

# 5. Controlled websites + real-world websites is an excellent idea

I would make one terminology adjustment.

The entire controlled-site corpus is not necessarily a **control group**.

Instead, I suggest two evaluation layers.

### Layer A — Controlled benchmark fixtures

We create websites whose characteristics we deliberately know.

For example:

```text
Base website
     │
     ├── Baseline
     ├── + large images
     ├── + heavy JavaScript computation
     ├── + deliberate layout shifts
     ├── + large DOM
     └── + many network resources
```

Here the **baseline version** can genuinely act as a control condition.

The modified versions become experimental conditions.

That allows questions such as:

> If we deliberately introduce a known long JavaScript task, does the profiler detect the expected change?

That gives us a form of **construct validation**.

---

### Layer B — Real-world live corpus

We then test actual deployed websites.

Those sites provide:

- real infrastructure;
    
- real third-party resources;
    
- unpredictable network conditions;
    
- modern frameworks;
    
- dynamic content;
    
- realistic workloads.
    

That gives us stronger external validity.

Together:

controlled fixtures+real-world URLs\boxed{ \text{controlled fixtures} + \text{real-world URLs} }

is substantially stronger than relying exclusively on either.

The literature still needs to tell us how the corpus should be selected and how many websites/runs are defensible.

---

# 6. Profiler overhead: change "eliminate" to "characterize, minimize and correct if justified"

This is another potentially interesting research direction.

But I would not begin with the assumption that we can mathematically **eliminate** instrumentation overhead.

Suppose the actual execution cost is conceptually:

Tobserved=Twebsite+Tinstrumentation+Tinteraction+ϵT_{\text{observed}} = T_{\text{website}} + T_{\text{instrumentation}} + T_{\text{interaction}} + \epsilon

where:

- TobservedT_{\text{observed}} is what we measure;
    
- TwebsiteT_{\text{website}} represents the underlying workload;
    
- TinstrumentationT_{\text{instrumentation}} represents profiler overhead;
    
- TinteractionT_{\text{interaction}} represents any way the profiler changes browser behaviour;
    
- ϵ\epsilon represents other noise.
    

Simply estimating an average profiler cost cc and calculating

Tcorrected=Tobserved−cT_{\text{corrected}}=T_{\text{observed}}-c

would only be valid if the overhead were approximately constant.

It probably isn't safe to assume that.

Heavy tracing might impose more overhead on:

- JavaScript-heavy sites;
    
- pages producing many trace events;
    
- pages with hundreds of network requests;
    

than on small static pages.

So the research should investigate three levels:

1. **Minimize** overhead through instrumentation architecture.
    
2. **Measure** whether remaining overhead is significant and workload-dependent.
    
3. **Correct or calibrate** measurements mathematically only if evidence supports a valid correction model.
    

Potential approaches worth researching include:

- event sampling;
    
- selective instrumentation;
    
- deferred/offline trace processing;
    
- paired instrumented/uninstrumented experiments;
    
- randomized measurement ordering;
    
- calibration models;
    
- regression-based correction;
    
- adaptive instrumentation.
    

Again, those are research candidates rather than methodology decisions.

---

# 7. Stage 3 should use multiple Deep Research prompts

I agree completely with this change.

One enormous Deep Research prompt creates two problems:

**breadth dilutes depth**, and the researcher may prematurely connect unrelated evidence into one convenient narrative.

Instead, we will run **independent thematic investigations** and synthesize them ourselves afterward.

That actually fits the evidence-led approach better:

```text
Theme 1 evidence ─┐
Theme 2 evidence ─┤
Theme 3 evidence ─┤
Theme 4 evidence ─┼──► Cross-theme synthesis
Theme 5 evidence ─┤             │
Theme 6 evidence ─┘             ▼
                           Candidate gaps
                                 │
                                 ▼
                          Gap evaluation
```

The reports themselves should **not be asked to manufacture one common gap**.

---

# Stage 3 — Tier 1 Deep Research Programme

I recommend expanding Tier 1 from five to **six investigations** because your RUM-informed synthetic-agent idea and the controlled/live experimental distinction deserve proper treatment.

Run them as separate Deep Research conversations.

---

## Tier 1.1 — Browser performance metrics, semantics and measurement validity

```text
Act as an expert academic researcher in web performance engineering, browser
instrumentation, software measurement, and computer systems.

I am researching the design and empirical evaluation of a custom browser-based
web performance profiler. The profiler will accept a live URL, execute the site
using controlled browser agents, collect runtime measurements, and expose
normalized measurements through an API.

The profiler may measure loading behaviour, rendering, main-thread activity,
network activity, memory behaviour, DOM characteristics, and related browser
performance metrics. Candidate metrics currently include First Contentful Paint
(FCP), Largest Contentful Paint (LCP), Cumulative Layout Shift (CLS), Total
Blocking Time (TBT), Speed Index, Time to Interactive (TTI), server response
timing, network transfer measurements, JavaScript execution, rendering/layout/
painting time, long tasks, memory usage, and DOM characteristics.

This research is evidence-led. Do NOT assume that every listed metric is current,
appropriate, independently measurable, or correctly classified. In particular,
verify the current definition and status of Core Web Vitals and distinguish Core
Web Vitals from other laboratory or diagnostic metrics.

RESEARCH OBJECTIVE

Establish a rigorous conceptual and technical foundation for what a custom
browser performance profiler can legitimately claim to measure.

INVESTIGATE:

1. The current authoritative definition of each important browser/web performance
   metric, including:
   - what phenomenon it intends to represent;
   - precise measurement semantics;
   - units;
   - start and termination conditions;
   - edge cases;
   - whether it is directly observed or algorithmically derived.

2. Distinguish metrics that represent:
   - loading performance;
   - responsiveness/interactivity;
   - visual stability;
   - visual loading progression;
   - server/network behaviour;
   - main-thread execution;
   - memory;
   - DOM complexity.

3. Distinguish:
   - laboratory/synthetic metrics;
   - field/real-user metrics;
   - metrics usable in both environments.

4. Determine which metrics remain current and recommended as of 2026 and which
   have been deprecated, replaced, modified, or primarily retained for diagnostic
   purposes.

5. Investigate construct validity:
   - What aspect of "web performance" does each metric actually measure?
   - What important behaviours does it fail to capture?
   - Can two sites with similar metric values nevertheless provide very different
     user experiences?

6. Investigate known weaknesses, sensitivity, instability, and limitations of
   individual metrics.

7. Determine whether metrics with identical names reported by Chrome DevTools,
   Lighthouse, Web Performance APIs, Chrome UX Report or other systems necessarily
   have identical semantics.

8. Identify metrics that should NOT be directly compared across tools unless
   particular collection conditions or definitions are matched.

SOURCE PRIORITY

Prioritize:
1. W3C/Web Performance Working Group specifications and standards;
2. authoritative Chromium/Chrome and Lighthouse technical documentation;
3. peer-reviewed journal and strong conference papers;
4. systematic reviews/surveys;
5. authoritative academic books.

Use technical blogs only where primary or academic evidence is unavailable.

Include seminal work where necessary and recent literature, particularly work
from approximately 2020–2026.

Do not invent papers, citations, DOIs or claims.

OUTPUT

Produce:

A. Executive synthesis.

B. Metric evidence matrix containing:
   metric;
   intended construct;
   formal/technical definition;
   measurement mechanism;
   direct versus derived;
   lab versus field applicability;
   current status;
   major limitations;
   authoritative sources.

C. A corrected taxonomy of metrics appropriate for a custom performance profiler.

D. Areas where terminology in common developer tools is misleading or easily
   confused.

E. Contradictory evidence or unresolved debates.

F. Implications for designing a custom browser profiler, clearly distinguishing
   literature-supported conclusions from researcher inference.

G. A list of 10–20 especially important original papers/specifications that should
   be downloaded and examined manually, including verified bibliographic details
   and DOI where one genuinely exists.

H. Candidate unanswered questions that deserve further investigation.

Do NOT declare a final research gap and do NOT design my final methodology.
The purpose of this report is to establish the measurement foundations from
which later research decisions will be made.
```

---

# Tier 1.2 — Browser instrumentation architecture and profiler observer effect

```text
Act as an expert academic researcher in browser internals, performance profiling,
systems instrumentation, benchmarking and software measurement.

I am researching a custom web performance profiler that programmatically loads
live websites using Chromium-based browser agents and collects performance,
network, main-thread, rendering, memory and DOM measurements.

Possible technologies include Puppeteer, Chrome DevTools Protocol (CDP),
browser Web Performance APIs/PerformanceObserver, Chromium tracing and
Lighthouse-related collection mechanisms.

Do not assume one instrumentation approach is superior.

RESEARCH OBJECTIVE

Determine how modern Chromium performance measurements can be collected
programmatically, what each instrumentation layer actually observes, and how
instrumentation itself may alter the workload being measured.

INVESTIGATE:

1. Architecture and measurement capabilities of:
   - Web Performance APIs;
   - PerformanceObserver;
   - Chrome DevTools Protocol;
   - relevant CDP domains;
   - Chromium tracing;
   - Puppeteer;
   - Lighthouse collection/artifact mechanisms.

2. For important performance measurements, determine which mechanisms provide:
   - raw browser events;
   - aggregate counters;
   - derived metrics;
   - trace-level evidence.

3. Investigate timestamp/timebase synchronization when data is collected from
   multiple instrumentation sources.

4. Investigate headed versus headless Chromium performance behaviour and whether
   empirical research demonstrates meaningful measurement differences.

5. Investigate instrumentation overhead and the profiler/observer effect:
   - tracing overhead;
   - event-listener overhead;
   - JavaScript injection overhead;
   - serialization overhead;
   - large trace processing;
   - workload-dependent overhead.

6. Search broader computer-systems and profiler literature for established methods
   to characterize instrumentation overhead.

7. Investigate methods to minimize overhead, including where supported:
   - passive browser instrumentation;
   - selective event collection;
   - sampling;
   - deferred/offline processing;
   - tiered instrumentation;
   - adaptive instrumentation.

8. Investigate whether mathematical or computational correction/calibration of
   profiler overhead has been successfully used.

   Search for methods such as:
   - paired measurements;
   - calibration functions;
   - regression correction;
   - randomized instrumented/uninstrumented trials;
   - overhead modelling;
   - trace sampling.

   Do NOT assume subtraction of a constant overhead is valid.

9. Examine reproducibility implications of:
   - Chromium/browser version;
   - operating system;
   - host hardware;
   - browser launch flags;
   - extension state;
   - background processes.

10. Identify which measurements can realistically be produced using low-overhead
    instrumentation and which require expensive tracing.

SOURCE PRIORITY

Prioritize peer-reviewed systems/performance papers, browser research, Chromium
technical sources, W3C specifications and authoritative Lighthouse/Puppeteer
documentation.

Include relevant profiling literature outside web browsers where the measurement
methodology transfers legitimately.

OUTPUT

A. Architecture-level explanation of available instrumentation mechanisms.

B. Instrumentation matrix:
   required metric/data;
   possible source;
   resolution;
   overhead;
   limitations;
   reproducibility concerns.

C. Evidence about headless versus headed measurement validity.

D. Evidence map of known profiler/instrumentation overhead.

E. Methods previously used to minimize, quantify or correct observer effects.

F. Candidate architectures for a low-overhead profiler, labelled explicitly as
   evidence-supported options rather than final recommendations.

G. Unresolved methodological questions.

H. 10–20 important original papers/specifications/technical sources to download,
   with verified bibliographic information.

Do NOT invent a research gap and do NOT prematurely select the final profiler
architecture.
```

---

# Tier 1.3 — RUM-informed synthetic agents and external validity

```text
Act as an expert researcher in web performance engineering, Real User Monitoring
(RUM), synthetic monitoring, distributed systems measurement and experimental
validity.

I am designing a browser performance profiler that remains synthetic but attempts
to represent real user conditions through configurable browser agents.

Each agent may define characteristics such as:
- device/viewport;
- CPU capability or throttling;
- network conditions;
- cache state;
- browser configuration;
- potentially geographic execution location.

The target URL is a real deployed website. Therefore the remote server, CDN,
third-party services and deployed resources are genuine production components.
Where network conditions are not fully emulated, the test also traverses a real
network path.

This is NOT intended to be misrepresented as actual Real User Monitoring.

RESEARCH OBJECTIVE

Determine how RUM evidence can inform realistic synthetic browser profiles and
how such profiling affects the internal and external validity of web-performance
experiments.

INVESTIGATE:

1. Formal and practical distinctions between:
   - Real User Monitoring;
   - synthetic monitoring;
   - laboratory performance testing;
   - distributed synthetic monitoring;
   - browser/device emulation.

2. Strengths and limitations of RUM and synthetic testing.

3. Published evidence comparing laboratory/synthetic metrics with field/RUM
   measurements.

4. To what extent synthetic agents can validly approximate:
   - low-end/mid-range/high-end devices;
   - mobile versus desktop users;
   - network latency/bandwidth conditions;
   - geographic/network-path variation.

5. CPU throttling validity:
   - what browser CPU throttling actually does;
   - how well it represents real devices;
   - hardware dependence;
   - limitations.

6. Network throttling validity:
   - request-level/devtools throttling;
   - packet/network emulation;
   - observed live-path networks;
   - differences between simulated and real networks.

7. Determine whether useful "RUM-informed synthetic profiles" can be derived from
   empirical field distributions rather than arbitrary labels such as "slow 3G".

8. Investigate distributed measurement agents and geographic testing.

9. Examine cache state, service workers, repeat visits and cold/warm browser
   conditions as representations of different user experiences.

10. Analyse external validity:
    What can legitimately be inferred from a controlled synthetic agent testing a
    real production URL, and what cannot?

11. Analyse internal validity:
    Which elements must remain controlled so differences can actually be
    attributed to the website/profile being investigated?

12. Find methodologies that intentionally combine controlled synthetic tests and
    real-world production targets.

OUTPUT

A. Precise terminology and conceptual model.

B. Comparison of RUM versus synthetic approaches.

C. Evidence on the validity and limitations of device, CPU and network emulation.

D. Candidate RUM-informed agent dimensions supported by evidence.

E. A framework distinguishing:
   controlled-condition realism;
   real-network/server realism;
   field-user realism.

F. Threats to internal and external validity.

G. Evidence-supported options for a future profiler-agent strategy, without
   prematurely selecting one.

H. Important papers/data sources that could help define realistic user profiles.

I. 10–20 priority original sources to download.

Do NOT claim that configurable synthetic agents constitute RUM and do NOT
manufacture a research gap.
```

---

# Tier 1.4 — Statistical modelling of repeated performance measurements

This one is particularly important given your distribution idea.

```text
Act as an expert quantitative research methodologist specializing in computer
systems performance evaluation, statistics, benchmarking and repeated
measurements.

I am researching a browser-performance profiler that repeatedly executes the
same live URL under a defined browser-agent profile.

Individual runs may vary because of browser scheduling, JavaScript execution,
network/server behaviour, CDN behaviour, third-party resources, garbage
collection and other stochastic effects.

I do NOT want to arbitrarily run each test a fixed small number of times and
report only an arithmetic mean.

I am considering distribution-based reporting involving statistics such as
median, percentiles (potentially p95), variance, interquartile range,
coefficient of variation, skewness and confidence intervals.

No statistic has yet been selected.

RESEARCH OBJECTIVE

Determine a statistically defensible framework for repeated web/browser
performance measurement and determine what quantity or quantities the profiler
should estimate.

INVESTIGATE:

1. Empirical distributional characteristics of browser/web performance
   measurements:
   - normality/non-normality;
   - positive skew;
   - heavy tails;
   - multimodality;
   - heteroscedasticity;
   - temporal dependence.

2. Explain and compare possible estimands:
   - expected value/mean;
   - median;
   - p75;
   - p90;
   - p95;
   - other quantiles.

3. Determine what different estimands mean operationally for website performance.

4. Examine measures of variability:
   - variance;
   - standard deviation;
   - coefficient of variation;
   - interquartile range;
   - robust alternatives.

5. Examine measures of distribution shape, including skewness and appropriate
   robust alternatives.

6. Clearly distinguish percentile estimates from confidence intervals.

7. Investigate methods for confidence intervals around:
   - means;
   - medians;
   - percentiles/quantiles;
   - relative variability measures.

8. Investigate bootstrap and non-parametric methods where distributional
   assumptions are inappropriate.

9. Determine how many repeated measurements are required for stable estimation,
   especially of high percentiles such as p95.

10. Investigate adaptive/sequential measurement procedures in which testing
    continues until a defined precision criterion is met, such as:
    - confidence interval width;
    - relative confidence interval width;
    - stabilization of a percentile;
    - convergence of a variability estimate.

11. Search computer systems benchmarking literature for statistically rigorous
    stopping rules rather than arbitrary fixed repetition counts.

12. Investigate warm-up runs, cold/warm cache runs and whether initial observations
    should ever be discarded.

13. Investigate outlier handling:
    When is an observation genuine performance behaviour versus measurement error?

14. Investigate dependence between sequential runs and implications for
    confidence intervals.

15. Consider hierarchical/repeated-measures modelling where measurements are
    nested within:
    runs;
    browser profiles;
    websites.

16. Determine whether p95 has sufficient statistical and practical justification
    for this research or whether another statistic/set of statistics would be
    stronger.

SOURCE PRIORITY

Prioritize peer-reviewed computer systems benchmarking/performance methodology,
statistical methodology and empirical web-performance studies.

Do not rely primarily on generic statistics tutorials.

OUTPUT

A. First-principles explanation of the measurement problem.

B. Evidence on likely distributional behaviour.

C. Comparison table of candidate location, tail, spread and uncertainty metrics.

D. Evidence-based discussion of suitable estimands.

E. Methods for determining required repetitions.

F. Detailed investigation of sequential/adaptive stopping rules.

G. Appropriate confidence-interval approaches for candidate estimands.

H. Risks of unstable p95 estimation at small sample sizes.

I. Candidate statistical frameworks, with assumptions and weaknesses explicitly
   stated.

J. Important original methodological papers to download.

Do NOT assume that p95, CV, a 95% confidence interval, the mean or any other
statistic is correct in advance. Do NOT formulate the final research hypothesis.
```

---

# Tier 1.5 — Validation and agreement with Chrome DevTools/Lighthouse

```text
Act as an expert academic researcher in software measurement, performance
benchmarking, measurement-system validation and browser performance tools.

I am designing a custom browser profiler whose results must eventually be
compared with recognized browser tools such as Chrome DevTools and/or Lighthouse.

I do not want to make the scientifically weak assumption that Chrome DevTools or
Lighthouse automatically represents absolute "ground truth".

RESEARCH OBJECTIVE

Establish a defensible methodology for validating and comparing a custom browser
performance profiler against established reference implementations.

INVESTIGATE:

1. What Chrome DevTools Performance and Lighthouse actually measure and how their
   purposes and data pipelines differ.

2. Which metrics can legitimately be compared between:
   - a custom CDP/tracing profiler;
   - Chrome DevTools;
   - Lighthouse.

3. Cases where identically named metrics have different collection or computation
   procedures.

4. Difference between:
   - accuracy;
   - precision;
   - repeatability;
   - reproducibility;
   - agreement;
   - correlation;
   - bias.

5. Explain why high correlation does not demonstrate measurement agreement.

6. Survey methods used to compare measurement systems, including where relevant:
   - absolute error;
   - relative error;
   - Mean Absolute Error;
   - percentage deviation;
   - systematic bias;
   - limits-of-agreement approaches;
   - regression-based approaches;
   - reliability/agreement coefficients.

Do not preselect a method simply because it is commonly used.

7. Determine which methods are appropriate when neither measurement system can be
   treated as perfect ground truth.

8. Investigate paired experimental designs in which both systems measure the same
   website under matched conditions.

9. Examine how repeated measurements should be incorporated into tool comparison.

10. Investigate controlled benchmark perturbations as an additional validation
    mechanism.

For example, if a controlled website deliberately introduces:
- a known large network payload;
- a known long main-thread task;
- a deliberate layout shift;
- additional DOM nodes;

can detection of the induced change strengthen validation independently of
agreement with Lighthouse?

11. Investigate sensitivity, specificity or effect-detection concepts where
    applicable to profiler issue detection.

12. Determine how browser version, Lighthouse configuration, throttling strategy
    and test environment influence fair comparison.

OUTPUT

A. Conceptual framework for profiler validation.

B. Chrome DevTools versus Lighthouse comparison relevant to this project.

C. Matrix of metrics that are directly comparable, conditionally comparable or
   not directly comparable.

D. Appropriate candidate agreement/error methods with assumptions.

E. Methods for detecting systematic bias.

F. Role of controlled injected performance defects/perturbations.

G. Proposed evidence structure for validation, without fixing the final
   methodology.

H. Threats to validity.

I. Priority papers and authoritative technical sources to download.

Do NOT describe correlation alone as validation and do NOT treat a reference tool
as unquestionable ground truth without evidence.
```

---

# Tier 1.6 — Experimental design: controlled fixtures + real-world URLs

```text
Act as an expert researcher in computer systems experimentation, software
benchmarking, web-performance evaluation and quantitative research design.

I am designing an empirical evaluation for a custom browser performance profiler.

I want to investigate a dual-corpus approach:

1. CONTROLLED BENCHMARK FIXTURES
   Websites/applications whose characteristics can deliberately be manipulated.
   A baseline implementation could be compared against variants containing known
   performance problems such as:
   - large images;
   - heavy JavaScript;
   - long main-thread tasks;
   - layout shifts;
   - large DOM structures;
   - many network requests;
   - deliberately inefficient resources.

2. REAL-WORLD LIVE URL CORPUS
   Deployed websites served by real production infrastructure over actual network
   paths, providing greater ecological/external validity.

Tests may also be executed using configurable synthetic user-condition agents.

RESEARCH OBJECTIVE

Determine a rigorous and reproducible experimental design that combines
controlled performance workloads with real-world live websites.

INVESTIGATE:

1. How published browser/web-performance studies construct benchmark corpora.

2. Controlled benchmark applications versus real-world websites:
   strengths, limitations and appropriate claims.

3. Correct use of experimental terminology:
   baseline;
   control condition;
   treatment/perturbed condition;
   benchmark;
   workload;
   corpus.

4. How a controlled baseline website can be modified one factor at a time to
   establish sensitivity to particular performance defects.

5. Whether factorial designs or multi-factor variations are useful once
   single-factor behaviour is understood.

6. Selection of real-world websites:
   - random sampling;
   - stratified sampling;
   - purposive workload categories;
   - popularity-based samples;
   - framework/application categories.

7. Whether categories such as:
   "static",
   "image-heavy",
   "JavaScript-heavy",
   "poorly optimized"
   require quantitative operational definitions.

8. Recommended corpus sizes and what determines an adequate number of websites.

9. Controlling nuisance variables:
   - test order;
   - time of day;
   - server variation;
   - geographic location;
   - browser state;
   - cache state;
   - CDN behaviour;
   - third-party resources.

10. Randomization, blocking and counterbalancing strategies for performance
    experiments.

11. How repeated measurements should be nested across websites and agent profiles.

12. Reproducibility:
    - preserving controlled fixtures;
    - versioning test sites;
    - recording browser versions;
    - storing profiler configurations;
    - preserving raw measurements;
    - documenting external URLs that may later change.

13. Internal validity of controlled fixtures.

14. External/ecological validity of live-site evaluation.

15. Whether a hybrid controlled + real-world design is supported by existing
    systems/web-performance research.

OUTPUT

A. Review of experimental designs used in relevant literature.

B. Controlled-fixture design options.

C. Real-world corpus selection options.

D. Suggested ways to operationalize website workload categories.

E. Experimental-variable map:
   independent variables;
   dependent variables;
   controlled variables;
   nuisance variables.

Do not declare these final for my study.

F. Randomization/counterbalancing options.

G. Internal and external validity analysis.

H. Reproducibility requirements.

I. Priority original papers to download.

Do NOT invent an arbitrary sample size and do NOT formulate a final research gap
or hypothesis.
```

---

## 8. How I recommend running these

Run **all six Tier 1 investigations independently**. Ideally, do not show one report to the next Deep Research conversation; otherwise later investigations may inherit assumptions from earlier ones.

I suggest naming the outputs:

```text
T1.1 Metric Semantics
T1.2 Browser Instrumentation
T1.3 Synthetic Agents and External Validity
T1.4 Statistical Measurement
T1.5 Profiler Validation
T1.6 Experimental Design
```

For each one, download the most important papers it identifies rather than every paper mentioned.

Once all six reports return, **we should not immediately go to Tier 2**. There should be a short synthesis stage:

Six independent reports→verify important papers→cross-theme evidence map→identify contradictions / unanswered questions\text{Six independent reports} \rightarrow \text{verify important papers} \rightarrow \text{cross-theme evidence map} \rightarrow \text{identify contradictions / unanswered questions}

Then we decide what Tier 2 needs to investigate. That prevents us from spending time researching scoring, severity classification or secondary implementation issues before we know which parts are actually consequential to the eventual research question.

I would also move **profiler overhead out of the old optional Tier 3 status**: your proposal has made it sufficiently relevant that Tier 1.2 now explicitly investigates it. If that report shows that observer overhead is significant and that correction/calibration is an unresolved problem, we can then create a dedicated specialist Deep Research prompt solely for **profiler overhead modelling and compensation**.
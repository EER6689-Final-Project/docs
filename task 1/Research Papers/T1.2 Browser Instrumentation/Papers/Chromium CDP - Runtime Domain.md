# Chromium CDP - Runtime Domain

- **Citation:** Chromium authors. *Chrome DevTools Protocol — Runtime domain*, protocol documentation endpoint tot. https://chromedevtools.github.io/devtools-protocol/tot/Runtime/
- **Zotero key:** WRY7VL9Z.
- **Source:** Zotero snapshot saved 29 August 2026 (item version 1473); current tot page checked 12 October 2026. The endpoint is mutable; pin the Chromium build and protocol revision for implementation claims.

## Abstract and scope

The Runtime domain defines remote JavaScript evaluation, execution contexts, object handles, and runtime events. It documents the automation surface, not its effects on a page.

## Outline Summary

- **Central idea:** A CDP client can evaluate JavaScript in a selected context and exchange serialized values or remote object references.
- **Problem and objectives:** Specify runtime evaluation and object-management commands. Research questions, datasets, participants, and experimental setup are N/A for protocol documentation.
- **Approach:** Runtime.evaluate supports context selection, promise awaiting, and returnByValue. Non-primitive results can be RemoteObject handles; object groups and release commands manage those handles. Async call-stack capture is configured separately and defaults to depth zero.
- **Methods and interpretation:** Record context, evaluation options, stack settings, and handle lifetimes; release remote objects and groups when no longer needed.
- **Limitations:** Evaluation executes code in the page context and is an active intervention. The protocol gives no estimate of runtime, memory, or measurement effects.
- **Author-stated future work:** N/A; protocol documentation.
- **Relationship to T1.2:** Possible control/collection interface. Evaluation frequency, injected code, stack capture, and retained handles are candidate observer effects requiring separate measurement.
- **Important source references:** [Runtime.evaluate](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-evaluate), [RemoteObject](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#type-RemoteObject), [releaseObject](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-releaseObject), [releaseObjectGroup](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-releaseObjectGroup), and [setAsyncCallStackDepth](https://chromedevtools.github.io/devtools-protocol/tot/Runtime/#method-setAsyncCallStackDepth). No page numbers.
- **Concise takeaway:** CDP Runtime provides evaluation and remote object handling; direct effects on the observed workload remain unmeasured by the specification.

## T1.2 Evidence Check

- **Protocol claim:** Methods expose evaluation, context, remote-object, and async stack configuration behavior.
- **Preliminary inference:** Record settings and test evaluation/handle-retention effects; the protocol page does not quantify them.

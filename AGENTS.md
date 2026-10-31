# Repository Guidelines

## Project Structure

This repository contains research materials for the EEI6689 project, not application source code. The project files are under `task 1/`:

- `Research Management/` contains seven report-working files: its index, selected research plan, study source map, literature matrix, novelty cross-reference, current decision log, and focused verification queue.
- `Research Archive/` preserves earlier assessments, the evidence map, source inventories, full historical decisions/verification ledger, screening logs, and audit artifacts.
- `Research Papers/T1.1` through `T1.6/` contains topic syntheses and associated source PDFs. Topic-specific paper notes are kept in `Papers/` where applicable.
- `Thought process/` contains staged planning notes.
- The proposal (`EER6689_Project Proposal.docx`) and task brief (`My tasks.pdf`) are at the project root. `.memory/` contains supporting synthesis notes.

There is no application source, test suite, or build output directory.

## Development and Review

No build or test command is configured. Review edits directly in a Markdown editor and use Git to inspect changes:

```sh
git status --short
git diff -- "task 1/Research Management/Research Plan.md"
```

Keep generated or temporary files out of the repository unless they are project deliverables. Preserve source PDFs alongside the notes that analyze them.

## Writing and Naming

Use Markdown headings to make long research notes navigable. Keep claims specific, distinguish evidence from interpretation, and cite sources close to the supported claim. When source details still need checking, record them in `Research Management/Zotero Verification Queue.md` rather than presenting them as verified. Update the evidence map or decision log when a change affects project-wide conclusions or choices.

Use descriptive filenames and retain the existing topic numbering and folder names, such as `T1.4 Statistical Measurement/`. Match the surrounding document’s heading, citation, and list style when editing; there is no formatter or linter configured.

## Commits and Pull Requests

Use a short imperative subject with a conventional type prefix. The initial commit uses `docs: add EEI6689 research proposal and evidence base`; follow that pattern, for example `docs: clarify T1.2 instrumentation assumptions`.

For pull requests, explain the research documents changed and why, identify sources added or revised, and summarize any effect on the evidence map or project decisions. Link related issues when available. Screenshots are unnecessary for text-only changes; include them only when they help review a rendered artifact.

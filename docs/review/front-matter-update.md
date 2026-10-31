# Front-matter revision — 31 October 2026

The preceding research/report-plan changes were committed and pushed as
`fabf6f9`. The subsequent requested revision removes the project-group line
from the title page and the department lines from both identity pages. The
drafted declaration is replaced by both original pages of `docs/format.pdf`.

`pdfpages` reserves the two pages and the contents destination. The build's
pypdf preservation step restores the source PDF's original content streams,
resources and page geometry without replacing destination page references.
The supplied PDF is unchanged. Both inserted Letter pages match its extracted
text and are pixel-identical at 120 dpi; no report heading or folio is added.
Other pages remain A4. Introduction remains Chapter 1, and the declaration
contents link points to the first inserted page. The rebuilt report has 41 pages.

Validation details and hashes are in `front-matter-validation.json`.
The source, identity-page and checklist renders were checked. The earlier
content/build reviews remain historical snapshots of the 40-page plan;
this note records the requested front-matter changes. The font limitation
recorded there is unchanged at this stage.

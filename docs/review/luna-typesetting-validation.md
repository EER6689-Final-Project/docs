# Luna typesetting validation

**Status:** intermediate fresh proof after Astra's manuscript rewrite; do not treat as the final submission artifact until the separate final cleanup and rebuild are complete.

**Build:** `bash docs/tools/build-report.sh` completed on 2026-10-31. The PDF has 44 pages, is A4 for authored pages, and has SHA-256 `e050b7f4b8a71ae8469cddd5613e5eb238d00962dab4cee5f349dfe3be328d1b`. The final XeLaTeX log has no unresolved references, missing characters, or overfull boxes. The log does contain underfull boxes in narrow table cells and a URL; these are ragged-wrap warnings, not text extending past the page margins. The final bibliography build completed with Biber.

## Required type and line spacing

The shared style now directly selects `Times New Roman`; if unavailable, XeLaTeX fails instead of silently substituting another family. The installed-font receipt is `font-verification.json`. Authored body text is embedded as Times New Roman in the fresh PDF, with regular, bold, and italic faces present where used. The source formatting sets normal body text to 12 TeX pt on a 15 TeX pt baseline. This distinction matters because PDF coordinate points are bp (72 per inch), while TeX points are 72.27 per inch: 12 TeX pt renders as 11.955 PDF bp, and 15 TeX pt renders as 14.94396 PDF bp.

I measured successive normal-text line tops in four body pages using PDF character coordinates. Pages 11, 18, 26, and 34 each had median 14.94 PDF-bp spacing, matching 15 TeX pt within coordinate rounding. The sampled lines include regular prose in the introduction, literature review, methodology, and work-plan chapters; headings, lists, and paragraph gaps were excluded. Extracted normal-text glyph size was 11.955 PDF bp (12 TeX pt). This verifies the actual normal paragraph output, including body paragraphs after earlier list and table material. Paragraph spacing remains a separate 6 TeX pt source setting.

The List of Figures (physical page 8), List of Tables (page 9), and references (pages 40–44) showed a median 17.93 PDF-bp line increment for their 12 pt text, matching an 18 TeX pt baseline (1.5 spacing). The bibliography style declares 12/18 pt independently of normal body text.

## Other typography and source checks

- **F02 margins:** `geometry` sets left/top 1.5 in and right/bottom 1 in. The authored A4 body begins at the expected 108 bp left and top offsets; representative body text and folio remain inside the page.
- **F04 headings:** chapter headings use 22 TeX pt uppercase, with 14 TeX pt section headings. The rendered opening at physical page 11 shows the numbered, left-aligned chapter form and legible text.
- **I01/I02 identity pages:** source uses 18/27 pt titles, 14 pt bold “By” and course, 16 pt bold author, and the specified faculty, university, date/registration/supervisor treatments. Rendered pages 1–2 fit without clipping; cover has no folio and the title page has Roman folio `i`.
- **S02/S03 supplied guide pages:** physical pages 3–4 retain 612 × 792 PDF-bp geometry, equal extracted text, and pixel-identical 120-dpi renders to `format.pdf` pages 1–2. No overlay was introduced.
- **Shared build fixes:** fallback-font selection and its draft status macro were removed from `report-format.sty`; the long work-plan table's final column was reduced from 43% to 42% of text width to remove a 2.65 pt overfull alignment. The fresh build has no remaining overfull-box warning.

This proof records the requested typography/runtime verification. Structural and content checks outside these IDs remain with the separate structure review. The exact full-caption wording, all margins on every page, and every heading/identity field were not exhaustively re-audited here. Embedded fonts belonging to the preserved original guide pages and plotted/math material are part of those source assets; they do not change the measured Times New Roman body text.

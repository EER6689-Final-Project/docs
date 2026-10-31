#!/usr/bin/env bash
# Build the existing report-writing plan without installing or downloading tools.
set -euo pipefail
report_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd -- "$report_root"
if ! command -v xelatex >/dev/null 2>&1; then
  report_tex_bin="${HOME}/.local/texlive/2026/bin/x86_64-linux"
  if [[ -x "$report_tex_bin/xelatex" ]]; then
    export PATH="$report_tex_bin:$PATH"
  fi
fi
for report_tool in xelatex biber; do
  if ! command -v "$report_tool" >/dev/null 2>&1; then
    printf 'Required tool is unavailable: %s\n' "$report_tool" >&2
    exit 1
  fi
done
# Minimal TeX Live installations may omit prebuilt formats and the Perl modules
# used by mktexfmt. Build a temporary XeLaTeX format directly in that case.
if ! kpsewhich -format=fmt xelatex.fmt >/dev/null 2>&1; then
  report_format_dir="$(mktemp -d "${TMPDIR:-/tmp}/eei6689-xelatex.XXXXXX")"
  (cd -- "$report_format_dir" && xetex -ini -etex -jobname=xelatex xelatex.ini >format.log)
  export TEXFORMATS="$report_format_dir:"
fi
# Run the tools directly: some minimal Perl installations ship latexmk without
# the core File::Copy module it needs.
xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
biber main
xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
report_pdf_python=python3
if ! "$report_pdf_python" -c 'import pypdf' >/dev/null 2>&1; then
  report_pdf_python="${HOME}/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
fi
"$report_pdf_python" tools/preserve-format-pages.py
printf 'Built %s/main.pdf. Inspect the font notice and review record before submission.\n' "$report_root"

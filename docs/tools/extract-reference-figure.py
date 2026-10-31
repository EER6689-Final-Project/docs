"""Reproduce the attributed planning illustration from the preserved source PDF.

Run from any directory with Python and pypdf. The original source is read only.
"""
from hashlib import sha256
import json
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

docs = Path(__file__).resolve().parents[1]
project = docs.parent
source = project / 'task 1/Research Archive/Review Artifacts/2026-10-31 Decision-Critical Source Checks/Sources/Hindsight - NSDI 2023.pdf'
target = docs / 'figures/hindsight-trace-lifecycle.pdf'
page = PdfReader(source).pages[5]
box = [314, 568, 561, 727]
page.mediabox = RectangleObject(box)
page.cropbox = RectangleObject(box)
writer = PdfWriter()
writer.add_page(page)
with target.open('wb') as output:
    writer.write(output)
record = {
    'asset': target.name,
    'source_zotero_key': '3ED3FDXH',
    'source_file': str(source.relative_to(project)),
    'source_sha256': sha256(source.read_bytes()).hexdigest(),
    'source_pdf_page_1_based': 6,
    'source_printed_page': 325,
    'source_figure': 'Figure 2',
    'crop_points_pdf_coordinates': box,
    'transform': 'Crop only; no content redrawn or data altered. Source caption excluded; report caption supplies citation.',
    'purpose': 'Illustrate original-event retention as prior art, not a browser implementation or experimental finding.',
    'reuse_status': 'Attributed reference illustration in a planning document; publication permissions/licence must be checked before external republication.',
}
(docs / 'figures/provenance.json').write_text(json.dumps([record], indent=2) + '\n')
print(target)

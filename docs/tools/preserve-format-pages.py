"""Preserve the supplied checklist and retain only submission metadata."""
from pathlib import Path
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject

docs = Path(__file__).resolve().parents[1]
report = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else docs / 'main.pdf'
source = PdfReader(docs / 'format.pdf')
metadata = PdfReader(report).metadata or {}
writer = PdfWriter(clone_from=report)
assert len(source.pages) == 2, 'Review insertion positions if format.pdf changes.'
keys = ('/Contents', '/Resources', '/MediaBox', '/CropBox', '/Rotate',
        '/BleedBox', '/TrimBox', '/ArtBox', '/UserUnit', '/Group', '/Annots')
for index, original in enumerate(source.pages):
    target = writer.pages[index + 2]
    assert ' '.join(original.extract_text().split()) == ' '.join(target.extract_text().split()), 'Unexpected checklist insertion position.'
    copied = original.clone(writer, ignore_fields=('/Parent',))
    for field in keys:
        target.pop(NameObject(field), None)
        if field in copied:
            target[NameObject(field)] = copied.raw_get(field)
# Keep bibliographic identity, excluding tool provenance and inherited XMP.
submission_metadata = {field: str(metadata[field]) for field in
                       ('/Title', '/Author', '/Subject', '/Keywords')
                       if metadata.get(field)}
writer.metadata = None
writer.add_metadata(submission_metadata)
writer.root_object.pop(NameObject('/Metadata'), None)
temporary = report.with_suffix('.preserved.pdf')
with temporary.open('wb') as output:
    writer.write(output)
temporary.replace(report)
print('Preserved both original checklist pages and retained only submission metadata.')

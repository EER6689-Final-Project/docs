from pathlib import Path
import hashlib,json,datetime
p=Path(__file__).parent
files={f.name:{'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size} for f in sorted(p.iterdir()) if f.is_file() and f.name!='file_manifest.json'}
(p/'file_manifest.json').write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exact Sol Scholar Batch4 Final50 directory; excludes this self-referential manifest; no external files written','files':files},indent=2)+'\n')

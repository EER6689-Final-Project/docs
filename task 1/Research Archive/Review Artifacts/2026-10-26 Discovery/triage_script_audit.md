# Historical triage implementation — not endorsed eligibility rules

Read-only script evidence preserved 2026-10-26. These scripts were inspected, not rerun. Original source SHA-256 is recorded below and in manifest.json. The README explains the unresolved ERP §§7/9 deviation. No project application code is introduced.

## final_screen.py

Original scratch path: `/tmp/opencode/eei6689-discovery/final_screen.py`; SHA-256 `2924fd339b46260c6bea4e662da054a275fc106e905bcde63de2c50da871c09e`.

```python
import csv,json,re,unicodedata,subprocess
from pathlib import Path
from collections import defaultdict
D=Path('/tmp/opencode/eei6689-discovery');root=Path('/home/mendydias/Projects/eei6689')
rows=[]
with (D/'screening_records.csv').open(encoding='utf8') as f:
 for x in csv.DictReader(f):
  if x['operation'].startswith('OpenAlex_'):rows.append(x)
with (D/'scholar_final_first50.csv').open(encoding='utf8') as f:rows.extend(csv.DictReader(f))
paths=[p.name for p in (root/'task 1').rglob('*.md')]
def norm(s):return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',s.lower()).encode('ascii','ignore').decode()).strip()
base={norm(Path(p).stem):p for p in paths}
seen={};out=[]
for r in rows:
 op=r.get('operation','');title=re.sub(r'^\[(?:PDF|HTML|BOOK|CITATION|PATENT)\]\s*','',r.get('title',''),flags=re.I).strip();meta=r.get('metadata','');doi='';year='';lang='';pubdate=''
 try:
  m=json.loads(meta);doi=m.get('doi','') or '';year=m.get('publication_year','') or '';lang=m.get('language','') or '';pubdate=m.get('publication_date','') or ''
 except: m={}
 if not year:
  m_year=re.search(r'(?<!\d)(19|20)\d{2}(?!\d)',meta)
  if m_year:year=m_year.group(0)
 key='doi:'+doi.lower().replace('https://doi.org/','') if doi else 'title:'+norm(title)
 dup=key in seen;seen.setdefault(key,op+':'+str(r.get('rank','')))
 q=r.get('query',''); tag=r.get('record_label','')
 if dup:dec='DUP';reason='Duplicate occurrence by exact DOI or normalized title in this discovery export; preserve occurrence; not a new work.'
 elif year and int(year)>2026:dec='X1';reason='Displayed publication year is after cutoff 2026-10-25.'
 elif pubdate and pubdate>'2026-10-25':dec='X1';reason='Publication date is after cutoff 2026-10-25.'
 elif lang and lang.lower() not in ('en','eng','english'):dec='X2';reason='OpenAlex metadata language is non-English; authorized English translation not established.'
 elif re.search(r'\[(?:PATENT|CITATION)\]',tag+' '+r.get('title',''),re.I):dec='X4';reason='Search platform marks item as patent or citation-only; excluded as primary evidence.'
 elif op.startswith('OpenAlex_'):
  blob=(title+' '+r.get('abstract','')).lower()
  if any(k in blob for k in ['browser','web performance','webpage','web page','lighthouse','javascript performance','browser performance','web timing','instrumentation','profiler','performance measurement','benchmarking','measurement perturbation','method comparison','agreement','repeated measurement','synthetic workload']):dec='ADVANCE';reason='Title/abstract has plausible R1–R6 relevance; advance at stage 1. Reconstructed OpenAlex inverted-index abstract is marked as such. No full text inferred.'
  else:dec='X3';reason='Title/abstract shows no plausible R1–R6 target or stated transfer; discovery-stage X3 only.'
 else:
  dec='ADVANCE';reason='Title/metadata/snippet insufficient to exclude; advance as uncertain. Search snippet is not an abstract/full text.'
 basename=base.get(norm(title),'')
 out.append({'operation':op,'query':q,'rank':r.get('rank',''),'title':title,'display_record_label':tag,'dedup_key':key,'duplicate_occurrence':str(dup),'first_occurrence':seen[key],'local_exact_filename_match':basename,'publication_year':year,'publication_date':pubdate,'language':lang,'source_platform':'OpenAlex' if op.startswith('OpenAlex_') else 'Google Scholar','abstract_or_snippet':r.get('abstract',r.get('snippet','')),'abstract_status':r.get('abstract_status',''),'stage1_decision':dec,'stage1_primary_code':dec if dec in ('X1','X2','X3','X4','DUP') else 'advance/uncertain','stage1_reason':reason,'stage2':('FT-PENDING; no full text inspected' if dec=='ADVANCE' else ('duplicate occurrence; follow first-occurrence disposition' if dec=='DUP' else 'not advanced; stage 2 not performed')),'reviewer':'Luna discovery pass; owner confirmation required','review_date':'2026-10-26','SID':'NOT ASSIGNED; crosswalk to canonical inventories/notes not ready'})
with (D/'stage1_screening.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
by=defaultdict(lambda:defaultdict(int))
for x in out:by[x['operation']][x['stage1_decision']]+=1
(D/'stage1_summary.json').write_text(json.dumps({k:dict(v) for k,v in by.items()},indent=2))
from collections import Counter
print('screened occurrences',len(out),'provisional identity keys',len(seen),'exact note filename matches',sum(bool(x['local_exact_filename_match']) for x in out))
print('overall',dict(Counter(x['stage1_decision'] for x in out)))
print('source records',dict(Counter(x['source_platform'] for x in out)))
print('scholar per operation')
for k in sorted(by):
 if k.startswith('ScholarFinal') and k.endswith('start0'): print(k,dict(by[k]))
```

## enrich_screen.py

Original scratch path: `/tmp/opencode/eei6689-discovery/enrich_screen.py`; SHA-256 `e6fb14670fb369646b926b7491882d5033f1ae2a74a5c2a73950e5d4eb087049`.

```python
import csv,json,re,hashlib
from pathlib import Path
from bs4 import BeautifulSoup
D=Path('/tmp/opencode/eei6689-discovery'); root=Path('/home/mendydias/Projects/eei6689/task 1')
# query-to-Q mapping from preserved receipts
recs=json.loads((D/'operation_receipts.json').read_text())['receipts']
qmap={r['operation']:r.get('proposed_Q_ID','') for r in recs}
# extract Google Scholar result cids from saved final HTML without making network requests
cidmap={}
for p in D.glob('ScholarFinal_*.raw'):
 op=p.stem; start=int(re.search(r'_start(\d+)$',op).group(1)); soup=BeautifulSoup(p.read_bytes(),'html.parser')
 cards=soup.select('.gs_r.gs_or.gs_scl')
 for i,c in enumerate(cards,start+1):
  if i<=50: cidmap[(op,i)]=c.get('data-cid','')
rows=list(csv.DictReader((D/'stage1_screening.csv').open(encoding='utf8')))
for r in rows:
 r['Q_ID']=qmap.get(r['operation'],'')
 r['platform_record_id']='';r['record_url']='';r['doi']='';r['raw_record_metadata']=''
 if r['source_platform']=='OpenAlex':
  try:
   m=json.loads(r['abstract_or_snippet']) if False else {}
   # retrieve metadata from raw extraction CSV by op/rank below
  except: pass
  # OpenAlex record identifier preserved in the metadata JSON in screening_records.csv
 else:
  op=r['operation'];rank=int(r['rank']);r['platform_record_id']=cidmap.get((op,rank),'');
  r['record_url']=''
# Join full source records by (operation, rank)
source={}
for f in ['screening_records.csv','scholar_final_first50.csv']:
 p=D/f
 if not p.exists():continue
 with p.open(encoding='utf8') as z:
  for x in csv.DictReader(z):source[(x.get('operation'),str(x.get('rank')))]=x
for r in rows:
 x=source.get((r['operation'],str(r['rank'])),{})
 r['record_url']=x.get('url','')
 meta=x.get('metadata','')
 r['raw_record_metadata']=meta
 try:
  m=json.loads(meta);r['platform_record_id']=m.get('openalex_id','') or r['platform_record_id'];r['doi']=m.get('doi','')
 except: pass
# Write stable ordered columns
cols=list(rows[0].keys())
with (D/'stage1_screening.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
print('rows',len(rows),'doc IDs',sum(bool(r['platform_record_id']) for r in rows),'URLs',sum(bool(r['record_url']) for r in rows),'DOI',sum(bool(r['doi']) for r in rows),'Q',sum(bool(r['Q_ID']) for r in rows))
```

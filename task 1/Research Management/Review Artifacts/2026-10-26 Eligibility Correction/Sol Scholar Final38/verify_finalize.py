import csv, json, hashlib, datetime
from pathlib import Path
from collections import Counter
P=Path(__file__).parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x): (P/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
freeze=json.loads((P/'target_freeze.json').read_text()); second=json.loads((P/'secondary_freeze.json').read_text())
source=Path(freeze['source_path']); assert sha(source)==freeze['source_sha256']
assert all(sha(Path(p))==h for p,h in freeze['producer_files'].items())
assert sha(P/'primary_checks.json')==second['primary_sha256']
checks=json.loads((P/'primary_checks.json').read_text())['items']; ids=freeze['ordered_target_EIDs']
assert [c['target_E_ID'] for c in checks]==ids
assert [c['event_E_ID'] for c in checks]==freeze['ordered_event_EIDs']
notes=json.loads((P/'secondary_notes.json').read_text())
assert set(notes)==set(second['finite_error_pattern_expansion_ordered'])==set(ids)
reread=[json.loads(line) for line in (P/'secondary_original_reread.jsonl').read_text().splitlines()]
assert [r['occurrence_E_ID'] for r in reread]==ids
with source.open(encoding='utf-8-sig',newline='') as f:
    reader=csv.DictReader(f);fields=reader.fieldnames; original={r['occurrence_E_ID']:r for r in reader if r['occurrence_E_ID'] in ids}
with (P/'overlay.csv').open(newline='',encoding='utf-8') as f: overlay=list(csv.DictReader(f))
assert len(overlay)==38
assert all(all(r[k]==original[r['occurrence_E_ID']][k] for k in fields) for r in overlay)
assert all(all(original[r['occurrence_E_ID']][k]==v for k,v in r.items()) for r in reread)
assert all(len(c['R1_R6'])==6 and c['claim_support']=='UNASSESSED' and c['methodological_confidence']=='UNASSESSED' and c['fulltext']=='NOT RUN' and c['citation']=='NOT RUN' for c in checks)
results=[]
for c in checks:
    results.append({'target_E_ID':c['target_E_ID'],'secondary_actual_original_reread':True,'R1_R6_rechallenged':True,'producer_X3':c['producer_stage1']=='X3','Sol_X3':c['stage1']=='X3','result':'retain primary with stated limitations','note':notes[c['target_E_ID']]})
    save('secondary_checks.json',{'reviewer':'Sol AI self-audit, not independent human scientific review','recorded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'secondary_freeze_sha256':sha(P/'secondary_freeze.json'),'reread_sha256':sha(P/'secondary_original_reread.jsonl'),'items':results,'completed':len(results),'unreviewed':38-len(results)})
save('group_QC.json',{'group_basis':'Corrected explicit positive and unresolved R groups plus whole method/type proxy groups; not canonical S-ID/C-ID claim QC','groups':[{'group':g,'members':members,'selected_first_EID':members[0],'actually_reread':True,'secondary_note':notes[members[0]],'status':'checked against original export; primary retained with uncertainty limits'} for g,members in second['corrected_explicit_groups'].items()],'R5_positive_group':'none; absence is not verified absence in full texts','unverified':'Source types, dates, language, identities, originality, claims and full texts remain unverified.'})
with (P/'item_checks.tsv').open('w',encoding='utf-8',newline='') as f:
    names=['target_E_ID','event_E_ID','stage1','producer_stage1','producer_X3_adjudication','type_proxy','method_proxy','reason','R1_R6','secondary_note']; w=csv.DictWriter(f,fieldnames=names,delimiter='\t',extrasaction='ignore');w.writeheader()
    for c in checks: w.writerow({**c,'R1_R6':json.dumps(c['R1_R6'],ensure_ascii=False),'secondary_note':notes[c['target_E_ID']]})
counts={'scope':'DELTA ONLY E-1000–E-1037; no accepted snapshot mutation','primary_checked':38,'primary_unreviewed':0,'R_judgments':228,'effective_stage1':dict(Counter(c['stage1'] for c in checks)),'producer_stage1':dict(Counter(c['producer_stage1'] for c in checks)),'producer_X3_checked':16,'producer_X3_retained':sum(c['producer_stage1']=='X3' and c['stage1']=='X3' for c in checks),'producer_X3_rejected':sum(c['producer_stage1']=='X3' and c['stage1']!='X3' for c in checks),'producer_X3_rejected_destinations':dict(Counter(c['stage1'] for c in checks if c['producer_stage1']=='X3' and c['stage1']!='X3')),'transitions':dict(Counter(c['producer_stage1']+' -> '+c['stage1'] for c in checks)),'changed_dispositions':sum(c['stage1']!=c['producer_stage1'] for c in checks),'secondary_minimum_selected':len(second['minimum_selected_ordered']),'secondary_expanded_checked':38,'secondary_unreviewed':0,'explicit_proxy_groups_checked':len(second['corrected_explicit_groups']),'secondary_primary_revisions':0,'mechanical_verification':'PASS: original-column values, input/producer hashes, ordered targets/events, original reread equality, six R judgments, coverage and unassessed/not-run invariants'}
save('counts.json',counts)
print(json.dumps(counts,indent=2))

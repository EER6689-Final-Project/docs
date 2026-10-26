"""Validate exact read/decision coverage and write the final owned-output manifest."""
import ast
import csv
import json
from collections import Counter
from datetime import datetime, timezone
from review_tools import HERE, QUEUE, SNAPSHOT, FREEZE, PROSPECTIVE, load, sha, stamp

f,q,s=load()
assert sha(PROSPECTIVE.read_bytes())==f['base_freeze_sha256']
expected_metadata_fields=('publication_year','publication_date','language','doi','platform_record_id','record_url','raw_record_metadata','operation','query','rank','source_platform')
read_sets={}
for phase in ('primary','secondary','pattern'):
    seen=[]
    for p in sorted(HERE.glob(phase+'_read_receipt*.json')):
        receipt=json.loads(p.read_text()); assert receipt['phase']==phase
        for r in receipt['records']:
            e=r['target']; original=q[e]
            assert r['title']==original['title']
            assert r['entire_abstract']==original['abstract_or_snippet']
            assert r['abstract_status']==original['abstract_status']
            assert r['metadata']=={k:original[k] for k in expected_metadata_fields}
            assert r['queue_record_sha256']==sha(json.dumps(original,ensure_ascii=False,sort_keys=True).encode())
            assert r['event']==f"E-{3500+f['exact_targets'].index(e)}"
            seen.append(e)
    assert len(seen)==len(set(seen))
    read_sets[phase]=seen
assert read_sets['primary']==f['exact_targets']
sf=json.loads((HERE/'secondary_freeze.json').read_text())
assert read_sets['secondary']==sf['selected_targets']
pat=json.loads((HERE/'secondary_pattern_expansion_freeze.json').read_text())
assert read_sets['pattern']==pat['exact_targets']
pf=json.loads((HERE/'primary_results_freeze.json').read_text())
for name,h in pf['primary_output_hashes'].items():assert sha((HERE/name).read_bytes())==h
assert sha((HERE/'primary_results_freeze.json').read_bytes())==sf['primary_results_freeze_sha256']
rows=list(csv.DictReader((HERE/'overlay_130_final.csv').open()))
assert [r['target_occurrence_EID'] for r in rows]==f['exact_targets']
assert [r['new_review_event_EID'] for r in rows]==[f'E-{i}' for i in range(3500,3630)]
mc=Counter()
for row in rows:
    e=row['target_occurrence_EID']; a=json.loads(row['affected_mapping_judgments_json'])
    affected={g['R'] for g in f['affected_groups'] if e in g['members']}
    assert set(a)==affected
    original=set(filter(None,s[e]['effective_RIDs'].split(';')))
    inherited=original-affected
    assert set(filter(None,row['inherited_unrevalidated_RIDs'].split(';')))==inherited
    final=inherited|{r for r,v in a.items() if v[0]=='supported'}
    assert set(filter(None,row['corrected_explicit_RIDs'].split(';')))==final
    assert final<=original
    assert row['proposed_stage1_status'] in ('ADVANCE','PENDING')
    if s[e]['effective_stage1_status']=='PENDING':assert row['proposed_stage1_status']=='PENDING'
    for key in ('claim_support','methodological_confidence'):assert row[key]=='UNASSESSED'
    for key in ('fulltext','citations'):assert row[key]=='NOT RUN'
    for v in a.values():mc[v[0]]+=1
assert mc==Counter(supported=87,unclear=44,outside=20)
qcs=list(csv.DictReader((HERE/'secondary_QA_results.csv').open()))
assert len(qcs)==65 and len({r['target_occurrence_EID'] for r in qcs})==65
assert {r['target_occurrence_EID'] for r in qcs}==set(read_sets['secondary']+read_sets['pattern'])
for p in HERE.glob('*.py'):ast.parse(p.read_text())
counts=json.loads((HERE/'final_counts.json').read_text())
assert counts['final_affected_mapping_results']==dict(mc)
validation={'validated_at_utc':stamp(),'state':'CHECKED artifact integrity; not scientific approval',
    'primary_exact_original_field_comparisons':130,'secondary_exact_original_field_comparisons':63,
    'additional_pattern_exact_original_field_comparisons':2,'target_order_and_event_range':'PASS',
    'frozen_primary_hashes':'UNCHANGED','input_hashes':'MATCH','inherited_mappings':'PRESERVED, NOT REVALIDATED',
    'new_mappings':0,'new_exclusions':0,'source_claims':'UNASSESSED','fulltext_citations':'NOT RUN',
    'source_scientific_eligibility':'PENDING original identity/date/language/type verification',
    'final_mapping_counts':dict(mc),'unclear_target_count':len(counts['unclear_mapping_targets']),
    'all_OA_QC_pass':False,'G3':'OPEN','G4':'OPEN'}
p=HERE/'validation_results.json';assert not p.exists();p.write_text(json.dumps(validation,indent=2)+'\n')
def info(p):
    return {'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,
        'observed_filesystem_mtime_utc':datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat()}
manifest={'generated_at_utc':stamp(),'owner_scope':str(HERE),
    'final_import_candidate':'overlay_130_final.csv','final_handoff':'reviewer_handoff.md',
    'input_hashes':{str(p):info(p) for p in (QUEUE,SNAPSHOT,FREEZE,PROSPECTIVE)},
    'outputs':{p.name:info(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='output_manifest.json'},
    'manifest_self_hash':'Not embedded; hash externally after generation.',
    'mtime_caveat':'Observed filesystem metadata, not semantic reading durations. Read-emission times are separately recorded.',
    'mutations':'Owned new subtree only; no merge, shared tracker, accepted CSV, source, library, staging or commit modification',
    'reviewer':'Sol AI technical self-audit, not independent human scientific review'}
p=HERE/'output_manifest.json';assert not p.exists();p.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'validation':validation,'output_manifest_sha256':sha(p.read_bytes()),'final_overlay_sha256':sha((HERE/'overlay_130_final.csv').read_bytes())},indent=2))

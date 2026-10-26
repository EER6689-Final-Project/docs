from pathlib import Path
import hashlib,json,datetime
ROOT=Path.cwd()
OUT=Path(__file__).parent
BASE=OUT.parent
PROD=BASE/'Scholar Batch4 Remaining75'
QUEUE=ROOT/'task 1/Research Management/Review Artifacts/2026-10-26 Discovery/REVIEWQUEUE.csv'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
files=[QUEUE,ROOT/'task 1/Research Management/Evidence Review Protocol.md',ROOT/'task 1/Research Management/Scope Resolution.md']+[PROD/n for n in ['remaining50_freeze.json','overlay_remaining50.csv','authored_remaining_750_774.json','authored_remaining_775_799.json','secondary_remaining50_freeze.json','secondary_remaining50_results.json','remaining50_counts.json','handoff.md','file_manifest.json','primary_overlay_frozen_for_QA.csv']]
if __name__=='__main__':
    target=OUT/'target_freeze.json'
    assert not target.exists()
    target.write_text(json.dumps({'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'before original target semantic reads','targets':[f'E-{i:04}' for i in range(750,800)],'events':[f'E-{i:04}' for i in range(3825,3875)],'inputs':{str(p.relative_to(ROOT)):sha(p) for p in files},'boundary':'Only assigned 50 files frozen by actual present hashes; shared producer folder/manifest may have grown. No assumption of historical whole-folder immutability.'},indent=2)+'\n')

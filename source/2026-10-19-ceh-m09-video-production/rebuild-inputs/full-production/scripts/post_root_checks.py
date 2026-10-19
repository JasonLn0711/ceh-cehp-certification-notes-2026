"""Run complete native seek checks after the actual 58-scene composition is checked."""
from pathlib import Path
import json,time,sys,subprocess
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';began=time.monotonic()
while True:
 d=json.load(open(Q/'prepare-master-process.json'))
 if d['status']=='failed':raise RuntimeError('Full-project preparation failed; inspect prepare-master.log')
 print(json.dumps({'phase':'waiting_checked_full_project_for_seek_audit','state':d['status'],'elapsed_seconds':round(time.monotonic()-began)}),flush=True)
 if d['status']=='completed':break
 time.sleep(15)
subprocess.run([sys.executable,str(R/'scripts/audit_scene_seek_stage.py')],cwd=R,check=True)
print(json.dumps({'phase':'actual_full_scene_seek_audit_complete','scenes':58}),flush=True)

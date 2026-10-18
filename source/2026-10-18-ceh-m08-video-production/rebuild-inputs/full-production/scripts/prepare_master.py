#!/usr/bin/env python3
"""Wait for all final chapter compositions, then check the full project and quizzes."""
from pathlib import Path
import json, subprocess, sys, time
from chapter import fingerprint, ENV, HF
ROOT=Path(__file__).resolve().parents[1];QA=ROOT.parent/'qa';started=time.monotonic()
while True:
 ready=[]
 for i in range(1,12):
  ch=f'C{i:02}';f=QA/f'{ch}-checked-fingerprint.json'
  if f.exists() and fingerprint(ROOT/'chapters'/ch)==json.loads(f.read_text())['sha256']:ready.append(ch)
 print(json.dumps({'phase':'waiting_checked_chapter_compositions','completed':len(ready),'total':11,'chapters':ready,'elapsed_seconds':round(time.monotonic()-started)}),flush=True)
 if len(ready)==11:break
 time.sleep(10)
for name in ['assemble_project.py','export_metadata.py']:
 print(json.dumps({'phase':'starting','script':name}),flush=True)
 subprocess.run([sys.executable,str(ROOT/'scripts'/name)],cwd=ROOT,check=True)
m=json.loads((ROOT/'data/master-timing.json').read_text())
times=[s['start']+s['duration']/2 for s in m['scenes']]+[(s['start']+s['end'])/2 for s in m['silences']]
print(json.dumps({'phase':'full_project_browser_check','sample_times':len(times)}),flush=True)
with (QA/'master-project-check.json').open('w') as log:
 subprocess.run([HF,'check',str(ROOT),'--at',','.join(f'{t:.6f}' for t in times),'--json'],cwd=ROOT,env=ENV,stdout=log,check=True)
c=json.loads((QA/'master-project-check.json').read_text());assert c['ok'] and not c['browserSkipped']
subprocess.run(['node',str(ROOT/'scripts/audit_quiz.mjs')],cwd=ROOT,env=ENV,check=True)
print(json.dumps({'phase':'full_project_and_quiz_checks_complete','elapsed_seconds':round(time.monotonic()-started)}),flush=True)

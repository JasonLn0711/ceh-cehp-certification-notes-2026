"""Map actual composed GSAP timelines with an isolated pinned analysis helper."""
from pathlib import Path
import os,subprocess,json,time,sys
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa'
while True:
 p=Q/'prepare-master-process.json';d=json.load(open(p))
 if d['status']=='completed':break
 if d['status']=='failed':raise RuntimeError('Master preparation failed; inspect prepare-master.log')
 print(json.dumps({'phase':'waiting_full_composition_for_motion_map','state':d['status']}),flush=True);time.sleep(15)
env=os.environ.copy();env.update(HYPERFRAMES_SKILL_NODE_MODULES=str(Q/'animation-helper/node_modules'),HYPERFRAMES_SKILL_PKG_VERSION='0.8.170',HYPERFRAMES_BROWSER_PATH='/home/jnlngx10/.cache/ms-playwright/chromium_headless_shell-1234/chrome-linux/headless_shell')
helper=Path('/home/jnlngx10/.agents/skills/hyperframes-animation/scripts/animation-map.mjs')
subprocess.run(['node',str(helper),str(R),'--frames','2','--out',str(Q/'full-animation-map'),'--min-duration','0.7'],cwd=R,env=env,check=True)
d=json.load(open(Q/'full-animation-map/animation-map.json'))
receipt={'status':'actual_composition_motion_map_generated','render_runtime':json.load(open(R/'node_modules/hyperframes/package.json'))['version'],'analysis_helper':{'producer':'0.8.170','core':'0.8.170'},'reason':'The optional producer0.8.171 helper depends on unpublished core0.8.171; isolated matching0.8.170 analysis packages do not modify the pinned0.8.171 renderer.','total_tweens':d['totalTweens'],'mapped_tweens':d['mappedTweens'],'scope':'Actual full composition GSAP geometry and timing diagnostics; flags require contextual review, separately from final encoded output.'}
(Q/'animation-helper-receipt.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt),flush=True)

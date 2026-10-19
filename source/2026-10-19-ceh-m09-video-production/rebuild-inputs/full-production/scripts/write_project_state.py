"""Update production navigation from verified completion, preserving immutable inputs."""
from pathlib import Path
import json,re,hashlib,subprocess,platform
from production_settings import MASTER_FILENAME
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';O=R.parent/'output'
d=json.load(open(Q/'delivery-validation.json'));assert d['status']=='automated_delivery_checks_passed'
(R/'README.md').write_text(f'''# CEH M09 Social Engineering — rendered production project

All 11 chapters and 58 animated scenes are rendered. The complete canonical narration has 9,814 spoken words; the measured film is {d['duration']:.6f} seconds / {d['frames']:,} frames at 1920 × 1080 / 30 fps. Approved M04 v3 Tally/Northstar design, baseline0.73 af_heart voice and exactly one narration-only1.5× pass are preserved. Each of the eight complete quiz questions has a1.000-second zero-PCM hold before its answer.

Start with [EDITING.md](EDITING.md), [BRIEF.md](BRIEF.md), [DESIGN.md](DESIGN.md), [the adopted series standard](PRODUCTION_STANDARD_v1.0.md) and [the full production instruction](AGENT_PROMPT.md). The original 305-file source ZIP and extraction remain immutable under `../inputs/`.

Final media and subtitles are in `../output/`, beginning with `{MASTER_FILENAME}` and `render_report.md`. Measured timing is `data/master-timing.json`; actual chapter/full-master evidence is `../qa/`. Human viewing/listening, learner progress and public release remain separate gates. The source package's earlier source-ready status remains recorded in the immutable input README.
'''.replace('baseline0.73','baseline 0.73').replace('narration-only1.5','narration-only 1.5').replace('a1.000','a 1.000'))
(R/'RENDER_PLAN.md').write_text('''# Full-film execution receipt and rebuild route

Current state: all 11 chapters / 58 scenes rendered and automated delivery checks passed. Actual files, hashes, review limits and exact durations are in `../output/render_report.md` and `../qa/delivery-validation.json`. The original source-ready plan remains in `../inputs/package/CEH_M09_English_Editorial_Masterclass/RENDER_PLAN.md`.

Measured speech and eight exact zero buffers govern scene timing. Final captions were aligned to processed speech. Native layers use finite paused timelines with narration anchors; chapter and full-project browser checks, scene seek comparisons and actual encoded sampling retain separate receipts. Chapters have input/output fingerprints and can be rebuilt independently.

Follow EDITING.md for a scoped change. Preserve unchanged audio and chapters; inspect the changed composition, render it, rebuild the continuous master and rerun checks affected by that change. Full human viewing/listening remains the next acceptance layer. Public media release requires a separate authorized action and verified URL.
''')
p=R/'STORYBOARD.md';text=p.read_text();assert len(re.findall(r'^- status: animated$',text,re.M))==58;assert 'measured from the final' in text
(R/'START_HERE_zh-TW.md').write_text('''# M09 完整製片成果入口

11 章、58 幕與完整英文配音已完成實際渲染；完整字幕、章節影片、零值 PCM 參考音軌及可編輯專案均依實際 QA 留證。

先讀 `EDITING.md`，成品與檢查報告位於 `../output/`，實際製作證據位於 `../qa/`。原始 ZIP 與來源包保留在 `../inputs/`。完整人工觀影／聽驗、本人學習進度與公開媒體發布各有獨立驗收；本次製片不新增學習時段或期限。
''')
def sha(p):
 with p.open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
files=[*sorted((R/'scripts').glob('*.py')),*sorted((R/'scripts').glob('*.mjs')),*sorted((R/'scripts').glob('*.json')),R/'package.json',R/'package-lock.json',R/'requirements-lock.txt',R/'data/production-overrides.json',R/'data/voice-calibration.json']
(Q/'production-provenance.json').write_text(json.dumps({'module':'M09','source_zip_sha256':sha(R.parent/'inputs/CEH_M09_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip'),'hyperframes':json.load(open(R/'node_modules/hyperframes/package.json'))['version'],'node':subprocess.check_output(['node','--version'],text=True).strip(),'python':platform.python_version(),'ffmpeg':subprocess.check_output(['ffmpeg','-version'],text=True).splitlines()[0],'files':[{'path':str(f.relative_to(R)),'sha256':sha(f)} for f in files],'scope':'Actual production implementation and pinned runtime identity; media payloads have separate delivery/extraction manifests.'},indent=2))
print(json.dumps({'state':'rendered_and_automated_QA_passed','implementation_files':len(files)}))

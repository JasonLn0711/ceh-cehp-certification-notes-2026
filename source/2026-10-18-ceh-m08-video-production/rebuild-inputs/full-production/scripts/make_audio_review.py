"""Create a local audition queue without claiming human listening acceptance."""
from pathlib import Path
import json,html
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';D=Q/'audio-audition';D.mkdir(exist_ok=True)
d=json.load(open(Q/'audio-review-diagnostics.json'));flags={}
for f in d['alignment_flags']:flags.setdefault(f['file'],[]).append(f)
rows=[];sections=[]
for key,items in sorted(flags.items()):
 sid,number=key.replace('.json','').split('-');a=json.load(open(R/'data'/f'{sid}.audio.json'));seg=next(s for s in a['segments'] if s['kind']=='spoken' and s['sentence']==int(number));rows.append({'scene':sid,'sentence':int(number),'path':seg['path'],'audio_sha256':seg['sha256'],'flags':items})
 sections.append(f'<article><h2>{sid} · clip{number}</h2><p>{html.escape(seg["canonical"])}</p><audio controls preload="none" src="../../project/{seg["path"]}"></audio><p>Timing flags: {html.escape(", ".join(x["word_text"]+" ("+x["reason"]+")" for x in items))}</p></article>')
(D/'index.html').write_text('<!doctype html><html lang="en-US"><meta charset="utf-8"><title>M08 flagged audio audition</title><style>body{font:20px/1.5 sans-serif;max-width:1000px;margin:40px auto;background:#F0EBE4;color:#292421}article{padding:20px 0;border-bottom:1px solid #B8B0A9}audio{width:100%}</style><h1>M08 audio audition queue</h1><p>Known-text timing flags are review leads. They do not establish pronunciation errors or omissions. Compare the actual speech with the canonical sentence. Full-film human viewing/listening acceptance remains separate. All speech uses the approved voice and one narration-only1.5× pass.</p>'+''.join(sections))
(D/'manifest.json').write_text(json.dumps({'status':'prepared_for_human_listening','flagged_clips':len(rows),'alignment_flags':len(d['alignment_flags']),'rows':rows},indent=2))
print(json.dumps({'audition_clips':len(rows),'status':'prepared_not_human_listened'}))

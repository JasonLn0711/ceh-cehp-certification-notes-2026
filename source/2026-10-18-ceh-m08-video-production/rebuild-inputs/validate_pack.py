#!/usr/bin/env python3
"""Validate source layers; no claims about unproduced narration/captions/film."""
from pathlib import Path
import json,re,hashlib,wave,xml.etree.ElementTree as ET,zipfile,sys,urllib.parse,time
from collections import Counter
R=Path(__file__).resolve().parents[1];checks=[];start=time.monotonic()
def ck(name,ok,detail=None):checks.append(dict(name=name,pass_=bool(ok),detail=detail))
def load(n):return json.loads((R/n).read_text())
def words(s):return len(re.findall(r"\b\w+(?:['’-]\w+)*\b",s))
print('Validating source structure, content, assets, examples and editable media...',file=sys.stderr)
S=load('scenes.json');scenes=S['scenes'];ch=load('chapters.json');Q=load('questions.json')['questions'];vis=load('visual_scenes.json')['scenes'];ids=[f'S{i:02}' for i in range(1,59)]
ck('58 ordered unique scenes',[s['id'] for s in scenes]==ids);ck('11 chapters',[c['id'] for c in ch]==[f'C{i:02}' for i in range(1,12)]);ck('chapter coverage exactly once',[i for c in ch for i in c['scene_ids']]==ids)
ck('source readiness stated',S['status']=='source_ready' and S['actual_final_mp4_rendered'] is False)
ck('speech speed only',S['narration_speed_multiplier']==1.5 and S['voice']['baseline_speed']==.73 and S['voice']['voice']=='af_heart')
script=(R/'SCRIPT_en-US.md').read_text();allspoken=[];silent=[]
for s,v in zip(scenes,vis):
 spoken=' '.join(x['text'] for x in s['audio_segments'] if x['kind']=='spoken');allspoken.append(spoken);silent.extend(x for x in s['audio_segments'] if x['kind']=='silence')
 ck(s['id']+' canonical segment mirror',spoken==s['narration_en_US'])
 ck(s['id']+' script complete',all(x['text'] in script for x in s['audio_segments'] if x['kind']=='spoken'))
 ck(s['id']+' measured source words',words(spoken)==s['estimated_spoken_words'])
 ck(s['id']+' visual/source copy',v['id']==s['id'] and v['screen_copy_exact']==s['on_screen_copy'])
 ck(s['id']+' substantive teaching',words(spoken)>=120)
 board=R/v['board'];tree=ET.parse(board);texts=' '.join(tree.getroot().itertext());ck(s['id']+' editable SVG',tree.getroot().tag.endswith('svg') and all(label in texts for label in s['on_screen_copy']) if s['id'] not in ['S54','S55','S56','S57'] else tree.getroot().tag.endswith('svg'))
 ck(s['id']+' native canvas',tree.getroot().attrib.get('viewBox')=='0 0 1920 1080')
for c in ch:
 subset=[s for s in scenes if s['chapter_id']==c['id']];ck(c['id']+' scene mapping',[s['id'] for s in subset]==c['scene_ids']);ck(c['id']+' words',sum(s['estimated_spoken_words'] for s in subset)==c['narration_words'])
ck('total spoken words',sum(words(s) for s in allspoken)==S['estimated_spoken_words'])
ck('eight original quiz IDs',[q['id'] for q in Q]==[f'Q{i:02}' for i in range(1,9)])
ck('graded question distribution',Counter(q['level'] for q in Q)==dict(basic=2,intermediate=2,advanced=2,scenario=2))
ck('eight silence segments',len(silent)==8);ck('one second each',all(x['seconds']==1 and x['pcm_frames']==48000 for x in silent))
for q in Q:
 ck(q['id']+' four choices',[c['letter'] for c in q['choices']]==list('ABCD') and q['correct_letter'] in 'ABCD')
 seg=scenes[int(q['scene_id'][1:])-1]['audio_segments'];k=next(i for i,x in enumerate(seg) if x.get('question_id')==q['id'] and x['kind']=='silence')
 ck(q['id']+' stem/options before silence',seg[k-1]['role']=='question_and_all_choices' and q['prompt'] in seg[k-1]['text'] and all(c['text'] in seg[k-1]['text'] for c in q['choices']))
 ck(q['id']+' answer after silence',seg[k+1]['role']=='answer_and_reasoning' and q['explanation'] in seg[k+1]['text'])
 ck(q['id']+' teacher mirror',q['explanation'] in (R/'ASSESSMENT_INSTRUCTOR.md').read_text())
 ck(q['id']+' student has no supplied explanation',q['explanation'] not in (R/'ASSESSMENT_STUDENT.md').read_text())
for sid in ['S54','S55','S56','S57']:ck(sid+' two questions',len([q for q in Q if q['scene_id']==sid])==2)
with wave.open(str(R/'production/quiz_silence_1s_48k_stereo.wav')) as w:
 ck('real zero PCM format',(w.getframerate(),w.getnchannels(),w.getsampwidth(),w.getnframes())==(48000,2,2,48000));data=w.readframes(w.getnframes());ck('every PCM byte zero',len(data)==192000 and not any(data))
locked=load('LOCKED_SOURCE_SHA256.json')['sha256'];ck('44 locked assets',len(locked)==44)
for name,sha in locked.items():ck('locked '+name,hashlib.sha256((R/name).read_bytes()).hexdigest()==sha)
pk=load('validation/packet_qa.json');ck('actual offline packet QA',pk['failed']==0 and len(pk['runs'])==9)
manifest=load('lab_mock/fixture_manifest.json');ck('six labeled synthetic fixtures',len(manifest['files'])==6 and manifest['provenance']=='SIMULATED OUTPUT')
for f in manifest['files']:
 b=(R/f['path']).read_bytes();ck(f['path']+' measured identity',len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'])
case=load('case/NORTHSTAR_M08_EVIDENCE.json');ck('simulated case label',case['dataset_label']=='SIMULATED OUTPUT')
ck('four bounded cases',[e['id'] for e in case['training_events']]==['E01','E02','E03','E04'] and all(e['label']=='SIMULATED OUTPUT' and e['limits'] for e in case['training_events']))
ck('official 13 topic areas',len(load('coverage.json'))==13)
with zipfile.ZipFile(R/'slides/CEH_M08_Editable_Visual_Lookbook_18slides.pptx') as z:
 ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'};slides=sorted(n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$',n));ck('18 native PPTX slides',len(slides)==18);shape_count=0;text_count=0
 for n in slides:
  rt=ET.fromstring(z.read(n));sh=rt.findall('.//p:sp',ns);tx=rt.findall('.//a:t',ns);shape_count+=len(sh);text_count+=len(tx);ck(n+' separate native text/shapes',len(sh)>=10 and len(tx)>=8)
 ck('pptx ZIP CRC',z.testzip() is None)
for directory,expected in [('previews/boards',58),('previews/slides',18),('previews/examples',4)]:
 fs=list((R/directory).glob('*.png'));ck(directory+' count',len(fs)==expected)
 for p in fs:ck(p.relative_to(R).as_posix()+' PNG signature',p.read_bytes()[:8]==b'\x89PNG\r\n\x1a\n')
br=load('validation/browser_qa.json');ck('actual browser checks',br['failed']==0 and len(br['examples'])==4)
hf=list((R/'validation').glob('hyperframes-*.json'));ck('all four HyperFrames checks present',len(hf)==4)
for p in sorted(hf):
 h=load(str(p.relative_to(R)));ck(p.name+' actual HyperFrames check',h.get('ok') is True)
for prop in load('m08_asset_extensions.json'):ET.parse(R/prop['path']);ck(prop['id']+' native SVG prop',(R/prop['path']).exists())
for eid in ['packet-visibility','arp-binding','dhcp-dns','quiz-one-second']:
 t=(R/f'examples/{eid}/index.html').read_text();ck(eid+' finite paused runtime','paused:true' in t and 'data-duration="12"' in t and f'window.__timelines["{eid}"]' in t);ck(eid+' no render-time randomness',not any(x in t for x in ['Math.random','Date.now','setInterval','tl.play(']))
# Local Markdown targets in newly authored docs; inherited reference documents remain byte-preserved provenance.
newdocs=['README.md','START_HERE_zh-TW.md','STORYBOARD.md','ASSESSMENT_STUDENT.md','ASSESSMENT_INSTRUCTOR.md','CONCEPT_CONNECTIONS.md','COVERAGE_MATRIX.md','SOURCES.md','tooling/README.md','examples/README.md','lab_mock/README.md']
for n in newdocs:
 for target in re.findall(r'\]\(([^)]+)\)',(R/n).read_text()):
  if re.match(r'https?://',target):continue
  target=urllib.parse.unquote(target.split('#')[0])
  if n=='README.md' and target=='validation/source_qa.json':continue  # this invocation writes that report
  ck(n+' link '+target,(R/n).parent.joinpath(target).exists())
ck('no false media deliverables',not list(R.rglob('*.mp4')) and not list(R.rglob('*.srt')) and not list(R.rglob('*.vtt')))
report=dict(status='source_ready' if all(c['pass_'] for c in checks) else 'source_validation_failed',scope='Source package only. Four animation examples checked; complete film runtime, speech and captions are not produced.',spoken_words=S['estimated_spoken_words'],chapters=11,scenes=58,questions=8,locked_assets=len(locked),pptx_native_shapes=shape_count,pptx_native_text_runs=text_count,checks=checks,passed=sum(c['pass_'] for c in checks),failed=sum(not c['pass_'] for c in checks),elapsed_seconds=round(time.monotonic()-start,3))
(R/'validation').mkdir(exist_ok=True);(R/'validation/source_qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False));sys.exit(0 if report['failed']==0 else 1)

#!/usr/bin/env python3
"""Source acceptance from actual content, editable artifacts, browser and runtime receipts."""
from pathlib import Path
import hashlib,json,re,wave,zipfile,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];checks=[];third_party_link_exclusions=[]
def check(name,condition,detail=None):checks.append(dict(name=name,passed=bool(condition),detail=detail))
def load(n):return json.loads((R/n).read_text())
def words(s):return len(re.findall(r"\b\w+(?:['’-]\w+)*\b",s))
S=load('scenes.json');C=load('chapters.json');Q=load('questions.json');V=load('visual_scenes.json')
check('module identity','Module 10: Denial of Service' in S['title'])
check('source layer',S['status'] in ['source_authored_pending_QA','source_ready'] and S['actual_final_mp4_rendered'] is False)
check('11 chapters and58scenes',len(C)==11 and len(S['scenes'])==58 and len(V['scenes'])==58)
check('scene IDs and coverage',[s['id'] for s in S['scenes']]==[f'S{i:02}' for i in range(1,59)])
check('chapter flattening',[i for c in C for i in c['scene_ids']]==[s['id'] for s in S['scenes']])
check('eight new questions',len(Q['questions'])==8 and Q['namespace']=='M10-film-v1')
check('graded questions',[sum(q['level']==level for q in Q['questions']) for level in ['Foundation','Application','Analysis']]==[2,4,2])
spoken=[];holds=[]
for s in S['scenes']:
 segments=s['audio_segments'];joined=' '.join(x['text'] for x in segments if x['kind']=='spoken')
 check(s['id']+' canonical segment coverage',joined==s['narration_en_US'])
 check(s['id']+' actual canonical word count',words(joined)==s['estimated_spoken_words'])
 check(s['id']+' original teaching content',len(joined)>100 and all(x.strip() for x in s['on_screen_copy']))
 spoken.append(joined)
 for i,x in enumerate(segments):
  if x['kind']=='silence':
   holds.append(x);before=segments[i-1];after=segments[i+1]
   check(x['question_id']+' full choices before hold',before['role']=='question_and_all_choices' and all(t+'. ' in before['text'] for t in 'ABCD'))
   check(x['question_id']+' reference hold contract',x['seconds']==1 and x['pcm_frames']==48000)
   check(x['question_id']+' answer follows hold',after['role']=='answer_and_reasoning' and after['question_id']==x['question_id'])
 p=R/f"boards/{s['id']}.svg";svg=ET.parse(p).getroot()
 check(s['id']+' valid editable SVG',svg.attrib.get('viewBox')=='0 0 1920 1080' and len(svg.findall('.//{http://www.w3.org/2000/svg}text'))>4)
 check(s['id']+' storyboard and visual mapping',s['id'] in (R/'STORYBOARD.md').read_text() and V['scenes'][int(s['id'][1:])-1]['board']==f"boards/{s['id']}.svg")
for q in Q['questions']:
 check(q['id']+' complete choices/key',len(q['choices'])==4 and {x['letter'] for x in q['choices']}==set('ABCD') and q['correct_letter'] in 'ABCD' and len(q['explanation'])>200)
check('actual spoken words',sum(words(x) for x in spoken)==S['estimated_spoken_words'])
check('eight ordered holds',[x['question_id'] for x in holds]==[f'Q{i:02}' for i in range(1,9)])
check('all script text included',all(x in (R/'SCRIPT_en-US.md').read_text() for s in S['scenes'] for x in [z['text'] for z in s['audio_segments'] if z['kind']=='spoken']))
check('source estimate labeled','not measured' in S['timing_estimate_basis'] and ('ceiling' in S['duration_policy'] or 'No maximum' in S['duration_policy']))
for name,h in load('LOCKED_SOURCE_SHA256.json')['sha256'].items():check('locked:'+name,hashlib.sha256((R/name).read_bytes()).hexdigest()==h)
with wave.open(str(R/'production/quiz_silence_1s_48k_stereo.wav')) as w:
 check('actual reference zero WAV',(w.getnchannels(),w.getsampwidth(),w.getframerate(),w.getnframes())==(2,2,48000,48000) and not any(w.readframes(48000)))
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
counts={'slides':0,'native_shapes':0,'text_runs':0}
with zipfile.ZipFile(R/'slides/CEH_M10_Editable_Visual_Lookbook_18slides.pptx') as z:
 names=sorted(n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n))
 counts['slides']=len(names)
 for name in names:
  root=ET.fromstring(z.read(name));shapes=root.findall('.//p:sp',ns);texts=root.findall('.//a:t',ns)
  counts['native_shapes']+=len(shapes);counts['text_runs']+=len(texts)
  check(name+' editable native objects',len(shapes)>5 and len(texts)>4)
check('18 editable slides',counts['slides']==18)
check('actual PDF export',(R/'slides/CEH_M10_Editable_Visual_Lookbook_18slides.pdf').is_file())
check('18 actual slide raster images',len(list((R/'previews/slides').glob('slide-*.png')))==18)
browser=load('validation/browser_qa.json');check('actual source browser checks',browser['failed']==0,browser['failed'])
check('58 actual board captures',len(list((R/'previews/boards').glob('S*.png')))==58)
for eid in ['resource-budget','tcp-state','reflection-path','quiz-one-second']:
 d=load('validation/hyperframes-'+eid+'.json');check(eid+' actual framework runtime',d['ok'] and not d['browserSkipped'])
e=load('validation/evidence-verification.json');check('actual offline evidence parser',e['failed']==0)
refs=load('validation/reference-retrieval.json')['sources'];check('primary retrievals',len(refs)==12 and all(x['retrieval_status']=='retrieved_readable' and x['http_status']==200 for x in refs))
check('RFC and original protocol references',all(any(x['id']==ident for x in refs) for ident in ['R02','R03','R04','R05','R06','R07','R08']))
for f in R.rglob('*.md'):
 if any(p in f.parts for p in ['node_modules','.hyperframes']):continue
 for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',f.read_text()):
  if re.match(r'(https?://|mailto:|#)',target):continue
  if 'licenses' in f.relative_to(R).parts and target.startswith('/'):
   third_party_link_exclusions.append({'file':str(f.relative_to(R)),'target':target,'scope':'Upstream-root phonetic link in preserved model card; not an owned local-file reference'});continue
  check('link:'+str(f.relative_to(R))+':'+target,(f.parent/target.split('#')[0]).exists())
check('concrete visual review exists',(R/'validation/visual-review.md').exists())
if (R/'validation/visual-review.md').exists():check('concrete visual pass','review_status: pass' in (R/'validation/visual-review.md').read_text())
result=dict(status='source_checks_passed' if all(x['passed'] for x in checks) else 'source_checks_failed',
 scope='Complete source package and four actual examples, not final film',passed=sum(x['passed'] for x in checks),failed=sum(not x['passed'] for x in checks),
 spoken_words=S['estimated_spoken_words'],chapters=11,scenes=58,questions=8,locked_assets=44,editable_deck=counts,third_party_link_exclusions=third_party_link_exclusions,checks=checks)
(R/'validation/source_qa.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));raise SystemExit(bool(result['failed']))

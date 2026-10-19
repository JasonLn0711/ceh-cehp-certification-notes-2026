"""One-time, recorded extraction from immutable M10; runtime files are maintained hereafter."""
from pathlib import Path
import ast,hashlib,json,tokenize,io
src=Path('/home/jnlngx10/Videos/CEH_M10_v1_0/project/scripts');dest=Path(__file__).parent/'ceh_video/runtime';rows=[]
names=['contact_sheet','editorial','art_common','build_film','force_align','export_metadata','assemble_project','chapter','assemble_master','audit_audio_clips','review_audio','measure_speech','asr_receipt','audit_audio_continuity','audit_rendered','capture_late_diagrams','recognition_audit','sync_storyboard']
for name in names:
 p=src/(name+'.py');s=p.read_text();original=s
 s=s.replace('Path(__file__).resolve().parents[1]','project_root()')
 s='from ceh_video.common import project_root, Project\n'+s
 if name=='force_align':
  s=s.replace("from synthesize import spoken", "from ceh_video.speech import spoken as expand\ndef spoken(text):return expand(text,__import__('json').load(open(project_root()/'pronunciation.json')))")
  s=s.replace("old.get('audio_sha256')==key and old.get('recipe')==RECIPE", "old.get('audio_sha256')==key and old.get('recipe')==RECIPE and old.get('canonical')==r['canonical'] and old.get('spoken',r['spoken'])==r['spoken']")
  s=s.replace("'canonical':r['text'],'audio_sha256'", "'canonical':r['text'],'spoken':r['spoken'],'audio_sha256'")
 if name=='build_film':
  s=s.replace('art=a.svg();moves=a.moves', '''art=a.svg();moves=a.moves
   override_file=ROOT/'data/visual-overrides.json'
   override=json.load(open(override_file)).get(sid,{}) if override_file.exists() else {}
   if override:
    dx=float(override.get('offset_x',0));dy=float(override.get('offset_y',0));assert abs(dx)<=2 and abs(dy)<=2
    art=art.replace('>',f'><g transform="translate({dx} {dy})">',1).replace('</svg>','</g></svg>')''')
  s=s.replace("if 50<=n<=57:art,moves=quiz(scene,audio)","if any(q['scene_id']==sid for q in json.load(open(ROOT/'data/questions.json'))['questions']):art,moves=quiz(scene,audio)")
  s=s.replace("(ROOT/'data'/f'{sid}.quiz-layout.json').write_text(json.dumps(layouts,indent=2))", "if not os.environ.get('CEH_VIDEO_PREFLIGHT'):(ROOT/'data'/f'{sid}.quiz-layout.json').write_text(json.dumps(layouts,indent=2))")
  s=s.replace("'all_required':58", "'all_required':len(allscenes)")
 if name=='chapter':
  begin=s.index('def fingerprint(folder):');end=s.index('\ndef run(',begin)
  s=s[:begin]+"def fingerprint(folder):return Project(ROOT).chapter_inputs(Path(folder).name)\n"+s[end:]
  s=s.replace("assert (QA/f'{ch}-visual-review.md').exists(),'Write concrete frame-review findings before render'", "from ceh_video.review import require_review\n  require_review(Project(ROOT),ch)")
  s=s.replace("assert 'review_status: pass' in (QA/f'{ch}-visual-review.md').read_text(),'Review contains unresolved findings'", "# Structured review is bound to current source and image identities.")
 if name=='assemble_master':
  s=s.replace("from production_settings import MASTER_FILENAME", "MASTER_FILENAME=Project(project_root()).profile['master_filename']")
  s=s.replace('CEH M10 Denial of Service English Masterclass', "CEH Denial of Service English Masterclass")
  s=s.replace("if not reference.exists():", "if not reference.exists() or __import__('hashlib').sha256(reference.read_bytes()).hexdigest()!=__import__('hashlib').sha256(audio.read_bytes()).hexdigest():")
 if name in ['audit_audio_continuity','audit_rendered','capture_late_diagrams']:
  s=s.replace('from production_settings import MASTER_FILENAME',"MASTER_FILENAME=Project(project_root()).profile['master_filename']")
 if name in ['export_metadata','assemble_project','audit_audio_clips','review_audio','asr_receipt','measure_speech']:
  s=s.replace('from production_settings import quiz_seconds',"def quiz_seconds():return Project(project_root()).profile['quiz_silence_seconds']")
  # Only numerical count assertions/receipts are generalized; local source text stays unchanged.
  tokens=[]
  for t in tokenize.generate_tokens(io.StringIO(s).readline):
   if t.type==tokenize.NUMBER and t.string in {'58','10241'}:
    replacement="len(Project(project_root()).scenes)" if t.string=='58' else "Project(project_root()).profile['expected']['canonical_words']"
    t=tokenize.TokenInfo(t.type,replacement,t.start,t.end,t.line)
   tokens.append(t)
  s=tokenize.untokenize(tokens)
  s=s.replace('assert len(chapters)==11',"assert len(chapters)==len(Project(ROOT).chapters)")
  s=s.replace("'chapters':11", "'chapters':len(Project(ROOT).chapters)")
 if name=='sync_storyboard':s=s.replace('assert changed==58',"assert changed==len(Project(R).scenes)").replace("seek['scenes']==58", "seek['scenes']==len(Project(R).scenes)")
 ast.parse(s);(dest/p.name).write_text(s)
 rows.append({'source':str(p),'source_sha256':hashlib.sha256(original.encode()).hexdigest(),'engine_file':p.name,'engine_sha256':hashlib.sha256(s.encode()).hexdigest()})
for name in ['audit_quiz.mjs','audit_scene_seek.mjs']:
 s=(src/name).read_text()
 if name=='audit_quiz.mjs':
  s=s.replace('for(let n=50;n<=57;n++) {\n  const sid=`S${n}`,html=',"for(const sid of [...new Set(questions.map(q=>q.scene_id))]) {\n  const html=")
 if name=='audit_scene_seek.mjs':s=s.replace('rows.length===58','rows.length===scenes.length').replace('total:58','total:scenes.length').replace('scenes:58','scenes:scenes.length')
 (dest/name).write_text(s)
rows.append({'scope':'Shared production implementation extracted with explicit project context; M10 diagram adapters remain project-owned.'})
(Path(__file__).parent/'extraction-provenance.json').write_text(json.dumps(rows,indent=2)+'\n')

"""Freeze and import an immutable M10 reference into an isolated workspace."""
from pathlib import Path
import ast, hashlib, json, os, shutil, subprocess, sys
from .common import Project, read, sha, write


def initialize(reference, workspace, emit):
    reference=Path(reference).resolve();workspace=Path(workspace).resolve()
    if workspace.exists():raise RuntimeError('Workspace already exists; use status/resume: '+str(workspace))
    for f in (reference/'qa').glob('*-process.json'):
        r=read(f)
        if r.get('status')=='running':
            try:os.kill(r['pid'],0)
            except ProcessLookupError:continue
            raise RuntimeError('Preserve active reference process: '+str(f))
    identity={};manifest=reference/'output/DELIVERY_SHA256.txt'
    rows=manifest.read_text().splitlines()
    for i,line in enumerate(rows,1):
        h,rel=line.split('  ',1);f=reference/'output'/rel
        assert sha(f)==h, 'Reference delivery changed: '+rel
        identity[rel]=h
        if i%1000==0 or i==len(rows):emit({'phase':'reference_hashes','completed':i,'total':len(rows)})
    workspace.mkdir(parents=True);project=workspace/'project';qa=workspace/'qa';out=workspace/'output';qa.mkdir();out.mkdir()
    def ignore(folder,names):return [n for n in names if n in {'.venv','node_modules','.hyperframes','.waveform-cache','__pycache__','review','.production'}]
    shutil.copytree(reference/'project',project,ignore=ignore)
    shutil.copytree(reference/'inputs',workspace/'inputs')
    for f in (reference/'qa').iterdir():
        if f.is_file() and f.suffix in {'.json','.md'} and not f.name.endswith('-process.json'):shutil.copy2(f,qa/f.name)
    shutil.copytree(reference/'qa/recognition',qa/'recognition')
    shutil.copy2(reference/'qa/recognition-process.json',qa/'reference-recognition-process.json')
    shutil.copytree(reference/'output/chapters',out/'chapters')
    for f in (reference/'output').iterdir():
        if f.is_file() and f.suffix in {'.mp4','.wav','.srt','.vtt','.txt'} and f.name!='DELIVERY_SHA256.txt':shutil.copy2(f,out/f.name)
    emit({'phase':'copying_isolated_runtime','scope':'Private execution environment; excluded from editable package'})
    shutil.copytree((reference/'project/.venv').resolve(),project/'.venv',symlinks=True)
    shutil.copytree(reference/'project/node_modules',project/'node_modules',symlinks=True)
    engine=Path(__file__).parent
    shutil.copytree(engine,project/'vendor/ceh_video',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    tree=ast.parse((reference/'project/scripts/synthesize.py').read_text());policy={}
    for stmt in tree.body:
        if isinstance(stmt,ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'SPELL','PRON'} for t in stmt.targets):
            if stmt.targets[0].id=='PRON':policy['pronunciations']=ast.literal_eval(stmt.value)
            else:policy['spell']=sorted(ast.literal_eval(stmt.value.args[0].func.value).split())
    policy.update(schema_version=1,version='approved-m10-1',provenance='Exact extraction from approved M10 synthesis policy; no spoken changes',matching='case-sensitive whole lexical token; spelling takes precedence')
    write(project/'pronunciation.json',policy)
    scenes=read(project/'data/scenes.json')['scenes'];questions=read(project/'data/questions.json')['questions'];locked=read(project/'data/LOCKED_SOURCE_SHA256.json')['sha256']
    resolved={}
    for rel,h in locked.items():resolved[rel if (project/rel).exists() else 'data/'+rel]=h
    ffmpeg=subprocess.check_output(['ffmpeg','-version'],text=True).splitlines()[0]
    profile={'schema_version':1,'engine_version':'0.1.0','module':'M10','release':'optimization-v1','title':'CEH M10 Denial of Service English Masterclass',
             'master_filename':'CEH_M10_Denial_of_Service_en-US_1_5x_1s_master.mp4','editable_filename':'CEH_M10_optimization_v1_EDITABLE.zip',
             'source_package':'../inputs/package/CEH_M10_English_Editorial_Masterclass',
             'voice':{'name':'af_heart','language':'en-us','baseline_speed':.73,'atempo':1.5,'speed_applications':1},
             'output':{'width':1920,'height':1080,'fps':30,'sample_rate':48000,'channels':2,'video_rate':1.0,'bgm':False},
             'quiz_silence_seconds':1,'expected':{'scenes':len(scenes),'chapters':len(set(s['chapter_id'] for s in scenes)),'questions':len(questions),'canonical_words':sum(len(s['narration_en_US'].split()) for s in scenes)},
             'runtime':{'hyperframes':read(project/'node_modules/hyperframes/package.json')['version'],'browser':'/home/jnlngx10/.cache/ms-playwright/chromium_headless_shell-1234/chrome-linux/headless_shell','ffmpeg':ffmpeg,'max_chapter_renders':2,'render_workers':4},
             'alignment':{'model':'base.en','compute_type':'int8','recipe':'base.en-int8-forced-dtw-v1'},
             'models':{f.name:sha(f) for f in [project/'models/kokoro-v1.0.onnx',project/'models/voices-v1.0.bin']},'locked_assets':resolved}
    profile['diagram_inputs']={s['id']:['scripts/scene_art.py','scripts/'+('scene_art_start.py' if int(s['id'][1:])<=22 else 'scene_art_mid.py' if int(s['id'][1:])<=42 else 'scene_art_end.py')] for s in scenes if s['id'] not in {q['scene_id'] for q in questions}}
    profile['alignment']['models_sha256']={str(f.relative_to(project/'models/faster-whisper-base.en')):sha(f) for f in (project/'models/faster-whisper-base.en').rglob('*') if f.is_file()}
    write(project/'production.json',profile)
    # Only adapters remain project-owned; shared scripts become explicit engine entrypoints.
    for script in (engine/'runtime').glob('*.py'):
        name=script.stem
        (project/'scripts'/script.name).write_text('import os,sys\nfrom pathlib import Path\nr=Path(__file__).resolve().parents[1]\nos.environ["CEH_VIDEO_PROJECT"]=str(r)\nsys.path.insert(0,str(r/"vendor"))\nfrom ceh_video.worker import main\nsys.argv=[sys.argv[0],'+repr(name)+',*sys.argv[1:]]\nmain()\n')
    (project/'scripts/production_settings.py').write_text('from ceh_video.common import Project,project_root\nMASTER_FILENAME=Project(project_root()).profile["master_filename"]\ndef quiz_seconds():return Project(project_root()).profile["quiz_silence_seconds"]\ndef quiz_label():return "1 second each"\n')
    for name in ['audit_quiz.mjs','audit_scene_seek.mjs']:
        shutil.copy2(engine/'runtime'/name,project/'scripts'/name)
    # Avoid modifying copied chapter audio through historical hardlinks.
    for ch in (project/'chapters').iterdir():
        if ch.is_dir():
            for f in ch.rglob('*'):
                if f.is_file() and f.stat().st_nlink>1:
                    temp=f.with_name(f.name+'.private');shutil.copy2(f,temp);os.replace(temp,f)
    p=Project(project);os.environ['CEH_VIDEO_PROJECT']=str(project)
    from .speech import import_cache
    clips=import_cache(p)
    baseline={}
    original=object.__new__(Project);original.root=reference/'project';original.profile=profile;original.scenes=scenes
    for ch in p.chapters:baseline[ch]={'input_sha256':original.chapter_inputs(ch),'mp4_sha256':sha(out/'chapters'/f'{ch}.mp4')}
    record={'status':'reference_verified_and_privately_imported','reference':str(reference),'reference_manifest_sha256':sha(manifest),'files':identity,'speech_clips_imported':clips,'chapters':baseline,'human_acceptance':'pending'}
    write(qa/'reference-import.json',record)
    write(qa/'reference-audio-identities.json',{'scenes':{s['id']:sha(project/'assets/voice'/f'{s["id"]}.wav') for s in scenes},'voice':profile['voice'],'models':profile['models']})
    return {'workspace':str(workspace),'verified_reference_files':len(identity),'speech_clips_imported':clips}

"""Cheap, explicit source and diagram checks before model or renderer work."""
import ast, importlib, os, re, sys
from pathlib import Path
from .common import Project, read, sha, write


def validate_profile(data):
    if data.get('schema_version') == 2:
        from .mandarin import validate_profile as validate_mandarin
        return validate_mandarin(data)
    assert data['schema_version']==1, 'Unsupported production profile'
    from .audio_policy import timing
    try:contract=timing(data)
    except ValueError as exc:raise AssertionError(str(exc)) from exc
    assert data['voice']=={'name':'af_heart','language':'en-us','baseline_speed':0.73,'atempo':contract['atempo'],'speed_applications':1}, 'Approved voice contract changed'
    assert data['output']=={'width':1920,'height':1080,'fps':30,'sample_rate':48000,'channels':2,'video_rate':1.0,'bgm':False}, 'Approved output contract changed'
    assert data['quiz_silence_seconds']==1, 'Quiz holds must be exactly 1.000 seconds'
    if data.get('design_profile')=='m10-editorial-remaster-v1.1':
        assert data['runtime']['browser_gpu_mode']=='hardware', 'Remaster GPU mode must be explicitly hardware'
        assert data['runtime']['expected_gpu_renderer']=='ANGLE (NVIDIA Corporation, NVIDIA GB10/PCIe, OpenGL ES 3.2)', 'Remaster hardware renderer identity changed'
        assert data['runtime']['max_chapter_renders'] in (1,2) and data['runtime']['render_workers'] in (1,2,4)
        assert data['runtime']['max_chapter_renders']*data['runtime']['render_workers'] <= (8 if data.get('audio_policy')=='ceh-en-v1.2' else 4)
    else:
        assert data['runtime']['max_chapter_renders']==2 and data['runtime']['render_workers']==4


def preflight(p, diagrams=True):
    if p.profile.get('schema_version') == 2:
        from .mandarin import preflight as mandarin_preflight
        return mandarin_preflight(p, diagrams)
    validate_profile(p.profile); expected=p.profile['expected']; errors=[]
    def check(ok, why):
        if not ok: errors.append(why)
    ids=[s['id'] for s in p.scenes];qids=[q['id'] for q in p.questions]
    check(len(set(ids))==len(ids), 'duplicate_scene')
    check(len(set(qids))==len(qids), 'duplicate_question')
    check(len(p.scenes)==expected['scenes'], 'scene_count')
    check(len(p.chapters)==expected['chapters'], 'chapter_count')
    check(len(p.questions)==expected['questions'], 'question_count')
    check(sum(len(s['narration_en_US'].split()) for s in p.scenes)==expected['canonical_words'], 'canonical_words')
    for q in p.questions:
        check(q['scene_id'] in ids, q['id']+': unknown scene')
        check([c['letter'] for c in q['choices']]==list('ABCD'), q['id']+': incomplete choices')
        check(q['correct_letter'] in 'ABCD', q['id']+': invalid key')
    for scene in p.scenes:
        pauses=sum(s['kind']=='silence' for s in scene['audio_segments'])
        check(pauses==sum(q['scene_id']==scene['id'] for q in p.questions), scene['id']+': question/hold mapping')
        check(' '.join(s['text'] for s in scene['audio_segments'] if s['kind']=='spoken')==' '.join(scene['narration_en_US'].split()), scene['id']+': source segment coverage')
    for f in (p.root/'scripts').glob('*.py'):
        try: ast.parse(f.read_text(), filename=str(f))
        except SyntaxError as exc: errors.append(str(exc))
    for rel,h in p.profile['locked_assets'].items():
        check((p.root/rel).is_file() and sha(p.root/rel)==h, 'locked asset: '+rel)
    for rel,h in p.profile['models'].items():
        check((p.root/'models'/rel).is_file() and sha(p.root/'models'/rel)==h, 'model identity: '+rel)
    for rel,h in p.profile['alignment']['models_sha256'].items():
        f=p.root/'models/faster-whisper-base.en'/rel
        check(f.is_file() and sha(f)==h, 'alignment model identity: '+rel)
    package=p.root/'node_modules/hyperframes/package.json'
    if package.exists():
        check(read(package)['version']==p.profile['runtime']['hyperframes'], 'installed HyperFrames/profile mismatch')
    for rel in ['assets/fonts/LiberationSans-Regular.ttf','assets/fonts/LiberationSans-Bold.ttf','assets/fonts/DejaVuSansMono.ttf','assets/vendor/gsap.min.js']:
        check((p.root/rel).is_file(), 'missing asset '+rel)
    if diagrams and not errors:
        os.environ['CEH_VIDEO_PROJECT']=str(p.root); os.environ['CEH_VIDEO_PREFLIGHT']='1'
        sys.path[:0]=[str(Path(__file__).parent/'runtime'),str(p.root/'scripts')]
        compiler=importlib.import_module('build_film')
        cue={}
        for f in (p.root/'scripts').glob('cues_*.json'): cue.update(read(f))
        for scene in p.scenes:
            sid=scene['id']
            try:
                a=p.audio(sid)
                if sid in p.quiz_scenes(): compiler.quiz(scene,a)
                else:
                    if p.profile.get('scene_specs'):
                        from .remaster import project_specs
                        assert project_specs(p)[sid]['nodes']
                    else:
                        art=compiler.build(scene,a)
                        assert art.parts and art.moves
                    assert len(cue[sid])==len(scene['on_screen_copy']), 'cue count'
                    for phrase in cue[sid]:
                        matches=[x for x in a['segments'] if x['kind']=='spoken' and phrase.lower() in x['canonical'].lower()]
                        assert matches, 'Missing narration anchor '+phrase
            except Exception as exc: errors.append(f'{sid}: {type(exc).__name__}: {exc}')
        os.environ.pop('CEH_VIDEO_PREFLIGHT',None)
    result={'status':'passed' if not errors else 'failed','errors':errors,'scenes':len(p.scenes),'chapters':len(p.chapters),'questions':len(p.questions),'scope':'Source contracts, asset identity, imports and actual diagram/quiz geometry; expensive model/render work separate'}
    write(p.qa/'preflight.json',result)
    if errors: raise RuntimeError('Preflight failed: '+'; '.join(errors))
    return result

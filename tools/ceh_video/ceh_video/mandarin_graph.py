"""Locale-v2 graph; M10/v1 receipts and execution remain unchanged."""
from pathlib import Path
from .common import read,sha
from .graph import Node
from .mandarin_policy import timing, deck_filename, archive_prefix

def nodes(p):
    result={};base=Path(__file__).parent
    def add(name,deps,inputs,outputs,modules):
        result[name]=Node(name,deps,{'recipe':inputs,'implementation':{n:sha(base/n) for n in modules}},[str(f) for f in outputs],[])
    from .mandarin_speech import spoken
    policy=read(p.root/'pronunciation.json')
    for s in p.scenes:
        sid=s['id'];spoken_segments=[x['text'] for x in s['audio_segments'] if x['kind']=='spoken']
        add('speech:'+sid,[],{'segments':s['audio_segments'],'spoken':[spoken(t,policy) for t in spoken_segments],'voice':p.profile['voice'],'ffmpeg':p.profile['runtime']['ffmpeg'],'timing':timing(p.profile),'chapter_last':p.chapter_scenes(s['chapter_id'])[-1]['id']==sid},[p.root/'data'/f'{sid}.audio.json',p.root/'assets/voice'/f'{sid}.wav'],['mandarin_speech.py','mandarin_policy.py'])
        align=[p.root/'data/forced-alignment'/f'{sid}-{i:03}.json' for i in range(len(spoken_segments))]
        add('align:'+sid,['speech:'+sid],p.profile['alignment'],align,['mandarin_speech.py','mandarin_policy.py'])
        visual={k:v for k,v in s.items() if k not in ['audio_segments','narration_zh_TW','paragraphs']}
        add('scene:'+sid,['align:'+sid],{'scene':visual,'questions':[q for q in p.questions if q['scene_id']==sid],'fonts':p.profile['fonts'],'assets':p.profile['locked_assets']},[p.root/'compositions'/f'{sid}.html',p.root/'compositions'/f'{sid}.motion.json',p.root/'data'/f'{sid}.captions.json',p.root/'data'/f'{sid}.geometry.json',p.root/'boards/svg'/f'{sid}.svg'],['mandarin_build.py','mandarin_art.py']+(['island_art.py'] if p.profile.get('art_profile')=='island-workshop-v1' else []))
    if p.profile.get('teaching_panels'):
        from .mandarin_panels import specification,assets
        inventory=assets(p)
        for scene in p.scenes:
            sid=scene['id'];spec=specification(p,sid)
            n=result['scene:'+sid];n.inputs['recipe']['panels']=spec
            n.inputs['recipe']['panel_assets']={r['asset']:sha(p.root/inventory[r['asset']]['file']) for r in spec}
            n.inputs['implementation']['mandarin_panels.py']=sha(base/'mandarin_panels.py')
            if spec:n.outputs.append(str(p.root/'data'/f'{sid}.panels.json'))
    for ch in p.chapters:
        add('prepare:'+ch,['scene:'+s['id'] for s in p.chapter_scenes(ch)],p.profile['runtime'],[p.qa/f'{ch}-check.json',p.qa/f'{ch}-checked-fingerprint.json',p.qa/f'{ch}-states/manifest.json',p.qa/f'{ch}-timing.json'],['mandarin.py','mandarin_build.py','pcm_reuse.py','capture.mjs'])
        add('render:'+ch,['prepare:'+ch],{'output':p.profile['output'],'renderer':p.profile['runtime']},[p.output/'chapters'/f'{ch}.mp4',p.qa/f'{ch}-render.json'],['mandarin.py','render_reuse.py'])
    add('root',['prepare:'+ch for ch in p.chapters],p.profile['output'],[p.root/'index.html',p.root/'data/master-timing.json',p.root/'data/master-captions.json',p.output/'captions.zh-TW.srt',p.output/'captions.zh-TW.vtt',p.qa/'master-project-check.json',p.qa/'quiz-runtime/checks.json',p.qa/'scene-seek-audit.json'],['mandarin.py','mandarin_build.py','mandarin_audit.mjs'])
    add('audio-review',['align:'+s['id'] for s in p.scenes],{},[p.qa/'audio-audition/manifest.json',p.qa/'audio-clip-structure-audit.json'],['mandarin_delivery.py','mandarin_policy.py'])
    add('master',['render:'+ch for ch in p.chapters]+['root'],{'title':p.profile['title']},[p.output/p.profile['master_filename'],p.output/'master.reference.pcm.wav',p.qa/'master-ffprobe.json'],['mandarin.py','runtime/assemble_master.py','master_reuse.py','pcm_reuse.py','media_scan.py'])
    result['master'].outputs += [str(p.qa/name) for name in ('master-full-decode.json','master-full-decode.log','master-full-decode.progress','master-stage-timing.json','master-audio-cache.json')]
    add('checks',['master','audio-review'],{'timing':timing(p.profile),'max_duration_seconds':p.profile.get('max_duration_seconds')},[p.qa/'rendered-artifact-audit.json',p.qa/'audio-continuity-audit.json',p.qa/'late-diagram-samples.json'],['mandarin_delivery.py','mandarin_policy.py','qa_inputs.py','media_scan.py'])
    add('delivery',['checks'],{'deck_filename':deck_filename(p.profile),'expected':p.profile['expected']},[p.qa/'engine-delivery.json',p.output/'engine-render-report.md',p.output/deck_filename(p.profile)],['mandarin_delivery.py','mandarin_build.py','mandarin_policy.py'])
    if p.profile.get('teaching_panels'):
        result['delivery'].inputs['implementation']['mandarin_panels.py']=sha(base/'mandarin_panels.py')
        result['delivery'].inputs['recipe']['teaching_assets']=read(p.root/'data/teaching-assets.json')
        result['delivery'].inputs['recipe']['deck_image_hashes']={r['id']:sha(p.root/r.get('deck_file',r['file'])) for r in read(p.root/'data/teaching-assets.json')}
    from .mandarin_package import source_inputs
    add('package',['delivery'],{'sources':source_inputs(p),'archive_prefix':archive_prefix(p.profile)},[p.output/p.profile['editable_filename'],p.qa/'engine-packaging.json'],['mandarin_delivery.py','mandarin_package.py','mandarin_policy.py'])
    from .packaging import walk_files
    result['package'].inputs['recipe']['bundled_engine'] = {
        rel:sha(f) for rel,f in walk_files(base,'ceh_video')}
    result['package'].inputs['recipe']['engine_metadata'] = sha(base.parent/'pyproject.toml')
    return result

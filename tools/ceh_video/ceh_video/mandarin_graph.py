"""Locale-v2 graph; M10/v1 receipts and execution remain unchanged."""
from pathlib import Path
from .common import read,sha
from .graph import Node

def nodes(p):
    result={};base=Path(__file__).parent
    def add(name,deps,inputs,outputs,modules):
        result[name]=Node(name,deps,{'recipe':inputs,'implementation':{n:sha(base/n) for n in modules}},[str(f) for f in outputs],[])
    from .mandarin_speech import spoken
    policy=read(p.root/'pronunciation.json')
    for s in p.scenes:
        sid=s['id'];spoken_segments=[x['text'] for x in s['audio_segments'] if x['kind']=='spoken']
        add('speech:'+sid,[],{'segments':s['audio_segments'],'spoken':[spoken(t,policy) for t in spoken_segments],'voice':p.profile['voice'],'ffmpeg':p.profile['runtime']['ffmpeg']},[p.root/'data'/f'{sid}.audio.json',p.root/'assets/voice'/f'{sid}.wav'],['mandarin_speech.py'])
        align=[p.root/'data/forced-alignment'/f'{sid}-{i:03}.json' for i in range(len(spoken_segments))]
        add('align:'+sid,['speech:'+sid],p.profile['alignment'],align,['mandarin_speech.py'])
        visual={k:v for k,v in s.items() if k not in ['audio_segments','narration_zh_TW','paragraphs']}
        add('scene:'+sid,['align:'+sid],{'scene':visual,'questions':[q for q in p.questions if q['scene_id']==sid],'fonts':p.profile['fonts'],'assets':p.profile['locked_assets']},[p.root/'compositions'/f'{sid}.html',p.root/'compositions'/f'{sid}.motion.json',p.root/'data'/f'{sid}.captions.json',p.root/'data'/f'{sid}.geometry.json',p.root/'boards/svg'/f'{sid}.svg'],['mandarin_build.py','mandarin_art.py'])
    for ch in p.chapters:
        add('prepare:'+ch,['scene:'+s['id'] for s in p.chapter_scenes(ch)],p.profile['runtime'],[p.qa/f'{ch}-check.json',p.qa/f'{ch}-checked-fingerprint.json',p.qa/f'{ch}-states/manifest.json',p.qa/f'{ch}-timing.json'],['mandarin.py','mandarin_build.py','capture.mjs'])
        add('render:'+ch,['prepare:'+ch],{'output':p.profile['output'],'renderer':p.profile['runtime']},[p.output/'chapters'/f'{ch}.mp4',p.qa/f'{ch}-render.json'],['mandarin.py'])
    add('root',['prepare:'+ch for ch in p.chapters],p.profile['output'],[p.root/'index.html',p.root/'data/master-timing.json',p.root/'data/master-captions.json',p.output/'captions.zh-TW.srt',p.output/'captions.zh-TW.vtt',p.qa/'master-project-check.json',p.qa/'quiz-runtime/checks.json',p.qa/'scene-seek-audit.json'],['mandarin.py','mandarin_build.py','mandarin_audit.mjs'])
    add('audio-review',['align:'+s['id'] for s in p.scenes],{},[p.qa/'audio-audition/manifest.json',p.qa/'audio-clip-structure-audit.json'],['mandarin_delivery.py'])
    add('master',['render:'+ch for ch in p.chapters]+['root'],{'title':p.profile['title']},[p.output/p.profile['master_filename'],p.output/'master.reference.pcm.wav',p.qa/'master-ffprobe.json'],['mandarin.py','runtime/assemble_master.py'])
    add('checks',['master','audio-review'],{},[p.qa/'rendered-artifact-audit.json',p.qa/'audio-continuity-audit.json',p.qa/'late-diagram-samples.json'],['mandarin_delivery.py'])
    add('delivery',['checks'],{},[p.qa/'engine-delivery.json',p.output/'engine-render-report.md',p.output/'Digital_Everyday_Masterclass_zh-TW_EDITABLE.pptx'],['mandarin_delivery.py','mandarin_build.py'])
    from .mandarin_package import source_inputs
    add('package',['delivery'],source_inputs(p),[p.output/p.profile['editable_filename'],p.qa/'engine-packaging.json'],['mandarin_delivery.py','mandarin_package.py'])
    return result

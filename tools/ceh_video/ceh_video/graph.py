"""Dependency planner with verified output reuse and per-stage implementation identity."""
from dataclasses import dataclass
from pathlib import Path
import re
from .common import digest, read, sha, write

@dataclass
class Node:
    name: str
    dependencies: list
    inputs: dict
    outputs: list
    action: list


def nodes(p):
    if p.profile.get('schema_version') == 2:
        from .mandarin_graph import nodes as mandarin_nodes
        return mandarin_nodes(p)
    root=p.root; runtime=Path(__file__).parent/'runtime'; result={}
    def add(name,deps,inputs,outputs,action,implementation):
        impl={f:sha(runtime/f) for f in implementation}
        result[name]=Node(name,deps,{'recipe':inputs,'implementation':impl},[str(x) for x in outputs],action)
    pronunciation=read(root/'pronunciation.json')
    from .speech import spoken
    for scene in p.scenes:
        sid=scene['id']; a=root/'data'/f'{sid}.audio.json'
        text=[s['text'] for s in scene['audio_segments'] if s['kind']=='spoken']
        add('speech:'+sid,[],{'text':text,'spoken':[spoken(s,pronunciation) for s in text], 'voice':p.profile['voice'],'models':p.profile['models'], 'segments':scene['audio_segments']},[a,root/'assets/voice'/f'{sid}.wav'],['speech',sid],[])
        result['speech:'+sid].inputs['implementation']={'speech.py':sha(Path(__file__).parent/'speech.py')}
        align=[root/'data/forced-alignment'/f'{sid}-{x["sentence"]:03}.json' for x in p.audio(sid)['segments'] if x['kind']=='spoken'] if a.exists() else []
        add('align:'+sid,['speech:'+sid],{'alignment':p.profile['alignment']},align,['force_align','--scene',sid],['force_align.py'])
        # Pronunciation is already represented by the audio dependency; art-only changes cannot invalidate it.
        visual={k:v for k,v in scene.items() if k not in {'narration_en_US','audio_segments'}}
        art_files=[root/x for x in p.profile['diagram_inputs'].get(sid,[])]
        visual['adapter']={x.name:sha(x) for x in art_files}; visual['cues']={x.name:sha(x) for x in (root/'scripts').glob('cues_*.json')}
        visual['override']=read(root/'data/visual-overrides.json').get(sid,{}) if (root/'data/visual-overrides.json').exists() else {}
        visual['questions']=[q for q in p.questions if q['scene_id']==sid]
        add('scene:'+sid,['speech:'+sid,'align:'+sid],visual,[root/'compositions'/f'{sid}.html',root/'compositions'/f'{sid}.motion.json',root/'data'/f'{sid}.captions.json'],['build_film','--scene',sid],['build_film.py','editorial.py','art_common.py'])
    for ch in p.chapters:
        deps=['scene:'+s['id'] for s in p.chapter_scenes(ch)]
        add('prepare:'+ch,deps,{'output':p.profile['output'],'runtime':p.profile['runtime']['hyperframes']},[p.qa/f'{ch}-check.json',p.qa/f'{ch}-checked-fingerprint.json',p.qa/f'{ch}-states/manifest.json'],['chapter','prepare',ch],['chapter.py'])
        result['prepare:'+ch].inputs['implementation']['capture.mjs']=sha(Path(__file__).parent/'capture.mjs')
        add('render:'+ch,['prepare:'+ch],{'encoding':p.profile['output'],'runtime':p.profile['runtime']['hyperframes']},[p.output/'chapters'/f'{ch}.mp4',p.qa/f'{ch}-render.json'],['chapter','render',ch],['chapter.py'])
    add('root',['prepare:'+x for x in p.chapters],{},[root/'index.html',root/'data/master-timing.json',p.output/'captions.en-US.srt',p.output/'captions.en-US.vtt',p.qa/'master-project-check.json',p.qa/'quiz-runtime/checks.json',p.qa/'scene-seek-audit.json'],['root'],['assemble_project.py','export_metadata.py','audit_quiz.mjs','audit_scene_seek.mjs'])
    recognition={s['id']:sha(p.qa/'recognition'/f'{s["id"]}.json') for s in p.scenes if (p.qa/'recognition'/f'{s["id"]}.json').exists()}
    add('audio-review',['speech:'+s['id'] for s in p.scenes]+['align:'+s['id'] for s in p.scenes],{'recognition':recognition},[p.qa/'audio-audition/manifest.json',p.qa/'audio-clip-structure-audit.json'],['audio-review'],['recognition_audit.py','audit_audio_clips.py','review_audio.py','measure_speech.py','asr_receipt.py'])
    result['audio-review'].inputs['implementation']['review.py']=sha(Path(__file__).parent/'review.py')
    add('master',['render:'+x for x in p.chapters]+['root'],{'metadata_title':p.profile.get('metadata_title',p.profile.get('title','CEH'))},[p.output/p.profile['master_filename'],p.output/'master.reference.pcm.wav',p.qa/'master-ffprobe.json'],['assemble_master'],['assemble_master.py'])
    add('checks',['master','audio-review'],{},[p.qa/'rendered-artifact-audit.json',p.qa/'audio-continuity-audit.json',p.qa/'late-diagram-samples.json'],['checks'],['audit_rendered.py','audit_audio_continuity.py','capture_late_diagrams.py'])
    add('delivery',['checks'],{},[p.qa/'engine-delivery.json',p.output/'engine-render-report.md'],['delivery'],[])
    add('package',['delivery'],{},[p.output/p.profile['editable_filename'],p.qa/'engine-packaging.json'],['package'],[])
    for name in ['delivery','package']:result[name].inputs['implementation']['delivery.py']=sha(Path(__file__).parent/'delivery.py')
    return result


def receipt_path(p,name): return p.state/'nodes'/(name.replace(':','--')+'.json')

def output_hashes(p,node):
    paths=[Path(x) for x in node.outputs]
    if node.name.startswith('speech:'):
        sid=node.name.split(':')[1]
        if (p.root/'data'/f'{sid}.audio.json').exists():
            for row in p.audio(sid)['segments']:
                if row['kind']=='spoken': paths += [p.root/row['path'],p.root/row['path'].replace('assets/voice/','assets/voice-baseline/'),(p.root/row['path']).with_suffix('.json')]
    result={}
    for f in sorted(set(paths)):
        if not f.is_file():continue
        if f.suffix=='.html':
            import hashlib
            value=hashlib.sha256(re.sub(rb' data-hf-id="[^"]*"',b'',f.read_bytes())).hexdigest()
        else:value=sha(f)
        result[str(f.relative_to(p.root.parent))]=value
    return result


def node_key(p,node):
    dependencies={}
    for name in node.dependencies:
        f=receipt_path(p,name);r=read(f) if f.exists() else {}
        dependencies[name]={'key':r.get('key'),'outputs':r.get('outputs',{})}
    return digest({'inputs':node.inputs,'dependencies':dependencies})


def inspect_node(p,node):
    # Reviews are live release guards even when encoded bytes are cached.
    if node.name.startswith('render:'):
        from .review import require_review
        require_review(p,node.name.split(':')[1])
    if node.name in {'delivery','package'}:
        from .review import require_encoded
        require_encoded(p)
    key=node_key(p,node);f=receipt_path(p,node.name);r=read(f) if f.exists() else None
    reasons=[]
    if not r:reasons.append('no verified receipt')
    elif r.get('key')!=key:reasons.append('declared input or dependency changed')
    elif r.get('status')!='verified':reasons.append('previous execution not verified')
    elif output_hashes(p,node)!=r['outputs'] or any(not Path(x).exists() for x in node.outputs):reasons.append('missing or changed output')
    return {'node':node.name,'key':key,'action':'run' if reasons else 'reuse','reasons':reasons or ['verified inputs and output hashes match']}


def planning(p,target):
    graph=nodes(p); rows=[]; visited={}; visiting=set()
    def walk(name):
        if name in visited: return visited[name]
        if name in visiting: raise ValueError('Dependency cycle '+name)
        visiting.add(name);node=graph[name];depkeys={n:{'key':walk(n)['key'],'outputs':read(receipt_path(p,n)).get('outputs',{}) if receipt_path(p,n).exists() else {}} for n in node.dependencies}
        key=digest({'inputs':node.inputs,'dependencies':depkeys});path=receipt_path(p,name);old=read(path) if path.exists() else None
        reasons=[]
        if not old: reasons.append('no verified receipt')
        elif old.get('key')!=key: reasons.append('declared input or dependency changed')
        elif old.get('status')!='verified': reasons.append('previous execution not verified')
        if old and not reasons:
            actual=output_hashes(p,node)
            if actual!=old['outputs'] or any(not Path(f).exists() for f in node.outputs): reasons.append('missing or changed output')
        changed_deps=[n for n in node.dependencies if visited[n]['action']=='run']
        if changed_deps: reasons.append('dependency requires work: '+','.join(changed_deps))
        row={'node':name,'key':key,'action':'run' if reasons else 'reuse','reasons':reasons or ['verified inputs and output hashes match']}
        visited[name]=row;rows.append(row);visiting.remove(name);return row
    walk(target);return rows


def commit_receipt(p,node,key,origin='executed'):
    outputs=output_hashes(p,node)
    missing=[f for f in node.outputs if not Path(f).is_file()]
    if missing:raise RuntimeError('Missing stage output: '+str(missing))
    row={'status':'verified','key':key,'outputs':outputs,'origin':origin}
    write(receipt_path(p,node.name),row);return row

"""Material inputs for English v1.2 encoded QA, independent of execution IDs."""
from .common import sha, read


def applies(p,node):
    if p.profile.get('schema_version')==2:
        return node.name=='checks'
    return node.name in {'checks:frames','checks:audio','checks:late'} and p.profile.get('audio_policy')=='ceh-en-v1.2'


def files(p,node):
    paths=[p.root/'production.json',p.root/'data/master-timing.json',p.output/p.profile['master_filename']]
    if p.profile.get('schema_version')==2:
        paths += [p.root/'data/questions.json',p.root/'data/scenes.json',p.output/'master.reference.pcm.wav',
                  p.qa/'master-full-decode.json',p.qa/'master-full-decode.log',
                  p.qa/'master-full-decode.progress',p.qa/'master-ffprobe.json']
        paths += [p.root/'data'/f'{s['id']}.audio.json' for s in p.scenes]
        paths += [p.root/'assets/voice'/f'{s['id']}.wav' for s in p.scenes]
        return paths
    if node.name=='checks:audio':
        paths += [p.root/'data/questions.json',p.output/'master.reference.pcm.wav']
        paths += [p.root/'data'/f'{s["id"]}.audio.json' for s in p.scenes]
    else:
        paths += [p.root/'assets/fonts/LiberationSans-Regular.ttf']
        if node.name=='checks:frames':
            paths += [p.output/'chapters'/f'{ch}.mp4' for ch in p.chapters]
        else:paths += [p.root/'data/scenes.json']
    return paths


def material(p,node,dependencies):
    # Preserve all master output hashes (including scan evidence); only its
    # execution recipe key is omitted. Current upstream work still precedes QA.
    deps={}
    for name,row in dependencies.items():
        receipt=p.state/'nodes'/(name.replace(':','--')+'.json')
        deps[name]={'outputs':row['outputs'],
                    'status':read(receipt).get('status') if receipt.exists() else None}
    inputs={str(f.relative_to(p.root.parent)):sha(f) if f.is_file() else None for f in files(p,node)}
    result={'consumed_files':inputs,'dependencies':deps}
    if p.profile.get('schema_version')==2:
        from .media_scan import decoder_identity
        result['decoder']=decoder_identity()
    return result

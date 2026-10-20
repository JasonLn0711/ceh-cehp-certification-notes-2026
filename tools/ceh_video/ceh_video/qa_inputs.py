"""Material inputs for English v1.2 encoded QA, independent of execution IDs."""
from .common import sha, read


def applies(p,node):
    return node.name in {'checks:frames','checks:audio','checks:late'} and p.profile.get('audio_policy')=='ceh-en-v1.2'


def files(p,node):
    paths=[p.root/'production.json',p.root/'data/master-timing.json',p.output/p.profile['master_filename']]
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
    return {'consumed_files':inputs,'dependencies':deps}

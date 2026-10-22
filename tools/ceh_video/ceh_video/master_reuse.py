"""Avoid remux/decode when actual assembly inputs and all proof remain intact.

This local receipt is populated only after successful assembly. Dependency gates
still execute in the runner. No historical receipt is promoted automatically.
"""
from pathlib import Path
from .common import read, sha, write
from .media_scan import decoder_identity, require_scan


def receipt(p):
    return p.state/'master-reuse.json'


def identity(p):
    timing=p.root/'data/master-timing.json';m=read(timing)
    files=[p.root/'production.json',timing]
    files += [p.root/'assets/voice'/f'{s["scene"]}.wav' for s in m['scenes']]
    files += [p.output/'chapters'/f'{c["id"]}.mp4' for c in m['chapters']]
    package=Path(__file__).parent
    return {'inputs':{str(f.relative_to(p.root.parent)):sha(f) for f in files},
            'runtime':decoder_identity(),
            'implementation':{rel:sha(package/rel) for rel in
                ('master_reuse.py','master_audio_cache.py','pcm_reuse.py','runtime/assemble_master.py','common.py')}}


def outputs(p):
    return [p.output/p.profile['master_filename'],p.output/'master.reference.pcm.wav',
            *[p.qa/name for name in ('master-ffprobe.json','master-full-decode.json',
             'master-full-decode.log','master-full-decode.progress','master-stage-timing.json',
             'master-audio-cache.json','master-assembly.log','master-assembly.progress',
             'chapter-concat.txt','chapter-metadata.ffmeta')]]


def reusable(p,key):
    try:
        row=read(receipt(p))
        if (row['status']!='verified' or row['identity']!=key or
            row['outputs']!={str(f):sha(f) for f in outputs(p)}):return False
        require_scan(p.output/p.profile['master_filename'],read(p.root/'data/master-timing.json')['frames'],p.qa)
        return True
    except (OSError,ValueError,KeyError,TypeError):
        return False


def retain(p,key):
    if identity(p)!=key:raise ValueError('Assembly inputs changed during execution')
    require_scan(p.output/p.profile['master_filename'],read(p.root/'data/master-timing.json')['frames'],p.qa)
    write(receipt(p),{'status':'verified','identity':key,
                     'outputs':{str(f):sha(f) for f in outputs(p)}})

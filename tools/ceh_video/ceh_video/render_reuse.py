"""Reuse encoded chapters after fresh QA without copying heavy media.

Only this engine's post-render receipt can seed reuse. Historical receipts alone
are insufficient. Callers must run current visual and review gates first.
"""
from pathlib import Path
import shutil
from .common import read, sha, write


def identity(p, chapter):
    package = Path(__file__).parent
    env = p.environment()
    files = [p.root/'package-lock.json', p.root/'node_modules/.bin/hyperframes',
             Path(p.profile['runtime']['browser']), Path(shutil.which('ffmpeg'))]
    # Bind installed renderer code as well as the lockfile; shared runtime may change.
    native = (p.root/'node_modules/hyperframes/dist')
    files += sorted(native.glob('*.js'))
    return {'source': p.chapter_inputs(chapter), 'runtime': p.profile['runtime'],
            'output': p.profile['output'],
            'environment': {k:v for k,v in env.items() if k.startswith(('PRODUCER_', 'HF_', 'HYPERFRAMES_')) and k != 'HYPERFRAMES_RUN_ID'},
            'runtime_files': {str(f.resolve()): sha(f) for f in files},
            'implementation': {f:sha(package/f) for f in
                               ('render_reuse.py','runtime/chapter.py','common.py')}}


def outputs(p, chapter):
    return [p.output/'chapters'/f'{chapter}.mp4',
            *[p.qa/f'{chapter}-{suffix}' for suffix in
              ('render.json','render.log','render.log.stderr')]]


def receipt(p, chapter):
    return p.state/'encoded-chapters'/f'{chapter}.json'


def reusable(p, chapter, key):
    try:
        row = read(receipt(p, chapter))
        return (row['status'] == 'verified' and row['identity'] == key and
                row['outputs'] == {str(f):sha(f) for f in outputs(p,chapter)})
    except (OSError, ValueError, KeyError):
        return False


def retain(p, chapter, key):
    if identity(p,chapter) != key:
        raise RuntimeError('Render inputs changed during chapter execution')
    result = read(p.qa/f'{chapter}-render.json')
    if (result.get('status') != 'rendered_codec_verified' or
        result.get('source_sha256') != key['source'] or
        result.get('output_sha256') != sha(p.output/'chapters'/f'{chapter}.mp4')):
        raise RuntimeError('Chapter render proof does not match encoded artifact')
    write(receipt(p,chapter),dict(status='verified',identity=key,
          outputs={str(f):sha(f) for f in outputs(p,chapter)}))

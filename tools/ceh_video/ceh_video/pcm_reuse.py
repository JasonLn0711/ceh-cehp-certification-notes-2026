"""Verified local PCM concatenation; no inference, tempo change or shared output inode."""
from pathlib import Path
import os
import tempfile
from .common import digest, read, sha, write


def concatenate(p, sources, target, force=False):
    import soundfile as sf
    sources = [Path(s) for s in sources]
    target = Path(target)
    key = {'sources': [sha(s) for s in sources], 'format': [48000, 2, 'PCM_16'],
           'implementation': sha(__file__), 'soundfile': sf.__version__,
           'libsndfile': sf.__libsndfile_version__}
    receipt = p.state/'pcm'/((digest(str(target)))+'.json')
    try:
        old = read(receipt)
        if not force and old['identity'] == key and old['sha256'] == sha(target):
            return old['samples']
    except (OSError, ValueError, KeyError, TypeError):
        pass
    receipt.unlink(missing_ok=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=target.name+'.partial-', suffix='.wav', dir=target.parent)
    os.close(fd)
    temp = Path(name)
    try:
        total = 0
        with sf.SoundFile(temp, 'w', samplerate=48000, channels=2, subtype='PCM_16') as out:
            for source in sources:
                with sf.SoundFile(source) as src:
                    if src.samplerate != 48000 or src.channels != 2 or len(src) % 1600:
                        raise ValueError('PCM input format/timing differs')
                    for block in src.blocks(blocksize=48000, dtype='int16', always_2d=True):
                        out.write(block); total += len(block)
        if [sha(s) for s in sources] != key['sources']:
            raise RuntimeError('PCM sources changed during assembly')
        temp.replace(target)
        write(receipt, {'identity': key, 'sha256': sha(target), 'samples': total})
        return total
    finally:
        temp.unlink(missing_ok=True)


def write_changed(path, data):
    path = Path(path)
    if isinstance(data, str):
        data = data.encode()
    if not path.exists() or path.read_bytes() != data:
        path.write_bytes(data)


def copy_changed(source, destination):
    import shutil
    if not destination.exists() or sha(source) != sha(destination):
        shutil.copy2(source, destination)

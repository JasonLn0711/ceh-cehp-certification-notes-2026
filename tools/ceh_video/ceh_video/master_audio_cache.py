"""Cache the continuously encoded AAC track, never concatenated chapter AAC.

Reusing this cache skips encoding only. Every assembled movie still requires the
full continuity, sample timing, AAC residue and artifact acceptance gates.
"""
from pathlib import Path
import subprocess
import time
from .common import digest, read, sha, write
from .media_scan import decoder_identity


def audio_key(pcm, samples, profile):
    return {'pcm_sha256': sha(pcm), 'samples': samples,
            'sample_rate': 48000, 'channels': 2,
            'voice': profile.get('voice'), 'models': profile.get('models'),
            'audio_policy': profile.get('audio_policy'),
            'encoder': {'codec': 'aac', 'bitrate': '192k', 'sample_rate': 48000},
            # QA implementation changes do not change AAC encoding identity.
            'runtime': {k:v for k,v in decoder_identity().items()
                        if k != 'implementation_sha256'},
            'implementation_sha256': sha(__file__)}


def cached_audio(folder, key):
    folder = Path(folder); stem = digest(key)
    audio = folder/(stem+'.m4a'); receipt = folder/(stem+'.json')
    if not audio.is_file() or not receipt.is_file():
        return None
    try:
        row = read(receipt)
        if (row['key'] == key and row['status'] == 'encoded_integrity_verified'
                and row['audio_sha256'] == sha(audio)):
            return audio
    except (KeyError, ValueError, TypeError):
        pass
    return None


def retain_audio(movie, folder, key):
    folder = Path(folder); folder.mkdir(parents=True, exist_ok=True)
    existing = cached_audio(folder, key)
    if existing:
        return existing
    stem = digest(key); audio = folder/(stem+'.m4a')
    temporary = folder/(stem+'.pending.m4a')
    before = sha(movie); began = time.monotonic()
    try:
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(movie),
                        '-map','0:a:0','-c:a','copy','-map_metadata','-1',
                        '-map_chapters','-1',
                        str(temporary)], check=True)
        if sha(movie) != before:
            raise ValueError('Master changed while retaining its continuous AAC track')
        temporary.replace(audio)
        write(folder/(stem+'.json'),
              dict(status='encoded_integrity_verified', key=key,
                   source_master_sha256=before, audio_sha256=sha(audio),
                   elapsed_seconds=time.monotonic()-began,
                   scope='Cache integrity only; assembled movie requires full audio QA'))
    finally:
        temporary.unlink(missing_ok=True)
    return audio

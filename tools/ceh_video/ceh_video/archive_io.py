"""Owned temporary archives: cleanup on exception, promotion only after verification."""
from contextlib import contextmanager
from pathlib import Path
import os
import tempfile


@contextmanager
def partial_archive(target):
    target = Path(target)
    # Same filesystem as the final archive, so promotion is an atomic rename.
    fd, name = tempfile.mkstemp(prefix=target.name+'.partial-', dir=target.parent)
    os.close(fd)
    partial = Path(name)
    try:
        yield partial
    finally:
        partial.unlink(missing_ok=True)


def verified_stream_archive(entries, target, emit):
    """Verify every member CRC/hash by streaming; no extracted media tree required."""
    import hashlib
    import json
    import shutil
    import zipfile
    from pathlib import PurePosixPath
    from .common import sha
    target = Path(target)
    if target.exists() or target.is_symlink():
        raise RuntimeError('Closed archive exists; choose a new release path')
    names = [name for _, name in entries]
    if len(names) != len(set(names)) or 'FILES_SHA256.json' in names:
        raise ValueError('Duplicate or reserved archive member')
    for path, name in entries:
        if (PurePosixPath(name).is_absolute() or '..' in PurePosixPath(name).parts
                or '\\' in name or Path(path).is_symlink()):
            raise ValueError('Unsafe archive input: '+name)
    size = sum(Path(f).stat().st_size for f,_ in entries)
    required = size + 128*1024*1024
    if shutil.disk_usage(target.parent).free < required:
        raise RuntimeError(f'Insufficient archive scratch space: need {required} bytes')
    manifest = {name:sha(f) for f,name in entries}
    with partial_archive(target) as partial:
        with zipfile.ZipFile(partial,'w',zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
            for i,(f,name) in enumerate(entries,1):
                z.write(f,name,compress_type=zipfile.ZIP_STORED if Path(f).suffix.lower() in
                        {'.mp4','.mp3','.jpg','.jpeg','.png','.pptx','.zip','.pdf'} else zipfile.ZIP_DEFLATED)
                if i%100==0 or i==len(entries):
                    emit({'phase':'archive_write','completed':i,'total':len(entries)})
            z.writestr('FILES_SHA256.json',json.dumps(manifest,sort_keys=True)+'\n')
        with zipfile.ZipFile(partial) as z:
            if json.loads(z.read('FILES_SHA256.json')) != manifest:
                raise RuntimeError('Archive manifest mismatch')
            for i,(name,expected) in enumerate(manifest.items(),1):
                with z.open(name) as stream:
                    actual=hashlib.file_digest(stream,'sha256').hexdigest()
                if actual != expected:
                    raise RuntimeError('Archive payload differs: '+name)
                if i%100==0 or i==len(manifest):
                    emit({'phase':'archive_crc_hash','completed':i,'total':len(manifest)})
        result={'sha256':sha(partial),'bytes':partial.stat().st_size,
                'entries':len(entries)+1,'verified_payloads':len(entries),
                'source_bytes':size,'crc':'passed','payload_hashes':'passed',
                'media_staging_bytes':0,'verification_extraction_bytes':0,
                'verification_mode':'stream_all_members_crc_sha256',
                'verification_workspace_retained':False}
        partial.replace(target)
    return result

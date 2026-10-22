"""Exact-byte content-addressed archives; legacy release paths remain immutable."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import tempfile
import zipfile
from .archive_io import partial_archive
from .common import sha
from .compact_restore import safe_name, restore


def write_compact(entries, target, emit=lambda row: None, verify=None, extra_restore_bytes=0):
    """Entries are (source Path or bytes, original relative path). Verify before publish."""
    entries = list(entries)
    target = Path(target)
    sidecar = target.with_name(target.name + '.sha256')
    restorer = target.parent / 'RESTORE.py'
    script = Path(__file__).with_name('compact_restore.py').read_bytes()
    if target.exists() or target.is_symlink() or sidecar.exists() or sidecar.is_symlink():
        raise FileExistsError('Closed archive exists')
    if restorer.is_symlink() or (restorer.exists() and restorer.read_bytes() != script):
        raise FileExistsError('Different RESTORE.py already exists')
    rows, objects, names = [], {}, set()
    for index, (source, name) in enumerate(entries, 1):
        safe_name(name)
        if name in names:
            raise ValueError('Duplicate payload path')
        names.add(name)
        if isinstance(source, bytes):
            h, size, mode = hashlib.sha256(source).hexdigest(), len(source), 0o644
        else:
            source = Path(source)
            if source.is_symlink() or not source.is_file():
                raise ValueError('Payload must be a regular file')
            h, size, mode = sha(source), source.stat().st_size, source.stat().st_mode & 0o777
        rows.append({'path': name, 'sha256': h, 'bytes': size, 'mode': mode})
        objects.setdefault(h, source)
        if index % 100 == 0 or index == len(entries):
            emit({'phase': 'archive_input_hashes', 'completed': index, 'total': len(entries)})
    total = sum(r['bytes'] for r in rows)
    unique = sum(len(s) if isinstance(s, bytes) else s.stat().st_size for s in objects.values())
    if type(extra_restore_bytes) is not int or extra_restore_bytes < 0:
        raise ValueError('Invalid reconstruction reserve')
    required = total + unique + extra_restore_bytes + 128 * 1024 * 1024
    if shutil.disk_usage(target.parent).free < required:
        raise OSError('Insufficient package/restore space: need ' + str(required))
    with partial_archive(target) as partial:
        with zipfile.ZipFile(partial, 'w', zipfile.ZIP_DEFLATED, compresslevel=1, allowZip64=True) as z:
            for i, (h, source) in enumerate(objects.items(), 1):
                observed = hashlib.sha256()
                with z.open('objects/' + h, 'w', force_zip64=True) as out:
                    if isinstance(source, bytes):
                        observed.update(source); out.write(source)
                    else:
                        with source.open('rb') as src:
                            while block := src.read(1024 * 1024):
                                observed.update(block); out.write(block)
                if observed.hexdigest() != h:
                    raise RuntimeError('Source changed during archive write')
                if i % 100 == 0 or i == len(objects):
                    emit({'phase': 'archive_unique_objects', 'completed': i, 'total': len(objects)})
            z.writestr('COMPACT_MANIFEST.json', json.dumps({'format': 'compact-v1', 'files': rows}, ensure_ascii=False))
            z.writestr('RESTORE.py', script)
        # Detect changes to duplicate sources too: each declared path is authoritative.
        for (source, _), row in zip(entries, rows):
            if not isinstance(source, bytes) and sha(source) != row['sha256']:
                raise RuntimeError('Source changed during archive write: ' + row['path'])
        with tempfile.TemporaryDirectory(prefix='verify-package-', dir=target.parent) as temp:
            result = restore(partial, Path(temp) / 'restored', emit)
            if verify:
                verify(Path(temp) / 'restored')
        result.update(sha256=sha(partial), bytes=partial.stat().st_size, source_bytes=total,
                      unique_bytes=unique, duplicate_bytes=total-unique, unique_objects=len(objects),
                      media_staging_bytes=0, verification_extraction_bytes=total,
                      verification_workspace_retained=False,
                      reconstruction_reserve_bytes=extra_restore_bytes, required_free_bytes=required)
        result.pop('destination', None)
        # Publish companions first, rolling back only files created by this call
        # if final archive promotion fails. Existing matching RESTORE.py is retained.
        published = []
        try:
            with partial_archive(sidecar) as temp:
                temp.write_text(result['sha256'] + '  ' + target.name + '\n')
                os.link(temp, sidecar); published.append(sidecar)
            if not restorer.exists():
                with partial_archive(restorer) as temp:
                    temp.write_bytes(script)
                    try:
                        os.link(temp, restorer); published.append(restorer)
                    except FileExistsError:
                        if restorer.is_symlink() or restorer.read_bytes()!=script:
                            raise
            elif restorer.is_symlink() or restorer.read_bytes()!=script:
                raise FileExistsError('RESTORE.py changed before publication')
            os.link(partial, target)  # Atomic no-clobber publication on the same filesystem.
        except BaseException:
            for path in reversed(published):
                path.unlink(missing_ok=True)
            raise
    return result

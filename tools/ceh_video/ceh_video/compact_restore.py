"""Standalone, standard-library-only compact-v1 restoration (also shipped as RESTORE.py)."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import sys
import tempfile
import zipfile


def safe_name(name):
    if not isinstance(name, str) or not name or '\\' in name or '\x00' in name:
        raise ValueError('Unsafe payload path')
    p = PurePosixPath(name)
    if p.is_absolute() or any(x in ('', '.', '..') for x in name.split('/')) or ':' in name:
        raise ValueError('Unsafe payload path: ' + name)
    return name


def manifest(z):
    names = z.namelist()
    if len(names) != len(set(names)):
        raise ValueError('Duplicate archive members')
    m = json.loads(z.read('COMPACT_MANIFEST.json'))
    if m.get('format') != 'compact-v1' or not isinstance(m.get('files'), list):
        raise ValueError('Unsupported archive format')
    paths = set()
    objects = {}
    for r in m['files']:
        name = safe_name(r['path'])
        h = r['sha256']
        if (not isinstance(h, str) or len(h) != 64 or any(c not in '0123456789abcdef' for c in h)
                or type(r['bytes']) is not int or r['bytes'] < 0
                or type(r['mode']) is not int or r['mode'] & ~0o777):
            raise ValueError('Invalid payload metadata')
        if name in paths:
            raise ValueError('Duplicate destination')
        paths.add(name)
        if h in objects and objects[h] != r['bytes']:
            raise ValueError('Inconsistent object size')
        objects[h] = r['bytes']
    for name in paths:
        if any(str(p) in paths for p in PurePosixPath(name).parents if str(p) != '.'):
            raise ValueError('Conflicting destination paths')
    expected = {'COMPACT_MANIFEST.json', 'RESTORE.py'} | {'objects/' + h for h in objects}
    if set(names) != expected:
        raise ValueError('Missing or unexpected archive members')
    for info in z.infolist():
        if info.is_dir() or stat.S_ISLNK(info.external_attr >> 16):
            raise ValueError('Archive links/directories are not payloads')
    for h, size in objects.items():
        if z.getinfo('objects/' + h).file_size != size:
            raise ValueError('Object size mismatch')
    return m


def restore(archive, destination, emit=lambda row: None):
    destination = Path(destination).absolute()
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('Restore destination must not exist')
    if not destination.parent.is_dir():
        raise ValueError('Destination parent must exist')
    with zipfile.ZipFile(archive) as z:
        m = manifest(z)
        required = sum(r['bytes'] for r in m['files']) + 128 * 1024 * 1024
        if shutil.disk_usage(destination.parent).free < required:
            raise OSError('Insufficient restore space: need ' + str(required))
        # The private staging tree contains independent regular files, never links.
        with tempfile.TemporaryDirectory(prefix='.compact-restore-', dir=destination.parent) as temp:
            base = Path(temp) / 'restored'
            base.mkdir()
            for i, row in enumerate(m['files'], 1):
                out = base / row['path']
                out.parent.mkdir(parents=True, exist_ok=True)
                h = hashlib.sha256()
                with z.open('objects/' + row['sha256']) as src, out.open('xb') as dst:
                    while block := src.read(1024 * 1024):
                        h.update(block)
                        dst.write(block)
                if h.hexdigest() != row['sha256'] or out.stat().st_size != row['bytes']:
                    raise ValueError('Corrupt object: ' + row['path'])
                out.chmod(row['mode'])
                if i % 100 == 0 or i == len(m['files']):
                    emit({'phase': 'restore_payloads', 'completed': i, 'total': len(m['files'])})
            # Recheck before promotion, including dangling symlinks.
            if destination.exists() or destination.is_symlink():
                raise FileExistsError('Destination appeared during restore')
            base.rename(destination)
    return {'format': 'compact-v1', 'verified_payloads': len(m['files']),
            'restored_bytes': sum(r['bytes'] for r in m['files']), 'destination': str(destination)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', required=True)
    parser.add_argument('--destination', required=True)
    args = parser.parse_args()
    def progress(row):
        print(json.dumps(row), file=sys.stderr, flush=True)
    try:
        result=restore(args.archive, args.destination, progress)
    except (Exception,KeyboardInterrupt) as exc:
        print(json.dumps({'status':'interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed','error':str(exc)}),file=sys.stderr)
        raise SystemExit(130 if isinstance(exc,KeyboardInterrupt) else 1)
    print(json.dumps(result, ensure_ascii=False))

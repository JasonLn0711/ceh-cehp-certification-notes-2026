"""One authorized batch: four exact archive-verification directories, 2026-10-22.

Default: prepare immutable preflight evidence. --apply: revalidate and remove
only these four redundant trees. No arbitrary paths or recursive discovery.
"""
import argparse
from contextlib import ExitStack
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import subprocess
import sys
import time
import zipfile

BASE = Path('/home/jnlngx10/Videos')
NAMES = ('Digital_Everyday_Masterclass_v1', 'Island_Workshop_MATLAB_Concepts_v1',
         'Island_Workshop_MATLAB_Concepts_v2_1p3', 'Island_Workshop_MATLAB_Concepts_v3_images_gpu')
HERE = Path(__file__).resolve().parent
EXCLUDED_HISTORY = BASE/'CEH_M11_initial_v1/qa/authoring-history/report-locator-correction/CEH_M11_English_Masterclass_v1_EDITABLE.zip.partial-e01d2c6d'


def sha(p):
    with Path(p).open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def write(p, obj):
    tmp = p.with_suffix('.json.tmp')
    with tmp.open('w') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n'); f.flush(); os.fsync(f.fileno())
    tmp.replace(p)


def event(phase, **data):
    print(json.dumps({'phase':phase, **data}), file=sys.stderr, flush=True)


def physical_tree(target):
    if target.resolve() != target or target.is_symlink() or not target.is_dir():
        raise RuntimeError('Target path identity differs: '+str(target))
    device = target.stat().st_dev
    rows = {}; blocks = target.stat().st_blocks*512
    for folder, dirs, files in os.walk(target, followlinks=False):
        for name in sorted(dirs+files):
            p = Path(folder)/name; info = p.lstat()
            if info.st_dev != device or stat.S_ISLNK(info.st_mode) or os.path.ismount(p):
                raise RuntimeError('Linked or mounted entry: '+str(p))
            if not (stat.S_ISDIR(info.st_mode) or stat.S_ISREG(info.st_mode)):
                raise RuntimeError('Nonregular entry: '+str(p))
            blocks += info.st_blocks*512
            if p.is_file():
                if info.st_nlink != 1:raise RuntimeError('Shared inode: '+str(p))
                rows[str(p.relative_to(target))] = {
                    'size':info.st_size,'mtime_ns':info.st_mtime_ns,
                    'inode':info.st_ino,'sha256':sha(p)}
    return rows, blocks


def idle(target):
    check = subprocess.run(['lsof','-nP','-Fpn','+D',str(target)], capture_output=True, text=True)
    if check.stdout.strip() or check.returncode not in (0,1):
        raise RuntimeError('Open handles or lsof failure: '+str(target))
    # Report visibility limits on unrelated filesystems; never suppress target warnings.
    for line in check.stderr.splitlines():
        if not line.strip() or 'Output information may be incomplete.' in line:continue
        if 'WARNING:' not in line or not any(s in line for s in (
                '/sys/kernel/debug/tracing','/var/lib/docker/overlay2/','/run/docker/netns/')):
            raise RuntimeError('Unresolved target inspection: '+line)
    return {'open_handles_observed':False,'exit_code':check.returncode,
            'other_filesystem_warnings':check.stderr.strip(),
            'scope':'Target lsof scan plus exclusive engine run lock; unrelated namespace visibility is not asserted'}


def protected(workspace):
    output = workspace/'output'; target = output/'archive-verification'
    result = {}
    for p in output.rglob('*'):
        if p==target or target in p.parents:continue
        if p.is_file() and not p.is_symlink():
            result[str(p)] = sha(p)
    receipt = workspace/'qa/engine-packaging.json'
    result[str(receipt)] = sha(receipt)
    return result


def verify(name):
    started = time.monotonic(); workspace=BASE/name
    target = workspace/'output/archive-verification'
    receipt_path = workspace/'qa/engine-packaging.json'
    receipt = json.loads(receipt_path.read_text())
    archive = Path(receipt['zip']); extracted = Path(receipt['extracted_root'])
    if archive.parent != workspace/'output' or archive.is_symlink():
        raise RuntimeError('Unexpected recovery ZIP location')
    if extracted.parent != target or set(target.iterdir()) != {extracted}:
        raise RuntimeError('Unexpected verification contents')
    if receipt['status'] != 'crc_extraction_and_all_payload_hashes_passed':
        raise RuntimeError('Missing original full archive verification')
    event('verify_start',workspace=name)
    if sha(archive) != receipt['zip_sha256']:raise RuntimeError('Recovery ZIP changed')
    with zipfile.ZipFile(archive) as z:
        manifest_name = extracted.name+'/FILES_SHA256.txt'
        raw = z.read(manifest_name)
    expected = {}
    for line in raw.decode().splitlines():
        digest, rel = line.split('  ',1)
        if PurePosixPath(rel).is_absolute() or '..' in PurePosixPath(rel).parts or rel in expected:
            raise RuntimeError('Invalid recovery manifest')
        expected[extracted.name+'/'+rel] = digest
    expected[manifest_name] = hashlib.sha256(raw).hexdigest()
    rows, blocks = physical_tree(target)
    if set(rows) != set(expected):raise RuntimeError('Missing or extra extracted files')
    if any(rows[rel]['sha256'] != h for rel,h in expected.items()):
        raise RuntimeError('Extracted file changed; preserve this tree')
    handles = idle(target)
    keep = protected(workspace)
    result = {'workspace':name,'target':str(target),'archive':str(archive),
              'archive_sha256':receipt['zip_sha256'],'receipt':str(receipt_path),
              'payloads':len(expected)-1,'files':rows,'allocated_bytes_including_directories':blocks,
              'target_inode':target.stat().st_ino,'protected_sha256':keep,'usage_check':handles}
    event('verified',workspace=name,files=len(rows),elapsed_seconds=round(time.monotonic()-started,2))
    return result


def incoming_links():
    targets = [BASE/name/'output/archive-verification' for name in NAMES]
    matches=[]
    roots=[BASE,Path('/home/jnlngx10/phd-research/repos/nycu-115-1-coursework')]
    def fail(exc):raise exc
    for root in roots:
        for folder,dirs,files in os.walk(root,followlinks=False,onerror=fail):
            dirs[:]=[d for d in dirs if d not in {'.git','.venv','node_modules'}]
            for name in dirs+files:
                p=Path(folder)/name
                if p.is_symlink():
                    actual=p.resolve()
                    if any(actual==t or t in actual.parents for t in targets):matches.append(str(p))
    if matches:raise RuntimeError('Incoming dependency links: '+str(matches))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    manifest=HERE/'preflight.json'; result_path=HERE/'result.json'
    if args.apply and result_path.exists():
        parser.error('Batch already has results; reconcile before retry')
    report={'schema':1,'policy_version':'longform-storage-v1.0.0',
            'cleanup_id':'longform-cleanup-2026-10-22','created_at':datetime.now(timezone.utc).isoformat(),
            'authorization':'User selected verification copies and temporary files, then said Implement the plan.',
            'script_sha256':sha(__file__),'status':'checking','items':[]}
    try:
        with ExitStack() as stack:
            # Coordinate with the existing producer; existing lock files are read-only.
            for name in NAMES:
                handle=stack.enter_context((BASE/name/'project/.production/run.lock').open('r'))
                fcntl.flock(handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
            incoming_links()
            if not args.apply:
                if manifest.exists():raise RuntimeError('Preflight evidence already exists')
                report['excluded_history_sha256']=sha(EXCLUDED_HISTORY)
                report['items']=[verify(name) for name in NAMES]
                report['status']='verified_ready_for_authorized_apply'
                write(manifest,report)
            else:
                saved=json.loads(manifest.read_text())
                if saved['script_sha256']!=sha(__file__):raise RuntimeError('Reviewed script changed')
                report['disk_before']=shutil.disk_usage(BASE)._asdict()
                write(result_path,report)
                for name,old in zip(NAMES,saved['items'],strict=True):
                    if old['workspace']!=name:raise RuntimeError('Allowlist order changed')
                    current=verify(name)
                    for key in ['files','target_inode','archive_sha256','protected_sha256']:
                        if current[key]!=old[key]:raise RuntimeError('Preflight became stale: '+name+' '+key)
                    item={'workspace':name,'target':old['target'],
                          'allocated_bytes_including_directories':current['allocated_bytes_including_directories'],
                          'payloads':current['payloads'],'usage_check':current['usage_check'],'status':'deleting'}
                    report['items'].append(item);write(result_path,report)
                    target=Path(old['target'])
                    idle(target)
                    # Recheck the exact complete tree metadata immediately before removal.
                    for rel,row in current['files'].items():
                        st=(target/rel).lstat()
                        if (st.st_ino,st.st_size,st.st_mtime_ns)!=(row['inode'],row['size'],row['mtime_ns']):
                            raise RuntimeError('Entry changed before removal')
                    event('removing_verified_copy',workspace=name)
                    shutil.rmtree(target)
                    if target.exists():raise RuntimeError('Removal incomplete')
                    if protected(BASE/name)!=old['protected_sha256']:
                        raise RuntimeError('Protected delivery verification failed')
                    item.update(status='removed_and_protected_outputs_verified',protected_hashes=len(old['protected_sha256']),
                                disk_free_after=shutil.disk_usage(BASE).free)
                    write(result_path,report);event('removed_verified',workspace=name)
                if sha(EXCLUDED_HISTORY)!=saved['excluded_history_sha256']:
                    raise RuntimeError('Excluded historical evidence changed')
                report['excluded_history_verified']=True
                report['disk_after']=shutil.disk_usage(BASE)._asdict()
                report['observed_free_bytes_increase']=report['disk_after']['free']-report['disk_before']['free']
                report['removed_allocated_bytes_including_directories']=sum(i['allocated_bytes_including_directories'] for i in report['items'])
                report['measurement_note']='Filesystem free-space delta includes concurrent activity; removed inode allocation is recorded separately.'
                report['status']='completed';write(result_path,report)
        print(json.dumps({'status':report['status'],'items':len(report['items']),
                          'receipt':str(result_path if args.apply else manifest)}))
        return 0
    except (Exception,KeyboardInterrupt) as exc:
        report.update(status='interrupted' if isinstance(exc,KeyboardInterrupt) else 'stopped',error=str(exc))
        if args.apply and result_path.exists():write(result_path,report)
        else:write(HERE/'preflight-error.json',report)
        print(json.dumps({'status':report['status'],'error':str(exc)}))
        return 130 if isinstance(exc,KeyboardInterrupt) else 1


if __name__=='__main__':sys.exit(main())

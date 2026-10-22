"""Read-only long-film storage inventory. Never infers permission to delete."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import stat
import sys
import time

POLICY = 'longform-storage-v1.0.0'


def category(parts):
    if any(p in {'archive-verification','engine_project_source','preflight-fixture',
                 'preflight-fixture-attempt-01','relocation-fixture','clean-C11'}
           or p.startswith('verify-package-') for p in parts):
        return 'review_duplicate_workspaces'
    if any('.partial-' in p or p.endswith('.tmp.zip') for p in parts):
        return 'review_interrupted_temporary_files'
    if any(p in {'.venv','node_modules','python-env'} for p in parts):
        return 'runtime_dependencies'
    if 'speech-cache' in parts or 'voice' in parts:
        return 'preserve_voice_and_reconstruction'
    if 'qa' in parts:
        return 'preserve_validation_evidence'
    if parts[0] == 'output' and len(parts) == 2:
        return 'preserve_delivery_outputs'
    if 'chapters' in parts or 'assets' in parts and 'audio' in parts:
        return 'review_rebuildable_hosts_and_chapters'
    return 'preserve_source_and_other'


def audit(workspace, emit=lambda row: None):
    workspace = Path(workspace)
    if workspace.is_symlink() or not workspace.is_dir():
        raise ValueError('Expected a real workspace directory: '+str(workspace))
    workspace = workspace.resolve()
    started = time.monotonic()
    buckets = defaultdict(lambda: {'files':0,'logical_bytes':0,'allocated_bytes':0})
    seen = set(); errors = []; links = 0; files = 0; hardlinks = 0
    emit({'phase':'storage_scan_started','workspace':str(workspace)})
    def failed(exc):
        errors.append({'path':str(exc.filename),'error':type(exc).__name__})
    for folder, dirs, names in os.walk(workspace, followlinks=False, onerror=failed):
        dirs.sort(); names.sort()
        for name in list(dirs):
            if (Path(folder)/name).is_symlink():
                dirs.remove(name); links += 1
        for name in names:
            f = Path(folder)/name
            try:
                info = f.lstat()
            except OSError as exc:
                failed(exc); continue
            if stat.S_ISLNK(info.st_mode):
                links += 1; continue
            if not stat.S_ISREG(info.st_mode):
                continue
            ident = (info.st_dev,info.st_ino)
            if ident in seen:
                hardlinks += 1; continue
            seen.add(ident)
            row = buckets[category(f.relative_to(workspace).parts)]
            row['files'] += 1; files += 1
            row['logical_bytes'] += info.st_size
            row['allocated_bytes'] += info.st_blocks*512
            if files%10000 == 0:
                emit({'phase':'storage_scan','files_scanned':files,
                      'elapsed_seconds':round(time.monotonic()-started,2)})
    result = {'schema':1,'policy_version':POLICY,
              'created_at':datetime.now(timezone.utc).isoformat(),
              'workspace':str(workspace),'status':'partial' if errors else 'completed',
              'read_only':True,'files':files,'symlinks_skipped':links,
              'hardlink_entries_not_recounted':hardlinks,'errors':errors,
              'categories':dict(sorted(buckets.items())),
              'logical_bytes':sum(r['logical_bytes'] for r in buckets.values()),
              'allocated_bytes':sum(r['allocated_bytes'] for r in buckets.values()),
              'reclaimable_bytes':None,
              'measurement_scope':'Unique regular-file inodes within this workspace; no content deduplication, directory blocks, symlink targets or reflink extent accounting. Review categories are not deletion approval.'}
    emit({'phase':'storage_scan_'+result['status'],'files':files,
          'elapsed_seconds':round(time.monotonic()-started,2)})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace',nargs='+',help='Explicit workspace directories; no mutation')
    parser.add_argument('--plain',action='store_true',help='Plain progress on stderr; JSON on stdout')
    args = parser.parse_args()
    from .progress import Progress
    try:
        progress = Progress(args.plain)
        reports = [audit(p,progress) for p in args.workspace]
        print(json.dumps({'policy_version':POLICY,'workspaces':reports}),flush=True)
        return 1 if any(r['status']=='partial' for r in reports) else 0
    except (Exception,KeyboardInterrupt) as exc:
        print(json.dumps({'status':'interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed',
                          'error':str(exc)}),flush=True)
        return 130 if isinstance(exc,KeyboardInterrupt) else 1


if __name__ == '__main__':
    sys.exit(main())

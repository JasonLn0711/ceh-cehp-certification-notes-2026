"""Coursework practice-film package; source/teaching evidence remains course-owned."""
from datetime import datetime, timezone
from pathlib import Path
from .archive_io import verified_stream_archive
from .common import lock, read, sha, write


def package(root, project, emit):
    root=Path(root).resolve();project=Path(project).resolve();output=project.parent/'output'
    archive=output/'third-video-DELIVERY.zip'
    with lock(project/'.production/package.lock'):
        if (root/'validation/delivery-package.json').exists():
            raise RuntimeError('Closed delivery receipt exists; use a new release workspace and content revision')
        report=read(root/'validation/delivery-media.json')
        if report.get('full_decode')!='passed' or report.get('visual_review')!='passed' or len(report['videos'])!=6:
            raise RuntimeError('Six decoded videos and encoded visual review required')
        entries={}
        from .packaging import walk_files
        for name,path in walk_files(root,'review-video-03',{'project','output'}):
            if path==root/'validation/delivery-package.json':continue
            if path.suffix=='.zip' and path.parent!=root/'source':continue
            entries[name]=path
        for name,path in walk_files(project,'review-video-03/project',{'proof'}):
            entries[name]=path
        for video in report['videos']:
            name=video['file']
            if Path(name).name!=name:raise ValueError('Video filename must be a basename')
            path=output/name
            if path.is_symlink() or sha(path)!=video['sha256']:
                raise RuntimeError('Delivery video hash mismatch: '+name)
            entries['review-video-03/output/'+name]=path
        # Ship the exact packaging modules used, without copying the large project.
        source=Path(__file__).parent
        for name in ['practice_package.py','archive_io.py','common.py','packaging.py','progress.py','compact_archive.py','compact_restore.py']:
            entries['review-video-03/engine/ceh_video/'+name]=source/name
        profile=read(project/'production.json') if (project/'production.json').exists() else {}
        writer=verified_stream_archive
        if profile.get('package_format')=='compact-v1':
            from .compact_archive import write_compact
            writer=write_compact
        result=writer([(f,n) for n,f in sorted(entries.items())],archive,emit)
        result.update(file=str(archive),storage_policy=('longform-storage-v2.0.0' if profile.get('package_format')=='compact-v1' else 'longform-storage-v1.0.0'),
                      created_at=datetime.now(timezone.utc).isoformat())
        (output/(archive.name+'.sha256')).write_text(result['sha256']+'  '+archive.name+'\n')
        write(root/'validation/delivery-package.json',result)
        emit({'phase':'package_verified','bytes':result['bytes']})
        return result

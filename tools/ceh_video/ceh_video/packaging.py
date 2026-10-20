"""Manifest-first release ZIP; no copied media staging or generated host trees."""
from pathlib import Path
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import zipfile
from .common import digest, read, sha, write

EXCLUDED = {'.venv', 'node_modules', '.production', '.hyperframes',
            '.waveform-cache', '__pycache__', '.git', 'review'}
DERIVED = ['project/chapters/', 'project/review/', 'project/assets/audio/',
           'qa/remaster-boundaries/hosts/']

def html_identity(file):
    return hashlib.sha256(re.sub(rb' data-hf-id="[^"]*"',b'',Path(file).read_bytes())).hexdigest()


def walk_files(root, prefix, excluded=()):
    root = Path(root)
    for folder, dirs, files in os.walk(root, followlinks=False):
        for name in list(dirs):
            f = Path(folder)/name
            rel = str(f.relative_to(root))
            if name in EXCLUDED or rel in excluded:
                dirs.remove(name)
            elif f.is_symlink():
                raise ValueError('Unregistered directory link: '+str(f))
        for name in sorted(files):
            f = Path(folder)/name
            if name.endswith(('.tmp', '.pyc')) or name in {'AGENTS.md', 'CLAUDE.md'}:
                continue
            if f.is_symlink():
                raise ValueError('Unregistered file link: '+str(f))
            yield prefix+'/'+str(f.relative_to(root)), f


def inventory(p):
    """Read-only. Heavy assets are referenced, never copied to a staging tree."""
    entries = dict(walk_files(p.root, 'project', {'chapters', 'assets/audio', 'vendor'}))
    entries.update(walk_files(p.root.parent/'inputs', 'inputs'))
    from .delivery import export_qa
    for f in p.qa.iterdir():
        if f.is_file() and export_qa(f) and f.name not in {
            'engine-packaging.json', 'engine-extracted-reconstruction.json',
            'run-package.json', 'package-plan.json',
        }:
            entries['qa/'+f.name] = f
    dirs = ['visual', 'remaster-boundaries', 'remaster-assets', 'quiz-divider-negative', 'root-visual-check',
            'audio-audition', 'recognition', 'early-candidate-review-final-freeze']
    dirs += [ch+'-states' for ch in p.chapters]
    for name in dirs:
        root = p.qa/name
        if not root.is_dir():
            continue
        excluded = {'hosts', 'host', 'precheck'}
        if name == 'visual':
            excluded.update(f.name for f in root.iterdir()
                            if f.name.startswith(('attempt-', 'diagnostic-', 'scoped-', 'precheck-')))
        entries.update(walk_files(root, 'qa/'+name, excluded))
    frames = p.output/'inspection_frames'
    if frames.is_dir():
        entries.update(walk_files(frames, 'output/inspection_frames'))
    runs=p.qa/'runs'
    if runs.is_dir():
        for attempt in runs.iterdir():
            if attempt.is_symlink() or not attempt.is_dir():
                raise ValueError('Invalid attempt directory: '+str(attempt))
            # Closed attempt records only: the active delivery log is external,
            # avoiding a circular archive identity while the archive is written.
            if not (attempt/'summary.json').is_file():
                continue
            if read(attempt/'summary.json').get('target')=='package':
                continue
            for f in attempt.iterdir():
                if f.is_file() and (f.name in {'events.jsonl','summary.json','qa-manifest.json','benchmark.json','benchmark.py','run_record.py'} or f.suffix=='.log'):
                    if f.is_symlink():raise ValueError('Attempt symlink: '+str(f))
                    entries['qa/runs/'+attempt.name+'/'+f.name]=f
    source = Path(__file__).parent
    entries.update(walk_files(source, 'project/vendor/ceh_video'))
    entries['project/vendor/pyproject.toml'] = source.parent/'pyproject.toml'
    entries['project/vendor/README.md'] = source.parent/'README.md'
    for name in ('tests','ci'):
        entries.update(walk_files(source.parent/name,'project/vendor/'+name))
    # Hash each physical source once within this inventory, including local hardlinks.
    identities, rows = {}, []
    for name, f in sorted(entries.items()):
        stat = f.stat()
        identity = (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns)
        h = identities.setdefault(identity, None)
        if h is None:
            h = identities[identity] = sha(f)
        rows.append(dict(path=name, source=str(f), bytes=stat.st_size, sha256=h))
    return dict(schema=1, entries=rows, bytes=sum(r['bytes'] for r in rows),
                files=len(rows), excluded=DERIVED,
                manifest_sha256=digest([{k:r[k] for k in ('path','bytes','sha256')} for r in rows]))


def restore_hosts(p):
    """Rebuild omitted host projects from shipped compositions and scene PCM."""
    sys.path[:0] = [str(Path(__file__).parent/'runtime'), str(p.root/'scripts')]
    from build_film import host, write_host
    (p.root/'assets/audio').mkdir(parents=True, exist_ok=True)
    ready = [(s, p.audio(s['id'])) for s in p.scenes]
    (p.root/'index.html').write_text(host(ready, 'master'))
    for ch in p.chapters:
        write_host('chapters/'+ch, host([(s,a) for s,a in ready if s['chapter_id']==ch], ch))
    return {'chapters': len(p.chapters), 'new_inferences': 0, 'tempo_passes': 0}


def package(p, emit):
    from .delivery import audio_restore_manifest, verify_encoded_evidence, verify_golden_review_evidence
    from .review import require_encoded
    assert read(p.qa/'engine-delivery.json')['status'] == 'automated_delivery_checks_passed'
    require_encoded(p)
    plan = inventory(p)
    generated = {
        'project/provenance/audio-restore.json': audio_restore_manifest(p),
        'qa/archive-exclusions.json': {'excluded': DERIVED, 'restore': 'python -m ceh_video restore'},
        'project/provenance/host-restore.json': {
            str(f.relative_to(p.root)):sha(f)
            for f in sorted((p.root/'assets/audio').glob('*.wav'))
            if f.stem=='master' or f.stem in p.chapters
        },
        'project/provenance/host-html-restore.json': {
            str(f.relative_to(p.root)):html_identity(f)
            for f in [p.root/'index.html',*[p.root/'chapters'/ch/'index.html' for ch in p.chapters]]
        },
    }
    review=read(p.qa/'encoded-review.json')
    generated['qa/encoded-frame-manifest.json']={
        'scope':'Exact encoded pictures; full media delivered adjacent to archive',
        'master_sha256':review['master_sha256'],'captures':review['captures'],
        'required_frames':len(review['captures']),
    }
    generated_bytes = {k:(json.dumps(v,indent=2)+'\n').encode() for k,v in generated.items()}
    rows = [r for r in plan['entries'] if r['path'] not in generated_bytes]
    manifest = {r['path']:r['sha256'] for r in rows}
    manifest.update({k:hashlib.sha256(v).hexdigest() for k,v in generated_bytes.items()})
    key = digest({'format':1, 'payloads':manifest, 'implementation':sha(Path(__file__))})
    archive = p.output/p.profile['editable_filename']
    old_path = p.qa/'engine-packaging.json'
    if old_path.exists() and archive.is_file():
        old = read(old_path)
        if old.get('package_key') == key and old.get('sha256') == sha(archive):
            emit({'phase':'package_reused','files':old['files'],'bytes':old['bytes']})
            return old
        raise RuntimeError('Closed release differs; use a new release workspace')
    write(p.qa/'package-plan.json', plan)
    generated_bytes['FILES_SHA256.json'] = (json.dumps(manifest,indent=2)+'\n').encode()
    partial = archive.with_name(archive.name+'.partial-'+uuid.uuid4().hex[:8])
    completed_bytes = 0
    with zipfile.ZipFile(partial,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=1,allowZip64=True) as z:
        for i, row in enumerate(rows,1):
            info = zipfile.ZipInfo('engine_project_source/'+row['path'], date_time=(2026,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info._compresslevel = 1
            h = hashlib.sha256()
            with open(row['source'],'rb') as source, z.open(info,'w',force_zip64=True) as target:
                while block := source.read(1024*1024):
                    h.update(block);target.write(block)
            if h.hexdigest() != row['sha256']:
                raise RuntimeError('Source changed during packaging: '+row['path'])
            completed_bytes += row['bytes']
            if i%100==0 or i==len(rows):
                emit({'phase':'package_bytes','completed':completed_bytes,'total':sum(r['bytes'] for r in rows),'files':i})
        for name, data in sorted(generated_bytes.items()):
            info=zipfile.ZipInfo('engine_project_source/'+name,date_time=(2026,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info._compresslevel=1
            z.writestr(info,data)
    with zipfile.ZipFile(partial) as z, tempfile.TemporaryDirectory(dir=p.qa,prefix='verify-package-') as temp:
        extracted_bytes=sum(info.file_size for info in z.infolist())
        # ZipExtFile checks each member's CRC at EOF during extractall.
        # A separate testzip would inflate every heavy payload a second time.
        z.extractall(temp)
        base=Path(temp)/'engine_project_source'
        for name, expected in manifest.items():
            assert sha(base/name)==expected, name
        picture=verify_encoded_evidence(base)
        golden=verify_golden_review_evidence(base)
        env=os.environ.copy();env['PYTHONPATH']=str(base/'project/vendor')
        env['CEH_VIDEO_PROJECT']=str(base/'project')
        code='from ceh_video.common import Project,project_root; from ceh_video.delivery import restore_packaged_audio_cache; from ceh_video.packaging import restore_hosts; import json; p=Project(project_root()); print(json.dumps(dict(audio=restore_packaged_audio_cache(p),hosts=restore_hosts(p))))'
        restored=json.loads(subprocess.check_output([sys.executable,'-c',code],cwd=base,env=env,text=True))
        assert restored['audio']['clips']==sum(p.audio(s['id'])['sentence_count'] for s in p.scenes)
        assert restored['audio']['new_inferences']==restored['audio']['tempo_passes']==0
        host_hashes=generated['project/provenance/host-restore.json']
        assert set(host_hashes)=={'assets/audio/'+ch+'.wav' for ch in ['master',*p.chapters]}
        for rel,expected in host_hashes.items():
            assert sha(base/'project'/rel)==expected, 'Restored host PCM differs: '+rel
        restored['hosts']['pcm_hashes_verified']=len(host_hashes)
        for rel,expected in generated['project/provenance/host-html-restore.json'].items():
            assert html_identity(base/'project'/rel)==expected, 'Restored host composition differs: '+rel
        restored['hosts']['html_identities_verified']=len(generated['project/provenance/host-html-restore.json'])
        write(p.qa/'engine-extracted-reconstruction.json',restored)
    os.replace(partial,archive)
    receipt=dict(status='crc_extraction_hashes_verified',package_key=key,files=len(manifest)+1,
                 payload_hashes=len(manifest),bytes=archive.stat().st_size,sha256=sha(archive),
                 archive=archive.name,encoded_picture_evidence=picture,golden_review_evidence=golden,
                 human_listening='pending',source_bytes=plan['bytes'],media_staging_bytes=0)
    receipt['verification_extraction_bytes']=extracted_bytes
    write(old_path,receipt)
    return receipt

"""Bounded archive inventory; extracted releases and test environments stay outside."""
from pathlib import Path
import os

EXCLUDED = {'.venv', 'node_modules', '__pycache__', '.hyperframes', '.waveform-cache', 'archive-verification', 'portability', 'python-env', '.git'}

def walk_files(root):
    root = Path(root)
    for folder, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED
                         and not d.startswith('verify-package-'))
        for d in dirs:
            if (Path(folder)/d).is_symlink():
                raise ValueError('Unregistered archive directory link: '+str(Path(folder)/d))
        for name in sorted(names):
            p = Path(folder)/name
            if p.is_symlink():
                raise ValueError('Unregistered archive file link: '+str(p))
            if p.is_file():
                yield p

def payload_files(p):
    files = []
    for f in walk_files(p.root):
        rel = f.relative_to(p.root)
        if '.production' in rel.parts and (len(rel.parts)<2 or rel.parts[1]!='speech-cache'): continue
        if 'chapters' in rel.parts or f.suffix in {'.log','.tmp','.pyc'}: continue
        files.append((f, 'project/'+str(rel)))
    for f in walk_files(p.output):
        rel = f.relative_to(p.output)
        media = f.suffix in {'.mp4','.wav','.srt','.vtt','.pptx','.pdf','.md'}
        review = 'inspection_frames' in rel.parts and f.suffix in {'.png','.jpg'}
        if media or review: files.append((f,'output/'+str(rel)))
    for f in walk_files(p.qa):
        if f.suffix not in {'.json','.jpg','.png','.html'} or 'tts-fixture' in f.parts: continue
        if f.name in {'engine-packaging.json'} or f.name.startswith('master.decoded'): continue
        files.append((f,'qa/'+str(f.relative_to(p.qa))))
    assert len({rel for _,rel in files})==len(files)
    return files

def source_inputs(p):
    """Authored package-only inputs, independent of generated QA and extraction output."""
    from .common import sha
    root = p.root
    paths = set(root.glob('*.md')) | set(root.glob('*.lock'))
    paths.update(root/f for f in ['package.json','package-lock.json','production.json','pronunciation.json'])
    paths.update(root/'data'/f for f in ['scenes.json','questions.json','chapters.json','coverage.json','coverage-contract.json'])
    if getattr(p,'profile',{}).get('teaching_panels'):
        paths.update([root/p.profile['teaching_panels'],root/'data/teaching-assets.json'])
        paths.update(walk_files(root/'assets/teaching'))
    for rel in ['assets/licenses','assets/registry','scripts']:
        if (root/rel).exists(): paths.update(walk_files(root/rel))
    return {str(f.relative_to(root)):sha(f) for f in sorted(paths) if f.is_file()}


def release_files(p):
    """Reference current engine files directly; do not populate project/vendor."""
    from .packaging import walk_files as engine_files
    files = {rel: f for f, rel in payload_files(p)
             if not rel.startswith('project/vendor/')}
    source = Path(__file__).parents[1]
    files.update(engine_files(source/'ceh_video', 'project/vendor/ceh_video/ceh_video'))
    files['project/vendor/ceh_video/pyproject.toml'] = source/'pyproject.toml'
    return [(f, rel) for rel, f in sorted(files.items())]


def package(p, emit):
    """Stream, extract once with CRC, hash, then promote; retain no full copy."""
    import hashlib
    import shutil
    import tempfile
    import zipfile
    from datetime import datetime, timezone
    from .archive_io import partial_archive
    from .common import read, write, sha
    from .mandarin_policy import archive_prefix
    from .review import require_encoded

    require_encoded(p)
    delivery = read(p.qa/'engine-delivery.json')
    if delivery.get('status') != 'rendered_automated_checks_passed':
        raise RuntimeError('Current automated delivery checks required')
    if delivery['master_sha256'] != sha(p.output/p.profile['master_filename']):
        raise RuntimeError('Delivery master hash mismatch')
    target = p.output/p.profile['editable_filename']
    if target.parent != p.output or target.is_symlink():
        raise ValueError('Archive must be a direct output file')
    # Closed releases are immutable. A new archive needs a new workspace.
    if target.exists() or (p.qa/'engine-packaging.json').exists():
        raise RuntimeError('Closed release exists; use a new release workspace')
    files = release_files(p)
    if p.profile.get('package_format') == 'compact-v1':
        from .compact_archive import write_compact
        result = write_compact([(f, archive_prefix(p.profile)+rel) for f,rel in files], target, emit)
        result.update(status='compact_restore_all_payload_hashes_passed',
                      storage_policy='longform-storage-v2.0.0', zip=str(target),
                      zip_sha256=result['sha256'], created_at=datetime.now(timezone.utc).isoformat(),
                      human_acceptance='pending')
        write(p.qa/'engine-packaging.json', result)
        return result
    source_bytes = sum(f.stat().st_size for f, _ in files)
    reserve = 128*1024*1024
    required = 2*source_bytes + reserve
    free = shutil.disk_usage(p.output).free
    emit({'phase':'package_capacity', 'source_bytes':source_bytes,
          'required_free_bytes':required, 'free_bytes':free})
    if free < required:
        raise RuntimeError(f'Insufficient package scratch space: need {required} bytes; have {free}')
    manifest = {rel:sha(f) for f, rel in files}
    prefix = archive_prefix(p.profile)
    completed = 0
    with partial_archive(target) as partial:
        with zipfile.ZipFile(partial, 'w', zipfile.ZIP_DEFLATED, compresslevel=1,
                             allowZip64=True) as archive:
            for i, (f, rel) in enumerate(files, 1):
                info = zipfile.ZipInfo(prefix+rel, date_time=(2026,1,1,0,0,0))
                info.compress_type = (zipfile.ZIP_STORED if f.suffix.lower() in
                                      {'.mp4','.mp3','.png','.jpg','.jpeg','.pptx','.pdf','.zip'}
                                      else zipfile.ZIP_DEFLATED)
                info._compresslevel = 1
                observed = hashlib.sha256()
                with f.open('rb') as src, archive.open(info,'w',force_zip64=True) as dst:
                    while block := src.read(1024*1024):
                        observed.update(block); dst.write(block); completed += len(block)
                if observed.hexdigest() != manifest[rel]:
                    raise RuntimeError('Source changed during packaging: '+rel)
                if i%100==0 or i==len(files):
                    emit({'phase':'package_bytes','completed':completed,
                          'total':source_bytes,'files':i})
            manifest_text = ''.join(f'{h}  {rel}\n' for rel,h in sorted(manifest.items()))
            archive.writestr(prefix+'FILES_SHA256.txt', manifest_text)
        with tempfile.TemporaryDirectory(dir=p.output, prefix='verify-package-') as temp:
            with zipfile.ZipFile(partial) as archive:
                # Extraction reads every member to EOF and verifies its CRC.
                archive.extractall(temp)
            extracted = Path(temp)/prefix
            for i,(rel,h) in enumerate(manifest.items(),1):
                if sha(extracted/rel) != h:
                    raise RuntimeError('Extracted payload differs: '+rel)
                if i%100==0 or i==len(manifest):
                    emit({'phase':'archive_extraction_hash','completed':i,'total':len(manifest)})
            if (extracted/'FILES_SHA256.txt').read_text() != manifest_text:
                raise RuntimeError('Extracted manifest differs')
        archive_hash = sha(partial)
        archive_bytes = partial.stat().st_size
        partial.replace(target)
    receipt = {'status':'crc_extraction_and_all_payload_hashes_passed',
               'storage_policy':'longform-storage-v1.0.0',
               'created_at':datetime.now(timezone.utc).isoformat(),
               'zip':str(target),'zip_sha256':archive_hash,'bytes':archive_bytes,
               'entries':len(files)+1,'verified_payloads':len(files),
               'source_bytes':source_bytes,'media_staging_bytes':0,
               'verification_extraction_bytes':source_bytes+len(manifest_text.encode()),
               'verification_workspace_retained':False,
               'private_assessment_included':False,'human_acceptance':'pending'}
    write(p.qa/'engine-packaging.json', receipt)
    emit({'phase':'package_verified','bytes':archive_bytes,
          'verification_workspace_retained':False})
    return receipt

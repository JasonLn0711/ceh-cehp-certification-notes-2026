"""Bounded archive inventory; extracted releases and test environments stay outside."""
from pathlib import Path
import os

EXCLUDED = {'.venv', 'node_modules', '__pycache__', '.hyperframes', '.waveform-cache', 'archive-verification', 'portability', 'python-env'}

def walk_files(root):
    root = Path(root)
    for folder, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED)
        for name in sorted(names):
            p = Path(folder)/name
            if p.is_file() and not p.is_symlink():
                yield p

def payload_files(p):
    files = []
    for f in walk_files(p.root):
        rel = f.relative_to(p.root)
        if '.production' in rel.parts and (len(rel.parts)<2 or rel.parts[1]!='speech-cache'): continue
        if 'chapters' in rel.parts or f.suffix in {'.log','.tmp'}: continue
        files.append((f, 'project/'+str(rel)))
    for f in walk_files(p.output):
        rel = f.relative_to(p.output)
        media = f.suffix in {'.mp4','.wav','.srt','.vtt','.pptx','.md'}
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
    for rel in ['assets/licenses','assets/registry','scripts']:
        if (root/rel).exists(): paths.update(walk_files(root/rel))
    return {str(f.relative_to(root)):sha(f) for f in sorted(paths) if f.is_file()}

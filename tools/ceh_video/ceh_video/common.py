"""Project contracts, exact identities and atomic receipts."""
from pathlib import Path
import contextlib, fcntl, hashlib, json, os, re, tempfile


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def sha(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name+'.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(value, stream, indent=2); stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp): os.unlink(temp)


@contextlib.contextmanager
def lock(path):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a') as stream:
        try: fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: raise RuntimeError('Already running: '+str(path))
        try: yield
        finally: fcntl.flock(stream, fcntl.LOCK_UN)


def project_root():
    return Path(os.environ['CEH_VIDEO_PROJECT']).resolve()


class Project:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.profile = read(self.root/'production.json')
        self.qa = self.root.parent/'qa'; self.output = self.root.parent/'output'
        self.state = self.root/'.production'; self.scenes = read(self.root/'data/scenes.json')['scenes']
        self.questions = read(self.root/'data/questions.json')['questions']
        self.chapters = list(dict.fromkeys(s['chapter_id'] for s in self.scenes))
        self.by_id = {s['id']: s for s in self.scenes}

    def audio(self, sid): return read(self.root/'data'/f'{sid}.audio.json')
    def chapter_scenes(self, ch): return [s for s in self.scenes if s['chapter_id'] == ch]
    def quiz_scenes(self): return set(q['scene_id'] for q in self.questions)
    def file_hashes(self, paths):
        return {str(p.relative_to(self.root)): sha(p) for p in sorted(set(map(Path, paths)))}

    def chapter_inputs(self, ch):
        """Explicit render inputs; preview caches and arbitrary directory files are excluded."""
        folder = self.root/'chapters'/ch
        files = [folder/'index.html', folder/'hyperframes.json']
        for s in self.chapter_scenes(ch):
            files += [folder/'compositions'/f'{s["id"]}.html', folder/'compositions'/f'{s["id"]}.motion.json']
        files += [p for p in (folder/'assets').rglob('*') if p.is_file()]
        result = {}
        for f in sorted(files):
            b = f.read_bytes()
            if f.suffix == '.html': b = re.sub(rb' data-hf-id="[^"]*"', b'', b)
            result[str(f.relative_to(folder))] = hashlib.sha256(b).hexdigest()
        return digest({'files': result, 'renderer': self.profile['runtime']['hyperframes'], 'encoding': self.profile['output']})

    def environment(self):
        env = os.environ.copy()
        env.update(CEH_VIDEO_PROJECT=str(self.root), PYTHONUNBUFFERED='1', OMP_NUM_THREADS='4', OMP_WAIT_POLICY='PASSIVE')
        env['PYTHONPATH'] = str(Path(__file__).parents[1])+os.pathsep+env.get('PYTHONPATH', '')
        if hasattr(self,'run_record'):env['CEH_RUN_ID']=self.run_record.id
        env['HYPERFRAMES_BROWSER_PATH'] = self.profile['runtime']['browser']
        if 'browser_gpu_mode' in self.profile['runtime']:env['PRODUCER_BROWSER_GPU_MODE']=self.profile['runtime']['browser_gpu_mode']
        return env

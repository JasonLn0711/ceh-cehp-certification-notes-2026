"""Verified cache hits must not load or require an alignment model."""
import hashlib,json,os,runpy,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch

class AlignmentCacheStartupTests(unittest.TestCase):
    def test_complete_verified_cache_works_without_whisper_import(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'data/forced-alignment').mkdir(parents=True)
            wave=root/'clip.wav';wave.write_bytes(b'identity-only cached fixture')
            digest=hashlib.sha256(wave.read_bytes()).hexdigest()
            (root/'data/scenes.json').write_text(json.dumps({'scenes':[{'id':'S01'}]}))
            segment={'kind':'spoken','sentence':0,'path':'clip.wav','canonical':'Hello.','spoken':'Hello.'}
            (root/'data/S01.audio.json').write_text(json.dumps({'segments':[segment]}))
            cached=root/'data/forced-alignment/S01-000.json'
            cached.write_text(json.dumps({'audio_sha256':digest,'recipe':'base.en-int8-forced-dtw-v1','canonical':'Hello.','spoken':'Hello.'}))
            before=cached.read_bytes()
            with patch.dict(os.environ,{'CEH_VIDEO_PROJECT':str(root)}),patch.dict(sys.modules,{'faster_whisper':None}),patch.object(sys,'argv',['force_align.py','--scene','S01']):
                script=Path(__file__).parents[1]/'ceh_video/runtime/force_align.py'
                runpy.run_path(str(script),run_name='__main__')
            self.assertEqual(cached.read_bytes(),before)

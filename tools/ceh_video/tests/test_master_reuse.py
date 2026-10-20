"""Real assembly subprocess verifies no-write reuse, force and invalidation."""
import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path
import numpy as np
import soundfile as sf
from ceh_video.common import write, sha

class MasterReuseIntegration(unittest.TestCase):
    def test_same_inputs_skip_assembly_but_force_and_changes_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/'project';qa=base/'qa';out=base/'output'
            for folder in [root/'data',root/'assets/voice',root/'assets/audio',out/'chapters',qa]:folder.mkdir(parents=True)
            write(root/'production.json',{'title':'Fixture','master_filename':'fixture.mp4','audio_policy':'ceh-en-v1.2'})
            write(root/'data/scenes.json',{'scenes':[]});write(root/'data/questions.json',{'questions':[]})
            pcm=np.repeat((np.sin(np.arange(48000)*2*np.pi*440/48000)*4000).astype('int16')[:,None],2,axis=1)
            sf.write(root/'assets/voice/S01.wav',pcm,48000,subtype='PCM_16')
            subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=white:s=64x64:r=30:d=1','-c:v','libx264','-pix_fmt','yuv420p',str(out/'chapters/C01.mp4')],check=True)
            write(root/'data/master-timing.json',{'scenes':[{'scene':'S01'}],'chapters':[{'id':'C01','title':'First','start':0,'duration':1,'start_sample':0,'duration_samples':48000}],'samples':48000,'frames':30,'duration':1})
            script=Path(__file__).parents[1]/'ceh_video/runtime/assemble_master.py'
            def run(*args):return subprocess.run([sys.executable,str(script),*args],env=dict(os.environ,CEH_VIDEO_PROJECT=str(root)),check=True,capture_output=True,text=True)
            run();movie=out/'fixture.mp4';scan=qa/'master-full-decode.log'
            before=(movie.stat().st_mtime_ns,scan.stat().st_mtime_ns,sha(movie))
            result=run()
            self.assertEqual((movie.stat().st_mtime_ns,scan.stat().st_mtime_ns,sha(movie)),before)
            self.assertIn('verified_master_reused',result.stdout)
            run('--force');self.assertNotEqual(scan.stat().st_mtime_ns,before[1])
            pcm[2000:2500]*=-1;sf.write(root/'assets/voice/S01.wav',pcm,48000,subtype='PCM_16')
            changed=run();self.assertNotIn('verified_master_reused',changed.stdout)
            actual,_=sf.read(out/'master.reference.pcm.wav',dtype='int16',always_2d=True);np.testing.assert_array_equal(actual,pcm)
            movie.write_bytes(b'corrupt');self.assertNotIn('verified_master_reused',run().stdout)
            scan.unlink();self.assertNotIn('verified_master_reused',run().stdout)
            # A failed forced attempt cannot leave its predecessor's success receipt.
            (out/'chapters/C01.mp4').write_bytes(b'corrupt chapter')
            with self.assertRaises(subprocess.CalledProcessError):run('--force')
            self.assertFalse((root/'.production/master-reuse.json').exists())

    def test_runner_forwards_explicit_force(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        from ceh_video.runner import action
        from ceh_video.graph import Node
        p=SimpleNamespace(profile={'schema_version':1,'audio_policy':'ceh-en-v1.2'})
        node=Node('master',[],{},[],['assemble_master'])
        with patch('ceh_video.runner.worker') as worker:
            action(p,node,lambda row:None,True)
            self.assertEqual(worker.call_args.args[1:3],('assemble_master',['--force']))

if __name__=='__main__':unittest.main()

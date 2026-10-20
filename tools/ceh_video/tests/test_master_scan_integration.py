"""Small real assembly, not a claim of full M10 production acceptance."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import numpy as np
import soundfile as sf
from ceh_video.common import write
from ceh_video.media_scan import require_scan

class MasterScanIntegration(unittest.TestCase):
    def test_actual_assembly_retains_pcm_chapters_and_decode_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/'project';qa=base/'qa';out=base/'output'
            for folder in (root/'data',root/'assets/voice',root/'assets/audio',qa,out/'chapters'):
                folder.mkdir(parents=True,exist_ok=True)
            write(root/'production.json',{'title':'Fixture','master_filename':'fixture.mp4'})
            write(root/'data/scenes.json',{'scenes':[]});write(root/'data/questions.json',{'questions':[]})
            scenes=[];chapters=[];pieces=[]
            for i,color in enumerate(('white','red')):
                sid=f'S{i+1:02}';ch=f'C{i+1:02}'
                pcm=np.repeat((np.sin(np.arange(48000)*2*np.pi*440/48000)*4000).astype('int16')[:,None],2,axis=1)
                sf.write(root/'assets/voice'/f'{sid}.wav',pcm,48000,subtype='PCM_16');pieces.append(pcm)
                subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color={color}:s=64x64:r=30:d=1','-c:v','libx264','-pix_fmt','yuv420p',str(out/'chapters'/f'{ch}.mp4')],check=True)
                scenes.append({'scene':sid});chapters.append({'id':ch,'title':ch,'start':i,'duration':1,'start_sample':i*48000,'duration_samples':48000})
            write(root/'data/master-timing.json',{'scenes':scenes,'chapters':chapters,'frames':60,'samples':96000,'duration':2})
            env=dict(os.environ,CEH_VIDEO_PROJECT=str(root))
            script=Path(__file__).parents[1]/'ceh_video/runtime/assemble_master.py'
            subprocess.run([sys.executable,str(script)],env=env,check=True,capture_output=True,text=True)
            probe=json.loads((qa/'master-ffprobe.json').read_text())
            video=next(s for s in probe['streams'] if s['codec_type']=='video')
            self.assertEqual(int(video['nb_read_frames']),60);self.assertEqual(len(probe['chapters']),2)
            self.assertEqual(probe['ceh_frame_count_evidence']['method'],'ffmpeg_full_decode_progress')
            actual,sr=sf.read(out/'master.reference.pcm.wav',dtype='int16',always_2d=True)
            np.testing.assert_array_equal(actual,np.concatenate(pieces));self.assertEqual(sr,48000)
            before=(qa/'master-full-decode.log').stat().st_mtime_ns
            self.assertEqual(require_scan(out/'fixture.mp4',60,qa)['decoded_frames'],60)
            self.assertEqual((qa/'master-full-decode.log').stat().st_mtime_ns,before)
            timings=json.loads((qa/'master-stage-timing.json').read_text())
            self.assertEqual(len(timings['stages']),7)
            self.assertTrue(all(r['status']=='completed' and r['elapsed_seconds']>=0 for r in timings['stages']))
            def decoded_audio():
                return subprocess.check_output(['ffmpeg','-v','error','-i',str(out/'fixture.mp4'),'-map','0:a:0','-f','f32le','-'])
            baseline=decoded_audio()
            self.assertFalse(json.loads((qa/'master-audio-cache.json').read_text())['reused'])
            cache_file=next((root/'.production/master-audio').glob('*.m4a'))
            cache_probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_chapters','-of','json',str(cache_file)]))
            self.assertEqual(cache_probe['chapters'],[])
            self.assertEqual([s['codec_type'] for s in cache_probe['streams']],['audio'])
            subprocess.run([sys.executable,str(script)],env=env,check=True,capture_output=True,text=True)
            self.assertTrue(json.loads((qa/'master-audio-cache.json').read_text())['reused'])
            self.assertEqual(decoded_audio(),baseline)
            self.assertEqual(require_scan(out/'fixture.mp4',60,qa)['decoded_frames'],60)

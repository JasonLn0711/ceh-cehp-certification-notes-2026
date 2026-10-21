import unittest,tempfile,json
from pathlib import Path
from types import SimpleNamespace
from ceh_video.mandarin_panels import cue_time,image_box,layout_objects
class PanelContracts(unittest.TestCase):
 def test_word_boundary_not_character_rate(self):
  with tempfile.TemporaryDirectory() as folder:
   root=Path(folder);(root/'data/forced-alignment').mkdir(parents=True)
   (root/'data/forced-alignment/S01-000.json').write_text(json.dumps({'words':[{'text':'先看','start':.2},{'text':'目標','start':3.7}]}))
   p=SimpleNamespace(root=root);audio={'segments':[{'kind':'spoken','canonical':'先看目標','sentence':0,'start_sample':48000}]}
   self.assertAlmostEqual(cue_time(p,'S01',audio,'目標'),4.7)
   with self.assertRaises(ValueError):cue_time(p,'S01',audio,'不存在')
 def test_contain_box_portrait(self):
  with tempfile.TemporaryDirectory() as folder:
   f=Path(folder)/'portrait.svg';f.write_text('<svg viewBox="0 0 100 200"/>')
   self.assertEqual(image_box(f),(162.5,55,125,250))
 def test_main_panel_clearance(self):
  o={'kind':'rect','x':190,'y':290,'w':1320,'h':350}
  changed=layout_objects([o])[0]
  self.assertLess(changed['x']+changed['w'],1340)
  self.assertEqual(o['w'],1320)
if __name__=='__main__':unittest.main()

class GPUContracts(unittest.TestCase):
 def test_requires_actual_hardware_and_nvenc(self):
  from ceh_video.mandarin import verify_gpu
  with tempfile.TemporaryDirectory() as folder:
   log=Path(folder)/'render.log';renderer='ANGLE (NVIDIA Corporation, NVIDIA GB10/PCIe, OpenGL ES 3.2)'
   p=SimpleNamespace(profile={'runtime':{'gpu_encoding':True,'expected_gpu_renderer':renderer}})
   good=f'browserGpuMode probe → hardware (WebGL renderer vendor="NVIDIA" renderer="{renderer}")'
   probe={'streams':[{'codec_type':'video','tags':{'encoder':'Lavc h264_nvenc'}}]}
   log.write_text(good);self.assertEqual(verify_gpu(p,log,probe)['encoding'],'h264_nvenc')
   log.write_text(good+'\nNo GPU encoder works on this machine; encoding with libx264.')
   with self.assertRaises(AssertionError):verify_gpu(p,log,probe)
   log.write_text(good.replace('→ hardware','→ software'))
   with self.assertRaises(AssertionError):verify_gpu(p,log,probe)
   log.write_text(good)
   with self.assertRaises(AssertionError):verify_gpu(p,log,{'streams':[{'codec_type':'video','tags':{'encoder':'Lavc libx264'}}]})

import unittest
from ceh_video.audio_policy import timing,CURRENT,LEGACY
from ceh_video.preflight import validate_profile

class TimingTests(unittest.TestCase):
    def profile(self):
        return dict(schema_version=1,audio_policy='ceh-en-v1.1',voice=dict(name='af_heart',language='en-us',baseline_speed=.73,atempo=1.4,speed_applications=1),output=dict(width=1920,height=1080,fps=30,sample_rate=48000,channels=2,video_rate=1.,bgm=False),quiz_silence_seconds=1,runtime=dict(max_chapter_renders=2,render_workers=4))
    def test_exact_frames(self):
        p=self.profile();validate_profile(p);t=timing(p)
        self.assertEqual([t[k] for k in ('opening','gap','ending','quiz')],[14400,9600,24000,48000])
        self.assertEqual(t['quiz']*8,384000)
        self.assertEqual(t['sample_rate']//t['fps'],1600)
    def test_no_double_processing(self):
        for speed,applications in [(1.5,1),(1.4,2)]:
            p=self.profile();p['voice'].update(atempo=speed,speed_applications=applications)
            with self.assertRaises(AssertionError):validate_profile(p)
    def test_language_scope_and_unknown_fail(self):
        p=self.profile();p['schema_version']=2
        with self.assertRaises(ValueError):timing(p)
        p=self.profile();p['audio_policy']='unknown'
        with self.assertRaises(ValueError):timing(p)
    def test_explicit_legacy_compatibility(self):
        p=self.profile();p.pop('audio_policy');p['voice']['atempo']=1.5
        self.assertEqual(timing(p),LEGACY)

class PCMIntegrationTests(unittest.TestCase):
    """Real atempo/PCM fixture. Optional scientific runtime required, no model inference."""
    policy_id='ceh-en-v1.1'
    def test_eight_exact_holds_and_tamper(self):
        try:
            import numpy as np
            import soundfile as sf
        except ImportError:self.skipTest('Run with the production Python runtime for real PCM validation')
        import tempfile
        from pathlib import Path
        from ceh_video.common import Project,write,sha
        from ceh_video.speech import baseline_entry,baseline_recipe,synthesize,recipe,cache_entry,valid_cache
        from ceh_video.engineering import verify_audio
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'project';root.mkdir();(root/'data').mkdir()
            profile=TimingTests().profile();profile.update(models={},audio_policy=self.policy_id);profile['runtime']['ffmpeg']='fixture-installed'
            write(root/'production.json',profile);write(root/'pronunciation.json',dict(spell=[],pronunciations={}))
            text='Question. A. Alpha. B. Beta. C. Gamma. D. Delta.'
            scenes=[dict(id=f'S{i:02}',chapter_id='C01',audio_segments=[dict(kind='spoken',text=text),dict(kind='silence'),dict(kind='spoken',text='Answer explained.')]) for i in range(1,9)]
            write(root/'data/scenes.json',dict(scenes=scenes));write(root/'data/questions.json',dict(questions=[dict(scene_id=s['id'],choices=[dict(text=x) for x in ['Alpha.','Beta.','Gamma.','Delta.']]) for s in scenes]))
            p=Project(root)
            from ceh_video.speech import sentences
            for t in sentences(text)+['Answer explained.']:
                folder=baseline_entry(p,t);folder.mkdir(parents=True,exist_ok=True)
                sf.write(folder/'baseline.wav',np.sin(np.arange(12000)*.1)*.1,24000,subtype='PCM_16')
                write(folder/'receipt.json',dict(recipe=baseline_recipe(p,t),sha256=sha(folder/'baseline.wav'),origin='controlled_tone_fixture'))
            for scene in scenes:self.assertEqual(synthesize(p,scene['id'])['generated'],0)
            result=verify_audio(p);self.assertEqual(sum(h['frames'] for h in result['silent_intervals']),384000)
            self.assertTrue(valid_cache(p,'Answer explained.'))
            old=cache_entry(p,'Answer explained.');p.profile['voice']['atempo']=1.5;p.profile.pop('audio_policy')
            self.assertNotEqual(old,cache_entry(p,'Answer explained.'));self.assertFalse(valid_cache(p,'Answer explained.'))
            p.profile['voice']['atempo']=1.4;p.profile['audio_policy']=self.policy_id
            a=p.audio('S01');f=root/'assets/voice/S01.wav';pcm,rate=sf.read(f,dtype='int16',always_2d=True)
            speech=next(x for x in a['segments'] if x['kind']=='spoken')
            changed=pcm.copy();changed[speech['start_sample'],0]+=1;sf.write(f,changed,rate,subtype='PCM_16')
            with self.assertRaises(AssertionError):verify_audio(p,reference_track=False)
            h=next(x for x in a['segments'] if x['kind']=='silence');pcm[h['start_sample'],0]=1;sf.write(f,pcm,rate,subtype='PCM_16')
            with self.assertRaises(AssertionError):verify_audio(p,reference_track=False)

class V12PCMIntegrationTests(PCMIntegrationTests):
    policy_id='ceh-en-v1.2'

class VisualGateTests(unittest.TestCase):
    def test_new_scene_cannot_inherit_legacy_or_stale_evidence(self):
        import tempfile
        from pathlib import Path
        from types import SimpleNamespace
        from ceh_video.common import write,sha
        from ceh_video.visual_gate import require_visual
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'compositions').mkdir();f=root/'compositions/S23.html';f.write_text('new scene')
            p=SimpleNamespace(root=root,qa=root/'qa',profile={'audio_policy':'ceh-en-v1.1'})
            with self.assertRaises(RuntimeError):require_visual(p,['S23'])
            (root/'data').mkdir();write(root/'data/S23.audio.json',{})
            visual=Path(__file__).parents[1]/'ceh_video/visual'
            report=dict(geometrySha256=sha(visual/'geometry.mjs'),qaScriptSha256=sha(visual/'qa.mjs'),environment={'tokens':sha(visual/'tokens.v1.1.json'),'lock':sha(visual/'package-lock.json')},audioSources={'S23':sha(root/'data/S23.audio.json')},status='passed',failures=[],exceptions=[],sources={'S23':sha(f)},rows=[dict(name='S23-0',golden_pixels=0,seek_pixels=0)])
            write(p.qa/'visual/scenes/manifest.json',report)
            write(p.qa/'all-text-geometry/report.json',dict(geometrySha256=sha(visual/'geometry.mjs'),validatorSha256=sha(visual/'all-text-geometry.mjs'),tokensSha256=sha(visual/'tokens.v1.1.json'),status='passed',rows=[dict(scene='S23',errors=[],exceptions=[],source_sha256=sha(f))]))
            require_visual(p,['S23'])
            f.write_text('changed')
            with self.assertRaises(RuntimeError):require_visual(p,['S23'])
            report['sources']['S23']=sha(f);report['exceptions']=['LEGACY-M10-SUBTITLE-001'];write(p.qa/'visual/scenes/manifest.json',report)
            with self.assertRaises(RuntimeError):require_visual(p,['S23'])

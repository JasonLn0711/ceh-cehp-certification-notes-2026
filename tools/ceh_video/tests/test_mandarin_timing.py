"""Offline PCM evidence for legacy and concepts timing, with no provider calls."""
import tempfile, unittest
from pathlib import Path
from unittest.mock import patch
from ceh_video.common import Project, write, read
from ceh_video.mandarin import validate_profile
from ceh_video.mandarin_policy import timing, chapter_gap_rows, archive_prefix, deck_filename
from ceh_video.mandarin_speech import synthesize
from test_mandarin import profile

class TimingTests(unittest.TestCase):
    def test_explicit_profile_version_and_legacy_defaults(self):
        p=profile();self.assertEqual(timing(p)['quiz_samples'],48000)
        self.assertEqual(timing(p)['opening_samples'],24000)
        self.assertEqual(timing(p)['tail_samples'],144000)
        p['quiz_silence_seconds']=.45
        with self.assertRaises(AssertionError):validate_profile(p)
        p['audio_policy']='zh-TW-concepts-v2';validate_profile(p)
        self.assertEqual(timing(p)['quiz_samples'],21600)
    def test_delivery_names_default_and_custom(self):
        self.assertEqual(deck_filename({}),'Digital_Everyday_Masterclass_zh-TW_EDITABLE.pptx')
        self.assertEqual(archive_prefix({'archive_prefix':'Island_v1/'}),'Island_v1/')
        with self.assertRaises(AssertionError):archive_prefix({'archive_prefix':'../escape'})
    def test_actual_pcm_hold_and_chapter_padding_for_both_versions(self):
        import numpy as np, soundfile as sf
        for modern in (False,True):
            with self.subTest(modern=modern),tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)/'project';d=profile()
                if modern:d.update(audio_policy='zh-TW-concepts-v2',quiz_silence_seconds=.45)
                write(root/'production.json',d)
                scenes=[{'id':sid,'chapter_id':ch,'audio_segments':[{'kind':'spoken','text':'選項。'},{'kind':'silence'},{'kind':'spoken','text':'答案。'}]} for sid,ch in [('S1','C1'),('S2','C2')]]
                write(root/'data/scenes.json',{'scenes':scenes});write(root/'data/questions.json',{'questions':[]})
                write(root/'pronunciation.json',{});p=Project(root);cache=root/'fixture';cache.mkdir()
                # Deliberately non-frame-aligned clip length exercises padding.
                pcm=np.full((5003,2),1000,dtype='int16')
                for name in ('processed.wav','baseline.wav'):sf.write(cache/name,pcm,48000,subtype='PCM_16')
                write(cache/'metadata.json',{'baseline_seconds':len(pcm)/48000})
                write(cache/'boundaries.json',{'recipe':'fixture','words':[]})
                with patch('ceh_video.mandarin_speech.cache_entry',return_value=cache),patch('ceh_video.mandarin_speech.valid_cache',return_value=True):
                    for scene in scenes:synthesize(p,scene['id'])
                a=p.audio('S1');track,sr=sf.read(root/'assets/voice/S1.wav',dtype='int16',always_2d=True)
                before,hold,after=a['segments'];n=21600 if modern else 48000
                self.assertEqual(before['end_sample'],hold['start_sample'])
                self.assertEqual(hold['end_sample'],after['start_sample'])
                self.assertEqual(hold['end_sample']-hold['start_sample'],n)
                self.assertFalse(np.any(track[hold['start_sample']:hold['end_sample']]))
                self.assertEqual(a['samples']%1600,0)
                self.assertEqual(before['start_sample'],4800 if modern else 24000)
                self.assertEqual(a['tail_samples'],16800 if modern else 144000)
                gaps=chapter_gap_rows(p)
                if modern:self.assertTrue(21600<=gaps[0]['added_silence_samples']<23200)
                else:self.assertTrue(168000<=gaps[0]['added_silence_samples']<169600)

if __name__=='__main__':unittest.main()

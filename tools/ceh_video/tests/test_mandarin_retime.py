import unittest
import numpy as np
from ceh_video.mandarin_speech import quiet_tail_window, align_events
from ceh_video.mandarin import validate_profile
from ceh_video.mandarin_policy import timing
from test_mandarin import profile

class RetimeTests(unittest.TestCase):
    def test_preserves_signal_after_last_provider_word(self):
        pcm=np.zeros((96000,2),dtype='int16');pcm[:48000]=100;pcm[70000]=100
        events=[{'text':'字','offset':0,'duration':10000000}]
        end=quiet_tail_window(pcm,48000,events,{'threshold_pcm16':32,'retain_seconds':.18})
        self.assertEqual(end,70001+8640)
        self.assertTrue(np.array_equal(pcm[:70001],pcm[:end][:70001]))
    def test_provider_boundary_guards_low_level_word(self):
        pcm=np.zeros((96000,2),dtype='int16');pcm[:10000]=100
        events=[{'text':'字','offset':0,'duration':15000000}]
        self.assertEqual(quiet_tail_window(pcm,48000,events,{'threshold_pcm16':32,'retain_seconds':.18}),72000+8640)
        self.assertEqual(quiet_tail_window(pcm,48000,events,None),96000)
    def test_new_rate_maps_real_boundaries_and_preserves_text(self):
        events=[{'text':'資料','offset':1300000,'duration':13000000}]
        words=align_events('資料。',events,2,rate=1.3)
        self.assertAlmostEqual(words[0]['start'],.1)
        self.assertAlmostEqual(words[0]['end'],1.1)
        self.assertEqual(words[0]['text'],'資料。')
    def test_versioned_rate_does_not_relax_legacy_profile(self):
        d=profile();d['voice']['atempo']=1.3
        with self.assertRaises(AssertionError):validate_profile(d)
        d.update(audio_policy='zh-TW-concepts-v3-1p3',quiz_silence_seconds=.45,quiet_tail={'threshold_pcm16':32,'retain_seconds':.18})
        validate_profile(d);self.assertEqual(timing(d)['quiz_samples'],21600)
        d['quiet_tail']['retain_seconds']=0
        with self.assertRaises(AssertionError):validate_profile(d)

if __name__=='__main__':unittest.main()

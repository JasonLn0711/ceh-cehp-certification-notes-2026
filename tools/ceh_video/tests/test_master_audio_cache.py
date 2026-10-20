import tempfile
from pathlib import Path
import unittest
from ceh_video.master_audio_cache import audio_key, cached_audio

class MasterAudioIdentityTests(unittest.TestCase):
    def test_recipe_tracks_pcm_frames_voice_runtime_and_policy(self):
        with tempfile.TemporaryDirectory() as tmp:
            pcm=Path(tmp)/'reference.wav';pcm.write_bytes(b'baseline PCM fixture')
            profile={'voice':{'atempo':1.4},'audio_policy':'ceh-en-v1.2'}
            key=audio_key(pcm,48000,profile)
            self.assertEqual(key,audio_key(pcm,48000,profile))
            self.assertNotEqual(key,audio_key(pcm,48001,profile))
            self.assertNotEqual(key,audio_key(pcm,48000,{**profile,'voice':{'atempo':1.5}}))
            pcm.write_bytes(b'changed PCM');self.assertNotEqual(key,audio_key(pcm,48000,profile))
            self.assertIsNone(cached_audio(Path(tmp),key))

    def test_changed_or_incomplete_cache_is_not_reused(self):
        from ceh_video.common import digest,sha,write
        with tempfile.TemporaryDirectory() as tmp:
            folder=Path(tmp);key={'recipe':'fixture'};stem=digest(key)
            audio=folder/(stem+'.m4a');audio.write_bytes(b'fixture AAC identity')
            receipt=folder/(stem+'.json')
            row={'status':'encoded_integrity_verified','key':key,'audio_sha256':sha(audio)}
            write(receipt,row);self.assertEqual(cached_audio(folder,key),audio)
            audio.write_bytes(b'changed AAC');self.assertIsNone(cached_audio(folder,key))
            receipt.write_text('unfinished {');self.assertIsNone(cached_audio(folder,key))
            write(receipt,[]);self.assertIsNone(cached_audio(folder,key))

    def test_decode_qa_implementation_does_not_invalidate_aac(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            pcm=Path(tmp)/'reference.wav';pcm.write_bytes(b'PCM')
            with patch('ceh_video.master_audio_cache.decoder_identity',return_value={'version':'fixed','implementation_sha256':'old'}):
                before=audio_key(pcm,48000,{})
            with patch('ceh_video.master_audio_cache.decoder_identity',return_value={'version':'fixed','implementation_sha256':'new'}):
                self.assertEqual(before,audio_key(pcm,48000,{}))
            with patch('ceh_video.master_audio_cache.decoder_identity',return_value={'version':'changed','implementation_sha256':'new'}):
                self.assertNotEqual(before,audio_key(pcm,48000,{}))

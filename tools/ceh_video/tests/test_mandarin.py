"""Locale-specific regression cases independent of the complete film's runtime evidence."""
import copy,json,tempfile,unittest
from pathlib import Path
from ceh_video.common import Project,write
from ceh_video.mandarin import validate_profile
from ceh_video.mandarin_speech import normalize,spoken,align_events,recipe,valid_cache

def profile():
    return {'schema_version':2,'content':{'locale':'zh-TW','narration_key':'narration_zh_TW'},
      'voice':{'provider':'edge-tts','provider_version':'7.3.1','name':'zh-TW-HsiaoChenNeural','language':'zh-TW','baseline_rate':'+0%','atempo':1.5,'speed_applications':1},
      'output':{'width':1920,'height':1080,'fps':30,'sample_rate':48000,'channels':2,'video_rate':1.0,'bgm':False},
      'quiz_silence_seconds':1,'alignment':{'backend':'provider_word_boundaries'},
      'runtime':{'max_chapter_renders':2,'render_workers':4,'ffmpeg':'test'}}

class MandarinTests(unittest.TestCase):
    def test_profile_keeps_picture_at_normal_rate(self):
        d=profile();validate_profile(d);d['output']['video_rate']=1.5
        with self.assertRaises(AssertionError):validate_profile(d)
    def test_speed_cannot_be_applied_twice(self):
        d=profile();d['voice']['speed_applications']=2
        with self.assertRaises(AssertionError):validate_profile(d)
    def test_source_rate_cannot_hide_a_second_speed_change(self):
        d=profile();d['voice']['baseline_rate']='-30%'
        with self.assertRaises(AssertionError):validate_profile(d)
    def test_taiwan_voice_is_explicit(self):
        d=profile();d['voice']['name']='zh-CN-XiaoxiaoNeural'
        with self.assertRaises(AssertionError):validate_profile(d)
    def test_han_text_survives_normalization(self):
        self.assertEqual(normalize('資料，ＳＳＤ 1.5 倍。'),'資料ssd15倍')
    def test_acronyms_adjacent_to_han_use_ascii_edges(self):
        self.assertEqual(spoken('使用SSD與CPU，但SSDStorage不拆開。',{'spell':['SSD','CPU']}),'使用S S D與C P U，但SSDStorage不拆開。')
    def test_real_boundaries_preserve_canonical_punctuation(self):
        text='禾日，SSD。'
        events=[{'text':'禾日','offset':1_000_000,'duration':6_000_000},{'text':'S','offset':9_000_000,'duration':1_000_000},{'text':'S','offset':11_000_000,'duration':1_000_000},{'text':'D','offset':13_000_000,'duration':1_000_000}]
        words=align_events(text,events,1.0)
        self.assertEqual(''.join(w['text'] for w in words),text)
        self.assertAlmostEqual(words[0]['start'],.1/1.5)
        self.assertAlmostEqual(words[0]['end'],.7/1.5)
        self.assertNotEqual(words[0]['end']-words[0]['start'],words[1]['end']-words[1]['start'])
    def test_missing_chinese_tokens_cannot_pass_empty_ascii_comparison(self):
        with self.assertRaises(ValueError):align_events('資料保存',[{'text':'資料','offset':0,'duration':1}],1)
    def test_non_monotonic_provider_boundaries_are_rejected(self):
        with self.assertRaises(AssertionError):align_events('資料',[{'text':'資','offset':3_000_000,'duration':1_000_000},{'text':'料','offset':1_000_000,'duration':1_000_000}],1)
    def test_short_processed_audio_cannot_swallow_boundary(self):
        with self.assertRaises(AssertionError):align_events('資料',[{'text':'資料','offset':0,'duration':30_000_000}],.2)
    def test_pronunciation_affects_only_its_resolved_recipe(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);write(root/'production.json',profile());write(root/'data/scenes.json',{'scenes':[]});write(root/'data/questions.json',{'questions':[]})
            write(root/'pronunciation.json',{'spell':['CPU'],'pronunciations':{}});p=Project(root);one=recipe(p,'CPU 運作。');stable=recipe(p,'訂單資料。')
            write(root/'pronunciation.json',{'spell':[],'pronunciations':{'CPU':'中央處理器'}})
            self.assertNotEqual(one,recipe(p,'CPU 運作。'));self.assertEqual(stable,recipe(p,'訂單資料。'));self.assertFalse(valid_cache(p,'CPU 運作。'))
    def test_osi_vertical_order_matches_low_to_high_arrow(self):
        from ceh_video.mandarin_art import build
        rows=build({'id':'OSI','kind':'osi','labels':['1 實體層','2 資料連結層','3 網路層','4 傳輸層','5 會議層','6 表達層','7 應用層']})
        layers={r['text'][0]:r['y'] for r in rows if r['kind']=='text' and r['text'][0] in '1234567'}
        self.assertGreater(layers['1'],layers['7'])
        self.assertTrue(all(layers[str(i)]>layers[str(i+1)] for i in range(1,7)))
    def test_switch_and_router_lesson_has_both_functional_devices(self):
        from ceh_video.mandarin_art import build
        rows=build({'id':'NET','kind':'switch_router','labels':[]})
        labels={r['text'] for r in rows if r['kind']=='text'}
        self.assertTrue({'交換器','路由器','MAC／訊框','IP／封包'}<=labels)


class ArchiveInventoryTests(unittest.TestCase):
    def test_repack_excludes_extracted_release_and_includes_review_media(self):
        from types import SimpleNamespace
        from ceh_video.mandarin_package import payload_files
        with tempfile.TemporaryDirectory() as t:
            home=Path(t);p=SimpleNamespace(root=home/'project',output=home/'output',qa=home/'qa')
            keep=['project/.production/speech-cache/a/provider.mp3','project/SCRIPT.md','output/film.mp4','output/inspection_frames/S01-late.png','qa/audio-audition/index.html']
            omit=['project/.venv/a.json','project/node_modules/a.json','project/.production/receipts/a.json','output/archive-verification/release/output/film.mp4','qa/portability/npm/node_modules/a.json','qa/engine-packaging.json']
            for rel in keep+omit:
                f=home/rel;f.parent.mkdir(parents=True,exist_ok=True);f.write_text('fixture')
            actual={rel for _,rel in payload_files(p)}
            self.assertEqual(actual,set(keep))
            self.assertEqual(actual,{rel for _,rel in payload_files(p)})

class PackageSourceTests(unittest.TestCase):
    def test_doc_edit_invalidates_package_without_including_generated_qa(self):
        from types import SimpleNamespace
        from ceh_video.mandarin_package import source_inputs
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);p=SimpleNamespace(root=root)
            (root/'START_HERE.md').write_text('first')
            before=source_inputs(p)
            (root/'START_HERE.md').write_text('revised')
            self.assertNotEqual(before,source_inputs(p))
            (root/'compositions').mkdir();(root/'compositions/generated.html').write_text('generated')
            self.assertEqual(set(source_inputs(p)),{'START_HERE.md'})

if __name__=='__main__':unittest.main()

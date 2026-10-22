import copy,json,tempfile,unittest
from pathlib import Path
from ceh_video.practice_video import validate_lesson,timeline,progress_at,cue_time,delivery_gate,text_hash,inside,sha
from ceh_video.practice_art import diagram,LABELS

def fixture():
    chapters=[];voice={};n=0
    for cid,count,case in [('C01',1,None),('C02',8,'case1'),('C03',8,'case2'),('C04',8,'case3'),('C05',1,None)]:
        steps=[]
        for i in range(1,count+1):
            n+=1;sid=f'S{n:02}';bid=sid+'-P1';text='先看目標，再看結果。'
            words=[{'text':'先看','char_start':0,'char_end':2,'start':0,'end':1},{'text':'目標，','char_start':2,'char_end':5,'start':1,'end':3},{'text':'再看結果。','char_start':5,'char_end':10,'start':3,'end':5}]
            steps.append({'id':sid,'case_id':case,'chapter_id':cid,'step':i if case else None,'label':'測試','capture_id':sid if case else None,'read_hold_seconds':0,'beats':[{'id':bid,'text':text,'cue':{'paragraph_id':bid},'panel':{'kind':'target'}}]})
            voice[bid]={'text_sha256':text_hash(text),'duration':5,'words':words,'speed_applications':1,'file':'test.wav','sha256':'fixture'}
        chapters.append({'id':cid,'title':'測試','case_id':case,'steps':steps})
    return {'schema_version':1,'chapters':chapters},voice

class PracticeContracts(unittest.TestCase):
    def test_ordered_eight_steps(self):
        lesson,_=fixture();self.assertTrue(validate_lesson(lesson));lesson['chapters'][1]['steps'][1]['step']=4
        with self.assertRaises(ValueError):validate_lesson(lesson)
    def test_duplicate_paragraph_rejected(self):
        lesson,_=fixture();lesson['chapters'][1]['steps'][0]['beats'][0]['id']='S01-P1'
        with self.assertRaises(ValueError):validate_lesson(lesson)
    def test_real_word_anchor_not_character_ratio(self):
        _,voice=fixture();v=voice['S01-P1'];self.assertEqual(cue_time('先看目標，再看結果。',v['words'],'目標'),1)
        with self.assertRaises(ValueError):cue_time('目標目標',v['words'],'目標')
        with self.assertRaises(ValueError):cue_time('先看目標',v['words'],'不存在')
    def test_stale_audio_rejected(self):
        lesson,voice=fixture();voice['S01-P1']['text_sha256']='bad'
        with self.assertRaises(ValueError):timeline(lesson,voice)
    def test_panel_order_is_not_silently_sorted(self):
        lesson,voice=fixture();lesson['chapters'][0]['steps'][0]['beats'][0]['panel']['states']=[{'cue_phrase':'再看','kind':'mask'},{'cue_phrase':'目標','kind':'contour'}]
        with self.assertRaises(ValueError):timeline(lesson,voice)
    def test_forward_backward_seek_and_case_reset(self):
        lesson,voice=fixture();t=timeline(lesson,voice);case=[s for s in t['scenes'] if s['case_id']=='case1']
        before=progress_at(case[2]['start']+1,t);progress_at(case[7]['start']+3,t)
        self.assertEqual(before,progress_at(case[2]['start']+1,t))
        new=next(s for s in t['scenes'] if s['case_id']=='case2');self.assertEqual(progress_at(new['start'],t)['fraction'],0)
        self.assertEqual(progress_at(case[7]['start']+case[7]['duration']-1e-8,t)['step'],8)
    def test_excerpt_keeps_case_step(self):
        lesson,voice=fixture();t=timeline(lesson,voice,selected=['S05']);self.assertEqual(progress_at(0,t)['step'],4);self.assertEqual(progress_at(0,t)['fraction'],3/8)
    def test_subtitle_text_preserved(self):
        lesson,voice=fixture();t=timeline(lesson,voice);self.assertEqual(''.join(c['text'] for c in t['captions']),'先看目標，再看結果。'*26)
    def test_missing_capture_blocks_delivery(self):
        lesson,voice=fixture();t=timeline(lesson,voice)
        with tempfile.TemporaryDirectory() as d:
            gate=delivery_gate(lesson,t,Path(d),{},{});self.assertFalse(gate['passed']);self.assertTrue(any('Missing Online capture' in x for x in gate['problems']))
    def test_receipt_without_artifacts_is_not_execution(self):
        lesson,voice=fixture();t=timeline(lesson,voice)
        with tempfile.TemporaryDirectory() as d:
            gate=delivery_gate(lesson,t,Path(d),{},{'environment':'MATLAB Online','status':'passed','version':'test','run_id':'test','checks':dict.fromkeys(['case1','case2','case3','run_matlab_tests'],True)})
            self.assertIn('No execution evidence artifacts',gate['problems'])
    def test_asset_path_cannot_escape(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):inside(Path(d),'../secret')
            with self.assertRaises(ValueError):inside(Path(d),'/tmp/file')
    def test_changed_capture_rejected(self):
        lesson,voice=fixture();t=timeline(lesson,voice)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'image.png').write_bytes(b'changed')
            gate=delivery_gate(lesson,t,p,{'S03-P1':{'environment':'MATLAB Online','run_id':'x','kind':'image','file':'image.png','sha256':'old'}},{'run_id':'x'})
            self.assertTrue(any('Invalid capture S03-P1' in x for x in gate['problems']))
    def test_overlength_blocks_delivery(self):
        lesson,voice=fixture();t=timeline(lesson,voice);t['duration']=1801
        with tempfile.TemporaryDirectory() as d:self.assertIn('Film exceeds 30 minutes',delivery_gate(lesson,t,Path(d),{},{})['problems'])
    def test_all_panels_have_real_svg(self):
        for kind in LABELS:self.assertIn('<svg',diagram(kind,'case1'))
        with self.assertRaises(ValueError):diagram('invented')

if __name__=='__main__':unittest.main()

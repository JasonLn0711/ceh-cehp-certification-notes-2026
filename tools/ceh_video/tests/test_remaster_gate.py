"""Fail-closed coverage and provenance checks; synthetic fixtures, not film QA."""
import tempfile
import unittest
from pathlib import Path
from ceh_video.common import sha
from ceh_video.visual_gate import required_frames, _checked_rows, _hash_matches


class RemasterGateTests(unittest.TestCase):
    def test_rounding_matches_javascript_at_half_frame(self):
        audio={'samples':1600*110,'segments':[]}
        self.assertIn(17,required_frames(audio,[]))  # Math.round(110*.15)
        self.assertIn(2,required_frames(audio,[{'start':0,'end':.1}]))

    def test_quiz_plan_includes_exact_required_boundary_frames(self):
        audio={'samples':1600*100,'segments':[{'kind':'silence','start_sample':20*1600,'end_sample':50*1600}]}
        self.assertTrue({19,20,21,27,35,42,49,50,51}<=set(required_frames(audio,[])))
        audio['segments'][0]['end_sample']+=1
        with self.assertRaisesRegex(RuntimeError,'quiz'):required_frames(audio,[])

    def report(self):
        return {'status':'passed','failures':[],'exceptions':[],
                'requiredStates':{'S01-f000000':0,'S01-f000010':10},
                'rows':[{'name':f'S01-f{f:06}','frame':f,'golden_pixels':0,'seek_pixels':0,
                         'seek_comparisons':dict(forward=0,reverse=0,repeated=0),'exceptions':[]} for f in (0,10)]}

    def test_missing_state_cannot_pass_on_one_successful_screenshot(self):
        report=self.report();expected=dict(report['requiredStates']);report['rows'].pop()
        with self.assertRaisesRegex(RuntimeError,'Missing'): _checked_rows(report,expected)
        report=self.report();report['requiredStates'].pop('S01-f000010')
        with self.assertRaisesRegex(RuntimeError,'Incomplete'): _checked_rows(report,expected)

    def test_unapproved_exception_and_missing_seek_mode_rejected(self):
        report=self.report();expected=report['requiredStates']
        self.assertEqual(len(_checked_rows(report,expected)),2)
        report['exceptions']=['LEGACY-M10-SUBTITLE-001']
        with self.assertRaisesRegex(RuntimeError,'exceptions'): _checked_rows(report,expected)
        report=self.report();report['rows'][0]['seek_comparisons'].pop('reverse')
        with self.assertRaisesRegex(RuntimeError,'seek'): _checked_rows(report,expected)

    def test_stale_source_and_layout_hashes_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            for name in ['S01.html','S01.layout.json']:
                path=Path(temp)/name;path.write_text('original');expected=sha(path)
                _hash_matches(path,expected,'scene artifact');path.write_text('changed')
                with self.assertRaisesRegex(RuntimeError,'stale'): _hash_matches(path,expected,'scene artifact')


if __name__=='__main__':unittest.main()

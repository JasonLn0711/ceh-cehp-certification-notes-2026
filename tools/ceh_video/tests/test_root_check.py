import copy
import unittest
from ceh_video.root_check import visual_only, validate_report


class RootVisualPartition(unittest.TestCase):
    def test_only_audio_elements_are_removed(self):
        before = '<style>.x{color:red}</style><div data-start="1.3">text</div><audio src="a.wav"></audio><svg><path d="M0 0"/></svg><script>window.t=3</script>'
        self.assertEqual(visual_only(before), before.replace('<audio src="a.wav"></audio>', ''))
        self.assertEqual(visual_only('<AUDIO src="a"/><span>audio</span>'), '<span>audio</span>')

    def test_full_native_coverage_and_contrast_remain_required(self):
        report = dict(ok=True, browserSkipped=False,
                      **{layer:dict(errorCount=0, warningCount=0)
                         for layer in ('lint','runtime','layout','contrast')})
        report['layout']['samples'] = [1.234, 2.345]
        report['contrast'].update(enabled=True, checked=2)
        validate_report(report, [1.2341, 2.3452])
        for layer, key, value in [
            ('layout','samples',[1.234]), ('layout','samples',[1.234,1.234]),
            ('runtime','errorCount',1), ('contrast','enabled',False),
            ('contrast','checked',0), ('lint','warningCount',1),
        ]:
            bad=copy.deepcopy(report);bad[layer][key]=value
            with self.assertRaises(AssertionError):
                validate_report(bad,[1.2341,2.3452])
        report['browserSkipped']=True
        with self.assertRaises(AssertionError):
            validate_report(report,[1.2341,2.3452])

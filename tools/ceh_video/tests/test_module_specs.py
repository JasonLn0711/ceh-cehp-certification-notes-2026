import unittest,json,tempfile
from pathlib import Path
from types import SimpleNamespace
from ceh_video.remaster import project_specs,semantic_scenes,SPECS,SEMANTIC_SCENES

class ModuleSpecsTests(unittest.TestCase):
    def test_full_frame_coverage_is_module_specific_and_fail_closed(self):
        from ceh_video.visual_gate import require_frame_coverage
        for count in (40,50):
            ids={f'S{i:02}' for i in range(count)}
            counts={sid:1800 for sid in ids}
            rows=[dict(scene=sid,frames=1800,errors=[]) for sid in sorted(ids)]
            require_frame_coverage(rows,ids,counts)
            for invalid in (rows[:-1],rows+[rows[0]],
                            [dict(rows[0],frames=1799),*rows[1:]],
                            [dict(rows[0],errors=['anchor detached']),*rows[1:]]):
                with self.assertRaisesRegex(RuntimeError,'all-frame'):
                    require_frame_coverage(invalid,ids,counts)

    def project(self,root,module='M11',source='data/specs.json'):
        return SimpleNamespace(root=root,profile=dict(module=module,**({'scene_specs':source} if source else {})),scenes=[{'id':'S01'},{'id':'S02'}],quiz_scenes=lambda:{'S02'})
    def test_new_module_cannot_inherit_m10_content(self):
        with tempfile.TemporaryDirectory() as d:
            p=self.project(Path(d),source=None)
            with self.assertRaisesRegex(ValueError,'explicit scene_specs'):project_specs(p)
            self.assertEqual(semantic_scenes(p),set())
    def test_exact_nonquiz_inventory_and_changed_content(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();f=root/'data/specs.json';p=self.project(root)
            f.write_text(json.dumps({'S01':{'note':'session lifecycle'}}))
            self.assertEqual(project_specs(p)['S01']['note'],'session lifecycle')
            f.write_text(json.dumps({'S01':{'note':'updated'}}))
            self.assertEqual(project_specs(p)['S01']['note'],'updated')
            for invalid in ({},{'S01':{},'S02':{}},{'S03':{}}):
                f.write_text(json.dumps(invalid))
                with self.assertRaisesRegex(ValueError,'inventory'):project_specs(p)
    def test_historical_m10_fallback_preserved(self):
        p=self.project(Path('/unused'),'M10',None)
        self.assertIs(project_specs(p),SPECS)
        self.assertEqual(semantic_scenes(p),SEMANTIC_SCENES)
    def test_explicit_semantic_inventory(self):
        p=self.project(Path('/unused'));p.profile['semantic_scenes']=['S01']
        self.assertEqual(semantic_scenes(p),{'S01'})

    def test_unnumbered_prompt_must_be_complete_before_hold(self):
        from ceh_video.remaster import unnumbered_quiz_start
        q={'prompt':'A condition. Which boundary?','choices':[{'text':x} for x in ['Choice A','Choice B','Choice C','Choice D']]}
        rows=[{'kind':'spoken','canonical':'A condition.','start_sample':14400,'end_sample':20000}, {'kind':'spoken','canonical':'Which boundary? Choice A Choice B Choice C Choice D','start_sample':30000,'end_sample':40000}, {'kind':'silence','start_sample':48000,'end_sample':96000}]
        self.assertEqual(unnumbered_quiz_start(q,{'segments':rows}),rows[0])
        rows[1]['canonical']='Which boundary? Choice A Choice B Choice C'
        with self.assertRaisesRegex(ValueError,'All choices'):unnumbered_quiz_start(q,{'segments':rows})
        rows[0]['canonical']='Unrelated.'
        with self.assertRaisesRegex(ValueError,'prompt'):unnumbered_quiz_start(q,{'segments':rows})

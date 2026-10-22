"""Failure/invalidation contracts; native performance evidence lives separately."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import unittest
from ceh_video.common import sha,write
from ceh_video.render_reuse import identity,reusable,retain,receipt

class MandarinReuseTests(unittest.TestCase):
    def fixture(self):
        from test_scoped_reuse import ScopedReuseTests
        fixture=ScopedReuseTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        p=fixture.p;p.profile['schema_version']=2
        fixture.render();(p.qa/'render-C1.log').write_text('native log fixture')
        return p

    def test_evidence_input_runtime_implementation_invalidates(self):
        p=self.fixture();key=identity(p,'C1');retain(p,'C1',key)
        self.assertTrue(reusable(p,'C1',key))
        for file in [p.root/'assets/scene',p.root/'browser',p.root/'package-lock.json',p.qa/'render-C1.log',p.output/'chapters/C1.mp4']:
            original=file.read_bytes();file.write_bytes(b'changed')
            self.assertFalse(reusable(p,'C1',identity(p,'C1')));file.write_bytes(original)
        with patch('ceh_video.render_reuse.sha',side_effect=lambda f:'changed' if Path(f).name=='mandarin.py' else sha(f)):
            self.assertFalse(reusable(p,'C1',identity(p,'C1')))
        (p.qa/'C1-render.json').unlink();self.assertFalse(reusable(p,'C1',key))

    def test_force_failure_and_cancellation_clear_success(self):
        from ceh_video.mandarin import action
        p=self.fixture();key=identity(p,'C1');retain(p,'C1',key)
        node=SimpleNamespace(name='render:C1')
        with patch('ceh_video.review.require_review'),patch('ceh_video.runner.subprocess_stage') as stage:
            self.assertEqual(action(p,node,lambda _:None),'verified_media_reuse');stage.assert_not_called()
            for error in [RuntimeError('failed'),KeyboardInterrupt()]:
                retain(p,'C1',key);stage.side_effect=error
                with self.assertRaises(type(error)):action(p,node,lambda _:None,True)
                self.assertFalse(receipt(p,'C1').exists())

    def test_force_master_forwarded(self):
        from ceh_video.mandarin import action
        with patch('ceh_video.runner.worker') as worker:
            action(SimpleNamespace(),SimpleNamespace(name='master'),lambda _:None,True)
            self.assertEqual(worker.call_args.args[1:3],('assemble_master',['--force']))

    def test_material_qa_ignores_recipe_but_tracks_consumed_sources(self):
        from test_qa_material_inputs import QAMaterialInputs
        from ceh_video.graph import Node,node_key,commit_receipt
        f=QAMaterialInputs();f.setUp();self.addCleanup(f.doCleanups)
        p=f.p;p.profile['schema_version']=2
        n=Node('checks',['master'],{},[],[])
        before=node_key(p,n)
        f.master.inputs={'recipe':'new upstream QA recipe'}
        commit_receipt(p,f.master,node_key(p,f.master))
        self.assertEqual(before,node_key(p,n))
        (p.root/'data/S01.audio.json').write_bytes(b'changed hold timing')
        self.assertNotEqual(before,node_key(p,n))

class GraphMediaGuardTests(unittest.TestCase):
    def test_graph_cache_hit_rechecks_runtime_material_receipt(self):
        from test_scoped_reuse import ScopedReuseTests
        from ceh_video.graph import Node,node_key,commit_receipt,inspect_node,planning
        f=ScopedReuseTests();f.setUp();self.addCleanup(f.doCleanups)
        p=f.p;p.profile['schema_version']=2;f.render();(p.qa/'render-C1.log').write_text('fixture')
        retain(p,'C1',identity(p,'C1'))
        n=Node('render:C1',[],{},[str(p.output/'chapters/C1.mp4')],[])
        commit_receipt(p,n,node_key(p,n))
        with patch('ceh_video.visual_gate.require_visual'),patch('ceh_video.review.require_review'):
            self.assertEqual(inspect_node(p,n)['action'],'reuse')
            (p.root/'browser').write_text('runtime changed')
            self.assertEqual(inspect_node(p,n)['action'],'run')
        with patch('ceh_video.graph.nodes',return_value={'render:C1':n}):
            self.assertEqual(planning(p,'render:C1')[-1]['action'],'run')

    def test_missing_encoded_sample_invalidates_qa_cache(self):
        from test_qa_material_inputs import QAMaterialInputs
        from ceh_video.graph import Node,node_key,commit_receipt,inspect_node
        f=QAMaterialInputs();f.setUp();self.addCleanup(f.doCleanups)
        p=f.p;p.profile['schema_version']=2
        image=p.output/'inspection_frames/hold.png';image.parent.mkdir();image.write_bytes(b'fixture')
        audit=p.qa/'rendered-artifact-audit.json';write(audit,{'sampled_frames':[{'file':'hold.png'}]})
        node=Node('checks',[],{},[str(audit)],[])
        commit_receipt(p,node,node_key(p,node))
        self.assertEqual(inspect_node(p,node)['action'],'reuse')
        image.unlink()
        self.assertEqual(inspect_node(p,node)['action'],'run')

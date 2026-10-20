"""Real encoded fixture cache; native HyperFrames performance is not simulated."""
from pathlib import Path
from types import SimpleNamespace
import subprocess, tempfile, unittest
from unittest.mock import patch
from ceh_video.common import write, sha
from ceh_video.render_reuse import identity, reusable, retain, receipt
from ceh_video.graph import nodes

class ScopedReuseTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        root=Path(self.tmp.name)/'project'
        for rel in ('node_modules/.bin','node_modules/hyperframes/dist','.production','assets'):
            (root/rel).mkdir(parents=True,exist_ok=True)
        for rel in ('package-lock.json','node_modules/.bin/hyperframes','browser','assets/scene'):
            (root/rel).write_text('fixture')
        self.p=SimpleNamespace(root=root,qa=root.parent/'qa',output=root.parent/'output',state=root/'.production',
            profile={'schema_version':1,'audio_policy':'ceh-en-v1.2','runtime':{'browser':str(root/'browser')},'output':{}},
            environment=lambda:{},chapter_inputs=lambda ch:sha(root/'assets/scene'),chapter_scenes=lambda ch:[{'id':'S1'}])
        self.p.qa.mkdir();(self.p.output/'chapters').mkdir(parents=True)
        self.ch='C1'
        write(self.p.qa/'C1-checked-fingerprint.json',{'sha256':self.p.chapter_inputs('C1')})
        write(self.p.qa/'C1-check.json',{'ok':True,'browserSkipped':False,**{k:{'errorCount':0,'warningCount':0} for k in ('lint','runtime','layout','contrast')}})

    def render(self,*args):
        p=self.p
        movie=p.output/'chapters/C1.mp4'
        subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=white:s=64x64:r=30:d=1','-c:v','libx264',str(movie)],check=True)
        write(p.qa/'C1-render.json',{'status':'rendered_codec_verified','source_sha256':p.chapter_inputs('C1'),'output_sha256':sha(movie)})
        for suffix in ('render.log','render.log.stderr'):(p.qa/('C1-'+suffix)).write_text('fixture execution')

    def test_real_bytes_reused_and_tampering_invalidates(self):
        key=identity(self.p,self.ch);self.assertFalse(reusable(self.p,self.ch,key))
        self.render();retain(self.p,self.ch,key);self.assertTrue(reusable(self.p,self.ch,key))
        (self.p.output/'chapters/C1.mp4').write_bytes(b'tampered')
        self.assertFalse(reusable(self.p,self.ch,key))

    def test_source_renderer_environment_and_log_invalidate(self):
        key=identity(self.p,self.ch);self.render();retain(self.p,self.ch,key)
        for rel in ('assets/scene','browser','package-lock.json'):
            f=self.p.root/rel;before=f.read_bytes();f.write_bytes(b'changed')
            self.assertFalse(reusable(self.p,self.ch,identity(self.p,self.ch)));f.write_bytes(before)
        self.p.environment=lambda:{'PRODUCER_FORCE_SCREENSHOT':'true'}
        self.assertFalse(reusable(self.p,self.ch,identity(self.p,self.ch)))
        self.p.environment=lambda:{}
        (self.p.qa/'C1-render.log').unlink()
        self.assertFalse(reusable(self.p,self.ch,identity(self.p,self.ch)))

    def test_actual_action_reuses_only_after_current_gates_and_force_runs(self):
        from ceh_video.runner import action, ReviewPending
        node=SimpleNamespace(name='render:C1')
        with patch('ceh_video.visual_gate.require_visual') as visual, patch('ceh_video.review.require_review') as review, patch('ceh_video.runner.worker',side_effect=self.render) as work:
            self.assertEqual(action(self.p,node,lambda _:None),'executed')
            self.assertEqual(action(self.p,node,lambda _:None),'verified_current_encoded_chapter_reused')
            self.assertEqual(work.call_count,1);self.assertEqual(visual.call_count,2);self.assertGreaterEqual(review.call_count,2)
            review.side_effect=RuntimeError('stale review')
            with self.assertRaises(ReviewPending):action(self.p,node,lambda _:None)
            review.side_effect=None
            self.assertEqual(action(self.p,node,lambda _:None,True),'executed')
            work.side_effect=RuntimeError('render failed')
            with self.assertRaises(RuntimeError):action(self.p,node,lambda _:None,True)
            self.assertFalse(receipt(self.p,self.ch).exists())

    def test_qa_implementation_changes_are_scoped(self):
        from test_engine import EngineTests
        fixture=EngineTests();fixture.setUp();self.addCleanup(fixture.tearDown)
        fixture.p.profile['audio_policy']='ceh-en-v1.2'
        before=nodes(fixture.p)
        with patch('ceh_video.graph.sha',side_effect=lambda f:'changed' if Path(f).name=='capture_late_diagrams.py' else sha(f)):
            after=nodes(fixture.p)
        changed={name for name in before if before[name].inputs!=after[name].inputs}
        self.assertEqual(changed,{'checks:late','package'})
        self.assertEqual(before['checks:audio'].dependencies,['master'])
        self.assertIn('audio-review',before['checks'].dependencies)
        self.assertIn(str(fixture.p.output/'inspection_frames/S99-midpoint.png'),before['checks:frames'].outputs)


class IndependentQATests(unittest.TestCase):
    def test_one_validator_change_reuses_other_real_receipts(self):
        from test_engine import EngineTests
        from ceh_video.graph import commit_receipt,node_key,inspect_node
        fixture=EngineTests();fixture.setUp();self.addCleanup(fixture.tearDown)
        fixture.p.profile['audio_policy']='ceh-en-v1.2'
        graph=nodes(fixture.p)
        for name in ('master','checks:frames','checks:audio','checks:late'):
            node=graph[name]
            for output in node.outputs:
                path=Path(output);path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(b'fixture output')
            commit_receipt(fixture.p,node,node_key(fixture.p,node))
        with patch('ceh_video.graph.sha',side_effect=lambda f:'changed' if Path(f).name=='capture_late_diagrams.py' else sha(f)):
            changed=nodes(fixture.p)
        self.assertEqual(inspect_node(fixture.p,changed['checks:late'])['action'],'run')
        for name in ('checks:audio','checks:frames'):
            self.assertEqual(inspect_node(fixture.p,changed[name])['action'],'reuse')
        image=fixture.p.output/'inspection_frames/S99-midpoint.png';image.unlink()
        self.assertEqual(inspect_node(fixture.p,changed['checks:frames'])['action'],'run')

if __name__=='__main__':unittest.main()

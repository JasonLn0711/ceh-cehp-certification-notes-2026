import tempfile,unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
from ceh_video.common import write
from ceh_video.graph import Node,node_key,commit_receipt,receipt_path,inspect_node,planning

class QAMaterialInputs(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        root=Path(self.tmp.name)/'project';root.mkdir()
        self.p=SimpleNamespace(root=root,state=root/'.production',qa=root.parent/'qa',output=root.parent/'output',profile={'audio_policy':'ceh-en-v1.2','master_filename':'master.mp4'},scenes=[{'id':'S01'}],chapters=['C01'])
        for folder in [root/'data',root/'assets/fonts',self.p.qa,self.p.output/'chapters']:folder.mkdir(parents=True)
        for f in [root/'production.json',root/'data/master-timing.json',root/'data/scenes.json',root/'data/questions.json',root/'data/S01.audio.json',root/'assets/fonts/LiberationSans-Regular.ttf',self.p.output/'chapters/C01.mp4',self.p.output/'master.mp4']:
            f.write_text('fixture')
        self.master=Node('master',[],{'recipe':'original'},[str(self.p.output/'master.mp4')],[])
        self.qa=Node('checks:frames',['master'],{},[str(self.p.qa/'audit.json')],[])
        (self.p.qa/'audit.json').write_text('{}')
        commit_receipt(self.p,self.master,node_key(self.p,self.master));commit_receipt(self.p,self.qa,node_key(self.p,self.qa))

    def test_upstream_receipt_change_preserves_material_qa(self):
        before=node_key(self.p,self.qa)
        self.master.inputs={'recipe':'QA-only upstream update'}
        commit_receipt(self.p,self.master,node_key(self.p,self.master))
        self.assertEqual(node_key(self.p,self.qa),before)
        self.assertEqual(inspect_node(self.p,self.qa)['action'],'reuse')
        with patch('ceh_video.graph.nodes',return_value={'master':self.master,'checks:frames':self.qa}):
            self.assertEqual(planning(self.p,'checks:frames')[-1]['action'],'reuse')

    def test_consumed_inputs_and_failed_parent_invalidate(self):
        before=node_key(self.p,self.qa)
        for f in [self.p.root/'data/master-timing.json',self.p.output/'chapters/C01.mp4',self.p.root/'assets/fonts/LiberationSans-Regular.ttf',self.p.output/'master.mp4']:
            data=f.read_bytes();f.write_bytes(b'changed');self.assertNotEqual(node_key(self.p,self.qa),before);f.write_bytes(data)
        write(receipt_path(self.p,'master'),{'status':'failed','outputs':{}})
        self.assertNotEqual(node_key(self.p,self.qa),before)

    def test_audio_annotation_and_reference_changes_invalidate(self):
        node=Node('checks:audio',['master'],{},[],[])
        before=node_key(self.p,node)
        f=self.p.root/'data/S01.audio.json';f.write_bytes(b'new hold boundary')
        self.assertNotEqual(node_key(self.p,node),before)
        before=node_key(self.p,node)
        (self.p.output/'master.reference.pcm.wav').write_bytes(b'new PCM')
        self.assertNotEqual(node_key(self.p,node),before)

    def test_legacy_key_still_tracks_execution_recipe(self):
        self.p.profile['audio_policy']='ceh-en-v1.1'
        before=node_key(self.p,self.qa)
        self.master.inputs={'recipe':'updated'};commit_receipt(self.p,self.master,node_key(self.p,self.master))
        self.assertNotEqual(node_key(self.p,self.qa),before)

if __name__=='__main__':unittest.main()

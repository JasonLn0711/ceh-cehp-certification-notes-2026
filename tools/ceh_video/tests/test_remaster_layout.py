"""Semantic device identity and reusable layout constraints."""
import unittest
from ceh_video.remaster import device_asset, layout_boxes

class RemasterLayoutTests(unittest.TestCase):
    def test_device_identity_is_explicit_even_when_label_mentions_users(self):
        node={'id':'server','kind':'device','label':'Server view: user success',
              'asset':'office_server','assetProvenance':'approved original server'}
        self.assertEqual(device_asset(node),'office_server')
        with self.assertRaisesRegex(ValueError,'explicit asset identity'):
            device_asset({'id':'server','kind':'device','label':'user'})
        self.assertIsNone(device_asset({'id':'person','kind':'card'}))

    def test_process_snakes_and_comparison_preserves_columns(self):
        region={'x':155,'y':304,'width':1280,'height':416}
        nodes=[{'id':str(i)} for i in range(4)]
        flow=layout_boxes('flow',nodes,region,40,188)
        comparison=layout_boxes('comparison',nodes,region,40,188)
        self.assertGreater(flow[2]['x'],flow[3]['x'])
        self.assertLess(comparison[2]['x'],comparison[3]['x'])
        for boxes in (flow,comparison):
            for b in boxes:
                self.assertGreaterEqual(b['x'],region['x'])
                self.assertGreaterEqual(b['y'],region['y'])
                self.assertLessEqual(b['x']+b['width'],region['x']+region['width'])
                self.assertLessEqual(b['y']+b['height'],region['y']+region['height'])

    def test_reflection_preserves_sender_and_claimed_return_distinction(self):
        nodes=[{'id':x} for x in ['sender','claimed-return-address','service','victim']]
        boxes=layout_boxes('reflection',nodes,{'x':155,'y':304,'width':1280,'height':416},40,188)
        b=dict(zip([n['id'] for n in nodes],boxes))
        self.assertEqual(b['sender']['y'],b['service']['y'])
        self.assertEqual(b['claimed-return-address']['y'],b['victim']['y'])
        self.assertLess(b['sender']['y'],b['claimed-return-address']['y'])

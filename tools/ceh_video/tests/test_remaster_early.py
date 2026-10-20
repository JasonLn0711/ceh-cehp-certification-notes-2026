"""Source-preserving semantics and integrity for the early remaster scenes."""
import unittest

from ceh_video.remaster_early import SCENES


class EarlyRemasterTests(unittest.TestCase):
    def test_complete_connected_references_and_cue_contract(self):
        self.assertEqual(set(SCENES), {f'S{i:02}' for i in range(1, 23)})
        for sid, scene in SCENES.items():
            with self.subTest(scene=sid):
                nodes = scene['nodes']
                ids = {node['id'] for node in nodes}
                self.assertEqual(len(ids), len(nodes))
                self.assertTrue(2 <= len(nodes) <= 9)
                self.assertIn('scene_art_start.py:', scene['provenance'])
                for node in nodes:
                    self.assertIn(node['cue'], range(4))
                    self.assertLessEqual(len(node['label']), 75)
                    self.assertFalse({'x', 'y', 'width', 'height'} & node.keys())
                    if node['kind'] in {'bar', 'queue', 'metric'}:
                        self.assertGreater(node['maximum'], 0)
                        self.assertTrue(0 <= node['value'] <= node['maximum'])
                for edge in scene['edges']:
                    self.assertIn(edge['from'], ids)
                    self.assertIn(edge['to'], ids)
                    self.assertNotEqual(edge['from'], edge['to'])

    def test_comparable_bandwidth_bars_preserve_common_scale(self):
        bars = SCENES['S11']['nodes']
        self.assertEqual([n['value'] for n in bars], [50, 150, 2400, 200])
        self.assertEqual({n['maximum'] for n in bars}, {2400})
        self.assertTrue(all('Mbps' in n['label'] for n in bars))
        self.assertIn('2200 Mbps', SCENES['S11']['note'])

    def test_filter_placement_preserves_constrained_boundary(self):
        self.assertEqual([(e['from'], e['to']) for e in SCENES['S16']['edges']],
                         [('upstream', 'link'), ('link', 'campus'), ('campus', 'server')])
        self.assertIn('not deployment proof', SCENES['S16']['note'])

    def test_queue_representation_retains_entry_units(self):
        backlog = next(n for n in SCENES['S18']['nodes'] if n['id'] == 'backlog')
        self.assertEqual((backlog['cells'], backlog['value'], backlog['maximum']),
                         (16, 1024, 1024))
        self.assertIn('64 entries', backlog['label'])
        for sid in ['S05', 'S06', 'S08', 'S10', 'S13', 'S20', 'S21', 'S22']:
            for node in SCENES[sid]['nodes']:
                if node['kind'] == 'queue':
                    self.assertIn('illustrative', node['label'])


if __name__ == '__main__':
    unittest.main()

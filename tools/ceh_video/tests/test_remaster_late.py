"""Semantic and contract checks for authored late M10 remaster figures."""
import unittest
from ceh_video.remaster_late import SCENES


class LateSceneSpecsTests(unittest.TestCase):
    def test_complete_scene_ownership(self):
        self.assertEqual(set(SCENES), {f'S{i:02d}' for i in range(23, 50)} | {'S58'})

    def test_coordinate_free_valid_graphs(self):
        for sid, spec in SCENES.items():
            with self.subTest(scene=sid):
                self.assertIn('source', spec['provenance'])
                if spec['template'] == 'matrix':
                    self.assertTrue(all(len(row) == len(spec['headers']) for row in spec['rows']))
                    continue
                ids = {n['id'] for n in spec['nodes']}
                self.assertEqual(len(ids), len(spec['nodes']))
                self.assertLessEqual(len(ids), 9)
                for n in spec['nodes']:
                    self.assertIn(n['cue'], range(4))
                    self.assertLessEqual(len(n['label']), 75)
                    self.assertFalse({'x', 'y', 'width', 'height'} & n.keys())
                    if n['kind'] in ('bar', 'queue'):
                        self.assertGreater(n['maximum'], 0)
                        self.assertLessEqual(n['value'], n['maximum'])
                for e in spec['edges']:
                    self.assertIn(e['from'], ids)
                    self.assertIn(e['to'], ids)

    def test_reflection_does_not_reply_to_actual_sender(self):
        edges = {(e['from'], e['to']) for e in SCENES['S23']['edges']}
        self.assertIn(('sender', 'service'), edges)
        self.assertIn(('service', 'victim'), edges)
        self.assertNotIn(('service', 'sender'), edges)

    def test_quantitative_scale_and_capstone(self):
        pool = next(n for n in SCENES['S32']['nodes'] if n['id'] == 'pool')
        self.assertEqual((pool['value'], pool['maximum'], pool['cells']), (32, 32, 32))
        backlog = next(n for n in SCENES['S44']['nodes'] if n['id'] == 'backlog')
        self.assertEqual((backlog['value'], backlog['maximum'], backlog['cells']), (1024, 1024, 16))
        self.assertEqual([r[0] for r in SCENES['S58']['rows']], ['E01', 'E02', 'E03', 'E04'])

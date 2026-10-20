import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from ceh_video.audio_policy import timing, modern
from ceh_video.common import write
from ceh_video.run_record import RunRecord, phase_summary
from ceh_video.scheduling import render_order
from ceh_video.timing_ledger import chapter_boundaries
from ceh_video.packaging import walk_files


class EfficiencyContract(unittest.TestCase):
    def test_new_migration_selects_v12_without_copying_runtime_or_host_audio(self):
        from unittest.mock import patch
        from ceh_video.engineering import migrate
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);source=base/'source/project'
            for name in ('assets/audio','models','.venv','node_modules','scripts','data','design'):
                (source/name).mkdir(parents=True,exist_ok=True)
            (source/'assets/audio/old-master.wav').write_bytes(b'generated fixture')
            write(source/'production.json',dict(module='M10',schema_version=1,locked_assets={},
                voice=dict(name='af_heart',language='en-us',baseline_speed=.73,atempo=1.4,speed_applications=1)))
            write(source/'data/scenes.json',dict(scenes=[]))
            write(source/'data/questions.json',dict(questions=[]))
            write(source/'design/tokens.json',dict(version='fixture'))
            original=(source/'production.json').read_bytes()
            with patch('ceh_video.preflight.validate_profile'),patch('ceh_video.speech.import_baselines',return_value=0):
                migrate(base/'source',base/'new')
            target=base/'new/project'
            self.assertEqual(json.loads((target/'production.json').read_text())['audio_policy'],'ceh-en-v1.2')
            self.assertTrue((target/'.venv').is_symlink())
            self.assertTrue((target/'node_modules').is_symlink())
            self.assertFalse((target/'assets/audio').exists())
            self.assertTrue((target/'design/tokens.json').is_file())
            self.assertEqual((source/'production.json').read_bytes(),original)

    def test_policy_identity_and_counts(self):
        profile={'audio_policy':'ceh-en-v1.2','voice':{'atempo':1.4,'speed_applications':1}}
        policy=timing(profile)
        self.assertEqual(policy['gap'],14400)
        self.assertEqual(policy['chapter_gap'],policy['opening']+policy['ending'])
        self.assertEqual(policy['quiz']*8,384000)
        with self.assertRaises(ValueError):modern({'audio_policy':'typo'})

    def test_boundary_references_buffers_without_inserting(self):
        a={'samples':50000,'ledger':[{'kind':'opening','start_sample':0,'end_sample':14400},
            {'kind':'spoken','start_sample':14400,'end_sample':25000},
            {'kind':'ending','start_sample':25000,'end_sample':49000},
            {'kind':'frame_alignment','start_sample':49000,'end_sample':50000}]}
        p=SimpleNamespace(profile={'audio_policy':'ceh-en-v1.2','voice':{'atempo':1.4,'speed_applications':1}},
            scenes=[{'id':'S01','chapter_id':'C01'},{'id':'S02','chapter_id':'C02'}],
            chapters=['C01','C02'],audio=lambda sid:a)
        row=chapter_boundaries(p)[0]
        self.assertEqual(row['named_pause_frames'],38400)
        self.assertEqual(row['actual_interval_frames'],39400)
        self.assertEqual(row['additional_inserted_frames'],0)
        self.assertEqual(row['end_sample']-row['start_sample'],39400)

    def test_longest_first_is_stable(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=SimpleNamespace(qa=Path(tmp),profile={'runtime':{}},
                audio=lambda sid:{'samples':{'S1':16000,'S2':16000,'S11':64000}[sid]},
                chapter_scenes=lambda ch:[{'id':ch.replace('C','S')}])
            self.assertEqual(render_order(p,['render:C2','render:C11','render:C1']),
                             ['render:C11','render:C1','render:C2'])

    def test_attempts_never_overwrite_and_events_are_ordered(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=SimpleNamespace(qa=Path(tmp))
            first=RunRecord(p,'checks');first.event({'phase':'node_start','node':'master'})
            first.finish('failed',error='controlled')
            second=RunRecord(p,'checks','retry',first.id);second.finish('verified')
            self.assertNotEqual(first.id,second.id)
            self.assertEqual(json.loads((first.directory/'summary.json').read_text())['status'],'failed')
            events=[json.loads(x) for x in (first.directory/'events.jsonl').read_text().splitlines()]
            self.assertEqual([x['sequence'] for x in events],list(range(1,len(events)+1)))
            self.assertTrue(all(x['elapsed_seconds']>=0 for x in events))
            with self.assertRaises(RuntimeError):first.finish('verified')
            with self.assertRaises(ValueError):RunRecord(p,'checks','retry')
            with self.assertRaises(ValueError):RunRecord(p,'checks','retry','../outside')

    def test_wall_tail_and_queue_are_not_summed_work(self):
        rows=[
            dict(phase='node_queued',node='render:C11',elapsed_seconds=1),
            dict(phase='node_start',node='render:C11',elapsed_seconds=2),
            dict(phase='node_start',node='render:C01',elapsed_seconds=2),
            dict(phase='node_verified',node='render:C01',elapsed_seconds=10),
            dict(phase='node_verified',node='render:C11',elapsed_seconds=12)]
        summary=phase_summary(rows)
        self.assertEqual(summary['render_window_seconds'],10)
        self.assertEqual(summary['single_job_tail_seconds'],2)
        self.assertEqual(summary['queue_wait_seconds'],{'render:C11':1})

    def test_packaging_rejects_links_before_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'asset').write_text('source')
            (root/'escape').symlink_to('/etc')
            with self.assertRaises(ValueError):list(walk_files(root,'project'))
            (root/'escape').unlink();(root/'bad').symlink_to(root/'missing')
            with self.assertRaises(ValueError):list(walk_files(root,'project'))

    def test_generated_hosts_are_excluded_narrowly(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'hosts').mkdir();(root/'hosts/media').symlink_to('/etc')
            (root/'report.json').write_text('{}');(root/'frame.png').write_bytes(b'actual fixture')
            rows=list(walk_files(root,'qa',{'hosts'}))
            self.assertEqual({x[0] for x in rows},{'qa/report.json','qa/frame.png'})

    def test_packaging_implementation_is_not_audio_dependency(self):
        from ceh_video.graph import nodes
        from ceh_video.common import Project
        root=Path('/home/jnlngx10/Videos/CEH_M10_efficiency_v1_2/project')
        if not root.exists():self.skipTest('Production dependency fixture is local')
        graph=nodes(Project(root))
        self.assertNotIn('delivery.py',graph['audio-review'].inputs['implementation'])
        self.assertNotIn('packaging.py',graph['audio-review'].inputs['implementation'])
        self.assertIn('packaging.py',graph['package'].inputs['implementation'])
        self.assertNotIn('packaging.py',graph['checks'].inputs['implementation'])
        from unittest.mock import patch
        from ceh_video.common import sha
        with patch('ceh_video.graph.sha',side_effect=lambda path:'changed-package-only' if Path(path).name=='packaging.py' else sha(path)):
            changed_graph=nodes(Project(root))
        affected={name for name in graph if graph[name].inputs!=changed_graph[name].inputs}
        while True:
            expanded=affected|{name for name,node in graph.items() if set(node.dependencies)&affected}
            if expanded==affected:break
            affected=expanded
        self.assertEqual(affected,{'package'})

    def test_pause_update_keeps_spoken_cache_identity(self):
        from ceh_video.speech import recipe, baseline_recipe
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            write(root/'pronunciation.json',dict(spell=[],pronunciations={}))
            profile=dict(audio_policy='ceh-en-v1.1',voice=dict(name='af_heart',language='en-us',baseline_speed=.73,atempo=1.4,speed_applications=1),models={},runtime=dict(ffmpeg='fixture'))
            p=SimpleNamespace(root=root,profile=profile)
            processed,baseline=recipe(p,'Known narration.'),baseline_recipe(p,'Known narration.')
            p.profile['audio_policy']='ceh-en-v1.2'
            self.assertEqual(processed,recipe(p,'Known narration.'))
            self.assertEqual(baseline,baseline_recipe(p,'Known narration.'))

    def test_v12_golden_review_requires_exact_candidate_inventory(self):
        from ceh_video.common import sha
        from ceh_video.delivery import verify_golden_review_evidence
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);qa=base/'qa';folder=qa/'visual'
            write(base/'project/production.json',{'audio_policy':'ceh-en-v1.2'})
            candidate=folder/'candidate-final-manifest.json'
            write(candidate,dict(sources={'S01':'source'},rows=[{'name':'S01-f000000'}]))
            contact=folder/'contact.png';contact.write_bytes(b'controlled contact fixture')
            review=folder/'agent-review-v1.2.json'
            evidence=dict(status='agent_visual_review_completed',candidate_sha256=sha(candidate),
                          scenes=['S01'],approved_states=['S01-f000000'],visually_inspected_states=['S01-f000000'],
                          contact_sheets={'visual/contact.png':sha(contact)},findings=['Fixture only'])
            write(review,evidence)
            def approval():
                write(folder/'golden-approval.json',dict(decision='approved_initial_golden',
                    candidate_sha256=sha(candidate),review_receipts={'visual/agent-review-v1.2.json':sha(review)}))
            approval();verify_golden_review_evidence(base)
            evidence['approved_states']=[];write(review,evidence);approval()
            with self.assertRaises(AssertionError):verify_golden_review_evidence(base)

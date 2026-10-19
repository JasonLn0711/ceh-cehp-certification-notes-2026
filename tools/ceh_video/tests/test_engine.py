"""Behavioral regression tests; fixture receipts do not establish live media execution."""
from pathlib import Path
import copy, json, os, subprocess, sys, tempfile, unittest
from unittest.mock import patch
from ceh_video.common import Project,digest,lock,read,sha,write
from ceh_video.graph import Node,commit_receipt,inspect_node,node_key,planning,receipt_path
from ceh_video.preflight import validate_profile
from ceh_video.review import audio_decision,capture_manifest,record,require_review
from ceh_video.speech import spoken,sentences


class EngineTests(unittest.TestCase):
    def setUp(self):
        from ceh_video.runner import STOP_REQUESTED
        STOP_REQUESTED.clear()
        self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name);self.root=self.base/'project';self.root.mkdir()
        profile={'schema_version':1,'voice':{'name':'af_heart','language':'en-us','baseline_speed':.73,'atempo':1.5,'speed_applications':1},'output':{'width':1920,'height':1080,'fps':30,'sample_rate':48000,'channels':2,'video_rate':1.0,'bgm':False},'quiz_silence_seconds':1,'runtime':{'max_chapter_renders':2,'render_workers':4,'hyperframes':'test','ffmpeg':'fixture-ffmpeg','browser':'/fixture/browser'},'expected':{'scenes':1,'chapters':1,'questions':0,'canonical_words':2},'alignment':{},'models':{},'diagram_inputs':{},'master_filename':'master.mp4','editable_filename':'editable.zip'}
        write(self.root/'production.json',profile);write(self.root/'data/scenes.json',{'scenes':[{'id':'S99','chapter_id':'C99','narration_en_US':'Hello world.','audio_segments':[{'kind':'spoken','text':'Hello world.'}],'on_screen_copy':['Hello']} ]})
        write(self.root/'data/questions.json',{'questions':[]});write(self.root/'pronunciation.json',{'spell':['CPU'],'pronunciations':{'SYN':'sin'}});write(self.root/'data/S99.audio.json',{'segments':[]})
        (self.root/'scripts').mkdir();self.p=Project(self.root)
    def tearDown(self):self.temp.cleanup()
    def test_atomic_json(self):
        write(self.root/'record.json',{'a':1});write(self.root/'record.json',{'a':2});self.assertEqual(read(self.root/'record.json'),{'a':2});self.assertFalse(list(self.root.glob('*.tmp')))
    def test_package_keeps_unrelated_custody_notes_local(self):
        from ceh_video.delivery import export_qa
        for name in ['C11-review.json','reference-audio-identities.json','recognition-refresh.json','asr-functional-events.jsonl']:self.assertTrue(export_qa(Path(name)),name)
        for name in ['coursework-before-merge.md','planning-merge-check.json','preexisting-planning-work.json','unrelated-coursework-preservation.json']:self.assertFalse(export_qa(Path(name)),name)
    def test_process_lock_excludes_second_writer(self):
        with lock(self.root/'lock'):
            with self.assertRaisesRegex(RuntimeError,'Already running'):
                with lock(self.root/'lock'):pass
    def test_voice_and_silence_are_explicit(self):
        validate_profile(self.p.profile)
        for field,value in [('quiz_silence_seconds',12),('schema_version',2)]:
            d=copy.deepcopy(self.p.profile);d[field]=value
            with self.assertRaises(AssertionError):validate_profile(d)
    def test_no_second_speed_pass(self):
        d=copy.deepcopy(self.p.profile);d['voice']['speed_applications']=2
        with self.assertRaises(AssertionError):validate_profile(d)
    def test_token_expansion_preserves_canonical_input(self):
        text='CPU SYN SYNTHESIS';self.assertEqual(spoken(text,{'spell':['CPU'],'pronunciations':{'SYN':'sin'}}),'C P U sin SYNTHESIS');self.assertEqual(text,'CPU SYN SYNTHESIS')
    def test_choice_letter_stays_with_sentence(self):
        self.assertEqual(sentences('Question 1. A. First option. B. Second option.'),['Question 1.','A. First option.','B. Second option.'])
    def test_recipe_includes_resolved_expansion(self):
        from ceh_video.speech import recipe
        a=recipe(self.p,'CPU works.');write(self.root/'pronunciation.json',{'spell':[],'pronunciations':{'CPU':'processor'}});self.assertNotEqual(a,recipe(self.p,'CPU works.'))
    def test_unrelated_pronunciation_change_does_not_invalidate(self):
        from ceh_video.speech import recipe
        a=recipe(self.p,'Hello world.');write(self.root/'pronunciation.json',{'spell':['CPU'],'pronunciations':{'SYN':'synchronize','UNUSED':'unused'}});self.assertEqual(a,recipe(self.p,'Hello world.'))
    def test_recipe_key_is_stable_under_reordering(self):
        from ceh_video.speech import cache_entry
        a=cache_entry(self.p,'Hello world.');self.assertEqual(a,cache_entry(self.p,'Hello world.'))
    def test_malformed_cache_receipt_is_a_miss(self):
        from ceh_video.speech import cache_entry,valid_cache
        d=cache_entry(self.p,'Hello world.');d.mkdir(parents=True);(d/'receipt.json').write_text('{partial')
        self.assertFalse(valid_cache(self.p,'Hello world.'))
    def test_output_tampering_invalidates_cache(self):
        f=self.root/'artifact';f.write_text('original');n=Node('test',[],{'x':1},[str(f)],[]);key=node_key(self.p,n);commit_receipt(self.p,n,key)
        self.assertEqual(inspect_node(self.p,n)['action'],'reuse');f.write_text('changed');self.assertEqual(inspect_node(self.p,n)['action'],'run')
    def test_missing_output_invalidates_cache(self):
        f=self.root/'artifact';f.write_text('original');n=Node('test',[],{},[str(f)],[]);commit_receipt(self.p,n,node_key(self.p,n));f.unlink();self.assertEqual(inspect_node(self.p,n)['action'],'run')
    def test_dependency_bytes_participate_in_key(self):
        n=Node('b',['a'],{},[],[]);write(receipt_path(self.p,'a'),{'key':'same','outputs':{'file':'first'}});one=node_key(self.p,n);write(receipt_path(self.p,'a'),{'key':'same','outputs':{'file':'second'}});self.assertNotEqual(one,node_key(self.p,n))
    def test_cycle_is_rejected(self):
        a=Node('a',['b'],{},[],[]);b=Node('b',['a'],{},[],[])
        with patch('ceh_video.graph.nodes',return_value={'a':a,'b':b}):
            with self.assertRaisesRegex(ValueError,'cycle'):planning(self.p,'a')
    def test_failed_receipt_is_not_reused(self):
        n=Node('test',[],{},[],[]);write(receipt_path(self.p,'test'),{'status':'failed','key':node_key(self.p,n),'outputs':{}});self.assertEqual(inspect_node(self.p,n)['action'],'run')
    def make_chapter(self):
        c=self.root/'chapters/C99';(c/'compositions').mkdir(parents=True);(c/'assets').mkdir();(c/'index.html').write_text('<div>test</div>');write(c/'hyperframes.json',{});(c/'compositions/S99.html').write_text('<div>scene</div>');write(c/'compositions/S99.motion.json',{});(c/'assets/audio.wav').write_bytes(b'fixture')
        q=self.p.qa/'C99-states';q.mkdir(parents=True);(q/'state.png').write_bytes(b'fixture capture, not a live image')
        import ceh_video.review as review
        write(q/'manifest.json',{'capture_recipe':sha(Path(review.__file__).parent/'capture.mjs'),'rows':[{'file':'state.png','sha256':sha(q/'state.png')}]})
        return c,q
    def test_preview_cache_is_not_an_input(self):
        c,q=self.make_chapter();before=self.p.chapter_inputs('C99');(c/'.waveform-cache').mkdir();(c/'.waveform-cache/view').write_text('cache');(c/'.hyperframes').mkdir();(c/'.hyperframes/state').write_text('preview');self.assertEqual(before,self.p.chapter_inputs('C99'))
    def test_rendered_assets_are_inputs(self):
        c,q=self.make_chapter();before=self.p.chapter_inputs('C99');(c/'assets/audio.wav').write_bytes(b'changed');self.assertNotEqual(before,self.p.chapter_inputs('C99'))
    def test_editor_metadata_is_not_picture_input(self):
        c,q=self.make_chapter();before=self.p.chapter_inputs('C99');(c/'index.html').write_text('<div data-hf-id="editor-id">test</div>');self.assertEqual(before,self.p.chapter_inputs('C99'))
    def test_review_is_bound_to_source(self):
        c,q=self.make_chapter();record(self.p,'C99','Inspected fixture for receipt contract only.');require_review(self.p,'C99');(c/'compositions/S99.html').write_text('changed')
        with self.assertRaisesRegex(RuntimeError,'Stale'):require_review(self.p,'C99')
    def test_review_is_bound_to_captured_image(self):
        c,q=self.make_chapter();record(self.p,'C99','Inspected fixture for receipt contract only.');(q/'state.png').write_bytes(b'changed')
        with self.assertRaisesRegex(RuntimeError,'Stale'):require_review(self.p,'C99')
    def test_empty_review_is_rejected(self):
        self.make_chapter()
        with self.assertRaises(ValueError):record(self.p,'C99','')
    def test_cached_render_still_requires_current_review(self):
        c,q=self.make_chapter();record(self.p,'C99','Fixture receipt contract only.')
        n=Node('render:C99',[],{},[],[]);commit_receipt(self.p,n,node_key(self.p,n))
        self.assertEqual(inspect_node(self.p,n)['action'],'reuse')
        (q/'state.png').write_bytes(b'changed')
        with self.assertRaisesRegex(RuntimeError,'Stale'):inspect_node(self.p,n)
    def test_batch_review_gate_runs_before_dispatch(self):
        from ceh_video.runner import review_batch,ReviewPending
        self.make_chapter()
        with self.assertRaises(ReviewPending):review_batch(self.p,[{'node':'prepare:C99','action':'reuse'},{'node':'render:C99','action':'run'}],lambda r:None)
        self.assertEqual(read(self.p.state/'review-gate.json')['status'],'waiting_review')
    def test_cancelled_queue_cannot_spawn_another_child(self):
        from ceh_video.runner import cancel_children,subprocess_stage,RunCancelled
        cancel_children();target=self.root/'must-not-exist'
        with self.assertRaises(RunCancelled):subprocess_stage(self.p,[sys.executable,'-c','from pathlib import Path;Path('+repr(str(target))+').write_text("unexpected")'],'cancelled-child',lambda r:None)
        self.assertFalse(target.exists())
    def test_automation_cannot_clear_listening_lead(self):
        write(self.p.qa/'audio-review-decisions.json',{'items':{'x':{}}})
        with self.assertRaisesRegex(ValueError,'Human'):audio_decision(self.p,'x','reviewed_no_defect','automated_technical','No actual listening')
    def test_cli_json_failure_has_nonzero_status(self):
        proc=subprocess.run([sys.executable,'-m','ceh_video','--project',str(self.root),'review','--chapter','C99','--findings',''],capture_output=True,text=True);self.assertNotEqual(proc.returncode,0);self.assertEqual(json.loads(proc.stdout)['status'],'failed')
    def test_non_m10_scene_and_question_mapping(self):
        from ceh_video.graph import nodes
        graph=nodes(self.p);self.assertIn('scene:S99',graph);self.assertIn('render:C99',graph)
    def test_master_metadata_uses_module_profile(self):
        import ast
        source=Path(__file__).parents[1]/'ceh_video/runtime/assemble_master.py'
        tree=ast.parse(source.read_text());function=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='metadata_lines')
        context={};exec(compile(ast.Module(body=[function],type_ignores=[]),str(source),'exec'),context)
        rows=context['metadata_lines']({'title':'M99 Example'},[{'id':'C99','title':'Title; test','start':0,'duration':1}])
        self.assertEqual(rows[1],'title=M99 Example');self.assertIn('END=48000',rows);self.assertIn('title=C99 Title\\; test',rows)
    def test_art_override_does_not_change_speech_key(self):
        from ceh_video.graph import nodes
        a=nodes(self.p);write(self.root/'data/visual-overrides.json',{'S99':{'offset_x':1}});b=nodes(self.p)
        self.assertEqual(a['speech:S99'].inputs,b['speech:S99'].inputs);self.assertNotEqual(a['scene:S99'].inputs,b['scene:S99'].inputs)
    def test_secret_redaction(self):
        from ceh_video.progress import sanitize
        s=sanitize('Authorization: Bearer private-value password=hidden https://user:secret@example.test')
        self.assertNotIn('private-value',s);self.assertNotIn('hidden',s);self.assertNotIn('user:secret',s)
    def test_redirected_progress_has_no_ansi(self):
        import io
        from ceh_video.progress import Progress
        stream=io.StringIO()
        with patch('sys.stderr',stream):Progress(plain=True)({'phase':'waiting','completed':2,'total':4})
        self.assertNotIn('\x1b',stream.getvalue());self.assertEqual(json.loads(stream.getvalue())['completed'],2)
    def test_actual_child_failure_preserves_code(self):
        from ceh_video.runner import subprocess_stage,StageFailure
        with self.assertRaises(StageFailure) as caught:subprocess_stage(self.p,[sys.executable,'-c','raise SystemExit(7)'],'controlled-failure',lambda r:None)
        self.assertEqual(caught.exception.exit_code,7);self.assertEqual(read(self.p.state/'children/controlled-failure.json')['exit_code'],7)
    def test_actual_quiet_child_is_not_reported_as_progress(self):
        from ceh_video.runner import subprocess_stage
        events=[];subprocess_stage(self.p,[sys.executable,'-c','import time;time.sleep(.05)'],'controlled-quiet',events.append)
        r=read(self.p.state/'children/controlled-quiet.json');self.assertEqual(r['status'],'completed');self.assertIsNone(r['last_actual_output_at'])
    def test_actual_interrupt_cleans_child_group(self):
        import signal,time
        script="""import sys
from ceh_video.common import Project
from ceh_video.runner import subprocess_stage
try:subprocess_stage(Project(sys.argv[1]),[sys.executable,'-c','import time;time.sleep(30)'],'controlled-interrupt',lambda r:None)
except KeyboardInterrupt:raise SystemExit(130)
"""
        parent=subprocess.Popen([sys.executable,'-c',script,str(self.root)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        record=self.p.state/'children/controlled-interrupt.json';deadline=time.monotonic()+5
        try:
            while not record.exists() and time.monotonic()<deadline:time.sleep(.01)
            self.assertTrue(record.exists());child=read(record)['pid'];parent.send_signal(signal.SIGINT);self.assertEqual(parent.wait(timeout=5),130)
            self.assertEqual(read(record)['status'],'interrupted')
            with self.assertRaises(ProcessLookupError):os.kill(child,0)
        finally:
            if parent.poll() is None:parent.kill();parent.wait()


if __name__=='__main__':unittest.main()

"""Delivery contract tests with synthetic data; no production acceptance claim."""
import ast
import copy
from pathlib import Path
import tempfile
import unittest
from ceh_video.delivery import validate_source_content,bundle_engine

ROOT=Path(__file__).parents[1]/'ceh_video'
def function(filename,name,**context):
    node=next(n for n in ast.parse((ROOT/'runtime'/filename).read_text()).body if isinstance(n,ast.FunctionDef) and n.name==name)
    exec(compile(ast.Module(body=[node],type_ignores=[]),filename,'exec'),context)
    return context[name]

class RemasterDeliveryTests(unittest.TestCase):
    def test_content_payload_is_exact_while_release_envelope_changes(self):
        old={'scenes':[{'id':'S01','narration_en_US':'Original words.'}],'narration_speed_multiplier':1.5}
        new=copy.deepcopy(old);new.update(narration_speed_multiplier=1.4,voice={'baseline_speed':.73,'postprocess':'exactly one atempo=1.4 on spoken clips'})
        questions={'questions':[{'scene_id':'S01','answer':'A'}]}
        profile={'design_profile':'m10-editorial-remaster-v1.1'}
        validate_source_content(profile,old,new,questions,questions)
        for mutation in ['words','question','tempo']:
            changed=copy.deepcopy(new);q=copy.deepcopy(questions)
            if mutation=='words':changed['scenes'][0]['narration_en_US']='Rewritten words.'
            if mutation=='question':q['questions'][0]['answer']='B'
            if mutation=='tempo':changed['narration_speed_multiplier']=1.5
            with self.assertRaises(AssertionError):validate_source_content(profile,old,changed,questions,q)
        with self.assertRaises(AssertionError):validate_source_content({},old,new,questions,questions)
    def test_integer_chapter_metadata_wins_over_rounded_seconds(self):
        metadata=function('assemble_master.py','metadata_lines')
        rows=metadata({'title':'Example'},[{'id':'C01','title':'Chapter','start':99,'duration':99,'start_sample':1600,'duration_samples':3200}])
        self.assertIn('START=1600',rows);self.assertIn('END=4800',rows)
    def test_worker_bounds_reject_bool_float_and_out_of_range(self):
        workers=function('chapter.py','render_workers')
        for n in [1,2,4]:self.assertEqual(workers({'runtime':{'render_workers':n}}),n)
        for n in [True,0,5,1.0,'2']:
            with self.assertRaises(ValueError):workers({'runtime':{'render_workers':n}})
    def test_aac_residue_counts_channel_samples_without_zero_claim(self):
        import numpy as np
        residue=function('audit_audio_continuity.py','hold_residue',np=np)
        data=np.zeros((48002,2),dtype='float32');data[1,0]=1/32768;data[48000,1]=-2/32768
        report=residue(data,1,48001)
        self.assertEqual(report['frames'],48000);self.assertEqual(report['nonzero_channel_samples'],2)
        self.assertEqual(report['peak_pcm16_units'],2);self.assertGreater(report['rms_normalized'],0)
        with self.assertRaises(AssertionError):residue(data,0,48003)
    def test_bundle_uses_maintained_source_replaces_stale_engine(self):
        with tempfile.TemporaryDirectory() as tmp:
            target=Path(tmp)/'vendor/ceh_video';target.mkdir(parents=True);(target/'stale.py').write_text('stale')
            manifest=bundle_engine(target)
            self.assertFalse((target/'stale.py').exists())
            self.assertEqual((target/'delivery.py').read_bytes(),(ROOT/'delivery.py').read_bytes())
            self.assertIn('visual/package-lock.json',manifest)
            self.assertFalse(any('node_modules' in name or '__pycache__' in name for name in manifest))
    def test_portable_cache_restoration_checks_provenance_and_never_transforms(self):
        from types import SimpleNamespace
        from ceh_video.common import write,sha
        from ceh_video.speech import recipe,baseline_recipe,valid_cache
        from ceh_video.delivery import restore_packaged_audio_cache
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=SimpleNamespace(root=root,state=root/'.production',profile={'audio_policy':'ceh-en-v1.1','voice':{'name':'af_heart','language':'en-us','baseline_speed':.73,'atempo':1.4,'speed_applications':1},'models':{},'runtime':{'ffmpeg':'fixture'}})
            write(root/'pronunciation.json',{'spell':[],'pronunciations':{}})
            for name,data in [('raw.wav',b'raw-reference'),('processed.wav',b'processed-reference'),('meta.json',b'{}')]: (root/name).write_bytes(data)
            item={'canonical':'Hello.','baseline':'raw.wav','processed':'processed.wav','metadata':'meta.json','baseline_receipt':{'recipe':baseline_recipe(p,'Hello.'),'sha256':sha(root/'raw.wav')},'processed_receipt':{'recipe':recipe(p,'Hello.'),'baseline_sha256':sha(root/'raw.wav'),'processed_sha256':sha(root/'processed.wav'),'metadata_sha256':sha(root/'meta.json')}}
            write(root/'provenance/audio-restore.json',{'items':[item]})
            result=restore_packaged_audio_cache(p);self.assertEqual(result['clips'],1);self.assertEqual(result['tempo_passes'],0);self.assertTrue(valid_cache(p,'Hello.'))
            (root/'raw.wav').write_bytes(b'changed')
            with self.assertRaises(AssertionError):restore_packaged_audio_cache(p)

    def test_prepare_reuse_requires_current_check_and_review(self):
        from types import SimpleNamespace
        from unittest.mock import patch
        from ceh_video.common import write
        from ceh_video.runner import checked_prepare_ready
        with tempfile.TemporaryDirectory() as tmp:
            p=SimpleNamespace(qa=Path(tmp),chapter_inputs=lambda ch:'current')
            clean={'ok':True,'browserSkipped':False,**{k:{'errorCount':0,'warningCount':0} for k in ['lint','runtime','layout','contrast']}}
            write(p.qa/'C01-checked-fingerprint.json',{'sha256':'current'});write(p.qa/'C01-check.json',clean)
            with patch('ceh_video.review.require_review',return_value={'decision':'pass'}) as review:
                self.assertTrue(checked_prepare_ready(p,'C01'));review.assert_called_once_with(p,'C01')
                write(p.qa/'C01-checked-fingerprint.json',{'sha256':'stale'});self.assertFalse(checked_prepare_ready(p,'C01'))
                write(p.qa/'C01-checked-fingerprint.json',{'sha256':'current'})
                for change in ['warning','error','browser','failed']:
                    changed=copy.deepcopy(clean)
                    if change=='warning':changed['layout']['warningCount']=1
                    if change=='error':changed['runtime']['errorCount']=1
                    if change=='browser':changed['browserSkipped']=True
                    if change=='failed':changed['ok']=False
                    write(p.qa/'C01-check.json',changed);self.assertFalse(checked_prepare_ready(p,'C01'))
            write(p.qa/'C01-check.json',clean)
            with patch('ceh_video.review.require_review',side_effect=RuntimeError('Stale capture image')):self.assertFalse(checked_prepare_ready(p,'C01'))

    def test_hardware_probe_rejects_fallback_and_binds_logs(self):
        import re,hashlib
        verify=function('chapter.py','gpu_evidence',re=re,hashlib=hashlib)
        renderer='ANGLE (NVIDIA Corporation, NVIDIA GB10/PCIe, OpenGL ES 3.2)'
        profile={'design_profile':'m10-editorial-remaster-v1.1','runtime':{'browser_gpu_mode':'hardware','expected_gpu_renderer':renderer}}
        with tempfile.TemporaryDirectory() as tmp:
            log=Path(tmp)/'render.log';err=Path(tmp)/'render.log.stderr';log.write_text('render complete')
            hardware=f'[hyperframes] browserGpuMode probe → hardware (WebGL renderer vendor="Google Inc. (NVIDIA Corporation)" renderer="{renderer}")'
            err.write_text(hardware);self.assertEqual(verify(profile,log)['observed_mode'],'hardware')
            for text in ['',hardware.replace('hardware','software'),hardware.replace('NVIDIA GB10','Other GPU'),hardware+' UNVERIFIED']:
                err.write_text(text)
                with self.assertRaises(RuntimeError):verify(profile,log)
    def test_gpu_environment_and_remaster_profile_validation(self):
        import json
        from ceh_video.common import Project,write
        from ceh_video.preflight import validate_profile
        profile={'schema_version':1,'design_profile':'m10-editorial-remaster-v1.1','audio_policy':'ceh-en-v1.1','voice':{'name':'af_heart','language':'en-us','baseline_speed':.73,'atempo':1.4,'speed_applications':1},'output':{'width':1920,'height':1080,'fps':30,'sample_rate':48000,'channels':2,'video_rate':1.0,'bgm':False},'quiz_silence_seconds':1,'runtime':{'max_chapter_renders':2,'render_workers':2,'browser':'/browser','browser_gpu_mode':'hardware','expected_gpu_renderer':'ANGLE (NVIDIA Corporation, NVIDIA GB10/PCIe, OpenGL ES 3.2)'}}
        validate_profile(profile)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);write(root/'production.json',profile);write(root/'data/scenes.json',{'scenes':[]});write(root/'data/questions.json',{'questions':[]})
            self.assertEqual(Project(root).environment()['PRODUCER_BROWSER_GPU_MODE'],'hardware')
        for key,value in [('browser_gpu_mode','auto'),('expected_gpu_renderer','SwiftShader')]:
            changed=copy.deepcopy(profile);changed['runtime'][key]=value
            with self.assertRaises(AssertionError):validate_profile(changed)

    def test_encoded_evidence_survives_extraction_and_rejects_tamper_or_missing(self):
        from types import SimpleNamespace
        import shutil,zipfile
        from ceh_video.common import write,sha
        from ceh_video.delivery import bundle_encoded_evidence,verify_encoded_evidence
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);p=SimpleNamespace(qa=base/'qa',output=base/'output',scenes=[{}],chapters=['C01'],questions=[])
            (p.output/'inspection_frames').mkdir(parents=True);names=['S01-midpoint.png','C01-first.png','C01-middle.png','C01-last.png','S01-late.png']
            # Bytes are synthetic: test package custody, not image appearance.
            for name in names:(p.output/'inspection_frames'/name).write_bytes(name.encode())
            review={'master_sha256':'master-reference','captures':{n:sha(p.output/'inspection_frames'/n) for n in names}}
            write(p.qa/'encoded-review.json',review);write(p.qa/'rendered-artifact-audit.json',{'sampled_frames':[{'file':n} for n in names[:-1]]});write(p.qa/'late-diagram-samples.json',{'samples':[{'file':names[-1]}]})
            staging=base/'staging';shutil.copytree(p.qa,staging/'qa');bundle_encoded_evidence(p,staging)
            archive=base/'images.zip'
            with zipfile.ZipFile(archive,'w') as z:
                for f in staging.rglob('*'):
                    if f.is_file():z.write(f,f.relative_to(staging))
            extracted=base/'extracted'
            with zipfile.ZipFile(archive) as z:z.extractall(extracted)
            self.assertEqual(verify_encoded_evidence(extracted)['frames'],5)
            target=extracted/'output/inspection_frames'/names[0];target.write_bytes(b'tampered')
            with self.assertRaises(AssertionError):verify_encoded_evidence(extracted)
            target.unlink()
            with self.assertRaises(FileNotFoundError):verify_encoded_evidence(extracted)
            (p.output/'inspection_frames'/names[-1]).write_bytes(b'changed-after-review')
            with self.assertRaises(AssertionError):bundle_encoded_evidence(p,base/'stale')

    def test_processing_and_render_runtime_have_separate_graph_fingerprints(self):
        from ceh_video.common import Project,write
        from ceh_video.graph import nodes
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            profile={'schema_version':1,'voice':{'name':'af_heart','language':'en-us','baseline_speed':.73,'atempo':1.5,'speed_applications':1},'models':{},'alignment':{},'output':{},'diagram_inputs':{},'runtime':{'ffmpeg':'ffmpeg-A','hyperframes':'0.8.174','browser':'/pinned/browser','render_workers':1},'master_filename':'master.mp4','editable_filename':'project.zip'}
            scene={'id':'S01','chapter_id':'C01','narration_en_US':'Hello.','audio_segments':[{'kind':'spoken','text':'Hello.'}]}
            write(root/'production.json',profile);write(root/'data/scenes.json',{'scenes':[scene]});write(root/'data/questions.json',{'questions':[]});write(root/'pronunciation.json',{'spell':[],'pronunciations':{}})
            p=Project(root);before=nodes(p)
            p.profile['runtime']['ffmpeg']='ffmpeg-B';changed=nodes(p)
            self.assertNotEqual(before['speech:S01'].inputs,changed['speech:S01'].inputs)
            self.assertEqual(before['render:C01'].inputs,changed['render:C01'].inputs)
            p.profile['runtime']['ffmpeg']='ffmpeg-A';p.profile['runtime']['render_workers']=2;changed=nodes(p)
            self.assertEqual(before['speech:S01'].inputs,changed['speech:S01'].inputs)
            self.assertNotEqual(before['render:C01'].inputs,changed['render:C01'].inputs)
            p.profile['runtime']['render_workers']=1;p.profile['runtime']['browser']='/different/browser';changed=nodes(p)
            self.assertEqual(before['speech:S01'].inputs,changed['speech:S01'].inputs)
            self.assertNotEqual(before['render:C01'].inputs,changed['render:C01'].inputs)


    def test_extracted_golden_reviews_reject_missing_and_tampered_evidence(self):
        from ceh_video.common import write,sha
        from ceh_video.delivery import verify_golden_review_evidence
        with tempfile.TemporaryDirectory() as temp:
            base=Path(temp);qa=base/'qa'
            candidate=qa/'visual/candidate-final-manifest.json'
            write(candidate,{'status':'candidate_baseline_review_required','rows':[{'scene':'S01'}]})
            names=['early-candidate-review-final-freeze/review.json',
                   'visual/agent-review-late-port-normal-final/candidate-review.json']
            for name in names:write(qa/name,{'status':'agent_sampled_visual_review_passed','scope':name})
            approval={'decision':'approved_initial_golden','candidate_sha256':sha(candidate),
                      'review_receipts':{name:sha(qa/name) for name in names}}
            write(qa/'visual/golden-approval.json',approval)
            result=verify_golden_review_evidence(base)
            self.assertEqual(result['review_receipts'],approval['review_receipts'])
            for name in names:
                target=qa/name;original=target.read_bytes();target.unlink()
                with self.assertRaises(FileNotFoundError):verify_golden_review_evidence(base)
                target.write_bytes(original+b' ')
                with self.assertRaisesRegex(AssertionError,'receipt changed'):verify_golden_review_evidence(base)
                target.write_bytes(original)
            original=candidate.read_bytes();candidate.write_bytes(original+b' ')
            with self.assertRaisesRegex(AssertionError,'candidate manifest changed'):verify_golden_review_evidence(base)
            candidate.write_bytes(original)
            incomplete=copy.deepcopy(approval);del incomplete['review_receipts'][names[0]]
            write(qa/'visual/golden-approval.json',incomplete)
            with self.assertRaisesRegex(AssertionError,'Incomplete golden'):verify_golden_review_evidence(base)


    def test_boundary_evidence_copy_excludes_linked_hosts_retains_evidence(self):
        import shutil
        from ceh_video.delivery import copy_remaster_qa
        with tempfile.TemporaryDirectory() as temp:
            base=Path(temp);source=base/'remaster-boundaries';source.mkdir()
            (source/'report.json').write_text('{"status":"passed"}')
            (source/'S01-S02-exact.png').write_bytes(b'actual-capture-fixture')
            linked=base/'large-media';linked.mkdir();(linked/'must-not-be-copied.wav').write_bytes(b'media')
            host=source/'hosts'/'C01';host.mkdir(parents=True)
            (host/'assets').symlink_to(linked,target_is_directory=True)
            # A dangling link would make ordinary following copytree fail.
            (host/'missing-runtime').symlink_to(base/'unavailable-runtime',target_is_directory=True)
            target=base/'archive/qa/remaster-boundaries'
            copy_remaster_qa(source,target,shutil.ignore_patterns('__pycache__'))
            self.assertFalse((target/'hosts').exists())
            self.assertEqual((target/'report.json').read_bytes(),(source/'report.json').read_bytes())
            self.assertEqual((target/'S01-S02-exact.png').read_bytes(),b'actual-capture-fixture')
            self.assertEqual(sorted(p.name for p in target.iterdir()),['S01-S02-exact.png','report.json'])
            # The exclusion is scoped to the boundary harness's derived root.
            other=base/'remaster-assets';(other/'hosts').mkdir(parents=True)
            (other/'hosts/evidence.json').write_text('{}')
            copy_remaster_qa(other,base/'archive/qa/remaster-assets',lambda folder,names:[])
            self.assertTrue((base/'archive/qa/remaster-assets/hosts/evidence.json').is_file())

if __name__=='__main__':unittest.main()

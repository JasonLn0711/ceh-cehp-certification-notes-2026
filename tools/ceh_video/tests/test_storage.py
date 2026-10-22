"""Storage changes must preserve releases and clean only their own temporary files."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

from ceh_video.archive_io import partial_archive
from ceh_video.common import sha, write, read
from ceh_video.mandarin_package import package, payload_files, release_files
from ceh_video.storage import audit


class StorageTests(unittest.TestCase):
    def test_inode_accounting_and_symlink_boundary(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);(root/'project').mkdir()
            f=root/'project/source';f.write_bytes(b'x'*8192)
            os.link(f,root/'project/alias')
            (root/'external').symlink_to('/tmp',target_is_directory=True)
            row=audit(root)
            self.assertEqual(row['logical_bytes'],8192)
            self.assertEqual(row['files'],1)
            self.assertEqual(row['hardlink_entries_not_recounted'],1)
            self.assertEqual(row['symlinks_skipped'],1)
            self.assertIsNone(row['reclaimable_bytes'])
            self.assertEqual(f.read_bytes(),b'x'*8192)

    def test_cli_json_and_failure(self):
        with tempfile.TemporaryDirectory() as t:
            run=subprocess.run([sys.executable,'-m','ceh_video.storage','--plain',t],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            self.assertTrue(json.loads(run.stdout)['workspaces'][0]['read_only'])
            self.assertNotIn('\x1b',run.stderr)
            run=subprocess.run([sys.executable,'-m','ceh_video.storage',t+'/missing'],capture_output=True,text=True)
            self.assertEqual(run.returncode,1)
            self.assertEqual(json.loads(run.stdout)['status'],'failed')

    def test_owned_partial_cleanup_does_not_touch_prior_archive(self):
        with tempfile.TemporaryDirectory() as t:
            target=Path(t)/'release.zip';target.write_bytes(b'old')
            stale=Path(t)/'release.zip.partial-older';stale.write_bytes(b'keep')
            with self.assertRaises(KeyboardInterrupt):
                with partial_archive(target) as scratch:
                    scratch.write_bytes(b'new');raise KeyboardInterrupt()
            self.assertFalse(scratch.exists())
            self.assertEqual(target.read_bytes(),b'old')
            self.assertEqual(stale.read_bytes(),b'keep')


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        home=Path(self.tmp.name)
        self.p=SimpleNamespace(root=home/'project',output=home/'output',qa=home/'qa',
                              profile={'master_filename':'film.mp4','editable_filename':'edit.zip','archive_prefix':'fixture'})
        for folder in (self.p.root,self.p.output,self.p.qa):folder.mkdir()
        self.movie=self.p.output/'film.mp4';self.movie.write_bytes(b'fixture encoded artifact')
        self.script=self.p.root/'SCRIPT.md';self.script.write_text('授權教材')
        write(self.p.qa/'engine-delivery.json',{'status':'rendered_automated_checks_passed','master_sha256':sha(self.movie)})
        self.files=[(self.script,'project/SCRIPT.md'),(self.movie,'output/film.mp4')]
        self.target=self.p.output/'edit.zip'
        self.gate=patch('ceh_video.review.require_encoded');self.gate.start();self.addCleanup(self.gate.stop)
        self.payload=patch('ceh_video.mandarin_package.release_files',return_value=self.files)
        self.payload.start();self.addCleanup(self.payload.stop)

    def assert_no_scratch(self):
        self.assertEqual(list(self.p.output.glob('verify-package-*')),[])
        self.assertEqual(list(self.p.output.glob('*.partial-*')),[])

    def test_verified_archive_has_exact_payload_and_no_retained_copy(self):
        events=[];result=package(self.p,events.append)
        with zipfile.ZipFile(self.target) as z:
            self.assertIsNone(z.testzip())
            self.assertEqual(z.read('fixture/project/SCRIPT.md'),self.script.read_bytes())
            self.assertEqual(z.getinfo('fixture/output/film.mp4').compress_type,zipfile.ZIP_STORED)
        self.assertEqual(result['zip_sha256'],sha(self.target))
        self.assertFalse(result['verification_workspace_retained'])
        self.assertFalse((self.p.root/'vendor').exists())
        self.assert_no_scratch()

    def test_closed_release_is_immutable(self):
        self.target.write_bytes(b'original')
        with self.assertRaisesRegex(RuntimeError,'Closed release'):
            package(self.p,lambda row:None)
        self.assertEqual(self.target.read_bytes(),b'original')
        self.assert_no_scratch()

    def test_english_archive_without_receipt_is_preserved(self):
        from ceh_video.packaging import package as english_package
        self.target.write_bytes(b'closed without receipt')
        with self.assertRaisesRegex(RuntimeError,'Incomplete closed release'):
            english_package(self.p,lambda row:None)
        self.assertEqual(self.target.read_bytes(),b'closed without receipt')
        self.assert_no_scratch()

    def test_disk_shortage_fails_before_writing_archive(self):
        with patch('shutil.disk_usage',return_value=SimpleNamespace(free=0)):
            with self.assertRaisesRegex(RuntimeError,'Insufficient'):
                package(self.p,lambda row:None)
        self.assertFalse(self.target.exists());self.assert_no_scratch()

    def test_extraction_failure_does_not_publish_and_cleans_up(self):
        with patch('zipfile.ZipFile.extractall',side_effect=OSError('disk full')):
            with self.assertRaisesRegex(OSError,'disk full'):
                package(self.p,lambda row:None)
        self.assertFalse(self.target.exists());self.assert_no_scratch()
        self.assertFalse((self.p.qa/'engine-packaging.json').exists())

    def test_interrupt_does_not_publish_and_cleans_up(self):
        with patch('zipfile.ZipFile.extractall',side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):package(self.p,lambda row:None)
        self.assertFalse(self.target.exists());self.assert_no_scratch()

    def test_source_changed_during_write_is_rejected(self):
        original=zipfile.ZipFile.open
        def changed(archive,name,mode='r',*args,**kwargs):
            if mode=='w' and name.filename.endswith('SCRIPT.md'):
                self.script.write_text('changed')
            return original(archive,name,mode,*args,**kwargs)
        with patch('zipfile.ZipFile.open',changed):
            with self.assertRaisesRegex(RuntimeError,'Source changed'):
                package(self.p,lambda row:None)
        self.assertFalse(self.target.exists());self.assert_no_scratch()

    def test_corrupt_extracted_payload_is_rejected(self):
        original=zipfile.ZipFile.extractall
        def corrupt(archive,path,*args,**kwargs):
            original(archive,path,*args,**kwargs)
            (Path(path)/'fixture/project/SCRIPT.md').write_text('wrong')
        with patch('zipfile.ZipFile.extractall',corrupt):
            with self.assertRaisesRegex(RuntimeError,'Extracted payload'):
                package(self.p,lambda row:None)
        self.assertFalse(self.target.exists());self.assert_no_scratch()

    def test_master_hash_mismatch_blocks_packaging(self):
        self.movie.write_bytes(b'changed')
        with self.assertRaisesRegex(RuntimeError,'master hash'):
            package(self.p,lambda row:None)
        self.assertFalse(self.target.exists())


class InventoryTests(unittest.TestCase):
    def test_payload_excludes_current_verification_and_retains_voice(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);p=SimpleNamespace(root=root/'project',qa=root/'qa',output=root/'output')
            for rel in ['project/.production/speech-cache/clip.wav','output/verify-package-123/old.mp4',
                        'project/vendor/ceh_video/obsolete.py','project/node_modules/large.js']:
                f=root/rel;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b'fixture')
            rows=dict((rel,f) for f,rel in release_files(p))
            self.assertIn('project/.production/speech-cache/clip.wav',rows)
            self.assertIn('project/vendor/ceh_video/ceh_video/archive_io.py',rows)
            self.assertNotIn('project/vendor/ceh_video/obsolete.py',rows)
            self.assertFalse(any('verify-package-' in rel or 'node_modules' in rel for rel in rows))

    def test_unknown_symlink_cannot_silently_omit_required_source(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);p=SimpleNamespace(root=root/'project',qa=root/'qa',output=root/'output')
            p.root.mkdir();(p.root/'source').symlink_to('/tmp',target_is_directory=True)
            with self.assertRaisesRegex(ValueError,'directory link'):payload_files(p)


class PracticePackageTests(unittest.TestCase):
    def fixture(self, home):
        root=home/'lesson';project=home/'workspace/project';output=project.parent/'output'
        project.mkdir(parents=True);output.mkdir()
        (project/'voice.wav').write_bytes(b'authorized voice fixture')
        videos=[]
        for i in range(6):
            f=output/f'film-{i}.mp4';f.write_bytes(f'encoded fixture {i}'.encode())
            videos.append({'file':f.name,'sha256':sha(f)})
        write(root/'validation/delivery-media.json',{'full_decode':'passed','visual_review':'passed','videos':videos})
        return root,project,output

    def test_actual_package_preserves_inputs_without_extracted_tree(self):
        from ceh_video.practice_package import package as practice
        with tempfile.TemporaryDirectory() as t:
            root,project,output=self.fixture(Path(t))
            result=practice(root,project,lambda row:None)
            self.assertEqual(result['payload_hashes'],'passed')
            self.assertEqual(result['verification_extraction_bytes'],0)
            with zipfile.ZipFile(result['file']) as z:
                self.assertEqual(z.read('review-video-03/project/voice.wav'),b'authorized voice fixture')
                self.assertIn('review-video-03/engine/ceh_video/practice_package.py',z.namelist())
            before=sha(result['file'])
            with self.assertRaisesRegex(RuntimeError,'Closed delivery'):practice(root,project,lambda row:None)
            self.assertEqual(sha(result['file']),before)

    def test_stale_video_receipt_blocks_release(self):
        from ceh_video.practice_package import package as practice
        with tempfile.TemporaryDirectory() as t:
            root,project,output=self.fixture(Path(t))
            (output/'film-0.mp4').write_bytes(b'changed')
            with self.assertRaisesRegex(RuntimeError,'video hash mismatch'):practice(root,project,lambda row:None)
            self.assertFalse((output/'third-video-DELIVERY.zip').exists())

    def test_stream_verification_detects_source_mutation(self):
        from ceh_video.archive_io import verified_stream_archive
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);f=root/'source';f.write_bytes(b'original');target=root/'archive.zip'
            original=zipfile.ZipFile.write
            def changed(archive,filename,*args,**kwargs):
                f.write_bytes(b'changed')
                return original(archive,filename,*args,**kwargs)
            with patch('zipfile.ZipFile.write',changed):
                with self.assertRaisesRegex(RuntimeError,'payload differs'):
                    verified_stream_archive([(f,'source')],target,lambda row:None)
            self.assertFalse(target.exists())
            self.assertEqual(list(root.glob('*.partial-*')),[])

    def test_stream_verification_interrupt_and_duplicate_names(self):
        from ceh_video.archive_io import verified_stream_archive
        with tempfile.TemporaryDirectory() as t:
            root=Path(t);f=root/'source';f.write_bytes(b'original');target=root/'archive.zip'
            with self.assertRaisesRegex(ValueError,'Duplicate'):
                verified_stream_archive([(f,'a'),(f,'a')],target,lambda row:None)
            with patch('zipfile.ZipFile.write',side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    verified_stream_archive([(f,'a')],target,lambda row:None)
            self.assertFalse(target.exists())
            self.assertEqual(list(root.glob('*.partial-*')),[])


if __name__=='__main__':unittest.main()

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile
from ceh_video.compact_archive import write_compact
from ceh_video.compact_restore import restore
from ceh_video.pcm_reuse import concatenate


class CompactTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.archive = self.root/'release.zip'

    def test_offline_roundtrip_duplicates_unicode_empty_modes(self):
        f=self.root/'script';f.write_bytes(b'echo hi\n');f.chmod(0o755)
        result=write_compact([(f,'project/run.sh'),(f,'project/副本.sh'),(b'','empty')],self.archive)
        self.assertEqual(result['unique_objects'],2)
        self.assertEqual(result['duplicate_bytes'],8)
        out=self.root/'out'
        env={'PATH':'/usr/bin:/bin'}
        subprocess.run([sys.executable,'-I',str(self.root/'RESTORE.py'),'--archive',str(self.archive),'--destination',str(out)],check=True,capture_output=True,env=env)
        self.assertEqual((out/'project/run.sh').stat().st_mode&0o777,0o755)
        self.assertNotEqual((out/'project/run.sh').stat().st_ino,(out/'project/副本.sh').stat().st_ino)
        (out/'project/run.sh').write_bytes(b'changed')
        self.assertEqual((out/'project/副本.sh').read_bytes(),b'echo hi\n')
        with self.assertRaises(FileExistsError):restore(self.archive,out)
        with self.assertRaises(FileExistsError):write_compact([],self.archive)

    def test_unsafe_paths_and_links(self):
        for name in ('../escape','/root','a/../b','a\\b','a//b','./a','C:/a'):
            with self.subTest(name=name),self.assertRaises(ValueError):
                write_compact([(b'x',name)],self.archive)
        f=self.root/'link';f.symlink_to('/etc/hosts')
        with self.assertRaises(ValueError):write_compact([(f,'x')],self.archive)
        self.assertFalse(self.archive.exists())

    def test_conflicts_fail_before_publication(self):
        for entries in ([(b'x','a'),(b'y','a')],[(b'x','a'),(b'y','a/b')]):
            with self.assertRaises(ValueError):write_compact(entries,self.archive)
        self.assertFalse(self.archive.exists())
        self.assertFalse(list(self.root.glob('*.partial-*')))

    def test_no_space_and_interrupt_cleanup(self):
        with patch('ceh_video.compact_archive.shutil.disk_usage',return_value=SimpleNamespace(free=0)):
            with self.assertRaises(OSError):write_compact([(b'x','a')],self.archive)
        def interrupted(_):raise KeyboardInterrupt()
        with self.assertRaises(KeyboardInterrupt):write_compact([(b'x','a')],self.archive,verify=interrupted)
        self.assertEqual(list(self.root.iterdir()),[])

    def forged(self, path='a', payload=b'bad', missing=False, mode=0o644, link=False):
        h=hashlib.sha256(b'expected').hexdigest()
        with zipfile.ZipFile(self.archive,'w') as z:
            z.writestr('COMPACT_MANIFEST.json',json.dumps({'format':'compact-v1','files':[{'path':path,'sha256':h,'bytes':len(payload),'mode':mode}]}))
            z.writestr('RESTORE.py','')
            if not missing:
                info=zipfile.ZipInfo('objects/'+h)
                if link:info.external_attr=0o120777<<16
                z.writestr(info,payload)

    def test_corrupt_missing_symlink_and_privileged_mode(self):
        for kwargs in ({},{'missing':True},{'link':True},{'mode':0o4755},{'path':'../a'}):
            self.forged(**kwargs)
            with self.assertRaises((ValueError,KeyError)):restore(self.archive,self.root/'out')
            self.assertFalse((self.root/'out').exists())
            self.assertFalse(list(self.root.glob('.compact-restore-*')))

    def test_restore_capacity_and_destination_symlink(self):
        write_compact([(b'x','a')],self.archive)
        out=self.root/'out'
        with patch('ceh_video.compact_restore.shutil.disk_usage',return_value=SimpleNamespace(free=0)):
            with self.assertRaises(OSError):restore(self.archive,out)
        out.symlink_to(self.root/'missing')
        with self.assertRaises(FileExistsError):restore(self.archive,out)


class PCMTests(unittest.TestCase):
    def test_reuse_force_mutation_and_failure(self):
        import numpy as np
        import soundfile as sf
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);p=SimpleNamespace(state=root/'.production')
            source=root/'source.wav';out=root/'out.wav'
            sf.write(source,np.zeros((1600,2),dtype='int16'),48000,subtype='PCM_16')
            self.assertEqual(concatenate(p,[source],out),1600)
            before=out.stat().st_mtime_ns
            concatenate(p,[source],out)
            self.assertEqual(out.stat().st_mtime_ns,before)
            concatenate(p,[source],out,force=True)
            self.assertNotEqual(out.stat().st_mtime_ns,before)
            out.write_bytes(b'corrupt');concatenate(p,[source],out)
            self.assertEqual(sf.info(out).frames,1600)
            sf.write(source,np.ones((3200,2),dtype='int16'),48000,subtype='PCM_16')
            self.assertEqual(concatenate(p,[source],out),3200)
            with patch('soundfile.SoundFile',side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):concatenate(p,[source],out,force=True)
            self.assertFalse(list((p.state/'pcm').glob('*.json')))
            self.assertFalse(list(root.glob('*.partial-*')))

class RouteTests(unittest.TestCase):
    def test_mandarin_compact_route(self):
        from test_storage import PackageTests
        from ceh_video.mandarin_package import package
        fixture=PackageTests();fixture.setUp();self.addCleanup(fixture.doCleanups)
        fixture.p.profile['package_format']='compact-v1'
        result=package(fixture.p,lambda _:None)
        self.assertEqual(result['format'],'compact-v1')
        self.assertTrue((fixture.p.output/'RESTORE.py').exists())
        self.assertFalse(result['verification_workspace_retained'])

    def test_practice_compact_route(self):
        from test_storage import PracticePackageTests
        from ceh_video.practice_package import package
        from ceh_video.common import write
        with tempfile.TemporaryDirectory() as temp:
            root,project,output=PracticePackageTests().fixture(Path(temp))
            write(project/'production.json',{'package_format':'compact-v1'})
            result=package(root,project,lambda _:None)
            self.assertEqual(result['format'],'compact-v1')
            self.assertTrue((output/'RESTORE.py').exists())

class PublicationFailureTests(unittest.TestCase):
    def test_promotion_failure_removes_only_new_companions(self):
        with tempfile.TemporaryDirectory() as temp:
            import os
            root=Path(temp);archive=root/'release.zip';original=os.link
            def replace(source,target):
                if Path(target)==archive:raise OSError('simulated promotion failure')
                return original(source,target)
            with patch('ceh_video.compact_archive.os.link',replace),self.assertRaises(OSError):
                write_compact([(b'x','a')],archive)
            self.assertEqual(list(root.iterdir()),[])
            good=root/'good.zip';write_compact([(b'x','a')],good)
            before=(root/'RESTORE.py').read_bytes()
            with patch('ceh_video.compact_archive.os.link',replace),self.assertRaises(OSError):
                write_compact([(b'x','a')],archive)
            self.assertEqual((root/'RESTORE.py').read_bytes(),before)
            self.assertTrue(good.exists())
            self.assertFalse((root/'release.zip.sha256').exists())

    def test_reconstruction_capacity_reserve_is_enforced(self):
        with tempfile.TemporaryDirectory() as temp:
            archive=Path(temp)/'release.zip'
            with patch('ceh_video.compact_archive.shutil.disk_usage',return_value=SimpleNamespace(free=128*1024*1024+100)):
                with self.assertRaises(OSError):write_compact([(b'x','a')],archive,extra_restore_bytes=1024)
            self.assertFalse(archive.exists())

class ConcurrentDestinationTests(unittest.TestCase):
    def test_archive_appearing_during_verification_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);target=root/'release.zip'
            def competing_release(_):target.write_bytes(b'other release')
            with self.assertRaises(FileExistsError):write_compact([(b'x','a')],target,verify=competing_release)
            self.assertEqual(target.read_bytes(),b'other release')
            self.assertFalse((root/'release.zip.sha256').exists())
            self.assertFalse((root/'RESTORE.py').exists())
            self.assertFalse(list(root.glob('*.partial-*')))

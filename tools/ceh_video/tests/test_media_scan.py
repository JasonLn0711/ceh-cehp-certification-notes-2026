"""Real decoder regression: count, black detection, integrity and bound reuse."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from ceh_video.media_scan import scan_master, require_scan

class MediaScanTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name); self.movie = self.root/'movie.mp4'
        self.make_movie('white')

    def make_movie(self, color):
        subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color={color}:s=64x64:r=30:d=1',
                        '-f','lavfi','-i','sine=frequency=440:sample_rate=48000:duration=1',
                        '-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-ac','2',str(self.movie)],check=True)

    def test_real_decode_count_and_reuse(self):
        row=scan_master(self.movie,30,self.root)
        self.assertEqual(row['decoded_frames'],30)
        self.assertEqual(row['black_intervals'],0)
        self.assertEqual(require_scan(self.movie,30,self.root),row)
        with self.assertRaises(ValueError): require_scan(self.movie,31,self.root)

    def test_black_rejected_and_no_pass_receipt(self):
        self.make_movie('black')
        with self.assertRaises(ValueError): scan_master(self.movie,30,self.root)
        self.assertFalse((self.root/'master-full-decode.json').exists())

    def test_incorrect_count_rejected(self):
        with self.assertRaises(ValueError): scan_master(self.movie,31,self.root)

    def test_changed_movie_and_log_rejected(self):
        scan_master(self.movie,30,self.root)
        log=self.root/'master-full-decode.log'; original=log.read_bytes();log.write_bytes(original+b'changed')
        with self.assertRaises(ValueError): require_scan(self.movie,30,self.root)
        log.write_bytes(original);self.make_movie('red')
        with self.assertRaises(ValueError): require_scan(self.movie,30,self.root)

    def test_failed_retry_cannot_leave_success(self):
        scan_master(self.movie,30,self.root)
        with self.assertRaises(ValueError): scan_master(self.movie,31,self.root)
        self.assertFalse((self.root/'master-full-decode.json').exists())

class ProgressEvidenceTests(unittest.TestCase):
    def test_terminal_progress_is_required_and_last_count_wins(self):
        from ceh_video.media_scan import decoded_count
        self.assertEqual(decoded_count('frame=2\nprogress=continue\nframe=30\nprogress=end\n'),30)
        for text in ('frame=30\nprogress=continue\n','progress=end\n','frame=30\n'):
            with self.assertRaises(ValueError):decoded_count(text)

if __name__=='__main__':unittest.main()

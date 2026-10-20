"""One full decode proves frame count, decoder integrity and absence of black.

Only the actual decoder's terminal progress counts as frame evidence. Container
headers and expected timeline counts never substitute for decoded frames.
"""
from pathlib import Path
import json
import shutil
import subprocess
import time

from .common import read, sha, write

RECEIPT = 'master-full-decode.json'
LOG = 'master-full-decode.log'
PROGRESS = 'master-full-decode.progress'


def decoder_identity():
    executable = Path(shutil.which('ffmpeg')).resolve()
    return {'binary_sha256': sha(executable),
            'version': subprocess.check_output(
                [str(executable), '-version'], text=True),
            'implementation_sha256': sha(__file__)}


def scan_command(movie, progress):
    return ['ffmpeg', '-v', 'info', '-nostats', '-xerror',
            '-err_detect', 'explode', '-i', str(movie),
            '-map', '0:v:0', '-map', '0:a:0?',
            '-vf', 'blackdetect=d=0.1:pix_th=0.1',
            '-fps_mode', 'passthrough', '-progress', str(progress),
            '-f', 'null', '-']


def decoded_count(progress):
    rows = [line.split('=', 1) for line in progress.splitlines() if '=' in line]
    values = dict(rows)
    if values.get('progress') != 'end' or 'frame' not in values:
        raise ValueError('Full decode did not emit terminal frame evidence')
    return int(values['frame'])


def require_scan(movie, expected_frames, qa):
    qa = Path(qa); row = read(qa/RECEIPT)
    expected = {
        'status': 'passed', 'master_sha256': sha(movie),
        'decoded_frames': expected_frames, 'black_intervals': 0,
        'decoder': decoder_identity(),
        'log_sha256': sha(qa/LOG), 'progress_sha256': sha(qa/PROGRESS),
        'command': scan_command(movie, qa/PROGRESS),
    }
    if any(row.get(key) != value for key, value in expected.items()):
        raise ValueError('Full-decode receipt is stale, incomplete or changed')
    if decoded_count((qa/PROGRESS).read_text()) != expected_frames:
        raise ValueError('Decoded count does not match timeline')
    if 'black_start:' in (qa/LOG).read_text():
        raise ValueError('Black interval detected')
    return row


def scan_master(movie, expected_frames, qa):
    movie = Path(movie); qa = Path(qa); qa.mkdir(parents=True, exist_ok=True)
    # A failed retry must never leave a passing receipt from its predecessor.
    (qa/RECEIPT).unlink(missing_ok=True)
    (qa/PROGRESS).unlink(missing_ok=True)
    began = time.monotonic(); before = sha(movie); decoder = decoder_identity()
    command = scan_command(movie, qa/PROGRESS)
    print(json.dumps({'phase': 'full_decode_start', 'expected_frames': expected_frames,
                      'progress_file': str(qa/PROGRESS)}), flush=True)
    with (qa/LOG).open('w') as log:
        subprocess.run(command, check=True, stdout=log, stderr=log)
    count = decoded_count((qa/PROGRESS).read_text())
    if count != expected_frames:
        raise ValueError(f'Decoded {count} frames; expected {expected_frames}')
    if 'black_start:' in (qa/LOG).read_text():
        raise ValueError('Black interval detected')
    if sha(movie) != before or decoder_identity() != decoder:
        raise ValueError('Movie or decoder changed during full decode')
    row = dict(status='passed', master_sha256=before, decoded_frames=count,
               black_intervals=0, decoder=decoder, command=command,
               log_sha256=sha(qa/LOG), progress_sha256=sha(qa/PROGRESS),
               elapsed_seconds=time.monotonic()-began)
    write(qa/RECEIPT, row)
    print(json.dumps({'phase': 'full_decode_passed', 'decoded_frames': count,
                      'elapsed_seconds': row['elapsed_seconds']}), flush=True)
    return row

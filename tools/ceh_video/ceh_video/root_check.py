"""Check the complete visual composition without decoding duplicate long audio.

The production host is unchanged. PCM, AAC and encoded-media checks own audio.
"""
from pathlib import Path
import re
import subprocess
import sys
from .common import Project, read, sha, write


def visual_only(source):
    return re.sub(r'<audio\b[^>]*>[\s\S]*?</audio\s*>|<audio\b[^>]*/\s*>',
                  '', source, flags=re.I)


def validate_report(report, times):
    assert report['ok'] and not report['browserSkipped']
    for layer in ('lint', 'runtime', 'layout', 'contrast'):
        assert report[layer]['errorCount'] == report[layer]['warningCount'] == 0
    assert report['contrast']['enabled'] and report['contrast']['checked'] > 0
    samples = report['layout']['samples']
    # Native layout samples are timestamp numbers in the pinned runtime.
    actual = [float(x) for x in samples]
    assert len(actual) == len(set(actual)) == len(times)
    assert all(abs(a-b) < .001 for a,b in zip(sorted(actual), sorted(times)))


def require_current(p):
    folder = p.qa/'root-visual-check'
    manifest = read(folder/'source-transform.json')
    report = read(p.qa/'master-project-check.json')
    partition = report['verification_partition']
    assert partition['source_manifest_sha256'] == sha(folder/'source-transform.json')
    assert partition['implementation_sha256'] == manifest['implementation_sha256'] == sha(Path(__file__))
    assert manifest['runtime'] == p.profile['runtime']
    assert manifest['config_sha256'] == sha(p.root/'hyperframes.json')
    assert set(manifest['sources']) == {'index.html', *[f'compositions/{s}.html' for s in p.by_id]}
    assert all(sha(p.root/name) == row['source_sha256'] for name,row in manifest['sources'].items())
    native = read(folder/'native.json')
    assert {k:v for k,v in report.items() if k != 'verification_partition'} == native
    m = read(p.root/'data/master-timing.json')
    times = [s['start']+s['duration']/2 for s in m['scenes']] + [(s['start']+s['end'])/2 for s in m['silences']]
    assert manifest['requested_times'] == partition['requested_times'] == times
    validate_report(native,times)


def check(p, times, emit):
    from .runner import subprocess_stage
    folder = p.qa/'root-visual-check'
    host = folder/'host'
    (host/'compositions').mkdir(parents=True, exist_ok=True)
    sources = {}
    for source in [p.root/'index.html', *sorted((p.root/'compositions').glob('*.html'))]:
        relative = source.relative_to(p.root)
        original = source.read_text()
        transformed = visual_only(original)
        target = host/relative
        target.write_text(transformed)
        sources[str(relative)] = dict(source_sha256=sha(source),
            visual_sha256=sha(target),
            audio_elements_removed=len(re.findall(r'<audio\b', original, re.I)))
    assert len(sources) == len(p.scenes)+1
    assets = host/'assets'
    if assets.exists() or assets.is_symlink():
        assert assets.is_symlink() and assets.resolve() == p.root/'assets'
    else:
        assets.symlink_to(p.root/'assets', target_is_directory=True)
    (host/'hyperframes.json').write_bytes((p.root/'hyperframes.json').read_bytes())
    manifest = dict(transform='Remove audio elements only; preserve all visual source, slots, global offsets and timelines',
        sources=sources, requested_times=times, runtime=p.profile['runtime'],
        config_sha256=sha(p.root/'hyperframes.json'),
        implementation_sha256=sha(Path(__file__)),
        audio_scope='Separate sample-accurate PCM, encoded AAC and complete-media acceptance')
    write(folder/'source-transform.json', manifest)
    emit(dict(phase='root_visual_check_start', samples=len(times), scenes=len(p.scenes)))
    subprocess_stage(p, [sys.executable, '-m', 'ceh_video.root_check', str(p.root)],
                     'root-native-visual', emit)
    report = read(folder/'native.json')
    validate_report(report, times)
    assert all(sha(p.root/name) == row['source_sha256'] for name,row in sources.items())
    report['verification_partition'] = dict(
        scope='Complete visual composition; audio elements omitted in a temporary QA host',
        source_manifest_sha256=sha(folder/'source-transform.json'),
        implementation_sha256=sha(Path(__file__)),
        requested_times=times, audio='Separate PCM/AAC/encoded-media gates; not a full-host audio playback claim')
    write(p.qa/'master-project-check.json', report)
    require_current(p)
    emit(dict(phase='root_visual_check_verified', samples=len(times),
              contrast_objects=report['contrast']['checked']))
    return report


if __name__ == '__main__':
    p = Project(sys.argv[1])
    folder = p.qa/'root-visual-check'
    manifest = read(folder/'source-transform.json')
    command = [str(p.root/'node_modules/.bin/hyperframes'), 'check', str(folder/'host'),
               '--at', ','.join(f'{t:.6f}' for t in manifest['requested_times']),
               '--strict', '--json']
    with (folder/'native.json').open('w') as output:
        code = subprocess.call(command, cwd=p.root, env=p.environment(), stdout=output)
    sys.exit(code)

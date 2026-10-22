"""Scoped feedback does not satisfy the complete release gate."""
from pathlib import Path
import os
import subprocess
import json
import shutil
from .common import read, sha
from .run_record import RunRecord

REPRESENTATIVES = ['S01','S07','S17','S23','S27','S33','S40','S44','S47','S48','S49','S50','S57','S58']

def changed_scenes(p, report):
    visual=Path(__file__).parent/'visual'
    identities={
        'qaScriptSha256':visual/'remaster-qa.mjs',
        'geometrySha256':visual/'remaster-geometry.mjs',
        'textGeometrySha256':visual/'geometry.mjs',
        'runtimeSha256':visual/'remaster-runtime.js',
        'hyperframesRuntimeSha256':p.root/'node_modules/hyperframes/dist/hyperframe-runtime.js',
        'browserExecutableSha256':Path(p.profile['runtime']['browser']),
        'gsapSha256':p.root/'assets/vendor/gsap.min.js',
    }
    if any(report.get(key)!=sha(file) for key,file in identities.items()):
        return list(p.by_id)
    if report.get('environment',{}).get('tokens')!=sha(p.root/p.profile['token_manifest']):
        return list(p.by_id)
    if report.get('environment',{}).get('lock')!=sha(visual/'package-lock.json'):
        return list(p.by_id)
    selected=[]
    for sid in p.by_id:
        paths={'sources':p.root/'compositions'/f'{sid}.html',
               'audioSources':p.root/'data'/f'{sid}.audio.json',
               'layoutSources':p.root/'data'/f'{sid}.layout.json',
               'sceneSpecSources':p.root/'data'/f'{sid}.scene-spec.json',
               'cueSources':p.root/'data'/f'{sid}.label-cues.json'}
        if any(report.get(key,{}).get(sid)!=(sha(file) if file.exists() else None)
               for key,file in paths.items()):
            selected.append(sid)
    return selected


def execute(p, scope, precheck, emit, kind='routine', parent_run=None):
    record=RunRecord(p,'qa:'+scope,kind,parent_run)
    env=p.environment()
    env.pop('CEH_QA_SCENE',None)
    env.pop('CEH_QA_SCENES',None)
    env['CEH_QA_RUN_ID']=record.id
    if scope=='representative':
        selected=p.profile.get('representative_scenes',REPRESENTATIVES)
    elif scope=='changed':
        manifest=p.qa/'visual/scenes/manifest.json'
        selected=changed_scenes(p,read(manifest) if manifest.is_file() else {})
    else:
        selected=None
    if selected is not None:
        env['CEH_QA_SCENES']=','.join(selected)
    command=['node',str(Path(__file__).parent/'visual/remaster-qa.mjs'),str(p.root)]
    if precheck:command.append('--precheck')
    if selected==[]:
        return record.finish('reused',scenes=[],scope=scope)
    try:
        log=record.directory/'qa.log'
        emit({'phase':'qa_start','scope':scope,'scenes':selected or list(p.by_id),'log':str(log)})
        with log.open('w') as stream:
            result=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
        for line in reversed(log.read_text().splitlines()):
            try:row=json.loads(line)
            except ValueError:continue
            if row.get('report') and Path(row['report']).is_file():
                shutil.copy2(row['report'],record.directory/'qa-manifest.json')
                break
        if result.returncode:
            raise RuntimeError('Scoped QA failed: '+str(log))
        return record.finish('completed',scope=scope,precheck=precheck,
                             release_acceptance=False,
                             note='Candidate baseline review remains separate; inspect manifest status')
    except BaseException as exc:
        record.finish('interrupted' if isinstance(exc,KeyboardInterrupt) else 'failed',error=str(exc))
        raise

#!/usr/bin/env bash
set -euo pipefail
: "${CEH_PROJECT:?Set CEH_PROJECT to the migrated, fully built local project}"
: "${CEH_PY:?Set CEH_PY to the approved Python runtime}"
export PYTHONPATH=tools/ceh_video
"$CEH_PY" -m unittest discover -s tools/ceh_video/tests -v
npm ci --prefix tools/ceh_video/ceh_video/visual --ignore-scripts --no-audit --no-fund
npm test --prefix tools/ceh_video/ceh_video/visual
"$CEH_PY" -c 'import os; from ceh_video.common import Project; from ceh_video.engineering import verify_audio; verify_audio(Project(os.environ["CEH_PROJECT"]),False)'
node tools/ceh_video/ceh_video/visual/representative.mjs "$CEH_PROJECT"
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage build
node tools/ceh_video/ceh_video/visual/all-text-geometry.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/qa.mjs "$CEH_PROJECT" fixtures
node tools/ceh_video/ceh_video/visual/qa.mjs "$CEH_PROJECT" scenes
node tools/ceh_video/ceh_video/visual/cross-scene-seek.mjs "$CEH_PROJECT"
"$CEH_PY" -c 'import os; from ceh_video.common import Project,read; from ceh_video.visual_gate import require_visual; p=Project(os.environ["CEH_PROJECT"]); require_visual(p,["S17","S23",*[f"S{i}" for i in range(50,58)]]); assert read(p.qa/"visual/fixtures/manifest.json")["status"]=="passed"'
git diff --check

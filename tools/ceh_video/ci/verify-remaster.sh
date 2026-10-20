#!/usr/bin/env bash
set -euo pipefail
: "${CEH_PROJECT:?Set CEH_PROJECT to an isolated CI copy of the full remaster project}"
: "${CEH_PY:?Set CEH_PY to the approved Python runtime}"
: "${CEH_CI_ISOLATED:?Set CEH_CI_ISOLATED=1 after provisioning an isolated CI workspace}"
[[ "$CEH_CI_ISOLATED" == 1 ]]
export PYTHONPATH=tools/ceh_video
"$CEH_PY" -m unittest discover -s tools/ceh_video/tests -v
npm ci --prefix tools/ceh_video/ceh_video/visual --ignore-scripts --no-audit --no-fund
npm test --prefix tools/ceh_video/ceh_video/visual
"$CEH_PY" -c 'import os; from ceh_video.common import Project; from ceh_video.engineering import verify_audio; verify_audio(Project(os.environ["CEH_PROJECT"]),False)'
"$CEH_PY" -m ceh_video --project "$CEH_PROJECT" --plain engineering --stage build
node tools/ceh_video/ceh_video/visual/remaster-qa.mjs "$CEH_PROJECT" --precheck
node tools/ceh_video/ceh_video/visual/quiz-divider-negative.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/remaster-qa.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/remaster-boundaries.mjs "$CEH_PROJECT"
node tools/ceh_video/ceh_video/visual/remaster-assets.mjs "$CEH_PROJECT"
"$CEH_PY" -c 'import os; from ceh_video.common import Project; from ceh_video.visual_gate import require_visual; p=Project(os.environ["CEH_PROJECT"]); require_visual(p,[s["id"] for s in p.scenes])'
git diff --check

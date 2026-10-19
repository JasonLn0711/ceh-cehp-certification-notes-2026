#!/usr/bin/env python3
"""Write module-specific source/production contracts from actual M09 interfaces."""
from pathlib import Path
import json,shutil
R=Path(__file__).resolve().parents[1];S=json.loads((R/'scenes.json').read_text());N=S['estimated_spoken_words']
def write(n,s):p=R/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
standard=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026/docs/video-production/PRODUCTION_STANDARD_v1.0.md')
if standard.exists():shutil.copy2(standard,R/'PRODUCTION_STANDARD_v1.0.md')
write('README.md',f'''# CEH M09 English Editorial Masterclass v1.0

**Social Engineering — source_ready applies after the source checks pass.** This package contains 11 chapters, 58 editable source boards, **{N:,} canonical spoken words**, eight original graded questions, four Northstar cases and an integrated capstone. Its source acceptance does not establish final speech, aligned captions or MP4; the separately executed production delivers those layers with their own receipts.

## Start here

Read [the adopted standard](PRODUCTION_STANDARD_v1.0.md), [the full-production prompt](AGENT_PROMPT.md), [course structure](COURSE_STRUCTURE.md), [complete narration](SCRIPT_en-US.md) and [storyboard](STORYBOARD.md). Review the [58-scene browser](previews/index.html), [18-slide editable deck](slides/CEH_M09_Editable_Visual_Lookbook_18slides.pptx), corresponding PDF and [four seekable examples](examples/index.html).

The design preserves M04 v3 warm paper, original Tally and Northstar. Local af_heart/en-US at baseline 0.73 receives exactly one spoken-only atempo=1.5. Video remains rate 1.0, BGM is off, and eight complete question/choice sets each precede exactly 1.000 second of reference-zero PCM. Actual voice and explanation determine duration without a ceiling.

## Teaching and evidence

[Coverage](COVERAGE_MATRIX.md), [concept connections](CONCEPT_CONNECTIONS.md) and [primary references](SOURCES.md) support newly authored Social Engineering content. [Four case cards](case/EVIDENCE_CARDS.md) distinguish identity claims, business authority, independent verification and outcome evidence. [Offline exercise](lab_mock/README.md), [student work](ASSESSMENT_STUDENT.md) and [independent instructor answers](ASSESSMENT_INSTRUCTOR.md) retain their own layers.

All campus artifacts are SIMULATED OUTPUT. The actual verifier reads inert local files and calculates hashes, fields and constructed counts. Receiver mail-authentication results are stipulated strings; no SPF/DKIM/DMARC execution or independent QR decoding is claimed. No messages, calls, services, credential collection or participant contact occur. Produced material adds no learner completion.

## Rebuild and inspect

Install the versions in requirements-source.txt and package.json. Use the documented local Chromium and LibreOffice tools; no voice model or paid provider is needed for this source layer. See [tooling](tooling/README.md).

```bash
python3 tooling/build_source.py
python3 tooling/build_evidence.py
python3 tooling/build_companions.py
python3 tooling/write_docs.py
python3 tooling/verify_evidence.py --record
python3 tooling/validate_pack.py
python3 -m http.server 8078 --bind 127.0.0.1
```

Source reconstruction invalidates old previews, QA and manifests until they are regenerated. The original shared artwork, fonts and GSAP are bundled. Four finite 12-second examples demonstrate implementation only; their quiz [6,7) interval is illustrative and is not the full-film timestamp. The final production uses measured narration and a sample ledger.

## Acceptance and rights

[QA contract](QA_CHECKLIST.md), [voice specification](VOICE_AND_AUDIO.md), [caption contract](production/CAPTION_CONTRACT.md) and [render plan](RENDER_PLAN.md) govern the authorized full-film execution. No pilot approval is required. A real blocker must name its stage, command, diagnostics and affected artifact.

The manifest excludes itself and FILES_SHA256.txt to avoid circular digests. The closed ZIP receipt separately measures CRC, extraction and every payload hash. [Licenses and provenance](LICENSES_AND_PROVENANCE.md) identify shared artwork, new teaching sources, fonts, GSAP and the QR encoder. Human acceptance and public media release retain separate evidence.
''')
write('START_HERE_zh-TW.md',f'''# CEH M09 使用入口

本來源包含11章、58幕、{N:,}字完整英文腳本、18頁可編輯簡報、四組動畫範例、四個Northstar案例、八題分級測驗與綜合作業。先讀[英文README](README.md)、[目前通則](PRODUCTION_STANDARD_v1.0.md)及[完整製片指令](AGENT_PROMPT.md)。

本輪已授權來源包與完整成片。來源ZIP的驗收只證明來源層；實際配音、字幕及MP4須以另外的製片結果與QA為準。旁白使用既有af_heart／0.73基準，每段僅一次atempo=1.5；八題各1.000秒零值PCM，影片正常速度。完整人工觀影／聽驗及公開上傳各自驗收。

案例與聯絡資料皆為合成教學素材，僅離線解析；準備好的教材不計為本人題目、學習分鐘或實作完成。
''')
write('AGENT_PROMPT.md',f'''# Execute the complete CEH M09 production workflow

Produce CEH Module 09: Social Engineering for Northstar Learning Center. Read every root specification, the complete {N:,}-word script, all chapter/scene/question/visual JSON, storyboard, synthetic case artifacts, source QA, licenses and all four motion examples. PRODUCTION_STANDARD_v1.0.md is the adopted series contract.

## Required actual delivery

Produce all 58 genuinely animated scenes across 11 chapters, complete simple American English narration, synchronized SRT/VTT and burned-in captions, chapter MP4s, an editable HyperFrames project and final 1920×1080/30fps H.264/AAC MP4 with chapter marks. Retain a lossless reference mix and measured timeline. Full source plus film is already authorized; do not impose a short-pilot or renewed render-approval gate. Source boards and examples are references, not completed full-film animation.

Preserve original M04v3 paper editorial design, Tally, inherited Northstar identities and all 44 locked assets. Add workflow roles separately from the immutable network map. Use native editable objects, labels, paths and meaningful cause/evidence relationships. Keep complete canonical content, options, answers and explanations. Use local frozen fonts, GSAP and assets.

## Voice and quizzes

Use approved local Kokoro af_heart/en-US at baseline 0.73. Apply exactly one atempo=1.5 to each spoken clip. No second tempo pass, whole-film acceleration, recalibration or BGM. Freeze model/voice/runtime fingerprints, native baseline clips and processed clips. Synthesis-only interventions preserve meaning and have a ledger.

audio_segments is authoritative. Each Q01–Q08 full stem and A–D set precedes exactly 48,000 stereo zero-valued PCM frames at 48 kHz, then the answer. Eight holds total 8.000 seconds. Keep captions and extra reading holds outside those windows. The reference example's [6,7) interval is illustrative; derive final boundaries from measured samples.

## Execute and verify

1. Revalidate source hashes, all 44 inherited locks, JSON/question mapping and the actual offline evidence verifier. Freeze immutable source input before adapting production.
2. Inspect the current HyperFrames runtime, CLI and skills. Pin dependencies; validate any upgrade before accepting it. Preserve older module workspaces and approved shared Python environment.
3. Synthesize complete ordered manageable clips, cache by text/voice/model/speed fingerprint, preserve baseline and processed speech and measure durations. Normalize consistently without clipping.
4. Build each scene with orient/explain/reason/hold phases, narration-anchored reveals and caption clearance. Register finite paused seek-safe timelines. Duration follows actual processed audio and explanation, with no ceiling.
5. Align captions against final audio. Verify complete canonical spoken coverage, positive cue intervals and empty silent quiz windows. Do not label estimated timestamps as final.
6. Validate every actual scene/chapter; inspect native frames; render all chapters with resumable source/output fingerprints. Assemble the complete master at picture rate 1.0 and embed all 11 chapter marks.
7. Fully decode the actual MP4; verify codec, dimensions, frame rate/count, boundaries, chapter/audio continuity and black-frame detection. Inspect encoded samples at every scene midpoint, chapter first/middle/last, every quiz hold and answer boundary, plus repaired late diagram states.
8. Verify every reference zero buffer. Independently measure decoded AAC window residue and disclose it separately from bit-exact reference silence. Audit speech and alignment flags; preserve a timecoded audition queue and do not substitute ASR availability for human pronunciation acceptance.
9. Package original source and full editable project separately; include actual hashes, source/model/license provenance, logs, QA, subtitles and remaining review items. CRC-test, extract and verify every payload. State actual counts and master location.

## Educational boundary and truthful status

All invented campus artifacts carry SIMULATED OUTPUT. Analyze files without sending, calling, opening live destinations, starting services or collecting credentials. Stipulated mail-authentication strings and QR construction do not prove live authentication or independent decoding. Account reset, transaction outcome, client interaction, entrant count and personal intent require separate evidence. Existing600question-bank IDs and learner results remain unchanged.

Keep source_ready, runtime readiness, actual rendered output, human acceptance and public release distinct. Full human viewing/listening is a separate acceptance layer. A real blocker report includes failed command, diagnostics, affected deliverable and smallest next check. A prompt, scaffold or source ZIP cannot establish completed narration, synchronized subtitles or MP4.
''')
write('VOICE_AND_AUDIO.md','''# Approved M09 voice and audio contract

Kokoro af_heart, en-US, native baseline speed0.73; exactly one FFmpeg atempo=1.5 on each spoken clip, resampled to48kHz stereo PCM. Preserve native baselines, processed clips, model/voice/text/speed hashes and ordered sample ledger. No BGM, whole-film speedup, second tempo pass or WPM forcing. Report raw clip WPM separately from any stated signal-based descriptive estimate.

Read the complete canonical script, including all questions/options/answers/explanations. Pronunciation/punctuation intervention belongs only in a synthesis ledger and preserves meaning. Derive durations from actual final audio. Complete human pronunciation/naturalness and full listening remain separately recorded acceptance; ASR/forced alignment flags are review leads rather than confirmed TTS defects.

Insert exactly 48,000 stereo zero-valued PCM frames at 48 kHz after each complete question/choice set. Preserve the lossless reference. Independently decode the actual AAC MP4 and measure all eight windows, disclosing boundary residue and sample padding. Do not call lossy decoded audio bit-exact zero without measured proof.
''')
write('production/CAPTION_CONTRACT.md','''# Final M09 caption contract

Align against the actual post-speed speech and retain the source-audio hash, canonical tokens, timing method and uncertainty flags. SRT/VTT plus burned-in captions cover all spoken stems, choices, explanations and teaching. Use positive nonoverlapping cue intervals, readable wrapping and the lower reserved caption zone. All eight sample-accurate silent buffers remain caption-free. Source estimates never become final alignment by relabeling.
''')
write('RENDER_PLAN.md','''# Full production and recovery

Use an independent project/ beside immutable inputs/, qa/ and output/. Run actual source verification first. Preserve shared asset hashes and new M09 interfaces. Use all 58 native compositions and11chapter projects. Complete voice/alignment determines scene timing. Chapter render receipts bind normalized source fingerprints to actual output hashes; reuse only matching completed artifacts.

Use measured bounded progress for synthesis, alignment, preparation, checks, rendering and packaging, with durable status/logs, real counts and preserved exit codes. Keep JSON stdout parseable, human progress on stderr and no secret values in logs. Inspect an existing process before launching a duplicate. Resume only affected failed/changed stages; never restart unrelated completed work.

Verify actual full decode and encoded frames after assembly. Final outputs: CEH_M09_Social_Engineering_en-US_1_5x_1s_master.mp4, chapters/C01–C11, chapters.txt, captions.en-US.srt/.vtt, master.reference.pcm.wav, CEH_M09_Social_Engineering_v1_0_EDITABLE.zip, render_report.md and DELIVERY_SHA256.txt. Source ZIP remains CEH_M09_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip. Media stay local; public release and human acceptance remain separate.
''')
write('QA_CHECKLIST.md','''# M09 acceptance layers

Source: full canonical text and JSON mapping;11chapters/58scenes/8questions; all 44locks; valid editable SVG; native editable18slide deck/PDF; four real runtime examples; actual offline artifact QA; primary-source retrieval; licenses; CRC/extracted payload hashes.

Runtime: actual speech coverage, one tempo pass, measured samples/chapters, aligned captions, eight exact reference-zero buffers, deterministic forward/backward seeking, native diagrams, readable labels and no caption overlap. HyperFrames errors must be resolved; any warnings retain their exact scope.

Rendered: all 11 chapters and master have matching fingerprints, correct codec/dimensions/rate, complete decode, audio coverage/continuity, embedded chapter marks and encoded visual sampling across scenes/transitions/quiz boundaries. Measure AAC separately. Review optional animation-map heuristics as such.

Human accepted: actual timecoded viewing/listening with findings resolved. Public release: separate authorized action and verified URL. None of these layers establish learner answers, practical acceptance, attendance, Blog publication or used study minutes.
''')
write('STYLE_INHERITANCE.md','''# M04 v3 inheritance and M09 additions

The44locked original assets preserve Tally, Northstar and approved design byte-for-byte. M09 adds workflow roles in m09_workflow_extensions.json without modifying inherited device identities or map geometry. Source interfaces and neutral build patterns derive from the owned M08 package; Social Engineering teaching, questions, cases, diagrams and motion references are newly authored. Source SVGs and PPTX native objects remain editable. Full-film animation requires actual production receipts.
''')
write('LICENSES_AND_PROVENANCE.md','''# Rights and provenance

Original Tally, style references and Northstar assets are user-supplied approved series material with inherited source hashes. Do not replace or rebrand the mascot. New M09 script, assessments, synthetic artifacts and diagrams are independently authored educational sources.

Local Liberation and DejaVu font copyright/license notices and GSAP license material are bundled under licenses/. qrcode8.2 is BSD-licensed; its upstream license and package metadata are recorded. Approved Kokoro model/voice and runtime licenses accompany the later editable production and retain their exact fingerprints. No private speaker reference or unauthorized voice clone is used.

Primary references are linked with retrieval metadata and concise claim mapping; the package does not redistribute EC-Council courseware or claim official exam questions. Large models, environments, node_modules and full-film media are excluded from the source ZIP. Local runtime/QA, human acceptance and public release are distinct.
''')
write('tooling/README.md','''# Rebuild the M09 source package

Python3.10+ with requirements-source.txt builds the source, evidence and editable deck. Node22+, Puppeteer/Chromium, LibreOffice and Poppler support actual browser/PDF QA. Original locked assets, local fonts and GSAP are bundled; no external voice provider is required for this layer.

Run build_source.py, build_evidence.py, build_companions.py and write_docs.py. The authored_scenes*.txt, authored_chapters.json and authored_questions.json are canonical authored inputs. write_references.py refreshes public-source retrieval metadata only when deliberately run with live access. verify_evidence.py is read-only unless --record is supplied.

Export the actual PPTX through LibreOffice in an isolated profile, rasterize its PDF and run browser_qa.cjs with PUPPETEER_PATH and CHROMIUM_PATH. Inspect all 58boards/18slides/four references and record concrete findings. Run all four HyperFrames checks. Run validate_pack.py and build_release.py only after required QA. Rebuilding invalidates older manifests/QA until verified again. Manifest/self-hash exclusions avoid circular digests. Only actual results establish the named layer.
''')
req=R/'requirements-source.txt';s=req.read_text();s+='\nqrcode==8.2\n' if 'qrcode==' not in s else '';req.write_text(s)
dump=dict(name='ceh-m09-editorial-source',version='1.0.0',private=True,description='New Social Engineering source and four motion references; full-film output has separate receipts',engines={'node':'>=22'},scripts={'qa:browser':'node tooling/browser_qa.cjs','qa:source':'python3 tooling/validate_pack.py'},devDependencies={'hyperframes':'0.8.173','puppeteer-core':'25.14.0'})
write('package.json',json.dumps(dump,indent=2)+'\n')
print(json.dumps({'stage':'source_contracts_written','canonical_words':N,'source_status':'awaiting_full_source_QA'}))

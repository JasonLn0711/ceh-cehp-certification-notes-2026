# M06 System Hacking — full film production and evidence

Recorded: 2026-10-18, Asia/Taipei. **Confirmed:** the complete English M06 v1.1 film is rendered and passed automated delivery checks: **58:07.500**, **104,625 frames**, **11 chapters / 58 animated scenes**, **8,969 canonical spoken words**, 1920×1080 at 30 fps, H.264/AAC. All eight quiz holds use exactly **1.000 second of zero-valued 48 kHz stereo PCM**. Full human viewing/listening acceptance remains pending.

Jason supplied the source package and set the editorial, timing and complete-film requirements. Codex implemented the layered scenes, local narration, captions, chapter/master rendering and QA. Audience: Jason's CEH review and reuse of the teaching material.

## FIRST PRINCIPLE and ownership

- Scarce resource: study capacity, review attention, reliable evidence and local production storage.
- Canonical home: this repo owns [source provenance](../../source/2026-10-18-ceh-m06-video-production/README.md), adopted decisions, compact QA and learning connections. `~/Videos/CEH_M06_v1_1/` owns executable project code, assets, models and media.
- Planning role: [October 18](../../../planning-everything-track/weeks/2026-W42/days/2026-10-18.md#ceh-m06-video-closeout), [W42](../../../planning-everything-track/weeks/2026-W42/weekly-plan.md#ceh-m06-video-closeout) and the [CEH locator](../../../planning-everything-track/data/projects/2026-07-ceh-cehp-certification-training.md#ceh-m06-video-closeout) keep status, capacity, evidence locations and the next gate.
- Evidence path: [preserved QA index](../../source/2026-10-18-ceh-m06-video-production/validation/README.md) and local `output/render_report.md`.
- Scope control: Git publication covers documentation and compact QA. Local media release, full human acceptance and actual learner progress each need their own evidence.
- Next gate: Jason reviews the delivered film when capacity permits and records any accepted changes or timecoded issues here.

## Source, design and content

The [exact instruction](../../source/2026-10-18-ceh-m06-video-production/source.md) and [original AGENT_PROMPT.md](../../source/2026-10-18-ceh-m06-video-production/agent-prompt.md) authorize full production without a short-pilot approval gate. The immutable original ZIP has 273 files, SHA-256 `13398381289734b31525cbd5c0c3afb01170039c7ff4ce8af379e94d3b151ee9`. All 271 manifest hashes and 44 locked assets matched; 1,065 source checks passed with zero failures. The earlier source-only validator wording remains preserved as a historical layer.

M06 has its own System Hacking script, cases and assessment. The repeated M05 background's 8,279-word count does not describe this M06 course. [M05 v1.1](../m05-vulnerability-analysis/video-production-2026-10-18.md) remains a separate 53:00.467 film. Original M04 v3 warm-paper art, Tally, Northstar, colors, stroke style, editable native diagrams, full teaching depth and no runtime cap remain the design baseline. The inherited 40 Tally files, 58 SVG boards and 18-slide editable PPTX were checked; the PPTX has 523 native shapes and 185 nonempty text shapes.

Two minimal working-script corrections align narration with the fictional case: S46 changes ten to **twenty-two minutes** for 10:04→10:26; S47 changes afternoon to **morning** for 10:33/10:34. [Receipts](../../source/2026-10-18-ceh-m06-video-production/validation/source-corrections.json) preserve the original and corrected wording. Total canonical words remain 8,969. Original ZIP files and the previously delivered M05 master remain hash-identical.

## Delivery and reproduction

Local owner: `~/Videos/CEH_M06_v1_1/`.

| Artifact | Local path / checked identity |
| --- | --- |
| Complete MP4 | `output/CEH_M06_System_Hacking_en-US_1_5x_1s_master.mp4` — 162,405,708 bytes |
| Eleven chapters | `output/chapters/C01.mp4` through `C11.mp4` |
| Full captions | `output/captions.en-US.srt` and `.vtt` — 1,139 blocks; canonical coverage checked |
| Chapter marks and scene ledger | `output/chapters.txt`, `output/scene_qa_ledger.csv` |
| Zero-PCM reference mix | `output/master.reference.pcm.wav` |
| Editable project folder | `output/project_source/README.md` → `project/EDITING.md` |
| Editable source ZIP | `output/CEH_M06_System_Hacking_v1_1_EDITABLE.zip` — 5,358 entries, 2,739,795,185 bytes; CRC passed |
| Full report, QA and manifest | `output/render_report.md`, `output/qa_evidence/`, `output/DELIVERY_SHA256.txt` |

Master SHA-256: `3651a8c75752949fbef7792a96f03544e88344d4a9c8f8771ea9f295df69876a`.
Editable ZIP SHA-256: `4353d5d9a9efd22ed8e9ce9dd64c82ade40eea26cd46d152b374c2fc034dee3a`.

The editable archive includes original source inputs, local production models and licenses, fonts, scripts, SVG/PPTX assets, measured voice clips and compositions. Python/Node environments and caches are excluded. HyperFrames 0.8.169, Node dependency lock and Python package pins support rebuilding; the editing guide records the actual workflow. Local Studio was started at `http://127.0.0.1:3003/#project/project` and returned HTTP 200. It is a local editing session, separate from public publication.

## What the checks establish

All 11 chapter outputs passed browser/runtime, codec, duration and source/output fingerprint checks. The full 58-scene root composition passed its browser check. The master fully decoded with zero detected black intervals. [115 encoded samples](../../source/2026-10-18-ceh-m06-video-production/validation/master-visual-review.md) cover every scene midpoint, chapter first/middle/last frames, every quiz hold and the before/answer boundaries. [64 actual-timeline assertions](../../source/2026-10-18-ceh-m06-video-production/validation/quiz-runtime-checks.json) passed, including backward seeking and exact answer visibility.

Every quiz zero buffer contains 48,000 audio frames / 96,000 channel samples, all zero. As agreed, the final AAC remains lossy: full decoded one-second windows are measured separately. Maximum full-window peak is 2.390798e-05; nonzero decoded channel samples across all eight windows total 49,152. These compression residues are disclosed rather than called bit-exact decoded zero. [Encoded audit](../../source/2026-10-18-ceh-m06-video-production/validation/rendered-artifact-audit.json) preserves each interval and its interior measurements.

The approved af_heart American English voice retains baseline 0.73 and exactly one `atempo=1.5` pass on each of 697 spoken clips. Raw clips including model edge padding measure 170.149651 WPM. The −50dBFS edge-trimmed signal estimate is 173.192412 WPM, with −60/−40dBFS sensitivity estimates 172.525006/174.042691. This calculation changes no samples and retains internal pauses. Video, animations and silent buffers retain normal playback; no BGM, paid service or external voice upload was used.

[Audio QA](../../source/2026-10-18-ceh-m06-video-production/validation/audio-review.md) includes independent unprompted ASR on all 58 final WAVs and 97 retained word-alignment flags. One short S56 question initially merged “What should” into “Watch” in two recognizers. A synthesis-only punctuation break improved separation; the canonical sentence, voice and speed remain unchanged. Only that sentence was regenerated; its other 20 spoken clips match. Final independent recognition resolves the exact question. S12's “A salt”, S39's steganalysis and a few short option letters remain listening priorities, not proven omissions.

Applied visual refinements include S27 path/label clearance and S42's visual event ordering to match the fictional case chronology. Simulated evidence retains `SIMULATED OUTPUT`. No actual scan, credential collection, exploit, persistence installation or log deletion occurred.

## Learning connections

| Film section | Existing learning home | Reuse and evidence boundary |
| --- | --- | --- |
| C01–C02: finding, access, identity and authorization | [M04–M06 evidence map](../2026-10-04-ceh-week-02/README.md), [M05 film](../m05-vulnerability-analysis/video-production-2026-10-18.md) | Carry a finding into a question about observed access; keep authentication, permitted actions and later effects distinct |
| C03: passwords, verifier data and MFA | [M06 questions](../../assessments/practice-bank/m06.md), [separate key](../../assessments/practice-bank/m06-key.md) | Repair an observed conceptual gap while preserving original IDs, choice/confidence and retest separation |
| C04–C07: exploitation conditions, privilege, activity and persistence | [CEHP practical families](../../assessments/practice-bank/practical.md) | Explain prerequisites and defensive evidence; a prepared diagram does not establish learner execution |
| C08–C09: concealment, logs and connected Northstar case | [October 4 corrections and evidence status](../2026-10-04-ceh-week-02/README.md#review-corrections) | Compare independent records, alternative causes and unsupported incident claims; fictional cards remain fictional |
| C10: defenses and AI review | [Weakness-to-harm foundation](../m05-vulnerability-analysis/lesson-01-weakness-to-harm.md) | Trace a claim to evidence, consequence and verified control; an AI summary is not direct observation |
| C11: eight questions and capstone brief | [Current course route](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md), [coverage register](../../assessment-governance/course-coverage-2026-09-18.md) | Pause playback for more thinking time; record actual learner work separately from teaching-package delivery |

The eight film questions do not add completed first answers to the 600-ID practice bank. This production changes no existing attendance, learner answers, practical results, daily Blog status or used study minutes. W42 Red, the shared 240-minute weekly ceiling and at most 25 self-study minutes on course days remain in force. Film runtime is distinct from production labor and Jason's learning time.

## Next review and release gates

Jason owns full human viewing/listening acceptance when capacity allows; timecoded issues belong here. Public media release remains deferred until a platform/release action is chosen and an actual URL is verified. The delivered local media and documentation can support later course review and teaching reuse without adding a new schedule or deadline.

Documentation closeout verified 20 unchanged QA copies and the original AGENT_PROMPT.md copy. The full local delivery manifest rechecked all 5,769 entries; direct reads of the delivered reference PCM confirmed all eight 48,000-frame stereo holds are zero. Touched Markdown/link checks found zero new failures; inherited unavailable sibling/private targets remain identified separately. Planning repository/knowledge validators passed with 44 grandfathered policy warnings, zero new; 181 metadata notes and catalog entries. Both repos passed `git diff --check`. Git publication is recorded separately after the actual push.

## Series reuse — October 18

The [initial CEH series standard](../../docs/video-production/PRODUCTION_STANDARD_v1.0.md) adopts this film's approved design and timing implementation. The next module's [M07 Malware Threats source record](../m07-malware-threats/video-production-2026-10-18.md) reuses Tally/Northstar and voice/quiz timing while supplying new content. M06's original source archive and rendered delivery remain historical evidence; M07 source readiness is a distinct layer.

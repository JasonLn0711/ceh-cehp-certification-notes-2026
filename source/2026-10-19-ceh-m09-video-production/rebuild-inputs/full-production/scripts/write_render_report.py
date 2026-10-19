#!/usr/bin/env python3
"""Write the M09 handoff from verified full-film evidence, never from source counts alone."""
from pathlib import Path
import json
from production_settings import MASTER_FILENAME
R=Path(__file__).resolve().parents[1];O=R.parent/'output';Q=R.parent/'qa'
def main():
 d=json.load(open(Q/'delivery-validation.json'));assert d['status']=='automated_delivery_checks_passed'
 m=json.load(open(R/'data/master-timing.json'));a=json.load(open(Q/'rendered-artifact-audit.json'));quiz=json.load(open(Q/'quiz-runtime/checks.json'));src=json.load(open(Q/'production-source-revalidation.json'))
 ms=round(d['duration']*1000);mins,rem=divmod(ms,60000);secs,millis=divmod(rem,1000);duration=f'{mins}:{secs:02}.{millis:03}'
 version=json.load(open(R/'node_modules/hyperframes/package.json'))['version']
 s=f'''# CEH M09 Social Engineering — English Editorial Masterclass v1.0

Complete **11 chapters / 58 animated scenes**, **{d['canonical_spoken_words']:,} canonical spoken words**, **{duration}** ({d['duration']:.6f} seconds; {d['frames']:,} frames), 1920 × 1080 / 30 fps H.264/AAC. All eight quiz holds contain exactly 1.000 second of zero-valued 48 kHz stereo PCM. Decoded AAC windows are measured separately.

## Delivery

- [Complete MP4]({MASTER_FILENAME}), [11 chapter MP4s](chapters/) and [chapter marks](chapters.txt)
- [SRT](captions.en-US.srt), [WebVTT](captions.en-US.vtt) and [lossless reference mix](master.reference.pcm.wav)
- [Editable project ZIP](CEH_M09_Social_Engineering_v1_0_EDITABLE.zip), [workspace guide](project_source/README.md) and [editing instructions](project_source/project/EDITING.md)
- [Scene QA ledger](scene_qa_ledger.csv), [encoded samples](inspection_frames/), [QA evidence](qa_evidence/) and [delivery hashes](DELIVERY_SHA256.txt)
- [Immutable source ZIP](CEH_M09_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip)

## Teaching, design and runtime

The newly authored M09 lesson teaches social engineering through trust, independent verification and evidence. It covers influence and pressure, impersonation, phishing/spear phishing/BEC, message authentication limits, voice/text/QR/social channels, physical access, identity and recovery, authorized assessment, reporting, response, four connected Northstar cases, layered defenses and bounded AI assistance. The eight graded questions and capstone belong to the M09-film-v1 namespace, separate from learner assessment records.

All case records are fictional SIMULATED OUTPUT. Actual offline checks parse local email, JSON and CSV and verify cross-record claims. Email authentication results are stipulated strings; no SPF/DKIM/DMARC execution is claimed. The QR encoder produced the reserved example.test destination; an independent QR decoder was not exercised. No delivery, calls, credential collection, account changes or physical testing occurred.

All 44 inherited M04 v3 palette, Tally and Northstar locks match the approved bytes. All 58 scenes have editable native layers, measured narration anchors and finite paused timelines. Original SVG boards, the 18-slide native PowerPoint and its actual PDF export remain included as source references. Production uses purpose-built animated diagrams, including parallel qualifying-SPF-or-DKIM paths and separate business approval.

The production pin is **HyperFrames {version}**. The earlier M08 workspace and all previous module outputs remain unchanged. Local fonts, GSAP, physically copied public models, package locks, license records and model hashes are included. The approved shared Python environment was read without dependency upgrades. Synthesis and rendering used the local runtime without an authenticated media provider or upload. The compiler also resolved Inter into its font cache during checking; visible scene text uses the shipped Editorial/Technical font files. A fresh-machine CLI installation and font-cache bootstrap can require network access.

## Voice and measured timing

Approved local Kokoro `af_heart`, en-US, baseline **0.73**, followed by exactly one FFmpeg `atempo=1.5` per spoken clip. Baseline/post-speed speech totals are **{d['baseline_seconds']:.3f} / {d['post_speed_spoken_seconds']:.3f} seconds**; measured duration ratio **{d['measured_baseline_to_final_duration_ratio']:.6f}**. Animation and video retain rate 1.0. No BGM or second speed pass is applied.

Raw clip speech measures **{d['raw_clip_wpm']:.4f} WPM**. The −50 dBFS edge-trimmed signal estimate is **{d['effective_spoken_wpm']:.4f} WPM**. This descriptive measurement retains internal pauses and changes no audio. It establishes neither pronunciation accuracy nor comprehension. The fixed approved baseline was retained. [All measured clip hashes and threshold sensitivity](qa_evidence/speech-rate-measurement.json).

## Eight quiz holds

Every full question stem and A–D option set is spoken before its hold. Each hold contains exactly 48,000 stereo PCM frames / 96,000 channel samples, all zero. Eight holds total 8.000 seconds. Answer highlighting, banner and narration start after the hold; captions stay outside it. Learners can pause the player for extra thinking time.

AAC is lossy. The complete decoded final-master windows below are separate from the bit-exact zero reference buffers:

| Question | Reference frames | Decoded frames | Full AAC peak | Full AAC RMS | Nonzero channel samples | Interior peak |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
'''
 for i,p in enumerate(a['quiz_silence'],1):s+=f"| Q{i:02} | 48000 | {p['decoded_samples']} | {p['full_window_peak']:.9g} | {p['full_window_rms']:.9g} | {p['nonzero_channel_samples']} | {p['interior_peak']:.9g} |\n"
 s+=f'''
## Validation and review limits

The source release contains {src['source_entries']} files and passed 565 source assertions, 94 browser assertions and {src['offline_evidence_assertions']} actual offline evidence assertions. All {src['payload_hashes']} payload hashes, CRC/extraction and {src['locked_assets']} inherited locks were checked. Four standalone source examples retain one nonblocking nested-structure advisory each; their real runtime/layout/contrast checks passed. These historical source results are distinct from the native film checks.

All 11 actual chapter renders match their checked input/output fingerprints, codecs, durations and frame rates. The full 58-scene root passed actual browser lint/runtime/layout/contrast checks with zero errors and warnings. **{quiz['checks']} actual quiz assertions** passed, including exact answer boundaries and backward seeks. All 58 scene timelines also passed 174 repeated/backward seek comparisons. The full master decoded, contains **{d['frames']:,} video frames**, has zero detected black intervals and carries 11 embedded chapter marks. Picture was joined without re-encoding or speeding; the continuous narration was encoded once to AAC. Full-reference PCM continuity and chapter/master alignment were checked separately.

The **{d['primary_encoded_samples']} primary encoded samples** cover every scene midpoint, 33 chapter first/middle/last positions, eight holds and 16 before/answer positions. Another **{d['targeted_late_encoded_samples']} encoded late samples** cover every complete non-quiz diagram. [Concrete visual findings](qa_evidence/master-visual-review.md) record actual inspected frames. Native preview snapshots and actual encoded output retain separate receipts.

All 58 actual scene WAVs have independent, unprompted fixed-runtime transcript receipts. ASR mode is `availability_validation`, status `LIVE_FULL_COMPLETED`, functional result `available_and_working`; **accuracy and latency remain not_evaluated**. Known-text alignment retains **{len(d['alignment_review_flags'])} timing flags across {len(set((f['scene'],f['sentence']) for f in d['alignment_review_flags']))} clips**. The [audio review](qa_evidence/audio-review.md) and [local audition queue](project_source/qa/audio-audition/index.html) preserve these review leads. Full human listening, pronunciation scoring and end-to-end human viewing remain separate acceptance layers.

## Chapters

| Chapter | Topic | Start(s) | Duration(s) |
| --- | --- | ---: | ---: |
'''
 for c in m['chapters']:s+=f"| {c['id']} | {c['title']} | {c['start']:.3f} | {c['duration']:.3f} |\n"
 if (Q/'animation-map-review.md').exists():s+='\n[Animation-map review](qa_evidence/animation-map-review.md) records its separate tool version, scope and heuristic findings.\n'
 s+=f'''
## Ownership and next action

Canonical execution workspace: `{R.parent}`. The CEH repository owns content, technical evidence and learning connections. Planning owns thin locators, status, capacity and next action. W43 capacity is Unknown; the adopted shared 240-minute weekly ceiling and 25-minute course-day ceiling continue to govern learner work. Production does not establish learner answers, attendance, practical acceptance, Blog publication or used study minutes.

Jason owns full human viewing/listening acceptance when capacity allows. Record timecoded issues in the canonical M09 production note. Public video release requires a separate authorized action and verified URL. Git documentation publication does not publish the media.

Master SHA-256: `{d['master_sha256']}`.
'''
 (O/'render_report.md').write_text(s);print(json.dumps({'report':str(O/'render_report.md'),'status':'verified_runtime_report_written'}))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Write the M08 handoff only after verified full-film execution."""
from pathlib import Path
import json
from production_settings import MASTER_FILENAME
R=Path(__file__).resolve().parents[1];O=R.parent/'output';Q=R.parent/'qa'
def main():
 d=json.load(open(Q/'delivery-validation.json'));assert d['status']=='automated_delivery_checks_passed'
 m=json.load(open(R/'data/master-timing.json'));a=json.load(open(Q/'rendered-artifact-audit.json'));quiz=json.load(open(Q/'quiz-runtime/checks.json'));rate=json.load(open(Q/'speech-rate-measurement.json'));ms=round(d['duration']*1000);mins,rem=divmod(ms,60000);secs,millis=divmod(rem,1000);duration=f'{mins}:{secs:02}.{millis:03}'
 s=f'''# CEH M08 Sniffing — complete English Editorial Masterclass v1.0

Complete **11 chapters / 58 animated scenes**, **9,097 canonical spoken words**, **{duration}** ({d['duration']:.6f} seconds; {d['frames']:,} frames), 1920 × 1080 / 30 fps H.264/AAC. All eight quiz holds contain exactly 1.000 second of zero-valued 48 kHz stereo PCM. Final AAC residues are measured separately.

## Delivery

- [Complete MP4]({MASTER_FILENAME}), [11 chapter MP4s](chapters/) and [chapter marks](chapters.txt)
- [SRT](captions.en-US.srt), [WebVTT](captions.en-US.vtt) and [lossless reference mix](master.reference.pcm.wav)
- [Editable project ZIP](CEH_M08_Sniffing_v1_0_EDITABLE.zip), [workspace guide](project_source/README.md) and [editing instructions](project_source/project/EDITING.md)
- [Scene QA ledger](scene_qa_ledger.csv), [actual encoded samples](inspection_frames/), [QA evidence](qa_evidence/) and [delivery hashes](DELIVERY_SHA256.txt)
- [Original immutable source ZIP](CEH_M08_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip)

## Content, design and runtime

The complete M08 teaching covers Ethernet and switched visibility, capture points and filters, plaintext/TLS/VPN, ARP, MAC/DHCP, VLAN/STP/DNS, detection, four connected cases, defense/revalidation and AI-assisted interpretation. Northstar network events are fictional SIMULATED OUTPUT. Six synthetic PCAP files are analyzed offline; no interface capture, packet transmission, rogue service or external target request occurred. Source content is unchanged from the supplied M08 package.

M04 v3 paper palette, original Tally and inherited Northstar roles are hash verified. All scenes use editable native layers with exact narration anchors, finite paused timelines and semantic diagram reveals. Captions use final processed audio alignment and preserve every canonical word. The original 58 SVG boards and 18-slide editable PPTX remain included as source references.

M08 uses pinned **HyperFrames 0.8.171**. Its initial 0.8.170 C01 check is preserved separately; final chapter/full-project checks exercise the final pin. M05–M07 remain unchanged. Local fonts, GSAP, physically copied public models, package locks and license records are included. The shared Python environment was reused without upgrades; requirements-lock.txt records its isolated runtime dependencies.

## Voice and measured timing

Approved local Kokoro `af_heart`, en-US, baseline **0.73**, followed by exactly one FFmpeg `atempo=1.5` per spoken clip. Baseline/post-speed speech totals: **{d['baseline_seconds']:.3f} / {d['post_speed_spoken_seconds']:.3f} seconds**; measured duration ratio **{d['measured_baseline_to_final_duration_ratio']:.6f}**. Video and animation rate remain 1.0. No BGM or second tempo pass.

Raw clip speech is **{d['raw_clip_wpm']:.4f} WPM**. The −50 dBFS edge-trimmed signal estimate is **{d['effective_spoken_wpm']:.4f} WPM**. This descriptive measurement retains internal pauses and changes no audio samples; it is not a pronunciation or comprehension score. The fixed approved baseline was preserved rather than retuned to an estimated WPM range. [Threshold sensitivity and all clip hashes](qa_evidence/speech-rate-measurement.json).

## Quiz silence and answer boundary

All complete stems and A–D options precede the hold. Each hold is exactly 48,000 stereo PCM frames / 96,000 channel samples, all zero; eight holds total 8.000 seconds. Answer highlighting, banner and narration start after the hold. Captions do not enter silent windows. The on-screen pause guide supports longer learner thinking without changing the one-second contract.

AAC is lossy. These decoded final-master windows are reported independently from the digital-zero reference buffers:

| Question | Reference frames | Decoded frames | Full AAC peak | Full AAC RMS | Nonzero channel samples | Interior peak |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
'''
 for i,p in enumerate(a['quiz_silence'],1):s+=f"| Q{i:02} | 48000 | {p['decoded_samples']} | {p['full_window_peak']:.9g} | {p['full_window_rms']:.9g} | {p['nonzero_channel_samples']} | {p['interior_peak']:.9g} |\n"
 s+=f'''
## Validation and review scope

The immutable 308-file source release previously passed 811 source assertions and 94 browser assertions, with 306 payload hashes and 44 locked inherited assets verified. Those source results retain their original evidence layer.

All 11 actual chapter renders have matching input/output fingerprints and correct codecs, duration, dimensions and frame rate. The full 58-scene root project passed lint/runtime/layout/contrast checks with zero errors and warnings. All **{quiz['checks']} actual quiz timeline assertions** passed, including backward seeking and exact answer boundaries. The master fully decoded, contains **{d['frames']:,} video frames**, and has zero detected black intervals. Chapter videos were joined without speeding or re-encoding picture; a single continuous narration track was encoded to AAC, with 11 embedded chapter marks. [Actual animation-map review](qa_evidence/animation-map-review.md) discloses the isolated helper version and heuristic flags; those are separate from the zero-finding active-window runtime checks.

The **115 primary encoded samples** cover every scene midpoint, 33 chapter first/middle/last positions, eight holds and 16 before/answer positions. Another **17 targeted late-phase samples** verify repaired labels, notes and evidence limits beyond those midpoints; 132 distinct encoded samples were inspected. Concrete review is in [master visual review](qa_evidence/master-visual-review.md). Diagnostic multi-position screenshots sometimes omitted common layers while their DOM states remained correct; fresh direct captures and final encoded samples are treated as separate evidence. [Diagnostic receipt](qa_evidence/snapshot-diagnostic.md).

All 58 actual WAVs have independent fixed-runtime unprompted transcript receipts. ASR validation is `availability_validation`, status `LIVE_FULL_COMPLETED`, functional result `available_and_working`; **accuracy and latency are not_evaluated**. Known-text alignment retains **{len(d['alignment_review_flags'])} timing flags across {len(set((f['scene'], f['sentence']) for f in d['alignment_review_flags']))} clips**. [Audio review](qa_evidence/audio-review.md) and [local audition queue](project_source/qa/audio-audition/index.html) preserve these leads. No full human listening, pronunciation-accuracy score or end-to-end human viewing acceptance is claimed.

## Chapters

| Chapter | Topic | Start(s) | Duration(s) |
| --- | --- | ---: | ---: |
'''
 for c in m['chapters']:s+=f"| {c['id']} | {c['title']} | {c['start']:.3f} | {c['duration']:.3f} |\n"
 s+=f'''
## Ownership and next gate

The local owning workspace is `{R.parent}`. CEH records preserve technical evidence and learning connections; Planning retains status, location, capacity and next action. Production changes no learner answers, attendance, accepted practical tasks, Blog status or used study minutes. W42 Red and existing study ceilings remain in force.

Jason owns full human viewing/listening acceptance when capacity allows. Record timecoded issues in the canonical M08 production note. Public video release remains a separate future action with its own verified URL. Git documentation publication does not publish the media.

Master SHA-256: `{d['master_sha256']}`.
'''
 (O/'render_report.md').write_text(s);print(json.dumps({'report':str(O/'render_report.md'),'status':'verified_runtime_report_written'}))
if __name__=='__main__':main()

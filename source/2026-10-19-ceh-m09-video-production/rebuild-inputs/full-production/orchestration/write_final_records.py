"""Connect the actual M09 delivery to existing CEH and thin Planning records."""
from pathlib import Path
import json,os
V=Path(__file__).resolve().parent;Q=V/'qa';O=V/'output';P=V/'project'
R=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026');PLAN=R.parent/'planning-everything-track';S=R/'source/2026-10-19-ceh-m09-video-production';NOTE=R/'notes/m09-social-engineering/video-production-2026-10-19.md'
def append(p,s):
 old=p.read_text();marker=s.splitlines()[0];assert marker not in old,('Reconcile existing final section',p,marker);p.write_text(old.rstrip()+'\n\n'+s.rstrip()+'\n')
def main():
 d=json.load(open(Q/'delivery-validation.json'));z=json.load(open(Q/'packaging-receipt.json'));m=json.load(open(P/'data/master-timing.json'));assert d['status']=='automated_delivery_checks_passed' and z['status']=='editable_zip_crc_extraction_hashes_verified'
 t=round(d['duration']*1000);mm,ms=divmod(t,60000);ss,milli=divmod(ms,1000);duration=f'{mm}:{ss:02}.{milli:03}'
 c=json.load(open(P/'data/build-ledger.json'));cues=sum(v['captions'] for v in c);rate=d['effective_spoken_wpm'];flags=len(d['alignment_review_flags']);flagclips=len(set((x['scene'],x['sentence']) for x in d['alignment_review_flags']));spokenclips=sum(sum(x['kind']=='spoken' for x in json.load(open(P/'data'/f'S{i:02}.audio.json'))['segments']) for i in range(1,59));aac=json.load(open(Q/'rendered-artifact-audit.json'))['quiz_silence'];peak=max(x['full_window_peak'] for x in aac);nonzero=sum(x['nonzero_channel_samples'] for x in aac)
 NOTE.write_text(f'''# M09 Social Engineering — rendered English Masterclass

Recorded 2026-10-19, Asia/Taipei. **rendered_and_automated_QA_passed:** the complete **{duration}** film contains **11 chapters, 58 native animated scenes, 9,814 canonical spoken words, {d['frames']:,} frames and {cues:,} caption cues**, with 11 embedded chapter marks at 1920×1080/30fps H.264/AAC. [Exact source request and approved full-film scope](../../source/2026-10-19-ceh-m09-video-production/source.md) → [source release](../../source/2026-10-19-ceh-m09-video-production/README.md) → [actual render evidence](../../source/2026-10-19-ceh-m09-video-production/render-validation/README.md).

Jason selected the full source-plus-film delivery and adopted the existing design, voice and timing. Codex authored M09-specific teaching and no-send evidence, built native animation, synthesized/aligned the complete narration, rendered every chapter and the master, inspected encoded samples and verified both archives. Full human viewing/listening remains a separate acceptance layer.

## Delivery and integrity

All paths are under /home/jnlngx10/Videos/CEH_M09_v1_0/.

| Artifact | Local path |
| --- | --- |
| Complete film | output/CEH_M09_Social_Engineering_en-US_1_5x_1s_master.mp4 |
| Chapter films / marks | output/chapters/C01.mp4 through C11.mp4; output/chapters.txt |
| Subtitles, also burned in | output/captions.en-US.srt and .vtt |
| Lossless reference audio | output/master.reference.pcm.wav |
| Editable production ZIP | output/CEH_M09_Social_Engineering_v1_0_EDITABLE.zip |
| Complete source ZIP | output/CEH_M09_English_Masterclass_HandDrawn_Editorial_v1_FULL.zip |
| Native editable workspace | project/; output/project_source/project/ |
| Report / encoded samples | output/render_report.md; output/inspection_frames/ |
| Audio review leads | qa/audio-audition/index.html |
| Complete payload identities | output/DELIVERY_SHA256.txt |

Master SHA-256: {d['master_sha256']}. Editable ZIP: **{z['bytes']:,} bytes / {z['entries']:,} files**; CRC, extraction and all **{z['payload_hashes']:,} payload hashes** pass. Its SHA-256 is {z['sha256']}. Models, local assets, measured speech/alignment, code and QA are included; environments/caches are excluded and final media are delivered alongside it.

The source ZIP is **11,312,006 bytes / 305 files**, SHA-256: 36898c5e335adf24ff3bddabd9e9a952cd95c726f514fab654fd6486e1e5ac66. All 303 source payload hashes and 44 inherited locks match. Original inputs remain immutable. [Source-stage QA](../../source/2026-10-19-ceh-m09-video-production/validation/README.md): 565 source,94 browser and36 actual inert-evidence assertions pass with zero failures in each layer. Four standalone source examples each retain one disclosed nonblocking structure advisory.

## Teaching, evidence and production decisions

The [initial series standard v1.0](../../docs/video-production/PRODUCTION_STANDARD_v1.0.md) applies unchanged: M04 v3 warm paper editorial design, original Tally, Northstar, simple American English and narration-only 1.5×. M09 content is newly authored for Social Engineering. It connects influence, impersonation, email/BEC/authentication limits, voice/text/QR/social channels, physical access, identity/recovery, authorized assessment, detection/response, four linked cases, layered controls and AI-assisted interpretation. [Coverage](../../source/2026-10-19-ceh-m09-video-production/content/COVERAGE_MATRIX.md) and [13 actually retrieved primary references](../../source/2026-10-19-ceh-m09-video-production/content/SOURCES.md) preserve claim scope, including current RFC9989 and NIST800-63B-4.

All 58 scenes use editable native layers, exact canonical phrase anchors and finite paused timelines. Full late diagrams retain distinct request, identity, permission and actual outcome states. The original 58 SVG boards,223 native PowerPoint shapes / 159 text runs across 18 pages, actual PDF export and four working seekable examples remain source references. Production improves branch-label spacing and makes channel/source independence and incomplete outcomes visible without changing canonical narration.

All campus records are fictional SIMULATED OUTPUT. Actual offline email/JSON/CSV parsing and arithmetic verify supplied bytes and cross-record relationships. Stipulated SPF/DKIM/DMARC PASS strings do not establish a real authentication run or business authorization. E01 payment is held; E02 recovery is pending with no reset/session event; E03 notice approval/interaction is unconfirmed; E04 one badge event leaves entrant count and intent unknown. The real QR encoder uses a reserved example.test destination; independent QR decoding was not exercised. No message delivery, calls, collection service, credential submission, account change or physical test occurred.

## Actual film checks

HyperFrames **0.8.173** chapter/root checks have zero lint/runtime/layout/contrast errors and warnings. All 11 chapter renders have matching checked-source/output fingerprints. **64 quiz assertions** and **174 actual repeated/backward scene seek comparisons** pass. The full master decoded with {d['frames']:,} frames, zero detected black intervals and the correct codecs/rate. **115 primary plus 54 late encoded samples** cover every scene, chapter first/middle/last, all eight holds/answer boundaries and every complete non-quiz diagram. [Concrete visual review](../../source/2026-10-19-ceh-m09-video-production/render-validation/master-visual-review.md) states the sampling limits. Reference/AAC continuity compares all {d['frames']*1600:,} stereo frames, separately from listening acceptance.

Voice remains approved af_heart/en-US, baseline 0.73, followed by exactly one atempo=1.5 on each of {spokenclips} spoken clips. Picture/animation retain rate 1.0; BGM is off. Raw clip speech measures {d['raw_clip_wpm']:.4f} WPM; the −50 dBFS edge-trimmed descriptive estimate is {rate:.4f} WPM. This measurement changes no samples and does not recalibrate the approved voice or score pronunciation.

Each full question/A–D set precedes exactly **48,000 stereo zero PCM frames / 1.000 second** at 48 kHz, then the answer. Eight holds total 8.000 seconds; captions stay outside them. Decoded lossy AAC has maximum full-window peak {peak:.10g} and {nonzero:,} nonzero channel samples across the eight windows; the measured residue is separate from bit-exact reference silence.

All 58 actual WAVs have fixed base.en CPU/int8 unprompted transcript receipts: availability_validation / LIVE_FULL_COMPLETED / valid_target_runtime / available_and_working. Accuracy and latency are not_evaluated. [Audio review](../../source/2026-10-19-ceh-m09-video-production/render-validation/audio-review.md) retains {flags} alignment timing flags across {flagclips} clips and the local audition queue. The separate animation-map receipt records its matching isolated 0.8.173 helper and contextual heuristic review. Full human listening, naturalness/pronunciation and full-film viewing remain open.

## FIRST PRINCIPLE, connections and next gate

Scarce resources are study attention, trustworthy evidence, local compute and storage. CEH owns source content, decisions, [recovery tooling](../../source/2026-10-19-ceh-m09-video-production/rebuild-inputs/full-production/README.md) and compact QA. Videos owns large media and assets. Planning owns [day](../../../planning-everything-track/weeks/2026-W43/days/2026-10-19.md#ceh-m09-masterclass), [week](../../../planning-everything-track/weeks/2026-W43/weekly-plan.md#ceh-m09-masterclass), project locator, capacity and next action.

| Connection | Existing home | Purpose |
| --- | --- | --- |
| Official M09 / human risk | [Scope map](../../curriculum/official-scope-map.md#ceh-m09-masterclass) / [practical families](../../assessments/practice-bank/practical.md) | Routes the consent-based no-send assessment; practical families keep their existing module mappings |
| Existing bank | [M09 questions](../../assessments/practice-bank/m09.md) / [key](../../assessments/practice-bank/m09-key.md) | Film namespace M09-film-v1 preserves existing IDs and results |
| Prior modules | [M06 system identity](../m06-system-hacking/video-production-2026-10-18.md), [M07 software behavior](../m07-malware-threats/video-production-2026-10-18.md), [M08 network observation](../m08-sniffing/video-production-2026-10-18.md) | Distinguishes account, process, network and human-workflow evidence |
| Learning and capacity | [Current course-aligned route](../../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md) | W43 Unknown; shared 240-minute ceiling and 25-minute course-day ceiling |
| Source and delivery | [Source index](../../source/README.md#ceh-m09-masterclass) / [video index](../../docs/video-production/README.md#ceh-m09-masterclass) | One adopted standard, separate source/render/human/publication receipts |

Prepared media add no learner answers, practical acceptance, attendance, Blog publication, used study minutes or new deadline. Jason owns full timecoded viewing/listening acceptance when capacity allows. Public video release retains a separate authorized action and verified URL; Git publishes documentation, recovery code and compact evidence. Record corrections in this note and retain the affected chapter's original evidence.
''')
 append(R/'docs/video-production/README.md',f'''<a id="ceh-m09-masterclass"></a>
## M09 Social Engineering — October 19

[Canonical M09 delivery](../../notes/m09-social-engineering/video-production-2026-10-19.md) provides the complete {duration} film,11 chapters/58 native animated scenes,9,814 spoken words,aligned captions and source/editable ZIPs. [Actual source QA](../../source/2026-10-19-ceh-m09-video-production/validation/README.md) and [render QA](../../source/2026-10-19-ceh-m09-video-production/render-validation/README.md) retain separate evidence. Initial standard v1.0 applies; full human viewing/listening is the next acceptance layer.''')
 p=R/'docs/video-production/README.md';s=p.read_text();line=next(x for x in s.splitlines() if x.startswith('| M08 Sniffing |'));s=s.replace(line,line+f'\n| M09 Social Engineering | [Complete film, source and evidence](../../notes/m09-social-engineering/video-production-2026-10-19.md) | Local {duration} film,11 chapters,captions and editable ZIP; human review separate |');p.write_text(s)
 for p,body in [
 (R/'source/README.md','''<a id="ceh-m09-masterclass"></a>
## October 19 M09 Social Engineering production

[Exact request and source](2026-10-19-ceh-m09-video-production/README.md) → [canonical delivery](../notes/m09-social-engineering/video-production-2026-10-19.md) → [source QA](2026-10-19-ceh-m09-video-production/validation/README.md) / [actual film QA](2026-10-19-ceh-m09-video-production/render-validation/README.md). Source bytes, full production and human acceptance retain distinct evidence.'''),
 (R/'curriculum/official-scope-map.md','''<a id="ceh-m09-masterclass"></a>
## M09 English Masterclass connection — October 19

The [M09 Social Engineering film and sources](../notes/m09-social-engineering/video-production-2026-10-19.md) connect official scope and insider-risk coverage to trust verification, human/computer/mobile techniques, social channels, identity/recovery, assessment, response and the cross-cutting human-risk evidence-review capstone. Eight film questions use M09-film-v1. Prepared content and offline synthetic parsing add no original bank answers or accepted learner practical. The [current course-aligned route](../study-plan/uuu-aligned-ceh-cehp-2026-09-18.md) governs actual learning and capacity.'''),
 (R/'README.md',f'''<a id="ceh-m09-masterclass"></a>
## M09 English Masterclass

[Social Engineering delivery and evidence](notes/m09-social-engineering/video-production-2026-10-19.md): complete {duration} English film,11 chapters/58 native animated scenes,9,814 spoken words,subtitles,source ZIP and editable production ZIP. The [initial series standard v1.0](docs/video-production/PRODUCTION_STANDARD_v1.0.md) preserves M04 v3,Tally/Northstar,narration-only 1.5× and eight 1.000-second quiz holds. Full human viewing/listening remains separate.'''),
 (R/'assessments/practice-bank/README.md','''<a id="ceh-m09-masterclass"></a>
## M09 teaching-media connection

The [M09 English Masterclass](../../notes/m09-social-engineering/video-production-2026-10-19.md) supplies eight graded film questions and a four-case inert-evidence capstone. M09-film-v1 is separate from this bank. Existing original answers, confidence, retests and practical acceptance retain their own records.''')]:append(p,body)
 for rel in ['weeks/2026-W43/days/2026-10-19.md','weeks/2026-W43/weekly-plan.md','data/projects/2026-07-ceh-cehp-certification-training.md']:
  p=PLAN/rel;link=os.path.relpath(NOTE,p.parent)
  body=f'''<a id="ceh-m09-masterclass"></a>
### CEH M09 Social Engineering完整製片 — 2026-10-19

已驗證本機交付：**{duration}／11章／58幕／9,814字／{cues:,}段字幕**的完整英文影片、章節MP4、來源ZIP與可編輯ZIP。Jason指定並採納既有設計、配音與時序；Codex完成新教材、四項模擬證據、動畫、配音、字幕、實際渲染及驗證。[CEH完整紀錄與QA]({link})持詳細內容、雜湊與貢獻，成品位於 ~/Videos/CEH_M09_v1_0/output/。

FIRST PRINCIPLE：保護學習注意力、可信證據與本機執行容量；CEH持內容及技術證據，Videos持大型媒體，Planning持定位、狀態、容量及下一步。初版通則v1.0維持M04 v3、原創Tally／Northstar、僅旁白1.5×及八題各1.000秒零值PCM。實際全片解碼、169張編碼畫面抽查、64項測驗及174次跳轉比較通過；完整證據留owner。

下一關由Jason在容量允許時完成全片觀影／聽驗，依時間碼回報。公開媒體URL、本人答題／實作與Blog各自驗收。W43容量Unknown、共用每週240分鐘與上課日25分鐘上限維持；本次製片不新增工時、期限或本人學習完成。
'''
  append(p,body)
 append(PLAN/'docs/phd-work-log-connections.md','''<a id="ceh-m09-masterclass"></a>
## CEH M09完整製片 — October 19

[CEH成品與實際QA](../../ceh-cehp-certification-notes-2026/notes/m09-social-engineering/video-production-2026-10-19.md) ↔ [10/19日誌](../weeks/2026-W43/days/2026-10-19.md#ceh-m09-masterclass) ↔ [W43](../weeks/2026-W43/weekly-plan.md#ceh-m09-masterclass) ↔ [CEH專案定位](../data/projects/2026-07-ceh-cehp-certification-training.md#ceh-m09-masterclass)。CEH保管完整內容、製片與驗證；Planning保留交付位置、狀態、容量及人工觀影／聽驗下一關，供週回顧與課程複習重用。本人學習與公開媒體發布各有獨立證據。''')
 append(S/'README.md','''## Actual full-film delivery

The authorized source-plus-film workflow has completed and passed automated delivery checks. [Actual render receipts](render-validation/README.md), [recovery inputs](rebuild-inputs/full-production/README.md) and [canonical M09 delivery](../../notes/m09-social-engineering/video-production-2026-10-19.md) establish the final media layer. The source checkpoint above retains its historical scope. Human full viewing/listening and public release remain separate.''')
 p=S/'README.md';s=p.read_text().replace('Full production is active in the separate project; this source-stage receipt establishes its own layer.','The source-stage checkpoint above preceded actual production in the separate project; its receipt establishes its own layer.').replace('Actual narration, final captions, native motion, chapter/master renders, editable-project integrity and human acceptance require their respective receipts.','Actual narration, final captions, native motion, chapter/master renders and editable-project integrity now have their separate receipts below. Full human acceptance remains open.');p.write_text(s)
 print(json.dumps({'duration':duration,'captions':cues,'spoken_clips':spokenclips,'planning_mirrors':4,'state':'final_records_written'}))
if __name__=='__main__':main()

"""Promote current records only after actual media and editable ZIP acceptance."""
from pathlib import Path
import json,re,os
V=Path(__file__).parent;Q=V/'qa';O=V/'output';R=Path('/home/jnlngx10/phd-research/repos/ceh-cehp-certification-notes-2026');P=R.parent/'planning-everything-track';D=R/'source/2026-10-19-ceh-m10-video-production';N=R/'notes/m10-denial-of-service/video-production-2026-10-19.md'
def main():
 d=json.loads((Q/'delivery-validation.json').read_text());z=json.loads((Q/'packaging-receipt.json').read_text());m=json.loads((V/'project/data/master-timing.json').read_text());a=json.loads((Q/'rendered-artifact-audit.json').read_text())
 assert d['status']=='automated_delivery_checks_passed' and z['status']=='editable_zip_crc_extraction_hashes_verified'
 ms=round(d['duration']*1000);mins,rest=divmod(ms,60000);sec,milli=divmod(rest,1000);duration=f'{mins}:{sec:02}.{milli:03}';captions=len(__import__('re').findall(r' --> ',(O/'captions.en-US.srt').read_text()))
 s=N.read_text();s=s.replace('**source_ready; full-film production in progress.**',f"**rendered_and_automated_QA_passed:** complete **{duration}**, {d['frames']:,} frames and {captions:,} subtitle cues at 1920×1080/30fps H.264/AAC.")
 start=s.index('Next production gate:');s=s[:start]+'''Jason owns full timecoded viewing/listening acceptance when capacity permits. Public video release requires a separate authorized action and verified URL. Production adds no learner answers, practical acceptance, attendance, Blog completion or study minutes.

'''
 peak=max(x['full_window_peak'] for x in a['quiz_silence']);nonzero=sum(x['nonzero_channel_samples'] for x in a['quiz_silence'])
 s+=f'''## Complete local media and verification

- Full film: `output/CEH_M10_Denial_of_Service_en-US_1_5x_1s_master.mp4`; SHA-256 `{d['master_sha256']}`.
- Eleven chapter MP4s and chapter marks: `output/chapters/` and `output/chapters.txt`.
- Aligned subtitles: `output/captions.en-US.srt` and `.vtt`; captions are also burned into picture.
- Lossless audio: `output/master.reference.pcm.wav`.
- Editable production: `output/CEH_M10_Denial_of_Service_v1_0_EDITABLE.zip`, {z['bytes']:,} bytes, {z['entries']:,} entries and {z['payload_hashes']:,} extracted payload hashes verified. SHA-256 `{z['sha256']}`.
- Local report and samples: `output/render_report.md`, `output/inspection_frames/`, `output/qa_evidence/` and `output/DELIVERY_SHA256.txt`.

[Actual render evidence](../../source/2026-10-19-ceh-m10-video-production/render-validation/README.md) records all 11 chapter fingerprints, full-root browser checks, 64 question-boundary assertions, 174 repeated/backward scene seeks, full decode and 11 embedded chapter marks. The 115 primary encoded samples and 50 late diagram samples were inspected separately from source previews. Full PCM/AAC continuity has its own receipt. [Recovery implementation](../../source/2026-10-19-ceh-m10-video-production/rebuild-inputs/full-production/README.md) preserves the exact native motion and production scripts.

All eight reference holds contain exactly 48,000 stereo zero PCM frames at 48 kHz. Decoded lossy AAC has maximum full-window peak {peak:.10g} and {nonzero:,} nonzero channel samples across the holds; the residue measurement does not change the exact reference silence claim. Raw clip speech measures {d['raw_clip_wpm']:.4f} WPM; the separate −50 dBFS edge-trimmed estimate is {d['effective_spoken_wpm']:.4f} WPM. No speed retuning or second pass was applied.

All 58 real WAVs have independent unprompted fixed-runtime transcript receipts under availability_validation / LIVE_FULL_COMPLETED. Accuracy and latency remain not_evaluated. Known-text alignment preserves {len(d['alignment_review_flags'])} timing flags as listening leads, not confirmed pronunciation errors. Full human viewing/listening remains open.
'''
 N.write_text(s)
 p=D/'README.md';s=p.read_text().replace('Full-film production is active; its actual acceptance requires separate runtime and encoded-media evidence.','The complete film now has [actual runtime and encoded-media evidence](render-validation/README.md); full human acceptance remains separate.');p.write_text(s)
 entries={
 'README.md':f'[M10 Denial-of-Service delivery](notes/m10-denial-of-service/video-production-2026-10-19.md): complete {duration} English film, 11 chapters/58 native animated scenes, 10,241 canonical words, {captions:,} subtitle cues and verified source/editable ZIPs. Initial series v1.0 applies; human viewing/listening remains separate.',
 'docs/video-production/README.md':f'[Canonical M10 delivery](../../notes/m10-denial-of-service/video-production-2026-10-19.md) provides the complete {duration} film, 11 chapters, 58 animated scenes, 10,241 words and {captions:,} subtitle cues. [Actual source QA](../../source/2026-10-19-ceh-m10-video-production/validation/README.md) and [render QA](../../source/2026-10-19-ceh-m10-video-production/render-validation/README.md) retain separate receipts. Initial v1.0 and full human review boundaries remain unchanged.'}
 for rel,body in entries.items():
  p=R/rel;s=p.read_text();marker='<a id="ceh-m10-masterclass"></a>';head,block=s.split(marker,1);title=block.splitlines()[1];match=re.search(r'\n(?:<a id=|## )',block[1:]);tail=block[1:][match.start():] if match else '';p.write_text(head+marker+'\n'+title+'\n\n'+body+'\n'+tail)
 for rel in ['weeks/2026-W43/days/2026-10-19.md','weeks/2026-W43/weekly-plan.md','data/projects/2026-07-ceh-cehp-certification-training.md','docs/phd-work-log-connections.md']:
  p=P/rel;s=p.read_text();marker='<a id="ceh-m10-masterclass"></a>';head,block=s.split(marker,1);link=os.path.relpath(N,p.parent)
  # Preserve any later unrelated sections if the remote added them.
  match=re.search(r'\n(?:<a id=|## )',block[1:]);tail=block[1:][match.start():] if match else ''
  body=f'''\n### CEH M10 Denial-of-Service 完整製片 — 2026-10-19

已驗證本機交付：**{duration}／11 章／58 幕／10,241 字／{captions:,} 段字幕**的完整英文影片、章節 MP4、來源 ZIP 與可編輯 ZIP。Jason 採納既有 v1.0 設計、配音與時序；Codex 完成新教材、四項模擬證據、動畫、配音、字幕、實際渲染及驗證。[CEH 主紀錄與 QA]({link})持有詳細內容、雜湊與驗收界線，成品位於 ~/Videos/CEH_M10_v1_0/output/。

稀缺資源是學習注意力、可信證據與本機運算／儲存；Planning 持定位、容量、發布狀態與下一步。W43 容量 Unknown，每週共用 240 分鐘、上課日 25 分鐘上限維持。本次教材製作不記為本人答題、實作、Blog 完成或已使用學習工時。

下一關由 Jason 在容量允許時完成全片觀影／聽驗，依時間碼回報。公開影片 URL、本人答題／實作與 Blog 各自驗收。Git 發布以獨立核對憑據更新；大型媒體保留本機。
'''
  p.write_text(head+marker+body+tail)
 print(json.dumps({'duration':duration,'caption_cues':captions,'records':'promoted_from_actual_media_evidence'}))
if __name__=='__main__':main()

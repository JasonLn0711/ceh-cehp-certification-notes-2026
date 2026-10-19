from pathlib import Path
import json
R=Path(__file__).parent/'project'
scenes=json.loads((R/'data/scenes.json').read_text())['scenes']; cues=json.loads((R/'scripts/cues_m10.json').read_text())
out='''---
format: 1920x1080
message: "Protect legitimate availability by matching evidence and controls to the constrained resource."
arc: "Availability → resource mechanisms → evidence → layered protection → four cases → assessment"
audience: "Jason and CEH learners"
mode: autonomous
---

# M10 actual production storyboard

All 58 scenes are required. The canonical source owns the lesson. Durations below are estimates until replaced by actual measured speech. Full source and rendering are authorized without a pilot approval. Source geometry, measured audio alignment, browser checks and encoded-film verification remain distinct evidence layers.

'''
for s in scenes:
 n=int(s['id'][1:]); sid=s['id']; quiz=50<=n<=57
 out+=f"## Frame {n} — {s['title']}\n\n- status: outline\n- src: compositions/{sid}.html\n- duration: {s['editorial_estimate_seconds']}s\n- transition_in: cut\n- scene: {s['visual_direction']}\n- rules: {'css-marker-patterns' if quiz else 'svg-path-draw, css-marker-patterns'}\n- voiceover: {s['narration_en_US']}\n\n"
 out+='Preserve DESIGN.md, original Tally and Northstar. Editable native diagrams occupy x210–1390/y330–710; notes y742–830; captions y945–1028. Show observation points, units, accounting boundaries, causal resource changes and responsible control owners. Fixtures are SIMULATED OUTPUT, never a live attack or deployed defense.\n\n'
 if not quiz:
  assert all(x.lower() in s['narration_en_US'].lower() for x in cues[sid])
  out+='Measured literal cue phrases: '+json.dumps(cues[sid])+'. Derive cue timing from actual aligned audio, not estimated duration.\n\n'
 else:out+='Read the complete question and A–D choices, then exactly 48,000 stereo zero PCM frames at 48 kHz. Reveal the answer only after that one-second hold. Keep captions and all audio outside the hold.\n\n'
(R/'STORYBOARD.md').write_text(out)
print(json.dumps({'frames':len(scenes),'anchored_scenes':len(cues)}))

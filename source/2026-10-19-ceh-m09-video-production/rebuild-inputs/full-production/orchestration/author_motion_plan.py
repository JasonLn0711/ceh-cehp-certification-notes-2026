from pathlib import Path
import json,re
W=Path(__file__).parent;R=W/'project';S=json.loads((R/'data/scenes.json').read_text())['scenes']
cues={
1:['A message asks','A caller asks','A visitor asks','Those technical observations'],
2:["how the requester's identity",'Next identify','whether that identity','inspect the evidence'],
3:['Northstar keeps','Eli works','The learning team','Mara coordinates'],
4:['Approval should identify','participant-protection','Decide how reports','expose personal data'],
5:['A supplied email file','A trusted mail-service record','each stronger statement','Use four columns'],
6:['An urgent request','ordinary pressures','its consequences require','A safe pause'],
7:['borrow authority','Social proof','Scarcity','confirm the request'],
8:['respond to a favor','shared interests','Commitment','sensitive boundary'],
9:['context gathering','A relationship can','first sensitive action','Record which stage'],
10:['A security process','unknown security contact','when the usual manager is absent','A constructive debrief'],
11:['Impersonation presents','The story','requested access','independent record needed'],
12:['ordinary question','Combined details','business purpose','approve disclosure'],
13:['Baiting offers','Quid pro quo','requested action','authorized software process'],
14:['access-controlled boundary','person holding a door','the next entrant','Physical controls should support'],
15:['Shoulder surfing','printed document','observation conditions','approved disposal'],
16:['Human-facing requests','role directory','Technical telemetry can show','Build an evidence chain'],
17:['Phishing uses','A link interaction','A submitted secret','successfully used it'],
18:['Broad phishing','Spear phishing','Whaling','Business email compromise'],
19:['display name','full address','Reply-To','requested action'],
20:['SPF evaluates','DKIM validates','DMARC uses','authorized to change'],
21:['websites','fake support warning','shared document','managed application process'],
22:['Preserve the supplied message','Read the displayed identity','independent record','Record who verified'],
23:['caller can claim','Caller ID','independently maintained','callback is useful'],
24:['text messages','preview hides details','link immediately','established portal directly'],
25:['encode information','controls the destination','sensitive action','known portal independently'],
26:['names, interests','compromised','shared contacts','sensitive-action check'],
27:['An email','a callback number','same source','trusted record'],
28:['identifying information','caller is that employee','successful authentication','later action'],
29:['legitimate access','relevant policy','account actually did','malicious intent'],
30:['unexpected authentication request','repeated prompts','report','identity-service records'],
31:['Recovery exists','approved identity evidence','ticket records','notification'],
32:['ordinary sign-in','recovery','Name the owner','both sides'],
33:['question','participant population','outcome','protected'],
34:['sponsor','State which populations','A stop condition','A useful plan also tells'],
35:['templates','A campaign configuration','A dashboard count','Those remain responsibilities'],
36:['eligible population','failed delivery','An automated link scanner','difficulty of detecting'],
37:['explains the scenario','person who reported','improve those processes','next test'],
38:['original artifact','Detection often begins','Screenshots can be useful','Record hashes'],
39:['Triage asks','evidence ledger','payment is merely requested','authorized finance and incident-response owners'],
40:['mail record','help-desk ticket','identity-service record','finance record'],
41:['held and verified','escalated','original evidence','which uncertainty remains'],
42:['intended state','For an account','At Northstar','Keep implementation'],
43:['E zero one','E zero two','E zero three','E zero four'],
44:['authentication passes','training account reference','independent contact','no completed payment'],
45:['claims to be a staff','contact number','directory record','no identity-service reset'],
46:['Northstar name','encoded URL','established portal','anyone scanned'],
47:['credential','witness report','appointment list','does not enumerate'],
48:['supplier verification','Account recovery','lesson notice','visitor'],
49:['Email protections','Browser protections','software installation','business authority'],
50:['Phishing-resistant','enrollment','At Northstar','For revalidation'],
51:['approved contact record','second reviewer','legitimate supplier change','unverified change request'],
52:['fluent text','synthetic audio','convincing impersonation','independent verification'],
53:["tool's task instructions",'untrusted artifacts','supporting record','compare the output'],
58:['file hashes','strongest supported state','responsible owner','unwanted-condition test']}
# Exact anchors must exist before any diagram can be compiled. A missing anchor is fixed explicitly.
bad=[]
for s in S:
 n=int(s['id'][1:])
 if n not in cues:continue
 for phrase in cues[n]:
  if phrase.lower() not in s['narration_en_US'].lower():bad.append((s['id'],phrase))
if bad:print(json.dumps({'missing_anchors':bad}));raise SystemExit(1)
(R/'scripts/cues_m09.json').write_text(json.dumps({f'S{k:02}':v for k,v in cues.items()},indent=2)+'\n')
out='''---
format: 1920x1080
message: "Verify the requested action through the right source and keep conclusions tied to evidence."
arc: "Trust question → mechanisms → governed analysis → connected cases → controls → assessment"
audience: "Jason and CEH learners"
mode: autonomous
---

# M09 actual production storyboard

All58scenes are required. The immutable source script owns canonical content. Durations below are estimates until replaced by actual measured speech. Full source plus render is already authorized without a pilot or renewed approval gate. Work is authored inline from bounded scene packets; no unapproved native delegation is used.

'''
for s in S:
 sid=s['id'];n=int(sid[1:]);rules='css-marker-patterns' if 54<=n<=57 else 'svg-path-draw, css-marker-patterns'
 out+=f"## Frame {n} — {s['title']}\n\n- status: outline\n- src: compositions/{sid}.html\n- duration: {s['editorial_estimate_seconds']}s\n- transition_in: cut\n- scene: {s['visual_direction']}\n- rules: {rules}\n- voiceover: {s['narration_en_US']}\n\n"
 out+='Preserve DESIGN.md and original Tally. Use editable native geometry, diagram area x200–1420/y300–820, separate right campus/mascot anchor, reserved captions y945–1028. Each requested change, identity claim, independent check and outcome is a separate state. Fictional artifacts carry SIMULATED OUTPUT.\n\n'
 if n in cues:out+='Measured anchor phrases in order of label identities: '+json.dumps(cues[n])+'. Labels: '+json.dumps(s['on_screen_copy'])+'. Use the final audio sample ledger for times, not the editorial estimate.\n\n'
 else:out+='Show one complete stem/A–D set at a time; read all choices before exactly48000stereo zero PCM frames at48kHz, then the correct answer. Derive boundaries from final samples and keep captions outside the holds.\n\n'
out=out.replace('All58scenes','All 58 scenes').replace('exactly48000stereo','exactly 48000 stereo').replace('at48kHz','at 48kHz')
(R/'STORYBOARD.md').write_text(out)
print(json.dumps({'storyboard_frames':58,'anchored_native_scenes':len(cues),'status':'outlined_not_animated'}))

#!/usr/bin/env python3
"""Build M09 evidence guides, separate assessments and four seekable references."""
from pathlib import Path
import html, json, shutil
R=Path(__file__).resolve().parents[1]
def write(n,s):
 p=R/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def dump(n,d):write(n,json.dumps(d,indent=2)+'\n')
S=json.loads((R/'scenes.json').read_text());Q=json.loads((R/'questions.json').read_text())['questions']
events=[
 dict(id='E01',sources=['E01_supplier_message.eml','E01_supplier_record.json','E01_payment_ticket.json'],observed='Expected supplier mailbox, stipulated authentication passes, changed training destination and differing supplied/approved contacts.',unknown='Sender control, supplier authorization and completed payment remain unmeasured.',next_check='Finance verifies through the approved independent contact and required approval/transaction records.'),
 dict(id='E02',sources=['E02_call_transcript.md','E02_directory_record.json','E02_recovery_ticket.json'],observed='Urgent claimed-employee recovery request; supplied contact differs from directory; ticket pending verification.',unknown='Verified identity, reset, enrollment and subsequent account use are not supplied.',next_check='Identity-service owner applies the recovery policy and checks actual account-state records.'),
 dict(id='E03',sources=['E03_notice.md','E03_qr_code.svg','E03_qr_payload.json','E03_portal_context.json'],observed='Reserved encoded destination differs from the stipulated known learning portal; notice approval unconfirmed.',unknown='QR scans, page loads, credential submissions and account use are unmeasured.',next_check='Learning owner verifies the announcement through the known campus route.'),
 dict(id='E04',sources=['E04_appointments.json','E04_door_events.csv','E04_witness_report.md'],observed='One credential event, a door-held interval and an unverified following-person report; claimed visit unconfirmed.',unknown='Entrant count, visitor identity, intent and complete approval state are not established.',next_check='Authorized physical-security owner reviews appointment, escort and access evidence safely.')]
dump('case/NORTHSTAR_M09_EVIDENCE.json',dict(label='SIMULATED OUTPUT',organization='Northstar Learning Center',training_events=events,scope='Inert files and no-send analysis only',actual_measurement='validation/evidence_qa.json measures bytes, parsing and arithmetic; campus events remain fictional.'))
dump('m09_workflow_extensions.json',dict(label='SIMULATED OUTPUT',inherited_map='network_map.json unchanged',people_roles={'June':'Finance verification coordinator','Eli':'Help-desk coordinator','Mara':'Office visitor coordinator'},workflows=['supplier change','account recovery','learning announcement','physical visitor access'],contact_namespace='Reserved .example.test domains and fictional 555-01xx phone strings; no contacts made.'))
write('case/EVIDENCE_CARDS.md','# Four connected Northstar trust cases\n\n**SIMULATED OUTPUT.** The files are constructed teaching artifacts. [Actual offline QA](../validation/evidence_qa.json) measures local parsing, hashes and arithmetic. Receiver authentication strings are stipulated, no QR decoder is exercised, and no contact, account, financial or physical system is activated.\n\n'+'\n\n'.join('## '+e['id']+'\n\nFiles: '+', '.join('[%s](../lab_mock/%s)'%(x,x) for x in e['sources'])+'\n\nObservation: '+e['observed']+'\n\nUnknown: '+e['unknown']+'\n\nNext check: '+e['next_check'] for e in events)+'\n')
write('lab_mock/README.md','''# Offline trust-evidence exercise

**SIMULATED OUTPUT:** 14 inert artifact files and their manifest, including one constructed email, JSON records, authored call/witness/notice text, a generated QR SVG and two CSV tables. The fixed campus dates are fictional context, not collection timestamps.

From the package root run `python3 tooling/verify_evidence.py`. Add `--record` only when deliberately refreshing validation/evidence_qa.json. The verifier uses Python's local email/JSON/CSV parsers and SHA-256. It sends nothing, opens no links, resolves no hosts, collects no credentials and starts no network service. Read the complete [case guide](../case/EVIDENCE_CARDS.md).

E01's Authentication-Results strings are stipulated receiver claims, not actual SPF/DKIM/DMARC execution. E03's QR encoder and source string are recorded; independent QR decoding is not exercised. These boundaries remain explicit. The reserved test-domain destination has no supplied collection page.

The assessment table has 20 fictional eligible rows, 18 delivered rows, six link events (five stipulated learners, one automated scanner), and four reports. Define a denominator and event before computing a rate. These counts describe constructed rows, not employee performance or a population experiment.
''')
write('ASSESSMENT_STUDENT.md','# M09 student worksheet\n\nEight original film questions use M09-film-v1, separate from existing course-bank IDs. Record choice, categorical confidence and reasoning before consulting the independent key. Each authored quiz hold is 1.000 second; pause playback if you need longer.\n\n'+'\n\n'.join('## '+q['id']+' · '+q['level']+'\n\n'+q['prompt']+'\n\n'+'\n'.join(c['letter']+'. '+c['text'] for c in q['choices'])+'\n\nChoice: ____ Confidence: low / medium / high. Reason: ____' for q in Q)+'''

## Integrated trust decision brief

1. Record file hashes, tool version, command, actual local result and evidence location.
2. For E01–E04, identify requested action, claimed authority, independent source, strongest supported state, unknown outcome, owner and next check.
3. Select a mechanism-specific control. Define a legitimate-workflow test and an unwanted-condition test with evidence to save.
4. Calculate eligible/delivered/event/report counts from the constructed metrics CSV. Separate automated events and justify denominators.
5. Draft a no-send awareness-assessment plan: question, approved population/channel, protection, measurement, stop authority, reporting and debrief.
6. Record your own output/result/blocker separately in the learning workspace when the learning activity is activated.

Prepared answers and package-builder results are not learner completion or operational-control acceptance.
''')
write('ASSESSMENT_INSTRUCTOR.md','# M09 independent instructor reference\n\nOpen after recording the original choice/confidence. Preserve original/retest scores separately.\n\n'+'\n\n'.join('## '+q['id']+' — '+q['correct_letter']+'\n\n'+q['explanation'] for q in Q)+'''

## Capstone reference and rubric

E01 supports a requested destination change held for verification; no payment is supplied. E02 supports a pending recovery request; no reset/session is supplied. E03 supports a constructed encoded URL and unconfirmed notice; no interaction or submission is supplied. E04 supports a credential event and an unverified report; entrant attribution remains unknown.

Actual offline counts: 20 eligible, 18 delivered, 6 link events, 5 stipulated learner interactions, 1 automated event and 4 reports. For the constructed delivered denominator, all link events are 6/18, stipulated learner interactions 5/18 and reports 4/18. These are distinct measures, not real employee-quality scores.

Six criteria require evidence: reproducible artifact/tool identities; precise requested-action and authority analysis; supported/unknown separation; independent-source mapping; control owner plus two-sided revalidation; protected no-send assessment with fair measurement and debrief. A proposed check is not an executed recovery, gateway, finance or physical-access test.
''')
coverage=[('Social engineering concepts','S01–S10','Trust, authority, evidence and influence'),('Types and human-based techniques','S11–S16','Pretexts, elicitation, baiting and physical boundaries'),('Impersonation','S11,S23,S27,S43–S48','Claimed roles versus verified permission'),('Computer-based techniques','S17–S22','Messages, warnings, files and business actions'),('Phishing and targeting','S17–S20','Broad/targeted/executive targeting and BEC'),('Phishing tool roles','S21,S33–S35','GoPhish/SET purposes and governed evidence; no campaigns'),('AI impersonation','S23,S52–S53','Original fictional examples and verification limits'),('Identity theft','S28,S31–S32','Identity data, recovery and account control'),('Mobile-based techniques','S23–S27','Voice, text, QR and social channels'),('Countermeasures','S38–S42,S49–S53','Detection, response and two-sided revalidation'),('Anti-phishing toolbar','S49','Managed browser warnings and their limitations'),('Insider-risk course connection','S29,S39–S40','Account events, policy and attribution limits')]
dump('coverage.json',[dict(topic=a,scenes=b,teaching=c) for a,b,c in coverage])
write('COVERAGE_MATRIX.md','# M09 official-topic coverage\n\n[EC-Council public course scope](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/) provides the module backbone. Labels are independently worded. Insider risk also follows the existing UUU-aligned local scope.\n\n| Topic | Scenes | Teaching |\n| --- | --- | --- |\n'+'\n'.join('| '+a+' | '+b+' | '+c+' |' for a,b,c in coverage)+'\n\nQuestions use M09-film-v1; existing bank IDs, learner answers and official labs retain their own evidence.\n')
write('CONCEPT_CONNECTIONS.md','''# Concept and learning connections

M04 identifies service information; M09 distinguishes that information from permission to act. M05 separates a possible weakness from verified impact; M09 applies the same evidence discipline to requests and human-facing outcomes. M06 account and recovery boundaries support M09's identity checks. M07 malware can follow a deceptive interaction, while BEC may involve no malware. M08 packet observations do not establish human authority. M11 sessions and M20 cryptography protect specific technical boundaries without replacing business approval.

The reusable chain is request → claimed identity → authority → independent verification → observed action → bounded outcome. Every case maps those elements to an owner and next check. Keep full production, human acceptance, learner answers, authorized practice and public media release distinct.
''')

examples=[('trust-verification','Verify the requested action',['Request','Identity check','Authority check','Recorded decision']),('message-evidence','Domain checks and business approval',['From: supplier','DMARC: PASS','Change requested','Approval: UNKNOWN']),('independent-callback','Find an independent verification source',['Email request','Supplied number','Approved directory','Required approval']),('quiz-one-second','Read all choices before the hold',[])]
for eid,title,labels in examples:
 for rel in ['fonts/LiberationSans-Regular.ttf','fonts/LiberationSans-Bold.ttf','vendor/gsap.min.js','mascot/tally_point.png']:
  p=R/f'examples/{eid}/assets'/rel;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/'assets'/rel,p)
 css="""@font-face{font-family:LocalSans;src:url('assets/fonts/LiberationSans-Regular.ttf')}@font-face{font-family:LocalSans;src:url('assets/fonts/LiberationSans-Bold.ttf');font-weight:700}*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#F0EBE4;color:#292421;font-family:LocalSans}.root,.clip{position:relative;width:100%;height:100%;overflow:hidden}.inner{padding:84px 138px}.eyebrow{font-size:26px;font-weight:700}h1{font-size:60px;max-width:1540px;margin:25px 0}.diagram{position:relative;width:1450px;height:480px;margin-top:65px}.card{position:absolute;width:550px;height:140px;padding:32px;border:4px solid #292421;background:#FFFAF3;font-size:36px;font-weight:700}.n0{left:0;top:0;background:#F2D4B7}.n1{left:720px;top:0}.n2{left:0;top:260px}.n3{left:720px;top:260px}.edges{position:absolute;inset:0;width:1450px;height:480px}.edges path{fill:none;stroke:#C8755D;stroke-width:6}.cue{position:absolute;left:138px;bottom:210px;font-size:34px;max-width:1450px}.foot{position:absolute;left:138px;bottom:98px;font-size:24px;max-width:1450px}.mascot{position:absolute;right:80px;bottom:190px;width:130px;height:130px}.question{max-width:1550px}.question h2{font-size:40px;margin:20px 0}.question p{font-size:32px;margin:17px 0}.hold,.answer{position:absolute;left:138px;bottom:210px;font-size:32px;padding:16px;background:#F2D4B7;opacity:0}.answer{max-width:1500px}.card{z-index:1}"""
 if labels:
  cue={'trust-verification':'A believable identity claim still needs authority for this action.','message-evidence':'Stipulated domain results do not approve a business change.','independent-callback':'The supplied number shares the request source; use the approved record.'}[eid]
  path={'trust-verification':'M550 70 H720 M995 140 V260 M720 330 H550','message-evidence':'M550 70 H720 M550 330 H720','independent-callback':'M550 70 H720 M275 140 V260 M550 330 H720'}[eid]
  nodes='<svg class="edges" viewBox="0 0 1450 480"><path d="'+path+'"/></svg>'+''.join(f'<div class="card n{i}">{html.escape(l)}</div>' for i,l in enumerate(labels))
  timing=[.5,2.1,4.8,6.8];tweens=''.join(f"tl.fromTo('.n{i}',{{opacity:0,x:{-24 if i%2==0 else 24}}},{{opacity:1,x:0,duration:.65,ease:'power2.out'}},{t});" for i,t in enumerate(timing))
  tweens+="for(const p of document.querySelectorAll('.edges path')){const L=p.getTotalLength();p.style.strokeDasharray=L;tl.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:4.2,ease:'none'},1.4);}tl.fromTo('.cue',{opacity:0},{opacity:1,duration:.5},8.2);"
  extra='<p class="cue">'+cue+'</p>'
 else:
  q=Q[0];nodes='<div class="question"><h2>'+html.escape(q['prompt'])+'</h2>'+''.join('<p>'+c['letter']+'. '+html.escape(c['text'])+'</p>' for c in q['choices'])+'</div>'
  extra='<div class="hold">Think · 1.000 second</div><div class="answer">Answer '+q['correct_letter']+' — verify the trust and approval boundary.</div>'
  tweens="tl.fromTo('.question',{opacity:0},{opacity:1,duration:.4},0);tl.set('.hold',{opacity:0},0);tl.set('.answer',{opacity:0},0);tl.set('.hold',{opacity:1},6);tl.set('.hold',{opacity:0},7);tl.set('.answer',{opacity:1},7);"
 cfg=dict(width=1920,height=1080,fps=30,duration=12)
 dump(f'examples/{eid}/hyperframes.json',cfg)
 write(f'examples/{eid}/index.html',f'''<!doctype html><html lang="en-US"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body><main class="root" data-composition-id="{eid}" data-width="1920" data-height="1080" data-duration="12"><section id="example-scene" class="clip" data-start="0" data-duration="12" data-track-index="0"><div class="inner"><p class="eyebrow">CEH M09 · NORTHSTAR · ANIMATION REFERENCE</p><h1>{title}</h1><div class="diagram">{nodes}</div>{extra}<img class="mascot" src="assets/mascot/tally_point.png" alt="Original Tally"><p class="foot">SIMULATED OUTPUT · illustrative timing; no generated narration</p></div></section></main><script src="assets/vendor/gsap.min.js"></script><script>window.__timelines=window.__timelines||{{}};const tl=gsap.timeline({{paused:true}});{tweens}window.__timelines[{json.dumps(eid)}]=tl;</script></body></html>''')
links=''.join(f'<option value="{eid}">{title}</option>' for eid,title,_ in examples)
write('examples/index.html',f'''<!doctype html><html lang="en-US"><meta charset="utf-8"><title>M09 seekable references</title><style>body{{font:20px sans-serif;background:#F0EBE4;color:#292421;margin:28px}}iframe{{width:960px;height:540px;border:2px solid #292421}}input{{width:640px}}</style><h1>M09 motion references</h1><p>Four 12-second technical examples; final film timing follows measured speech.</p><select id="which">{links}</select><input id="seek" type="range" min="0" max="12" step="0.01" value="0"><output id="time">0.00</output><p><iframe id="frame" title="Animation reference" src="trust-verification/index.html"></iframe></p><script>const frame=document.querySelector('#frame'),seek=document.querySelector('#seek'),which=document.querySelector('#which');which.onchange=()=>{{seek.value=0;frame.src=which.value+'/index.html'}};seek.oninput=()=>{{document.querySelector('#time').value=Number(seek.value).toFixed(2);const tl=frame.contentWindow.__timelines?.[which.value];if(tl)tl.seek(Number(seek.value),false)}};</script></html>''')
print(json.dumps({'stage':'companions_built','cases':4,'questions':8,'motion_examples':4,'official_topic_rows':len(coverage)}))

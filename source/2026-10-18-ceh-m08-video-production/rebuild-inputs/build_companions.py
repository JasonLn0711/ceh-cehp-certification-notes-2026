#!/usr/bin/env python3
from pathlib import Path
import json,html,shutil
R=Path(__file__).resolve().parents[1]
def write(n,s):
 p=R/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
def dump(n,d):write(n,json.dumps(d,ensure_ascii=False,indent=2)+'\n')
S=json.loads((R/'scenes.json').read_text());Q=json.loads((R/'questions.json').read_text())['questions']
events=[
 dict(id='E01',source='lab_mock/visibility_endpoint.pcap and visibility_mirror.pcap',observation='ANALYST endpoint view has one broadcast; mirror view additionally includes three STAFF DNS packets.',limits='Collection topology is stipulated synthetic context, not an actual SPAN measurement.'),
 dict(id='E02',source='lab_mock/arp_claims.pcap',observation='Two replies claim 10.44.10.1 with MAC 02:44:10:00:00:01 and 02:44:10:00:00:66.',limits='Recipient cache, forwarding and approved change status unmeasured.'),
 dict(id='E03',source='lab_mock/dhcp_offers.pcap',observation='One discovery and two offers; transaction 0x4e530008; router options 10.44.10.1 and 10.44.10.66.',limits='No REQUEST/ACK or installed client configuration; no pool exhaustion evidence.'),
 dict(id='E04',source='lab_mock/dns_answers.pcap',observation='One query and two A responses for lesson.northstar.example.test; transaction 0x4808; answers 203.0.113.80 and 203.0.113.81.',limits='No cache adoption, zone-history verdict, later connection or compromise shown.')]
for e in events:e['label']='SIMULATED OUTPUT'
case=dict(organization='Northstar Learning Center',dataset_label='SIMULATED OUTPUT',time_zone='Asia/Taipei UTC+08:00',approved_scope='Read supplied synthetic PCAP files offline; no live capture or traffic transmission.',training_events=events,approval_card=dict(label='SIMULATED OUTPUT',gateway_change='unconfirmed',authorized_router='10.44.10.1',authorized_dns='10.44.20.53',limits='Fictional context, not an actual device inventory export.'),actual_measurement='validation/packet_qa.json records real offline parser measurements of synthetic bytes.')
dump('case/NORTHSTAR_M08_EVIDENCE.json',case)
dump('m08_network_extensions.json',dict(label='SIMULATED OUTPUT',inherited_map='network_map.json unchanged',office_vlan=10,server_vlan=20,office_gateway=dict(ip='10.44.10.1',mac='02:44:10:00:00:01',role='Office SVI and synthetic authorized DHCP service; separate from SWITCH management IP'),staff_mac='02:44:10:00:00:21',analyst_mac='02:44:10:00:00:10',unexpected_sender=dict(ip='10.44.10.66',mac='02:44:10:00:00:66'),domain='lesson.northstar.example.test',returned_documentation_addresses=['203.0.113.80','203.0.113.81']))
write('case/EVIDENCE_CARDS.md','# Northstar connected cases\n\n**SIMULATED OUTPUT.** All campus events, control states and approval context are fictional. Actual offline measurements of the supplied bytes are separately recorded in [packet QA](../validation/packet_qa.json). Fixed fixture timestamps use Asia/Taipei; they are not actual collection times.\n\n'+'\n\n'.join('## '+e['id']+'\n\nSource: '+e['source']+'\n\n'+e['observation']+'\n\nLimit: '+e['limits'] for e in events)+'\n\n## Approval card\n\nSIMULATED OUTPUT. Expected office gateway 10.44.10.1 / 02:44:10:00:00:01; expected resolver 10.44.20.53. A gateway change is unconfirmed. Missing approval is not proof of malicious intent. No switch enforcement result is supplied.\n')
write('ASSESSMENT_STUDENT.md','# Student worksheet — M08 film questions and capstone\n\nRecord choice and categorical confidence (low / medium / high) before opening the separate key. These eight original film questions use M08-film-v1, independently of existing course-bank IDs. Pause for extra thinking time; each authored hold is exactly 1.000 second. Prepared material establishes no learner completion.\n\n'+'\n\n'.join('## '+q['id']+' · '+q['level']+'\n\n'+q['prompt']+'\n\n'+'\n'.join(c['letter']+'. '+c['text'] for c in q['choices'])+'\n\nChoice: ____  Confidence: ____  Reason or evidence: ____' for q in Q)+"""
\n\n## Capstone: a reproducible packet brief
Read [the lab guide](lab_mock/README.md) and [the evidence cards](case/EVIDENCE_CARDS.md).
1. Record your date/time, file hashes, tcpdump version, exact commands and actual results.
2. Compare endpoint and mirror coverage; state why missing rows need a vantage-point check.
3. For E02–E04, record packet fields, a supported observation, an alternative and a next check.
4. Distinguish offer/claim/answer from client adoption, forwarding, cache state and impact.
5. Recommend mechanism-specific controls with owner, prerequisites, legitimate-flow test and unwanted-condition test.
6. Save your brief, evidence and rubric result in the owning learning workspace when activated.
Learner scope confirmed: ____ Actual result/blocker: ____ Review owner: ____
""")
write('ASSESSMENT_INSTRUCTOR.md','# Instructor key and capstone walkthrough\n\nKeep separate until the first choice/confidence is recorded. Original answers and retests retain separate scores.\n\n'+'\n\n'.join('## '+q['id']+' — '+q['correct_letter']+'\n\n'+q['explanation'] for q in Q)+"""
\n\n## Capstone reference
Expected packet totals: endpoint 1; mirror 4; ARP 2; DHCP 3; DNS 3; HTTP 6. The fixture manifest supplies actual generated-file identities. The packet QA receipt records actual offline tool results; the network events remain synthetic.
E01 demonstrates collection coverage. E02 shows two gateway claims, not installed cache state. E03 shows competing offers, not selected configuration or exhausted leases. E04 shows conflicting answers, not accepted cache contents or a successful interception. The HTTP fixture contains a dummy POST and response, with no authentication claim.
A sound brief checks legitimate gateway change, authorized server path, client configuration and resolver policy before strengthening the incident interpretation. Proposed protections are matched to each mechanism and verified for permitted service plus the unwanted condition in a later authorized isolated lab.
## Acceptance rubric
All six criteria require explicit evidence: reproducible file/tool record; correct vantage comparison; accurate protocol-field reading; supported/unknown/alternative separation; control-to-mechanism mapping; owner and two-sided revalidation plan. A proposed plan is not an executed switch test. Package-builder results are not learner execution.
""")
write('lab_mock/README.md',"""# Offline synthetic packet exercise
**SIMULATED OUTPUT:** six deterministic Ethernet PCAP files, not captures of real traffic.
The generator writes bytes only. The executable scope reads files; no interface capture, packet transmission, spoofing, DHCP service, external request or real credential is needed.
From the package root run:
    python3 tooling/verify_packets.py
This prints actual hashes, counts, tool version, commands and results without modifying files. The builder uses --record to save validation/packet_qa.json. Use tcpdump with -r and -nn to preserve the offline numeric workflow.
| File | Declared view | Packets |
| --- | --- | --- |
| visibility_endpoint.pcap | ANALYST ordinary access-port view | 1 |
| visibility_mirror.pcap | stipulated office mirror view | 4 |
| arp_claims.pcap | two gateway claims | 2 |
| dhcp_offers.pcap | discovery plus two offers | 3 |
| dns_answers.pcap | query plus two answers | 3 |
| http_plaintext.pcap | dummy TCP/HTTP exchange | 6 |

For Wireshark, open the local file and try display expressions: arp; ip.addr == 10.44.10.21; udp.port == 67 || udp.port == 68; dns.flags.response == 1; tcp.port == 80. Use Follow TCP Stream on the HTTP file to read the dummy lesson message. Display expressions are documentation-reviewed, not executed by this build's tcpdump verifier. Record your actual Wireshark version/results if you perform them.
The capture-filter language in actual tcpdump checks is different. See [official sources](../SOURCES.md). Preserve original files and use fixture_manifest.json and packet_ledger.csv for identity/timing. A successful offline read proves fixture parsing, not live capture or control enforcement.
""")
# Four finite, deterministic renderable examples. The review slider lives in a separate page.
examples=[('packet-visibility','Where packets become visible', ['STAFF sends','Switch forwards','Destination receives','SPAN copies']),('arp-binding','ARP claims need validation',['Gateway IPv4','Expected MAC','Conflicting MAC','Check approval']),('dhcp-dns','DHCP and DNS evidence',['DHCP offer','Client adoption?','DNS reply','Cache acceptance?']),('quiz-one-second','Question 1: switched visibility',[])]
for eid,title,labels in examples:
 for name in ['fonts/LiberationSans-Regular.ttf','fonts/LiberationSans-Bold.ttf','vendor/gsap.min.js']:
  target=R/f'examples/{eid}/assets'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/'assets'/name,target)
 if labels:
  nodes=''.join(f'<div class="card n{i}"><span>{i+1:02}</span><h2>{html.escape(l)}</h2></div>' for i,l in enumerate(labels))
  extra='<p class="limit">A supplied claim is visible; client acceptance needs additional evidence.</p>'
  tweens="\n".join(f"tl.fromTo('.n{i}',{{opacity:0,y:28}},{{opacity:1,y:0,duration:.7,ease:'power2.out'}},{.5+i*1.6});" for i in range(4))+"\ntl.fromTo('.limit',{opacity:0},{opacity:1,duration:.6},7.4);"
  if eid=='packet-visibility':
   nodes='<svg class="edges" viewBox="0 0 1500 480"><path d="M 720 80 H 780 M 1125 150 V 210 H 375 M 1125 150 V 210 H 1125 V 245"/></svg>'+nodes
   tweens+="\nfor(const p of document.querySelectorAll('.edges path')){const L=p.getTotalLength();p.style.strokeDasharray=L;tl.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:1.3,ease:'none'},2);}"
  if eid=='arp-binding':
   nodes='<svg class="edges" viewBox="0 0 1500 480"><path d="M 750 145 V 210"/></svg>'+nodes
   tweens+="\nconst p=document.querySelector('.edges path');const L=p.getTotalLength();p.style.strokeDasharray=L;p.style.strokeDashoffset=L;tl.fromTo(p,{strokeDashoffset:L},{strokeDashoffset:0,duration:1.2,ease:'none'},1.3);"
  if eid=='dhcp-dns':tweens+="\ntl.fromTo('.n2',{backgroundColor:'#FFFAF3'},{backgroundColor:'#F2D4B7',duration:.5},7);"
  duration=12
 else:
  q=Q[0];nodes='<div class="question"><h2>'+html.escape(q['prompt'])+'</h2>'+''.join('<p>'+c['letter']+'. '+html.escape(c['text'])+'</p>' for c in q['choices'])+'</div>'
  extra='<p class="hold">Think · 1.000 second</p><div class="answer">Answer A — the switch may never deliver those frames.</div>'
  tweens="tl.fromTo('.question',{opacity:0},{opacity:1,duration:.5},0);tl.set('.hold',{opacity:0},0);tl.set('.hold',{opacity:1},6);tl.set('.hold',{opacity:0},7);tl.set('.answer',{opacity:0},0);tl.set('.answer',{opacity:1},7);"
  duration=12
 css='''@font-face{font-family:LocalSans;src:url('assets/fonts/LiberationSans-Regular.ttf')}@font-face{font-family:LocalSans;src:url('assets/fonts/LiberationSans-Bold.ttf');font-weight:700}*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%}body{background:#F0EBE4;font-family:LocalSans,Arial;color:#292421}.root{position:relative;width:100%;height:100%;overflow:hidden}.clip{position:relative;width:100%;height:100%}.inner{position:relative;width:100%;height:100%;padding:96px 138px}.eyebrow{font-size:26px;color:#292421;font-weight:700}h1{font-size:64px;margin:22px 0 40px;max-width:1500px}.nodes{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:34px;width:1500px;margin-top:80px}.card{border:4px solid #292421;background:#FFFAF3;border-radius:0;padding:30px;min-height:150px}.card span{font-size:26px;color:#292421}.card h2{font-size:40px;margin:18px 0}.limit{font-size:36px;max-width:1500px;margin-top:56px}.question{grid-column:1/3}.question h2{font-size:42px;line-height:1.2;margin:0 0 25px}.question p{font-size:36px;margin:14px 0}.hold,.answer{opacity:0;position:absolute;left:138px;bottom:190px;font-size:36px}.answer{padding:24px;background:#F2D4B7;max-width:1500px}.foot{position:absolute;left:138px;bottom:100px;font-size:24px;color:#292421}.edges{position:absolute;left:0;top:0;width:1500px;height:480px;z-index:0}.edges path{stroke:#C8755D;stroke-width:5;fill:none}.card{position:relative}'''
 if eid=='arp-binding':css+='.nodes{height:480px;display:block}.card{position:absolute;width:420px;min-height:125px}.n0{left:540px;top:-35px}.n1{left:540px;top:220px}.n2{left:0;top:220px}.n3{left:1080px;top:220px}.limit{margin-top:0}'
 write(f'examples/{eid}/index.html',f'''<!doctype html><html lang="en-US"><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head><body><main class="root" data-composition-id="{eid}" data-width="1920" data-height="1080" data-duration="{duration}"><section id="example-scene" class="clip" data-start="0" data-duration="{duration}" data-track-index="0"><div class="inner"><p class="eyebrow">CEH M08 · NORTHSTAR · ANIMATION EXAMPLE</p><h1>{title}</h1><div class="nodes">{nodes}</div>{extra}<p class="foot">SIMULATED OUTPUT · illustrative timing, no generated narration</p></div></section></main><script src="assets/vendor/gsap.min.js"></script><script>window.__timelines=window.__timelines||{{}};const tl=gsap.timeline({{paused:true}});{tweens}\nwindow.__timelines[{json.dumps(eid)}]=tl;</script></body></html>''')
 write(f'examples/{eid}/hyperframes.json',json.dumps({'composition':'index.html'},indent=2)+'\n')
write('examples/index.html','''<!doctype html><html lang="en-US"><meta charset="utf-8"><title>M08 seekable examples</title><style>body{font:18px Arial;background:#F0EBE4;color:#292421;margin:24px}select,input{font:inherit}iframe{width:960px;height:540px;border:1px solid #292421;background:#F0EBE4}main{width:960px}input{width:650px}</style><main><h1>Four seekable animation examples</h1><p>Illustrative timing only. Quiz hold: [6.000, 7.000) seconds; answer appears at 7.000. No narration is synthesized.</p><p><select id="which"><option>packet-visibility</option><option>arp-binding</option><option>dhcp-dns</option><option>quiz-one-second</option></select></p><iframe id="f" title="Composition preview"></iframe><p><input id="seek" type="range" min="0" max="12" step="0.001" value="0"><output id="time">0.000</output> s</p></main><script>const f=document.querySelector('#f'),sel=document.querySelector('#which'),seek=document.querySelector('#seek');function load(){f.src=sel.value+'/index.html';seek.value=0}sel.onchange=load;seek.oninput=()=>{const t=Number(seek.value);f.contentWindow.__timelines[sel.value].seek(t,false);document.querySelector('#time').value=t.toFixed(3)};f.onload=()=>{const d=f.contentDocument;d.querySelector('html').style.width='1920px';d.querySelector('html').style.height='1080px';d.body.style.transform='scale(.5)';d.body.style.transformOrigin='0 0';d.body.style.width='1920px';d.body.style.height='1080px'};load();</script></html>''')
write('examples/README.md','''# Four seek-safe motion examples\n\nOpen `index.html` through the package's local HTTP server. Each child directory is a standalone 1920×1080 / 12-second composition with one paused GSAP timeline registered under its root ID. The review slider is outside the composition root.\n\n- `packet-visibility`: source, forwarding, destination and optional mirror path.\n- `arp-binding`: gateway claim nodes and a measured SVG path draw.\n- `dhcp-dns`: compare proposed settings with actual acceptance evidence.\n- `quiz-one-second`: complete Q01 card; illustrative silent hold from 6.000 to 7.000; answer at 7.000.\n\nThese four working examples are source implementation references. They do not claim that all 58 final scene animations, narration, captions, or MP4 have been produced. Actual quiz time is derived after question and choices are synthesized; do not use 6.000 as a final-film timestamp. The real silent WAV is in `production/`.\n\nFor browser inspection, start `python3 -m http.server 8077 --bind 127.0.0.1` from the package root. For HyperFrames validation/render commands, use the installed CLI's `--help` and run from the selected example directory. Preserve the root's fixed duration and local relative assets.\n''')

print(json.dumps({'stage':'companions_built','cases':4,'questions':8,'examples':4}))

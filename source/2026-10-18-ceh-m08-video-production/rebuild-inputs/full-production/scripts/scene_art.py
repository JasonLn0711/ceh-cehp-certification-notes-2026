"""M08 Sniffing native teaching diagrams; generated from measured narration anchors."""
from m08_art_common import *

def S01(a):
 pipeline(a,['Discover objects','Identify roles','Observe behavior','Trace traffic'],['scanner_magnifier','inventory_tag','evidence_slip','m08-packet'],'Observation point → supported claim → next check')
def S02(a):
 for i,(y,w,label) in enumerate([(330,1120,'Ethernet frame: local delivery'),(425,950,'IP packet: network endpoint'),(520,780,'Transport: conversation'),(615,610,'Application: content or ciphertext')]):
  block(a,210+i*45,y,label,i,w,82,SOFT if i==0 else WHITE,'layer-'+str(i))
 note(a,'Recorded bytes → interpretation → bounded claim')
def S03(a):
 P(a,'school_laptop',220,350,185,0);L(a,315,565,'STAFF · 10.44.10.21',0,30,25)
 P(a,'edge_router',680,350,185,1);L(a,775,565,'Office SVI · 10.44.10.1',1,30,27)
 P(a,'office_server',1120,350,185,2);L(a,1215,565,'DNS · 10.44.20.53',2,30,25)
 R(a,430,435,675,435,1,label='Local gateway MAC')
 R(a,885,435,1110,435,2,label='Routed IP delivery')
 block(a,205,640,'ANALYST: named capture point',3,535,83)
 block(a,810,640,'Separate management interface',3,590,83)
 note(a,'Destination IP persists; link-layer addresses change')
def S04(a):
 g=a.add(rect(205,330,1190,370,PAPER,15),'scope-boundary');a.show(g,at(a,0))
 for i,(x,k,l) in enumerate([(245,'scope_sheet','Purpose + owner'),(665,'scanner_magnifier','Named interface'),(1060,'m08-lock','Minimum data')]):
  P(a,k,x,370,190,i);L(a,x+95,650,l,i,31,23)
 note(a,'Offline supplied files only; record retention and stop conditions')
def S05(a):
 table(a,['Destination MAC','Source MAC','EtherType'],[['Local recipient','Local sender','IPv4 / ARP']],row_h=110)
 block(a,210,610,'Broadcast: local domain',2,540,100)
 block(a,850,610,'MAC ≠ human identity',3,540,100)
 note(a,'Read link type and local delivery fields first')
def S06(a):
 P(a,'managed_switch',675,330,190,0);L(a,770,535,'Learning switch',0,34,25)
 table(a,['Source MAC','Observed ingress'],[['STAFF MAC','Office port'],['ANALYST','Audit port']],x=210,y=360,width=420,row_h=85,name='learn')
 block(a,980,350,'Destination lookup',1,400,100)
 block(a,980,510,'Known: selected port',2,400,100)
 block(a,980,650,'Unknown: scoped flood',3,400,100)
 R(a,635,430,670,430,1,True);R(a,875,430,975,430,2,False)
def S07(a):
 P(a,'managed_switch',625,330,215,0);P(a,'school_laptop',220,585,170,1);P(a,'school_laptop',1050,585,170,2)
 L(a,310,790,'ANALYST',1);L(a,1140,790,'STAFF path',2)
 R(a,730,545,1140,585,1,label='Selected delivery')
 R(a,730,545,310,585,2,True,label='No copy guaranteed')
 block(a,205,335,'Promiscuous: local NIC filter',0,350,145)
 block(a,940,335,'Monitor mode: wireless role',3,460,145)
def S08(a):
 block(a,205,340,'Office VLAN',0,350,110,SOFT)
 block(a,675,340,'Gateway',1,250,110)
 block(a,1045,340,'Server VLAN',2,350,110)
 R(a,560,395,665,395,1);R(a,930,395,1035,395,2)
 table(a,['Local frame','IP destination'],[['Gateway MAC','DNS server IP'],['New frame at router','Same destination IP']],x=210,y=500,width=1180,row_h=75)
 note(a,'ARP is local; routing creates a new link-layer frame')
def S09(a):
 four(a,['Packet trace: transport','Switch counters: link','Service log: application','Endpoint: process attribution'],['m08-packet','managed_switch','office_server','school_laptop'])
def S10(a):
 P(a,'school_laptop',245,375,230,0);P(a,'m08-capture',725,365,220,1)
 R(a,485,470,715,470,1,label='Host collection hook')
 block(a,1080,340,'Checksum offload',2,330,120)
 block(a,1080,530,'Segmentation / truncation',3,330,150)
 note(a,'An apparent bad checksum needs collection-path context')
def S11(a):
 nodes(a,['Source port','Switch mirror','Collector'])
 L(a,995,535,'Selected directions',2,30,30)
 note(a,'Copied traffic can exceed mirror or collector capacity')
def S12(a):
 P(a,'school_laptop',220,350,180,0);P(a,'office_server',1130,350,180,0)
 block(a,690,345,'TAP',1,200,110,SOFT)
 R(a,410,425,680,425,1);R(a,895,425,1115,425,1)
 block(a,600,605,'Collector: capacity + directions',2,560,100)
 R(a,790,465,790,595,2)
 note(a,'The monitored link defines coverage; encryption still applies')
def S13(a):
 pipeline(a,['SHA-256','Tool version','tcpdump -nn -r','Saved result'],['m08-packet','inventory_tag','m08-capture','report_file'],'Real parser measurement of synthetic bytes')
def S14(a):
 block(a,210,330,'Capture filter',0,530,100,SOFT)
 block(a,850,330,'Display filter',1,530,100)
 block(a,210,470,'Admission / offline selector',1,530,120)
 block(a,850,470,'Stored-packet visibility',2,530,120)
 L(a,470,650,'udp port 53',2,33,23);L(a,1120,650,'udp.port == 53',2,33,26)
 note(a,'Clearing the display cannot restore excluded packets')
def S15(a):
 table(a,['Layer','Read before concluding'],[['Endpoints','Addresses + transport ports'],['TCP / UDP','State or transaction context'],['Application','Actual request and response']],row_h=88)
 note(a,'A port number alone does not establish application success')
def S16(a):
 four(a,['Capture interval','Snapshot length','Dropped copies','Sensor path'],['analog_clock','m08-packet','m08-boundary','m08-capture'],'Not retained under these conditions ≠ absent from network')
def S17(a):
 table(a,['HTTP fixture','Visible constructed content'],[['POST /classroom','lesson=packet-evidence'],['HTTP/1.1 200 OK','Dummy response: OK']],row_h=102)
 note(a,'Readable body proves visibility here; no real login or credentials')
def S18(a):
 block(a,205,350,'Client',0,300,100)
 block(a,1095,350,'Intended service',0,300,100)
 g=a.add(rect(535,325,530,210,SOFT,12),'tls-channel');a.show(g,at(a,1))
 L(a,800,390,'Authenticated TLS channel',1,34,28)
 L(a,800,465,'Protected application records',1,32,30)
 R(a,510,405,1085,405,2,True)
 block(a,225,615,'Visible: endpoints + timing',2,530,100)
 block(a,850,615,'Check certificate + hostname',3,530,100)
 note(a,'Conceptual TLS diagram; no handshake fixture is claimed')
def S19(a):
 for i,(x,label) in enumerate([(210,'Before tunnel'),(650,'Protected tunnel'),(1090,'After endpoint')]):
  block(a,x,385,label,i,300,130,SOFT if i==1 else WHITE)
  if i:R(a,x-130,450,x-10,450,i)
 block(a,425,625,'Observation point changes what is visible',3,740,100)
 note(a,'Tunnel protection has defined endpoints')
def S20(a):
 compare(a,('Legacy service','Plaintext exposure?'),('Approved alternative','Authenticated protection'),['managed_switch','m08-lock'],'Verify protocol and configuration, not only port number')
def S21(a):
 four(a,['Was relevant traffic retained?','Was the path protected?','What can this sensor show?','Which independent record helps?'],['m08-capture','m08-lock','scanner_magnifier','evidence_thread'])
def S25(a):
 pipeline(a,['Trusted bindings','ARP inspection','Correct trust ports','Permitted + rejected tests'],['inventory_tag','managed_switch','m08-lock','retake_check'],'Static hosts and wrong trust placement require explicit handling')
def S26(a):
 compare(a,('Observe fields','Wireshark / binding monitor'),('Active functions','Separate authorized lab'),['m08-capture','scope_sheet'],'Tool output ≠ changed cache or measured forwarding')
def S27(a):
 table(a,['Observed source','Possible context'],[['New MAC','Replacement / VM / privacy'],['Same MAC','Identity still needs evidence']],row_h=104)
 note(a,'MAC policy is not strong person or device authentication')
def S28(a):
 table(a,['Observation','Dependency / handling'],[['Many source claims','Learning resources'],['Unknown destination','Platform-dependent handling']],width=1180,row_h=104)
 block(a,240,630,'Limit learning / drop / scoped flooding?',3,1120,80)
 note(a,'Table pressure does not guarantee hub-like forwarding')
def S29(a):
 four(a,['Expected devices per port','Learning limit + action','Legitimate classroom flow','Violation + recovery'],['inventory_tag','managed_switch','school_laptop','retake_check'])
def S33(a):
 block(a,210,330,'Access-port intent',0,340,110)
 block(a,655,330,'Trunk prerequisites',1,340,110,SOFT)
 block(a,1095,330,'Allowed VLAN path',2,300,110)
 R(a,560,385,645,385,1,True);R(a,1000,385,1085,385,2,True)
 table(a,['Outer tag','Inner tag','Forwarding conditions'],[['First-hop behavior','Next-hop interpretation','Not universal']],x=210,y=535,width=1180,row_h=88)
 note(a,'A tagged packet alone does not prove boundary crossing')
def S34(a):
 four(a,['Explicit access / trunk roles','Allowed + native VLAN policy','Approved reachability','Intended isolation test'],['managed_switch','scope_sheet','school_laptop','retake_check'])
def S35(a):
 for i,(x,y,label) in enumerate([(235,365,'Expected root'),(825,365,'Neighbor bridge'),(550,630,'Access endpoint')]):
  P(a,'managed_switch' if i<2 else 'school_laptop',x,y,155,min(i,2));L(a,x+80,y+175,label,min(i,2),30,23)
 R(a,405,445,815,445,1,True,'BPDUs + election')
 R(a,880,545,720,650,2,True)
 block(a,1060,615,'Verify selected root + port state',3,350,140)
def S36(a):
 table(a,['Expected role','Guard purpose'],[['Ordinary edge endpoint','BPDU Guard'],['Root must not arrive here','Root Guard'],['Operational recovery','Platform-specific check']],row_h=90)
 note(a,'Guard selection follows topology intent and service needs')
def S39(a):
 compare(a,('Passive observation','Traffic available at a sensor'),('Active manipulation','Changes delivery or network state'),['m08-capture','managed_switch'],'Mechanism, authorization and observed result are separate')
def S40(a):
 P(a,'scanner_magnifier',240,365,225,0)
 block(a,655,335,'Local-Ethernet probe',1,735,100)
 block(a,655,490,'Endpoint + inventory context',2,735,100)
 block(a,655,625,'Negative test ≠ no collector',3,735,100)
 note(a,'Promiscuous state can support legitimate monitoring')
def S41(a):
 table(a,['Question','Tool role'],[['Interactive dissection','Wireshark'],['Actual offline check','tcpdump -r'],['Command-line dissection','TShark: not run here']],row_h=90)
 note(a,'Binding and switch records answer additional questions')
def S42(a):
 compare(a,('Accurate observation','Mapping changed'),('Unverified inference','Attacker caused change'),['evidence_slip','scanner_magnifier'],'Validate the interpretation and sensor coverage separately')
def S43(a):
 table(a,['Evidence to preserve','Interpretation','Next check / owner'],[['Source + packet ID','Bounded hypothesis','Independent record'],['Capture digest + time','Explicit alternatives','Decision owner']],row_h=106)
 note(a,'Several charts from one capture are one underlying observation')
def S44(a):
 compare(a,('ANALYST access view','1 broadcast'),('Office mirror view','4 supplied records'),['school_laptop','managed_switch'])
 block(a,270,740,'3 STAFF DNS records appear only in stipulated mirror view',3,1080,82)
def S45(a):
 table(a,['Packet','Gateway IPv4 claim','Claimed MAC suffix'],[['1','10.44.10.1','...:00:01'],['2','10.44.10.1','...:00:66']],row_h=105,row_times=[a.at(index=0),a.at('Both are visible')])
 note(a,'Approval unconfirmed; recipient cache and forwarding unmeasured')
def S46(a):
 table(a,['Supplied exchange','Proposed router'],[['Discover → approved Offer','10.44.10.1'],['Second Offer, same transaction','10.44.10.66']],row_h=90)
 block(a,245,630,'REQUEST / ACK / installed client state: not supplied',3,1110,80)
 note(a,'Competing offers do not establish acceptance or exhausted pool')
def S48(a):
 pipeline(a,['Collection coverage','ARP claims','DHCP offers','DNS answers'],['m08-capture','managed_switch','m08-lease','dns_drawer'],'Shared context does not prove one successful interception chain')
def S49(a):
 four(a,['Authenticated encryption','Access policy','Switch protections','Monitoring + owner'],['m08-lock','scope_sheet','managed_switch','scanner_magnifier'],'Each control needs prerequisites and a mechanism-specific test')
def S50(a):
 pipeline(a,['Versioned baseline','Permitted service','Unwanted condition','Actual saved result'],['inventory_tag','school_laptop','m08-boundary','report_file'],'Proposed test ≠ completed control enforcement')
def S51(a):
 table(a,['Preserve','Explain'],[['Original bytes + digest','Observation point + time'],['Exact command + result','Claim + limit + next owner']],row_h=110)
 note(a,'Synthetic event, parser measurement and learner result stay distinct')
def S52(a):
 pipeline(a,['Minimized extract','Source-linked proposal','Run the actual filter','Compare original bytes'],['m08-packet','ai_sorter','m08-capture','retake_check'],'AI assists a checkable hypothesis; keep evidence and authority')
def S53(a):
 compare(a,('Unsupported story','Every password stolen'),('Supported brief','Conflicting claims; acceptance unknown'),['m08-packet','m08-evidence'],'Check the exact claim and the evidence needed to strengthen it')
def S58(a):
 pipeline(a,['Verify files + tools','Compare named views','Bound each claim','Verify proposed defense'],['m08-packet','m08-capture','m08-evidence','retake_check'],'Save your own brief and result only when learner execution is activated')

def build(scene,audio):
 a=base(scene,audio)
 sid=scene['id'];modules={**dict.fromkeys(['S22','S23','S24'],'art_arp'),**dict.fromkeys(['S30','S31','S32'],'art_dhcp'),**dict.fromkeys(['S37','S38','S47'],'art_dns')}
 fn=getattr(__import__(modules[sid]),sid) if sid in modules else globals()[sid]
 fn(a);return a

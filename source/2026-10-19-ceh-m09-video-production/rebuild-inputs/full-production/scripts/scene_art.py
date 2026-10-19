"""All M09 native diagrams; full figures are newly authored for Social Engineering."""
from art_common import *

def S01(a):
 flow(a,['Business request','Identity claim','Action authority','Evidence + next check'],['mail_envelope','inventory_tag','scope_sheet','evidence_slip'],'Verify the requested action through the right source')
def S02(a):
 table(a,['Decision question','Evidence to seek'],[['Who is asking?','Independently established identity'],['What may they change?','Action-specific permission'],['What happened?','Actual state and outcome record']])
 note(a,'Account control, permission and business outcome are different claims')
def S03(a):
 four(a,['June: finance approvals','Eli: account recovery','Learning: known portal','Mara: visitor permission'],['report_file','school_laptop','web_window','school_building'],'New workflow roles; inherited campus identities remain unchanged')
def S04(a):
 P(a,'scope_sheet',245,345,235,0)
 C(a,610,330,'Sponsor + scope owner',0,w=775,h=100)
 C(a,610,455,'Participant care + minimum data',1,w=775,h=100)
 C(a,610,580,'Stop contact + reporting + debrief',2,w=775,h=112)
 note(a,'This exercise analyzes inert files without involving real participants')
def S05(a):
 layers(a,['Supplied artifact: encoded bytes','Interpretation: a supported explanation','Unknown outcome: name the missing state','Next check: evidence that changes the decision'],'A suspicious request does not establish completed compromise')
def S06(a):
 P(a,'analog_clock',240,350,240,0)
 C(a,610,330,'A deadline may be genuine',0,w=775,h=100)
 C(a,610,460,'Pressure can shorten verification',1,w=775,h=100)
 C(a,610,590,'Use a workable verified alternative',3,w=775,h=100,fill=SOFT)
 note(a,'A safe pause needs an actionable route to the responsible owner')
def S07(a):
 compare(a,('Appearance and cues','Leader name · logo · other people · scarcity'),('Independent verification','Known announcement owner and approved action path'),'Authority cues are observations, not authorization',['inventory_tag','scope_sheet'])
def S08(a):
 flow(a,['Helpful favor','Shared interest','Small agreement','Sensitive request'],None,'A favor or earlier agreement does not grant sensitive-action permission')
def S09(a):
 flow(a,['Context gathering','Contact + story','Requested action','Outcome evidence'],['inventory_tag','mail_envelope','scope_sheet','evidence_slip'],'A lifecycle organizes evidence; it does not fill missing stages')
def S10(a):
 table(a,['Workflow friction','Usable improvement'],[['Contact hard to find','Known directory and route'],['Owner unavailable','Defined escalation and coverage'],['Fear of reporting','Constructive response and debrief']])
 note(a,'Repair the decision process and preserve legitimate work')
def S11(a):
 person(a,355,370,'Claimed technician',0)
 C(a,640,345,'Printed work order',1,w=340,h=115)
 C(a,1035,345,'Approved appointment?',2,w=350,h=115,fill=SOFT)
 R(a,510,420,625,420,1,dashed=True)
 R(a,985,420,1025,420,3,dashed=True)
 C(a,640,575,'Identity + escort + access permission',3,w=745,h=120)
 note(a,'Confidence, clothing and a document do not establish the right to enter')
def S12(a):
 flow(a,['Ordinary question','Combined details','Need-to-know boundary','Approved disclosure'],['mail_envelope','evidence_thread','shield_lock','scope_sheet'],'Offer the public route; protect private recovery and schedule details')
def S13(a):
 compare(a,('Bait','Attractive content or an unknown device'),('Promised exchange','Help or a reward for cooperation'),'Inspect the required action through the authorized software/data process',['patch_package','risk_scale'])
def S14(a):
 person(a,350,370,'Authorized employee',0);door(a,725,345,0)
 C(a,1065,350,'Following visitor request',2,w=325,h=140)
 C(a,1065,555,'Reception + safe escort route',3,w=325,h=140,fill=SOFT)
 R(a,475,485,700,485,1,dashed=True,label='Access boundary')
 note(a,'Conceptual tailgating risk; a door event does not identify every entrant')
def S15(a):
 four(a,['Screen and keyboard view','Printed sensitive page','Observation conditions','Approved secure disposal'],['school_laptop','report_file','scanner_magnifier','sealed_folder'],'Exposure and information sensitivity need actual evidence')
def S16(a):
 table(a,['People process','Technical record'],[['Verified role + scope','Approved device or access state'],['Formal action approval','Install/session/change event'],['Escalation owner','Preserved log and next check']])
 note(a,'State what each surface verified; keep missing authority explicit')
def S17(a):
 flow(a,['Delivered message','Known interaction','Data submission','Actual account use'],['mail_envelope','web_window','sealed_folder','school_laptop'],'Every stronger outcome needs its own evidence')
def S18(a):
 four(a,['Broad phishing: many recipients','Spear phishing: tailored target','Whaling: senior/high-value target','BEC: deceptive business action'],None,'Targeting and business-fraud purpose can overlap')
def S19(a):
 table(a,['Message field','Constructed E01 context'],[['Display name','Cedar Teaching Supplies'],['From address','supplier@cedar.example.test'],['Reply path','Expected mailbox, still verify action'],['Requested change','TRAINING-ACCOUNT-02']],row_h=75)
 note(a,'The parser exposes supplied fields; sender control remains unmeasured')
def S20(a):
 L(a,790,320,'Domain authentication',0,34,40)
 C(a,210,355,'SPF pass + From-domain alignment',0,w=470,h=105,size=30)
 C(a,210,490,'DKIM pass + From-domain alignment',1,w=470,h=105,size=30)
 C(a,930,420,'DMARC pass: either qualifying aligned result',2,w=455,h=135,fill=SOFT,size=30)
 R(a,690,407,915,455,2);R(a,690,542,915,510,2)
 L(a,795,490,'OR',2,32,5)
 C(a,210,630,'Separate business verification and approval',3,w=1175,h=78)
 note(a,'A domain pass does not approve a supplier or payment change')
def S21(a):
 four(a,['Unexpected file or web page','Fake support warning','Requested software installation','Managed application process'],['web_window','vulnerability_notice','patch_package','scope_sheet'],'Keep content inspection, execution and later system change separate')
def S22(a):
 flow(a,['Preserve original','Read complete fields','Verify independently','Record actual decision'],['sealed_folder','mail_envelope','inventory_tag','report_file'],'Local parsing is real; no message, live link or domain verification is sent')
def S23(a):
 phone(a,260,350,'Caller claim',0)
 C(a,560,330,'Displayed caller ID',1,w=360,h=125)
 C(a,1015,330,'Known directory source',2,w=370,h=125,fill=SOFT)
 R(a,450,450,545,450,1,dashed=True)
 C(a,590,580,'Callback follows the approved recovery policy',3,w=795,h=115)
 R(a,1195,460,1195,570,3)
 note(a,'A convincing voice or supplied number is not independent identity proof')
def S24(a):
 phone(a,250,345,'Text preview',0)
 C(a,575,330,'Small screen hides context',1,w=810,h=110)
 C(a,575,470,'Unexpected account link',2,w=810,h=110)
 C(a,575,610,'Open the known portal independently',3,w=810,h=100,fill=SOFT)
 note(a,'Preserve and report the message through the established route')
def S25(a):
 P(a,'m09-qr',245,365,275,0)
 C(a,650,330,'Encoded reserved test URL',0,w=735,h=110)
 C(a,650,465,'Notice owner + requested action',1,w=735,h=110)
 C(a,650,600,'Known portal verification',3,w=735,h=110,fill=SOFT)
 note(a,'Encoding is not certification; scans and submissions are unmeasured')
def S26(a):
 person(a,345,355,'Profile or account',0)
 C(a,605,330,'Public context + shared contacts',0,w=780,h=110)
 C(a,605,465,'Known account may be compromised',1,w=780,h=110)
 C(a,605,600,'Business permission still required',3,w=780,h=110,fill=SOFT)
 note(a,'Account activity and attribution to a person need different evidence')
def S27(a):
 C(a,210,330,'Email request',0,w=515,h=110)
 C(a,210,500,'Supplied call / text path',1,w=515,h=110)
 R(a,470,445,470,490,2,dashed=True)
 C(a,865,330,'Approved contact record',3,w=520,h=110,fill=SOFT)
 C(a,865,500,'Independent action verification',3,w=520,h=110)
 R(a,1125,445,1125,490,3)
 L(a,470,675,'Same unverified source',2,30,30)
 L(a,1125,675,'Established source + policy',3,30,32)
 note(a,'Several channels can repeat one claim without confirming it independently')
def S28(a):
 layers(a,['Identifying information','Claimed person or role','Actual account control','Authority for the business action'],'Knowing identity details does not prove the right to act')
def S29(a):
 compare(a,('Observed account event','An unusual export or approval request'),('Investigation questions','Permission · context · account control · attribution'),'An alert or account name does not independently establish personal intent',['evidence_slip','scanner_magnifier'])
def S30(a):
 phone(a,245,350,'Unexpected prompt',0)
 C(a,590,330,'Repeated request pressure',1,w=795,h=110)
 C(a,590,465,'Deny + report through known route',2,w=795,h=110,fill=SOFT)
 C(a,590,600,'Review identity-service events',3,w=795,h=110)
 note(a,'A prompt, an approval, a reset and a session are separate states')
def S31(a):
 flow(a,['Recovery request','Identity verification','Authorized reset','Notification + review'],['mail_envelope','inventory_tag','shield_lock','evidence_slip'],'The request record alone does not establish a reset or account use')
def S32(a):
 decision(a,'Protected state change','Normal approved route','Recovery or exception route','Every permitted branch needs an owner, evidence, logs and a two-sided test')
def S33(a):
 flow(a,['One business question','Defined population','Defined outcome','Protection plan'],['scope_sheet','school_building','evidence_slip','shield_lock'],'A no-send worksheet measures reasoning, not live campaign behavior')
def S34(a):
 four(a,['Named sponsor and owner','Population + channel + dates','Stop authority and data limits','Reporting and constructive debrief'],None,'Specific assessment governance comes before tool activation')
def S35(a):
 table(a,['Tool capability','Evidence and ownership'],[['Templates and recipient groups','Approved assessment configuration'],['Delivery and interaction records','Defined event, coverage and limits'],['GoPhish / SET roles','Tool purpose does not grant authority']])
 note(a,'No campaign or credential-collection service is activated by this lesson')
def S36(a):
 C(a,210,325,'20 eligible · 18 delivered',0,w=1180,h=85,fill=SOFT)
 for i in range(18):
  x=225+i*62;fill=ACCENT if i<5 else '#E9B94D' if i==5 else WHITE
  g=a.add(rect(x,470,48,60,fill,2),'metric-unit-'+str(i));a.show(g,at(a,1)+(i%6)*.05)
 L(a,500,590,'5 stipulated learner events',2,32,34)
 L(a,1110,590,'1 automated event',2,32,28)
 L(a,800,670,'6/18 link events ≠ 5/18 stipulated learner interactions',3,30,65)
 note(a,'Constructed counts: define event, denominator and difficulty before comparison')
def S37(a):
 flow(a,['Explain the scenario','Recognize reporting','Repair workflow friction','Plan a useful recheck'],['mail_envelope','report_file','patch_package','retake_check'],'A constructive debrief improves the process and preserves participant care')
def S38(a):
 flow(a,['Original artifact','Reporter context','Time reference','Evidence location'],['sealed_folder','mail_envelope','analog_clock','report_file'],'Make reporting easy; preserve evidence without opening live destinations')
def S39(a):
 four(a,['Requested business change','Known interaction or disclosure','Protected resource at risk','Responsible response owner'],None,'Route the observed state to its owner without inventing impact')
def S40(a):
 table(a,['Record surface','What it may establish'],[['Mail or ticket','Delivery or requested action'],['Identity service','Actual reset/enrollment/session event'],['Business or access record','Approval, transaction or credential event']])
 note(a,'Reliable keys and timing support correlation; a name alone does not prove identity')
def S41(a):
 flow(a,['Hold the sensitive action','Notify responsible owner','Preserve original evidence','Check the next state'],['shield_lock','scope_sheet','sealed_folder','evidence_slip'],'Record the action actually taken and the uncertainty that remains')
def S42(a):
 table(a,['Validation surface','Required evidence'],[['Intended state','Named control and target configuration'],['Legitimate workflow','Actual permitted result'],['Unverified shortcut','Actual hold, refusal or escalation']])
 note(a,'A policy, diagram or proposed test does not establish operational acceptance')
def S43(a):
 four(a,['E01: supplier payment change','E02: urgent account recovery','E03: QR lesson notice','E04: visitor and door event'],['report_file','shield_lock','web_window','school_building'],'Each case separates claimed authority, independent source and outcome')
def S44(a):
 table(a,['Supplied E01 record','Supported state'],[['Supplier address + PASS strings','Stipulated domain context'],['TRAINING-ACCOUNT-02','Change requested; ticket held'],['Independent contact / payment','Supplier approval and payment unmeasured']])
 note(a,'Use the approved supplier record and finance approval route')
def S45(a):
 phone(a,245,350,'Claimed staff',0)
 table(a,['E02 surface','Supplied state'],[['Caller contact','Different from directory'],['Recovery ticket','Pending verification'],['Reset / enrollment / session','No event supplied']],x=580,y=330,w=805,row_h=91)
 note(a,'Follow recovery policy; no completed MFA bypass is established')
def S46(a):
 P(a,'m09-qr',235,370,265,1)
 C(a,625,330,'Notice: Northstar name; approval unconfirmed',0,w=760,h=110)
 C(a,625,465,'Encoded: learn-check test host',1,w=760,h=110)
 C(a,625,600,'Known portal: learn test host',2,w=760,h=110,fill=SOFT)
 note(a,'No scan, page load, credential submission or account use is supplied')
def S47(a):
 door(a,665,340,0)
 C(a,210,330,'Badge event: one credential',0,w=365,h=125)
 C(a,210,530,'Witness report: unverified',1,w=365,h=125)
 C(a,1030,330,'Appointment: unconfirmed',2,w=360,h=125)
 C(a,1030,530,'Entrants and intent: unknown',3,w=360,h=125,fill=SOFT)
 note(a,'The door log does not enumerate or independently identify every entrant')
def S48(a):
 table(a,['Requested action','Owner and independent check'],[['Payment / recovery','Supplier approval / identity policy'],['Portal route / visitor entry','Announcement owner / access permission'],['Outcome claim','Actual state record for that outcome']])
 note(a,'Shared trust questions; mechanism-specific controls and evidence')
def S49(a):
 layers(a,['Mail authentication and filtering','Managed browser warnings and reporting','Approved software, privilege and access','Independent business verification and approval'],'A permitted page or absent warning does not certify a legitimate request')
def S50(a):
 decision(a,'Protected account access','Verifier-bound sign-in','Enrollment + recovery policy','Protect normal and replacement routes; business approval remains separate')
def S51(a):
 C(a,210,335,'Approved contact source',0,w=535,h=110,fill=SOFT)
 C(a,850,335,'Separate approver responsibility',1,w=535,h=110)
 R(a,750,390,840,390,1)
 C(a,210,555,'Test legitimate work',2,w=535,h=120)
 C(a,850,555,'Test unverified shortcut',3,w=535,h=120)
 note(a,'Two approvals are weak if both repeat one unverified source')
def S52(a):
 compare(a,('Generated appearance','Fluent text · synthetic voice · plausible context'),('Evidence needed','Known source · action authority · actual result'),'Realism and detector confidence do not establish identity or authorization',['ai_sorter','scope_sheet'])
def S53(a):
 C(a,210,330,'Trusted task instructions',0,w=535,h=120,fill=SOFT)
 C(a,850,330,'Untrusted message artifact',1,w=535,h=120)
 C(a,210,560,'Link every observation to its source',2,w=535,h=135)
 C(a,850,560,'Review claims and missing evidence',3,w=535,h=135)
 R(a,750,620,840,620,3,dashed=True)
 note(a,'Instructions inside an artifact are data; a fluent summary still needs verification')
def S58(a):
 flow(a,['Artifact + tool identities','Supported + unknown states','Control + owner','Two-sided revalidation'],['evidence_slip','evidence_thread','scope_sheet','retake_check'],'A defensible brief names the next evidence-backed decision')

BUILDERS={name:fn for name,fn in list(globals().items()) if re.fullmatch(r'S\d{2}',name) and callable(fn)}
def build(scene,audio):
 a=base(scene,audio);BUILDERS[scene['id']](a);return a

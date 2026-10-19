#!/usr/bin/env python3
"""Fetch primary-source identities; retain metadata, not redistributed courseware."""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,re,sys,urllib.request
R=Path(__file__).resolve().parents[1]
sources=[
 ('REF01','EC-Council CEH public course scope','https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/','Official course scope','All chapters','Module09 topic backbone; independently authored teaching, no courseware redistribution.'),
 ('REF02','NIST SP800-63B-4','https://pages.nist.gov/800-63-4/sp800-63b.html','Published standard; July2025','S28,S30–S32,S50','Authentication, phishing resistance and authenticator/recovery boundaries; not business approval.'),
 ('REF03','NIST Phish Scale User Guide','https://www.nist.gov/publications/nist-phish-scale-user-guide','Government research guidance','S33,S36–S37,Q07','Email detection difficulty and context; not an individual-ability score or causal proof.'),
 ('REF04','RFC9989 DMARC','https://www.rfc-editor.org/rfc/rfc9989.html','Standards Track; May2026','S20,S44,Q04','Current DMARC core; obsoletes7489/9091. Domain authentication and display-name/business-authority limits.'),
 ('REF05','RFC7208 SPF','https://www.rfc-editor.org/rfc/rfc7208.html','Protocol standard','S20','Sending-source authorization for evaluated domain identities, not payment authorization.'),
 ('REF06','RFC6376 DKIM','https://www.rfc-editor.org/rfc/rfc6376.html','Protocol standard','S20','Signing-domain association and signed-content validation; separate from human intent.'),
 ('REF07','RFC8601 Authentication-Results','https://www.rfc-editor.org/rfc/rfc8601.html','Protocol standard','S19–S22','Receiver result fields require a trusted evaluation context; fixture fields are stipulated only.'),
 ('REF08','FBI IC3 Business Email Compromise','https://www.ic3.gov/CrimeInfo/BEC','Government fraud guidance','S18,S27,S44,S51','Business request verification, response and independently established contacts.'),
 ('REF09','CISA Insider Threat Mitigation Guide','https://www.cisa.gov/sites/default/files/publications/Insider%20Threat%20Mitigation%20Guide_Final_508.pdf','Government mitigation guidance','S29,S39–S40','Program and evidence context; unusual account events do not independently establish personal intent.'),
 ('REF10','Joint advisory: Scattered Spider','https://www.cisa.gov/sites/default/files/2023-11/aa23-320a_scattered_spider_0.pdf','Government threat-intelligence advisory','S23,S30–S32','Primary documented help-desk/identity-targeting pattern; assessment rather than proof about Northstar.'),
 ('REF11','GoPhish user guide','https://docs.getgophish.com/user-guide','Official tool documentation','S35','Simulation platform roles and output interpretation; no campaign execution in this package.'),
 ('REF12','TrustedSec SET project','https://raw.githubusercontent.com/trustedsec/social-engineer-toolkit/master/README.md','Official upstream documentation','S35','Assessment-tool purpose and scope; no toolkit activation.'),
 ('REF13','NIST SP800-50 Rev1','https://csrc.nist.gov/pubs/sp/800/50/r1/final','Published government guidance','S10,S33–S37','Cybersecurity/privacy learning program, measurement and improvement context.')]
def fetch(row):
 i,title,url,kind,scenes,claim=row;d=dict(id=i,title=title,url=url,evidence_class=kind,scenes=scenes,claim_and_limit=claim,retrieved_at=datetime.datetime.now().astimezone().isoformat())
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 CEH educational source verification'})
  with urllib.request.urlopen(req,timeout=45) as response:
   body=response.read();d.update(status='retrieved',http_status=response.status,final_url=response.url,bytes=len(body),content_sha256=hashlib.sha256(body).hexdigest(),content_type=response.headers.get('content-type'))
 except Exception as e:d.update(status='retrieval_blocked',diagnostic=type(e).__name__+': '+str(e))
 return d
results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for d in pool.map(fetch,sources):
  results.append(d);print(f"Primary references {len(results)}/{len(sources)}: {d['id']} {d['status']}",file=sys.stderr,flush=True)
(R/'validation').mkdir(exist_ok=True)
(R/'validation/reference_retrieval.json').write_text(json.dumps(results,indent=2)+'\n')
text='# M09 primary references and claim boundaries\n\nLive retrieval metadata records actual byte identities and failures. It does not by itself prove technical interpretation; the claim mapping below names the reviewed scope. Sources are foundational standards, official guidance or official upstream documentation. Northstar is fictional and is not attributed to any real incident.\n\n'
for d in results:
 text+='## '+d['id']+' — '+d['title']+'\n\n['+d['title']+']('+d['url']+') · '+d['evidence_class']+'\n\nScenes: '+d['scenes']+'. '+d['claim_and_limit']+'\n\nRetrieval: '+d['status']+'; '+d['retrieved_at']+'.'
 if d['status']=='retrieved':text+=' HTTP '+str(d['http_status'])+'; '+str(d['bytes'])+' bytes; SHA-256 '+d['content_sha256']+'.'
 else:text+=' '+d['diagnostic']+'. Browser retrieval or another official primary endpoint must be documented separately before claiming it was read.'
 text+='\n\n'
text+='## Current-version distinction\n\nRFC9989 was published in May2026 and explicitly obsoletes RFC7489 and9091. The lesson uses its current core semantics; older training references remain historical. Receiver authentication, human identity, business approval and transaction outcome remain different claims. SP800-63B-4 is the July2025 final revision. No unmeasured deployment adoption rate, AI-detector accuracy or assessment-causality claim is made.\n'
(R/'SOURCES.md').write_text(text)
print(json.dumps({'references':len(results),'retrieved':sum(d['status']=='retrieved' for d in results),'blocked':sum(d['status']!='retrieved' for d in results)}))

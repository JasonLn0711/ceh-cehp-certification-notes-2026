#!/usr/bin/env python3
"""Read-only offline verification; saves no state unless --record is explicit."""
from pathlib import Path
import hashlib,json,struct,subprocess,shutil,sys,re,datetime
R=Path(__file__).resolve().parents[1];checks=[];runs=[]
def ck(n,p,d=None):checks.append(dict(name=n,pass_=bool(p),detail=d))
manifest=json.loads((R/'lab_mock/fixture_manifest.json').read_text())
for f in manifest['files']:
 b=(R/f['path']).read_bytes();ck(f['path']+' bytes and digest',len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'])
 magic,major,minor,tz,sig,snap,link=struct.unpack('<IHHIIII',b[:24]);ck(f['path']+' classic Ethernet PCAP',(magic,major,minor,snap,link)==(0xa1b2c3d4,2,4,65535,1))
 pos=24;n=0;valid=True
 while pos<len(b):
  ts,usec,inc,orig=struct.unpack('<IIII',b[pos:pos+16]);pos+=16
  valid=valid and inc==orig and pos+inc<=len(b) and usec==0
  packet=b[pos:pos+inc];pos+=inc;n+=1
  typ=struct.unpack('!H',packet[12:14])[0]
  if typ==0x800:
   hdr=packet[14:34];ck(f['path']+f' packet {n} IP checksum',sum(struct.unpack('!10H',hdr))%65535==0)
 ck(f['path']+' complete records and count',valid and pos==len(b) and n==f['packet_count'])
exe=shutil.which('tcpdump');ck('tcpdump available',bool(exe))
if exe:
 version=subprocess.run([exe,'--version'],capture_output=True,text=True)
 for file,expr,count in [('visibility_endpoint.pcap','arp',1),('visibility_mirror.pcap','udp port 53',3),('arp_claims.pcap','arp',2),('arp_claims.pcap','arp and ether src 02:44:10:00:00:66',1),('dhcp_offers.pcap','udp port 67 or udp port 68',3),('dns_answers.pcap','udp src port 53',2),('http_plaintext.pcap','tcp port 80',6),('http_plaintext.pcap','host 203.0.113.80',6),('http_plaintext.pcap','tcp port 443',0)]:
  cmd=[exe,'-nn','-tt','-q','-r',str(R/'lab_mock'/file),expr]
  p=subprocess.run(cmd,capture_output=True,text=True);actual=len(re.findall(r'^\d+\.\d+',p.stdout,re.M))
  ck(file+' filter '+expr,p.returncode==0 and actual==count,dict(expected=count,actual=actual,exit_code=p.returncode))
  runs.append(dict(argv=['tcpdump','-nn','-tt','-q','-r','lab_mock/'+file,expr],stdout=p.stdout,stderr=p.stderr.replace(str(R)+'/', ''),exit_code=p.returncode,matched_packets=actual))
else:version=None
report=dict(status='validated' if all(c['pass_'] for c in checks) else 'failed',scope='Real offline parser measurements of synthetic fixture bytes; no live collection or control enforcement.',recorded_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),tcpdump_version=version.stdout.strip() if version else None,display_filters=dict(status='documentation_reviewed_not_executed',reason='Wireshark/TShark not invoked by this verifier'),checks=checks,runs=runs,passed=sum(c['pass_'] for c in checks),failed=sum(not c['pass_'] for c in checks))
if '--record' in sys.argv:
 (R/'validation').mkdir(exist_ok=True);(R/'validation/packet_qa.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report));sys.exit(0 if report['failed']==0 else 1)

#!/usr/bin/env python3
"""Deterministic synthetic files only. No sockets, transmission or interface access."""
from pathlib import Path
import struct, socket, hashlib, json, datetime, csv, sys
R=Path(__file__).resolve().parents[1]
D=R/'lab_mock';D.mkdir(exist_ok=True)
def ip(x): return socket.inet_aton(x)
def mac(x): return bytes.fromhex(x.replace(':',''))
STAFF='02:44:10:00:00:21';GW='02:44:10:00:00:01';OTHER='02:44:10:00:00:66';ANALYST='02:44:10:00:00:10';BCAST='ff:ff:ff:ff:ff:ff'
def checksum(b):
 if len(b)%2:b+=b'\0'
 n=sum(struct.unpack('!'+str(len(b)//2)+'H',b))
 while n>>16:n=(n&65535)+(n>>16)
 return (~n)&65535
def eth(src,dst,kind,b):return mac(dst)+mac(src)+struct.pack('!H',kind)+b
def ipv4(src,dst,proto,payload,ident):
 h=struct.pack('!BBHHHBBH4s4s',0x45,0,len(payload)+20,ident,0,64,proto,0,ip(src),ip(dst))
 return h[:10]+struct.pack('!H',checksum(h))+h[12:]+payload
def udp(src,dst,sp,dp,b,sm=STAFF,dm=GW):
 u=struct.pack('!HHHH',sp,dp,len(b)+8,0)+b
 pseudo=ip(src)+ip(dst)+struct.pack('!BBH',0,17,len(u))
 c=checksum(pseudo+u) or 65535
 return eth(sm,dm,0x800,ipv4(src,dst,17,u[:6]+struct.pack('!H',c)+u[8:],dp))
def tcp(src,dst,sp,dp,seq,ack,flags,b=b'',sm=STAFF,dm=GW):
 h=struct.pack('!HHIIBBHHH',sp,dp,seq,ack,0x50,flags,65535,0,0)
 c=checksum(ip(src)+ip(dst)+struct.pack('!BBH',0,6,len(h)+len(b))+h+b)
 h=h[:16]+struct.pack('!H',c)+h[18:]
 return eth(sm,dm,0x800,ipv4(src,dst,6,h+b,seq%65535))
def arp(sm,dm,sip,tip,op=2):
 target=mac(dm) if op==2 else bytes(6)
 return eth(sm,dm,0x806,struct.pack('!HHBBH',1,0x800,6,4,op)+mac(sm)+ip(sip)+target+ip(tip))
def name(x):return b''.join(bytes([len(p)])+p.encode() for p in x.split('.'))+b'\0'
question=name('lesson.northstar.example.test')+struct.pack('!HH',1,1)
def dns(answer=None):
 if answer is None:return struct.pack('!HHHHHH',0x4808,0x100,1,0,0,0)+question
 return struct.pack('!HHHHHH',0x4808,0x8180,1,1,0,0)+question+b'\xc0\x0c'+struct.pack('!HHIH',1,1,60,4)+ip(answer)
def bootp(server=None,router=None):
 op=1 if server is None else 2
 fixed=struct.pack('!BBBBIHH4s4s4s4s16s64s128s',op,1,6,0,0x4e530008,0,0x8000,ip('0.0.0.0'),ip('0.0.0.0' if server is None else '10.44.10.21'),ip('0.0.0.0' if server is None else server),bytes(4),mac(STAFF)+bytes(10),bytes(64),bytes(128))
 opts=b'\x63\x82\x53\x63'+bytes([53,1,1 if server is None else 2])
 if server:opts+=bytes([54,4])+ip(server)+bytes([1,4])+ip('255.255.255.0')+bytes([3,4])+ip(router)+bytes([6,4])+ip('10.44.20.53')+bytes([51,4])+struct.pack('!I',3600)
 return fixed+opts+b'\xff'
base=int(datetime.datetime(2026,10,18,9,tzinfo=datetime.timezone(datetime.timedelta(hours=8))).timestamp())
ledger=[]
def save(filename,packets,offset,vantage,meaning):
 out=struct.pack('<IHHIIII',0xa1b2c3d4,2,4,0,0,65535,1)
 for i,p in enumerate(packets):
  ts=base+offset+i
  out+=struct.pack('<IIII',ts,0,len(p),len(p))+p
  ledger.append(dict(file=filename,packet=i+1,epoch_seconds=ts,frame_bytes=len(p),vantage=vantage,provenance='SIMULATED OUTPUT'))
 path=D/filename;path.write_bytes(out)
 return dict(path='lab_mock/'+filename,bytes=len(out),sha256=hashlib.sha256(out).hexdigest(),packet_count=len(packets),link_type='Ethernet (DLT_EN10MB)',snaplen=65535,timestamp_basis='fixed synthetic 2026-10-18 Asia/Taipei; no wall clock',vantage=vantage,meaning=meaning,provenance='SIMULATED OUTPUT')
dq=udp('10.44.10.21','10.44.20.53',53008,53,dns())
dr1=udp('10.44.20.53','10.44.10.21',53,53008,dns('203.0.113.80'),GW,STAFF)
dr2=udp('10.44.20.53','10.44.10.21',53,53008,dns('203.0.113.81'),GW,STAFF)
br=arp(ANALYST,BCAST,'10.44.10.10','10.44.10.1',1)
files=[
save('visibility_endpoint.pcap',[br],0,'ANALYST ordinary office access-port endpoint view','One local broadcast only; no STAFF unicast delivered in this constructed subset.'),
save('visibility_mirror.pcap',[br,dq,dr1,dr2],0,'Office VLAN fictional mirror destination','Includes the same broadcast and additional STAFF DNS unicast. Configuration is stipulated, not measured.'),
save('arp_claims.pcap',[arp(GW,STAFF,'10.44.10.1','10.44.10.21'),arp(OTHER,STAFF,'10.44.10.1','10.44.10.21')],120,'Office VLAN fictional mirror destination','Two claims; no recipient cache or measured forwarding.'),
save('dhcp_offers.pcap',[udp('0.0.0.0','255.255.255.255',68,67,bootp(),STAFF,BCAST),udp('10.44.10.1','255.255.255.255',67,68,bootp('10.44.10.1','10.44.10.1'),GW,BCAST),udp('10.44.10.66','255.255.255.255',67,68,bootp('10.44.10.66','10.44.10.66'),OTHER,BCAST)],180,'Office VLAN fictional mirror destination','Discover and two offers; no REQUEST/ACK, client adoption or exhausted pool.'),
save('dns_answers.pcap',[dq,dr1,dr2],240,'Office VLAN fictional mirror destination','Query and conflicting A answers; no cache state or later application acceptance.')]
body=b'lesson=packet-evidence'
request=b'POST /classroom HTTP/1.1\r\nHost: lesson.northstar.example.test\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: '+str(len(body)).encode()+b'\r\n\r\n'+body
response=b'HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK'
src,dst='10.44.10.21','203.0.113.80'
http=[tcp(src,dst,50080,80,100,0,2),tcp(dst,src,80,50080,900,101,0x12,sm=GW,dm=STAFF),tcp(src,dst,50080,80,101,901,0x10),tcp(src,dst,50080,80,101,901,0x18,request),tcp(dst,src,80,50080,901,101+len(request),0x18,response,GW,STAFF),tcp(src,dst,50080,80,101+len(request),901+len(response),0x10)]
files.append(save('http_plaintext.pcap',http,300,'STAFF office-side constructed endpoint view','Complete illustrative TCP request/response with dummy lesson text; no credentials or authentication.'))
(D/'fixture_manifest.json').write_text(json.dumps(dict(provenance='SIMULATED OUTPUT',generator='tooling/build_packets.py',transport_action='file bytes only; no packets transmitted',files=files),indent=2)+'\n')
with (D/'packet_ledger.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(ledger[0]));w.writeheader();w.writerows(ledger)
print(json.dumps({'stage':'synthetic_packets_built','files':len(files),'packets':len(ledger),'transmitted':0}))

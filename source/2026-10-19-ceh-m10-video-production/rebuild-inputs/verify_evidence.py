"""Independent byte parsing and arithmetic for the inert M10 case files."""
from pathlib import Path
import csv,json,struct,hashlib,os
R=Path(__file__).resolve().parents[1];L=R/'lab_mock';checks=[]
def check(name,condition):
    checks.append(dict(name=name,passed=bool(condition)))
    if not condition:raise AssertionError(name)
def rows(name):return list(csv.DictReader((L/name).open()))
for name,h in json.loads((L/'FILES_SHA256.json').read_text()).items():check('hash:'+name,hashlib.sha256((L/name).read_bytes()).hexdigest()==h)
wan=rows('E01_wan_windows.csv')
for r in wan:
    rate=int(r['provider_offered_ip_octets'])*8/int(r['window_seconds'])/1e6
    accepted=int(r['campus_accepted_ip_octets'])*8/int(r['window_seconds'])/1e6
    discarded=int(r['constrained_ingress_discarded_ip_octets'])*8/int(r['window_seconds'])/1e6
    check('E01 conservation:'+r['phase'],rate==accepted+discarded)
    check('E01 ingress capacity:'+r['phase'],accepted<=int(r['capacity_mbps']))
    check('E01 simulation:'+r['phase'],r['provenance']=='SIMULATED OUTPUT')
incident=next(r for r in wan if r['phase']=='incident')
check('E01 offered 2400Mbps',int(incident['provider_offered_ip_octets'])*8/60/1e6==2400)
state=rows('E02_connection_state.csv');incident=next(r for r in state if r['phase']=='incident')
check('E02 backlog full',int(incident['half_open_entries'])==int(incident['backlog_capacity'])==1024)
check('E02 unique completion fraction',int(incident['completed_unique_handshakes'])/int(incident['unique_attempts'])==.01)
check('E02 retransmissions separate',int(incident['separately_counted_retransmissions'])==9000)
b=(L/'E03_reflector_fixture.pcap').read_bytes();check('PCAP Ethernet link',struct.unpack('<I',b[20:24])[0]==1)
offset=24;packets=[]
while offset<len(b):
    sec,micro,inc,original=struct.unpack('<IIII',b[offset:offset+16]);offset+=16
    frame=b[offset:offset+inc];offset+=inc;check('PCAP complete frame',len(frame)==inc==original)
    check('PCAP IPv4 type',frame[12:14]==b'\x08\x00')
    ip=frame[14:];check('IP total length',struct.unpack('!H',ip[2:4])[0]==len(ip))
    check('IP UDP protocol',ip[9]==17)
    dns=ip[28:];packets.append(dict(frame=frame,ip=ip,dns=dns))
check('Two constructed packets',len(packets)==2)
a,z=packets;check('DNS transaction matches',a['dns'][:2]==z['dns'][:2])
check('DNS flags request response',a['dns'][2]&128==0 and z['dns'][2]&128==128)
check('Reflected IP directions',a['ip'][12:16]==z['ip'][16:20] and a['ip'][16:20]==z['ip'][12:16])
check('IP amplification 50',len(z['ip'])/len(a['ip'])==50)
check('Ethernet ratio distinct',len(z['frame'])/len(a['frame'])!=50)
check('Reserved DNS question',b'example\x04test' in a['dns'])
work=rows('E04_request_work.csv');demand={r['phase']:int(r['requests_per_second'])*int(r['toy_cpu_service_ms_per_request'])/1000 for r in work}
check('E04 baseline2cores',demand['baseline']==2)
check('E04 offered24cores',demand['incident']==24)
check('Legitimate enrollment1.5cores',demand['legitimate_enrollment']==1.5)
check('Offered work exceeds8corebudget',demand['incident']>8)
status=json.loads((L/'case_status.json').read_text());check('No live deployment',not status['live_network_execution'] and not status['live_controls_deployed'])
result=dict(status='passed',passed=len(checks),failed=0,checks=checks,live_network_execution=False,
            actual_validation='File hashes, CSV arithmetic and independent PCAP/IP/DNS field parsing.',
            inference_boundary='Toy output is not observed Internet traffic, actual mitigation efficacy or learner acceptance.')
if not os.environ.get('CEH_EVIDENCE_READONLY'):
 (R/'validation').mkdir(exist_ok=True);(R/'validation/evidence-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

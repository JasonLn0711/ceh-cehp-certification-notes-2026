"""Construct inert, explicitly simulated M10 records; never opens a socket."""
from pathlib import Path
import csv, json, struct, hashlib

R = Path(__file__).resolve().parents[1]
L = R / 'lab_mock'
L.mkdir(exist_ok=True)

def dump(name, value):
    p = L / name
    p.write_text(json.dumps(value, indent=2) + '\n')

def table(name, rows):
    with (L / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

base = dict(provenance='SIMULATED OUTPUT', window_seconds=60, layer='IPv4 IP octets')
wan = []
for phase, offered, accepted, cpu, success in [
    ('baseline', 50, 50, 30, 100),
    ('legitimate_enrollment', 150, 150, 40, 99),
    ('incident', 2400, 200, 25, 20),
    ('proposed_control_fixture', 80, 80, 35, 98),
]:
    wan.append(dict(base, case_id='E01', phase=phase, capacity_mbps=200,
                    provider_offered_ip_octets=offered * 1_000_000 * 60 // 8,
                    campus_accepted_ip_octets=accepted * 1_000_000 * 60 // 8,
                    constrained_ingress_discarded_ip_octets=(offered-accepted) * 1_000_000 * 60 // 8,
                    cpu_percent=cpu, stipulated_probe_attempts=100, stipulated_probe_success=success))
table('E01_wan_windows.csv', wan)
table('E02_connection_state.csv', [
    dict(provenance='SIMULATED OUTPUT', case_id='E02', phase=phase,
         window_seconds=60, backlog_capacity=1024, half_open_entries=half,
         unique_attempts=attempts, completed_unique_handshakes=complete,
         separately_counted_retransmissions=retry, link_mbps=rate,
         stipulated_probe_attempts=100, stipulated_probe_success=success)
    for phase, half, attempts, complete, retry, rate, success in [
        ('baseline', 24, 600, 594, 12, 25, 99),
        ('incident', 1024, 6000, 60, 9000, 30, 5),
        ('proposed_control_fixture', 128, 6000, 5400, 400, 32, 90),
    ]
])
table('E04_request_work.csv', [
    dict(provenance='SIMULATED OUTPUT', case_id='E04', phase=phase,
         requests_per_second=rps, toy_cpu_service_ms_per_request=ms,
         cpu_core_budget=8, dependency_pool_capacity=32,
         dependency_busy=busy, queued_requests=queue)
    for phase, rps, ms, busy, queue in [
        ('baseline', 100, 20, 12, 0),
        ('incident', 120, 200, 32, 400),
        ('legitimate_enrollment', 300, 5, 18, 0),
        ('proposed_control_fixture', 100, 30, 20, 10),
    ]
])

def checksum(data):
    if len(data) % 2: data += b'\0'
    value = sum(struct.unpack('!' + 'H'*(len(data)//2), data))
    while value >> 16: value = (value & 65535) + (value >> 16)
    return (~value) & 65535

def addr(s): return bytes(int(x) for x in s.split('.'))

def ip_udp(src, dst, sport, dport, payload, ident):
    udp = struct.pack('!HHHH', sport, dport, 8+len(payload), 0) + payload
    pseudo = addr(src) + addr(dst) + struct.pack('!BBH', 0, 17, len(udp))
    udp = udp[:6] + struct.pack('!H', checksum(pseudo+udp) or 65535) + udp[8:]
    header = struct.pack('!BBHHHBBH4s4s', 69, 0, 20+len(udp), ident, 0, 64, 17, 0, addr(src), addr(dst))
    return header[:10] + struct.pack('!H', checksum(header)) + header[12:] + udp

qname = b'\x01a\x07example\x04test\0'
question = qname + struct.pack('!HH', 16, 1)
request_dns = struct.pack('!HHHHHH', 0x1010, 0x0100, 1, 0, 0, 0) + question
txt = (b'\xff' + b'x'*255)*11 + b'\x6f' + b'x'*111
answer = b'\xc0\x0c' + struct.pack('!HHIH', 16, 1, 60, len(txt)) + txt
response_dns = struct.pack('!HHHHHH', 0x1010, 0x8180, 1, 1, 0, 0) + question + answer
request = ip_udp('192.0.2.10', '198.51.100.53', 53000, 53, request_dns, 1)
response = ip_udp('198.51.100.53', '192.0.2.10', 53, 53000, response_dns, 2)
assert len(request) == 60 and len(response) == 3000
ether = bytes.fromhex('0200000000020200000000010800')
with (L/'E03_reflector_fixture.pcap').open('wb') as f:
    f.write(struct.pack('<IHHIIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1))
    for sec, micros, packet in [(0, 0, request), (0, 1000, response)]:
        frame=ether+packet
        f.write(struct.pack('<IIII', sec, micros, len(frame), len(frame)))
        f.write(frame)
dump('E03_observation_contract.json', dict(
    provenance='SIMULATED OUTPUT', case_id='E03', fixture='E03_reflector_fixture.pcap',
    purpose='Two constructed packets; not a captured or replayed attack.',
    observation_point='Constructed reflector-side request and response; victim ingress is a separate viewpoint.',
    network='Reserved documentation IPv4 addresses, reserved example.test name; teaching MTU 9000.',
    source_claim='Victim address is deliberately assigned by this constructor; source identity is not authenticated.',
    ip_request_octets=60, ip_response_octets=3000,
    ethernet_request_octets_without_FCS=74, ethernet_response_octets_without_FCS=3014,
    deployment='No packets sent; no resolver or collection service started.'
))
dump('case_status.json', dict(
    provenance='SIMULATED OUTPUT', cases=['E01','E02','E03','E04'],
    observed_layer='Constructed files and toy arithmetic only',
    live_network_execution=False, live_controls_deployed=False,
    proposed_control_rows='Stipulated teaching outcomes; they do not prove real mitigation efficacy.',
    attribution='Resource pressure and availability impact do not establish personal identity or intent.'
))
(L/'README.md').write_text('''# Inert Northstar availability evidence

Every record is **SIMULATED OUTPUT**. The builder creates CSV/JSON and two valid constructed DNS/IP packets inside a PCAP; it never sends packets or opens a socket. Documentation addresses and example.test names identify toy records. The packet fixture uses a stipulated 9000-byte teaching MTU; its large response is not an Internet path-MTU observation.

E01 compares aligned IP-octet windows at distinct provider and campus observation points. E02 unique connection attempts, completions and retransmissions are separately stipulated counters. E03 demonstrates a 50× ratio at the IP layer; the Ethernet ratio has a different denominator. E04 calculates offered CPU service demand from toy per-request work, separately from dependency-pool occupancy.

`proposed_control_fixture` rows are constructed expected states. A real deployment requires a separately authorized two-sided test and service recovery evidence. Source construction, local parsing, learner execution and real network observations remain distinct.
''')
dump('FILES_SHA256.json', {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(L.iterdir()) if p.is_file() and p.name!='FILES_SHA256.json'})
print(json.dumps(dict(stage='inert_evidence_constructed', files=len(list(L.iterdir())), live_network_execution=False)))

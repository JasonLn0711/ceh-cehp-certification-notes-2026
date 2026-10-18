#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def write(n,s):
 p=R/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding='utf-8')
refs=[
('ECC','EC-Council CEH v13 course outline','https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh-v13-north-america/','Living course page','C01–C11','Official M08 topic boundary; active course labs retain their own authorization.'),
('WS','Wireshark User Guide','https://www.wireshark.org/docs/wsug_html/','Living development guide; version 5.1.0 displayed at access, not asserted as stable installed version','S07,S10–S18,S40–S43','Capture/display languages, dissection, offload and collection limits. No Wireshark execution receipt is claimed.'),
('PCAP','The Tcpdump Group libpcap filter manual source','https://github.com/the-tcpdump-group/libpcap/blob/master/pcap-filter.manmisc.in','Living upstream source','S13–S14,S41','Capture expression semantics; actual installed tcpdump/libpcap versions are in packet QA.'),
('ARP','RFC 826: Ethernet Address Resolution','https://www.rfc-editor.org/rfc/rfc826','November 1982','S05–S08,S22–S26','Foundational local address-resolution mechanism, not evidence of any Northstar event.'),
('DHCP','RFC 2131: Dynamic Host Configuration Protocol','https://www.rfc-editor.org/rfc/rfc2131','March 1997','S30–S32,S46','Lease exchange, states and client selection; a supplied offer does not establish installed configuration.'),
('DNSSEC','RFC 4033: DNS Security Introduction and Requirements','https://www.rfc-editor.org/rfc/rfc4033','March 2005','S37–S38,S56','Signed-data authentication/integrity and validation assumptions; no DNS query confidentiality guarantee.'),
('TLS','RFC 8446: TLS 1.3','https://www.rfc-editor.org/rfc/rfc8446','August 2018','S18–S21','Protected channel and authentication model; no TLS runtime is supplied in the fixtures.'),
('DAI','Cisco: Troubleshoot DAI and IP Source Guard','https://www.cisco.com/c/en/us/support/docs/switches/lan-switch-software/222274-troubleshoot-dynamic-arp-inspection-dai.html','Vendor platform-specific guidance','S25,S29–S32,S49–S50','Binding and trust prerequisites; vendor examples are not deployed Northstar configuration.'),
('L2','Cisco: Layer 2 security feature configuration example','https://www.cisco.com/c/en/us/support/docs/switches/catalyst-3750-series-switches/72846-layer2-secftrs-catl3fixed.html','Historical Catalyst example; platform/release-specific','S25,S29,S32','Port security and DHCP concepts; verify current target commands before any live change.')]
refs.extend([
('STP','Cisco Catalyst 6500 best-practice recommendations','https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst6500/ios/12-2SX/best/practices/recommendations.html','Historical platform-specific guidance','S33–S36','Trunk/VLAN and STP guard design; current platform commands require separate validation.'),
('BC','Bettercap Ethernet spoofers overview','https://www.bettercap.org/modules/ethernet/spoofers/introduction/','Living project documentation','S26,S37','Named ARP and DNS spoofing roles only; no active tool execution or TLS interception success inferred.'),
('NMAP','Nmap sniffer-detect script documentation','https://nmap.org/nsedoc/scripts/sniffer-detect.html','Living project documentation','S40','Intrusive local-Ethernet promiscuous-mode test; a negative result does not rule out every collector.')
])

write('SOURCES.md','# Primary references and limits\n\nLive access: 2026-10-18, Asia/Taipei. Source roles and dates are recorded below. The narration and questions are independently authored. All Northstar events are SIMULATED OUTPUT; sources explain mechanisms and do not prove fictional campus events.\n\n| ID | Source | Publication context | Connection | Use and limit |\n| --- | --- | --- | --- | --- |\n'+'\n'.join(f'| {i} | [{t}]({u}) | {d} | {s} | {l} |' for i,t,u,d,s,l in refs)+'\n\nFoundational protocols and modern deployment choices remain separate. The course outline defines module coverage; Wireshark and upstream libpcap define their own analysis interfaces. Vendor feature guidance applies to its named platforms. AI assistance is a proposed analysis aid, not an observed autonomous deployment. This source review does not establish a completed learner research block or official practical lab.\n')
coverage=[
('Packet observation fundamentals','S01–S18,S39','Visibility, workflow, content protection and evidence'),
('MAC-table pressure','S06,S28–S29','Learning resources and platform-dependent forwarding'),
('DHCP resource exhaustion','S30–S32,S46','Lease mechanism, pool evidence and separate acceptance claims'),
('False ARP bindings','S22–S25,S45','Local mapping and MITM prerequisites'),
('ARP manipulation tool roles','S26,S41','Observation versus active functions; offline-only exercise'),
('MAC address impersonation','S27,S29','Address claims, inventory and access policy'),
('Cross-VLAN techniques','S33–S34','Trunk and tag prerequisites plus isolation verification'),
('STP topology manipulation','S35–S36','Root/port role changes and guard distinctions'),
('DNS response manipulation','S37–S38,S47','Transaction context, cache limits and protections'),
('DNS analysis and tool roles','S14–S15,S26,S37–S38,S41','DNS spoofing tool roles plus analysis tools; no rogue service execution'),
('Packet analysis tools','S10–S16,S41','Actual offline workflow and separate display expressions'),
('Detecting suspicious collectors','S39–S43','Endpoint/network evidence and passive-observer limits'),
('Promiscuous-mode detection limits','S07,S40','Implementation-dependent probes and bounded conclusions')]
write('COVERAGE_MATRIX.md','# M08 coverage matrix\n\nThe [official course outline](https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh-v13-north-america/) supplies the 13 topic areas. This table uses independently worded labels and maps them to the actual lesson.\n\n| Topic area | Scenes | Teaching evidence |\n| --- | --- | --- |\n'+'\n'.join(f'| {t} | {s} | {e} |' for t,s,e in coverage)+'\n\nEight film questions use M08-film-v1. Existing bank IDs and learner answers remain separate. Active official labs retain their own environment, scope and acceptance.\n')
write('coverage.json',json.dumps([dict(topic=t,scenes=s,evidence=e) for t,s,e in coverage],indent=2)+'\n')
write('CONCEPT_CONNECTIONS.md','''# Concept connections

| Prior concept | M08 connection | Next use | Evidence boundary |
| --- | --- | --- | --- |
| M03 discovery | Visibility and collection point, S01–S16 | Choose a sensor for a concrete network question | Missing capture data does not establish an absent host |
| M04 enumeration | Device/service identities, S03,S15 | Join traffic to an inventory | Packet addresses do not prove a human or process identity |
| M05 vulnerability analysis | Protocol and configuration prerequisites, S22–S38 | Choose a mechanism-specific control | A possible weakness is not observed exploitation |
| M06 permissions | Capture authority and host evidence, S04,S10 | Bound collection and operational actions | File parsing is not live capture permission |
| M07 behavior analysis | Network clue and independent source, S09,S43 | Correlate records without shared-source double counting | A connection is not confirmed data theft |
| M08 claims and acceptance | ARP/DHCP/DNS cases, S44–S48 | Write a defensible packet brief | Claims, adopted state and impact stay separate |
| P3 traffic analysis | Read-only PCAP capstone, S58 | Later learner-executed practical acceptance | Builder QA is not learner evidence |
| M11/M16/M18 | Session, wireless and IoT observation limits | Reuse capture-placement and encrypted-path reasoning | Later modules retain their own scope |
| Existing W3 class locator | Sniffing/HTTP teaching connection | Return to the class evidence and unresolved acceptance checks | This new synthetic fixture does not retroactively validate a class PCAP |

The CEH repo owns the detailed video record, current course route and practice bank. Planning carries locators and status. The existing 2026-10-18 class locator is a separate evidence thread; no private capture or Notion transcript is copied here.
''')
gloss=[
('Sniffing','Observing traffic available at a collection point.','SNIFF-ing'),
('Frame','Link-layer delivery unit.','frame'),('Packet','Network-layer data unit in this lesson.','PACK-et'),
('Promiscuous mode','Local acceptance of more delivered frames; no switch-wide visibility guarantee.','pro-MISS-kyoo-us'),
('SPAN','Configured copying of selected switch traffic.','span'),
('TAP','Link observation device with design-specific requirements.','tap'),
('Capture filter','A libpcap-language admission or offline packet selector.','CAP-ture FIL-ter'),
('Display filter','Selection among retained packets using analyzer fields.','dis-PLAY FIL-ter'),
('ARP','Local IPv4-to-hardware address resolution.','A R P'),
('MITM','A middle position requiring actual delivery and forwarding for the claimed path.','man in the middle'),
('DAI','Inspection of ARP claims against trusted bindings and policy.','D A I'),
('DHCP','Protocol for obtaining leased network configuration.','D H C P'),
('DORA','Common discover, offer, request, acknowledgment teaching sequence.','DOOR-uh'),
('VLAN','Logical Layer Two broadcast domain.','V lan'),
('STP','Protocol family that constructs a loop-free forwarding topology.','S T P'),
('BPDU','Spanning-tree control information.','B P D U'),
('DNSSEC','Validation of supported signed DNS data; no query encryption.','D N S sec'),
('TLS','Protected authenticated channel protocol.','T L S'),
('Offloading','Network work delegated to hardware or another processing layer.','OFF-load-ing'),
('PCAP','Capture-file format family; these fixtures use classic Ethernet PCAP.','P cap')]
write('GLOSSARY_en-US.md','# Glossary and pronunciation\n\n| Term | Meaning | Spoken guide |\n| --- | --- | --- |\n'+'\n'.join(f'| {t} | {d} | {p} |' for t,d,p in gloss)+'\n\nPreserve canonical text; log any synthesis-only pronunciation changes in later production.\n')
write('tooling/README.md','''# Reproduce the source package

Use Python 3.10+ with the versions in requirements-source.txt, Node 22+, Puppeteer/Chromium, LibreOffice, Poppler and tcpdump. The tested tool paths and versions are recorded under validation. No TTS model or paid provider is needed for this source layer.

Run build_props.py, build_source.py, build_packets.py, build_companions.py, write_docs.py and write_references.py in that order. Run verify_packets.py --record. The authored scene/question files are source inputs; shared locked artwork and the copied standard are preserved inputs.

Export the editable 18-slide deck using LibreOffice to a separate output directory, then rasterize its PDF with pdftoppm into previews/slides. Set CHROMIUM_PATH to an existing Chromium and PYTHON_PATH to a Python containing Pillow. Run browser_qa.cjs, then contact_sheets.py. Inspect all boards, deck pages and motion references; record actual findings and corrections. Use HYPERFRAMES_BROWSER_PATH for HyperFrames checks on each example. The four examples use a finite paused GSAP timeline with explicit absolute states, measured SVG path draws and local assets.

Run validate_pack.py after the actual browser checks and visual review. Run build_release.py with the intended output directory only after all source checks pass. Rebuilding invalidates earlier QA and sealed manifests until they are checked again. FILES_SHA256.txt and PACK_MANIFEST.json exclude themselves from payload hashing; the external release receipt measures the closed ZIP.

Commands emit bounded plain progress on stderr and JSON on stdout. A nonzero failure retains diagnostics; do not treat a partial stage as source-ready. The offline packet verifier does not write state without --record. It performs no live capture or traffic transmission. Wireshark display expressions remain documentation-reviewed, not run by tcpdump.

The four working examples demonstrate implementation references, not full-film production. Native PPTX text/shapes are structurally checked and exported by LibreOffice; Microsoft PowerPoint application editing is not claimed.
''')
write('ANIMATION_LAYER_CONTRACT.md','''# Animation layer contract

The 58 SVGs express editable design intent. Preserve source text and semantic geometry in full production. For each scene, establish the observation point, reveal named objects, connect the mechanism, identify the evidence limit and hold for reading. Use the original Tally artwork, approved palette and caption safe region.

The four examples implement finite seek-safe states using the HyperFrames composition contract, GSAP explicit from/to states and measured svg-path-draw connectors. The quiz uses absolute boundary states. All assets are local. Video/animation rate remains 1.0. Final timing comes from measured once-processed narration, with reading/motion time outside each exact 1.000-second quiz interval.

Runtime QA for four examples does not establish runtime readiness of all 58 final scenes. AGENT_PROMPT.md governs full production without a short-pilot approval gate.
''')
print(json.dumps({'stage':'references_built','primary_sources':len(refs),'topic_areas':len(coverage)}))

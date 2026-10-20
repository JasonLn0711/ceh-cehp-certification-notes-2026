"""Source-bound, coordinate-free M10 S01–S22 editorial scene specifications.

``cue`` indexes canonical on_screen_copy, not sorted label-cue records. Resolve
against each record's labels; combined/reordered narration anchors are valid.
Queue counts marked illustrative retain the original drawing's abstractions.
"""


def node(id, label, cue, kind='card', **details):
    return dict(id=id, label=label, cue=cue, kind=kind, **details)


def edge(source, target, cue, dashed=False):
    return {'from': source, 'to': target, 'cue': cue, 'dashed': dashed}


def spec(line, template, nodes, edges, note, rationale):
    return dict(template=template, nodes=nodes, edges=edges, note=note,
                provenance=f'scripts/scene_art_start.py:{line}; {rationale}')


SCENES = {
    'S01': spec(132, 'flow', [
        node('student', 'Northstar: authorized student', 0, 'device'),
        node('learning', 'Learning access', 1, 'device'),
        node('enrollment', 'Enrollment', 2, 'device'),
        node('availability', 'Availability', 3),
    ], [edge('student', 'learning', 1), edge('learning', 'enrollment', 2)],
        'Protect the completed task; all campus incidents are simulated',
        'Retain authorized user, two useful tasks, and availability framing.'),
    'S02': spec(146, 'flow', [
        node('dns', 'Name lookup', 0, 'device'),
        node('network', 'Network path', 1, 'device'),
        node('connection', 'Connection', 2, 'device'),
        node('application', 'Application', 3, 'device'),
    ], [edge('dns', 'network', 1), edge('network', 'connection', 2),
        edge('connection', 'application', 3)],
        'A failure at any dependency can interrupt the useful task',
        'Keep the ordered dependency chain.'),
    'S03': spec(167, 'evidence', [
        node('success', 'Success: completed task / attempted checks', 0),
        node('delay', 'Delay: start → useful result', 1),
        node('errors', 'Errors: record the failed stage', 2, 'document'),
        node('window', 'Time window: aligned observations', 3),
    ], [], 'Keep the task, denominator, timing basis and observation interval',
        'Separate the four observation dimensions without causal arrows.'),
    'S04': spec(183, 'scope', [
        node('scope', 'Written scope: owner + systems; permitted action; contact', 0, 'document'),
        node('files', 'Offline evidence: local files', 1, 'document'),
        node('analysis', 'Offline evidence: local analysis', 1, 'document'),
        node('stop', 'Stop conditions', 2),
        node('custody', 'Evidence custody', 3, 'document'),
    ], [edge('files', 'analysis', 1)],
        'Read and analyze local fixtures; no network traffic or capture replay',
        'Preserve written authority and local-only evidence relationship.'),
    'S05': spec(198, 'resource', [
        node('resource', 'Resource: illustrative 6 / 8 occupied slots', 0, 'queue', value=6, maximum=8, cells=8),
        node('demand', 'Demand', 1), node('evidence', 'Evidence', 2, 'document'),
        node('control', 'Control', 3),
    ], [edge('demand', 'resource', 1), edge('resource', 'evidence', 2),
        edge('evidence', 'control', 3), edge('control', 'resource', 3, True)],
        'Ask whether the proposed control can spare the constrained resource',
        'Preserve demand-to-resource and evidence-to-control feedback loop.'),
    'S06': spec(213, 'evidence', [
        node('failure', 'Service failure: task → symptom', 0, 'device'),
        node('pressure', 'Resource pressure: illustrative 8 / 8 slots', 1, 'queue', value=8, maximum=8, cells=8),
        node('mechanism', 'Mechanism', 2), node('intent', 'Intent: separate evidence', 3, 'document'),
    ], [edge('failure', 'pressure', 1, True), edge('pressure', 'mechanism', 2, True),
        edge('mechanism', 'intent', 3, True)],
        'Protect users while the cause and attribution are investigated',
        'Dashed investigative relationships retain uncertainty about cause and intent.'),
    'S07': spec(228, 'comparison', [
        node('bits', 'Bits per second: IP octets × 8 / seconds', 0),
        node('packets', 'Packets per second: packets / seconds', 1),
        node('requests', 'Requests per second: application requests / seconds', 2),
        node('window', 'Same window', 3),
    ], [], 'Match time, observation point and counted layer before comparing rates',
        'Keep distinct numerator units and a shared observation window.'),
    'S08': spec(245, 'flow', [
        node('arrival', 'Arrival', 0),
        node('queue', 'Queue: illustrative 7 / 8 waiting slots', 2, 'queue', value=7, maximum=8, cells=8),
        node('capacity', 'Capacity: work desk', 1, 'device'),
        node('completion', 'Completion', 3),
    ], [edge('arrival', 'queue', 2), edge('queue', 'capacity', 2), edge('capacity', 'completion', 3)],
        'Persistent excess work must wait, be rejected or be dropped',
        'Represent finite waiting budget followed by a service desk and completed work.'),
    'S09': spec(264, 'comparison', [
        node('single', 'One source', 0, 'device'), node('single-server', 'Server', 0, 'device'),
        node('many', 'Many sources', 1, 'device'), node('many-server', 'Server', 1, 'device'),
        node('address', 'Observed address: 192.0.2.10', 2, 'document'),
        node('attribution', 'Attribution: unresolved', 3),
    ], [edge('single', 'single-server', 0), edge('many', 'many-server', 1)],
        'Distribution describes observed traffic; addresses do not identify people',
        'Compare traffic distributions without equating addresses to identities.'),
    'S10': spec(280, 'resource', [
        node('bandwidth', 'Bandwidth', 0), node('packets', 'Packet work', 1),
        node('state', 'Connection state: illustrative 4 / 6 slots', 2, 'queue', value=4, maximum=6, cells=6),
        node('application', 'Application work', 3, 'device'),
    ], [edge('bandwidth', 'packets', 1), edge('packets', 'state', 2), edge('state', 'application', 3)],
        'Packet names alone do not identify the resource being exhausted',
        'Preserve one path with several distinct finite resources.'),
    'S11': spec(302, 'comparison', [
        node('baseline', 'Baseline: 50 Mbps', 0, 'bar', value=50, maximum=2400),
        node('enrollment', 'Enrollment: 150 Mbps', 1, 'bar', value=150, maximum=2400),
        node('offered', 'Offered load: 2400 Mbps', 2, 'bar', value=2400, maximum=2400),
        node('accepted', 'Accepted load: 200 Mbps', 3, 'bar', value=200, maximum=2400),
    ], [], 'Same 60-second IP-octet windows · discarded equivalent: 2200 Mbps',
        'All four bars retain the common 0–2400 Mbps scale; WAN ingress capacity is 200 Mbps.'),
    'S12': spec(317, 'flow', [
        node('provider', 'Provider view: 2400 Mbps offered', 0),
        node('ingress', 'Ingress limit: 200 Mbps', 1),
        node('discarded', 'Discarded traffic: 2200 Mbps', 2),
        node('server', 'Server view: CPU 25%; user success 20 / 100', 3, 'device'),
    ], [edge('provider', 'ingress', 1), edge('ingress', 'server', 3), edge('ingress', 'discarded', 2)],
        'A downstream processor can be lightly loaded behind a constrained path',
        'Branch discarded traffic at the constrained ingress; preserve all measured values.'),
    'S13': spec(336, 'comparison', [
        node('size', 'Packet size: equal illustrative data volume', 0),
        node('rate', 'Packet rate', 1),
        node('cost', 'Processing cost: illustrative 6 / 8 slots', 2, 'queue', value=6, maximum=8, cells=8),
        node('limit', 'Measured limit: device + configuration + traffic', 3),
    ], [], 'Illustration, not a measured router result · check packets and bytes',
        'Keep packet-size/rate comparison separate from actual device-limit measurement.'),
    'S14': spec(352, 'flow', [
        node('direct', 'Direct traffic', 0, 'device'),
        node('coordinated', 'Coordinated devices', 1, 'device'),
        node('bottleneck', 'Shared bottleneck', 2),
        node('server', 'Server', 2, 'device'),
        node('uncertainty', 'Source uncertainty', 3),
    ], [edge('direct', 'bottleneck', 2), edge('coordinated', 'bottleneck', 2), edge('bottleneck', 'server', 2)],
        'Architecture illustration · the fixture does not establish a botnet',
        'Both source patterns converge on the same bottleneck, without asserting attribution.'),
    'S15': spec(369, 'evidence', [
        node('packets', 'Packet analyzer', 0, 'document'), node('flows', 'Flow records', 1, 'document'),
        node('counters', 'Interface counters', 2, 'document'), node('checks', 'Service checks', 3, 'document'),
    ], [], 'Local evidence views have different coverage, sampling and timing limits',
        'Compare complementary evidence views without inventing causal relationships.'),
    'S16': spec(386, 'flow', [
        node('upstream', 'Upstream filter', 1), node('link', 'Protected link: 200 Mbps capacity', 2),
        node('campus', 'Campus filter', 0), node('server', 'User outcome', 3, 'device'),
    ], [edge('upstream', 'link', 2), edge('link', 'campus', 2), edge('campus', 'server', 3)],
        'Proposed placement · recovery rows are simulated, not deployment proof',
        'Retain upstream-before-link and campus-after-link placement.'),
    'S17': spec(404, 'timeline', [
        node('syn', 'Client → server: synchronize (SYN)', 0),
        node('pending', 'Server → client: SYN + ACK; pending state', 2),
        node('ack', 'Client → server: acknowledge (ACK)', 1),
        node('established', 'Established', 3),
    ], [edge('syn', 'pending', 0), edge('pending', 'ack', 1), edge('ack', 'established', 3)],
        'Sequence coordination does not authenticate the person or later request',
        'Ordered message timeline preserves direction and pending-to-established transition.'),
    'S18': spec(422, 'resource', [
        node('occupancy', 'Half-open entries: reported occupancy 1024', 0),
        node('backlog', 'Backlog: 16 tiles × 64 entries = 1024', 1, 'queue', value=1024, maximum=1024, cells=16),
        node('attempts', 'New attempts: 6000', 2),
        node('completed', 'Completed handshakes: 60', 3),
    ], [], 'Same 60-second fixture · unique attempts exclude retransmissions',
        'Keep occupancy and attempt/completion observations distinct; each tile denotes 64 entries.'),
    'S19': spec(439, 'comparison', [
        node('link', 'Link load: 30 / 200 Mbps', 0, 'bar', value=30, maximum=200),
        node('state', 'State pressure: 1024 / 1024 pending', 1, 'bar', value=1024, maximum=1024),
        node('success', 'Client success: 5 / 100 checks', 2, 'bar', value=5, maximum=100),
        node('alternatives', 'Alternative causes: loss · routing · legitimate demand', 3),
    ], [], 'State pressure is supported; intent and source identity remain open',
        'Compare utilization in explicitly different resource units.'),
    'S20': spec(453, 'comparison', [
        node('backlog', 'Larger backlog: illustrative 5 / 10 slots', 0, 'queue', value=5, maximum=10, cells=10),
        node('timeout', 'Shorter timeout: shorter retention', 1),
        node('state', 'Smaller state: compact pending records', 2),
        node('tradeoff', 'Client tradeoff', 3),
    ], [], 'Proposed mechanisms need client, resource and failure-behavior validation',
        'Compare capacity, retention, and record-size mechanisms without claiming measured improvement.'),
    'S21': spec(470, 'timeline', [
        node('cookie', 'Server → client: cookie response', 0),
        node('sequence', 'Encoded sequence value', 0),
        node('ack', 'Client → server: return acknowledgment', 1),
        node('state', 'State allocation: illustrative 3 / 5 slots', 2, 'queue', value=3, maximum=5, cells=5),
        node('limits', 'Remaining limits: bandwidth · packets · app work', 3),
    ], [edge('cookie', 'sequence', 0), edge('sequence', 'ack', 1), edge('ack', 'state', 2)],
        'Proposed defense for incomplete handshakes; useful clients need validation',
        'Preserve reply-before-allocation ordering and limits outside handshake state.'),
    'S22': spec(488, 'flow', [
        node('client', 'Client', 0, 'device'), node('proxy', 'Screening proxy', 0),
        node('server', 'Protected server', 1, 'device'),
        node('budget', 'New bottleneck: illustrative 5 / 8 state slots', 2, 'queue', value=5, maximum=8, cells=8),
        node('validation', 'Separate validation: clients · capacity · failure path', 3),
    ], [edge('client', 'proxy', 0), edge('proxy', 'server', 1)],
        'Proxy and cookies are candidates; supplied recovery rows are simulated',
        'Keep screening before protected server and expose the proxy state budget.'),
}

# Device identity is source-bound; labels containing “user” must never change a
# server into a laptop. Abstract/person figures use cards when no locked matching
# asset exists. None of these choices changes narration, quantities or cue timing.
_DEVICE_ASSETS = {
    'S01': {'learning': ('school_laptop', 134), 'enrollment': ('school_laptop', 136)},
    'S02': {'dns': ('office_server', 151), 'network': ('edge_router', 153),
            'application': ('office_server', 151)},
    'S06': {'failure': ('school_laptop', 214)},
    'S09': {'single': ('school_laptop', 266), 'single-server': ('office_server', 267),
            'many': ('school_laptop', 271), 'many-server': ('office_server', 273)},
    'S10': {'application': ('office_server', 293)},
    'S12': {'server': ('office_server', 326)},
    'S14': {'direct': ('school_laptop', 354), 'coordinated': ('school_laptop', 358),
            'server': ('office_server', 363)},
    'S16': {'server': ('office_server', 388)},
    'S22': {'client': ('school_laptop', 489), 'server': ('office_server', 491)},
}
_NON_DEVICE_FIGURES = {
    ('S01', 'student'): 'scripts/scene_art_start.py:133; authorized person, not a campus building or hardware identity',
    ('S02', 'connection'): 'scripts/scene_art_start.py:157; bidirectional exchange, not a separate server',
    ('S08', 'capacity'): 'scripts/scene_art_start.py:254; abstract finite work desk, not an observed server',
}
# Distinct semantic relationships must retain separate ports and visible paths.
# Final-state review found merged/reversed segments in these five diagrams.
_INDEPENDENT_PORTS = {
    'S05': [('left', .5, 'right', .5), ('bottom', .5, 'top', .5),
            ('right', .5, 'left', .5), ('left', .25, 'right', .75)],
    'S06': [('right', .5, 'left', .5), ('left', .75, 'right', .25),
            ('right', .5, 'left', .5)],
    'S10': [('right', .5, 'left', .5), ('left', .75, 'right', .25),
            ('right', .5, 'left', .5)],
    'S12': [('right', .5, 'left', .5), ('left', .75, 'right', .25),
            ('bottom', .5, 'top', .5)],
    'S14': [('right', .75, 'left', .75), ('right', .5, 'left', .5),
            ('bottom', .5, 'top', .5)],
}
for _scene_id, _ports in _INDEPENDENT_PORTS.items():
    for _edge_spec, (_from_side, _from_fraction, _to_side, _to_fraction) in zip(
            SCENES[_scene_id]['edges'], _ports, strict=True):
        _edge_spec['routingVariant'] = 'independent-ports'
        _edge_spec['fromPort'] = {'side': _from_side, 'fraction': _from_fraction}
        _edge_spec['toPort'] = {'side': _to_side, 'fraction': _to_fraction}

for _scene, _spec in SCENES.items():
    for _node in _spec.get('nodes', []):
        if (_scene, _node['id']) in _NON_DEVICE_FIGURES:
            _node['kind'] = 'card'
            _node['assetProvenance'] = _NON_DEVICE_FIGURES[(_scene, _node['id'])]
        elif _node['kind'] == 'device':
            _asset, _line = _DEVICE_ASSETS[_scene][_node['id']]
            _node['asset'] = _asset
            _node['assetProvenance'] = f'scripts/scene_art_start.py:{_line}; locked icon represents the original labeled role; not evidence of a physical device model'

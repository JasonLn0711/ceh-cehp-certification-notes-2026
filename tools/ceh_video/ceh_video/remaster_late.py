"""Constraint-ready M10 figures, transcribed from approved scene artwork.

Cue indexes refer to canonical on_screen_copy, not grouped label-cues records.
Labels and numbers retain the original evidence; the renderer owns coordinates.
"""


def node(ident, label, cue=0, kind='card', **kwargs):
    return dict(id=ident, label=label, cue=cue, kind=kind, **kwargs)


def edge(source, target, cue=0, **kwargs):
    return dict({'from': source, 'to': target, 'cue': cue}, **kwargs)


def figure(template, nodes, edges=(), note=None):
    result = dict(template=template, nodes=nodes, edges=list(edges))
    if note:
        result['note'] = note
    return result


SCENES = {
    'S23': figure('reflection', [
        node('sender', 'Actual sender', 0, 'device'),
        node('claimed-return-address', 'Return address: victim', 2),
        node('service', 'Answering service', 1, 'device'),
        node('victim', 'Northstar victim', 3, 'device'),
    ], [edge('sender', 'service', 1), edge('claimed-return-address', 'service', 2, dashed=True),
        edge('service', 'victim', 3)],
        'Constructed source field; human identity remains unknown.'),
    'S24': figure('comparison', [
        node('request', 'Request: 60 bytes', 1, 'bar', value=60, maximum=3000),
        node('response', 'Response: 3000 bytes', 1, 'bar', value=3000, maximum=3000),
        node('ratio', '3000 / 60 = 50x', 2, 'metric'),
        node('basis', 'Same measurement layer', 3),
    ], note='The ratio describes this exchange; a traffic rate also needs time.'),
    'S25': dict(template='matrix', headers=['Measurement', 'Request', 'Response', 'Ratio'], rows=[
        ['IP packet', '60 B', '3000 B', '50x'],
        ['Ethernet frame', '74 B', '3014 B', '40.7x']],
        note='Frame lengths exclude other possible physical-link overhead.'),
    'S26': figure('flow', [
        node('role', 'Name service role', 0), node('recursive', 'Recursive lookup', 0),
        node('audience', 'Intended audience', 1), node('authoritative', 'Published zone records', 2),
        node('separate', 'Authoritative role', 2),
    ], [edge('role', 'recursive'), edge('recursive', 'audience', 1),
        edge('role', 'authoritative', 2), edge('authoritative', 'separate', 2)],
        'Review service roles; no external resolver queries are sent.'),
    'S27': figure('flow', [
        node('origin', 'Origin network', 0, 'device'),
        node('boundary', 'Source validation boundary', 1),
        node('others', 'Other networks', 1, 'device'),
        node('outside', 'Outside allowed range', 2),
        node('allowed', 'Allowed prefix', 0),
    ], [edge('origin', 'allowed'), edge('allowed', 'boundary', 1),
        edge('boundary', 'others', 1), edge('outside', 'boundary', 2, dashed=True)],
        'Allowed ranges can still contain harmful traffic.'),
    'S28': figure('evidence', [
        node('origin', 'Origin network\nValidate sources', 0),
        node('reflector', 'Reflector owner\nLimit recursive use', 1),
        node('provider', 'Victim provider\nAct before campus link', 2),
    ], note='Each owner acts at a different part of the reflection path.'),
    'S29': figure('resource', [
        node('ordinary', '100/s x 0.020 s = 2 core-seconds/s', 1, 'bar', value=2, maximum=24),
        node('budget', '8-core limit', 2, 'bar', value=8, maximum=24),
        node('incident', '120/s x 0.200 s = 24 core-seconds/s', 3, 'bar', value=24, maximum=24),
    ], note='24 core-seconds/s of offered work exceeds an 8-core budget.'),
    'S30': figure('evidence', [
        node('count', '300 requests each second', 0, 'metric'),
        node('work', '300 x 0.005 = 1.5 core-seconds/s', 1, 'metric'),
        node('latency', 'Check latency', 2), node('success', 'Check task success', 3),
    ], note='Separate scales: count and CPU demand are different quantities.'),
    'S31': figure('timeline', [
        node('connection', 'Connection held', 0), node('slots', 'Finite service slots', 1),
        node('progress', 'Progress checkpoint', 2), node('useful', 'Useful progress', 3),
        node('waiting', 'No progress', 1),
    ], [edge('connection', 'slots', 1), edge('slots', 'progress', 2),
        edge('progress', 'useful', 3), edge('waiting', 'progress', 2, dashed=True)],
        'Deadlines must preserve legitimate slow-client operations.'),
    'S32': figure('resource', [
        node('app', 'Application work', 0),
        node('pool', 'Dependency pool: 32 slots', 1, 'queue', value=32, maximum=32, cells=32),
        node('queue', 'Queue: 400 waiting', 2, 'metric'), node('limit', 'Limit admission', 3),
    ], [edge('app', 'pool'), edge('queue', 'pool', 2), edge('limit', 'app', 3)],
        'Occupancy is known; why the operations are slow remains open.'),
    'S33': figure('timeline', [
        node('connection', 'One connection', 0), node('streams', 'Parallel streams', 0),
        node('cancel', 'Early cancellation', 1), node('work', 'Work already started', 2),
        node('policy', 'Assess behavior across time', 3),
    ], [edge('connection', 'streams'), edge('streams', 'cancel', 1),
        edge('cancel', 'work', 2), edge('work', 'policy', 3)],
        'Concept only. Cancellation can be legitimate; no traffic replay.'),
    'S34': figure('comparison', [
        node('ordinary', 'Ordinary: 50 Mbps', 0, 'bar', value=50, maximum=200),
        node('enrollment', 'Enrollment: 150 Mbps', 1, 'bar', value=150, maximum=200),
        node('capacity', '200 Mbps capacity', 2, 'bar', value=200, maximum=200),
        node('window', 'Aligned 60-second windows', 0),
    ], note='Expected demand needs service outcomes as well as rate.'),
    'S35': figure('evidence', [
        node('provider', 'Provider: offered\n2400 Mbps', 0, 'metric'),
        node('campus', 'Campus: accepted\n200 Mbps', 1, 'metric'),
        node('outcome', 'Service outcome\n20 / 100 succeed', 2, 'metric'),
        node('discarded', '2200 Mbps discarded; CPU 25%', 2, 'metric'),
    ], note='These are different observation points in the same 60-second window.'),
    'S36': figure('evidence', [
        node('alert', 'Rate alert', 0), node('signals', 'Impact + resource signals', 1),
        node('alternatives', 'Enrollment, retries, defects', 2),
    ], [edge('alert', 'signals', 1), edge('alert', 'alternatives', 2, dashed=True)],
        'Bound the claim: impact, mechanism, and attribution are distinct.'),
    'S37': figure('evidence', [
        node('packet', 'Stored packet\nFields + lengths', 0, 'document'),
        node('flow', 'Flow records\nGrouped counters', 1, 'document'),
        node('host', 'Host snapshot\nFinite resources', 2, 'document'),
    ], note='Limits: truncation, sampling, byte definitions, and snapshot timing.'),
    'S38': figure('flow', [
        node('source', 'Original source', 0, 'document'),
        node('units', 'Units + arithmetic', 1), node('finding', 'Bounded finding', 2),
        node('next', 'Next check answers the unresolved decision', 3),
    ], [edge('source', 'units', 1), edge('units', 'finding', 2), edge('finding', 'next', 3)],
        'A hash detects byte changes; it does not certify the observation.'),
    'S39': dict(template='matrix', headers=['Constrained resource', 'Control placement'], rows=[
        ['Constrained link', 'Upstream assistance'],
        ['Handshake slots', 'Protocol-specific defense'],
        ['Expensive requests', 'Application work budget']],
        note='Protect the constrained resource and verify the learner task.'),
    'S40': figure('flow', [
        node('gate', 'Admission gate', 0), node('reuse', 'Reusable result', 1),
        node('deadline', 'Work deadline', 2),
        node('budgets', 'Separate critical budgets', 3), node('service', 'Useful service', 3),
    ], [edge('gate', 'reuse', 1), edge('reuse', 'deadline', 2),
        edge('deadline', 'budgets', 3), edge('budgets', 'service', 3)],
        'Proposed controls need authorized changes and real validation.'),
    'S41': figure('comparison', [
        node('proposal', 'Proposed change\nThreshold + expected effect', 1),
        node('observation', 'Real observation\nUser success + rejection', 2),
        node('rollback', 'Revise or reverse when criteria are met', 3),
    ], [edge('proposal', 'observation', 1, dashed=True), edge('observation', 'rollback', 3)],
        'Generated post-control rows are calculation examples, not deployment proof.'),
    'S42': figure('flow', [
        node('impact', 'Impact + evidence', 0, 'document'),
        node('owner', 'Owner + request', 1, 'document'),
        node('change', 'Authorized change', 2, 'document'),
        node('recovery', 'Resource health + learner task', 3),
    ], [edge('impact', 'owner', 1), edge('owner', 'change', 2), edge('change', 'recovery', 3)],
        'Offline handoff draft only; no provider contact or live changes.'),
    'S43': figure('resource', [
        node('offered', 'Offered: 2,400 Mbps', 0, 'bar', value=2400, maximum=2400),
        node('accepted', 'Accepted: 200 Mbps', 1, 'bar', value=200, maximum=2400),
        node('limit', 'WAN limit 200 Mbps\nDiscarded 2,200 Mbps', 1),
        node('outcome', 'User checks: 20 / 100\nServer CPU: 25%', 2),
    ], [edge('offered', 'accepted', 1)],
        'Place upstream protection before the constrained access link'),
    'S44': figure('resource', [
        node('attempts', '6,000 unique attempts', 0, 'metric'),
        node('backlog', 'Backlog 1,024 / 1,024', 1, 'queue', value=1024, maximum=1024, cells=16),
        node('scale', '16 cells × 64 entries = 1,024', 1),
        node('completed', 'Only 60 completed', 2, 'metric'),
        node('outcome', 'Client success 5 / 100\nLink traffic 30 Mbps', 2),
    ], [edge('attempts', 'completed', 2)],
        'A control trial needs measured legitimate and unwanted outcomes'),
    'S45': figure('comparison', [
        node('request', 'Request\n60 IP bytes', 0, 'bar', value=60, maximum=3000),
        node('response', 'Response\n3,000 IP bytes', 1, 'bar', value=3000, maximum=3000),
        node('ip', '3,000 ÷ 60 = 50× at IP', 2, 'metric'),
        node('ethernet', '3,014 ÷ 74 ≈ 40.7× at Ethernet', 2, 'metric'),
    ], [edge('request', 'response', 1)],
        'Source validation, reflector policy and victim protection have different owners'),
    'S46': figure('resource', [
        node('work', 'Offered CPU work: 24 cores', 1, 'bar', value=24, maximum=24),
        node('budget', 'CPU budget: 8 cores', 1, 'bar', value=8, maximum=24),
        node('calculation', '120 requests/sec × 0.2 sec\n= 24 core-seconds/sec', 0, 'metric'),
        node('pool', 'Dependency: 32 / 32 busy', 2, 'queue', value=32, maximum=32, cells=32),
        node('queue', 'Queue: 400 requests', 2, 'metric'),
    ], note='Toy demand accounting; proposed limits need a separate service test'),
    'S47': figure('timeline', [
        node('impact', 'Name user impact', 0, asset='school_building'),
        node('evidence', 'Preserve aligned evidence', 1, asset='evidence_slip'),
        node('owner', 'Select control owner', 2, asset='scope_sheet'),
        node('decision', 'Record decision + rollback', 3, asset='report_file'),
    ], [edge('impact', 'evidence', 1), edge('evidence', 'owner', 2), edge('owner', 'decision', 3)],
        'Restore legitimate service while keeping observations and decisions traceable'),
    'S48': figure('evidence', [
        node('user', 'Legitimate user path\nLookup → connect → complete', 0),
        node('resource', 'Resource path\nLink · state · work · dependency', 1),
        node('repeat', 'Repeat across an agreed window\nCheck false rejection', 2),
        node('owner', 'Owner + monitoring + follow-up\nPreserve original evidence', 3),
    ], [edge('user', 'resource', 1)],
        'One quiet interval or one successful request does not establish stable recovery'),
    'S49': figure('flow', [
        node('allowed', 'Allowed, minimized evidence', 0, 'document'),
        node('draft', 'AI draft: claim → record → uncertainty', 1),
        node('review', 'Human review + independent calculation + decision owner', 2),
    ], [edge('allowed', 'draft', 1), edge('draft', 'review', 2)],
        'Treat log text as untrusted data; keep change authority with the named owner'),
    'S58': dict(template='matrix', headers=['Case', 'Resource / evidence', 'Control + acceptance'], rows=[
        ['E01', 'Provider + WAN IP octets', 'Upstream + user continuity'],
        ['E02', 'Half-open state / completions', 'State control + legitimate flow'],
        ['E03', 'Paired packet layer / bytes', 'Owner-specific validation'],
        ['E04', 'Request work + dependency', 'Bounded work + service outcome']],
        note='Submit your own evidence, resource explanation, control plan and acceptance check'),
}

# Source identities refer to the frozen approved project scripts. These references
# document semantic provenance; the production manifest records their file hashes.
_SOURCE_LINES = {'S23': 72, 'S24': 85, 'S25': 98, 'S26': 108, 'S27': 120, 'S28': 132, 'S29': 143, 'S30': 155, 'S31': 168, 'S32': 181, 'S33': 192, 'S34': 206, 'S35': 218, 'S36': 230, 'S37': 240, 'S38': 249, 'S39': 259, 'S40': 269, 'S41': 281, 'S42': 291, 'S43': 11, 'S44': 20, 'S45': 31, 'S46': 38, 'S47': 46, 'S48': 49, 'S49': 56, 'S58': 62}
for _sid, _spec in SCENES.items():
    _source = 'scene_art_mid.py' if int(_sid[1:]) <= 42 else 'scene_art_end.py'
    _spec['provenance'] = {
        'source': f'scripts/{_source}:{_SOURCE_LINES[_sid]}',
        'design_reason': 'Preserve approved mechanism and evidence with measured components and computed connection ports.',
    }

# Explicit role-to-asset mapping prevents incidental words in labels from
# selecting hardware identities. These are explanatory icons, not measured
# device-model assertions; source diagrams establish the named roles.
_DEVICE_ASSETS = {
    'S23': {
        'sender': ('school_laptop', 'scripts/scene_art_mid.py:73; Actual sender'),
        'service': ('office_server', 'scripts/scene_art_mid.py:74; Answering service'),
        'victim': ('school_building', 'scripts/scene_art_mid.py:75; Northstar victim'),
    },
    'S27': {
        'origin': ('edge_router', 'scripts/scene_art_mid.py:121; Origin network'),
        'others': ('edge_router', 'scripts/scene_art_mid.py:122; Other networks'),
    },
}
for _scene, _spec in SCENES.items():
    for _node in _spec.get('nodes', []):
        if _node['kind'] == 'device':
            _asset, _reference = _DEVICE_ASSETS[_scene][_node['id']]
            _node['asset'] = _asset
            _node['assetProvenance'] = _reference + '; locked icon represents the labeled role, not a physical device-model finding'

# The original S47 flow explicitly pairs these four labels with these assets.
for _node in SCENES['S47']['nodes']:
    _node['assetProvenance'] = (
        'scripts/scene_art_end.py:47; approved flow pairs '
        + _node['label'] + ' with ' + _node['asset'] + '.svg'
    )

# Distinct relationships receive independent ports and non-overlapping lanes.
for _sid in ('S23','S26','S27','S31','S32','S36'):
    for _edge in SCENES[_sid]['edges']:
        _edge['routingVariant'] = 'independent-ports'
# Original source validation diagram ends the forged path in an explicit cross.
SCENES['S27']['edges'][3]['terminal'] = 'blocked'
SCENES['S27']['edges'][3]['terminalProvenance'] = 'scripts/scene_art_mid.py:128; crossed terminal rejects outside allowed range'
# Align admission with the application and the waiting queue with its dependency.
# This semantic order yields independent vertical branches in the resource grid.
_s32_nodes = {n['id']: n for n in SCENES['S32']['nodes']}
SCENES['S32']['nodes'] = [_s32_nodes[k] for k in ('app', 'pool', 'limit', 'queue')]

# Fixed fractional ports remain stable throughout narration-bound entrance motion.
_EXPLICIT_PORTS = {'S23': [{'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.25},
          'toPort': {'side': 'left', 'fraction': 0.75}},
         {'fromPort': {'side': 'bottom', 'fraction': 0.5},
          'toPort': {'side': 'top', 'fraction': 0.5}}],
 'S26': [{'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.75},
          'toPort': {'side': 'left', 'fraction': 0.25}},
         {'fromPort': {'side': 'left', 'fraction': 0.5},
          'toPort': {'side': 'right', 'fraction': 0.5}}],
 'S27': [{'fromPort': {'side': 'right', 'fraction': 0.75},
          'toPort': {'side': 'left', 'fraction': 0.25}},
         {'fromPort': {'side': 'top', 'fraction': 0.5},
          'toPort': {'side': 'bottom', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'left', 'fraction': 0.25},
          'toPort': {'side': 'right', 'fraction': 0.75}}],
 'S31': [{'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'bottom', 'fraction': 0.5},
          'toPort': {'side': 'top', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.25},
          'toPort': {'side': 'left', 'fraction': 0.75}}],
 'S32': [{'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'top', 'fraction': 0.5},
          'toPort': {'side': 'bottom', 'fraction': 0.5}},
         {'fromPort': {'side': 'top', 'fraction': 0.5},
          'toPort': {'side': 'bottom', 'fraction': 0.5}}],
 'S36': [{'fromPort': {'side': 'right', 'fraction': 0.5},
          'toPort': {'side': 'left', 'fraction': 0.5}},
         {'fromPort': {'side': 'right', 'fraction': 0.25},
          'toPort': {'side': 'left', 'fraction': 0.25}}]}
for _sid, _ports in _EXPLICIT_PORTS.items():
    for _edge, _port_pair in zip(SCENES[_sid]["edges"], _ports):
        _edge.update(_port_pair)

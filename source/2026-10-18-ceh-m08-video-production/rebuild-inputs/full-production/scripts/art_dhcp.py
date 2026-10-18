"""DHCP teaching diagrams; mechanisms and supplied evidence keep separate states."""
from m08_art_common import *


def _dhcp_label(a, x, y, value, when, size=32, width=60, name=None,
                color=INK, anchor='middle'):
    g = a.add(text(x, y, value, size, width, anchor, color), name)
    a.show(g, when, dy=8)
    return g


def _dhcp_trace(a, d, when, name=None, color=INK, dashed=False, duration=1.1):
    g = a.add(path(d, color, '9 9' if dashed else ''), name)
    a.moves.append({'target': g, 'start': round(when, 6),
                    'duration': duration, 'draw': True, 'dashed': dashed})
    return g


def _dhcp_layers(a, first, last=None):
    return [re.match(r'<g id="([^"]+)"', p).group(1)
            for p in a.parts[first:last]]


def _dhcp_hide(a, layers, when):
    for g in layers:
        a.move(g, when, .45, opacity=0)


def _dhcp_prop(a, kind, x, y, w, when, name):
    g = a.prop(kind, x, y, w, name)
    a.show(g, when, dy=14)
    return g


def _dhcp_flow(a, x1, y1, x2, y2, when, label=None, dashed=False):
    # The compiler owns the deterministic paper-token motion on this path.
    n = len(a.parts)
    g = a.route(x1, y1, x2, y2, when, label=label, dashed=dashed)
    if x1 == x2:
        sign = 1 if y2 >= y1 else -1
        a.parts[n + 1] = re.sub(
            r'<path d="[^"]+"',
            f'<path d="M{x2-10} {y2-sign*16} L{x2} {y2} L{x2+10} {y2-sign*16}"',
            a.parts[n + 1], count=1)
    return g


def _dhcp_offer_case(a, when, missing_when):
    """E03 contains one Discover and two Offers, with no acceptance state."""
    heading = _dhcp_label(a, 805, 323, 'E03 · one constructed transaction',
                          when, name='case-heading')
    _dhcp_label(a, 395, 350, 'Authorized service', when, width=24,
                name='authorized-role')
    _dhcp_label(a, 1175, 350, 'Unexpected sender', when, width=24,
                name='unexpected-role')
    _dhcp_prop(a, 'edge_router', 330, 365, 130, when, 'case-authorized-service')
    _dhcp_prop(a, 'office_server', 1110, 365, 130, when, 'case-unexpected-server')
    _dhcp_prop(a, 'school_laptop', 720, 565, 170, when, 'case-client')
    _dhcp_label(a, 805, 725, 'Client', when, name='case-client-role')

    # A single broadcast stem branches toward the service candidates.
    _dhcp_label(a, 805, 389, 'Discover', when + .15,
                name='case-discover-label')
    _dhcp_flow(a, 805, 548, 805, 421, when + .15)
    _dhcp_trace(a, 'M805 421 H490 M805 421 H1080', when + 1.1,
                'case-discover-broadcast', GRAY, True)

    for x, router, offset, prefix in [
            (395, '10.44.10.1', 4, 'authorized'),
            (1175, '10.44.10.66', 5.5, 'unexpected')]:
        _dhcp_label(a, x, 508, 'Router option', when + offset,
                    size=30, name=prefix + '-router-role')
        _dhcp_label(a, x, 548, router, when + offset,
                    size=34, name=prefix + '-router-value')
    _dhcp_flow(a, 548, 558, 716, 620, when + 4)
    _dhcp_flow(a, 1052, 558, 894, 620, when + 5.5)
    _dhcp_label(a, 620, 540, 'Offer', when + 4, size=30,
                name='authorized-offer-label')
    _dhcp_label(a, 982, 540, 'Offer', when + 5.5, size=30,
                name='unexpected-offer-label')

    question = a.add(text(805, 639, '?', 52, 2), 'client-state-question')
    a.show(question, missing_when)
    a.move(question, missing_when + .8, .5, scale=1.08,
           svgOrigin='805 620')
    a.move(question, missing_when + 1.3, .5, scale=1,
           svgOrigin='805 620')
    _dhcp_trace(a, 'M295 753 H1315', missing_when,
                'case-evidence-rule', GRAY)
    missing = _dhcp_label(
        a, 805, 795, 'Request / ACK / client state: not supplied', missing_when,
        size=32, name='case-acceptance-limit')
    return heading, missing


def S30(a):
    t0, correlate, fixture, unknown = [at(a, i) for i in range(4)]
    first = len(a.parts)
    _dhcp_label(a, 790, 326, 'DORA · initial-exchange model', t0,
                size=32, name='dora-model-heading')
    _dhcp_label(a, 430, 347, 'Client', t0, name='dora-client-label')
    _dhcp_label(a, 1140, 347, 'DHCP service', t0, name='dora-service-label')
    _dhcp_prop(a, 'school_laptop', 380, 362, 100, t0, 'dora-client')
    _dhcp_prop(a, 'edge_router', 1083, 360, 115, t0, 'dora-gateway-role')
    _dhcp_trace(a, 'M430 445 V684 M1140 445 V684', t0,
                'dora-lifelines', GRAY, True)

    exchange = a.at('In a common initial exchange')
    for j, (label, y, forward) in enumerate([
            ('1  Discover', 475, True), ('2  Offer', 537, False),
            ('3  Request', 599, True), ('4  ACK', 661, False)]):
        beat = exchange + .2 + j * 1.55
        _dhcp_label(a, 785, y - 27, label, beat, size=32,
                    name='dora-message-' + str(j + 1))
        _dhcp_flow(a, 430 if forward else 1140, y,
                    1140 if forward else 430, y, beat)

    _dhcp_label(a, 790, 704, 'Match transaction ID · client · type · options',
                correlate, size=30, name='dora-correlation')
    options = a.at('A server identifier, router option, and DNS option')
    for x, title, value, key in [
            (210, 'Server identifier', 'Service identity', 'server-id'),
            (610, 'Router option', '10.44.10.1', 'router'),
            (1010, 'DNS option', '10.44.20.53', 'dns')]:
        card = a.add(rect(x, 726, 360, 80, WHITE, 3)
                     + text(x + 180, 756, title, 30, 24)
                     + text(x + 180, 793, value, 32, 24),
                     'option-' + key)
        a.show(card, options, dy=10)

    # The teaching exchange leaves before the retained fixture is introduced.
    _dhcp_hide(a, _dhcp_layers(a, first), fixture - .05)
    _, limit = _dhcp_offer_case(
        a, fixture, a.at('It does not include a completed request'))
    _dhcp_hide(a, [limit], unknown)
    _dhcp_label(a, 805, 795, 'Client acceptance remains unmeasured', unknown,
                size=34, name='acceptance-remains-open', color=ACCENT)


def S31(a):
    t0, pool_check, fixture, next_check = [at(a, i) for i in range(4)]
    first = len(a.parts)
    _dhcp_label(a, 495, 335, 'Starvation attempt', t0, size=36,
                name='starvation-heading')
    _dhcp_trace(a, 'M810 354 V730', t0, 'mechanism-divider', GRAY, True)

    # Discover tokens represent demand; the rack never drains or claims zero leases.
    for j, (x, y) in enumerate([(250, 407), (281, 445), (312, 483)]):
        token = a.add(
            f'<path d="M{x} {y} h98 v47 h-98 Z M{x} {y} l49 26 l49 -26" '
            f'fill="{SOFT}" stroke="{INK}" stroke-width="3"/>',
            'demand-token-' + str(j))
        a.show(token, t0 + j * .3, dx=-16)
        a.move(token, t0 + 1 + j * .3, 1.1, x=18)
    _dhcp_label(a, 345, 592, 'Discover demand', t0, size=32,
                width=23, name='demand-label')
    _dhcp_flow(a, 440, 481, 551, 481, t0 + .6)
    rack = rect(566, 409, 180, 142, WHITE, 10)
    for row in range(2):
        for col in range(3):
            rack += rect(580 + col * 53, 425 + row * 56, 43, 42, PAPER, 3)
    rack += (f'<circle cx="656" cy="480" r="34" fill="{WHITE}" '
             f'stroke="{INK}" stroke-width="3"/>'
             + text(656, 494, '?', 44, 2))
    pool = a.add(rack, 'unmeasured-lease-rack')
    a.show(pool, t0, dy=12)
    _dhcp_label(a, 656, 386, 'Lease pool', t0, name='lease-pool-label')
    _dhcp_label(a, 635, 592, 'State unmeasured', pool_check, size=30,
                name='pool-state-limit')
    _dhcp_label(a, 495, 676, 'Check leases, capacity and client results',
                pool_check, size=32, width=33, name='starvation-evidence')

    rogue = a.at('A rogue DHCP server supplies unauthorized configuration')
    _dhcp_label(a, 1110, 335, 'Rogue configuration', rogue, size=36,
                name='rogue-heading')
    _dhcp_prop(a, 'office_server', 875, 390, 130, rogue, 'rogue-service-model')
    _dhcp_prop(a, 'school_laptop', 1245, 390, 130, rogue, 'rogue-client-model')
    _dhcp_label(a, 940, 570, 'Server', rogue, name='rogue-server-label')
    _dhcp_label(a, 1310, 570, 'Client', rogue, name='rogue-client-label')
    _dhcp_label(a, 1125, 400, 'Offer', rogue + .35,
                name='rogue-offer-label')
    _dhcp_flow(a, 1023, 453, 1225, 453, rogue + .35)
    _dhcp_label(a, 1125, 514, 'Router / DNS', rogue + .35,
                size=30, name='proposed-settings')
    acceptance = a.at('Likewise, an unexpected offer does not prove')
    q = a.add(f'<circle cx="1310" cy="626" r="29" fill="{WHITE}" '
              f'stroke="{ACCENT}" stroke-width="4"/>'
              + text(1310, 640, '?', 40, 2), 'unmeasured-acceptance')
    a.show(q, acceptance)
    _dhcp_label(a, 1105, 680, 'Check selected exchange and client state',
                acceptance, size=32, width=29, name='rogue-evidence')

    _dhcp_hide(a, _dhcp_layers(a, first), fixture - .05)
    heading, limit = _dhcp_offer_case(a, fixture, fixture + .2)
    _dhcp_hide(a, [heading, limit], next_check)
    _dhcp_label(a, 805, 323, 'Check sending ports + authorized servers',
                next_check, name='check-offer-source')
    _dhcp_label(a, 805, 795, 'Verify selected exchange + client configuration',
                next_check, name='check-client-acceptance')


def S32(a):
    t0, dependencies, validate, preserve = [at(a, i) for i in range(4)]
    status = _dhcp_label(a, 805, 323, 'PROPOSED CONTROL · switch model', t0,
                         size=30, name='control-status')
    _dhcp_prop(a, 'edge_router', 230, 365, 145, t0, 'approved-server-path')
    _dhcp_prop(a, 'managed_switch', 700, 373, 210, t0, 'snooping-switch')
    _dhcp_prop(a, 'school_laptop', 1220, 378, 140, t0, 'snooping-client')
    _dhcp_label(a, 302, 351, 'Server / relay', t0, name='server-relay-role')
    _dhcp_label(a, 805, 351, 'Snooping switch', t0, name='snooping-role')
    _dhcp_label(a, 1290, 351, 'Client', t0, name='access-client-role')
    _dhcp_label(a, 545, 391, 'Trusted path', t0, name='trusted-path-label')
    _dhcp_label(a, 1075, 391, 'Untrusted access', t0,
                name='untrusted-access-label')
    _dhcp_trace(a, 'M405 446 H690 M925 446 H1205', t0,
                'switch-topology', GRAY)
    _dhcp_flow(a, 405, 446, 690, 446, t0 + .3)
    _dhcp_flow(a, 1205, 467, 925, 467, t0 + 1.25)
    _dhcp_label(a, 545, 510, 'Server replies', t0 + .3,
                size=30, name='trusted-server-message')
    _dhcp_label(a, 1075, 515, 'Client requests', t0 + 1.25,
                size=30, name='access-client-message')

    correct_trust = a.at('Correct trust placement helps prevent')
    unwanted_start = len(a.parts)
    _dhcp_label(a, 1240, 556, 'Unwanted OFFER', correct_trust,
                size=30, name='unwanted-offer-label')
    _dhcp_flow(a, 1330, 590, 1090, 590, correct_trust + .2)
    # This is the intended policy boundary, visibly inside the proposed model.
    gate = a.add(path('M1062 558 V620', ACCENT)
                 + f'<circle cx="1062" cy="590" r="17" fill="{PAPER}" '
                   f'stroke="{ACCENT}" stroke-width="4"/>'
                 + path('M1051 579 L1073 601', ACCENT),
                 'access-server-message-boundary')
    a.show(gate, correct_trust + .5)
    unwanted_layers = _dhcp_layers(a, unwanted_start)

    lower = len(a.parts)
    learned = a.at('The learned database can also support')
    _dhcp_trace(a, 'M805 510 V575', learned,
                'switch-to-bindings', ACCENT)
    sheet = rect(230, 584, 785, 138, WHITE, 3)
    sheet += text(622, 624, 'Binding schema · illustrative fields', 32, 48)
    sheet += path('M246 645 H999', GRAY)
    for j, label in enumerate(['MAC', 'IP', 'VLAN', 'Port', 'Lease']):
        xx = 246 + j * 151
        if j:
            sheet += path(f'M{xx-8} 654 V705', GRAY)
        sheet += text(xx + 67, 690, label, 30, 12)
    schema = a.add(sheet, 'binding-schema')
    a.show(schema, learned, dy=12)
    _dhcp_trace(a, 'M1015 666 H1100 V641 H1144 M1100 666 V711 H1144',
                learned + .3, 'binding-dependent-features', ACCENT)
    for cy, label in [(641, 'DAI'), (711, 'IP Source Guard')]:
        feature = a.add(
            f'<circle cx="1160" cy="{cy}" r="15" fill="{SOFT}" '
            f'stroke="{INK}" stroke-width="3"/>'
            + text(1190, cy + 11, label, 30, 24, 'start'),
            'dependent-' + ('dai' if cy == 641 else 'ipsg'))
        a.show(feature, learned + .3, dx=-10)
    _dhcp_label(a, 790, 777, 'Binding quality affects dependent controls',
                dependencies, name='binding-dependency-limit')
    rate = a.at('Rate limits may help constrain abuse')
    dial = a.add(f'<circle cx="260" cy="548" r="17" fill="{WHITE}" '
                 f'stroke="{INK}" stroke-width="3"/>'
                 + path('M260 548 L269 539', ACCENT), 'rate-policy-dial')
    a.show(dial, rate)
    _dhcp_label(a, 500, 558, 'Rate policy: platform-specific', rate,
                size=30, width=35, name='rate-policy-limit')

    _dhcp_hide(a, unwanted_layers, validate - .05)
    _dhcp_hide(a, _dhcp_layers(a, lower), validate - .05)
    _dhcp_label(a, 800, 588, 'Planned isolated-lab checks', validate,
                name='validation-plan-heading')
    for cy, key in [(646, 'lease'), (741, 'offer')]:
        result = a.add(f'<circle cx="250" cy="{cy}" r="15" fill="{PAPER}" '
                       f'stroke="{INK}" stroke-width="3"/>',
                       'pending-check-' + key)
        a.show(result, validate, dx=-8)
    _dhcp_label(a, 286, 654, 'Legitimate lease', validate,
                anchor='start', name='lease-validation-label')
    _dhcp_label(a, 980, 638, 'Router 10.44.10.1', validate,
                name='expected-client-router')
    _dhcp_label(a, 980, 680, 'DNS 10.44.20.53', validate,
                name='expected-client-dns')
    _dhcp_trace(a, 'M230 700 H1390', validate,
                'validation-separator', GRAY)
    _dhcp_label(a, 286, 750, 'Unauthorized teaching OFFER', validate,
                anchor='start', name='offer-validation-label')
    _dhcp_label(a, 1100, 750, 'Record handling', validate,
                name='offer-validation-evidence')
    _dhcp_label(a, 800, 802, 'Save bindings · counters · client configuration',
                preserve, name='preserve-control-evidence')
    final_limit = a.at('Our source cards describe the proposed controls')
    _dhcp_hide(a, [status], final_limit)
    _dhcp_label(a, 805, 323, 'Proposal only · switch export and live test pending',
                final_limit, size=30, name='control-evidence-limit')

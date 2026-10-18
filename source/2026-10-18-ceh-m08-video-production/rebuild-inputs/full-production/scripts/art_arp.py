"""Narration-paced ARP teaching diagrams; no live cache or path is inferred."""
from m08_art_common import *


def _arp_label(a, x, y, value, when, size=32, width=40, name=None,
               mono=False, color=INK, anchor='middle'):
    if mono:
        content = (f'<text x="{x}" y="{y}" font-family="Technical" '
                   f'font-size="{size}" fill="{color}" stroke="none" '
                   f'text-anchor="{anchor}">{esc(value)}</text>')
    else:
        content = text(x, y, value, size, width, anchor, color)
    ident = a.add(content, name)
    a.show(ident, when)
    return ident


def _arp_layer(a, content, when, name, dy=0):
    ident = a.add(content, name)
    a.show(ident, when, dy=dy)
    return ident


def _arp_line(a, d, when, name, color=INK, dashed=False, duration=1.0):
    ident = a.add(path(d, color, '10 10' if dashed else ''), name)
    a.moves.append({'target': ident, 'start': when, 'duration': duration,
                    'draw': True, 'dashed': dashed})
    return ident


def _arp_arrow(a, x1, y1, x2, y2, when, name, dashed=False, color=INK):
    middle = (x1 + x2) / 2
    line = _arp_line(a, f'M{x1} {y1} C{middle} {y1} {middle} {y2} {x2} {y2}',
                     when, name + '-line', color, dashed)
    direction = 1 if x2 >= x1 else -1
    head = _arp_layer(a, path(f'M{x2-direction*14} {y2-9} L{x2} {y2} '
                              f'L{x2-direction*14} {y2+9}', color),
                      when + .8, name + '-head')
    return [line, head]


def _arp_packet(a, x1, y1, x2, y2, when, name):
    """Conceptual request/reply token, used only in the explanatory first scene."""
    token = a.add('<path d="M-20 -13 H20 V13 H-20 Z M-20 -13 L0 2 L20 -13" '
                  f'fill="{SOFT}" stroke="{INK}" stroke-width="3"/>', name)
    a.parts[-1] = a.parts[-1].replace(f'id="{token}"', f'id="{token}" style="opacity:0"')
    a.moves.append({'target': token, 'start': when, 'duration': 1.6,
                    'travel': [x1, y1, x2, y2]})
    return token


def _arp_fade(a, ids, when, opacity=0):
    for ident in ids:
        a.move(ident, when, .55, opacity=opacity)


def S22(a):
    """A broadcast question, a reply, and the two address layers it describes."""
    t0 = at(a, 0)
    request = a.at('A request can ask')
    retained = a.at('Hosts retain mappings')
    remote = at(a, 1)
    unauthenticated = a.at("ARP's original mechanism")
    fields = a.at('Read the sender hardware')

    _arp_label(a, 795, 323, 'LOCAL LINK', t0, 32, name='local-link')
    P(a, 'school_laptop', 235, 380, 170, 0, 'staff')
    _arp_label(a, 320, 550, 'STAFF', t0, 34, name='staff-name')
    _arp_label(a, 320, 588, '10.44.10.21', t0, 30, mono=True, name='staff-ip')
    P(a, 'edge_router', 1180, 380, 170, 0, 'gateway')
    _arp_label(a, 1265, 550, 'Gateway', t0, 34, name='gateway-name')
    _arp_label(a, 1265, 588, '10.44.10.1', t0, 30, mono=True, name='gateway-ip')

    request_parts = _arp_arrow(a, 430, 425, 1155, 425, request,
                               'arp-request', color=ACCENT)
    request_parts.append(_arp_label(a, 792, 390, 'Who has 10.44.10.1?', request,
                                     32, name='request-question'))
    request_parts.append(_arp_label(a, 792, 464, 'Local broadcast', request,
                                     30, name='broadcast-label'))
    request_parts.append(_arp_packet(a, 430, 425, 1155, 425, request + .9,
                                      'request-token'))
    # The little outward forks make broadcast scope explicit, without adding hosts.
    request_parts.append(_arp_line(a, 'M1027 425 V473 M1011 460 L1027 473 L1043 460',
                                    request + .2, 'broadcast-fork', GRAY))
    reply_parts = _arp_arrow(a, 1155, 520, 430, 520, request + 2.5,
                             'arp-reply', color=ACCENT)
    reply_parts.append(_arp_label(a, 792, 563, '02:44:10:00:00:01', request + 2.5,
                                   30, mono=True, name='reply-hardware-address'))
    reply_parts.append(_arp_packet(a, 1155, 520, 430, 520, request + 3.4,
                                    'reply-token'))

    # This is a teaching mapping, never a depiction of an installed fixture cache.
    mapping = _arp_layer(a, rect(420, 615, 945, 150, WHITE, 3), retained,
                         'example-mapping-paper', dy=12)
    _arp_label(a, 892, 650, 'Teaching mapping', retained, 32,
               name='example-mapping-title')
    _arp_label(a, 610, 691, 'Protocol address', retained, 30,
               name='mapping-protocol-field')
    _arp_label(a, 1080, 691, 'Hardware address', retained, 30,
               name='mapping-hardware-field')
    _arp_label(a, 610, 734, '10.44.10.1', retained, 32, mono=True,
               name='mapping-protocol-value')
    _arp_label(a, 1080, 734, '02:44:10:00:00:01', retained, 30, mono=True,
               name='mapping-hardware-value')
    _arp_arrow(a, 777, 723, 867, 723, retained + .25, 'mapping-association')

    _arp_fade(a, request_parts + reply_parts, remote)
    # A nested IP packet retains its remote destination inside a locally addressed frame.
    frame = _arp_layer(a, rect(480, 350, 620, 190, SOFT, 3)
                       + rect(508, 448, 564, 72, WHITE, 3), remote,
                       'ethernet-ip-nesting', dy=12)
    _arp_label(a, 790, 387, 'Ethernet destination', remote, 30,
               name='ethernet-destination-label')
    _arp_label(a, 790, 428, 'gateway MAC', remote, 34,
               name='ethernet-destination-value')
    _arp_label(a, 790, 494, 'IP destination: remote server', remote + .45,
               30, name='ip-destination')
    _arp_arrow(a, 421, 475, 472, 475, remote + .3, 'frame-left-stub')
    _arp_arrow(a, 1108, 475, 1160, 475, remote + .6, 'frame-right-stub')

    proof = _arp_layer(a, rect(480, 558, 620, 54, WHITE, 3), unauthenticated,
                       'identity-proof-strip')
    proof_text = _arp_label(a, 790, 595, 'No cryptographic identity proof',
                            unauthenticated, 30, name='identity-proof-label')
    _arp_fade(a, [proof, proof_text], fields)
    _arp_line(a, 'M1114 350 H1130 V540 H1114', fields, 'layer-bracket', ACCENT)
    _arp_label(a, 790, 595, 'Ethernet header / ARP sender fields', fields,
               30, name='related-distinct-fields')
    _arp_label(a, 892, 810 - 7, 'Offline reading • no cache install',
               a.at('It does not cause any operating system'), 30,
               name='offline-cache-boundary')


def S23(a):
    """Conflicting reply content remains separate from unknown cache and forwarding."""
    t0 = at(a, 0)
    adopted = a.at('If the recipient uses')
    mitm = a.at('A man-in-the-middle arrangement')
    northstar = a.at('At Northstar, the synthetic ARP file')
    claims = at(a, 2)
    unknown = at(a, 3)
    next_check = a.at('To strengthen a live-lab conclusion')

    _arp_label(a, 575, 326, 'Claimed gateway: 10.44.10.1', t0, 32,
               name='claimed-ip')
    # The trace supplies the two rows. Neither row is promoted to an authorization record.
    _arp_layer(a, rect(220, 350, 710, 80, WHITE, 3), northstar,
               'reply-a-paper', dy=10)
    _arp_label(a, 304, 400, 'Reply A', northstar, 30, name='reply-a-label')
    _arp_label(a, 640, 400, '02:44:10:00:00:01', northstar, 30,
               mono=True, name='reply-a-mac')
    _arp_layer(a, rect(220, 452, 710, 80, SOFT, 3), t0,
               'reply-b-paper', dy=10)
    _arp_label(a, 304, 502, 'Reply B', t0, 30, name='reply-b-label')
    _arp_label(a, 640, 502, '02:44:10:00:00:66', t0, 30,
               mono=True, name='reply-b-mac')

    # A blank ledger and a question mark deliberately remain unchanged throughout.
    _arp_layer(a, rect(1045, 350, 330, 180, WHITE, 3)
               + path('M1045 407 H1375', GRAY), t0, 'recipient-cache-paper', dy=10)
    _arp_label(a, 1210, 389, 'Recipient cache', t0, 32, name='cache-title')
    cache_unknown = _arp_label(a, 1210, 456, 'UNMEASURED', t0, 30,
                               name='cache-unmeasured')
    _arp_label(a, 1210, 508, '?', t0, 38, color=INK, name='cache-question')
    _arp_arrow(a, 939, 493, 1036, 471, adopted, 'adoption-question',
               dashed=True, color=ACCENT)
    _arp_label(a, 996, 328, 'Adoption?', adopted, 30, name='adoption-label')

    # These icons and dashed arrows explain conditions. No packet token ever travels here.
    P(a, 'school_laptop', 235, 585, 130, 0, 'staff-conditional')
    _arp_label(a, 300, 725, 'STAFF', t0, 32, name='staff-label')
    _arp_label(a, 300, 767, '10.44.10.21', t0, 30, mono=True, name='staff-address')
    _arp_layer(a, _arp_prop_content('school_laptop', 690, 585, 130), adopted,
               'claiming-station', dy=12)
    _arp_label(a, 755, 725, 'Claiming station', adopted, 30,
               name='claiming-station-label')
    _arp_arrow(a, 385, 640, 670, 640, adopted, 'conditional-redirection',
               dashed=True, color=ACCENT)
    _arp_label(a, 525, 604, 'If adopted', adopted, 30, name='conditional-label')
    _arp_layer(a, _arp_prop_content('edge_router', 1195, 585, 130), mitm,
               'gateway-conditional', dy=12)
    _arp_label(a, 1260, 725, 'Gateway', mitm, 32, name='gateway-label')
    _arp_arrow(a, 840, 640, 1172, 640, mitm, 'conditional-forwarding',
               dashed=True, color=ACCENT)
    _arp_label(a, 1005, 604, 'Forwarding?', mitm, 30, name='forwarding-question')
    required = _arp_label(a, 1005, 690, 'Required for MITM', at(a, 1), 30,
                          name='mitm-condition')

    _arp_label(a, 575, 568, '2 conflicting binding claims', claims, 30,
               name='observed-claim-count')
    _arp_line(a, 'M224 438 H926', claims, 'claims-separator', ACCENT)
    _arp_line(a, 'M1080 474 H1340', unknown, 'cache-evidence-underline', ACCENT)
    path_unknown = _arp_label(a, 930, 785, 'Path: UNMEASURED', unknown, 30,
                              name='path-unmeasured')
    # The final check is a proposed evidence collection step, never a performed action.
    _arp_fade(a, [required, path_unknown], next_check)
    _arp_label(a, 910, 785, 'Next: cache + ports + records + both sides', next_check,
               30, 60, name='live-lab-next-check')


def _arp_prop_content(kind, x, y, w):
    """Reuse staged native props while allowing an exact sentence reveal."""
    source = ROOT / 'assets/props' / f'{kind}.svg'
    svg = source.read_text()
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1).split()
    return f'<g transform="translate({x} {y}) scale({w/float(vb[2])})">{inner(source)}</g>'


def S24(a):
    """An observed change fans into hypotheses and independently checked records."""
    t0 = at(a, 0)
    replacement = a.at('A planned gateway replacement')
    duplicate = a.at('A duplicate-address mistake')
    compare_records = at(a, 1)
    unconfirmed = at(a, 2)
    analysis = a.at('A strong analysis records')
    decision = at(a, 3)

    # Full trace values remain legible; the card makes no approval assertion.
    _arp_layer(a, rect(215, 350, 400, 280, WHITE, 3)
               + path('M575 350 V390 H615', GRAY), t0, 'observed-change-paper', dy=12)
    _arp_label(a, 415, 391, '10.44.10.1', t0, 34, mono=True, name='changed-ip')
    _arp_label(a, 415, 434, 'Claim A', t0, 30, name='old-claim-label')
    _arp_label(a, 415, 474, '02:44:10:00:00:01', t0, 30, mono=True,
               name='old-claim-mac')
    _arp_line(a, 'M415 491 V527 M404 514 L415 527 L426 514', t0 + .5,
               'mapping-change-arrow', ACCENT)
    _arp_label(a, 415, 566, 'Claim B', t0, 30, name='new-claim-label')
    _arp_label(a, 415, 607, '02:44:10:00:00:66', t0, 30, mono=True,
               name='new-claim-mac')
    _arp_label(a, 940, 325, 'Plausible explanations', t0, 34,
               name='hypotheses-title')

    # Every branch is a candidate cause; differing native symbols explain the mechanism.
    _arp_line(a, 'M629 490 C692 490 692 385 764 385', replacement,
               'failover-branch')
    routers = (rect(774, 361, 30, 38, SOFT, 4)
               + rect(818, 361, 30, 38, WHITE, 4)
               + path('M779 372 H798 M823 372 H842 M785 407 H837 '
                      'M828 400 L837 407 L828 414', ACCENT))
    _arp_layer(a, routers, replacement, 'failover-router-pair', dy=8)
    _arp_label(a, 975, 388, 'Gateway failover', replacement, 30, 16,
               name='failover-label')

    _arp_line(a, 'M629 490 C692 490 692 475 764 475', replacement + .45,
               'maintenance-branch')
    wrench = (f'<path d="M792 450 C783 447 778 454 780 464 L800 484 '
              f'L812 472 L793 454 L799 448 C808 447 814 452 815 460 '
              f'L825 469 L805 490 L786 470 C775 468 771 455 778 447 Z" '
              f'fill="{SOFT}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    _arp_layer(a, wrench, replacement + .45, 'maintenance-wrench', dy=8)
    _arp_label(a, 975, 483, 'Maintenance', replacement + .45, 30, 16,
               name='maintenance-label')

    _arp_line(a, 'M629 490 C692 490 692 565 764 565', duplicate,
               'duplicate-branch')
    duplicates = (rect(775, 540, 43, 38, WHITE, 2)
                  + rect(798, 554, 43, 38, SOFT, 2)
                  + path('M783 551 H809 M806 565 H832', GRAY))
    _arp_layer(a, duplicates, duplicate, 'duplicate-address-tickets', dy=8)
    _arp_label(a, 975, 576, 'Duplicate address', duplicate, 30, 16,
               name='duplicate-label')

    _arp_line(a, 'M629 490 C692 490 692 655 764 655', duplicate + .6,
               'spoofing-branch')
    _arp_layer(a, f'<circle cx="810" cy="654" r="24" fill="{WHITE}" '
                  f'stroke="{INK}" stroke-width="3"/>'
                  + text(810, 666, '?', 34, 2), duplicate + .6,
               'spoofing-question', dy=8)
    _arp_label(a, 975, 661, 'Spoofing hypothesis', duplicate + .6, 30, 17,
               name='spoofing-label')

    # Blank checkboxes ask for records; they never change to completed checks.
    record_paper = _arp_layer(a, rect(1125, 350, 280, 365, WHITE, 3)
                              + path('M1125 407 H1405', GRAY), compare_records,
                              'approval-record-paper', dy=12)
    _arp_label(a, 1265, 391, 'Check records', compare_records, 32,
               name='records-title')
    for j, label in enumerate(['Inventory', 'Window', 'Switch port']):
        y = 438 + j * 70
        _arp_layer(a, rect(1145, y - 22, 28, 28, WHITE, 1),
                   compare_records + j * .2, 'record-checkbox-' + str(j))
        _arp_label(a, 1189, y, label, compare_records + j * .2, 30,
                   name='record-label-' + str(j), anchor='start')
    name_warning = _arp_label(a, 1265, 678, 'Names ≠ approval',
                              a.at('A device name inferred'), 30,
                              name='name-approval-boundary')
    _arp_fade(a, [name_warning], unconfirmed)
    _arp_layer(a, rect(1141, 640, 248, 57, SOFT, 1), unconfirmed,
               'unconfirmed-stamp', dy=7)
    _arp_label(a, 1265, 679, 'UNCONFIRMED', unconfirmed, 30,
               name='unconfirmed-status')

    _arp_layer(a, rect(220, 744, 1180, 64, WHITE, 3)
               + f'<circle cx="252" cy="776" r="17" fill="{PAPER}" '
                 f'stroke="{INK}" stroke-width="3"/>'
               + path('M252 764 V776 L261 781'), analysis,
               'record-evidence-strip', dy=8)
    _arp_label(a, 818, 787, 'Record addresses + timestamps; compare evidence',
               analysis, 32, 60, name='record-evidence-label')
    _arp_label(a, 1265, 325, 'Next check', decision, 30,
               name='next-record-check')
    _arp_label(a, 415, 689, 'Cause: OPEN',
               a.at('Do not turn a training alert'), 32, name='cause-open')

"""M10 S01–S22: native resource, network and TCP teaching geometry.

Only finite, narration-anchored paint/transform/path moves are emitted.  Units
and observation points stay attached to the simulated values they describe.
"""
from art_common import *


def _draw(a, d, i=0, color=INK, name=None, t=None, dashed=False):
    g = a.add(path(d, color, '10 10' if dashed else ''), name)
    a.moves.append({'target': g, 'start': at(a, i) if t is None else t,
                    'duration': .8, 'draw': True, 'dashed': dashed})
    return g


def _label(a, x, y, value, t, size=30, width=36, name=None, anchor='middle'):
    g = a.add(text(x, y, value, size, width, anchor), name)
    a.show(g, t)
    return g


def _box(a, x, y, w, h, value, t, fill=WHITE, size=30, width=None, name=None):
    g = a.add(rect(x, y, w, h, fill, 5) +
              text(x + w / 2, y + 39, value, size,
                   width or max(10, int(w / (size * .55)))), name)
    a.show(g, t, dy=10)
    return g


def _bar(a, x, y, w, h, fraction, t, name, fill=ACCENT):
    """Authored final geometry, transform-only fill, explicit global SVG origin."""
    outline = a.add(rect(x, y, w, h, WHITE, 3), name + '-budget')
    a.show(outline, t)
    filled = a.add(f'<rect x="{x+4}" y="{y+4}" width="{(w-8)*fraction}" '
                   f'height="{h-8}" rx="2" fill="{fill}" stroke="none"/>',
                   name + '-fill')
    a.moves.append({'target': filled, 'start': t + .15, 'duration': 1,
                    'from': {'scaleX': 0, 'opacity': 0,
                             'svgOrigin': f'{x+4} {y+h/2}'},
                    'props': {'scaleX': 1, 'opacity': 1,
                              'svgOrigin': f'{x+4} {y+h/2}',
                              'ease': 'power2.out'}})
    return outline


def _laptop(a, x, y, i=0, w=180, label=None, t=None, name=None):
    h = w * .63
    content = rect(x, y, w, h, WHITE, 5) + rect(x+12, y+12, w-24, h-26, SOFT, 2)
    content += path(f'M{x-8} {y+h+9} H{x+w+8} L{x+w-5} {y+h+23} H{x+5} Z')
    g = a.add(content, name)
    now = at(a, i) if t is None else t
    a.show(g, now, dy=12)
    if label:
        _label(a, x+w/2, y+h+65, label, now, 30, 23)
    return g


def _server(a, x, y, i=0, w=170, label=None, t=None, name=None):
    h = 172
    content = rect(x, y, w, h, WHITE, 5)
    for j in range(3):
        yy = y+20+j*48
        content += rect(x+12, yy, w-24, 34, SOFT, 3)
        content += f'<circle cx="{x+w-31}" cy="{yy+17}" r="5" fill="{INK}"/>'
    g = a.add(content, name)
    now = at(a, i) if t is None else t
    a.show(g, now, dy=12)
    if label:
        _label(a, x+w/2, y+h+43, label, now, 30, 23)
    return g


def _packet(a, x, y, w=42, h=26, i=0, name=None, t=None):
    g = a.add(rect(x, y, w, h, SOFT, 2) +
              path(f'M{x} {y} L{x+w/2} {y+h*.6} L{x+w} {y}'), name)
    a.show(g, at(a, i) if t is None else t, dx=-10)
    return g


def _queue(a, x, y, w, h, filled, t, name, cells=8):
    border = a.add(rect(x, y, w, h, WHITE, 4), name + '-boundary')
    a.show(border, t)
    gap = 8
    cw = (w-24-(cells-1)*gap)/cells
    for j in range(cells):
        g = a.add(rect(x+12+j*(cw+gap), y+15, cw, h-30,
                       SOFT if j < filled else WHITE, 2), name+f'-cell-{j}')
        a.show(g, t + min(j, filled)*.065, dy=8)
    return border


def _rule(a, x1, y, x2, i=0, t=None):
    return _draw(a, f'M{x1} {y} H{x2}', i, GRAY, t=t)


_CLOSING_PHRASES = {
    'S01': "Begin with the student's task",
    'S02': 'This map is a starting model',
    'S03': 'A good incident note',
    'S04': 'Tally keeps the scope card',
    'S05': 'The method also leaves room',
    'S06': 'This approach does not require',
    'S07': 'When a dashboard uses',
    'S08': 'A capacity number without',
    'S09': 'First describe the traffic pattern',
    'S10': 'Choose a hypothesis',
    'S11': 'The evidence supports',
    'S12': 'The analysis should connect',
    'S13': 'In an incident record',
    'S14': 'Protecting the constrained access path',
    'S15': 'Our learner workflow',
    'S16': 'We will discuss control selection',
    'S17': 'For availability analysis',
    'S18': 'To interpret a real operating system',
    'S19': 'The next step is to compare',
    'S20': 'It would also check',
    'S21': 'For Northstar',
    'S22': 'Keep the original incident evidence',
}


def _closing_note(a, label):
    # A later reasoning beat must remain distinct from the four object reveals.
    # Shift the common note's complete bounded draw/marker/text group together.
    first = len(a.moves)
    note(a, label)
    delta = max(0, a.at(_CLOSING_PHRASES[a.sid]) - at(a, 3))
    for move in a.moves[first:]:
        move['start'] = round(move['start'] + delta, 6)


def S01(a):
    person(a, 300, 345, 'Authorized student', 0)
    _laptop(a, 600, 355, 1, 220)
    L(a, 710, 555, 'Learning access', 1, 34, 21)
    _laptop(a, 1080, 355, 2, 220)
    L(a, 1190, 555, 'Enrollment', 2, 34, 21)
    R(a, 360, 425, 580, 425, 1)
    R(a, 835, 425, 1065, 425, 2)
    _draw(a, 'M585 610 V643 H1320 V610', 3)
    L(a, 950, 692, 'Availability', 3, 36, 25)
    _label(a, 800, 335, 'Northstar', at(a, 0), 32, 30)
    _closing_note(a, 'Protect the completed task; all campus incidents are simulated')


def S02(a):
    xs = [235, 540, 845, 1150]
    labels = ['Name lookup', 'Network path', 'Connection', 'Application']
    for i, (x, label) in enumerate(zip(xs, labels)):
        if i in (0, 3):
            _server(a, x+26, 365, i, 150)
        elif i == 1:
            for dx, dy in [(0, 28), (112, 0), (112, 90)]:
                g = a.add(rect(x+dx, 390+dy, 73, 48, SOFT, 4))
                a.show(g, at(a, i), dy=10)
            _draw(a, f'M{x+73} 442 L{x+112} 414 M{x+73} 442 L{x+112} 504', i)
        else:
            _draw(a, f'M{x+18} 395 V515 M{x+183} 395 V515', i)
            R(a, x+20, 420, x+180, 420, i)
            R(a, x+180, 485, x+20, 485, i)
        L(a, x+100, 625, label, i, 32, 15)
        if i:
            R(a, x-40, 460, x+10, 460, i)
    _closing_note(a, 'A failure at any dependency can interrupt the useful task')


def S03(a):
    L(a, 430, 345, 'Success', 0, 34, 24)
    _box(a, 240, 380, 380, 135, 'Completed task / attempted checks', at(a, 0), size=31)
    L(a, 965, 345, 'Delay', 1, 34, 24)
    _draw(a, 'M715 470 H1260 M715 455 V485 M1260 455 V485', 1)
    for j, x in enumerate([750, 900, 1050, 1200]):
        _draw(a, f'M{x} 456 V484', 1, GRAY)
    _label(a, 990, 420, 'Start → useful result', at(a, 1), 30, 30)
    _box(a, 240, 560, 380, 125, 'Errors: record the failed stage', at(a, 2), SOFT, 31)
    _label(a, 430, 547, 'Errors', at(a, 2), 34, 24)
    _draw(a, 'M720 575 V660 H1260 V575', 3)
    L(a, 990, 620, 'Time window', 3, 34, 27)
    _label(a, 990, 706, 'Aligned observations', at(a, 3), 30, 30)
    _closing_note(a, 'Keep the task, denominator, timing basis and observation interval')


def S04(a):
    _box(a, 230, 345, 410, 305, 'Written scope', at(a, 0), WHITE, 34, 20)
    for j, value in enumerate(['Owner + systems', 'Permitted action', 'Responsible contact']):
        _rule(a, 260, 425+j*70, 610, 0)
        _label(a, 435, 465+j*70, value, at(a, 0), 29, 25)
    _draw(a, 'M710 360 H1350 V655 H710 Z', 1, ACCENT, dashed=True)
    L(a, 1030, 405, 'Offline evidence', 1, 34, 28)
    _box(a, 770, 445, 220, 110, 'Local files', at(a, 1), SOFT)
    _box(a, 1060, 445, 230, 110, 'Local analysis', at(a, 1), WHITE)
    R(a, 996, 497, 1048, 497, 1)
    L(a, 1030, 625, 'Stop conditions', 2, 32, 28)
    _label(a, 435, 700, 'Evidence custody', at(a, 3), 34, 24)
    _closing_note(a, 'Read and analyze local fixtures; no network traffic or capture replay')


def S05(a):
    L(a, 400, 345, 'Resource', 0, 35, 20)
    _queue(a, 235, 380, 330, 115, 6, at(a, 0), 'resource', 8)
    L(a, 1040, 345, 'Demand', 1, 35, 20)
    for j in range(4):
        _packet(a, 875+j*80, 420, 50, 34, 1, f'demand-{j}')
    R(a, 850, 440, 590, 440, 1)
    _box(a, 235, 565, 330, 115, 'Evidence', at(a, 2), SOFT, 34)
    _box(a, 865, 565, 350, 115, 'Control', at(a, 3), WHITE, 34)
    R(a, 400, 505, 400, 550, 2)
    R(a, 580, 623, 850, 623, 3)
    _draw(a, 'M1225 600 H1350 V355 H585', 3, ACCENT, dashed=True)
    _closing_note(a, 'Ask whether the proposed control can spare the constrained resource')


def S06(a):
    _laptop(a, 250, 375, 0, 215)
    L(a, 357, 610, 'Service failure', 0, 33, 20)
    _draw(a, 'M290 445 L325 480 M325 445 L290 480', 0, ACCENT)
    _queue(a, 575, 395, 350, 125, 8, at(a, 1), 'pressure', 8)
    L(a, 750, 350, 'Resource pressure', 1, 33, 24)
    R(a, 480, 455, 560, 455, 1, dashed=True)
    _box(a, 1030, 385, 335, 145, 'Mechanism', at(a, 2), SOFT, 33)
    R(a, 940, 455, 1018, 455, 2, dashed=True)
    _box(a, 715, 595, 490, 100, 'Intent: separate evidence', at(a, 3), WHITE, 32)
    R(a, 1195, 543, 1120, 580, 3, dashed=True)
    _label(a, 400, 700, 'Task → symptom', at(a, 0), 30, 26)
    _closing_note(a, 'Protect users while the cause and attribution are investigated')


def S07(a):
    rows = [('Bits per second', 'IP octets × 8 / seconds'),
            ('Packets per second', 'Packets / seconds'),
            ('Requests per second', 'Application requests / seconds')]
    for i, (label, formula) in enumerate(rows):
        yy = 365+i*105
        L(a, 465, yy, label, i, 32, 24)
        _label(a, 1020, yy, formula, at(a, i), 31, 32)
        _rule(a, 235, yy+35, 1370, i)
        if i == 0:
            for j in range(5):
                _packet(a, 765+j*80, yy+48, 55, 22, i, f'bits-{j}')
    _draw(a, 'M255 690 V711 H1350 V690', 3)
    L(a, 800, 690, 'Same window', 3, 32, 26)
    _closing_note(a, 'Match time, observation point and counted layer before comparing rates')


def S08(a):
    L(a, 330, 345, 'Arrival', 0, 34, 20)
    for j in range(3):
        _packet(a, 235+j*75, 395, 50, 34, 0, f'arrival-{j}')
    R(a, 460, 413, 580, 413, 0)
    _queue(a, 600, 370, 490, 115, 7, at(a, 2), 'bounded-queue', 8)
    L(a, 845, 540, 'Queue', 2, 34, 20)
    _draw(a, 'M1135 365 V500 M1117 365 H1153 M1117 500 H1153', 1)
    L(a, 1250, 350, 'Capacity', 1, 34, 20)
    _box(a, 1190, 400, 180, 95, 'Work desk', at(a, 1), SOFT, 30)
    R(a, 1098, 430, 1175, 430, 1)
    R(a, 1280, 510, 1280, 610, 3)
    L(a, 1190, 705, 'Completion', 3, 34, 22)
    _packet(a, 1260, 625, 48, 30, 3, 'completed-work')
    _label(a, 620, 660, 'Illustrative finite work budget',
           a.at('Real services have several queues'), 30, 43)
    _closing_note(a, 'Persistent excess work must wait, be rejected or be dropped')


def S09(a):
    L(a, 480, 345, 'One source', 0, 34, 24)
    _laptop(a, 235, 400, 0, 145)
    _server(a, 610, 390, 0, 145)
    R(a, 395, 455, 595, 455, 0)
    L(a, 1085, 345, 'Many sources', 1, 34, 24)
    for j, yy in enumerate([380, 480, 580]):
        _laptop(a, 845, yy, 1, 100)
        R(a, 958, yy+30, 1195, 498, 1)
    _server(a, 1210, 420, 1, 145)
    _label(a, 470, 630, 'Observed address', at(a, 2), 32, 26)
    _label(a, 470, 685, '192.0.2.10', at(a, 2), 31, 22)
    _label(a, 1120, 700, 'Attribution: unresolved', at(a, 3), 32, 29)
    _closing_note(a, 'Distribution describes observed traffic; addresses do not identify people')


def S10(a):
    positions = [245, 545, 845, 1145]
    labels = ['Bandwidth', 'Packet work', 'Connection state', 'Application work']
    for i, (x, label) in enumerate(zip(positions, labels)):
        if i == 0:
            _draw(a, f'M{x} 405 H{x+180} M{x} 485 H{x+180}', i)
            R(a, x+7, 445, x+173, 445, i)
        elif i == 1:
            for j in range(6):
                _packet(a, x+(j%3)*65, 390+(j//3)*70, 45, 32, i)
        elif i == 2:
            _queue(a, x, 385, 210, 140, 4, at(a, i), 'connection-budget', 6)
        else:
            _server(a, x+25, 365, i, 150)
        L(a, x+90, 605, label, i, 32, 17)
        if i:
            R(a, x-45, 455, x-5, 455, i)
    _label(a, 800, 706, 'One path · several finite resources',
           a.at('These families can interact'), 31, 50)
    _closing_note(a, 'Packet names alone do not identify the resource being exhausted')


def S11(a):
    labels = ['Baseline', 'Enrollment', 'Offered load', 'Accepted load']
    values = [50, 150, 2400, 200]
    _label(a, 965, 335, 'Common scale: 0–2400 Mbps', at(a, 0), 29, 39)
    for i, (label, value) in enumerate(zip(labels, values)):
        yy = 375+i*81
        L(a, 385, yy+32, label, i, 32, 21)
        _bar(a, 585, yy, 590, 47, value/2400, at(a, i), f'rate-{i}',
             ACCENT if i == 2 else SOFT)
        _label(a, 1285, yy+32, f'{value} Mbps', at(a, i), 30, 14)
    _label(a, 950, 700, 'WAN ingress capacity: 200 Mbps',
           a.at('These figures describe different observation points'), 30, 43)
    _closing_note(a, 'Same 60-second IP-octet windows · discarded equivalent: 2200 Mbps')


def S12(a):
    L(a, 350, 345, 'Provider view', 0, 33, 21)
    _box(a, 235, 385, 230, 105, '2400 Mbps offered', at(a, 0), SOFT, 31, 15)
    _draw(a, 'M730 365 V535 M712 365 H748 M712 535 H748', 1, ACCENT)
    L(a, 730, 340, 'Ingress limit', 1, 33, 22)
    _label(a, 825, 410, '200 Mbps', at(a, 1), 31, 20)
    R(a, 480, 455, 705, 455, 1)
    R(a, 755, 455, 1090, 455, 1)
    _server(a, 1110, 380, 3, 185)
    L(a, 1200, 345, 'Server view', 3, 33, 20)
    R(a, 630, 470, 630, 595, 2)
    _box(a, 475, 610, 320, 90, 'Discarded traffic', at(a, 2), WHITE, 30, 22)
    _label(a, 635, 565, '2200 Mbps', at(a, 2), 31, 20)
    _label(a, 1175, 610, 'CPU: 25%', at(a, 3), 32, 24)
    _label(a, 1175, 675, 'User success: 20 / 100',
           a.at('while only twenty'), 30, 29)
    _closing_note(a, 'A downstream processor can be lightly loaded behind a constrained path')


def S13(a):
    L(a, 450, 345, 'Packet size', 0, 34, 23)
    L(a, 1100, 345, 'Packet rate', 1, 34, 23)
    for j in range(2):
        _packet(a, 245+j*220, 390, 200, 55, 0, f'large-{j}')
    for j in range(8):
        _packet(a, 245+j*55, 505, 50, 55, 1, f'small-{j}')
    _label(a, 455, 620, 'Equal illustrative data volume', at(a, 1), 30, 32)
    _draw(a, 'M765 370 V660', 1, GRAY)
    _queue(a, 850, 400, 470, 100, 6, at(a, 2), 'packet-work', 8)
    L(a, 1085, 555, 'Processing cost', 2, 33, 25)
    _label(a, 1085, 625, 'Measured limit', at(a, 3), 33, 24)
    _label(a, 1085, 686, 'Device + configuration + traffic', at(a, 3), 29, 32)
    _closing_note(a, 'Illustration, not a measured router result · check packets and bytes')


def S14(a):
    L(a, 450, 340, 'Direct traffic', 0, 34, 22)
    _laptop(a, 235, 385, 0, 140)
    R(a, 390, 430, 800, 430, 0)
    L(a, 410, 570, 'Coordinated devices', 1, 32, 24)
    for j in range(3):
        _laptop(a, 230+j*175, 600, 1, 115)
        R(a, 290+j*175, 600, 805, 480, 1)
    _draw(a, 'M835 390 H990 M835 510 H990 M990 390 L1040 425 '
             'V475 L990 510', 2, ACCENT)
    L(a, 1100, 340, 'Shared bottleneck', 2, 33, 23)
    _server(a, 1160, 390, 2, 170)
    R(a, 1050, 450, 1145, 450, 2)
    L(a, 1090, 665, 'Source uncertainty', 3, 33, 24)
    _closing_note(a, 'Architecture illustration · the fixture does not establish a botnet')


def S15(a):
    _laptop(a, 245, 445, 0, 160, t=a.at())
    _draw(a, 'M740 430 V600 M700 465 H780 M700 565 H780', 0, t=a.at())
    _server(a, 1190, 425, 0, 160, t=a.at())
    R(a, 420, 495, 700, 495, 0)
    R(a, 785, 495, 1175, 495, 0)
    L(a, 480, 345, 'Packet analyzer', 0, 32, 25)
    _draw(a, 'M480 365 V455', 0, ACCENT, dashed=True)
    L(a, 1020, 345, 'Flow records', 1, 32, 25)
    _draw(a, 'M1020 365 V455', 1, ACCENT, dashed=True)
    L(a, 795, 680, 'Interface counters', 2, 32, 26)
    _draw(a, 'M795 635 V565', 2, ACCENT, dashed=True)
    L(a, 420, 690, 'Service checks', 3, 32, 25)
    _draw(a, 'M420 645 V580', 3, ACCENT, dashed=True)
    _closing_note(a, 'Local evidence views have different coverage, sampling and timing limits')


def S16(a):
    _laptop(a, 235, 445, 0, 120, t=a.at())
    _server(a, 1240, 415, 0, 140, t=a.at())
    _draw(a, 'M790 435 H930 M790 535 H930', 2)
    L(a, 860, 345, 'Protected link', 2, 33, 23)
    _label(a, 860, 390, '200 Mbps capacity', at(a, 2), 29, 27)
    _box(a, 1020, 430, 170, 120, 'Campus filter', at(a, 0), WHITE, 30, 12)
    _box(a, 470, 430, 185, 120, 'Upstream filter', at(a, 1), SOFT, 30, 12)
    R(a, 370, 490, 455, 490, 1)
    R(a, 670, 490, 775, 490, 2)
    R(a, 945, 490, 1005, 490, 0)
    R(a, 1200, 490, 1225, 490, 0)
    _draw(a, 'M480 585 V615 H935 V585', 2, ACCENT)
    _label(a, 710, 670, 'Spare capacity before the boundary', at(a, 2), 30, 40)
    L(a, 1225, 685, 'User outcome', 3, 32, 21)
    _closing_note(a, 'Proposed placement · recovery rows are simulated, not deployment proof')


def S17(a):
    _label(a, 350, 340, 'Client', a.at(), 34, 20)
    _label(a, 1020, 340, 'Server', a.at(), 34, 20)
    _draw(a, 'M350 365 V690 M1020 365 V690', 0, t=a.at())
    R(a, 365, 405, 1005, 405, 0)
    L(a, 680, 385, 'Synchronize', 0, 32, 24)
    response = a.at('The server responds')
    a.route(1005, 510, 365, 510, response, label='SYN + ACK')
    R(a, 365, 615, 1005, 615, 1)
    L(a, 680, 595, 'Acknowledge', 1, 32, 24)
    _box(a, 1090, 425, 275, 105, 'Pending state', at(a, 2), SOFT, 30, 19)
    _box(a, 1090, 605, 275, 85, 'Established', at(a, 3), WHITE, 30, 19)
    _draw(a, 'M1230 545 V590', 3, ACCENT)
    _label(a, 680, 705, 'Ordinary three-message exchange',
           a.at('This is a simplified normal handshake'), 29, 42)
    _closing_note(a, 'Sequence coordination does not authenticate the person or later request')


def S18(a):
    L(a, 490, 345, 'Half-open entries', 0, 33, 25)
    L(a, 1090, 345, 'Backlog capacity', 1, 33, 25)
    _label(a, 475, 430, 'Reported occupancy: 1024', at(a, 0), 33, 26)
    _label(a, 475, 495, 'State observation', at(a, 0), 30, 26)
    _draw(a, 'M810 380 H1370 V610 H810 Z', 1)
    for j in range(16):
        x = 830+(j%8)*65
        y = 403+(j//8)*85
        g = a.add(rect(x, y, 50, 60, SOFT, 3), f'pending-tile-{j}')
        a.show(g, at(a, 1)+j*.045, dy=10)
    _label(a, 1090, 655, '16 tiles × 64 entries = 1024', at(a, 1), 29, 34)
    _label(a, 440, 610, 'New attempts: 6000', at(a, 2), 32, 28)
    _label(a, 440, 680, 'Completed handshakes: 60', at(a, 3), 31, 30)
    _closing_note(a, 'Same 60-second fixture · unique attempts exclude retransmissions')


def S19(a):
    L(a, 480, 345, 'Link load', 0, 34, 20)
    _bar(a, 240, 385, 485, 75, .15, at(a, 0), 'link-headroom', SOFT)
    _label(a, 480, 515, '30 / 200 Mbps', at(a, 0), 34, 23)
    L(a, 1100, 345, 'State pressure', 1, 34, 23)
    _bar(a, 850, 385, 485, 75, 1, at(a, 1), 'full-state', ACCENT)
    _label(a, 1090, 515, '1024 / 1024 pending', at(a, 1), 32, 26)
    _label(a, 480, 600, 'Client success', at(a, 2), 32, 25)
    _label(a, 480, 665, '5 / 100 checks', at(a, 2), 34, 23)
    _label(a, 1100, 600, 'Alternative causes', at(a, 3), 32, 25)
    _label(a, 1100, 665, 'Loss · routing · legitimate demand', at(a, 3), 29, 34)
    _closing_note(a, 'State pressure is supported; intent and source identity remain open')


def S20(a):
    L(a, 400, 345, 'Larger backlog', 0, 32, 23)
    _queue(a, 230, 395, 340, 115, 5, at(a, 0), 'larger-budget', 10)
    L(a, 810, 345, 'Shorter timeout', 1, 32, 23)
    _draw(a, 'M810 385 A65 65 0 1 1 810 515 A65 65 0 1 1 810 385 '
             'M810 410 V450 H850', 1)
    _label(a, 810, 560, 'Shorter retention', at(a, 1), 29, 22)
    L(a, 1210, 345, 'Smaller state', 2, 32, 23)
    for j in range(4):
        g = a.add(rect(1070+j*69, 420, 54, 80, SOFT, 3))
        a.show(g, at(a, 2)+j*.06, dy=8)
    _label(a, 1210, 560, 'Compact pending records', at(a, 2), 29, 25)
    _draw(a, 'M245 600 V625 H1360 V600', 3)
    L(a, 800, 690, 'Client tradeoff', 3, 34, 30)
    _closing_note(a, 'Proposed mechanisms need client, resource and failure-behavior validation')


def S21(a):
    _label(a, 345, 340, 'Client', a.at(), 34, 20)
    _label(a, 1195, 340, 'Server', a.at(), 34, 20)
    _laptop(a, 250, 390, 0, 175, t=a.at())
    _server(a, 1105, 405, 0, 175, t=a.at())
    _draw(a, 'M435 420 V580 M1090 420 V580', 0, t=a.at())
    R(a, 1090, 420, 445, 420, 0)
    L(a, 770, 380, 'Cookie response', 0, 32, 27)
    _box(a, 580, 455, 370, 80, 'Encoded sequence value', at(a, 0), SOFT, 30, 27)
    R(a, 445, 580, 1090, 580, 1)
    L(a, 770, 630, 'Return acknowledgment', 1, 31, 29)
    _label(a, 1195, 625, 'State allocation', at(a, 2), 30, 20)
    _queue(a, 1080, 640, 270, 62, 3, at(a, 2), 'allocated-after-reply', 5)
    _label(a, 430, 660, 'Remaining limits', at(a, 3), 31, 23)
    _label(a, 470, 700, 'Bandwidth · packets · app work', at(a, 3), 28, 34)
    _closing_note(a, 'Proposed defense for incomplete handshakes; useful clients need validation')


def S22(a):
    _laptop(a, 230, 410, 0, 155, t=a.at())
    _box(a, 515, 380, 300, 180, 'Screening proxy', at(a, 0), SOFT, 33, 21)
    _server(a, 1150, 385, 1, 175)
    L(a, 1237, 340, 'Protected server', 1, 32, 23)
    R(a, 400, 470, 500, 470, 0)
    R(a, 830, 470, 1135, 470, 1)
    _label(a, 665, 590, 'Illustrative state budget', at(a, 2), 28, 28)
    _queue(a, 515, 610, 300, 50, 5, at(a, 2), 'proxy-illustrative-budget', 8)
    L(a, 665, 705, 'New bottleneck', 2, 32, 25)
    _label(a, 1140, 620, 'Separate validation', at(a, 3), 32, 28)
    _label(a, 1140, 680, 'Clients · capacity · failure path', at(a, 3), 28, 33)
    _closing_note(a, 'Proxy and cookies are candidates; supplied recovery rows are simulated')


def render(scene, audio):
    a = base(scene, audio)
    sid = scene['id']
    if sid not in {f'S{i:02}' for i in range(1, 23)}:
        raise ValueError(('scene_art_start ownership', sid))
    globals()[sid](a)
    return a

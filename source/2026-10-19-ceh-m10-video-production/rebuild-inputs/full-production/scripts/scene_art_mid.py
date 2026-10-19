"""Native M10 mechanism diagrams for S23–S42; narration-anchored finite motion.

Geometry is authored at its complete state. Parent converts Art moves to its
single seekable timeline. All fictional values come from the approved fixtures.
"""
from art_common import *


def _draw(a, d, i=0, name=None, color=INK, phrase=None):
    ident = a.add(path(d, color), name)
    a.moves.append({'target': ident, 'start': a.at(phrase) if phrase else at(a, i),
                    'duration': 1.1, 'draw': True})
    return ident


def _fill(a, x, y, w, h, i=0, name=None, fill=ACCENT, phrase=None):
    ident = a.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
                  f'rx="3" fill="{fill}" stroke="none"/>', name)
    a.moves.append({'target': ident, 'start': a.at(phrase) if phrase else at(a, i),
                    'duration': 1.1, 'from': {'scaleX': 0, 'svgOrigin': f'{x} {y+h/2}'},
                    'props': {'scaleX': 1, 'ease': 'power2.out'}})
    return ident


def _bar(a, x, y, w, h, value_w, i=0, name='bar', phrase=None):
    ident = a.add(rect(x, y, w, h, WHITE, 3), name+'-track')
    a.show(ident, a.at(phrase) if phrase else at(a, i))
    return _fill(a, x+3, y+3, max(1, value_w-6), h-6, i, name+'-fill', phrase=phrase)


def _foot(a, label, phrase):
    """Late note appears on a real later sentence, rather than a guessed clock."""
    first = len(a.moves)
    note(a, label)
    shift = a.at(phrase) - at(a, 3)
    for move in a.moves[first:]:
        move['start'] += shift


def _node(a, x, y, label, i=0, w=250, h=96, fill=WHITE):
    return C(a, x, y, label, i, w=w, h=h, fill=fill, size=30)


def _document(a, x, y, title, i=0, w=260, h=150):
    ident = a.add(rect(x, y, w, h, WHITE, 3) +
                  path(f'M{x+w-42} {y} V{y+40} H{x+w}', GRAY) +
                  text(x+w/2, y+47, title, 30, int(w/17)) +
                  path(f'M{x+28} {y+h-50} H{x+w-28} M{x+28} {y+h-28} H{x+w-55}', GRAY))
    a.show(ident, at(a, i), dy=12)
    return ident


def _pool(a, x, y, i=1, filled=True):
    """Exactly 32 slots, not a decorative proxy for an unspecified quantity."""
    for n in range(32):
        xx = x+(n % 8)*43
        yy = y+(n // 8)*44
        ident = a.add(rect(xx, yy, 33, 32, WHITE, 3), 'slot-'+str(n))
        a.show(ident, at(a, 0))
        if filled:
            ident = a.add(f'<rect x="{xx+3}" y="{yy+3}" width="27" height="26" '
                          f'rx="2" fill="{ACCENT}" stroke="none"/>', 'busy-'+str(n))
            a.moves.append({'target': ident, 'start': at(a, i)+(n/32)*.8, 'duration': .45,
                            'from': {'opacity': 0, 'scaleY': 0, 'svgOrigin': f'{xx+16} {yy+29}'},
                            'props': {'opacity': 1, 'scaleY': 1, 'ease': 'power2.out'}})


def render(scene, audio):
    a = base(scene, audio)
    sid = scene['id']

    if sid == 'S23':
        _node(a, 230, 360, 'Actual sender', 0, 280)
        _node(a, 730, 360, 'Answering service', 1, 290)
        _node(a, 1040, 605, 'Northstar victim', 3, 320, 94, SOFT)
        R(a, 515, 410, 715, 410, 1)
        L(a, 615, 365, 'request', 1, 30, 14)
        _node(a, 260, 580, 'Return address: victim', 2, 430, 110, SOFT)
        R(a, 690, 630, 875, 465, 2, dashed=True)
        L(a, 795, 555, 'claimed', 2, 28, 12)
        R(a, 1020, 460, 1195, 590, 3)
        L(a, 1230, 510, 'reply', 3, 30, 10)
        _foot(a, 'Constructed source field; human identity remains unknown.', 'Tally follows the return address')

    elif sid == 'S24':
        L(a, 800, 340, 'One paired IP exchange', 0, 35, 45)
        L(a, 310, 420, 'request', 0, 30, 12)
        _bar(a, 430, 385, 900, 52, 18, 1, 'request-sixty')
        L(a, 520, 475, '60 bytes', 1, 32, 16)
        L(a, 310, 575, 'response', 1, 30, 12)
        _bar(a, 430, 540, 900, 52, 900, 1, 'response-three-thousand')
        L(a, 1130, 635, '3000 bytes', 1, 32, 22)
        L(a, 820, 475, '3000 / 60 = 50x', 2, 36, 28)
        _draw(a, 'M430 660 H1330 M430 650 V670 M1330 650 V670', 3)
        L(a, 800, 705, 'Same measurement layer', 3, 30, 50)
        _foot(a, 'The ratio describes this exchange; a traffic rate also needs time.', 'To estimate a traffic rate')

    elif sid == 'S25':
        L(a, 800, 335, 'Comparable byte accounting', 0, 35, 50)
        table(a, ['Measurement', 'Request', 'Response', 'Ratio'],
              [['IP packet', '60 B', '3000 B', '50x'],
               ['Ethernet frame', '74 B', '3014 B', '40.7x']],
              x=210, y=365, w=1180, row_h=80)
        _draw(a, 'M505 623 H1095 M505 614 V633 M1095 614 V633', 1)
        L(a, 800, 674, '+14 header bytes to each packet', 1, 31, 51)
        _foot(a, 'Frame lengths exclude other possible physical-link overhead.', 'Neither number describes every physical bit')

    elif sid == 'S26':
        _node(a, 620, 330, 'Name service role', 0, 360, 90, SOFT)
        _node(a, 245, 535, 'Recursive lookup', 0, 420, 140)
        _node(a, 940, 535, 'Published zone records', 2, 420, 140)
        R(a, 680, 425, 465, 520, 0)
        R(a, 920, 425, 1145, 520, 2)
        _draw(a, 'M290 475 V515 M290 485 H620 M620 475 V515', 1, color=ACCENT)
        L(a, 465, 460, 'Intended audience', 1, 30, 23)
        L(a, 1150, 460, 'Authoritative role', 2, 30, 25)
        _draw(a, 'M800 455 V700', 3, color=GRAY)
        _foot(a, 'Review service roles; no external resolver queries are sent.', 'Our reserved test name and saved packets')

    elif sid == 'S27':
        _node(a, 215, 380, 'Origin network', 0, 300, 170)
        _node(a, 1070, 380, 'Other networks', 1, 300, 170)
        _draw(a, 'M800 335 V650 M780 335 H820 M780 650 H820', 1, color=ACCENT)
        L(a, 800, 695, 'Source validation boundary', 1, 30, 39)
        R(a, 520, 410, 1055, 410, 0)
        L(a, 800, 365, 'Allowed prefix', 0, 30, 24)
        R(a, 520, 530, 775, 530, 2)
        _draw(a, 'M760 510 L800 550 M800 510 L760 550', 2, color=ACCENT)
        L(a, 650, 610, 'Outside allowed range', 2, 29, 30)
        _foot(a, 'Allowed ranges can still contain harmful traffic.', 'A permitted source range can still contain abusive traffic')

    elif sid == 'S28':
        positions = [225, 635, 1045]
        titles = ['Origin network', 'Reflector owner', 'Victim provider']
        controls = ['Validate sources', 'Limit recursive use', 'Act before campus link']
        for j, x in enumerate(positions):
            _node(a, x, 350, titles[j], j, 335, 95, SOFT)
            _draw(a, f'M{x+168} 448 V520', j)
            _node(a, x, 535, controls[j], j, 335, 135)
        _draw(a, 'M392 697 H1212 M392 680 V710 M1212 680 V710', 3)
        _foot(a, 'Each owner acts at a different part of the reflection path.', 'A Shared response therefore needs clear observations')

    elif sid == 'S29':
        L(a, 800, 335, 'CPU work each second — toy estimate', 0, 34, 54)
        L(a, 320, 410, 'ordinary', 0, 30, 14)
        _bar(a, 450, 375, 840, 62, 70, 1, 'ordinary-demand')
        L(a, 950, 414, '100/s x 0.020 s = 2', 1, 31, 37)
        L(a, 320, 580, 'incident', 0, 30, 14)
        _bar(a, 450, 545, 840, 62, 840, 3, 'incident-demand')
        L(a, 920, 664, '120/s x 0.200 s = 24', 3, 31, 39)
        _draw(a, 'M730 455 V625', 2, color=ACCENT)
        L(a, 730, 495, '8-core limit', 2, 32, 23)
        _foot(a, '24 core-seconds/s of offered work exceeds an 8-core budget.', 'The Demand estimate exceeds that budget')

    elif sid == 'S30':
        L(a, 800, 335, 'Higher count can require less CPU work', 0, 34, 57)
        L(a, 330, 405, 'requests/s', 0, 30, 18)
        _bar(a, 505, 365, 780, 58, 780, 0, 'legitimate-count')
        L(a, 890, 465, '300 requests each second', 0, 31, 38)
        L(a, 330, 565, 'core demand', 1, 30, 18)
        _bar(a, 505, 525, 780, 58, 146.25, 1, 'cheap-work')
        L(a, 1030, 567, '300 x 0.005 = 1.5', 1, 32, 32)
        L(a, 635, 665, 'Check latency', 2, 30, 25)
        L(a, 1130, 665, 'Check task success', 3, 30, 31)
        _draw(a, 'M500 625 H1370', 2, color=GRAY)
        _foot(a, 'Separate scales: count and CPU demand are different quantities.', 'The class should explain the calculation and its limits')

    elif sid == 'S31':
        _node(a, 220, 360, 'Connection held', 0, 315, 110, SOFT)
        _node(a, 1070, 360, 'Finite service slots', 1, 315, 110)
        _draw(a, 'M540 415 H1060', 0)
        L(a, 800, 365, 'Elapsed time', 1, 30, 25)
        _draw(a, 'M780 475 V635', 2, color=ACCENT)
        L(a, 780, 685, 'Progress checkpoint', 2, 31, 32)
        R(a, 360, 560, 750, 560, 1)
        L(a, 480, 635, 'No progress', 1, 29, 19)
        R(a, 820, 560, 1250, 560, 3)
        L(a, 1110, 635, 'Useful progress', 3, 29, 23)
        _foot(a, 'Deadlines must preserve legitimate slow-client operations.', 'A single aggressive timeout can reject legitimate uploads')

    elif sid == 'S32':
        _node(a, 225, 365, 'Application work', 0, 310, 110, SOFT)
        L(a, 1120, 355, 'Dependency pool: 32 slots', 0, 31, 37)
        _pool(a, 950, 390, 1)
        R(a, 535, 425, 925, 425, 0)
        _node(a, 560, 560, 'Queue: 400 waiting', 2, 350, 115)
        R(a, 910, 615, 1120, 585, 2)
        R(a, 550, 645, 375, 500, 3)
        L(a, 390, 700, 'Limit admission', 3, 29, 24)
        _foot(a, 'Occupancy is known; why the operations are slow remains open.', 'Our fixture establishes pool pressure')

    elif sid == 'S33':
        L(a, 800, 335, '2023 historical mechanism', 0, 34, 44)
        L(a, 350, 405, 'One connection', 0, 30, 22)
        _draw(a, 'M540 390 H1320 M540 530 H1320', 0, color=GRAY)
        for j in range(3):
            y = 414+j*42
            _draw(a, f'M580 {y} H850', 0)
            _draw(a, f'M810 {y-13} L838 {y+13} M838 {y-13} L810 {y+13}', 1, color=ACCENT)
            _fill(a, 920, y-14, 300, 25, 2, 'work-'+str(j), fill=SOFT)
        L(a, 1090, 585, 'Work already started', 2, 30, 31)
        _draw(a, 'M1340 385 V535', 3, color=ACCENT)
        L(a, 800, 680, 'Assess behavior across time', 3, 31, 43)
        _foot(a, 'Concept only. Cancellation can be legitimate; no traffic replay.', 'Cancellation itself is legitimate protocol behavior')

    elif sid == 'S34':
        L(a, 800, 335, 'Aligned 60-second windows', 0, 35, 48)
        labels = [('Ordinary', 50, 0), ('Enrollment', 150, 1)]
        for j, (label, value, cue) in enumerate(labels):
            yy = 405+j*155
            L(a, 340, yy+34, label, cue, 30, 17)
            _bar(a, 530, yy, 760, 62, value/200*760, cue, 'baseline-'+str(j))
            L(a, 960, yy+34, str(value)+' Mbps', cue, 32, 20)
        _draw(a, 'M1290 380 V650', 2, color=ACCENT)
        L(a, 1120, 695, '200 Mbps capacity', 2, 31, 31)
        _foot(a, 'Expected demand needs service outcomes as well as rate.', 'A rate graph alone answers neither question completely')

    elif sid == 'S35':
        row_data = [('Provider: offered', '2400 Mbps', 0),
                    ('Campus: accepted', '200 Mbps', 1),
                    ('Service outcome', '20 / 100 succeed', 2)]
        for j, (left, right, cue) in enumerate(row_data):
            yy = 345+j*120
            L(a, 405, yy+45, left, cue, 30, 23)
            _node(a, 675, yy, right, cue, 680, 85, SOFT if j==0 else WHITE)
        _draw(a, 'M610 340 V690', 3, color=GRAY)
        L(a, 795, 710, '2200 Mbps discarded; CPU 25%', 2, 30, 47)
        _foot(a, 'These are different observation points in the same 60-second window.', 'Aligned time keeps these observations tied')

    elif sid == 'S36':
        _node(a, 610, 330, 'Rate alert', 0, 390, 90, SOFT)
        _node(a, 220, 545, 'Impact + resource signals', 1, 500, 135)
        _node(a, 870, 545, 'Enrollment, retries, defects', 2, 510, 135)
        R(a, 685, 425, 470, 530, 1)
        R(a, 925, 425, 1120, 530, 2, dashed=True)
        L(a, 470, 480, 'Corroborate', 1, 29, 20)
        L(a, 1120, 480, 'Other explanations', 2, 29, 28)
        _foot(a, 'Bound the claim: impact, mechanism, and attribution are distinct.', 'State a Confidence level for the specific claim')

    elif sid == 'S37':
        _document(a, 225, 355, 'Stored packet', 0, 335, 190)
        _document(a, 635, 355, 'Flow records', 1, 335, 190)
        _document(a, 1045, 355, 'Host snapshot', 2, 335, 190)
        for j, word in enumerate(['Fields + lengths', 'Grouped counters', 'Finite resources']):
            L(a, 392+j*410, 625, word, j, 30, 25)
            _draw(a, f'M{392+j*410} 550 V580', j)
        _foot(a, 'Limits: truncation, sampling, byte definitions, and snapshot timing.', 'Known limits belong beside each result')

    elif sid == 'S38':
        _document(a, 220, 350, 'Original source', 0, 300, 160)
        _node(a, 630, 350, 'Units + arithmetic', 1, 330, 160, SOFT)
        _node(a, 1060, 350, 'Bounded finding', 2, 320, 160)
        R(a, 525, 430, 615, 430, 1)
        R(a, 965, 430, 1045, 430, 2)
        _draw(a, 'M370 520 V650 H1215 V520', 3)
        L(a, 800, 695, 'Next check answers the unresolved decision', 3, 30, 61)
        _foot(a, 'A hash detects byte changes; it does not certify the observation.', 'A matching hash does not prove')

    elif sid == 'S39':
        ys = [345, 465, 585]
        left = ['Constrained link', 'Handshake slots', 'Expensive requests']
        right = ['Upstream assistance', 'Protocol-specific defense', 'Application work budget']
        for i, yy in enumerate(ys):
            _node(a, 215, yy, left[i], i, 385, 90, SOFT)
            _node(a, 945, yy, right[i], i, 440, 90)
            R(a, 610, yy+45, 930, yy+45, i)
        _foot(a, 'Protect the constrained resource and verify the learner task.', 'User continuity keeps the response tied')

    elif sid == 'S40':
        _node(a, 215, 355, 'Admission gate', 0, 285, 105, SOFT)
        _node(a, 630, 355, 'Reusable result', 1, 325, 105)
        _node(a, 1070, 355, 'Work deadline', 2, 305, 105)
        R(a, 505, 410, 615, 410, 1)
        R(a, 960, 410, 1055, 410, 2)
        _draw(a, 'M1215 470 V550 H790', 3)
        _node(a, 580, 560, 'Separate critical budgets', 3, 500, 125, SOFT)
        L(a, 330, 635, 'Useful service', 3, 30, 22)
        R(a, 580, 620, 465, 620, 3)
        _foot(a, 'Proposed controls need authorized changes and real validation.', 'Operators would still need authorized configuration changes')

    elif sid == 'S41':
        L(a, 500, 340, 'Proposed change', 0, 35, 31)
        L(a, 1120, 340, 'Real observation', 2, 35, 31)
        _node(a, 215, 395, 'Threshold + expected effect', 1, 555, 160, SOFT)
        _node(a, 835, 395, 'User success + rejection', 2, 550, 160)
        R(a, 775, 470, 820, 470, 1, dashed=True)
        _draw(a, 'M1110 565 V675 H495 V565', 3)
        L(a, 800, 645, 'Revise or reverse when criteria are met', 3, 30, 57)
        _foot(a, 'Generated post-control rows are calculation examples, not deployment proof.', 'In this course, post-control rows are generated examples')

    elif sid == 'S42':
        _document(a, 215, 345, 'Impact + evidence', 0, 330, 180)
        _document(a, 635, 345, 'Owner + request', 1, 330, 180)
        _document(a, 1055, 345, 'Authorized change', 2, 330, 180)
        R(a, 550, 435, 620, 435, 1)
        R(a, 970, 435, 1040, 435, 2)
        _draw(a, 'M1215 535 V650 H380 V535', 3)
        L(a, 800, 700, 'Resource health + learner task', 3, 32, 46)
        _foot(a, 'Offline handoff draft only; no provider contact or live changes.', 'Northstar\'s offline exercise prepares this handoff as a draft')

    else:
        raise ValueError(f'{sid}: scene_art_mid owns S23–S42 only')
    return a

"""Native DNS teaching layers for S37, S38 and S47.

Source: case/EVIDENCE_CARDS.md, E04; lab_mock/dns_answers.pcap.
The short label ``lesson`` denotes lesson.northstar.example.test, type A.
The supplied transaction is 0x4808, with answers 203.0.113.80 and
203.0.113.81.  Paths end at an explicit evidence boundary; they never
establish client acceptance, cache adoption, a later connection or compromise.
"""
from m08_art_common import *


def _g(a, content, name, meaning, when, dx=0, dy=0):
    ident = a.add(
        '<g role="img" aria-label="' + esc(meaning) + '"><title>'
        + esc(meaning) + '</title>' + content + '</g>', name)
    a.show(ident, when, dx=dx, dy=dy)
    return ident


def _draw(a, d, name, meaning, when, color=ACCENT, dash='', duration=1.25):
    ident = a.add(
        '<g role="img" aria-label="' + esc(meaning) + '"><title>'
        + esc(meaning) + '</title>' + path(d, color, dash) + '</g>', name)
    a.moves.append({'target': ident, 'start': when, 'duration': duration,
                    'draw': True, 'dashed': bool(dash)})
    return ident


def _mono(x, y, value, size=34, width=28, anchor='middle', color=INK):
    return '<g font-family="DejaVu Sans Mono">' + text(
        x, y, value, size, width, anchor, color) + '</g>'


def _paper(a, x, y, name, label, when):
    """A requested record, never a checkmark or a completed validation."""
    body = (f'<path d="M{x} {y} H{x+43} L{x+62} {y+19} V{y+58} H{x} Z" '
            f'fill="{WHITE}" stroke="{INK}" stroke-width="3"/>'
            + path(f'M{x+43} {y} V{y+19} H{x+62}', GRAY)
            + path(f'M{x+12} {y+35} H{x+47} M{x+12} {y+48} H{x+39}', GRAY)
            + text(x+77, y+43, label, 30, 20, 'start'))
    return _g(a, body, name, 'Evidence to request: ' + label, when, dy=12)


def S37(a):
    """A query and competing records stop before acceptance evidence."""
    t0 = at(a, 0)
    t_correlate = a.at('For analysis, correlate the question')
    t_accept = at(a, 1)
    t_alternatives = a.at('A different IP address is not enough')
    t_case = at(a, 2)
    t_verify = at(a, 3)
    t_claim = a.at("A packet's source IP is also a claim")

    P(a, 'school_laptop', 240, 427, 180, 0, 'querying-client')
    L(a, 330, 615, 'Client', 0, 34, 14)
    P(a, 'office_server', 1180, 425, 175, 0, 'resolver-role')
    resolver_label = L(a, 1267, 614, 'Resolver role', 0, 30, 19)

    _g(a, rect(480, 310, 600, 90, WHITE, 5), 'question-record',
       'A DNS question carries a name, type and transaction context', t0)
    generic = _g(a, text(780, 346, 'Question name + type', 36, 30)
                 + text(780, 384, 'transaction context', 30, 30),
                 'question-generic', 'Name, type and transaction context', t0)
    R(a, 435, 455, 1150, 455, 0)
    _g(a, text(795, 435, 'query', 30, 20), 'query-label',
       'The DNS query goes from client to resolver role', t0)

    correlate = _g(a, text(790, 786, 'Name / ID / endpoint / time / records', 32, 65),
                   'correlation-fields', 'Correlate all five DNS response fields',
                   t_correlate)
    a.move(correlate, t_alternatives, .35, opacity=0)
    alternative = _g(a, text(790, 786, 'Different IP: check legitimate context', 32, 65),
                     'different-address-context',
                     'A different address alone does not establish poisoning',
                     t_alternatives)
    a.move(alternative, t_case, .35, opacity=0)

    # The dotted edge is deliberately outside the supplied response records.
    # No packet token travels through either recipient-state boundary.
    _draw(a, 'M458 493 V722', 'acceptance-boundary',
          'Client acceptance is outside the supplied packet evidence',
          t_accept, GRAY, '8 10')
    _g(a, f'<circle cx="330" cy="665" r="24" fill="{PAPER}" '
          f'stroke="{INK}" stroke-width="3"/>'
          + text(330, 677, '?', 36, 2)
          + text(330, 719, 'Acceptance?', 30, 16),
       'client-acceptance-open', 'Client acceptance remains unmeasured', t_accept)

    cache = (rect(1170, 657, 185, 24, PAPER, 4)
             + rect(1170, 679, 185, 24, PAPER, 4)
             + rect(1170, 701, 185, 24, PAPER, 4)
             + text(1262, 759, 'Cache adoption?', 30, 19))
    _g(a, cache, 'recursive-cache-open',
       'Recursive cache adoption is a distinct, unmeasured outcome', t_accept, dy=10)

    a.move(generic, t_case, .35, opacity=0)
    _g(a, text(780, 346, 'lesson.northstar.example.test · A', 30, 60)
       + _mono(780, 384, 'transaction 0x4808', 30, 28),
       'fixture-question',
       'E04 question lesson.northstar.example.test, A, transaction 0x4808', t_case)
    a.move(resolver_label, t_case, .35, opacity=0)
    _g(a, text(1267, 614, 'Response endpoint', 30, 20),
       'claimed-response-endpoint',
       'Response endpoint is packet context, not authenticated sender identity', t_case)

    for n, (yy, address) in enumerate(((505, '203.0.113.80'),
                                       (625, '203.0.113.81'))):
        when = t_case + n * .35
        _g(a, rect(540, yy, 525, 88, WHITE, 5)
           + _mono(802, yy+56, 'A → ' + address, 34, 26),
           'supplied-answer-' + str(n+1),
           'Supplied response ' + str(n+1) + ' returns ' + address,
           when, dx=24)
        # The real record reaches the evidence boundary, without entering a cache.
        a.route(1150, yy+20, 1080, yy+44, when)
        _draw(a, f'M540 {yy+44} H470', 'answer-boundary-' + str(n+1),
              'Supplied response stops before an observed acceptance outcome',
              when+.55, ACCENT, '7 9', .8)

    _g(a, text(790, 786, 'Compare approved zone data + resolver logs', 32, 65),
       'expected-record-check',
       'Approved zone data and resolver logs are needed to establish the expected answer',
       t_verify)
    _g(a, text(1262, 333, 'Source IP:', 30, 18)
       + text(1262, 370, 'a packet claim', 30, 19),
       'source-ip-claim', 'A packet source IP does not independently authenticate its sender',
       t_claim)


def S38(a):
    """Orthogonal signed-data validation and transport-protection lanes."""
    t0 = at(a, 0)
    t_no_encrypt = a.at('It does not encrypt the DNS query')
    t_transport = a.at('Encrypted DNS transports protect a communication path')
    t_context = at(a, 1)
    t_complement = at(a, 2)
    t_fixture = a.at("The fixture's conflicting replies are deliberately simple")
    t_verify = at(a, 3)

    _g(a, text(220, 325, 'DNSSEC: signed-data authenticity', 34, 55, 'start'),
       'dnssec-layer-title', 'DNSSEC addresses signed-data origin authentication and integrity', t0)
    signed = (f'<path d="M250 365 H432 L465 397 V477 H250 Z" fill="{WHITE}" '
              f'stroke="{INK}" stroke-width="4"/>'
              + path('M432 365 V397 H465', GRAY)
              + text(357, 411, 'A record', 34, 12)
              + path('M276 448 C291 422 298 467 312 440 C326 420 332 458 348 442', ACCENT)
              + f'<circle cx="423" cy="448" r="15" fill="{SOFT}" '
                f'stroke="{INK}" stroke-width="3"/>'
              + text(357, 514, 'Signed DNS data', 32, 20))
    _g(a, signed, 'signed-dns-record', 'A signed DNS data record, represented conceptually', t0, dy=12)
    R(a, 485, 421, 1115, 421, 0)
    for j, xx in enumerate((610, 795, 980)):
        _g(a, f'<circle cx="{xx}" cy="421" r="19" fill="{SOFT}" '
              f'stroke="{INK}" stroke-width="3"/>',
           'trust-chain-link-' + str(j),
           'A link in the conceptual DNSSEC validation chain', t0+.25*j)
    _g(a, text(795, 382, 'Validation chain + policy', 30, 34),
       'validation-prerequisites', 'Validation requires the chain and supporting policy', t0)

    shield = (f'<path d="M1160 367 L1225 348 L1290 367 V418 '
              f'C1290 456 1250 480 1225 492 C1200 480 1160 456 1160 418 Z" '
              f'fill="{SOFT}" stroke="{INK}" stroke-width="4"/>'
              + _mono(1225, 426, 'SIG', 32, 5)
              + text(1225, 527, 'Validation', 32, 18))
    _g(a, shield, 'signed-data-validator',
       'A validator checks signed data; no validation result is asserted', t0, dy=12)

    no_encrypt = _g(a, text(790, 560, 'DNSSEC does not encrypt query contents', 30, 70),
                    'dnssec-query-visibility', 'DNSSEC does not provide query encryption',
                    t_no_encrypt)
    a.move(no_encrypt, t_context, .35, opacity=0)
    context = _g(a, text(790, 560, 'Resolver trust · endpoint settings · validation · zone', 30, 74),
                 'control-context',
                 'Resolver trust, endpoint state, validation and zone state still matter',
                 t_context)
    a.move(context, t_verify, .35, opacity=0)

    _draw(a, 'M220 580 H1390', 'separate-control-layers',
          'Signed-data validation and transport protection are separate layers',
          t_transport, GRAY)
    _g(a, text(220, 620, 'Encrypted DNS: path confidentiality', 34, 55, 'start'),
       'transport-layer-title', 'Encrypted DNS protects a communication path to a resolver',
       t_transport)
    client = a.prop('school_laptop', 250, 642, 130, 'encrypted-path-client')
    a.show(client, t_transport, dy=12)
    resolver = a.prop('office_server', 1220, 634, 130, 'encrypted-path-resolver')
    a.show(resolver, t_transport, dy=12)
    _g(a, text(315, 782, 'Client', 30, 12)
       + text(1285, 782, 'Chosen resolver', 30, 20),
       'transport-endpoints', 'The protected path terminates at the chosen resolver', t_transport)
    _g(a, rect(440, 655, 680, 64, SOFT, 30), 'encrypted-tunnel',
       'Conceptual encrypted transport between client and resolver', t_transport)
    # The token stays within the path; it never becomes a correctness verdict.
    a.route(455, 687, 1105, 687, t_transport+.25)
    lock = (f'<path d="M773 663 V652 C773 625 813 625 813 652 V663" '
            f'fill="none" stroke="{INK}" stroke-width="4"/>'
            + rect(764, 663, 58, 45, WHITE, 7)
            + f'<circle cx="793" cy="680" r="5" fill="{INK}"/>'
            + path('M793 685 V694', INK))
    _g(a, lock, 'transport-lock', 'Encryption protects this communication path', t_transport+.3)
    _g(a, text(790, 759, 'Protected path to the resolver', 30, 46),
       'transport-scope', 'Transport confidentiality does not establish every answer is correct',
       t_transport)

    # A bracket joins the two independent scopes only when narration names complementarity.
    _draw(a, 'M1350 421 H1390 V687 H1350', 'complementary-controls-bracket',
          'The controls can complement one another without being equivalent',
          t_complement, GRAY)
    _g(a, f'<circle cx="1390" cy="555" r="20" fill="{WHITE}" '
          f'stroke="{INK}" stroke-width="3"/>'
          + text(1390, 566, '+', 34, 2),
       'complementary-controls-plus', 'Complementary controls have distinct protection scopes',
       t_complement)

    _g(a, text(790, 800, 'Fixture: no validation run or encrypted session claimed', 30, 76),
       'control-tests-unperformed',
       'No DNSSEC validation run or encrypted DNS session is claimed for the fixture',
       t_fixture)
    _g(a, text(790, 560, 'Verify resolver, policy, validation, expected record and client behavior', 30, 79),
       'verification-state-request',
       'Record actual resolver, policy, validation state, expected record and client behavior',
       t_verify)


def S47(a):
    """Correlate the E04 bytes and keep the resulting verdict bounded."""
    t0 = at(a, 0)
    t_correlate = a.at('Compare the question, transaction identifier, endpoints, and answer data')
    t_conflict = at(a, 1)
    t_open = a.at('They do not show which answer entered a cache')
    t_request = at(a, 2)
    t_recommend = at(a, 3)

    _g(a, rect(235, 305, 1130, 106, SOFT, 5)
       + _mono(800, 351, 'E04 · QUERY  lesson · A  /  ID 0x4808', 34, 48),
       'e04-query-record',
       'E04 query for lesson.northstar.example.test, type A, transaction 0x4808', t0, dy=12)
    _g(a, text(800, 393, 'Cache adoption, later connection and compromise: unmeasured', 30, 76),
       'e04-outcome-boundary',
       'The bytes do not establish cache adoption, later application connection or compromise',
       t_open)

    widths = (210, 310, 230, 380)
    centers = (340, 600, 870, 1175)
    for j, label in enumerate(('Message', 'Question / type', 'Transaction', 'Returned A')):
        _g(a, text(centers[j], 440, label, 30, 24), 'e04-column-' + str(j),
           'Comparison field: ' + label, t0)

    for n, (yy, address) in enumerate(((459, '203.0.113.80'),
                                      (562, '203.0.113.81'))):
        when = t0 + .3*n
        body = rect(235, yy, 1130, 85, WHITE, 5)
        xx = 235
        for cw in widths[:-1]:
            xx += cw
            body += path(f'M{xx} {yy+11} V{yy+74}', GRAY)
        body += (text(340, yy+54, 'Response ' + str(n+1), 32, 14)
                 + text(600, yy+54, 'lesson · A', 34, 17)
                 + _mono(870, yy+54, '0x4808', 34, 10)
                 + _mono(1175, yy+54, address, 34, 17))
        _g(a, body, 'e04-response-' + str(n+1),
           'Matching question and transaction, response ' + str(n+1) + ' returns ' + address,
           when, dx=24)

    # Brackets compare fields; they are not arrows into a client or cache.
    _draw(a, 'M460 452 V444 H970 V452 M460 653 V665 H970 V653',
          'e04-matching-context-bracket',
          'Both supplied responses match the classroom question and transaction identifier',
          t_correlate, GRAY)
    _g(a, text(715, 705, 'Matching question + ID', 32, 31),
       'e04-matching-context', 'The question and transaction match in the supplied response set',
       t_correlate)
    for n, yy in enumerate((459, 562)):
        _draw(a, f'M1000 {yy+7} H1353 V{yy+77} H1000 Z',
              'e04-answer-difference-' + str(n+1),
              'Different returned address in supplied response ' + str(n+1),
              t_conflict+.15*n, ACCENT, duration=.8)
    _draw(a, 'M1175 650 V667', 'e04-conflict-pointer',
          'The supported observation is a conflict in the supplied answers', t_conflict)
    _g(a, text(1175, 705, 'Different A records', 32, 25),
       'e04-supported-conflict', 'The packet bytes establish conflicting supplied answers',
       t_conflict)

    _paper(a, 250, 742, 'e04-request-resolver', 'Resolver policy', t_request)
    _paper(a, 650, 742, 'e04-request-zone', 'Zone state', t_request)
    _paper(a, 1045, 742, 'e04-request-client', 'Client behavior', t_request)
    _draw(a, 'M250 806 H1380', 'e04-recommendation-prerequisites',
          'A DNS recommendation follows the supported weakness and these evidence prerequisites',
          t_recommend, ACCENT)


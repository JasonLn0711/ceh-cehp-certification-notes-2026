#!/usr/bin/env python3
"""Construct inert Northstar teaching artifacts. No mail, calls, DNS or services."""
from pathlib import Path
from email.message import EmailMessage
from email import policy
import csv, hashlib, json, sys

R = Path(__file__).resolve().parents[1]
local_deps = R.parent.parent / '.tool-deps'
if local_deps.exists():
    sys.path.insert(0, str(local_deps))
import qrcode
import qrcode.image.svg

LABEL = 'SIMULATED OUTPUT'
D = R / 'lab_mock'
D.mkdir(exist_ok=True)
def write(name, text):
    p = D / name
    p.write_text(text, encoding='utf-8')
def dump(name, value):
    write(name, json.dumps({'label': LABEL, **value}, indent=2) + '\n')
def table(name, rows):
    with (D / name).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader(); w.writerows(rows)

m = EmailMessage(policy=policy.SMTP)
m['From'] = 'Cedar Teaching Supplies <supplier@cedar.example.test>'
m['To'] = 'Northstar Finance <finance@northstar.example.test>'
m['Reply-To'] = 'supplier@cedar.example.test'
m['Subject'] = '[SIMULATED OUTPUT] Supplier change request for review'
m['Date'] = 'Mon, 12 Oct 2026 09:00:00 +0800'
m['Message-ID'] = '<e01-training-only@cedar.example.test>'
m['X-Training-Label'] = LABEL
m['Authentication-Results'] = ('mail.northstar.example.test; spf=pass '
    'smtp.mailfrom=cedar.example.test; dkim=pass header.d=cedar.example.test; '
    'dmarc=pass header.from=cedar.example.test')
m.set_content('SIMULATED OUTPUT — inert classroom artifact.\n\n'
    'Please review a proposed supplier destination change to TRAINING-ACCOUNT-02. '
    'The request says a lesson deadline is approaching and supplies +1 202 555 0177 '
    'for confirmation. This is not an actual payment instruction. '
    'Use the approved supplier and finance process before any sensitive action.\n')
(D / 'E01_supplier_message.eml').write_bytes(m.as_bytes())
dump('E01_supplier_record.json', {'case_id': 'E01', 'supplier_id': 'CEDAR-TRAINING',
    'expected_mailbox': 'supplier@cedar.example.test', 'approved_contact': '+1 202 555 0144',
    'approved_destination': 'TRAINING-ACCOUNT-01', 'owner_role': 'Finance verification owner',
    'record_status': 'stipulated approved training record'})
dump('E01_payment_ticket.json', {'case_id': 'E01', 'ticket_id': 'FIN-TRAINING-01',
    'requested_destination': 'TRAINING-ACCOUNT-02', 'provided_contact': '+1 202 555 0177',
    'change_status': 'held_pending_independent_verification', 'transaction_record_supplied': False,
    'receiver_results': 'stipulated synthetic strings; no SPF/DKIM/DMARC execution',
    'account_compromise': 'unknown', 'supplier_authorization': 'unconfirmed'})
write('E02_call_transcript.md', '# Fictional call transcript\n\nSIMULATED OUTPUT. '
    'Authored text, not a real call or generated voice recording.\n\n'
    'Caller claims to be STAFF-TRAINING-07 and asks for an authenticator reset before a lesson. '
    'Caller mentions a campus schedule and supplies +1 202 555 0177 for a callback. '
    'Eli records the request and routes it to the approved recovery process. '
    'No verification, reset or account use is established by this transcript.\n')
dump('E02_directory_record.json', {'case_id': 'E02', 'staff_id': 'STAFF-TRAINING-07',
    'established_contact': '+1 202 555 0133', 'recovery_owner': 'Authorized identity-service team',
    'identity_evidence': 'must follow approved recovery policy; public facts are insufficient'})
dump('E02_recovery_ticket.json', {'case_id': 'E02', 'ticket_id': 'ID-TRAINING-02',
    'status': 'pending_verification', 'provided_contact': '+1 202 555 0177',
    'identity_verified': False, 'reset_event_supplied': False, 'session_event_supplied': False,
    'next_action': 'Authorized owner verifies identity and checks actual account-state records'})
url = 'https://learn-check.northstar.example.test/review'
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4, box_size=10)
qr.add_data(url); qr.make(fit=True)
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(D / 'E03_qr_code.svg')
dump('E03_qr_payload.json', {'case_id': 'E03', 'encoded_text': url,
    'encoder': 'qrcode 8.2', 'matrix_width_including_border': len(qr.get_matrix()),
    'decoder_execution': 'not_exercised; encoded source and matrix construction are recorded',
    'destination_service': 'not provided', 'link_interaction': 'unmeasured',
    'credential_submission': 'unmeasured'})
dump('E03_portal_context.json', {'case_id': 'E03', 'known_portal': 'https://learn.northstar.example.test',
    'notice_owner': 'Learning announcement team', 'notice_approval': 'unconfirmed',
    'reporting_route': 'Known campus support directory; not a link in the notice'})
write('E03_notice.md', '# Lesson review notice\n\nSIMULATED OUTPUT. A constructed Northstar-themed '
    'notice asks learners to use the accompanying QR image for a review. Approval is unconfirmed. '
    'The reserved test destination has no supplied sign-in service. No scans, page loads, '
    'submissions or account use are asserted.\n')
dump('E04_appointments.json', {'case_id': 'E04', 'date': '2026-10-12',
    'appointments': [{'id': 'VISIT-TRAINING-01', 'time': '11:00+08:00', 'escort_role': 'Mara',
                      'visitor_role': 'Approved classroom maintenance visit'}],
    'claimed_0900_visit': 'not confirmed in supplied list',
    'limits': 'List absence alone does not establish intent or the complete approval state'})
table('E04_door_events.csv', [{'label': LABEL, 'case_id': 'E04',
    'event_id': 'DOOR-TRAINING-01', 'time': '2026-10-12T09:05:00+08:00',
    'door': 'OFFICE-TRAINING', 'credential': 'BADGE-TRAINING-21',
    'result': 'credential_presented_door_open', 'held_seconds': 15,
    'entrant_count': 'unknown', 'person_attribution': 'not_established'}])
write('E04_witness_report.md', '# Unverified witness report\n\nSIMULATED OUTPUT. '
    'A fictional witness reports someone following an employee through the office door. '
    'The report is a lead; no independent entrant count, identification or video is supplied. '
    'Use authorized reception, appointment, escort and safety procedures.\n')
rows = []
for i in range(1, 21):
    rows.append(dict(label=LABEL, case_id='METRICS', participant=f'SIM-{i:03}', eligible=True,
        delivery='failed' if i > 18 else 'delivered',
        link_actor='automated_scanner' if i == 6 else 'stipulated_learner' if i <= 5 else 'none',
        reported=i in (2, 4, 9, 12), difficulty='one_constructed_scenario'))
table('assessment_metrics.csv', rows)
files = sorted(p for p in D.iterdir() if p.is_file() and p.name != 'fixture_manifest.json')
manifest = {'label': LABEL, 'scope': 'Generated inert files only; no contacts, sending, DNS, services or targets.',
    'fictional_time_context': '2026-10-12 Asia/Taipei; not actual collection or build time',
    'phone_numbers': 'Fictional North American 555-01xx teaching numbers; no call is made.',
    'files': [{'path': p.name, 'bytes': p.stat().st_size,
               'sha256': hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
write('fixture_manifest.json', json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'stage': 'inert_evidence_built', 'artifact_files': len(files),
    'fictional_assessment_rows': 20, 'live_activity': False}))

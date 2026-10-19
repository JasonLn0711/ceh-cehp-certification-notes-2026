#!/usr/bin/env python3
"""Measure synthetic files offline. --record is the only persistent operation."""
from pathlib import Path
from email.parser import BytesParser
from email import policy
import argparse, csv, datetime, hashlib, json, sys

R = Path(__file__).resolve().parents[1]; D = R / 'lab_mock'
checks = []
def check(name, condition): checks.append({'name': name, 'passed': bool(condition)})
def load(name): return json.loads((D / name).read_text())
manifest = load('fixture_manifest.json')
for f in manifest['files']:
    p = D / f['path']
    check('file_identity:' + f['path'], p.is_file() and p.stat().st_size == f['bytes'] and
          hashlib.sha256(p.read_bytes()).hexdigest() == f['sha256'])
m = BytesParser(policy=policy.default).parsebytes((D / 'E01_supplier_message.eml').read_bytes())
supplier = load('E01_supplier_record.json'); payment = load('E01_payment_ticket.json')
check('email_label', m['X-Training-Label'] == 'SIMULATED OUTPUT')
check('expected_from_address', m['From'].addresses[0].addr_spec == supplier['expected_mailbox'])
check('reserved_sender_domain', m['From'].addresses[0].domain.endswith('.example.test'))
check('authentication_result_stipulation', 'dmarc=pass' in m['Authentication-Results'] and
      'no SPF/DKIM/DMARC execution' in payment['receiver_results'])
check('changed_destination', payment['requested_destination'] != supplier['approved_destination'])
check('callback_not_independent', payment['provided_contact'] != supplier['approved_contact'])
check('payment_not_supplied', payment['transaction_record_supplied'] is False)
check('payment_held', payment['change_status'] == 'held_pending_independent_verification')
recovery = load('E02_recovery_ticket.json'); directory = load('E02_directory_record.json')
check('pending_recovery', recovery['status'] == 'pending_verification')
check('recovery_contact_difference', recovery['provided_contact'] != directory['established_contact'])
check('reset_and_session_unmeasured', not recovery['reset_event_supplied'] and not recovery['session_event_supplied'])
qr = load('E03_qr_payload.json'); portal = load('E03_portal_context.json')
check('qr_reserved_destination', qr['encoded_text'].startswith('https://') and '.example.test/' in qr['encoded_text'])
check('qr_differs_from_known_portal', not qr['encoded_text'].startswith(portal['known_portal'] + '/'))
check('qr_decoder_boundary', qr['decoder_execution'].startswith('not_exercised'))
check('no_collection_service', qr['destination_service'] == 'not provided')
door = list(csv.DictReader((D / 'E04_door_events.csv').open()))
check('one_badge_event', len(door) == 1 and door[0]['result'] == 'credential_presented_door_open')
check('entrants_not_inferred', door[0]['entrant_count'] == 'unknown' and door[0]['person_attribution'] == 'not_established')
rows = list(csv.DictReader((D / 'assessment_metrics.csv').open()))
eligible = len(rows); delivered = sum(x['delivery'] == 'delivered' for x in rows)
interactions = sum(x['link_actor'] != 'none' for x in rows)
learner = sum(x['link_actor'] == 'stipulated_learner' for x in rows)
automated = sum(x['link_actor'] == 'automated_scanner' for x in rows)
reports = sum(x['reported'] == 'True' for x in rows)
check('metric_population', eligible == 20 and delivered == 18)
check('metric_actor_separation', interactions == 6 and learner == 5 and automated == 1)
check('metric_reports', reports == 4)
check('metric_no_events_on_failed_delivery', all(x['link_actor'] == 'none' and x['reported'] == 'False' for x in rows if x['delivery'] == 'failed'))
check('fixture_labels', all(x['label'] == 'SIMULATED OUTPUT' for x in rows + door))
result = {'stage': 'offline_synthetic_evidence_verification',
    'verified_at': datetime.datetime.now().astimezone().isoformat(),
    'python': sys.version.split()[0], 'passed': sum(x['passed'] for x in checks),
    'failed': sum(not x['passed'] for x in checks), 'checks': checks,
    'parsed_email': {'from': str(m['From']), 'reply_to': str(m['Reply-To']),
        'subject': str(m['Subject']), 'authentication_results': str(m['Authentication-Results'])},
    'metric_counts': {'eligible': eligible, 'delivered': delivered, 'link_events': interactions,
        'stipulated_learner_events': learner, 'automated_events': automated, 'reports': reports},
    'measurement_boundary': 'Actual local bytes, parsing and arithmetic. All campus events and participant rows are fictional. No mail authentication, QR decoder, live delivery, contacts, account changes or physical tests executed.'}
args = argparse.ArgumentParser(); args.add_argument('--record', action='store_true'); args = args.parse_args()
if args.record:
    (R / 'validation').mkdir(exist_ok=True)
    (R / 'validation/evidence_qa.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2)); raise SystemExit(bool(result['failed']))

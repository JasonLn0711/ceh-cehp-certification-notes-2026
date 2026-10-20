"""Versioned English timing contracts. Mandarin has its own policy owner."""
from .common import digest

LEGACY = dict(id='ceh-en-v1.0', sample_rate=48000, channels=2, fps=30,
              atempo=1.5, opening=24000, gap=8640, ending=144000, quiz=48000)
CURRENT = dict(id='ceh-en-v1.1', sample_rate=48000, channels=2, fps=30,
               atempo=1.4, opening=14400, gap=9600, ending=24000, quiz=48000)
V12 = dict(CURRENT, id='ceh-en-v1.2', gap=14400, chapter_gap=38400)
POLICIES = {p['id']: p for p in (LEGACY, CURRENT, V12)}


def modern(profile):
    """Resolve first: unknown policies must never bypass modern safety gates."""
    identifier = profile.get('audio_policy', LEGACY['id'])
    if identifier not in POLICIES:
        raise ValueError('Unknown audio policy: '+str(identifier))
    return identifier != LEGACY['id']


def timing(profile):
    if profile.get('schema_version') == 2:
        raise ValueError('English timing cannot be applied to a Mandarin profile')
    identifier = profile.get('audio_policy', LEGACY['id'])
    if identifier not in POLICIES:
        raise ValueError('Unknown audio policy: '+str(identifier))
    result = dict(POLICIES[identifier])
    if profile['voice']['atempo'] != result['atempo'] or profile['voice']['speed_applications'] != 1:
        raise ValueError('Voice processing disagrees with audio policy')
    return result


def fingerprint(profile):
    return digest(timing(profile))

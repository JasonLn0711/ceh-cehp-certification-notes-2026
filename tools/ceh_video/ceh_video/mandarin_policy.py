"""Versioned Mandarin PCM timing. Missing policy preserves the first film."""
LEGACY = 'zh-TW-legacy-v1'
CONCEPTS = 'zh-TW-concepts-v2'
CONCEPTS_13 = 'zh-TW-concepts-v3-1p3'

def voice_rate(profile):
    return 1.3 if profile.get('audio_policy') == CONCEPTS_13 else 1.5

def timing(profile):
    name = profile.get('audio_policy', LEGACY)
    assert name in (LEGACY, CONCEPTS, CONCEPTS_13), 'Unknown Mandarin audio policy'
    modern = name in (CONCEPTS, CONCEPTS_13)
    expected = .45 if modern else 1
    assert profile['quiz_silence_seconds'] == expected
    return {'version': name, 'opening_samples': 4800 if modern else 24000,
            'sentence_gap_samples': 8640, 'tail_samples': 9600 if modern else 144000,
            'chapter_tail_samples': 16800 if modern else 144000,
            'quiz_samples': 21600 if modern else 48000,
            'chapter_gap_samples': 21600 if modern else None}

def tail_samples(p, scene):
    policy = timing(p.profile)
    chapter = p.chapter_scenes(scene['chapter_id'])
    return policy['chapter_tail_samples'] if chapter[-1]['id'] == scene['id'] else policy['tail_samples']

def deck_filename(profile):
    return profile.get('deck_filename', 'Digital_Everyday_Masterclass_zh-TW_EDITABLE.pptx')

def archive_prefix(profile):
    prefix = profile.get('archive_prefix', 'Digital_Everyday_Masterclass_zh-TW_v1').rstrip('/')
    assert prefix and '/' not in prefix and '\\' not in prefix and prefix not in ('.', '..')
    return prefix + '/'

def chapter_gap_rows(p):
    """Measure explicit padding between complete spoken clips, excluding TTS prosody."""
    policy = timing(p.profile); rows = []
    for before, after in zip(p.chapters, p.chapters[1:]):
        left = p.audio(p.chapter_scenes(before)[-1]['id'])
        right = p.audio(p.chapter_scenes(after)[0]['id'])
        last = next(s for s in reversed(left['segments']) if s['kind'] == 'spoken')
        first = next(s for s in right['segments'] if s['kind'] == 'spoken')
        frames = left['samples'] - last['end_sample'] + first['start_sample']
        target = policy['chapter_gap_samples']
        if target is not None:
            assert target <= frames < target + 1600, (before, after, frames, target)
        rows.append({'before': before, 'after': after, 'added_silence_samples': frames,
                     'added_silence_seconds': frames / 48000, 'target_samples': target,
                     'scope': 'Explicit padding; natural provider clip silence retained'})
    return rows

def duration_limit(profile):
    default = 1800 if timing(profile)['version'] in (CONCEPTS, CONCEPTS_13) else float('inf')
    return min(profile.get('max_duration_seconds', default), default)

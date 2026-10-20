"""Chapter pauses reference existing scene buffers; never insert another pause."""
from .audio_policy import timing


def chapter_boundaries(p):
    contract = timing(p.profile)
    rows = []
    cursor = 0
    previous = None
    for scene in p.scenes:
        audio = p.audio(scene['id'])
        if previous and previous[0]['chapter_id'] != scene['chapter_id']:
            prior, data, start = previous
            ending = next(x for x in data['ledger'] if x['kind'] == 'ending')
            opening = audio['ledger'][0]
            assert opening['kind'] == 'opening' and opening['start_sample'] == 0
            tail = data['ledger'][data['ledger'].index(ending)+1:]
            assert all(x['kind'] == 'frame_alignment' for x in tail)
            padding = sum(x['end_sample']-x['start_sample'] for x in tail)
            named = ending['end_sample']-ending['start_sample']+opening['end_sample']
            assert named == contract.get('chapter_gap', contract['ending']+contract['opening'])
            rows.append({
                'from_chapter': prior['chapter_id'], 'to_chapter': scene['chapter_id'],
                'from_scene': prior['id'], 'to_scene': scene['id'],
                'start_sample': start+ending['start_sample'],
                'end_sample': cursor+opening['end_sample'],
                'named_pause_frames': named, 'frame_alignment_frames': padding,
                'actual_interval_frames': named+padding,
                'components': ['previous.ending', 'next.opening'],
                'additional_inserted_frames': 0,
            })
        previous = (scene, audio, cursor)
        cursor += audio['samples']
    assert len(rows) == len(p.chapters)-1
    return rows

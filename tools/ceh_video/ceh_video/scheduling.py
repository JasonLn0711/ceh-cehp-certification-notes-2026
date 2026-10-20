"""Longest estimated chapter first; presentation order remains unchanged."""
from .common import read


def render_order(p, names):
    def estimate(name):
        chapter = name.split(':', 1)[1]
        frames = sum(p.audio(s['id'])['samples']//1600 for s in p.chapter_scenes(chapter))
        receipt = p.qa/(chapter+'-render.json')
        if receipt.exists():
            r = read(receipt)
            # History is useful only for the same worker/renderer configuration.
            if r.get('render_configuration') == p.profile['runtime']:
                video = next(s for s in r['probe']['streams'] if s['codec_type'] == 'video')
                return frames*r['elapsed_seconds']/int(video['nb_read_frames'])
        return frames
    return sorted(names, key=lambda name: (-estimate(name), name))

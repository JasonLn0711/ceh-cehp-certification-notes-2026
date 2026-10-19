"""Dispatch all newly authored M10 semantic diagrams; quizzes use their own pages."""
import scene_art_start,scene_art_mid,scene_art_end
def build(scene,audio):
    number=int(scene['id'][1:])
    if number<=22:return scene_art_start.render(scene,audio)
    if number<=42:return scene_art_mid.render(scene,audio)
    if number<=49 or number==58:return scene_art_end.render(scene,audio)
    raise ValueError(('Quiz scenes are built by the question renderer',scene['id']))

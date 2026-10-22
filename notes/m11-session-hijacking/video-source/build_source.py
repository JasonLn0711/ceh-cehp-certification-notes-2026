"""Compile original module copy and coordinate-free diagrams; no media generation."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parent
def write(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
figure_notes={
 'Four different failures':'Four mechanisms: theft, prediction, fixation and replay',
 'Time has two meanings':'Two independent lifetime limits • both enforced by the server',
 'Sequence numbers describe bytes':'Toy interval [1000, 2000): 1100 inside; 3000 outside • not full TCP validation',
 'A timeline without secrets':'Synthetic events: 1 login → 2 old denied → 3 fresh allowed → 5 logout → 6 denied',
 'Compare flawed and corrected rotation':'Offline assertion: known old label allowed before repair; denied after rotation',
 'Logout must withdraw authority':'Acceptance check: fresh label allowed → logout → same label denied',
 'Regression tests preserve boundaries':'Positive: own resource allowed • Negative: another owner denied',
 'Verify containment and recovery':'Three checks: old denied • new authorized path works • exposure repaired',
 "Validate the token's meaning":'Independent checks: protection • issuer/audience • lifetime/purpose',
 'Secure and HttpOnly differ':'Secure: transport • HttpOnly: script access • authorization: server decision',
}
figure_labels={
 'Four different failures':['Obtain: theft / prediction','Choose: fixation','Reuse: replay'],
 'Sequence numbers describe bytes':['Byte position: 1100','Acknowledgment: 1000','Window: [1000, 2000)'],
 'A timeline without secrets':['Events 1–6','Symbolic session','Allowed / denied'],
}
scenes=[];specs={};cues={};chapters={};sid=0
for block in re.split(r'^# ',(ROOT/'lesson.txt').read_text(),flags=re.M)[1:]:
 header,*parts=re.split(r'^## ',block,flags=re.M);ch,chapter=header.strip().split(' | ');chapters[ch]=chapter
 for part in parts:
  head,body=part.split('\n',1);title,labels,assets=head.split(' | ');paragraphs=[p.strip() for p in body.strip().split('\n') if p.strip()]
  sid+=1;ident=f'S{sid:02}'; labels=labels.split(';');assets=assets.split(';');assert len(paragraphs)==len(labels)==len(assets)==3
  narration=' '.join(paragraphs)
  scene=dict(id=ident,chapter_id=ch,chapter_title=chapter,title=title,tags=['M11','Session Hijacking','simulated'],on_screen_copy=labels,narration_en_US=narration,audio_segments=[dict(kind='spoken',text=narration)],estimated_spoken_words=len(narration.split()),notes='Original educational scenario; final timing from measured PCM',review_requirements=['8% bottom safe area','source-bound semantics','exact narration timing'])
  scenes.append(scene);cues[ident]=[p.split('.')[0] for p in paragraphs]
  nodes=[dict(id=f'n{i}',label=label,cue=i,kind='device',asset=asset,assetProvenance='Approved M10 editorial prop; inherited immutable hash in production.json') for i,(label,asset) in enumerate(zip(figure_labels.get(title,labels),assets))]
  # Only causal/ordered explanations receive arrows; comparisons remain parallel.
  flow=ch in ('C01','C02','C03','C06','C09','C11') and title not in ('Four different failures','Time has two meanings')
  specs[ident]=dict(template='flow' if flow else 'comparison',nodes=nodes,edges=[{'from':f'n{i}','to':f'n{i+1}','cue':i+1,'dashed':False} for i in range(2)] if flow else [],note=figure_notes.get(title,'Fictional Northstar example • interpret the stated boundary'),provenance='Original module-owned lesson.txt: '+title)
# Move synthesis after the eight questions, retaining sequential presentation IDs.
teaching=[s for s in scenes if s['chapter_id']!='C11'];closing=[s for s in scenes if s['chapter_id']=='C11'];questions=[]
quiz_start=len(teaching)
for i,q in enumerate(json.loads((ROOT/'authoring-questions.json').read_text()),1):
 ident=f'S{quiz_start+i:02}';choices=[dict(letter=k,text=v) for k,v in zip('ABCD',q['options'])]
 before=q['prompt']+' '+' '.join(f'{c["letter"]}. {c["text"]}.' for c in choices)
 after=f'The correct answer is {q["answer"]}. '+q['explanation']
 questions.append(dict(id=f'Q{i:02}',scene_id=ident,level='Application',prompt=q['prompt'],choices=choices,correct_letter=q['answer'],silent_think_seconds=1,explanation=q['explanation']))
 teaching.append(dict(id=ident,chapter_id='C10',chapter_title='Eight questions',title=f'Question {i}: check the boundary',tags=['M11','quiz'],on_screen_copy=[],narration_en_US=before+' '+after,audio_segments=[dict(kind='spoken',text=before),dict(kind='silence',seconds=1),dict(kind='spoken',text=after)],estimated_spoken_words=len((before+' '+after).split()),notes='Read all options before exact 48000-frame hold'))
# Normalize presentation IDs after inserting the quiz chapter.
allscenes=teaching+closing;new_specs={};new_cues={}
for i,s in enumerate(allscenes,1):
 old=s['id'];s['id']=f'S{i:02}'
 if s['chapter_id']!='C10':new_specs[s['id']]=specs[old];new_cues[s['id']]=cues[old]
for i,q in enumerate(questions):q['scene_id']=f'S{37+i:02}'
assert len(allscenes)==48 and len(new_specs)==40
write('scenes.json',dict(title='CEH Module 11: Session Hijacking — Northstar Session Lab',version='1.0',language='en-US',scene_count=48,question_count=8,estimated_spoken_words=sum(len(s['narration_en_US'].split()) for s in allscenes),status='source_ready',narration_speed_multiplier=1.4,voice=dict(engine='Kokoro',voice='af_heart',baseline_speed=.73,postprocess='exactly one atempo=1.4 on spoken clips'),scenes=allscenes))
write('quiz.json',dict(language='en-US',namespace='M11-film-v1',question_count=8,silent_think_seconds_each=1,questions=questions));write('scene-specs.json',new_specs);write('cues_m11.json',new_cues)
print('scenes',len(allscenes),'words',sum(len(s['narration_en_US'].split()) for s in allscenes))

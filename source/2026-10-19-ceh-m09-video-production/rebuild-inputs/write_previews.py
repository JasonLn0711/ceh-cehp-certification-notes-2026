from pathlib import Path
import html,json
R=Path(__file__).resolve().parents[1];S=json.loads((R/'scenes.json').read_text())['scenes']
css="body{margin:36px;background:#F0EBE4;color:#292421;font:18px Arial}h1{font-size:38px}section{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}article{background:#FFFAF3;border:2px solid #292421;padding:14px}img{width:100%;height:auto}a{color:#292421}p{line-height:1.5}"
text='<!doctype html><html lang="en-US"><meta charset="utf-8"><title>M09 visual source browser</title><style>'+css+'</style><h1>CEH M09: Social Engineering</h1><p>Editable source boards and actual deck export; final film has separate production evidence.</p><p><a href="../examples/index.html">Four draggable animation references</a> · <a href="../SCRIPT_en-US.md">Complete narration</a> · <a href="../slides/CEH_M09_Editable_Visual_Lookbook_18slides.pptx">Editable deck</a> · <a href="../slides/CEH_M09_Editable_Visual_Lookbook_18slides.pdf">Actual PDF</a></p><h2>All58scene boards</h2><section>'
for s in S:text+='<article><a href="../boards/'+s['id']+'.svg"><img src="boards/'+s['id']+'.png" alt="'+html.escape(s['title'])+'"></a><p>'+s['id']+' · '+html.escape(s['title'])+'. Editable composition for this lesson mechanism.</p></article>'
text+='</section><h2>18editable visual slides</h2><section>'
for i in range(1,19):text+=f'<article><img src="slides/slide-{i:02}.png" alt="Visual slide {i}"><p>Slide {i}: actual LibreOffice export of editable source objects.</p></article>'
text+='</section></html>';(R/'previews').mkdir(exist_ok=True);(R/'previews/index.html').write_text(text)

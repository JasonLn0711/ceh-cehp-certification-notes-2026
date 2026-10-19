#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import json
R=Path(__file__).resolve().parents[1];font=ImageFont.truetype(str(R/'assets/fonts/LiberationSans-Regular.ttf'),20)
for kind,source in [('boards',R/'previews/boards'),('slides',R/'previews/slides')]:
 files=sorted(source.glob('*.png'));assert len(files)==(58 if kind=='boards' else 18),(kind,len(files))
 for start in range(0,len(files),20):
  group=files[start:start+20];out=Image.new('RGB',(1600,math_height:=((len(group)+3)//4)*255),'#F0EBE4');d=ImageDraw.Draw(out)
  for j,p in enumerate(group):
   im=Image.open(p).convert('RGB');im.thumbnail((390,220));x=(j%4)*400;y=(j//4)*255;out.paste(im,(x,y));d.text((x+8,y+225),p.stem,fill='#292421',font=font)
  out.save(R/f'previews/{kind}-contact-{start//20+1:02}.jpg',quality=90)
# A full local gallery; thumbnails link to native SVG or actual exported slide images.
scenes=json.loads((R/'scenes.json').read_text())['scenes'];cards=''.join(f'<a href="../boards/{s["id"]}.svg"><img loading="lazy" src="boards/{s["id"]}.png" alt="{s["id"]}"><span>{s["id"]} · {s["title"]}</span></a>' for s in scenes)
slides=''.join(f'<a href="slides/{p.name}"><img loading="lazy" src="slides/{p.name}" alt="{p.stem}"><span>{p.stem}</span></a>' for p in sorted((R/'previews/slides').glob('*.png')))
(R/'previews/index.html').write_text('<!doctype html><html lang="en-US"><meta charset="utf-8"><title>M10 visual source browser</title><style>body{font:18px Arial;background:#F0EBE4;color:#292421;margin:40px}h1,h2{max-width:1200px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:24px}a{color:inherit;text-decoration:none}img{width:100%;border:1px solid #B8B0A9}span{display:block;padding:10px 0}</style><h1>CEH M10 · Denial of Service</h1><p>58 editable source boards and 18 actual LibreOffice-exported deck slides. Source ready; full-film animation and narration remain the next layer.</p><p><a href="../examples/index.html">Four seekable motion examples</a> · <a href="../slides/CEH_M10_Editable_Visual_Lookbook_18slides.pptx">Editable PowerPoint</a></p><h2>Scene boards</h2><div class="grid">'+cards+'</div><h2>Actual deck export</h2><div class="grid">'+slides+'</div></html>',encoding='utf-8')
print(json.dumps({'stage':'contact_sheets','boards':58,'slides':18}))

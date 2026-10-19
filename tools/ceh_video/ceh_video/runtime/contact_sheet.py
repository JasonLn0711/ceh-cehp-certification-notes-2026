from ceh_video.common import project_root, Project
"""Build labeled contact pages from real PNG captures."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import sys,math
p=Path(sys.argv[1]);pattern=sys.argv[2] if len(sys.argv)>2 else '*.png';files=sorted(p.glob(pattern));assert files
font=ImageFont.truetype(str(project_root()/'assets/fonts/LiberationSans-Regular.ttf'),25)
for page in range(math.ceil(len(files)/9)):
 subset=files[page*9:(page+1)*9];sheet=Image.new('RGB',(1920,400*math.ceil(len(subset)/3)),(240,235,228));draw=ImageDraw.Draw(sheet)
 for j,f in enumerate(subset):
  x=j%3*640;y=j//3*400;draw.text((x+12,y+5),f.stem,font=font,fill=(41,36,33));im=Image.open(f).convert('RGB');im.thumbnail((640,360));sheet.paste(im,(x,y+36))
 sheet.save(p/f'contact-{page+1:02}.jpg',quality=93)
print({'captured_frames':len(files),'contact_pages':math.ceil(len(files)/9)})

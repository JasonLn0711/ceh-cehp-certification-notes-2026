"""Build inspectable sheets from actual captured native frames, without approving them."""
from pathlib import Path
import sys,json,math
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa'
font=ImageFont.truetype(str(R/'assets/fonts/LiberationSans-Regular.ttf'),24)
for ch in sys.argv[1:]:
 files=sorted((Q/(ch+'-direct')).glob('S*.png'))
 assert files,ch+' native frames missing'
 for page in range(math.ceil(len(files)/9)):
  group=files[page*9:(page+1)*9];sheet=Image.new('RGB',(1920,400*math.ceil(len(group)/3)),(240,235,228));draw=ImageDraw.Draw(sheet)
  for i,p in enumerate(group):
   x=i%3*640;y=i//3*400;draw.text((x+10,y+3),p.stem,font=font,fill=(41,36,33));im=Image.open(p);im.thumbnail((640,360));sheet.paste(im,(x,y+36))
  sheet.save(Q/f'{ch}-native-contact-{page+1:02}.jpg',quality=94)
 print(json.dumps({'phase':'native_contact_sheets','chapter':ch,'captured_frames':len(files),'sheets':math.ceil(len(files)/9),'review':'pending'}),flush=True)

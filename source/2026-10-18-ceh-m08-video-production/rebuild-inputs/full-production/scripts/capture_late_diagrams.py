"""Capture actual encoded late-phase repairs missed by the standard midpoint sample."""
from pathlib import Path
import json,hashlib,subprocess,concurrent.futures,math
from PIL import Image,ImageDraw,ImageFont
from production_settings import MASTER_FILENAME
R=Path(__file__).resolve().parents[1];Q=R.parent/'qa';O=R.parent/'output'
def main():
 movie=O/MASTER_FILENAME;meta=json.load(open(R/'data/master-timing.json'));ids={'S06','S08','S11','S22','S23','S24','S28','S30','S32','S37','S40','S42','S43','S44','S45','S46','S53'}
 rows=[{'scene':s['scene'],'time':s['start']+s['duration']-4,'local_time':s['duration']-4,'file':s['scene']+'-late.png'} for s in meta['scenes'] if s['scene'] in ids]
 def grab(row):subprocess.run(['ffmpeg','-v','error','-ss',str(row['time']),'-i',str(movie),'-frames:v','1','-update','1','-y',str(O/'inspection_frames'/row['file'])],check=True);return row
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for i,row in enumerate(pool.map(grab,rows),1):print(json.dumps({'phase':'late_encoded_repairs_captured','completed':i,'total':len(rows),'scene':row['scene']}),flush=True)
 font=ImageFont.truetype(str(R/'assets/fonts/LiberationSans-Regular.ttf'),24)
 for page in range(math.ceil(len(rows)/9)):
  group=rows[page*9:(page+1)*9];sheet=Image.new('RGB',(1920,400*math.ceil(len(group)/3)),(240,235,228));draw=ImageDraw.Draw(sheet)
  for j,row in enumerate(group):
   x=j%3*640;y=j//3*400;draw.text((x+10,y+3),row['scene']+' late '+f'{row["time"]:.3f}s',font=font,fill=(41,36,33));im=Image.open(O/'inspection_frames'/row['file']);im.thumbnail((640,360));sheet.paste(im,(x,y+36))
  sheet.save(O/'inspection_frames'/f'late-repairs-contact-{page+1:02}.jpg',quality=94)
 with movie.open('rb') as f:master_hash=hashlib.file_digest(f,'sha256').hexdigest()
 (Q/'late-diagram-samples.json').write_text(json.dumps({'status':'captured_pending_visual_review','reason':'Targeted late-phase repairs are not visible at every standard scene midpoint.','master_sha256':master_hash,'count':len(rows),'samples':rows},indent=2))
if __name__=='__main__':main()

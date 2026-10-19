#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys,json,os,time
root=Path(__file__).resolve().parents[1];qa=root.parent/'qa';name=sys.argv[1];start=time.time()
record={'stage':name,'pid':os.getpid(),'status':'running','started':start,'command':sys.argv[2:]};target=qa/(name+'-process.json');target.write_text(json.dumps(record,indent=2))
with (qa/(name+'.log')).open('a') as log:
 result=subprocess.run(sys.argv[2:],cwd=root,stdout=log,stderr=log)
record.update(status='completed' if result.returncode==0 else 'failed',exit_code=result.returncode,elapsed_seconds=time.time()-start);target.write_text(json.dumps(record,indent=2));sys.exit(result.returncode)

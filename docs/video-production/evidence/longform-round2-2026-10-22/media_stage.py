"""One native stage, pinned engine selected by PYTHONPATH; no mocked producer gates."""
import sys,time,json
from types import SimpleNamespace
from ceh_video.common import Project
from ceh_video.mandarin import action
from ceh_video.mandarin_build import assemble,host
from ceh_video.progress import Progress
p=Project(sys.argv[1]);stage=sys.argv[2];start=time.monotonic()
if stage=='host':
    host(p,p.scenes,'C01',p.root/'chapters/C01');result=assemble(p)
else:result=action(p,SimpleNamespace(name=stage),Progress(plain=True))
print(json.dumps({'stage':stage,'seconds':time.monotonic()-start,'result':result}))

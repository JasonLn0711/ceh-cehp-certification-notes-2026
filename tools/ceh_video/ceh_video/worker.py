"""Run shared media implementations in an explicit project context."""
import os, runpy, sys
from pathlib import Path
from .common import project_root

def main():
    root = project_root(); name = sys.argv[1]
    runtime = Path(__file__).parent/'runtime'
    sys.path[:0] = [str(runtime), str(root/'scripts')]
    script = runtime/(name+'.py')
    if not script.is_file(): raise SystemExit('Unknown shared stage: '+name)
    sys.argv = [str(script), *sys.argv[2:]]
    os.chdir(root)
    runpy.run_path(str(script), run_name='__main__')

if __name__ == '__main__': main()

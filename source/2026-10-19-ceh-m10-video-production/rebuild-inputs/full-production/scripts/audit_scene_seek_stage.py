"""Run the real native forward/backward seek audit with the fixed local browser."""
from pathlib import Path
import subprocess,os
R=Path(__file__).resolve().parents[1];env=os.environ.copy();env['HYPERFRAMES_BROWSER_PATH']='/home/jnlngx10/.cache/ms-playwright/chromium_headless_shell-1234/chrome-linux/headless_shell'
subprocess.run(['node',str(R/'scripts/audit_scene_seek.mjs')],cwd=R,env=env,check=True)

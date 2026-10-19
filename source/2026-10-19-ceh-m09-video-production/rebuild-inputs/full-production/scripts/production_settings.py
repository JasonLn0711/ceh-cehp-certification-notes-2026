"""M09 production identity; immutable speech/quiz contract."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
MASTER_FILENAME='CEH_M09_Social_Engineering_en-US_1_5x_1s_master.mp4'
def quiz_seconds():
 d=json.loads((ROOT/'data/production-overrides.json').read_text());assert d['module']=='M09' and d['quiz_silence_seconds']==1
 return 1
def quiz_label():return '1 second each'

"""M10 production identity; immutable speech/quiz contract."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
MASTER_FILENAME='CEH_M10_Denial_of_Service_en-US_1_5x_1s_master.mp4'
def quiz_seconds():
 d=json.loads((ROOT/'data/production-overrides.json').read_text());assert d['module']=='M10' and d['quiz_silence_seconds']==1
 return 1
def quiz_label():return '1 second each'

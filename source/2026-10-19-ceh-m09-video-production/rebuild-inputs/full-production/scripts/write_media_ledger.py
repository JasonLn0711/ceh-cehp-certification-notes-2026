"""Hash the actual frozen series artwork, fonts, models and M09 QR without touching media."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];S=R.parent/'inputs/package/CEH_M09_English_Editorial_Masterclass';M08=R.parent.parent/'CEH_M08_v1_0/project'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
rows=[]
for base in ['assets/props','assets/fonts','assets/mascot','assets/vendor','models']:
 for p in sorted((R/base).rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(R);h=sha(p)
  if (S/rel).is_file() and sha(S/rel)==h:origin='Immutable M09 source ZIP; inherited M04 v3 artwork and notices retained'
  elif p.name=='m09-qr.svg':
   assert h==sha(S/'lab_mock/E03_qr_code.svg');origin='Immutable M09 lab_mock/E03_qr_code.svg; reserved example.test URL'
  elif (M08/rel).is_file() and sha(M08/rel)==h:origin='Approved M08 production dependency; physically copied unchanged'
  else:raise RuntimeError(('Unclassified frozen media origin',str(rel)))
  rows.append({'path':str(rel),'sha256':h,'origin':origin,'scope':'Local CEH teaching production; no provider upload'})
(R/'licenses/M09-media-ledger.json').write_text(json.dumps({'module':'M09','assets':rows,'model_policy':'Public non-cloned af_heart; model cards and licenses included','source_scope':'44 inherited locks are verified separately. M04 v3 assets and neutral owned series props reused; M09 content and native case geometry newly authored. Generated audio has separate per-clip and delivery manifests.'},indent=2)+'\n')
print(json.dumps({'phase':'frozen_media_ledger_written','files':len(rows),'mascot_files':sum(x['path'].startswith('assets/mascot/') for x in rows)}))

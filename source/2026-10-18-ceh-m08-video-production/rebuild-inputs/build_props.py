#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];out=R/'assets/props';out.mkdir(exist_ok=True)
props={
'packet':('Recorded packet bytes','M 60 25 L 145 25 L 180 60 L 180 180 L 60 180 Z M 145 25 L 145 60 L 180 60 M 83 92 L 155 92 M 83 118 L 155 118 M 83 144 L 132 144',['S05','S06','S27']),
'capture':('Offline capture view','M 30 50 L 200 50 L 200 165 L 30 165 Z M 30 80 L 200 80 M 48 64 L 55 64 M 75 64 L 82 64 M 80 105 L 98 123 L 80 141 M 115 143 L 153 143',['S05','S34','S45']),
'switch':('Switch forwarding resources','M 40 65 L 195 65 L 195 155 L 40 155 Z M 62 45 L 62 65 M 92 45 L 92 65 M 123 45 L 123 65 M 154 45 L 154 65 M 182 45 L 182 65 M 62 155 L 62 177 M 92 155 L 92 177 M 123 155 L 123 177 M 154 155 L 154 177 M 182 155 L 182 177 M 72 90 L 160 90 L 160 130 L 72 130 Z',['S20','S36']),
'network':('Packet observation path','M 25 30 L 92 30 L 92 85 L 25 85 Z M 143 135 L 210 135 L 210 190 L 143 190 Z M 58 85 L 58 112 L 176 112 L 176 135 M 104 100 L 118 112 L 104 124',['S03','S11','S35']),
'boundary':('Scoped forwarding boundary','M 65 25 L 170 25 L 200 60 L 200 180 L 35 180 L 35 60 Z M 72 62 L 162 152 M 162 62 L 72 152',['S49']),
'lease':('Recorded lease information','M 35 50 Q 117 18 200 50 L 200 170 Q 117 202 35 170 Z M 35 50 Q 117 85 200 50 M 35 110 Q 117 145 200 110 M 92 110 L 117 135 L 156 91',['S25','S26','S51']),
'evidence':('Source-linked claims','M 55 35 L 185 35 L 185 190 L 55 190 Z M 88 25 L 153 25 L 153 55 L 88 55 Z M 78 84 L 95 99 L 116 75 M 130 89 L 166 89 M 78 134 L 95 149 L 116 125 M 130 139 L 166 139',['S09','S38','S48','S58']),
'lock':('Restricted access','M 65 95 L 65 65 Q 65 20 117 20 Q 170 20 170 65 L 170 95 M 45 95 L 192 95 L 192 195 L 45 195 Z M 118 126 L 118 162',['S22','S24'])}
ledger=[]
for name,(title,path,scenes) in props.items():
 target=out/f'm08-{name}.svg';target.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="240" height="220" viewBox="0 0 240 220"><title>{title}</title><path d="{path}" fill="none" stroke="#292421" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/></svg>')
 ledger.append(dict(id='m08-'+name,path=str(target.relative_to(R)),purpose=title,scenes=scenes,source='Generic editable line geometry adopted from M07 source and assigned M08 roles; no image model or stock asset.'))
(R/'m08_asset_extensions.json').write_text(json.dumps(ledger,indent=2)+'\n');print(json.dumps({'stage':'props_built','editable_props':len(ledger)}))

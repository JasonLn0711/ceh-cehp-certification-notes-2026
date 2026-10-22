"""Make review pages from actual candidate PNGs; never approve goldens."""
import argparse
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument("project", type=Path)
args = parser.parse_args()
p = args.project.resolve()
qa = p.parent / "qa"
source = qa / "visual/scenes"
manifest = json.loads((source / "manifest.json").read_text())
quiz = {q["scene_id"] for q in json.loads((p / "data/questions.json").read_text())["questions"]}
selected = []
for sid in sorted(manifest["sources"]):
    rows = sorted((r for r in manifest["rows"] if r["name"].startswith(sid + "-")),
                  key=lambda r: r["frame"])
    # All quiz boundary states; one late visible teaching state per other scene.
    selected.extend(rows if sid in quiz else [rows[-2]])
folder = qa / "visual/candidate-review"
folder.mkdir(exist_ok=True)
font = ImageFont.truetype(str(p / "assets/fonts/LiberationSans-Regular.ttf"), 25)
pages = {}
for i in range(math.ceil(len(selected) / 9)):
    group = selected[i * 9:(i + 1) * 9]
    image = Image.new("RGB", (1920, 400 * math.ceil(len(group) / 3)), (240, 235, 228))
    draw = ImageDraw.Draw(image)
    for j, row in enumerate(group):
        x, y = (j % 3) * 640, (j // 3) * 400
        draw.text((x + 10, y + 4), row["name"], font=font, fill=(41, 36, 33))
        with Image.open(source / (row["name"] + ".png")) as full:
            thumb = full.convert("RGB")
            thumb.thumbnail((640, 360))
            image.paste(thumb, (x, y + 36))
    file = folder / f"contact-{i + 1:02}.jpg"
    image.save(file, quality=95)
    pages[str(file.relative_to(qa))] = hashlib.sha256(file.read_bytes()).hexdigest()
result = {
    "status": "awaiting_actual_visual_inspection",
    "candidate_sha256": hashlib.sha256((source / "manifest.json").read_bytes()).hexdigest(),
    "selected_states": [r["name"] for r in selected],
    "contact_sheets": pages,
}
(folder / "selection.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"pages": len(pages), "states": len(selected), "status": result["status"]}))

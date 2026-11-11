"""Grid of channel thumbnails (numbered) to pick shorts in the target style.

usage: thumb_grid.py <channel_list.txt> <thumbs_dir> <out.jpg> [start] [count]
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw

lst, tdir, out = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
count = int(sys.argv[5]) if len(sys.argv) > 5 else 30
ids = [l.split("|")[0] for l in open(lst, encoding="utf-8") if l.strip()][start:start + count]

W, H, COLS = 216, 384, 10
rows = (len(ids) + COLS - 1) // COLS
grid = Image.new("RGB", (W * COLS, H * rows), "black")
d = ImageDraw.Draw(grid)
for i, vid in enumerate(ids):
    p = tdir / f"{vid}.jpg"
    if not p.exists():
        continue
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if w > h:  # landscape thumbnail: centre-crop to 9:16
        cw = int(h * 9 / 16)
        im = im.crop(((w - cw) // 2, 0, (w - cw) // 2 + cw, h))
    x, y = (i % COLS) * W, (i // COLS) * H
    grid.paste(im.resize((W, H)), (x, y))
    d.rectangle([x, y, x + 28, y + 16], fill="black")
    d.text((x + 3, y + 2), str(start + i + 1), fill="yellow")
grid.save(out, quality=85)
print(out, grid.size)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Slice strict black-line contact-sheet grids into individual product photos.
Smart: high-threshold line detection + false-gutter filtering + empty-cell skip."""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

ROOT = Path("/home/user")
GRIDS = ROOT / "catalog_assets" / "grids"
OUT = ROOT / "catalog_assets" / "products"
CHECK = ROOT / "catalog_assets" / "checkers"
OUT.mkdir(exist_ok=True); CHECK.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT / "catalog"))
from products_data import P  # noqa: E402

MAPPING = {
    "g1_uwc.png":    ["UWC-%02d" % i for i in range(1, 13)],
    "g2_uwd.png":    ["UWD-%02d" % i for i in range(1, 11)],
    "g3_alw.png":    ["ALW-%02d" % i for i in range(1, 11)],
    "g4_ald.png":    ["ALD-%02d" % i for i in range(1, 9)],
    "g5_alp.png":    ["ALP-%02d" % i for i in range(1, 9)],
    "g6_glz.png":    ["GLZ-%02d" % i for i in range(1, 11)],
    "g7_stf.png":    ["STF-%02d" % i for i in range(1, 9)],
    "g8_mst.png":    ["MST-%02d" % i for i in range(1, 11)],
    "g9_sls.png":    ["SLS-%02d" % i for i in range(1, 9)],
    "g10_rlsmod.png":["RLS-%02d" % i for i in range(1, 9)] + ["MOD-%02d" % i for i in range(1, 11)],
}

def line_frac(gray, axis, pos):
    if axis == "r":
        vals = [gray.getpixel((x, pos)) for x in range(0, gray.width, 2)]
    else:
        vals = [gray.getpixel((pos, y)) for y in range(0, gray.height, 2)]
    return sum(1 for v in vals if v < 115) / len(vals)

def find_runs(fracs, thr=0.8, min_run=3):
    runs, start = [], None
    for i, f in enumerate(fracs):
        if f >= thr:
            if start is None:
                start = i
        else:
            if start is not None and i - start >= min_run:
                runs.append([start, i - 1])
            start = None
    if start is not None:
        runs.append([start, len(fracs) - 1])
    return runs

def filter_gutters(runs, size):
    """Keep internal lines only; drop false positives that sit too close to a neighbour."""
    internal = [r for r in runs if r[0] > 2 and r[1] < size - 3]
    if len(internal) <= 1:
        return internal
    centers = sorted((r[0] + r[1]) // 2 for r in internal)
    gaps = [centers[i + 1] - centers[i] for i in range(len(centers) - 1)]
    med = sorted(gaps)[len(gaps) // 2]
    out = [internal[0]]
    for r in internal[1:]:
        c = (r[0] + r[1]) // 2
        prev = (out[-1][0] + out[-1][1]) // 2
        if c - prev < med * 0.35:
            continue  # too close -> false positive
        out.append(r)
    return out

def cell_ink(gray, box):
    x0, y0, x1, y1 = box
    if x1 - x0 < 25 or y1 - y0 < 25:
        return 0.0
    region = gray.crop(box)
    px = region.load()
    n = tot = 0
    for yy in range(0, region.height, 2):
        for xx in range(0, region.width, 2):
            tot += 1
            if px[xx, yy] < 245:
                n += 1
    return n / tot

def slice_grid(path, codes):
    im = Image.open(path).convert("RGB")
    gray = ImageOps.grayscale(im)
    w, h = im.size
    vg = filter_gutters(find_runs([line_frac(gray, "c", x) for x in range(w)]), w)
    hg = filter_gutters(find_runs([line_frac(gray, "r", y) for y in range(h)]), h)
    xs = [0] + [(r[0] + r[1]) // 2 for r in vg] + [w]
    ys = [0] + [(r[0] + r[1]) // 2 for r in hg] + [h]
    cells = []
    for yi in range(len(ys) - 1):
        for xi in range(len(xs) - 1):
            x0, x1 = xs[xi] + 4, xs[xi + 1] - 4
            y0, y1 = ys[yi] + 4, ys[yi + 1] - 4
            if x1 - x0 < 30 or y1 - y0 < 30:
                continue
            cells.append((x0, y0, x1, y1))
    kept = [(box, ink) for box in cells if (ink := cell_ink(gray, box)) >= 0.02]
    print(f"{path}: grid {len(xs)-1}x{len(ys)-1} -> {len(cells)} cells, {len(kept)} non-empty (need {len(codes)})")
    sheet = im.copy()
    dr = ImageDraw.Draw(sheet)
    n_saved = 0
    for i, (box, ink) in enumerate(kept):
        if i >= len(codes):
            break
        code = codes[i]
        dr.rectangle(box, outline=(255, 0, 0), width=3)
        dr.text((box[0] + 6, box[1] + 6), code, fill=(255, 0, 0))
        crop = im.crop(box)
        if crop.width > 0 and crop.height > 0:
            crop = ImageOps.fit(crop, (800, 600), Image.LANCZOS)
            crop.save(OUT / f"{code}.jpg", quality=84, optimize=True)
            n_saved += 1
    sheet.save(CHECK / (Path(path).stem + "_checker.png"))
    missing = [c for c in codes if not (OUT / f"{c}.jpg").exists()]
    print(f"   saved {n_saved}; missing: {missing}")
    return n_saved

if __name__ == "__main__":
    total = 0
    for fname, codes in MAPPING.items():
        p = GRIDS / fname
        if not p.exists():
            print(f"!! MISSING GRID: {fname}")
            continue
        total += slice_grid(p, codes)
    n_files = len(list(OUT.glob("*.jpg")))
    print(f"\nTOTAL saved: {total} | product files on disk: {n_files} / 102")

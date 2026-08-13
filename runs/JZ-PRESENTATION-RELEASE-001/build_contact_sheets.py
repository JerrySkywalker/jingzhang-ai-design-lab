#!/usr/bin/env python3
"""Make deterministic contact sheets from rasterized RC2 PDFs for QA only."""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent / "qa" / "final-pdf-raster"
OUT = ROOT.parent / "contact-sheets"


def font(size: int, bold: bool = False):
    path = Path(r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf")
    return ImageFont.truetype(str(path), size=size)


def sort_key(path: Path):
    match = re.search(r"-(\d+)\.png$", path.name)
    return int(match.group(1)) if match else 0


def build(prefix: str, columns: int) -> Path:
    pages = sorted(ROOT.glob(f"{prefix}-*.png"), key=sort_key)
    if not pages:
        raise RuntimeError(f"No raster pages for {prefix}")
    thumbs = []
    for page in pages:
        image = Image.open(page).convert("RGB")
        image.thumbnail((860, 610), Image.Resampling.LANCZOS)
        thumbs.append((page, image.copy()))
    gap, label_h, margin = 24, 46, 36
    rows = math.ceil(len(thumbs) / columns)
    cell_w = max(image.width for _, image in thumbs)
    cell_h = max(image.height for _, image in thumbs) + label_h
    sheet = Image.new("RGB", (margin * 2 + columns * cell_w + (columns - 1) * gap, margin * 2 + rows * cell_h + (rows - 1) * gap), "#F4F1EA")
    draw = ImageDraw.Draw(sheet)
    draw.text((margin, 10), f"RC2 PDF QA · {prefix.upper()} · {len(thumbs)} pages", fill="#17324D", font=font(24, True))
    for index, (page, image) in enumerate(thumbs):
        col, row = index % columns, index // columns
        x = margin + col * (cell_w + gap)
        y = margin + row * (cell_h + gap)
        sheet.paste(image, (x + (cell_w - image.width) // 2, y + label_h))
        draw.rectangle((x, y + label_h, x + cell_w, y + label_h + image.height), outline="#AAB8BC", width=2)
        draw.text((x, y + 12), f"{index + 1:02d} · {page.name}", fill="#4C5D64", font=font(18))
    OUT.mkdir(parents=True, exist_ok=True)
    output = OUT / f"{prefix}-contact-sheet.png"
    sheet.save(output, "PNG", optimize=False)
    return output


def main() -> None:
    outputs = [build("a3-zh", 3), build("a3-en", 3), build("a0-zh", 2), build("a0-en", 2)]
    for output in outputs:
        print(output)


if __name__ == "__main__":
    main()

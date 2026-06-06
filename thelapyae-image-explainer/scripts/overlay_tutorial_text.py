#!/usr/bin/env python3
"""Overlay exact tutorial text on a generated illustration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


DEFAULT_FONT = Path.home() / "Library/Fonts/NotoSansMyanmar[wdth,wght].ttf"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--font", type=Path, default=DEFAULT_FONT)
    return parser.parse_args()


def fit_font(font_path: Path, text: str, max_width: int, start_size: int):
    size = start_size
    while size >= 24:
        font = ImageFont.truetype(str(font_path), size)
        box = font.getbbox(text)
        if box[2] - box[0] <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(str(font_path), 24)


def rounded_text_box(
    draw: ImageDraw.ImageDraw,
    box: list[int],
    text: str,
    font_path: Path,
    fill: str,
    text_fill: str,
    start_size: int,
    radius: int = 28,
    outline: str | None = None,
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=4)
    font = fit_font(font_path, text, x2 - x1 - 48, start_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    x = x1 + (x2 - x1 - (bbox[2] - bbox[0])) / 2
    y = y1 + (y2 - y1 - (bbox[3] - bbox[1])) / 2 - bbox[1]
    draw.text((x, y), text, font=font, fill=text_fill)


def main() -> int:
    args = parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    image = Image.open(args.input).convert("RGB")
    draw = ImageDraw.Draw(image)

    for area in spec.get("erase_areas", []):
        draw.rectangle(area, fill="white")

    draw.rectangle(spec["header_area"], fill="white")
    rounded_text_box(
        draw,
        spec["step_box"],
        spec["step"],
        args.font,
        "#f7931e",
        "white",
        78,
    )
    rounded_text_box(
        draw,
        spec["heading_box"],
        spec["heading"],
        args.font,
        "white",
        "black",
        86,
        radius=0,
    )

    for item in spec.get("overlays", []):
        rounded_text_box(
            draw,
            item["box"],
            item["text"],
            args.font,
            item.get("fill", "white"),
            item.get("text_fill", "black"),
            item.get("size", 48),
            item.get("radius", 22),
            item.get("outline"),
        )

    draw.rectangle(spec["footer_area"], fill="white")
    rounded_text_box(
        draw,
        spec["footer_box"],
        spec["footer"],
        args.font,
        "#63b96b",
        "white",
        52,
        outline="#2e7d32",
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output)
    print(f"Saved image: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

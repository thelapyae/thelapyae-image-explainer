#!/usr/bin/env python3
"""Generate one illustration with Gemini's native image model."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


DEFAULT_MODEL = "gemini-3.1-flash-image"
VALID_ASPECT_RATIOS = {
    "1:1",
    "1:4",
    "1:8",
    "2:3",
    "3:2",
    "3:4",
    "4:1",
    "4:3",
    "4:5",
    "5:4",
    "8:1",
    "9:16",
    "16:9",
    "21:9",
}
VALID_IMAGE_SIZES = {"512", "1K", "2K", "4K"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate one PNG illustration with Gemini."
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Prompt text.")
    prompt_group.add_argument(
        "--prompt-file", type=Path, help="UTF-8 file containing the prompt."
    )
    parser.add_argument("--output", required=True, type=Path, help="Output PNG path.")
    parser.add_argument(
        "--reference",
        action="append",
        default=[],
        type=Path,
        help="Optional reference image. Repeat for multiple images.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--aspect-ratio", default="16:9", choices=VALID_ASPECT_RATIOS)
    parser.add_argument("--image-size", default="1K", choices=VALID_IMAGE_SIZES)
    return parser.parse_args()


def load_dependencies():
    try:
        from google import genai
        from google.genai import types
        from PIL import Image
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency. Install with: "
            "python3 -m pip install --user google-genai pillow"
        ) from exc
    return genai, types, Image


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        if not args.prompt_file.is_file():
            raise SystemExit(f"Prompt file not found: {args.prompt_file}")
        prompt = args.prompt_file.read_text(encoding="utf-8")
    else:
        prompt = args.prompt or ""
    if not prompt.strip():
        raise SystemExit("Prompt cannot be empty.")
    return prompt.strip()


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit(
            "Set GEMINI_API_KEY (preferred) or GOOGLE_API_KEY before running."
        )

    genai, types, Image = load_dependencies()
    contents: list[object] = [read_prompt(args)]
    for reference in args.reference:
        if not reference.is_file():
            raise SystemExit(f"Reference image not found: {reference}")
        contents.append(Image.open(reference))

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=args.model,
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=args.aspect_ratio,
                image_size=args.image_size,
            ),
        ),
    )

    images = []
    for part in response.parts or []:
        if getattr(part, "thought", False):
            continue
        inline_data = getattr(part, "inline_data", None)
        if inline_data is not None:
            image = part.as_image()
            if image is not None:
                images.append(image)

    if not images:
        raise SystemExit("Gemini returned no image. Revise the prompt or check quota.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    images[-1].save(args.output)
    print(f"Saved image: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

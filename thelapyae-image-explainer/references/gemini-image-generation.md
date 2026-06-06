# Gemini Image Generation

Use this fallback when built-in `image_gen` is unavailable or rate-limited.

## Setup

Install the official Python SDK and Pillow:

```bash
python3 -m pip install --user google-genai pillow
```

Set exactly one key environment variable. Prefer `GEMINI_API_KEY`:

```bash
export GEMINI_API_KEY="your-key"
```

Never put the key in a prompt file, command argument, source file, committed
shell file, generated artifact, or terminal output.

## Generate

Write the final prompt to a UTF-8 text file, then run:

```bash
python3 scripts/generate_with_gemini.py \
  --prompt-file /absolute/path/prompt.txt \
  --output /absolute/path/output.png \
  --aspect-ratio 16:9 \
  --image-size 1K
```

To preserve avatar identity after an approved reference exists:

```bash
python3 scripts/generate_with_gemini.py \
  --prompt-file /absolute/path/prompt.txt \
  --reference assets/avatar-reference.png \
  --output /absolute/path/output.png
```

Generate one illustration per command. Validate the result with
`references/qa-checklist.md` before delivery.

## Defaults

- Model: `gemini-3.1-flash-image`
- Aspect ratio: `16:9`
- Resolution: `1K`
- Output: PNG

All Gemini-generated images include Google's SynthID watermark.

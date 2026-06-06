# TheLapyae Image Explainer

A Codex skill for turning technical topics, workflows, and abstract ideas into
clean hand-drawn visual explanations featuring TheLapyae's custom avatar.

## Features

- Plans concise illustration shot lists
- Generates one clear visual metaphor per image
- Preserves a consistent custom avatar
- Uses built-in `image_gen` when available
- Falls back to Gemini native image generation
- Supports reference-image-based character consistency
- Includes generation QA rules

## Install

```bash
git clone https://github.com/thelapyae/thelapyae-image-explainer.git
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R thelapyae-image-explainer/thelapyae-image-explainer \
  "${CODEX_HOME:-$HOME/.codex}/skills/"
```

## Use

```text
Use $thelapyae-image-explainer to explain cloud computing in four illustrations.
```

## Gemini Fallback

Install the official SDK:

```bash
python3 -m pip install --user google-genai pillow
```

Set the API key as an environment variable:

```bash
export GEMINI_API_KEY="your-key"
```

Never commit API keys to source control.

## Structure

```text
thelapyae-image-explainer/
├── SKILL.md
├── agents/openai.yaml
├── assets/avatar-reference.png
├── references/
└── scripts/generate_with_gemini.py
```

## License

MIT. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

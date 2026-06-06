---
name: thelapyae-image-explainer
description: Plan, generate, and edit clean hand-drawn visual explanations featuring TheLapyae's recurring custom avatar. Use for blog posts, Notion documents, technical explainers, workflows, concepts, social posts, visual metaphors, shot lists, or requests mentioning TheLapyae's avatar, image explainers, article illustrations, or custom character diagrams.
---

# TheLapyae Image Explainer

Create 16:9 article illustrations that turn one important idea, process, state, or
contrast into a memorable hand-drawn scene. Make Lapyae's avatar perform the
conceptual action instead of standing beside it as decoration.

## Load References

- Read `references/avatar-profile.md` before every generation or avatar edit.
- Read `references/style-dna.md` when planning or generating illustrations.
- Read `references/composition-patterns.md` when choosing a visual metaphor.
- Read `references/prompt-template.md` immediately before calling `image_gen`.
- Read `references/qa-checklist.md` after generation.
- If `assets/avatar-reference.png` exists, use it as the identity reference.
- Read `references/gemini-image-generation.md` before using the Gemini fallback.

## Workflow

1. Read the supplied article, file, screenshot, link content, or concept.
2. Extract the key claim, cognitive turn, process, contrast, or failure state.
3. Select only useful illustration points. Do not illustrate every section.
4. When the user asks for planning, return a concise shot list with:
   - placement
   - core idea
   - composition type
   - avatar action
   - objects
   - up to five short labels
5. When the user asks to generate images, proceed without another confirmation.
6. Generate each illustration separately:
   - Try built-in `image_gen` first.
   - If built-in generation is unavailable or rate-limited and
     `GEMINI_API_KEY` or `GOOGLE_API_KEY` is set, use
     `scripts/generate_with_gemini.py`.
   - Never paste, print, log, or store the API key in the skill or workspace.
   - Use `gemini-3.1-flash-image`, 16:9, and 1K by default.
7. Keep one core idea per image and invent a fresh physical metaphor.
8. Validate every result against `references/qa-checklist.md`.
9. Save project images under `assets/<article-slug>-illustrations/` with ordered
   filenames such as `01-input-bottleneck.png`.

## Output Rules

- Default to 1-3 images for short content and 4-6 for long content.
- Use English labels unless the user requests Burmese or another language.
- Keep labels short because generated text can be unreliable.
- Never imitate a living artist or copy a prior composition.
- Preserve the avatar identity markers across all images.
- Report the purpose and saved path of every delivered image.
- Report which image backend and model produced the files.

## Avatar Customization

When the user supplies a portrait or asks to change the avatar:

1. Treat the portrait as an identity reference, not an edit target, unless stated.
2. Update `references/avatar-profile.md` with only visible, stable traits.
3. Generate a neutral five-pose reference sheet.
4. Save the approved sheet as `assets/avatar-reference.png`.
5. Keep clothing and accessories simple enough to reproduce consistently.
6. Do not infer sensitive traits or identity details from the portrait.

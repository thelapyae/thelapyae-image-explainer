# Prompt Template

Use one `image_gen` call per image.

```text
Use case: illustration-story
Asset type: 16:9 horizontal article illustration
Primary request: Visualize {core idea} as one clear hand-drawn metaphor.

Avatar identity:
Use assets/avatar-reference.png as the primary identity reference. Lapyae is a
simplified illustrated adult man with short side-parted black hair, an oval
clean-shaven face, dark almond-shaped eyes, thick eyebrows, a slim average build,
a plain black crew-neck T-shirt, medium-gray pants, and black low-top shoes.
Preserve these traits consistently. Lapyae must perform the core conceptual action.

Composition:
{describe the avatar action, primary object, information movement, and spacing}

Labels:
Use only these short handwritten labels: {labels}

Visual style:
Pure white background. Thin slightly wobbly hand-drawn black ink lines. Keep
object interiors white. Use orange ink only for paths and arrows, red ink only
for warnings or emphasis, blue ink only for secondary handwritten notes, and
light gray only for structural guides or avatar pants. No painted surfaces or
large flat color fills. Main scene occupies 40-60% of the canvas.

Constraints:
One image communicates one idea. No title. No presentation slide, formal
flowchart, commercial vector style, realistic UI, gradient, shadow, texture,
complex background, colored panels, glossy UI, cute mascot styling, watermark,
or extra character.
Invent a fresh metaphor and do not copy an existing illustration composition.
```

For Burmese Concept Mode, keep labels concise. If the meaning is materially
wrong, regenerate with fewer labels. Never replace or overlay the generated text.

## Tutorial Mode Template

```text
Use case: tutorial explainer
Asset type: information-rich 16:9 horizontal how-to illustration
Step: {STEP number}
Action heading: {exact heading}
Explanation: {one exact short sentence}

Avatar identity:
Use assets/avatar-reference.png. Preserve Lapyae's face, hair, black T-shirt,
gray pants, black shoes, and natural adult proportions. Make him demonstrate the
step rather than stand beside it.

Main demonstration:
{physical action and objects}

Information blocks:
- Exact command or path: {exact string}
- Input callout: {exact text}
- Process callout: {exact text}
- Result callout: {exact text}
- Bottom note: {exact text}

Layout:
Use 65-80% of the canvas. Put STEP badge at top-left, action heading across the
top, demonstration in the center, command/path in a white box outlined with blue
ink, 2-4 handwritten callouts connected by orange arrows, and the result note
along the bottom. Keep boxes and banners white inside.

Constraints:
Keep every supplied text string verbatim. Do not invent extra labels. Pure white
background, black/red/orange/blue ink drawing, no large flat color fills, no
realistic UI, no corporate slide template, no decorative scenery, no watermark
text, and no extra person. Generate all text natively in the image. Do not plan
for any later text overlay, typesetting, or post-processing.
```

For Burmese Tutorial Mode, allow 6-10 short Burmese text elements. Visually
review the generated text but keep it unchanged in the delivered image. If the
meaning is materially wrong, regenerate the whole image with fewer or shorter
text elements; never overlay replacement text.

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
Pure white background, thin slightly wobbly black ink lines, restrained flat
colors, sparse orange paths or arrows, red only for warnings or key results,
blue only for secondary notes, and lots of blank white space. Main scene occupies
40-60% of the canvas.

Constraints:
One image communicates one idea. No title. No presentation slide, formal
flowchart, commercial vector style, realistic UI, gradient, shadow, texture,
complex background, cute mascot styling, watermark, or extra character.
Invent a fresh metaphor and do not copy an existing illustration composition.
```

For Burmese labels, provide exact short Burmese text and limit the image to three
labels. If spelling is wrong, regenerate with fewer labels or add text later with
a deterministic graphics tool.

# QA Checklist

Accept only when all are true:

- The image is 16:9 with a clean white background.
- The avatar matches `assets/avatar-reference.png`.
- Hair, facial features, black T-shirt, gray pants, and black shoes are consistent.
- The avatar performs the central action.
- The scene explains one idea and has substantial white space.
- The metaphor is fresh and understandable within a few seconds.
- Labels are short, readable, correctly spelled, and limited in number.
- Accent colors follow their assigned roles.
- The result does not resemble a slide, formal diagram, or children's poster.

Tutorial Mode must also pass:

- A viewer can identify the step without reading an external caption.
- The image contains a step number and direct action heading.
- The exact command, path, prompt, or required input is visible when relevant.
- Input, action, and result are connected with clear visual callouts.
- The canvas is information-rich without becoming crowded.
- Burmese spelling matches the supplied strings exactly.
- If generated Burmese is wrong, the final delivered image uses deterministic
  text overlay and is checked again.

Regenerate or edit when facial identity or clothing drifts, the old indigo
placeholder returns, the avatar is decorative, the scene is crowded, text is
incorrect, a title appears, or the background gains texture, gradients, shadows,
or unnecessary detail.

For Tutorial Mode, also regenerate when the image is too empty, lacks an action
heading, omits a command/path, provides no result, or needs an external caption
to explain what is happening.

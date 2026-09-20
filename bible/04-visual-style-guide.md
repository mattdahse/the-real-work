# The Real Work — Visual Style Guide

The archive shares **one house look with The Fifth Crusade**: every image made for either site —
chapter plates, scenes, portraits — is rendered the same way, so the two chronicles read as one
illustrated work. This file carries what a prompt needs. The long-form lessons (combat scenes,
eyelines, map plates, the ways a referenced character refuses to recede) live in the crusade's
`bible/04-visual-style-guide.md`, and they apply here unchanged.

## The look, in one line

> Cinematic, painterly fantasy realism — a lone figure lit by a single cold light source against
> a desolate, storm-lit ruin, muted earthy colours broken by one luminous accent.

## The rules

**Medium.** Painterly illustration with real brush texture and grain. Semi-realistic — grounded
anatomy and real weight, not photographs and not stylised. **Never** anime, cel-shaded, cartoon,
3-D render, comic-book ink, or flat vector.

> **The word "painterly" alone does NOT stop a photograph.** Lead the prompt with the medium as its
> own block, stated as an override, describing the physical facts of paint:
>
> *THIS IS A PAINTING, NOT A PHOTOGRAPH. A traditional narrative OIL PAINTING on canvas: visible
> directional brush strokes throughout, loaded paint and impasto in the lights, soft scumbled
> painted edges, visible canvas weave, colour mixed on a palette rather than sampled from life.
> Every surface should read as pigment. Render the background in looser, broader brushwork than
> the figure.*
>
> and put the camera words in `Avoid:` — *a photograph, photorealistic rendering, photoreal skin,
> photographic grain, a film still, DSLR photography, lens bokeh, shallow depth-of-field blur, lens
> flare, visible skin pores, hyperreal skin texture.*

**Light.** Low-key and dramatic. One dominant light placed behind or to the side of the figure so
it rims them and throws the rest into shadow. Deep shadows are welcome; never bright, even,
front-on lighting.

**Palette.** Muted and earthy: browns, blacks, ash-greys, deep oxblood, worn leather. Desaturated
overall, then **one** luminous accent that carries the image.

**Composition.** A single subject, full-body or three-quarter, with quiet gravity. Portrait
orientation, roughly 3:4, unless the scene is a standoff or a wide establishing shot (landscape).

**World.** Backgrounds are Drezen and the Marchlands — a half-searched city, scrap yards and
rope-walks, cellars and tunnels, broken walls, a ruined manor on an empty road. Desolate,
atmospheric, lived-in. No clean modern surfaces, no anachronisms.

**Finish.** High detail on faces, leather and metal; visible fabric and armour texture; soft
atmospheric depth behind. No text, no watermark, no signature, no UI, no border.

**Every figure needs an eyeline and an inner state.** Name what the figure is looking at, and give
the feeling of the instant as two or three physical tells. A calm blank face is a failure.

## The company's colours

The company were painted as a **set**, because they stand on the same map at once and must be told
apart at a glance. Keep the set in every scene that holds more than one of them:

| Character | Colour | Light |
|---|---|---|
| Riven Maelus | ash-grey and cold arcane blue | a cold blue key from the spell in his own hand |
| Dorogh Kell | bright steel and moss-grey | warm key on polished steel |
| Diddle Scribes | tan and bomb-orange | a warm glow from the flask in his hands |
| Kora Sjon | blue-black plumage, light grey cloth, pale gold | a cold key, or the faint white of her own healing |

## Devices, and the cross

**Name every religious device explicitly, and name the cross in the Avoid line.** The model
reaches for a Christian cross whenever a scene smells of priests or armoured figures, unprompted.
Shelyn's symbol is **a songbird with a long multicoloured tail feather**, in silver and
enamel — never a sun, never a sword; the world already carries Sarenrae's bare sun and Iomedae's
sword-and-sun, and a third sun-device collapses the faiths together. Dorogh carries **no device at
all**: nothing at the chest.

## Table art is not site art

Tokens and Fantasy Grounds portraits are read at forty pixels on a shared screen and are held to
a different standard — high contrast, value first, a distinct dominant colour each. They may be
brighter and more vivid than the house look. Where a campaign asset needs to appear on the site,
the table painting is a **reference to generate site-style art from**, not something published
directly. The portraits in `characters/` are the untreated paintings, which is what the site wants.

## Reusable prompt scaffold

> *[the paint override block above]*
>
> Cinematic painterly fantasy illustration, semi-realistic. **[SUBJECT — pull the likeness anchors
> from `characters/CANON.md`]**, **[action / pose]**, in **[setting: a South Bank yard at dusk, a
> cellar, the empty western road]**. Dramatic low-key lighting, strong rim light from **[single
> source]**, muted earthy palette with a single luminous **[accent from the table above]**.
> **[EYELINE — what this figure is looking at, named explicitly]**, **[INNER STATE — two or three
> physical tells]**. Portrait orientation ~3:4, high detail.
>
> **Avoid:** *[the camera words]*, anime, cartoon, cel-shaded, 3-D render, comic ink, flat vector,
> bright even lighting, oversaturated, glossy, a cross, a crucifix, any Christian symbol, modern
> clothing or objects, text, watermark, signature, border, extra limbs, deformed hands, a calm or
> blank expression, a posed portrait look, looking at the viewer.

## The iron rule: canonical likeness

When the image depicts a character listed in [`../characters/CANON.md`](../characters/CANON.md),
**supply that character's portrait to the image tool as a reference** and preserve their likeness
anchors. Never regenerate a known character from a text description alone. **Before writing the
prompt, open the portrait** — read the actual `characters/*.webp` and check the row against it.
New characters are rendered fresh in this style and, once settled, added to the registry.

Art is generated through the `chatgpt-image-gen` skill in `.claude/skills/`, which carries the
mechanics.

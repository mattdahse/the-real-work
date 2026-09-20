# Canonical Character Portraits

This directory is the **source of truth for how the people of the chronicle look.** Every named
character who has been given a face lives here as a single portrait, `characters/<kebab-name>.webp`.
When any image is generated that depicts one of them, that portrait **must** be supplied to the
image tool as a likeness reference, so they stay recognisable from picture to picture. New art
follows the house look in [`../bible/04-visual-style-guide.md`](../bible/04-visual-style-guide.md).

The company portraits were painted for the Fantasy Grounds campaign and are the **untreated**
paintings — the table copies get a contrast pass for token size, these do not. They are also the
`PORTRAITS` map in `index.html`, keyed by the exact Cast name.

**Diddle's portrait was repainted on 2026-09-20.** The previous file was a flat cartoon character
sheet: thick outlines, flat fills, cel shading. Its *design* is canon and the repaint was built
from it — the mask, the notched ear and its cuff, the lattice-stitched coat, the vial colours —
but it was unusable as a likeness reference, because handing a cartoon to an image tool drags the
whole render out of the house look, and on the Personalities page it sat beside three oil
paintings looking like a sticker. If another portrait ever arrives in a foreign style, do the same
thing: keep the design, repaint the medium, and say so here.

> **The mask, and the mistake that came out of it.** The first repaint read the cartoon's four
> glowing holes as four eyes and gave him a four-eyed face with a long ridged nose and a tiny
> mouth. It is a mask, and the error had already been written into this file and the bible before
> anyone looked at the art closely. **Read the source image before trusting a written anchor**,
> and when a description and a picture disagree, the picture is the character.
> The original cartoon is preserved in git at `d8c0c43:characters/diddle-scribes.webp` and is the
> design reference to hand the image tool for any Diddle art.

**Identity here, gear elsewhere.** This file fixes what never changes — face, build, colouring,
species markers. At first level their gear is plain and dented; when the company re-equips, note
the change in the row rather than repainting the face.

## Registry

| Character | Portrait | Cast group | Likeness anchors (keep these constant) |
|---|---|---|---|
| **Riven Maelus** | [`riven-maelus.webp`](riven-maelus.webp) | The Company | **Tiefling** man, early twenties, lean and road-worn. **Ash-grey skin, a pair of swept-back ridged horns, pale blue eyes that carry their own light**, dark hair cropped close at the sides; **faint drawn sigils inked along both forearms**. A dark travel-worn coat with a plain ring-clasp, one shoulder gone ragged; nothing ornamental. Expression: level, unhurried, watching something off to one side. *Avoid:* robes, a staff, a pointed hat, a spellbook held open, finery, a beard, warm or golden light, a smile. Confirmed tiefling; the portrait carries over from the character's earlier name unchanged. |
| **Dorogh Kell** | [`dorogh-kell.webp`](dorogh-kell.webp) | The Company | Half-orc man, early twenties, **noticeably bigger than a human** — broad neck, heavy shoulders. More orc than human: heavy brow, broad jaw, **grey-green skin**, **ears subtly pointed** (never round human ears — renders drift), **two small clean lower tusks**, dignified, never a brutish underbite. **Plain round wireframe spectacles**, small on a large face. **An open-faced steel nasal helm** that hides nothing. Battered mail, a padded collar; **nothing at the chest — no pendant, no device**. Expression at rest: a deliberate, slightly self-conscious attempt at looking friendly — closed-mouth smile, brows a little raised, steady eye contact. **In a fight he is allowed a full open-mouthed battle roar**, brows driven down, eyes wide and furious, tusks showing: that is rage and it reads as rage. What is forbidden is the *grin* — a bared-teeth smile on a tusked face reads as caricature instantly. *Avoid:* a grin, a smirk, a sneer, a goofy or stupid expression, huge tusks, a full-face or horned helm, modern glasses, a cross or holy symbol, an old man. |
| **Diddle Scribes** | [`diddle-scribes.webp`](diddle-scribes.webp) | The Company | Goblin man, small and **leaner than the usual goblin**; greenish-tan freckled skin. **His face is an ordinary goblin face: two eyes, a broad flat nose, a wide mouth.** In the field it is hidden behind **a rigid faceted alchemist's mask** of dark oiled leather over plate, covering the whole face — a vertical seam down the centre, radiating seams below it, small rivets at the joins, and **four round holes: the upper two are eye-holes with his eyes behind them, the lower two are smaller, set closer together, and are for breathing.** Pale alchemical vapour curls around it. A **deep hood** over the mask; **very large tapered ears** stand clear of it, the left one notched and hung with a plain metal cuff. Quilted tan lattice-stitched coat over a long brown work-coat, dark leather gloves, heavy boots, and a **belt and bandolier of pouches and stoppered vials** — green, blue, violet. Usually holding an **orange bomb-flask**. He takes the mask and hood off indoors once he is warm and settled. Expression (unmasked): curious, guileless, mid-explanation. *Avoid:* **four eyes on his actual face, a long ridged nose, a tiny mouth** — all three are misreadings of the mask; also a snarl, bared teeth, a manic grin, red eyes, a hobgoblin's bulk, warpaint, a hooked nose, tribal rags, a cauldron. |
| **Kora Sjon** | [`kora-sjon.webp`](kora-sjon.webp) | The Company | Tengu woman of thirty-three, 5'7" and a shade taller than a human woman — glossy blue-black plumage over the whole body, a **raven's head and neck**, a **heavy dark grey beak**, one **amber-gold eye** visible in profile, a ruff of layered neck feathers; **hands humanlike, legs birdlike** (the portrait keeps the hands dark and claw-tipped, but they are hands, not talons). A **deep hood lined in pale gold knotwork** worn back off the face, a **feathered mantle** over dark layered vestments, a slate sash, and **hanging chains of small charms — a compass-rose disc, a crescent** — with a rolled scroll at the hip. Carries a **tall crook-headed wooden staff with a lit lantern swinging from it**. Expression: composed, looking off past the viewer. *Avoid:* a human face, a beak-shaped mask over human features, a parrot's colouring, an owl, bright plumage, armour, a holy symbol on a cross, a grin. *Note:* Freya's own description dresses her in a **light grey** dress and hooded robe; the portrait she supplied is much darker. Painted cloth follows the portrait, but grey is the cloth she names — worth confirming before any full-figure art. |

## Known drift

Things the model invents unless forbidden explicitly. Copy the relevant lines into the prompt
body *and* the `Avoid:` line.

- **The cross.** Any priest, any armoured figure, any chapel — a Latin cross appears unprompted.
  Name the true device explicitly and name the cross in Avoid. Dorogh gets no device.
- **Human ears on Dorogh.** Half-orc ears come back round; state *subtly pointed and tapered*
  and put *round human ears* in Avoid.
- **Teeth on Dorogh.** A bared-teeth smile on a tusked face reads as caricature instantly. His
  smile is closed-mouth, every time.
- **Warm skin on Dorogh.** Half-orc skin under a torch renders warmer than asked; the portrait was
  greyed by warmth after the fact. Ask for grey-green and check it.

## The module's portraits

The Fantasy Grounds module **The Marchlands Commission** carries a painted portrait for every
named person in it, in this same house look, and those are the paintings Matt shows at the table.
**They are canon on sight.** When a person is met in play, copy their portrait across rather than
generating a new one:

```
%APPDATA%\SmiteWorks\Fantasy Grounds\modules\The Marchlands Commission.mod   (a zip)
  portraits\<kebab-name>.webp      full-size, what belongs here
  tokens\<kebab-name>.webp         the table token, contrast-passed; not this
  images\<scene>.webp              scene and battle maps
```

The module also holds portraits for people the company has **not** met. Do not copy those across
and do not add them to `PORTRAITS`: the gallery shows no one the players have not met.

Brought over after session 1, keyed to their Cast names and wired into `PORTRAITS`:

| Character | Portrait | Cast group |
|---|---|---|
| **Mira Thistledance** | [`mira-thistledance.webp`](mira-thistledance.webp) | Employers |
| **Jory Tallow** | [`jory-tallow.webp`](jory-tallow.webp) | Met in Drezen |
| **Pip Venn** | [`pip-venn.webp`](pip-venn.webp) | Met in Drezen |
| **Oskar Venn** | [`oskar-venn.webp`](oskar-venn.webp) | Met in Drezen |
| **Wat Crake** | [`wat-crake.webp`](wat-crake.webp) | Met in Drezen |
| **Marit Olsk** | [`marit-olsk.webp`](marit-olsk.webp) | Met in Drezen |
| **Bruna Aske** | [`bruna-aske.webp`](bruna-aske.webp) | Met in Drezen |
| **Old Hrenna** | [`old-hrenna.webp`](old-hrenna.webp) | Met in Drezen |
| **Hobb Garrow** | [`hobb-garrow.webp`](hobb-garrow.webp) | Met in Drezen |
| **Aldo Fenn** | [`aldo-fenn.webp`](aldo-fenn.webp) | Met in Drezen |
| **Liesl Ambry** | [`liesl-ambry.webp`](liesl-ambry.webp) | Met in Drezen |
| **Dun Ferrow** | [`dun-ferrow.webp`](dun-ferrow.webp) | Met in Drezen |
| **Ketta Holm** | [`ketta-holm.webp`](ketta-holm.webp) | Met in Drezen |
| **Piet Harl** | [`piet-harl.webp`](piet-harl.webp) | Met in Drezen |
| **Hesk Dolvan** | [`hesk-dolvan.webp`](hesk-dolvan.webp) | Adversaries |
| **Alia Dolvan** | [`alia-dolvan.webp`](alia-dolvan.webp) | Adversaries |

Available in the module and **not** brought over yet, because the company has not met them:
`sera-dolvan`, `corin-dolvan`, `dolvan-infant`, `yard-dog`, and the whole of the manor cast.

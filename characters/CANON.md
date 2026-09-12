# Canonical Character Portraits

This directory is the **source of truth for how the people of the chronicle look.** Every named
character who has been given a face lives here as a single portrait, `characters/<kebab-name>.webp`.
When any image is generated that depicts one of them, that portrait **must** be supplied to the
image tool as a likeness reference, so they stay recognisable from picture to picture. New art
follows the house look in [`../bible/04-visual-style-guide.md`](../bible/04-visual-style-guide.md).

The company portraits were painted for the Fantasy Grounds campaign and are the **untreated**
paintings — the table copies get a contrast pass for token size, these do not. They are also the
`PORTRAITS` map in `index.html`, keyed by the exact Cast name.

**Identity here, gear elsewhere.** This file fixes what never changes — face, build, colouring,
species markers. At first level their gear is plain and dented; when the company re-equips, note
the change in the row rather than repainting the face.

## Registry

| Character | Portrait | Cast group | Likeness anchors (keep these constant) |
|---|---|---|---|
| **Trivius Malrec** | [`trivius-malrec.webp`](trivius-malrec.webp) | The Company | Tiefling transmuter — likeness anchors TBD; bio and look not yet set. |
| **Wende Sandhauler** | [`wende-sandhauler.webp`](wende-sandhauler.webp) | The Company | Dwarf woman, mid-thirties, stocky and broad-shouldered. **Copper-red hair in tight braids bound with dull steel rings, grey stone dust worked into them**; strong brow; a broad nose broken once; ruddy freckled skin; pale grey eyes. **No beard** — short sideburns. Hands too big for her. Battered chain shirt over a padded coat, plain steel shield on the left arm, a warhammer. *Avoid:* a beard, a horned helmet, plate, polished or heraldic armour, gold, blue or green light, a cheerful grin. |
| **Esper Toevel** | [`esper-toevel.webp`](esper-toevel.webp) | The Company | Human man, late twenties, lean and quick-faced. Dark brown hair a little long and pushed back, a few days' stubble, brown eyes. **Deep green wool coat with tarnished brass buttons** over a travel-worn shirt, a wound scarf, cuffs frayed; **a small brass-fitted stringed instrument carried high against the chest**. *Avoid:* a feathered cap, motley, a jester, a lute held out at arm's length, finery, red or copper hair, orange light, a broad theatrical grin. |
| **Jules Arine** | [`jules-arine.webp`](jules-arine.webp) | The Company | Human woman, early thirties. Warm brown skin, dark hair pinned up with loose strands escaping, dark eyes, a calm level face that is not sweet. Plainly cut travel-worn robes in **dove-grey and rose** over a padded gambeson. **At her throat on a silver chain, her only ornament: a small silver-and-enamel songbird with a long multicoloured tail feather** — the only saturated colour on her. A glaive across the back, barely noticed. *Avoid:* a cross or any Christian symbol, a sun, a sunburst, a halo, a sword device, white-and-gold vestments, a mitre, a wimple, plate, gold jewellery, a beatific smile. |
| **Dorogh Kell** | [`dorogh-kell.webp`](dorogh-kell.webp) | The Company | Half-orc man, early twenties, **noticeably bigger than a human** — broad neck, heavy shoulders. More orc than human: heavy brow, broad jaw, **grey-green skin**, **ears subtly pointed** (never round human ears — renders drift), **two small clean lower tusks**, dignified, never a brutish underbite. **Plain round wireframe spectacles**, small on a large face. **An open-faced steel nasal helm** that hides nothing. Battered mail, a padded collar; **nothing at the chest — no pendant, no device**. Expression: a deliberate, slightly self-conscious attempt at looking friendly — closed-mouth smile, brows a little raised, steady eye contact. *Avoid:* bared teeth, a grin, a snarl, a goofy or stupid expression, huge tusks, a full-face or horned helm, modern glasses, a cross or holy symbol, an old man. |
| **Diddle Scribes** | [`diddle-scribes.webp`](diddle-scribes.webp) | The Company | Goblin man, small and **leaner than the usual goblin**. **Four small yellow eyes** in two pairs, set in shadow under a deep hood; **very large tapered ears**, the left one notched and hung with a plain metal cuff; greenish-tan freckled skin, only the ears and the lower face ever catching light. Quilted tan lattice-stitched coat over a long brown work-coat, dark leather gloves, heavy boots, and a **belt and bandolier of pouches and stoppered vials** — green, blue, violet. Usually holding an **orange bomb-flask**. Expression: curious, guileless, mid-explanation. *Avoid:* a snarl, bared teeth, a manic grin, red eyes, two eyes, a hobgoblin's bulk, warpaint, a hooked nose, tribal rags, a cauldron. |

## Known drift

Things the model invents unless forbidden explicitly. Copy the relevant lines into the prompt
body *and* the `Avoid:` line.

- **The cross.** Any priest, any armoured figure, any chapel — a Latin cross appears unprompted.
  Name the true device (Shelyn's songbird) and name the cross in Avoid. Dorogh gets no device.
- **Human ears on Dorogh.** Half-orc ears come back round; state *subtly pointed and tapered*
  and put *round human ears* in Avoid.
- **Teeth on Dorogh.** A bared-teeth smile on a tusked face reads as caricature instantly. His
  smile is closed-mouth, every time.
- **Warm skin on Dorogh.** Half-orc skin under a torch renders warmer than asked; the portrait was
  greyed by warmth after the fact. Ask for grey-green and check it.
- **Wende's beard.** A dwarf reads as bearded to the model whatever the prompt says. *No beard*
  goes in Avoid every time.
- **Esper's instrument.** Held out at arm's length it leaves the crop; it is carried high against
  the chest.

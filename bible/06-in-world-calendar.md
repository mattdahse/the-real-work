# The Calendar of The Real Work

*The in-world date authority for the chronicle. Golarion reckoning, year 4713 AR.*

The campaign's days are kept in **Fantasy Grounds**, on the campaign calendar of *The Real Work*.
This file is that record rendered into the chronicle's voice; the untouched extraction lives
beside it in `06-in-world-calendar.json`, which is machine-written and should never be
hand-edited. Regenerate the JSON with `pwsh -File ./extract-calendar.ps1` from the repo root,
then write any new days into this file by hand.

**Published.** `build.ps1` reads the month sections below into `window.JOURNAL`, and the site's
**Timeline** tab shows each day's entry beside the chapters that cover it. Everything after the
horizontal rule — the silent days and the open discrepancies — stays authoring matter and is not
read by the build. So this file is both the reference chapters are checked against *and* the text
the Timeline displays: write it in the chronicle's voice, and keep it accurate.

A chapter's place on that Timeline comes from its own `<!-- inworld: … -->` marker in `source/`,
not from this file. When a chapter's dates change, change both.

The campaign begins after **Drezen changed hands on the 13th of Rova, 4713 AR**. The same year
and the same weekday cycle as The Fifth Crusade's chronicle: a date here and a date there name
the same day.

**Format.** One `## <Month>, 4713 AR` heading per month (`## Neth, 4713 AR`), then one bullet
per recorded day: the day's number in bold, then an em-dash, then the entry —
`- **14th** — The **South Bank** watched from **Cinder Row** until dusk.` A wrapped continuation
line is indented. Third person, **bold** proper names, ***italic*** relics and spells, no
mechanics. (The example is written inline here on purpose: a real heading in this file, even
inside a code fence, is read by the build as a month.)

## Neth, 4713 AR

- **26th** — Four strangers were standing in **Drezen's** market when **Jory Tallow** climbed a
  crate, preached the coming of **Deskari**, and kicked the side out of a box holding four giant
  centipedes. **Riven Maelus**, **Dorogh Kell**, **Diddle Scribes** and **Kora Sjon** killed all
  four between them. A baker's daughter named **Pip Venn** was bitten through and lived, because a
  tengu stopped her bleeding under her father's handcart and a goblin spent a healing potion on
  her. **Mira
  Thistledance** watched the whole thing from a second-floor window, had the boy tied to a chair
  in her office by evening, and hired the four of them as her first strike team for a hundred and
  fifty gold and a note to the citadel library. That night they read what the books had on
  **Deskari** and on **Baphomet**, and found the two of them allies rather than rivals.
- **27th** — The company crossed the dry **Ahari** into the **South Bank** and walked the fence of
  a scrapyard on **Cinder Row**: eight feet of uneven plank, two chained dogs, and the labyrinth
  of **Baphomet** inked on the man who quoted them a copper a pound for good steel. They spent an
  hour building a sled and loading it with honest salvage, went back in as customers, and started
  a fight they could not finish. **Riven** was dropped in a doorway by a hatchet and brought back
  with **Diddle's** last potion. The lumber was burning, a trapdoor in the floor stood chained,
  and there were children behind the doors. It ended with **Hesk Dolvan's**
  hands in the air and his account of himself across his own kitchen table: a knee taken to
  **Baphomet** to stay out of a collar, slave tunnels under his floor, and **the Labyrinth**
  lodging in them. The company left his strongbox with him, called it a robbery, and went back to
  the market, where **Mira Thistledance** paid a hundred and fifty gold apiece, became the
  Gardener, and renamed her vegetables as flowers.
- **28th** — A boy in a red dress with a rose behind his ear led the company to an abandoned
  tannery on **Cinder Row** and a ladder forty feet down. Under the **South Bank** they found
  swallows scratched low on the walls, the nest where **Jory Tallow** trapped his centipedes, and
  an old digger named **Emmet**, called the Mole, clearing a rockfall that still falls every few
  minutes for the six slaves under it. They dug the six out in an hour and a half. He led them
  past the thing in the midden pit, which he calls **the Bishop** and which **Dorogh** fed, and
  stopped at the mouth of a cavern nobody can cross without a torch.

---

## Silent days

- **24 Neth, 4713** — logged in Fantasy Grounds with no entry. Nothing at the table happened on it;
  it is the campaign's setup day.

## Open discrepancies

Between what was said at the table and what the Fantasy Grounds module *The Marchlands
Commission* records. The chronicle follows the table in every case below; Matt rules.

- **When Drezen fell.** The bible, the in-world calendar and The Fifth Crusade's chronicle all
  give **the 13th of Rova, 4713**. Two of the module's NPC notes (Old Hrenna, Wat Crake) say
  **the 13th of Neth** and "the taking this Neth". Chapter I says the market was "ten weeks out of
  demon hands", which is the 13th of Rova to the 26th of Neth. If Neth is right, the whole
  campaign is thirteen days after the liberation instead of ten weeks, and a good deal of the
  city's settledness has to go.
- **Jory Tallow's age.** The module calls him a twenty-year-old. At the table he was played as
  sixteen and "not shaving yet". Chapter I has him at sixteen at most, and **his portrait was
  repainted on 2026-09-20 to match the table** rather than the module, so the prose and the picture
  now agree. The module's own art still shows a man in his twenties.
- **Jory's master.** The module has the master die in the fire at Kenabres. At the table he is
  alive in Drezen, keeps the candle shop, and closed it to go and speak for the boy. Chapter I has
  him alive.
- **The man Dorogh brained.** Chapter I as first published said Dorogh *killed* the worker at the
  breakfast table. In session 2 he was dying, not dead: Kora stabilised him and Hesk called him
  "Stewie". Chapter I now reads "put down". "Stewie" is audio-only and has no module entry.
- **The tannery ladder.** The module gives a short wooden ladder; at the table it went down forty
  feet. Chapter II says forty.
- **When the Bakehouse branch fell.** At the table Emmet said the six died "about four years ago".
  The module does not date it. Chapter II says four years.
- **The Bishop's day.** The module's Bishop asks whether it is Sunday. At the table it said "It's
  Moon Day", which matches the 28th. Chapter II follows the table.
- **Alia Dolvan's term.** The module says seven months gone; at the table she was "due in weeks,
  not months". Chapter I says only that she is heavily pregnant.

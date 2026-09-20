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
  and there were children behind the doors when the day broke off.

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
  sixteen and "not shaving yet". Chapter I has him at sixteen at most.
- **Jory's master.** The module has the master die in the fire at Kenabres. At the table he is
  alive in Drezen, keeps the candle shop, and closed it to go and speak for the boy. Chapter I has
  him alive.
- **Alia Dolvan's term.** The module says seven months gone; at the table she was "due in weeks,
  not months". Chapter I says only that she is heavily pregnant.

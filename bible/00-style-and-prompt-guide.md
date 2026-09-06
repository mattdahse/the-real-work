# Campaign Bible — Style & Prompt Guide

*The Real Work — A Chronicle of the Ground-Level Campaign at Drezen*

This is the authoring source of truth for the chronicle's **voice**. Read it before drafting any
chapter. The voice is the one The Fifth Crusade's chronicle keeps: this is a second table in the
same world, and the two archives should read as one hand.

## I. Campaign Meta

- **System:** Pathfinder 1e. A homebrew campaign, *The Marchlands Commission*, run alongside
  *Wrath of the Righteous*. The Fantasy Grounds campaign is named **The Real Work**, and so is
  this site.
- **Premise:** Drezen changed hands on the 13th of Neth, 4713 AR, and is still learning how to be
  a city again. While the mythic four fight their way west, the cohorts they left behind hire
  whoever is standing in Drezen to keep the road open, the shrine supplied, and the city fed. The
  company are those people — 1st level, unaffiliated, and picked for it.
- **Scope:** Book I, *The Marchlands Commission* — the commissions one after another, beginning
  with the South Bank job.
- **Party moniker:** none yet. Record it here when the table settles one.

### The Company (player → character)

Player names are not recorded yet — fill them in here. They live only in the bible, never in the prose.

- **? → Theep Gvosh** — tiefling evoker; ash-grey skin, short ram's horns, eyes with no whites,
  and a spell light that burns cold blue-white. His familiar **Snicker**, an old ginger monkey,
  goes where he goes.
- **? → Wende Sandhauler** — quarry dwarf; shield, warhammer, a dented chain shirt, and copper
  braids bound with steel rings.
- **? → Esper Toevel** — human bard of the road; green wool, tarnished brass, an instrument kept
  close.
- **? → Jules Arine** — human priestess of Shelyn; dove-grey and rose, a silver-and-enamel
  songbird at her throat, a glaive across her back.
- **? → Dorogh Kell** — young half-orc fighter, bigger than a human, in an open nasal helm and
  plain wire spectacles. Sharper than he looks and knows it.

*Matt runs the game.*

## II. Tone & Formatting Rules

- **Perspective:** Third-person omniscient, focused on the company's actions.
- **Tone:** Grounded high-fantasy chronicle — reads like a novel or a sourcebook page. Dramatic
  weight without melodrama or outright comedy.
- **Scale:** These are first-level people doing the half of the war the heroes have outgrown.
  Keep the weight without borrowing the crusade's scale: a yard dog is dangerous, a broken arm is
  a week, a hundred gold is a fortune, and a cellar can kill everyone.
- **Exclusions:** No out-of-character banter, no dice numbers, no rules or mechanics talk, no
  table cross-talk. Translate every mechanical outcome into narrative (a failed save is a spell
  taking hold; a critical is a decisive, telling blow; a level is a turning point, not a milestone).
- **In-game names only** in the prose. Player names live only here in the bible.

### Markdown conventions (the build depends on these)

- Chapter header: `## **Title**` — **no chapter number**; the build numbers chapters by position.
- An italic subtitle line: `*<Month Day, Year> session — <in-game framing>*`. The build reads the
  real-world play date off it. If the subtitle cannot carry one, add `<!-- date: Month Day, Year -->`.
- `<!-- inworld: 14 Neth 4713 to 15 Neth 4713 -->` — the chapter's in-world span, which places it
  on the Timeline. Prefix `approx` if the Fantasy Grounds log never recorded it.
- `<!-- fathom: call=<call-id> recording=<recording-id> -->` — the session's recording, both ids.
  Not rendered.
- Body organised into `### **Subsection**` beats. **Bold** proper names; ***triple-asterisk
  italic*** for spells, items and relics.
- A standalone `![Caption](images/<file>.webp)` line renders as a captioned figure.
- Close with `*— Session of <Month Day, Year> —*`.

### Continuity guardrail

Chronicle only what happened at this table. The Fifth Crusade's chronicle is canon for the world
the company walks through — Drezen's streets and offices, Lupenor's Market, Iomedae's Preservers,
the Fane in the west — and may be read for it. But nothing the mythic four learn reaches this
company unless someone in Drezen tells them, and the company's own discoveries stay theirs.

## III. Where the truth lives

- **Chronicle source:** `source/book-1-the-marchlands-commission.md`.
- **Bible:** this file, `02-dramatis-personae.md`, `03-lore-and-locations.md`,
  `04-visual-style-guide.md`, `06-in-world-calendar.md`.
- **Likenesses:** `characters/CANON.md`.
- **Published site:** built from the source markdown via `build.ps1` → `data.js`, served by
  `index.html` on GitHub Pages.

The end-of-session workflow (read the sources, write the next chapter, rebuild, commit, push) is
defined by the `real-work-chronicle` skill.

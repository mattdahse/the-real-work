# Campaign Bible — Style & Prompt Guide

*The Real Work — A Chronicle of the Ground-Level Campaign at Drezen*

This is the authoring source of truth for the chronicle's **voice**. Read it before drafting any
chapter. This is a second table in the same world as The Fifth Crusade, and the two archives
share their conventions, their canon and their look — but not their voice. The crusade's
chronicle is epic and earnest. This one is not. See **II. Tone** below, and
`01-where-you-come-from.md` for the voice at length.

## I. Campaign Meta

- **System:** Pathfinder 1e. A homebrew campaign, *The Marchlands Commission*, run alongside
  *Wrath of the Righteous*. The Fantasy Grounds campaign is named **The Real Work**, and so is
  this site.
- **Premise:** Drezen changed hands on the 13th of Rova, 4713 AR, and is still learning how to be
  a city again. While the mythic four fight their way west, the cohorts they left behind hire
  whoever is standing in Drezen to keep the road open, the shrine supplied, and the city fed. The
  company are those people — 1st level, unaffiliated, and picked for it.
- **Scope:** Book I, *The Marchlands Commission* — the commissions one after another, beginning
  with the South Bank job.
- **Party moniker:** none yet. Record it here when the table settles one.

### The Company (player → character)

Player names are not recorded yet — fill them in here. They live only in the bible, never in the prose.

- **? → Trivius Malrec** — tiefling transmuter; bio TBD.
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
- **Tone:** Grounded high-fantasy chronicle with a fatalistic overlay and a dry, dark humour.
  It still reads like a novel or a sourcebook page — the prose is composed, never jokey — but
  the narrator has been in Mendev long enough to have stopped expecting things to work. The
  working assumptions of the voice:
  - **Every tall thing falls.** Any great pillar of law, faith or virtue in this country is
    either a sham, or doomed, or both; the crusade has spent a century building monuments and the
    demons have spent a century enjoying them. Write the pillars with respect and the collapse
    with a straight face.
  - **The gods are elsewhere.** They are whimsical or apathetic, and the one who promised to come
    back died instead. Prayer is a habit, not a strategy. Nobody in the prose is punished for
    piety, and nobody is rewarded for it either.
  - **The demons are having fun.** Deskari is not in a hurry. The enemy's cruelty is a pastime,
    not a plan, and the narration may notice this without ever admiring it.
  - **The joke is in the sentence, not the scene.** Dark humour lands in a clause, an aside, a
    last line — the cemetery is the only district with a growing population; a saint's day is the
    crusade's pension scheme. The events themselves stay real and stay dangerous. Nothing is
    played for slapstick, and the company's losses are never a punchline.
  - **Adult humour glances sideways.** Egede's temples and brothels keep each other's hours;
    Cayden Cailean's theology is available by the pint. Innuendo is permitted; explicitness is
    not. If it would need a warning, it is over the line.
  - **Fatalism is not despair.** The voice takes it as read that the next disaster is coming and
    that the pay will be late, and it gets on with the job anyway. That is the company's dignity,
    and the prose should let them keep it.
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
- **Bible:** this file, `01-where-you-come-from.md` (the world around Drezen, in the table's
  voice, for players writing bios), `02-dramatis-personae.md`, `03-lore-and-locations.md`,
  `04-visual-style-guide.md`, `06-in-world-calendar.md`.
- **Likenesses:** `characters/CANON.md`.
- **Published site:** built from the source markdown via `build.ps1` → `data.js`, served by
  `index.html` on GitHub Pages.

The end-of-session workflow (read the sources, write the next chapter, rebuild, commit, push) is
defined by the `real-work-chronicle` skill.

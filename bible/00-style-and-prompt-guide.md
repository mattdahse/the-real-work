# Campaign Bible: Style & Prompt Guide

*The Real Work. A Chronicle of the Ground-Level Campaign at Drezen.*

This is the authoring source of truth for the chronicle's **voice**. Read it before drafting any
chapter. This is a second table in the same world as The Fifth Crusade, and the two archives
share their conventions, their canon and their look, but not their voice. The crusade's chronicle
is epic and earnest. This one is not. See **II. Tone** below, and `secrets/lore-where-you-come-from.md`
for the voice at length (published to the Lore tab; `bible/01-where-you-come-from.md` is a pointer).

## I. Campaign Meta

- **System:** Pathfinder 1e. A homebrew campaign, *The Marchlands Commission*, run alongside
  *Wrath of the Righteous*. The Fantasy Grounds campaign is named **The Real Work**, and so is
  this site.
- **Premise:** Drezen changed hands on the 13th of Rova, 4713 AR, and is still learning how to be
  a city again. While the mythic four fight their way west, the cohorts they left behind hire
  whoever is standing in Drezen to keep the road open, the shrine supplied, and the city fed. The
  company are those people: 1st level, unaffiliated, and picked for it.
- **Scope:** Book I, *The Marchlands Commission*. The commissions one after another, beginning
  with the South Bank job.
- **Party moniker:** none yet. Record it here when the table settles one.

### The Company (player → character)

Player names are not recorded yet. Fill them in here. They live only in the bible, never in the
prose.

- **John → Riven Maelus**: tiefling; self-taught wanderer-wizard, drawn to transmutation; lost his parents in the
  raid on Blackreed and keeps an ear out for them. Reads people, remembers roads, wants a way out of
  every room.
- **? → Dorogh Kell**: young half-orc fighter, bigger than a human, in an open nasal helm and
  plain wire spectacles. Sharper than he looks and knows it.
- **? → Diddle Scribes**: goblin alchemist raised by a human shopkeeper; four small yellow eyes
  under a deep hood, oversized ears, a belt of stoppered vials. Guileless, and handy with a bomb.

*Matt runs the game.*

## II. Tone & Formatting Rules

- **Perspective:** Third-person omniscient, focused on the company's actions.
- **Tone:** Grounded high-fantasy chronicle with a fatalistic overlay and a dry, dark humour.
  It still reads like a novel or a sourcebook page. The prose is composed, never jokey, but the
  narrator has been in Mendev long enough to have stopped expecting things to work. The working
  assumptions of the voice:
  - **Every tall thing falls.** Any great pillar of law, faith or virtue in this country is
    either a sham, or doomed, or both. The crusade has spent a century building monuments and the
    demons have spent a century enjoying them. Write the pillars with respect and the collapse
    with a straight face.
  - **The gods are elsewhere.** They are whimsical or apathetic, and the one who promised to come
    back died instead. Prayer is a habit, not a strategy. Nobody in the prose is punished for
    piety, and nobody is rewarded for it either.
  - **The demons are having fun.** Deskari is not in a hurry. The enemy's cruelty is a pastime,
    not a plan, and the narration may notice this without ever admiring it.
  - **Adult humour glances sideways.** Egede's temples and brothels keep each other's hours;
    Cayden Cailean's theology is available by the pint. Innuendo is permitted; explicitness is
    not. If it would need a warning, it is over the line.
  - **Fatalism is not despair.** The voice takes it as read that the next disaster is coming and
    that the pay will be late, and it gets on with the job anyway. That is the company's dignity,
    and the prose should let them keep it.
- **How the humour is built.** The failure mode is a fact with a sarcastic tail: *the wall
  fell, which tells you something about walls.* One of those a page is a voice. One a paragraph
  is a tic. Use these instead, in roughly this order of preference:
  - **Let the world be funny.** Put the absurdity in things that exist: a notice on a door, a
    price board, a recruiting bill, a ledger with a column called *Shrinkage*, a chair kept for a
    god who is not coming. Report them deadpan and move on.
  - **Let people talk.** A named character gets one line in their own voice and the line does
    the work. Mira Thistledance, asked what the job pays: "Glory. Also a hundred and fifty gold."
    Dialogue varies the rhythm for free.
  - **Deadpan without the tail.** State the fact and stop. *Hulrun spent fifty years burning
    people to keep the demons out. The demons killed him first.* Do not add "there is a lesson in
    that." The reader has it.
  - **Specific beats abstract.** *The pay is what it is* is a gesture. *Twelve left Nerosyan,
    nine arrived* is a joke. A number, a name or an object every time.
  - **Running bits and callbacks.** A few things recur and escalate across a chapter or a book:
    Tuesday's mistake, the *Shrinkage* column, the place set for Aroden, the Order of Heralds'
    line in a table. A callback three pages later is worth five new quips.
  - **Structural jokes.** A table whose columns are the joke (*Declared* / *What it did*). A
    list where the last item breaks the pattern instead of tagging it. A form. A FAQ with the
    answers a clerk would actually give.
  - **Density.** When everything is a joke, nothing is. Keep the ten best lines in a chapter and
    let the plain sentences carry the facts. The survivors land harder.
  - **The losses are never the punchline.** The events stay real and stay dangerous. Nothing is
    slapstick. A dead friend is a dead friend; the joke, if there is one, is in what the living do
    next.
- **Scale:** These are first-level people doing the half of the war the heroes have outgrown.
  Keep the weight without borrowing the crusade's scale: a yard dog is dangerous, a broken arm is
  a week, a hundred gold is a fortune, and a cellar can kill everyone.
- **Exclusions:** No out-of-character banter, no dice numbers, no rules or mechanics talk, no
  table cross-talk. Translate every mechanical outcome into narrative (a failed save is a spell
  taking hold; a critical is a decisive, telling blow; a level is a turning point, not a milestone).
- **In-game names only** in the prose. Player names live only here in the bible.
- **No em dashes.** Not in the chronicle, not in the bible, not in the secrets or the maps. Use
  a full stop, a colon, a comma, or parentheses. The em dash is the crusade's punctuation and the
  sarcastic tail's favourite hinge; this table does without it. (The en dash in a year range,
  4622–4630, is fine.) One exception, forced by machinery: the calendar's day bullets in
  `06-in-world-calendar.md` keep their `- **14th** — ` form, because `build.ps1` parses the
  em dash there. The entry text after it follows the rule.

### Markdown conventions (the build depends on these)

- Chapter header: `## **Title**`. **No chapter number**; the build numbers chapters by position.
- An italic subtitle line: `*<Month Day, Year> session. <In-game framing>*`. The build reads the
  real-world play date off it (it looks only for the month, day and year, so the punctuation
  after the date is free). If the subtitle cannot carry a date, add
  `<!-- date: Month Day, Year -->`.
- `<!-- inworld: 14 Neth 4713 to 15 Neth 4713 -->`: the chapter's in-world span, which places it
  on the Timeline. Prefix `approx` if the Fantasy Grounds log never recorded it.
- `<!-- fathom: call=<call-id> recording=<recording-id> -->`: the session's recording, both ids.
  Not rendered.
- Body organised into `### **Subsection**` beats. **Bold** proper names; ***triple-asterisk
  italic*** for spells, items and relics.
- A standalone `![Caption](images/<file>.webp)` line renders as a captioned figure.
- Close with `*Session of <Month Day, Year>.*`

### Continuity guardrail

Chronicle only what happened at this table. The Fifth Crusade's chronicle is canon for the world
the company walks through (Drezen's streets and offices, Lupenor's Market, Iomedae's Preservers,
the Fane in the west) and may be read for it. But nothing the mythic four learn reaches this
company unless someone in Drezen tells them, and the company's own discoveries stay theirs.

The invented colour in `secrets/lore-where-you-come-from.md` (quoted lines, notices, the ledger's columns,
the chair for Aroden) is this table's canon once used in a chapter, and not before. Until then it
may be struck without consequence.

## III. Where the truth lives

- **Chronicle source:** `source/book-1-the-marchlands-commission.md`.
- **Bible:** this file, `01-where-you-come-from.md` (a pointer to `secrets/lore-where-you-come-from.md`, the world
  around Drezen in the table's voice, for players writing bios), `02-dramatis-personae.md`, `03-lore-and-locations.md`,
  `04-visual-style-guide.md`, `06-in-world-calendar.md`.
- **Likenesses:** `characters/CANON.md`.
- **Published site:** built from the source markdown via `build.ps1` → `data.js`, served by
  `index.html` on GitHub Pages.

The end-of-session workflow (read the sources, write the next chapter, rebuild, commit, push) is
defined by the `real-work-chronicle` skill.

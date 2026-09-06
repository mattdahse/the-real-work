# The Real Work — Campaign Archive

The **source of truth** for *The Marchlands Commission* — the ground-level Pathfinder campaign
that runs alongside The Fifth Crusade — and the searchable site built from it.

**Live site:** https://mattdahse.github.io/the-real-work/
**Sister site:** https://mattdahse.github.io/the-fifth-crusade/ — the same reader, the same world,
the other table.

Drezen changed hands on the 13th of Neth, 4713 AR. While the mythic four fight their way west,
the cohorts they left behind hire whoever is standing in Drezen to keep the road open, the shrine
supplied, and the city fed. The company are those people: 1st level, unaffiliated, and picked for
it. Their chronicle lives here.

The Fantasy Grounds campaign is named **The Real Work**; the module the table plays from,
*The Marchlands Commission*, is authored in The Fifth Crusade's repository under `fg/` and
compiled by its `build-fg.ps1`. That is the table's side. This repository is the chronicle's.

## Repository layout

```
source/                         ← the canonical chronicle (edit these)
  book-1-the-marchlands-commission.md   Book I (ongoing): the commissions, one after another
bible/                          ← authoring reference (voice, cast, lore, look)
  00-style-and-prompt-guide.md
  02-dramatis-personae.md
  03-lore-and-locations.md
  04-visual-style-guide.md      the house look, shared with the crusade's site; the company's colour set
  06-in-world-calendar.md       the campaign's days in the chronicle's voice → the Timeline tab
  06-in-world-calendar.json     MACHINE-WRITTEN extraction from Fantasy Grounds — never hand-edit (not yet extracted)
characters/                     ← canonical portraits (CANON.md + one .webp per face)
secrets/                        ← in-world documents → the Lore tab (empty until the company finds some)
maps/                           ← one region per file, and the places found on it → the Map tab (empty)
images/                         ← chapter plates, .webp only
build.ps1                       ← compiles source/*.md + secrets/*.md + maps/*.md + the calendar → data.js
extract-calendar.ps1            ← re-extracts bible/06-in-world-calendar.json from Fantasy Grounds
index.html                      ← the reader app (Chronicle / Timeline / Personalities / Map / Lore, search)
data.js                         ← BUILD OUTPUT — do not hand-edit
next-session.js                 ← the next game's date, hand-edited; drives the header notice
favicon.svg                     ← the site mark: a working hammer, gold on green. Edit THIS one
favicon.ico, apple-touch-icon.png   rasterised from favicon.svg by make-favicon.py — regenerate, never hand-edit
.claude/skills/                 ← Claude Code skills, checked in so they travel to every station
  real-work-chronicle/          Compile a session into a chapter, then publish
  chatgpt-image-gen/            Generate art through a logged-in ChatGPT tab
.nojekyll
```

The reader, the build and the calendar extractor are **copies of The Fifth Crusade's**, taken on
5 September 2026. The two sites are meant to look and behave the same, so when the engine gains
something over there, bring it across here (and the other way). The only deliberate differences
are the identity at the top of `index.html`, its accent colour (green here, crimson there), the
`CAST` and `PORTRAITS` blocks, the `$books` list and the secrets categories in `build.ps1`, and the
campaign name in `extract-calendar.ps1`.

Chapters are **not numbered in the markdown** — the build assigns each book's numbering by chapter
order, so inserting a chapter renumbers the rest. Each chapter's **real-world play date** is read
from its subtitle line (`*Month Day, Year session — …*`). Inline markers a chapter may carry:

- `<!-- epilogue -->` — flags the chapter as its book's Epilogue.
- `<!-- date: Month Day, Year -->` — explicit play-date override.
- `<!-- inworld: 14 Neth 4713 to 15 Neth 4713 -->` — the chapter's **in-world span**, which places
  it on the Timeline. A single day may be given alone. Prefix `approx` for a span the Fantasy
  Grounds log never recorded; those blocks are drawn with a dashed edge. Every chapter needs one.
- `<!-- fathom: call=<call-id> recording=<recording-id> -->` — dormant metadata, not rendered.
  Fathom numbers a session twice: the **call id** is in the share URL, the **recording id** is what
  the Fathom API takes. Store both.

## The calendar and the Timeline

The campaign runs on Golarion's calendar in **4713 AR**, the same year as the crusade, and the
weekday cycle in `build.ps1` is the crusade's anchor (Fire Day, the 13th of Rova) — a date on
either site names the same day. The Timeline stacks every day between the first and last chapter
markers, with the journal from `bible/06-in-world-calendar.md` on the left and each chapter drawn
as a block enclosing its days. Nothing on it is hand-placed.

`extract-calendar.ps1` reads the **The Real Work** campaign's `db.xml` at whichever station has
it and rewrites the JSON; the prose calendar is then written by hand from what is new.

## Adding a session

1. Draft the chapter into `source/book-1-the-marchlands-commission.md`, following
   `bible/00-style-and-prompt-guide.md`: a plain `## **Title**` header, the play date in the
   subtitle, the `<!-- inworld: … -->` marker, both Fathom ids.
2. Write any new days into `bible/06-in-world-calendar.md` (run `pwsh -File ./extract-calendar.ps1`
   first — it reports which days are new).
3. Rebuild the search index:
   ```powershell
   pwsh -File ./build.ps1
   ```
4. Commit and push — GitHub Pages redeploys automatically (~1 minute).

The `real-work-chronicle` skill automates all of it from a raw session transcript.

## The next session

The header carries a notice of the next game, read from the hand-edited
[`next-session.js`](next-session.js): `when` in Arizona time (always `-07:00`), a `mode` of
`'in-person'`, `'online'` or `'hybrid'`, an optional publishable `where` (never a meeting link),
and `runsHours`. The page converts the instant into each reader's own local time, says *Session
Under Way* while it runs, and once it has run out says the next session is **not yet scheduled** —
which is also what `when: null` says. The crusade's table lets the weekday decide the mode; this
table has not settled a rule yet, so the skill asks rather than guesses.

## The Cast

The Personalities tab is hand-authored in `index.html` (the `CAST` array), not built from source.
Entry shape: `['Name','one-line role']`, with `'dead'` as a third element for a ☠. These are
single-quoted JS strings — every apostrophe inside one must be a curly ’, never a straight `'`.
A portrait is wired through the `PORTRAITS` map, keyed by the exact cast name, pointing at
`characters/<name>.webp`; see `characters/CANON.md`.

## Adding a secret

Drop a markdown file in `secrets/` — a `# Title` line, an italic `*attribution*` line, then the
body. The filename prefix files it: `company-` (the company's own letters and dispatches),
`letter-` and `journal-` (recovered documents), `lore-` (history and accounts). Rebuild, commit, push.

## Adding a map

A region is one markdown file in `maps/` with an `<!-- image: images/<plate>.webp -->` marker and
one `## Place` section per marker, each carrying `<!-- at: x, y -->` in percentages of the plate,
a `<!-- kind: … -->`, and optionally `<!-- chapter: Title -->`, `<!-- letter: … -->`,
`<!-- style: icon -->` and `<!-- revealed: no -->`. A hex layer needs `<!-- surface: … -->` and
`<!-- hexes: C x R -->`. To read coordinates off a plate, open the Map tab and Alt-click the spot.
The full account of the format — kinds, the legend-as-filter, crowding, the hex projection — is
in The Fifth Crusade's README; the engine here is the same one.

`data.js` carries five globals: `window.CHAPTERS`, `window.SECRETS`, `window.CALENDAR`,
`window.JOURNAL` and `window.MAPS`.

## Running locally

Open `index.html` in any browser — it runs entirely client-side (works from `file://`). No server
or dependencies. `.claude/launch.json` also defines an `archive` server on port 8765 for the
in-app preview.

*Compiled from session transcripts (Fathom) and the emailed chapter recaps.*

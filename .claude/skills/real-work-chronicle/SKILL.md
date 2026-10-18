---
name: real-work-chronicle
description: Compose and publish recaps for Matt's second Pathfinder table — The Real Work, the ground-level campaign (The Marchlands Commission) that runs alongside the Fifth Crusade at Drezen — and keep its Cast, Lore, in-world calendar, player-email draft, and Discord #recaps post in sync. Use whenever Matt pastes a session transcript for this table, describes a session from memory, asks for a recap / chronicle update / "Chapter X" for The Real Work, asks to update its cast, add a secret, or refresh its calendar/timeline, or refers to its characters (Riven Maelus, Dorogh Kell, Diddle Scribes) or its jobs (the South Bank job, Cinder Row, the Sarkorian manor, Mira's commission). Triggers include "transcript", "recap", "session summary", "chronicle update", "Chapter X", "The Real Work", "Marchlands Commission", or any pasted multi-paragraph game-session log set in Drezen's South Bank or on the western road. If a pasted log is about Harlock, Varic, Lupenor or Rabiah it belongs to the crusade's repository and its wotr-chronicle skill instead — say so.
---

# The Real Work → Repo & Site

The campaign's **source of truth is this git repository** — the checkout you are running in, at
any of Matt's three stations (two Macs and a PC). **Never hardcode an absolute path to it**; use
repo-relative paths throughout. Public GitHub Pages site: **https://mattdahse.github.io/the-real-work/**.

This is the **second table**. The first — the mythic four of *Wrath of the Righteous* — has its own
repository (`the-fifth-crusade`) and its own skill. The two share a world, a year (4713 AR), a
reader, and a house look; they do **not** share chapters, casts or secrets. A session log about
Harlock, Varic, Lupenor or Rabiah is the other table's.

Maintaining the archive after a session means up to **seven** jobs — do all that apply:

1. **Chronicle** — write the session's chapter and publish it.
2. **Cast** — add any new persons of importance; mark the dead.
3. **Lore** — check the Fantasy Grounds Player Notes for anything new worth harvesting.
4. **Calendar** — pull the session's new in-world days out of Fantasy Grounds.
5. **Player draft** — leave a Gmail *draft* to the players linking the latest session.
6. **Next session** — read the next game off Matt's Google Calendar into `next-session.js`.
7. **Discord** — post a short blurb and a link to the new chapter in the server's #recaps, once
   Matt has approved the draft.

## Repository layout

- `source/book-1-the-marchlands-commission.md` — the chronicle. **Book I is ongoing; new sessions go there.**
  A later book is a new file added to the `$books` list at the top of `build.ps1`.
- `secrets/*.md` — a **parallel corpus** of in-world documents (the "Lore" tab), filed by filename
  prefix: `company-`, `letter-`, `journal-`, `lore-`.
- `index.html` — the reader app. **The Cast is hand-authored here** (the `CAST` array), NOT built from source.
- `bible/00-style-and-prompt-guide.md`, `02-dramatis-personae.md`, `03-lore-and-locations.md` —
  authoring reference; Matt curates these.
- `bible/04-visual-style-guide.md`, `characters/CANON.md` — the look and the likenesses.
- `next-session.js` — the next game's date, mode and length, read by the site header. Hand-written
  JS, **not** build output; `build.ps1` never touches it.
- `build.ps1` — compiles `source/*.md` + `secrets/*.md` + `maps/*.md` + the calendar → `data.js`.
  Run after any change to those.
- `extract-calendar.ps1` → `bible/06-in-world-calendar.json` — the campaign's in-world dates,
  pulled from Fantasy Grounds. Paired with `bible/06-in-world-calendar.md`, the hand-written prose
  calendar, which the build **does** publish to the Timeline.
- Chapters are **not numbered in the markdown**; the build assigns Roman numerals by position
  (`<!-- epilogue -->` marks a book's last chapter as its Epilogue). Each chapter's **real-world
  play date** is read from its subtitle line. If a subtitle can't carry a full date, add
  `<!-- date: Month Day, Year -->`.

**Encoding:** always read/write with `[IO.File]::ReadAllText/WriteAllText` (UTF-8), never
`Get-Content -Raw`. Never type an em-dash literal into a `.ps1` — use `[char]0x2014`. Use
**PowerShell 7 (`pwsh`)** at every station; 5.1 serialises JSON differently and churns `data.js`.

## Inputs

- **A session transcript** pasted in chat, **or Matt's description** from memory, **or** just "do
  the recap" (figure out the next chapter from the chronicle).
- The session's **real-world play date** — put it in the subtitle. If unknown, check Matt's Google
  Calendar. **Event naming rule (Matt, 2026-09-20):** an invite naming **"The Real Work"** is this
  table; one naming **"Wrath of the Righteous"** is the crusade's table in `the-fifth-crusade`.
  The live events read `Pathfinder - The Real Work`. Match on the title, then confirm on the date.

### The table (recorded 2026-09-20, session 1)

| Player | Character | Email |
| --- | --- | --- |
| John Lake | Riven Maelus | johnclake102@gmail.com |
| Alexander Cantella | Dorogh Kell | ajcantella@gmail.com |
| Jeremy Weathers | Diddle Scribes | renjitwulf@gmail.com |
| Freya Dahse | Kora Sjon | fdahse12@gmail.com |

Matt runs the game (mattdahse@gmail.com). Player names live here and in the bible, **never in the
prose**. Fathom's speaker labels are still not trustworthy; use this table to sanity-check, not to
attribute.

## The module — read it before writing, every time

Matt's homebrew Fantasy Grounds module **The Marchlands Commission** is the campaign's own
reference, and it outranks the transcript on every name, spelling, description and background.
Fathom mangles names badly; the module has them right. It is a zip:

```
%APPDATA%\SmiteWorks\Fantasy Grounds\modules\The Marchlands Commission.mod
  db.xml                         npc / battle / treasureparcels / quest / encounter / library
  portraits\<kebab-name>.webp    full-size portraits, house look, canon on sight
  tokens\<kebab-name>.webp       contrast-passed table tokens, not for the site
  images\<scene>.webp            scene and battle maps
```

Read the `npc` nodes for everyone the session touched: each carries a *Description*, *Tactics* and
*Roleplaying* block, and the Roleplaying block is where the character actually lives. Convert FG
formattedtext the same way as the Player Notes in step 3. The live campaign's own `db.xml` holds
no NPCs of its own, so the module is the only roster.

**The spoiler line.** The module is written for the GM and contains a great deal the company has
not found: what is under the scrapyard floor, the cult's name, the manor, and people they have not
met. Use it for **who somebody is** once the company has met them, and for correct names,
descriptions and backgrounds. Do **not** publish live plot the party has not uncovered, and do not
add an unmet person to the Cast or to `PORTRAITS`.

**Where the module and the table disagree, the table wins** — the chronicle records what happened
in front of the players — and the disagreement goes in **Open discrepancies** in
`bible/06-in-world-calendar.md` so Matt can rule on it.

## Recording metadata — record BOTH ids

Fathom gives a session **two different numbers**: the **call id** in the share URL
(`https://fathom.video/calls/650843307`) and the **recording id** that every Fathom tool takes as
`recording_id` (`141062294`). Passing a call id to `get_meeting_transcript` fails with *"recording_id
not found or access denied"*, which reads like a permissions problem and is not one. Every chapter
written from a recording stores both:

```
<!-- fathom: call=650843307 recording=141062294 -->
```

To get the pair, call `list_meetings` bounded to the play date and read `recording_id` and `url`
off the entry — the number in `url` is the call id, the `id` field is the recording id. Match on
the **date**, not the title. `build.ps1` strips the line before rendering.

Transcripts run long; pull them in sequential chunks of ~250–300 lines and read all of it.
**Speaker labels in Fathom transcripts are unreliable.** Identify who did what from *content* —
a bomb is Diddle's, a transmutation is Riven's, a sword-blow is Dorogh's — not from the
name on the line.

## Workflow — 1. The chapter

**Load first (always):** `bible/00-style-and-prompt-guide.md` (voice — read every time);
`bible/02-dramatis-personae.md` (names/spellings); `bible/03-lore-and-locations.md`; and the
**end of `source/book-1-the-marchlands-commission.md`** to match the current voice and continuity.
For the first chapter there is no end to match — match the crusade's chronicle instead, which the
bible says is the same hand.

**Scope:** new chapter (append), continuation (rewrite the prior ending to flow in), or ambiguous
(ask Matt — don't guess boundaries).

**Extract beats:** combat turning points, criticals, deaths; decisions, promises, who was paid and
what for; discoveries (people, places, documents, the thing under the floor); levels as *story
beats*. **In-game names only** in prose. **Keep the scale honest** — see the bible's *Scale* rule:
these are first-level people, and the chronicle should never sound like the crusade's.

**Draft in house style** (plain title, no chapter number):
```
## **<Title>**

*<Month Day, Year> session — <in-game framing>*

<!-- inworld: 14 Neth 4713 to 15 Neth 4713 -->

<!-- fathom: call=<call-id> recording=<recording-id> -->

### **<Subsection>**
<prose with **bold names** and ***italic spells/relics***>
…
*— Session of <Month Day, Year> —*
```
Translate all mechanics into narrative — no OOC, dice, or rules talk. Then **append** it to the end
of Book I (or, for a backfill, insert it by date between the chapters that bracket it).

## Workflow — 2. The Cast (`index.html`)

Scan the recap for **new persons of importance** and update the `CAST` array:
- **New employers or allies** → the `Employers` section, or a new section if the company gathers
  people of its own.
- **New enemies** → an `Adversaries` section (create it after `Employers` the first time).
- **Deaths / reveals** → update the entry; add `'dead'` as a third element for a ☠.

Entry shape: `['Name','one-line role']`. **CRITICAL:** single-quoted JS strings — every apostrophe
*inside* must be a **curly ’** (U+2019), never a straight `'`, or the page breaks silently. Cast
edits need no rebuild, but re-read the edited entries to confirm.

**Portraits.** A cast member with a portrait shows a thumbnail on the gallery. The likeness lives in
`characters/` and is wired via the `PORTRAITS` map (`'<Cast Name>': 'characters/<file>.webp'`). The
company portraits are already there; to give a new character a face, follow
`characters/CANON.md` and the `chatgpt-image-gen` skill. Keep what the site publishes to what the
players know — the module's GM material in the crusade repository's `fg/` is not a source for the
Cast until it has happened at the table.

## Workflow — 3. Lore (Fantasy Grounds Player Notes)

The players' in-world writing lives in the local FG campaign **The Real Work**
(`%APPDATA%\SmiteWorks\Fantasy Grounds\campaigns\The Real Work\db.xml` on the PC; the Mac paths are
in `extract-calendar.ps1`), under the `<notes>` node. After a session, **check for new notes** not
already represented in `secrets/`, and harvest anything worth keeping.

Extract: read db.xml with `[IO.File]::ReadAllText`, pull the `<notes>…</notes>` block, `[xml]` it,
iterate children (`$n.name`, `$n.text.InnerXml`). Convert FG formattedtext → markdown (`<h>`→`###`,
`<p>`→paragraph, `<b>/<i>`→`**`/`*`, `<list>/<li>`→bullets, strip the rest, HtmlDecode). Write each
as `secrets/<prefix>-<slug>.md` with `# Title`, an italic `*attribution*` line, then the body.
**Never write to db.xml.** Rebuild. If it's unclear whether a note is new or belongs in Lore, list
what you found and ask Matt.

## Workflow — 4. The Calendar (Fantasy Grounds campaign dates)

From the repo root: `pwsh -File ./extract-calendar.ps1`. It finds the campaign's `db.xml` at any
station, rewrites `bible/06-in-world-calendar.json` (**machine-written, never hand-edit it**), and
prints the days that are new since the last run. **Write those new days into
`bible/06-in-world-calendar.md` by hand**, in the chronicle's voice: one bullet per day under its
month heading, third person, **bold** proper names, ***italic*** relics and spells, no mechanics.
This file **is published** — the Timeline shows it — so write it to be read.

Where the log and the chronicle disagree, do **not** quietly pick a winner: render the line to
match the chronicle and add it to **Open discrepancies** at the foot of the file. If the extractor
reports no new days, Matt hasn't advanced the FG calendar; say so rather than inventing dates.

## Workflow — 5. Build, publish, and draft the player email

1. Rebuild, from the repo root: `pwsh -File ./build.ps1`
2. Commit & push (outward-facing publish — proceed, it's the skill's purpose, and tell Matt it's
   live): `git commit -am "Add <title>"` then `git push`. Pages redeploys in ~1 min; verify against
   the live URL.
3. **Leave a Gmail draft** to the players linking the latest session — `create_draft`, **never
   send**. Recipients are the four player emails in **The table** above. Subject like `The Real Work recap — <Chapter Title> (<date>)`, a one- or two-line
   teaser, and the site link. To deep-link the new chapter, use
   `https://mattdahse.github.io/the-real-work/#/read/ch<order>` where `<order>` is the chapter's
   global position (= total chapter count after the build).

## Workflow — 6. The next session (Google Calendar → `next-session.js`)

Find this table's next event on Matt's primary calendar (`list_events`, `orderBy:"startTime"`,
`startTime:` now, `timeZone:"America/Phoenix"`), take the **first that starts after now**, and write
its start in Arizona time (`-07:00`) with `runsHours` from the event's **own length**, rounded to the
half hour. **Never copy `location` into `where`** — it may be a live meeting link, and this file is
served on the public site.

**The mode.** This table has played **online** so far: session 1 ran on Zoom with Fantasy Grounds,
and the invites carry a Zoom link. Default to `'online'` and leave `where: ''`. This is a habit,
not yet a rule, and it is **not** the crusade's weekday rule (Friday online, Saturday in person):
if a session is ever called in person, Matt has to say so. If no future event exists, set
`when: null` — the header then says the next session is not yet scheduled.

## Workflow — 7. The Discord post (#recaps)

The table's Discord server, **Pathfinder - The Real Work**, keeps one short post per chapter in
**#recaps**: a blurb, one plate, and a link to the chapter on the site. **Never post the whole
chapter.** Matt ruled that out (2026-09-21) because it means too much scrolling once the sessions
pile up. This step belongs to this table only: the crusade has no Discord channel, so do not
carry it over to `wotr-chronicle`.

**Show Matt the full draft and wait for a yes before posting.** The post goes straight to the
players, and IFTTT can post but **cannot edit or delete**. A bad post has to be deleted by hand
in Discord and posted again. Post only after step 5's push is live, so the link and the plate
both resolve.

Post through the IFTTT connector with `run_action`: `service_slug: "discord"`,
`slug: "post_rich_message_to_channel"`, `account_id: 460523335` (Matt's Discord account,
`mattdahse`), and these fields:

| Field | Value |
| --- | --- |
| `channel_id` | `1549450429249748995/1551745386396385311` (#recaps) |
| `message` | `New chapter in the chronicle.` |
| `allowable_mentions` | `no_mentions` |
| `embed_title` | the chapter title, plain, with no numeral |
| `embed_description` | the blurb, a blank line, then `**[Read Chapter <N> on the archive →](<deep link>)**` |
| `embed_footer` | `Chapter <N> · <Month Day, Year> session` |
| `embed_color` | `9c6b1e` (the site's gold, `--accent2`) |
| `embed_image_url` | one plate from the chapter, on the live site: `https://mattdahse.github.io/the-real-work/images/<file>.webp` |

- **The link goes inside the embed as a masked link.** Never put it in `message` as
  `<https://…>`: IFTTT reads the angle brackets as an HTML tag and strips the link out, which is
  what happened to the first Chapter I post. A bare URL in `message` survives, but Discord unfurls
  it into a second card, and the site has no link-preview tags to make that card worth having.
- The deep link is the Gmail draft's (`#/read/ch<order>`). `<N>` is the chapter's Roman numeral.
- **The blurb** is two or three sentences in the chronicle's voice: no mechanics, no player names,
  nothing the table has not seen. Say only what the chapter says. A job offered is not a job paid:
  Chapter I's blurb reads "the promise of a hundred and fifty gold", not "a hundred and fifty gold".
- **The plate** should show the company, ideally all four of them. Check that it returns 200 on the
  live site before posting, and if more than one plate fits, offer Matt the choice.
- If the channel list ever changes, `get_actions` for `discord` with `resolve_options: true`
  lists the channels the IFTTT bot can reach.

**Posted so far:** Chapter I (2026-09-21, the tavern plate); Chapter II (2026-10-16, the Bishop plate); Chapter III (2026-10-18, the "Get in the box" plate). Add each new chapter here once it is
up, so that a later run never posts the same chapter twice.

## Illustrations & the house art style

The archive is illustrated in the same house look as the crusade's. Two files govern it:
`bible/04-visual-style-guide.md` (the look, the paint override, the company's colour set, the
no-cross rule) and `characters/CANON.md` (likeness anchors and known drift). Follow the
`chatgpt-image-gen` skill for the mechanics.

**Step 0 — pre-flight, never skip.** Before writing a prompt, `Read` the actual `characters/*.webp`
for everyone in the scene and check it against their `CANON.md` row. Attach the portraits as
references. State the corrections as explicit negatives. QA the render against the references
before publishing. A chapter-opening illustration goes between the subtitle line and the first
`###`, as `![Caption](images/<file>.webp)`; save WebP only, never commit the PNG.

## Present results

- One-paragraph summary: chapter number, session date covered, that it's live (link the site).
- What changed in the **Cast**, **Lore**, and the **Calendar**, if anything.
- That the **player draft** is ready in Gmail for Matt to review and send.
- The **Discord post**: either that it is up in #recaps, or the draft (blurb, plate, footer) waiting
  on Matt's yes.
- **Suggested bible updates** (do not silently overwrite `bible/*`): new NPCs, places, items.
- Open questions. The calendar event's name, the mode, the player emails and who plays whom are
  now recorded above; still open are the **party moniker** (Mira is still auditioning names) and
  the two audio-only spellings under **Canon spellings**.

## Canon spellings

Riven Maelus, Dorogh Kell, Diddle Scribes, Kora Sjon, James Helmsmith, Vaelus and
Seraphine Maelus, Blackreed, Threshold, Mira Thistledance, Elara Dawnstrider, Drezen, the South Bank, Cinder Row, Lupenor's Market, Iomedae's
Preservers, Rothin Vald, the Hidden Temple of Sarenrae, Deskari, Baphomet, Kenabres, the Ahari.

Verified against the module after session 1: **Jory Tallow**, **Pip Venn**, **Oskar Venn**,
**Marit Olsk**, **Ketta Holm**, **Bruna Aske**, **Old Hrenna**, **Hobb Garrow**, **Aldo Fenn**,
**Liesl Ambry** (her son **Benno**), **Dun Ferrow**, **Piet Harl**, **Wat Crake**,
**Hesk Dolvan**, **Alia Dolvan**, **Sera Dolvan**, **Corin Dolvan**, the **Two Pints and a Song**.
The candle-maker with the walrus moustache was improvised at the table and has no module entry or
name yet.

Transcripts will drift — fix all of them: Rivet, Malus/Maelus, Diddel/Dittles/Dibbles,
Doroug/Doro/Doreau/Darug, Cora/Korra, Thistledown, Dresden, Descari/Discari/Dysgari,
Canabras/Canaveras, Baphomat, Merrick/Merritt (Marit Olsk), Keta (Ketta), Oscar (Oskar), Hob
(Hobb), Dunn (Dun Ferrow), Pete (Piet Harl), Aaliyah (Alia), Dolvin (Dolvan), Creekey (Crake).
**Do not settle a name from audio when the module has it.** Add settled spellings here as the
table produces them.

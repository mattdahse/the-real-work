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

The campaign begins after **Drezen changed hands on the 13th of Neth, 4713 AR**. The same year
and the same weekday cycle as The Fifth Crusade's chronicle: a date here and a date there name
the same day.

**Format.** One `## <Month>, 4713 AR` heading per month (`## Neth, 4713 AR`), then one bullet
per recorded day: the day's number in bold, then an em-dash, then the entry —
`- **14th** — The **South Bank** watched from **Cinder Row** until dusk.` A wrapped continuation
line is indented. Third person, **bold** proper names, ***italic*** relics and spells, no
mechanics. (The example is written inline here on purpose: a real heading in this file, even
inside a code fence, is read by the build as a month.)

---

## Silent days

None yet.

## Open discrepancies

None yet.

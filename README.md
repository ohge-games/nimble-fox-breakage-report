# Nimble Fox breakage report

Where the Nimble Fox web builder breaks, collected across game builds (BLACKOUT, formerly BLACKOUT DISTRICT, and Salvage Diver).
Published at https://ohge-games.github.io/nimble-fox-breakage-report/ (GitHub Pages, `main`, root).
Each entry uses the 5W format: Who / What / When / Where / Why, then impact, mitigation and suggested fix.

| Path | What it is |
|---|---|
| `REPORT.md` | **The source.** Edit this (or send an update file); never edit `index.html` by hand. |
| `index.html` | The built page that Pages serves. |
| `updates/` | One `YYYY-MM-DD-<what>.md` per update; `APPLIED.txt` lists the ones already merged. |
| `notes/` | The note sets sent to the Nimble builder, one file per run. |
| `builds/` | Build-log summaries, one file per run. |
| `archive/` | The hand-written first edition the source was converted from. |
| `tools/` | `build_report.py`, `merge_update.py`, `publish_report.py` (Python 3, no packages). |
| `templates/report.css` | The report stylesheet, plus a status pill. |

Everything here is public.

## Merge pending updates and publish

```
python tools/publish_report.py
```

This merges every update not yet in `updates/APPLIED.txt` (in date order), builds `index.html`,
commits everything (updates, notes and builds too) and pushes. Pages updates in about a minute.
Pass a commit message as the first argument if you want one; otherwise it lists the merged files.

To look before publishing: `python tools/merge_update.py --pending --dry-run` prints the diff to
`REPORT.md`, and `python tools/build_report.py` builds `index.html` locally.

## The source: REPORT.md

- **Front matter** (between `---` lines): `title`, `h1`, `edition`, `subject`, `updated`, `facts`
  (a list of `Label: value`), `footer`, and an optional `status` banner (for example
  `Final edition: project paused 2026-12-01`). The edition line at the top of the page is built from
  `edition`, `subject`, `updated` and the severity counts in the index.
- **`# Heading`** (not rendered), then the lede paragraph.
- **Named sections** such as `## Current state {#state}`. `{#id}` sets the anchor, `{.class}` a CSS
  class. Sections above `## Index` render above the index; sections below the cards render below them.
- **`## Index`**: a table `| ID | Severity | Title | Status |`, followed by `---`. Severity is
  Critical, High, Medium or Low.
- **Cards**: `## N1. Title`, then a `**High. Why: confirmed.**` line, then fields:
  `- **Who:**`, `What`, `When`, `Where` and `Why` form the 5W list; any other `- **Field:**`
  (Impact, Mitigation, Status, Suggested fix...) is shown beneath it. Indented `  - ` lines are
  bullets inside a field, and an indented plain line after them continues the field. A field named
  `Update, 26 Oct (recovery run)` (any name starting with `Update`) renders as a dated note at the
  end of the card. A card can also be, or end with, plain paragraphs and `- ` lists after a blank
  line, shown in source order. A `---` line follows the last card.
- **`## Changelog`**: bullets, newest first.
- **Inline:** `` `code` ``, `**bold**`, `[text](https://...)`, and `{{Fixed}}` for a status pill.

The build refuses a report where an index row has no card (or the reverse), an ID is repeated, or a
card's severity disagrees with its index row.

## Update files

Each update is `updates/YYYY-MM-DD-<what>.md`, written in the same syntax as `REPORT.md`. Each
`## ` heading is one operation:

| Heading | Effect |
|---|---|
| front matter | Keys replace the report's (`edition`, `subject`, `status`...). `updated` defaults to the file's date. |
| `## Index` | Rows for existing IDs change only the cells you fill (leave a cell empty or `-` to keep it). New IDs add a row (all four cells). |
| `## N27. Title` (new ID) | Adds the card. It also needs an index row. |
| `## N6` or `## N6. New title` | Patches the card: a new title, a new `**Severity. Why: ...**` line (the index severity follows), each `- **Field:**` replaces that field or adds it, and other text is appended as a paragraph. |
| `## N6. Title {replace}` | Replaces the whole card. |
| `## Changelog` | Bullets go on top. |
| `## Current state` | Replaces that section's body (any named section; the heading only has to start the same way). |
| `## What worked {append}` | Appends to that section. An unknown section is added before the Changelog. |

`REPORT.md` is only written if the merged result passes the build's checks.

### Example: `updates/2026-11-02-full-build.md`

```markdown
---
edition: Second edition
---
## Current state
- **Full build delivered 2 Nov.** Desktop and iPhone playtests done; balance pass next.
- **The open issues that matter most:**
  - N15: the build still overheats a phone;
  - N27: the boss arena soft-locks after a death.

## Index
| ID | Severity | Title | Status |
|---|---|---|---|
| N6 | | | Fixed in the full build |
| N27 | High | The boss arena soft-locks if the player dies during the EMP phase | Open |

## N6
- **Status:** {{Fixed}} The full build draws the x-ray layer only behind walls (checked on the iPhone 18 Pro Max).

## N27. The boss arena soft-locks after a death
**High. Why: observed.**

- **Who:** Any player who dies to the ENFORCER MECH during its EMP phase.
- **What:** The arena doors stay locked on the next run and the boss never spawns.
- **Suggested fix:** Reset the arena state on run start.

## Changelog
- **2 Nov 2026 (second edition):** N27 from the full build; N6 fixed; Current state replaced.
```

Then `python tools/publish_report.py`.

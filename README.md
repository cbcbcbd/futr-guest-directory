# FUTR.tv Guest Directory

Automation for the [FUTR.tv](https://futr.tv) **Guest Directory** — one searchable table of
every podcast guest across Chris Brandt's shows (FUTR.tv originals plus the Mission cross-posts
*IT Visionaries* and *The Fleet*), each guest row linking to that episode's FUTR.tv page.

## The idea

The directory used to store its ~230 rows **inside** the live Squarespace block. That data
renders client-side and isn't machine-readable, so every update meant re-supplying all the rows by
hand — error-prone and slow.

This repo moves the **source of truth** to a machine-readable JSON file
([`data/guests.json`](data/guests.json)) and makes the Squarespace block a **dumb renderer** that
`fetch()`es it. A daily GitHub Action detects newly published episodes and commits them. Result:
**zero paste per update.** The only manual step is a one-time paste of the new block into
Squarespace (there is no Squarespace write API).

```
Squarespace Code block  ──fetch──▶  data/guests.json  ◀──commit──  GitHub Action (daily cron)
   (paste once, ever)                (source of truth)              (scripts/update_directory.py)
```

## Layout

| Path | What it is |
| --- | --- |
| [`data/guests.json`](data/guests.json) | **Source of truth.** JSON array, one object per guest row. Public raw URL is what the block fetches. |
| `data/guests.md` | Plain Markdown-table fallback (regenerated alongside the JSON). |
| `data/seen_urls.json` | Detection state — permalinks already examined (so they aren't re-fetched). |
| [`scripts/update_directory.py`](scripts/update_directory.py) | Detect new episodes, extract guest/show, merge, write JSON. Stdlib only. |
| [`block/directory-block.html`](block/directory-block.html) | The Squarespace Code block (fetches `guests.json`, renders searchable table). |
| [`.github/workflows/update-directory.yml`](.github/workflows/update-directory.yml) | Daily cron Action that runs the script and commits changes. |

## Data schema (`data/guests.json`)

One object per guest row. **All seven keys are required on every row** — the block and the script
both depend on them.

| key | meaning | example |
| --- | --- | --- |
| `g` | Guest full name | `Anthony Vinci` |
| `c` | Company / title | `Vico` |
| `s` | Show | `FUTR.tv` / `IT Visionaries` / `The Fleet` |
| `t` | Episode title | `A Former Spy Chief on How AI Really Manipulates You` |
| `d` | Date, `YYYY-MM-DD` | `2026-07-02` |
| `u` | Episode URL (FUTR.tv permalink) | `https://futr.tv/thefeed/2026/7/2/...` |
| `su` | Show category URL | `https://futr.tv/thefeed/category/Show%3A+FUTR.tv` |

`su` pattern: `https://futr.tv/thefeed/category/Show%3A+{name}` — colon → `%3A`, spaces → `+`.
A multi-guest episode is **one row per guest** (same `u`, different `g`).

> The current `data/guests.json` is a **placeholder** (obvious `Sample Guest …` rows) until the
> one-time conversion below replaces it wholesale.

## How detection works

1. Load the current `data/guests.json` (+ `seen_urls.json`).
2. Fetch the three live `Show:` category pages (newest-first). Walk each from the top and stop at
   the first permalink already known — everything above is new. Category pages are server-rendered,
   so a plain HTTP GET with a browser User-Agent is enough (no dependencies).
3. For each new permalink, fetch the post and lift the **`Guest:`**, **`Show:`**, and
   **`Company:`** tags — they render server-side as `<a rel="tag">Guest: Name</a>`. (Verified
   live.) `Company:` is emitted by the post-creation skill; older posts lack it, so company is
   left blank to fill by hand. The date comes from the permalink itself. Multi-guest posts carry
   several `Guest:` tags → one row each.
4. If a guest can't be determined, the cell is set to `[NEEDS REVIEW]` — **never guessed**.
5. Merge on `(guest, url)`: new pairs append; existing rows are preserved (keeping any manual
   edits) with only blank fields filled. A row count sanity-check guards against drops/dupes.
6. Sort newest-first, write `guests.json` and `guests.md`.

Slugs are **never constructed** — only exact permalinks from the listing pages are used.

## Running it locally

```bash
# Dry run against the live feed (fetches nothing to disk, prints what it would add):
python3 scripts/update_directory.py --dry-run

# Real run (writes data/guests.json + data/guests.md):
python3 scripts/update_directory.py
```

### One-time seed from the current published block (the conversion)

Save the currently published directory block's HTML as `current-directory.html` in the repo root,
then:

```bash
python3 scripts/update_directory.py --from-html current-directory.html --dry-run   # verify counts
python3 scripts/update_directory.py --from-html current-directory.html              # write it
```

This extracts the inlined `var DATA=[...]` array **verbatim** (typos and all — those are cleaned
later as manual edits, not during conversion) and writes it to `data/guests.json`.

## Installing / updating the Squarespace block

`block/directory-block.html` goes into a Squarespace **Code block** (needs JS/iframe support →
Business plan or higher, same dependency as the Spotify embed). You paste it **once**; from then
on all updates flow through `guests.json` and the block never changes again.

If the currently published block differs cosmetically from this reference, prefer the published
one and apply only the single change marked **`FETCH WIRING`** in this file: delete the inline
`var DATA=[...]` literal and replace it with the `fetch()` of the raw `guests.json` URL.

**Fallback:** if the Code block can't run, `data/guests.md` is a static hyperlinked table.

## The Action

[`update-directory.yml`](.github/workflows/update-directory.yml) runs daily (and on demand via the
Actions tab). It runs the script, commits `data/` if anything changed, and — if any new episode
lacks a clean guest tag — opens a **`needs-review`** issue listing them so the missing name can be
filled in `guests.json` directly. It uses the repo's built-in `GITHUB_TOKEN`; no personal keys.

## Honest limits

- One final Squarespace paste installs the new block — once, not per update. No write API exists.
- Guest naming occasionally needs a human touch when a post lacks a clean `Guest:` tag; the Action
  flags it rather than guessing.
- The block is plan-dependent (Business+). The Markdown table is the fallback.

# Using the Guest Directory from Claude chat (claude.ai project)

This note is for the **Claude.ai project side** (the skills: `guest-directory`,
`mission-feed-post`, `linkedin-episode-post`, `opus-episode-distribution`, etc.).
It explains the automation that now lives in GitHub so the chat side **defers to it
instead of reproducing it**, and shows how to use the directory data as the
**authoritative record of what's been posted**.

## What changed

The FUTR.tv Guest Directory is no longer a "re-paste all the rows each time" job.
It is a small automated pipeline:

- **Source of truth:** `data/guests.json` in
  `github.com/cbcbcbd/futr-guest-directory` (public).
  Raw URL (fetchable, no auth):
  `https://raw.githubusercontent.com/cbcbcbd/futr-guest-directory/main/data/guests.json`
- **The Squarespace block** is now a dumb renderer that `fetch()`es that JSON. It is
  pasted **once** and never edited again.
- **A daily GitHub Action** diffs the three `Show:` category pages, reads each new
  post's `Guest:` / `Show:` / `Company:` tags, and commits new rows automatically.

Each row has 7 keys: `g` guest, `c` company/title, `s` show, `t` episode title,
`d` date (YYYY-MM-DD), `u` episode URL (FUTR.tv permalink), `su` show category URL.
Multi-guest episodes are **one row per guest** (same `u`, different `g`).

## What the chat side should NOT do (don't reproduce this)

- ❌ **Do not rebuild the directory** from a pasted block or re-transcribe rows. The
  older `guest-directory` flow ("paste in the whole HTML, regenerate everything") is
  **superseded**. If the directory needs updating, the GitHub cron already does it;
  a manual run is `python3 scripts/update_directory.py` in the repo (local task, not
  a chat task).
- ❌ **Do not ask Chris to paste all ~230 rows.** The only manual step that ever
  remains is pasting `block/directory-block.html` into Squarespace **once** (already
  done unless the block itself changes).
- ❌ **Do not scrape the live directory page** to learn what's posted — it renders
  client-side and returns empty. Read `guests.json` instead.
- ❌ **`mission-feed-post` does not need a separate "update the directory" step.**
  Because it emits `Show:` / `Guest:` / `Company:` tags on each cross-post, the cron
  picks the episode up automatically within a day.

## Use guests.json as the authoritative "what's been posted" record

Treat `guests.json` as the canonical list of published **guest** episodes. Fetch the
raw URL and parse the JSON array. Use it to:

1. **Dedupe before posting.** Before creating a new Feed post or social package for an
   episode, check whether its permalink `u` already appears. If it does, it's already
   published — don't create a duplicate.
2. **Pull canonical facts.** Guest name, company, show, title, date, and the exact
   FUTR.tv permalink for any episode — use these verbatim rather than re-deriving
   (e.g. for a LinkedIn post or clip caption) so names/links stay consistent.
3. **Answer "who have we had on / what have we posted"** questions — filter by show,
   by date range, by company, by guest.
4. **Find gaps** — compare against a YouTube/Feed list to see what still needs a Feed
   post or social treatment.

Match/dedupe on `(g, u)` for a specific guest appearance, or on `u` alone for "is this
episode in the directory at all."

### Important caveats

- **Guest episodes only.** Solo/editorial/news/recap episodes with **no guest** are
  intentionally excluded. So "URL not in guests.json" means *not a published guest
  episode* — it does **not** prove the episode was never posted at all.
- **Up to ~24h lag.** The cron runs daily, so a brand-new post may not appear until
  the next run. If you need certainty for something just published, note the lag (the
  Action can also be run manually from the repo's Actions tab).
- **Manual edits live in the JSON.** Chris may fix a typo or company directly in
  `guests.json`; it stays authoritative. Don't "correct" values back from other
  sources without checking.
- **One row per guest.** A 2-guest episode is two rows sharing one `u` — don't collapse
  them.

### Minimal fetch (illustrative)

```
GET https://raw.githubusercontent.com/cbcbcbd/futr-guest-directory/main/data/guests.json
-> JSON array of {g,c,s,t,d,u,su}
```

That array is the record. Everything else (the Squarespace block, the Markdown
fallback) is generated from it.

#!/usr/bin/env python3
"""
update_directory.py — detect newly published FUTR.tv episodes and merge them
into data/guests.json (the machine-readable source of truth for the Guest
Directory Squarespace block).

Design notes (see the repo README and the build spec for full context):

* SOURCE OF TRUTH is data/guests.json — a JSON array, one object per guest row,
  with the seven keys g, c, s, t, d, u, su (see SCHEMA below). The Squarespace
  block is a dumb renderer that fetch()es this file.

* DETECTION walks the three live `Show:` category pages (newest-first) and finds
  permalinks not yet in the directory. Category pages ARE server-rendered, so a
  plain HTTP GET with a browser User-Agent is enough — no third-party deps.

* GUEST + SHOW come from the post's own tags, which render server-side as
  <a rel="tag">Guest: Name</a> / <a rel="tag">Show: Name</a>. Verified live.
  Multi-guest episodes carry several Guest: tags -> one ROW PER GUEST.

* We NEVER construct slugs. Every URL is the exact permalink lifted from a
  listing page (Squarespace slugs carry surprises like a trailing "-nmfta").

* MERGE keys on (guest, url), never url alone (multi-guest episodes share a url).
  Existing rows are preserved verbatim (they may hold Chris's manual edits);
  only blank fields get filled. A [NEEDS REVIEW] guest never overwrites a real,
  hand-filled one.

Stdlib only. Runnable locally:  python3 scripts/update_directory.py --dry-run
One-time seed from the live block HTML:  python3 scripts/update_directory.py --from-html current-directory.html
"""

from __future__ import annotations

import argparse
import html as htmllib
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #

SITE = "https://futr.tv"

# The three shows and their live category pages. New episodes can land under ANY
# of them, so all three are always checked.
CATEGORY_PAGES = {
    "FUTR.tv":        SITE + "/thefeed/category/Show%3A+FUTR.tv",
    "IT Visionaries": SITE + "/thefeed/category/Show%3A+IT+Visionaries",
    "The Fleet":      SITE + "/thefeed/category/Show%3A+The+Fleet",
}

# Repo-relative default paths (resolved against the repo root, i.e. this file's
# parent's parent, so the script works from any CWD).
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(REPO_ROOT, "data", "guests.json")
MD_PATH = os.path.join(REPO_ROOT, "data", "guests.md")
SEEN_PATH = os.path.join(REPO_ROOT, "data", "seen_urls.json")
REVIEW_PATH = os.path.join(REPO_ROOT, "data", "review_needed.txt")

SCHEMA_KEYS = ("g", "c", "s", "t", "d", "u", "su")
REVIEW = "[NEEDS REVIEW]"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36 "
    "futr-guest-directory-bot"
)

PERMALINK_RE = re.compile(r"/thefeed/(20\d{2})/(\d{1,2})/(\d{1,2})/[a-z0-9][a-z0-9-]*")
TAG_RE = re.compile(r'rel="tag"[^>]*>\s*([^<]+?)\s*</a>', re.IGNORECASE)
# Also match the (href, rel) reversed ordering just in case Squarespace flips it.
TAG_RE_ALT = re.compile(r'>\s*(Guest|Show|Company):\s*([^<]+?)\s*</a>', re.IGNORECASE)
OG_TITLE_RE = re.compile(r'<meta[^>]+property="og:title"[^>]+content="([^"]*)"', re.IGNORECASE)
TITLE_TAG_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)


# --------------------------------------------------------------------------- #
# HTTP
# --------------------------------------------------------------------------- #

def http_get(url: str, retries: int = 3, timeout: int = 30) -> str:
    """GET a URL as text with a browser UA. Retries transient failures."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                return resp.read().decode(charset, errors="replace")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last = e
            if attempt < retries - 1:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url} ({last})")


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #

def category_permalinks(html: str) -> list[str]:
    """Absolute post permalinks from a category page, in document order, deduped.

    Document order on the category pages is newest-first, so the first entry is
    the newest post. We only trust the exact strings the page emits.
    """
    seen, out = set(), []
    for m in PERMALINK_RE.finditer(html):
        path = m.group(0)
        if path not in seen:
            seen.add(path)
            out.append(SITE + path)
    return out


def date_from_permalink(url: str) -> str:
    m = PERMALINK_RE.search(url)
    if not m:
        return ""
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return f"{y:04d}-{mo:02d}-{d:02d}"


def extract_tags(html: str) -> tuple[list[str], str | None, str | None]:
    """Return (guest_names, show_name, company) from the post's rel="tag" anchors.

    `Company:` is a newer tag (added by the post-creation skill); older posts
    won't have it, in which case company comes back None and the row's `c` is
    left blank for a human to fill.
    """
    guests, show, company = [], None, None
    texts = TAG_RE.findall(html)
    if not texts:
        # Fall back to the label-anchored pattern.
        for label, val in TAG_RE_ALT.findall(html):
            texts.append(f"{label}: {val}")
    for raw in texts:
        text = htmllib.unescape(raw).strip()
        low = text.lower()
        if low.startswith("guest:"):
            name = text.split(":", 1)[1].strip()
            if name and name not in guests:
                guests.append(name)
        elif low.startswith("show:"):
            if show is None:
                show = text.split(":", 1)[1].strip()
        elif low.startswith("company:"):
            if company is None:
                company = text.split(":", 1)[1].strip()
    return guests, show, company


def extract_title(html: str) -> str:
    m = OG_TITLE_RE.search(html)
    if m:
        return htmllib.unescape(m.group(1)).strip()
    m = TITLE_TAG_RE.search(html)
    if m:
        # Squarespace <title> is often "Post Title — Site"; keep the left part.
        return htmllib.unescape(m.group(1)).split("—")[0].split(" — ")[0].strip()
    return ""


def show_category_url(show: str) -> str:
    """https://futr.tv/thefeed/category/Show%3A+{name}  (colon->%3A, space->+)."""
    return SITE + "/thefeed/category/Show%3A+" + show.replace(" ", "+")


# --------------------------------------------------------------------------- #
# Data IO
# --------------------------------------------------------------------------- #

def load_json_list(path: str) -> list:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        txt = f.read().strip()
    return json.loads(txt) if txt else []


def save_json(path: str, data) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def normalize_row(row: dict) -> dict:
    """Guarantee all seven keys exist (string values)."""
    return {k: (row.get(k) or "") for k in SCHEMA_KEYS}


# --------------------------------------------------------------------------- #
# Core: build new rows for a post
# --------------------------------------------------------------------------- #

def build_rows_for_post(url: str, fallback_show: str | None) -> list[dict]:
    """Fetch one post and return one row per guest (or a single [NEEDS REVIEW])."""
    html = http_get(url)
    guests, show, company = extract_tags(html)
    show = show or fallback_show or ""
    title = extract_title(html)
    date = date_from_permalink(url)
    su = show_category_url(show) if show else ""

    if not guests:
        # No guest tag and no reliable blurb -> flag, never guess.
        guests = [REVIEW]

    rows = []
    for g in guests:
        rows.append(normalize_row({
            "g": g, "c": company or "", "s": show, "t": title,
            "d": date, "u": url, "su": su,
        }))
    return rows


# --------------------------------------------------------------------------- #
# Merge
# --------------------------------------------------------------------------- #

def merge_rows(existing: list[dict], new_rows: list[dict]) -> tuple[list[dict], int]:
    """Surgical merge keyed on (guest, url). Returns (merged, num_appended)."""
    existing = [normalize_row(r) for r in existing]
    by_pair = {(r["g"], r["u"]): r for r in existing}
    urls_with_real_guest = {r["u"] for r in existing if r["g"] and r["g"] != REVIEW}

    appended = 0
    for nr in new_rows:
        key = (nr["g"], nr["u"])
        if key in by_pair:
            # Preserve the existing row; only fill blank fields.
            cur = by_pair[key]
            for k in SCHEMA_KEYS:
                if not cur.get(k) and nr.get(k):
                    cur[k] = nr[k]
            continue
        if nr["g"] == REVIEW and nr["u"] in urls_with_real_guest:
            # Never re-add a review row for a url a human already resolved.
            continue
        existing.append(nr)
        by_pair[key] = nr
        if nr["g"] and nr["g"] != REVIEW:
            urls_with_real_guest.add(nr["u"])
        appended += 1
    return existing, appended


def sort_newest_first(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda r: (r.get("d", ""), r.get("g", "")), reverse=True)


# --------------------------------------------------------------------------- #
# Markdown fallback
# --------------------------------------------------------------------------- #

def render_markdown(rows: list[dict]) -> str:
    pub = [r for r in rows if r["g"] and r["g"] != REVIEW and r["s"] != "No Guest"]
    lines = [
        "# FUTR.tv Guest Directory",
        "",
        "| Guest | Company / Title | Show | Episode | Date |",
        "| --- | --- | --- | --- | --- |",
    ]
    for r in pub:
        guest = f"[{r['g']}]({r['u']})" if r["u"] else r["g"]
        show = f"[{r['s']}]({r['su']})" if r["su"] else r["s"]
        title = (r["t"] or "").replace("|", "\\|")
        lines.append(f"| {guest} | {r['c']} | {show} | {title} | {r['d']} |")
    lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# One-time conversion from the live block HTML (spec section 3)
# --------------------------------------------------------------------------- #

def convert_from_html(path: str) -> list[dict]:
    """Extract the inlined `var DATA=[...]` array from a pasted block HTML file.

    Carries every row VERBATIM (typos and all) — no auto-correction.
    """
    with open(path, encoding="utf-8") as f:
        html = f.read()
    m = re.search(r"var\s+DATA\s*=\s*(\[.*?\])\s*;", html, re.DOTALL)
    if not m:
        raise SystemExit("Could not find `var DATA=[...]` in " + path)
    rows = json.loads(m.group(1))
    return rows


def verify_converted(rows: list[dict]) -> None:
    print(f"  rows parsed: {len(rows)}")
    missing = [i for i, r in enumerate(rows)
               if any(k not in r for k in SCHEMA_KEYS)]
    if missing:
        print(f"  !! rows missing one of the 7 keys: indices {missing[:10]}")
    blank_su = [i for i, r in enumerate(rows) if not r.get("su")]
    if blank_su:
        print(f"  !! rows with blank su: indices {blank_su[:10]}")
    pairs = {}
    for i, r in enumerate(rows):
        pairs.setdefault((r.get("g"), r.get("u")), []).append(i)
    dups = {k: v for k, v in pairs.items() if len(v) > 1}
    if dups:
        print(f"  !! duplicate (guest,url) pairs: {len(dups)} -> {list(dups)[:5]}")
    else:
        print("  no duplicate (guest,url) pairs")
    if rows:
        for label, idx in (("first", 0), ("middle", len(rows) // 2), ("last", -1)):
            r = rows[idx]
            print(f"  spot-check {label}: {r.get('g')!r} | {r.get('s')!r} | {r.get('d')!r}")


# --------------------------------------------------------------------------- #
# Detection driver
# --------------------------------------------------------------------------- #

def detect_new(existing: list[dict], seen: list[str], limit: int) -> list[str]:
    """Return the list of new permalinks (union across the three category pages)."""
    known = {r["u"] for r in existing} | set(seen)
    candidates: list[str] = []
    seen_cand = set()
    for show, cat_url in CATEGORY_PAGES.items():
        try:
            html = http_get(cat_url)
        except RuntimeError as e:
            print(f"  WARN: could not fetch {show} category page: {e}", file=sys.stderr)
            continue
        links = category_permalinks(html)
        # Walk newest-first; stop at the first already-known permalink.
        for url in links:
            if url in known:
                break
            if url not in seen_cand:
                seen_cand.add(url)
                candidates.append((url, show))
        print(f"  {show}: {len(links)} listed, "
              f"{sum(1 for c in candidates if c[1] == show)} new above known")
    if limit:
        candidates = candidates[:limit]
    return candidates


def main() -> int:
    ap = argparse.ArgumentParser(description="Update the FUTR.tv guest directory JSON.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Detect and print changes but write nothing.")
    ap.add_argument("--from-html", metavar="FILE",
                    help="One-time seed: parse `var DATA=[...]` out of a pasted block HTML.")
    ap.add_argument("--data", default=DATA_PATH, help="Path to guests.json.")
    ap.add_argument("--limit", type=int, default=50,
                    help="Max new posts to fetch in one run (safety cap).")
    ap.add_argument("--no-md", action="store_true", help="Do not (re)write guests.md.")
    args = ap.parse_args()

    # ---- One-time conversion mode -----------------------------------------
    if args.from_html:
        print(f"Converting {args.from_html} -> {args.data}")
        rows = convert_from_html(args.from_html)
        verify_converted(rows)
        if args.dry_run:
            print("(dry-run) not writing.")
            return 0
        save_json(args.data, sort_newest_first([normalize_row(r) for r in rows]))
        if not args.no_md:
            with open(MD_PATH, "w", encoding="utf-8") as f:
                f.write(render_markdown([normalize_row(r) for r in rows]))
        print(f"Wrote {args.data}")
        return 0

    # ---- Normal detect + merge mode ---------------------------------------
    existing = load_json_list(args.data)
    seen = load_json_list(SEEN_PATH) if os.path.exists(SEEN_PATH) else []
    print(f"Loaded {len(existing)} existing rows; {len(seen)} seen URLs.")

    candidates = detect_new(existing, seen, args.limit)
    print(f"Found {len(candidates)} new permalink(s).")

    new_rows: list[dict] = []
    for url, show in candidates:
        try:
            rows = build_rows_for_post(url, fallback_show=show)
        except RuntimeError as e:
            print(f"  WARN: could not fetch post {url}: {e}", file=sys.stderr)
            continue
        for r in rows:
            flag = "  [NEEDS REVIEW]" if r["g"] == REVIEW else ""
            print(f"  + {r['d']} | {r['s']:14} | {r['g']}{flag}")
        new_rows.extend(rows)

    merged, appended = merge_rows(existing, new_rows)
    review_rows = [r for r in merged if r["g"] == REVIEW]

    # Sanity check (spec 5.8): only appends happen, so counts must line up.
    expected = len(existing) + appended
    if len(merged) != expected:
        print(f"ABORT: row count sanity failed "
              f"(got {len(merged)}, expected {expected}).", file=sys.stderr)
        return 2

    merged = sort_newest_first(merged)

    print(f"\nSummary: {appended} row(s) appended; "
          f"{len(merged)} total; {len(review_rows)} need review.")

    if args.dry_run:
        print("(dry-run) not writing.")
        return 0

    if appended == 0:
        print("No changes; leaving files untouched.")
        # Still record any newly-seen (No-op) URLs so we don't re-walk them.
    else:
        save_json(args.data, merged)
        if not args.no_md:
            with open(MD_PATH, "w", encoding="utf-8") as f:
                f.write(render_markdown(merged))
        print(f"Wrote {args.data}")

    # Update the seen ledger with every candidate we examined.
    new_seen = sorted(set(seen) | {c[0] for c in candidates})
    save_json(SEEN_PATH, new_seen)

    # Emit review list for the workflow to raise an issue from.
    if review_rows:
        with open(REVIEW_PATH, "w", encoding="utf-8") as f:
            for r in review_rows:
                f.write(f"- {r['d']} — {r['s']} — {r['t']} — {r['u']}\n")
        print(f"Wrote {REVIEW_PATH} ({len(review_rows)} row(s) need a guest name).")
    elif os.path.exists(REVIEW_PATH):
        os.remove(REVIEW_PATH)

    return 0


if __name__ == "__main__":
    sys.exit(main())

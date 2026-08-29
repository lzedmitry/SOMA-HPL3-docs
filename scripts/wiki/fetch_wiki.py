#!/usr/bin/env python3
"""Fetch Frictional Wiki pages for SOMA / shared HPL3 documentation."""

from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://wiki.frictionalgames.com/api.php"
UA = "SOMA-HPL3-Docs-Importer/1.0 (unofficial community docs)"
ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "sources" / "wiki" / "raw"
INDEX_PATH = ROOT / "sources" / "wiki" / "page-index.json"
SKIP_SUBSTRINGS = (
    "Amnesia: Rebirth",
    "Amnesia: The Bunker",
    "HPL3/Community/",
    "Category:",
)


def api(params: dict) -> dict:
    q = urllib.parse.urlencode({**params, "format": "json"})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))


def wanted(title: str) -> bool:
    if any(s in title for s in SKIP_SUBSTRINGS):
        return False
    if title.startswith("HPL3/SOMA"):
        return True
    if title.startswith("HPL3/") and "Amnesia" not in title:
        return True
    return title in {"HPL3"}


def titles_from_index() -> list[dict]:
    data = json.loads(INDEX_PATH.read_text())
    seen: dict[str, dict] = {}
    for p in data.get("soma", []) + data.get("hpl3_all", []):
        t = p["title"]
        if wanted(t):
            seen[t] = p
    # Always include HPL3 root if present
    return sorted(seen.values(), key=lambda x: x["title"])


def fetch_batch(titles: list[str]) -> dict[str, dict]:
    joined = "|".join(titles)
    d = api(
        {
            "action": "query",
            "titles": joined,
            "prop": "revisions|info",
            "rvprop": "content|ids|timestamp|user",
            "rvslots": "main",
            "inprop": "displaytitle",
            "redirects": "1",
        }
    )
    query = d.get("query", {})
    pages = query.get("pages", {})
    normalized = {n["from"]: n["to"] for n in query.get("normalized", [])}
    redirects = {r["from"]: r["to"] for r in query.get("redirects", [])}
    by_title: dict[str, dict] = {}
    for page in pages.values():
        title = page.get("title", "")
        rev = (page.get("revisions") or [None])[0]
        content = ""
        revid = None
        timestamp = None
        user = None
        if rev:
            content = rev.get("slots", {}).get("main", {}).get("*", "") or rev.get("*", "")
            revid = rev.get("revid")
            timestamp = rev.get("timestamp")
            user = rev.get("user")
        rec = {
            "pageid": page.get("pageid"),
            "title": title,
            "missing": "missing" in page,
            "redirect": "redirect" in page,
            "length": page.get("length"),
            "touched": page.get("touched"),
            "revisionId": revid,
            "revisionTimestamp": timestamp,
            "revisionUser": user,
            "wikitext": content,
            "sourceUrl": f"https://wiki.frictionalgames.com/page/{title.replace(' ', '_')}",
        }
        by_title[title] = rec
    # Map requested titles through normalize/redirect
    out: dict[str, dict] = {}
    for t in titles:
        mapped = redirects.get(normalized.get(t, t), normalized.get(t, t))
        rec = by_title.get(mapped) or by_title.get(t)
        if rec:
            rec = dict(rec)
            rec["requestedTitle"] = t
            if mapped != t:
                rec["resolvedTitle"] = mapped
            out[t] = rec
    return out


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    pages = titles_from_index()
    titles = [p["title"] for p in pages]
    print(f"Fetching {len(titles)} pages", flush=True)
    results: dict[str, dict] = {}
    batch_size = 40
    for i in range(0, len(titles), batch_size):
        batch = titles[i : i + batch_size]
        try:
            got = fetch_batch(batch)
        except Exception as e:
            print(f"  batch {i} failed: {e}; retrying", flush=True)
            time.sleep(2)
            got = fetch_batch(batch)
        results.update(got)
        # persist incrementally
        for title, rec in got.items():
            safe = str(rec.get("pageid") or title.replace("/", "__"))
            path = RAW_DIR / f"{safe}.json"
            path.write_text(json.dumps(rec, indent=2, ensure_ascii=False))
        print(f"  {min(i + batch_size, len(titles))}/{len(titles)}", flush=True)
        time.sleep(0.15)

    manifest_path = ROOT / "sources" / "wiki" / "raw-index.json"
    summary = {
        "fetchedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "count": len(results),
        "pages": [
            {
                "title": t,
                "pageid": r.get("pageid"),
                "revisionId": r.get("revisionId"),
                "revisionTimestamp": r.get("revisionTimestamp"),
                "missing": r.get("missing"),
                "wikitextLength": len(r.get("wikitext") or ""),
            }
            for t, r in sorted(results.items())
        ],
    }
    manifest_path.write_text(json.dumps(summary, indent=2))
    print(f"Wrote {len(results)} pages to {RAW_DIR}", flush=True)


if __name__ == "__main__":
    main()

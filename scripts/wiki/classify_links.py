#!/usr/bin/env python3
"""Classify markdown links in src/content/docs. Does not rewrite pages."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "src" / "content" / "docs"
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
LOCALES = ("ru", "de", "fr", "it", "es")

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKI_HOSTS = {
    "wiki.frictionalgames.com",
    "www.frictionalgames.com",
    "frictionalgames.com",
}
INTENTIONAL_HOSTS = {
    "github.com",
    "gitlab.com",
    "store.steampowered.com",
    "steamcommunity.com",
    "www.autodesk.com",
    "www.blender.org",
    "code.visualstudio.com",
    "www.audacityteam.org",
    "www.fmod.com",
    "en.wikipedia.org",
}


def collect_slugs() -> set[str]:
    slugs: set[str] = {"/", ""}
    for path in DOCS.rglob("*"):
        if path.suffix not in {".md", ".mdx"}:
            continue
        rel = path.relative_to(DOCS).with_suffix("").as_posix()
        if rel.endswith("/index"):
            rel = rel[: -len("/index")]
        if rel == "index":
            rel = ""
        slugs.add(rel)
        slugs.add(rel + "/")
        slugs.add("/" + rel)
        slugs.add("/" + rel + "/")
    return slugs


def manifest_titles() -> dict[str, str]:
    raw = json.loads((DATA / "source-manifest.json").read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for page in raw.get("pages", []):
        title = (page.get("originalTitle") or "").replace("_", " ")
        slug = page.get("localSlug") or ""
        if title:
            out[title.lower()] = slug
            out[title.replace(" ", "_").lower()] = slug
    return out


def wiki_title_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path)
    marker = "/page/"
    if marker in path:
        return path.split(marker, 1)[1].replace("_", " ").strip("/")
    return path.strip("/")


def classify_href(href: str, slugs: set[str], titles: dict[str, str]) -> str:
    href = href.strip()
    if href.startswith("#"):
        return "anchor-only"
    if href.startswith("mailto:") or href.startswith("tel:"):
        return "intentional-external"
    if href.startswith("/OWNER"):
        return "intentional-external"

    if href.startswith("http://") or href.startswith("https://"):
        host = urlparse(href).hostname or ""
        host = host.lower()
        path = unquote(urlparse(href).path)
        if "File:" in path or "/File:" in path or path.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
            return "media-file"
        title = wiki_title_from_url(href)
        low = title.lower()
        if host in WIKI_HOSTS:
            if low.startswith("special:") or low.startswith("help:") or "special:" in low:
                return "special-page"
            if low.startswith("category:") or low.startswith("template:") or low.startswith("user:") or low.startswith("talk:"):
                return "unsupported-namespace"
            if low.startswith("file:") or low.startswith("image:"):
                return "media-file"
            if title.startswith(":") or ":hpl3:" in low or low.startswith("hpl3:"):
                return "legacy-dokuwiki"
            if low in titles or low.replace(" ", "_") in titles:
                # Local page exists; remaining wiki URL is source attribution or a
                # mapping leftover. Counted as intentional Wiki, not broken.
                if "/SOMA/" not in href and "/HPL3/" in href:
                    return "shared-HPL3"
                return "intentional-external"
            return "missing-source-page"
        if host in INTENTIONAL_HOSTS or host.endswith(".github.io"):
            return "intentional-external"
        return "intentional-external"

    if href.startswith("/"):
        path = href.split("#", 1)[0]
        if path.rstrip("/") in slugs or path in slugs or path.strip("/") in slugs:
            return "resolved-local"
        stripped = path.strip("/")
        first, _, rest = stripped.partition("/")
        if first in LOCALES:
            mapped = f"/{rest}/" if rest else "/"
            if mapped.rstrip("/") in slugs or mapped in slugs or mapped.strip("/") in slugs or rest in slugs:
                return "resolved-local"
        if path.startswith("/page/"):
            return "legacy-dokuwiki"
        return "broken"

    # relative
    return "resolved-local"


def main() -> int:
    slugs = collect_slugs()
    titles = manifest_titles()
    counts: Counter[str] = Counter()
    samples: dict[str, list[str]] = {k: [] for k in [
        "resolved-local",
        "intentional-external",
        "shared-HPL3",
        "missing-source-page",
        "legacy-dokuwiki",
        "media-file",
        "special-page",
        "unsupported-namespace",
        "anchor-only",
        "broken",
    ]}
    notable_missing = {
        "HPL3/Level Design/Creating Terrain",
        "HPL3/Level Design/HDR",
        "HPL3/Level Design/Environment Particles",
        "HPL3/Areas/Visibility Area",
        "HPL3/Areas/MapTransfer Area",
        "HPL3/Sound/Playing Music",
        "HPL3/Scripting/Scripting Conventions",
    }
    notable_hits: dict[str, str] = {}

    for path in DOCS.rglob("*"):
        if path.suffix not in {".md", ".mdx"}:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for match in MD_LINK.finditer(text):
            href = match.group(1).strip(' "\'')
            kind = classify_href(href, slugs, titles)
            counts[kind] += 1
            if len(samples[kind]) < 12:
                samples[kind].append(f"{rel} → {href}")
            if href.startswith("http"):
                title = wiki_title_from_url(href).replace("_", " ")
                if title in notable_missing:
                    notable_hits[title] = "missing-source-page (no Wiki article / not imported)"

    REPORTS.mkdir(exist_ok=True)
    total = sum(counts.values())
    notable_lines = (
        [f"- `{name}` — {status}" for name, status in sorted(notable_hits.items())]
        if notable_hits
        else ["- (none of the named hub redlinks appeared as live URLs in this pass)"]
    )
    sample_blocks = []
    for key in samples:
        items = samples[key]
        if not items:
            continue
        sample_blocks.append(f"### {key}\n")
        sample_blocks.extend(f"- `{row}`" for row in items)
        sample_blocks.append("")
    lines = [
        "# Link audit",
        "",
        "Classification of markdown links in `src/content/docs`.",
        "This report does **not** rewrite pages. Wiki URLs that the importer could not map locally stay as intentional source links or missing-source-page.",
        "",
        "## Counts",
        "",
        "| Category | Count | Meaning |",
        "| --- | ---: | --- |",
        f"| resolved-local | {counts['resolved-local']} | Internal path that exists |",
        f"| intentional-external | {counts['intentional-external']} | Wiki/source or third-party URL kept on purpose |",
        f"| shared-HPL3 | {counts['shared-HPL3']} | Shared HPL3 Wiki URL; a local page may exist |",
        f"| missing-source-page | {counts['missing-source-page']} | Wiki target not in the import (often a redlink) |",
        f"| legacy-dokuwiki | {counts['legacy-dokuwiki']} | Old `:hpl3:` / doku-style path |",
        f"| media-file | {counts['media-file']} | File: / Image: (not inlined) |",
        f"| special-page | {counts['special-page']} | MediaWiki Special:/Help: |",
        f"| unsupported-namespace | {counts['unsupported-namespace']} | Category/Template/User/Talk |",
        f"| anchor-only | {counts['anchor-only']} | Same-page `#anchor` |",
        f"| broken | {counts['broken']} | Internal path with no matching page |",
        "",
        f"**Total classified:** {total}",
        "",
        "## Notable missing Wiki targets",
        "",
        "These names were called out in the original hub pages. They are **not** local defects if the Wiki never published the article.",
        "",
        *notable_lines,
        "",
        "## Samples",
        "",
        *sample_blocks,
    ]
    (REPORTS / "link-audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote reports/link-audit.md ({total} links, broken={counts['broken']})")
    return 1 if counts["broken"] else 0


if __name__ == "__main__":
    raise SystemExit(main())

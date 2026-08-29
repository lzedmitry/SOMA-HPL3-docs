#!/usr/bin/env python3
"""Check internal markdown links against files that exist in src/content/docs."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "src" / "content" / "docs"
LOCALES = ("ru", "de", "fr", "it", "es")

# Explicit allowlist for known-missing Wiki redlinks referenced as plain text, not links.
ALLOW = {
    "/api/categories/entity/",  # exists
}


def collect_slugs() -> set[str]:
    slugs = {"/", ""}
    for p in DOCS.rglob("*"):
        if p.suffix not in {".md", ".mdx"}:
            continue
        rel = p.relative_to(DOCS).with_suffix("").as_posix()
        if rel.endswith("/index"):
            rel = rel[: -len("/index")]
        if rel == "index":
            rel = ""
        slugs.add(rel)
        slugs.add(rel + "/")
        slugs.add("/" + rel)
        slugs.add("/" + rel + "/")
    return slugs


def english_href(href: str) -> str:
    """Map /ru/foo/ to /foo/ so locale-prefixed fallback links resolve."""
    stripped = href.strip("/")
    if not stripped:
        return "/"
    first, _, rest = stripped.partition("/")
    if first in LOCALES:
        return f"/{rest}/" if rest else "/"
    return href


LINK = re.compile(r"\[[^\]]+\]\((/[^)#\s]+)(?:#[^)]*)?\)")


def main() -> int:
    slugs = collect_slugs()
    fatal = []
    for p in DOCS.rglob("*"):
        if p.suffix not in {".md", ".mdx"}:
            continue
        text = p.read_text(encoding="utf-8")
        for m in LINK.finditer(text):
            href = m.group(1)
            if href.startswith("//") or href.startswith("/http"):
                continue
            if href.startswith("/page/"):
                continue
            # skip GitHub / external-looking
            if href.startswith("/OWNER"):
                continue
            candidates = {href, href.rstrip("/"), href.strip("/"), f"/{href.strip('/')}/"}
            mapped = english_href(href)
            candidates.update({mapped, mapped.rstrip("/"), mapped.strip("/"), f"/{mapped.strip('/')}/"})
            if any(c in slugs for c in candidates):
                continue
            fatal.append(f"{p.relative_to(ROOT)} -> {href}")
    if fatal:
        print(f"Broken internal links: {len(fatal)}")
        for line in fatal[:80]:
            print(" ", line)
        if len(fatal) > 80:
            print(f"  … {len(fatal) - 80} more")
        return 1
    print("Internal links OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

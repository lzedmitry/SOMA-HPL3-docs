#!/usr/bin/env python3
"""QA for translated hubs: identifiers, fences, and basic structure."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "src" / "content" / "docs"
TERMS = json.loads((ROOT / "data" / "i18n" / "terminology.json").read_text(encoding="utf-8"))
LOCALES = ("ru", "de", "fr", "it", "es")

IDENTIFIERS = [t["term"] for t in TERMS.get("terms", []) if t.get("identifier")]
# Also always-check engine tokens that must not be rewritten.
EXTRA = [
    "cScript_GetGlobalArgBool",
    "cLux_AddDebugMessage",
    "OnStart",
    "entry.hpc",
    "resources.cfg",
    "MinimalCustomMapMod",
    "PlayerStart",
    "helper_area.hps",
]


def locale_files(locale: str) -> list[Path]:
    folder = DOCS / locale
    if not folder.exists():
        return []
    return [p for p in folder.rglob("*") if p.suffix in {".md", ".mdx"}]


def fence_count(text: str) -> int:
    return text.count("```")


def heading_count(text: str) -> int:
    return len(re.findall(r"(?m)^#{2,3} ", text))


def body_only(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def main() -> int:
    warnings: list[str] = []
    for locale in LOCALES:
        files = locale_files(locale)
        if not files:
            warnings.append(f"{locale}: no translated files")
            continue
        for path in files:
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(DOCS)
            en_rel = Path(*rel.parts[1:])
            en_path = DOCS / en_rel
            if not en_path.exists() and en_rel.as_posix().endswith("/index.mdx"):
                # hubs sometimes map to index.mdx while English uses the same
                pass
            if en_path.exists():
                en = en_path.read_text(encoding="utf-8")
                if fence_count(text) != fence_count(en) and "```" in en:
                    warnings.append(f"{rel}: code fence count {fence_count(text)} != English {fence_count(en)}")
                en_body = body_only(en)
                loc_body = body_only(text)
                for ident in IDENTIFIERS + EXTRA:
                    if ident in en_body and ident not in loc_body:
                        warnings.append(f"{rel}: missing identifier {ident}")
    if warnings:
        print(f"Translation QA warnings: {len(warnings)}")
        for line in warnings[:80]:
            print(" ", line)
        if len(warnings) > 80:
            print(f"  … {len(warnings) - 80} more")
        return 0  # warnings, not fatal — generator reports remaining work
    print("Translation QA: no identifier/fence warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

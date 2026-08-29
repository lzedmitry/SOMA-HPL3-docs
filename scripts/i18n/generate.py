#!/usr/bin/env python3
"""Generate TIER 1+2 translated hubs and the translation manifest."""

from __future__ import annotations

import importlib.util
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "src" / "content" / "docs"
LOCALES = ("ru", "de", "fr", "it", "es")
REV = 1

TRANSLATED = {
    "index",
    "start",
    "start/create-and-launch-your-mod",
    "start/terminology",
    "recipes/first-mod",
    "modding",
    "level-editor",
    "level-building",
    "areas",
    "scripting",
    "debugging",
    "assets",
    "glossary",
    "recipes",
    "scripting/helpers",
    "entities",
    "materials",
    "particles",
    "audio",
    "dialogue",
    "api",
    "videos",
    "about",
    "about/translations",
}

EN_PATH = {
    "index": "index.mdx",
    "start": "start/index.mdx",
    "start/create-and-launch-your-mod": "start/create-and-launch-your-mod.md",
    "start/terminology": "start/terminology.mdx",
    "recipes/first-mod": "recipes/first-mod.mdx",
    "modding": "modding/index.mdx",
    "level-editor": "level-editor/index.mdx",
    "level-building": "level-building/index.mdx",
    "areas": "areas/index.mdx",
    "scripting": "scripting/index.mdx",
    "debugging": "debugging/index.mdx",
    "assets": "assets/index.mdx",
    "glossary": "glossary/index.mdx",
    "recipes": "recipes/index.mdx",
    "scripting/helpers": "scripting/helpers/index.mdx",
    "entities": "entities/index.mdx",
    "materials": "materials/index.mdx",
    "particles": "particles/index.mdx",
    "audio": "audio/index.mdx",
    "dialogue": "dialogue/index.mdx",
    "api": "api/index.mdx",
    "videos": "videos/index.mdx",
    "about": "about/index.mdx",
    "about/translations": "about/translations.mdx",
}

COMPONENTS = {
    "index": "HomeDashboard",
    "assets": "Pipeline",
    "about": "DocStats",
    "api": "ApiBrowser",
    "videos": "VideoLibrary",
    "about/translations": "TranslationsCoverage",
}

# Loaded in main() via importlib from titles.py (same directory).
TITLES: dict = {}


def _yaml_str(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _front(locale: str, slug: str, extra: str = "") -> str:
    title, desc = TITLES[slug][locale]
    extra_yaml = extra.rstrip() + "\n" if extra.strip() else ""
    return (
        f"---\n"
        f"title: {_yaml_str(title)}\n"
        f"description: {_yaml_str(desc)}\n"
        f"{extra_yaml}"
        f"translation:\n"
        f"  locale: {locale}\n"
        f"  sourceLocale: en\n"
        f"  sourceRevision: {REV}\n"
        f"  translationRevision: {REV}\n"
        f"  status: current\n"
        f"---\n\n"
    )


def _imp(locale: str, slug: str, name: str) -> str:
    rel = EN_PATH[slug]
    dirs = Path(locale, rel).parent.parts
    up = "../" * (len(dirs) + 2)
    return f'import {name} from "{up}components/{name}.astro";\n\n'


MD_LINK = re.compile(r"\]\((/[^)#\s]+)(#[^)]*)?\)")
HREF = re.compile(r'href="(/[^"]+)"')


def localize_links(body: str, locale: str) -> str:
    """Prefix every internal docs path with the locale.

    Untranslated children then hit Starlight fallback (English body + banner)
    instead of dropping the reader onto an English URL / losing UI locale.
    """

    def swap(path: str) -> str:
        raw = path
        if path.startswith("//") or path.startswith("/http"):
            return raw
        if path.startswith("/ru/") or path.startswith("/de/") or path.startswith("/fr/") or path.startswith("/it/") or path.startswith("/es/"):
            return raw
        stripped = path.split("#")[0].strip("/")
        key = stripped or "index"
        if key == "index":
            return f"/{locale}/"
        return f"/{locale}/{stripped}/"

    def md(m: re.Match[str]) -> str:
        path, frag = m.group(1), m.group(2) or ""
        new = swap(path)
        return f"]({new}{frag})"

    def hr(m: re.Match[str]) -> str:
        return f'href="{swap(m.group(1))}"'

    return HREF.sub(hr, MD_LINK.sub(md, body))


def extra_fm(slug: str) -> str:
    mapping = {
        "index": "tableOfContents: false\neditUrl: false",
        "start": "difficulty: beginner\ncategory: start",
        "start/create-and-launch-your-mod": "category: start\nsourceStatus: verified",
        "start/terminology": "difficulty: beginner\ncategory: start",
        "recipes/first-mod": "category: recipes\ndifficulty: beginner",
        "modding": "category: modding",
        "level-editor": "category: level-editor",
        "level-building": "category: level-building",
        "areas": "category: areas",
        "scripting": "category: scripting",
        "debugging": "category: debugging",
        "assets": "category: assets",
        "glossary": "category: glossary",
        "recipes": "category: recipes",
        "scripting/helpers": "category: scripting\nsourceStatus: undocumented",
        "entities": "category: entities",
        "materials": "category: materials\nsourceStatus: wip",
        "particles": "category: particles\nsourceStatus: wip",
        "audio": "category: audio\nsourceStatus: wip",
        "dialogue": "category: dialogue",
        "api": "category: api",
        "videos": "category: videos\ntableOfContents: false",
        "about": "category: about",
        "about/translations": "category: about\ntableOfContents: false",
    }
    return mapping.get(slug, "")


def english_slugs() -> list[str]:
    slugs = []
    skip_top = set(LOCALES)
    for p in DOCS.rglob("*"):
        if p.suffix not in {".md", ".mdx"}:
            continue
        rel = p.relative_to(DOCS).as_posix()
        if rel.split("/")[0] in skip_top:
            continue
        key = rel.rsplit(".", 1)[0]
        if key.endswith("/index"):
            key = key[: -len("/index")]
        slugs.append(key)
    return sorted(set(slugs))


def write_manifest(slugs: list[str]) -> None:
    pages = {}
    for slug in slugs:
        row: dict = {"en": {"revision": REV}}
        for loc in LOCALES:
            if slug in TRANSLATED:
                row[loc] = {"revision": REV, "status": "current"}
            else:
                row[loc] = None
        pages[slug] = row
    data = {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "englishPageCount": len(slugs),
        "translatedSlugs": sorted(TRANSLATED),
        "pages": pages,
    }
    dest = ROOT / "data" / "translation-manifest.json"
    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {dest} ({len(slugs)} English slugs, {len(TRANSLATED)} translated hubs)")


def write_locale_reports(slugs: list[str]) -> None:
    out = ROOT / "reports" / "translations"
    out.mkdir(parents=True, exist_ok=True)
    total = len(slugs)
    n = len(TRANSLATED)
    pct = round(n / total * 1000) / 10 if total else 0
    names = {"ru": "Russian", "de": "German", "fr": "French", "it": "Italian", "es": "Spanish"}
    for loc in LOCALES:
        missing = [s for s in slugs if s not in TRANSLATED]
        text = f"""# Translation report — {names[loc]} (`{loc}`)

- English pages: {total}
- Translated (current): {n}
- Outdated: 0
- Missing: {total - n}
- Coverage: {pct}%

## Translated hubs (TIER 1–2)

{chr(10).join(f"- `{s}`" for s in sorted(TRANSLATED))}

## Missing (TIER 3 / remaining English)

{len(missing)} pages stay on English via Starlight fallback. Language switcher does not 404.

First missing examples:

{chr(10).join(f"- `{s}`" for s in missing[:40])}

## Terminology

Technical identifiers (`Area`, `Entity`, `OnStart`, `.hps`, `cScript_GetGlobalArgBool`, editor names) stay English. See `data/i18n/terminology.json`.

## QA warnings

Run `pnpm i18n:qa` after generation.
"""
        (out / f"{loc}.md").write_text(text, encoding="utf-8")
    print("Wrote reports/translations/{ru,de,fr,it,es}.md")


def load_hubs() -> dict:
    merged: dict = {}
    for name in ("hub_bodies", "hubs_rest", "hubs_more", "hubs_catalog", "hubs_last"):
        path = Path(__file__).with_name(f"{name}.py")
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise SystemExit(f"{name}.py missing")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        merged.update(getattr(mod, "HUBS", {}))
    return merged


def extra_bodies(locale: str) -> dict[str, str]:
    """Homepage, videos, translations page, quickstart."""
    spec = importlib.util.spec_from_file_location("inline_bodies", Path(__file__).with_name("inline_bodies.py"))
    if spec is None or spec.loader is None:
        raise SystemExit("inline_bodies.py missing")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.for_locale(locale)


def main() -> None:
    global TITLES
    titles_path = Path(__file__).with_name("titles.py")
    spec = importlib.util.spec_from_file_location("titles", titles_path)
    if spec is None or spec.loader is None:
        raise SystemExit("titles.py missing")
    tmod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tmod)
    TITLES = tmod.TITLES

    hub_bodies = load_hubs()
    slugs = english_slugs()
    write_manifest(slugs)

    missing = []
    for locale in LOCALES:
        inline = extra_bodies(locale)
        for slug in sorted(TRANSLATED):
            body = inline.get(slug) or hub_bodies.get(slug, {}).get(locale)
            if not body:
                missing.append(f"{locale}:{slug}")
                continue
            title_block = _front(locale, slug, extra_fm(slug))
            comp = COMPONENTS.get(slug)
            head = _imp(locale, slug, comp) if comp else ""
            text = title_block + head + localize_links(body, locale)
            dest = DOCS / locale / EN_PATH[slug]
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
        print(f"Wrote pages for {locale}")
    if missing:
        print("MISSING BODIES:")
        for m in missing:
            print(" ", m)
        raise SystemExit(1)
    write_locale_reports(slugs)


if __name__ == "__main__":
    main()

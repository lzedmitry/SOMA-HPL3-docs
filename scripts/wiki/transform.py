#!/usr/bin/env python3
"""Transform fetched Frictional Wiki pages into Starlight Markdown."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wikitext import (  # noqa: E402
    detect_status,
    wikitext_to_markdown,
    convert_wikilinks,
    convert_inline_markup,
    convert_headings,
    convert_lists,
    convert_tables,
    convert_templates,
    strip_chrome,
    _split_top_level_pipes,
)

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "sources" / "wiki" / "raw"
NORM_DIR = ROOT / "sources" / "wiki" / "normalized"
DOCS = ROOT / "src" / "content" / "docs"
DATA = ROOT / "data"
REPORTS = ROOT / "reports"

SYNC_STAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

EDITOR_PAGES = {
    # Editorial files that must not be overwritten by wiki sync
    "index.mdx",
    "start/index.mdx",
    "start/terminology.mdx",
    "start/what-is-hpl3.mdx",
    "start/what-can-be-modified.mdx",
    "start/where-next.mdx",
    "modding/index.mdx",
    "level-editor/index.mdx",
    "level-building/index.mdx",
    "areas/index.mdx",
    "scripting/index.mdx",
    "scripting/helpers/index.mdx",
    "api/index.mdx",
    "assets/index.mdx",
    "entities/index.mdx",
    "materials/index.mdx",
    "particles/index.mdx",
    "audio/index.mdx",
    "dialogue/index.mdx",
    "debugging/index.mdx",
    "recipes/index.mdx",
    "tools/index.mdx",
    "glossary/index.mdx",
    "about/index.mdx",
    "about/licensing.mdx",
    "about/contributing.mdx",
    "editors/index.mdx",
    "scripting/common-patterns.mdx",
    "wiki-index/index.mdx",
}


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = s.replace("&", " and ")
    s = s.replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s or "page"


def display_title(title: str) -> str:
    leaf = title.split("/")[-1]
    leaf = re.sub(r"\s+Area$", "", leaf)
    return leaf


def classify(title: str) -> str:
    t = title
    if "/Scripting/Scripting Api/" in t or re.search(r"/Scripting/[ceit][A-Z]", t):
        return "api"
    if "/Scripting/" in t and re.match(r".*/(c|e|i|t)[A-Za-z0-9].*$", t):
        last = t.split("/")[-1]
        if last[0] in "ceit" and last[1:2].isupper() or last.startswith(("c", "e", "i", "t")) and len(last) > 2:
            if last not in {"array"} and not last.startswith(("Scripting", "Input", "Terminal", "hps")):
                if re.match(r"^[ceit][A-Z]", last) or re.match(r"^[ceit][A-Za-z].*(Iterator|Interface|Data|Type|Flag)", last):
                    return "api"
                if re.match(r"^[cei][A-Z]", last) or last.startswith(("cLux", "cPost", "cImGui", "cWidget", "cVector", "cColor", "cScript")):
                    return "api"
                if last[0] in "ei" and last[1:2].isupper():
                    return "api"
    if t.startswith("HPL3/SOMA/Scripting/") or t.startswith("HPL3/Scripting/"):
        last = t.split("/")[-1]
        if re.match(r"^[ceit][A-Za-z]", last) and last not in {
            "array",
        }:
            if last[0] in "ceit" and (len(last) > 1 and (last[1].isupper() or last.startswith(("Lux", "Post", "ImGui", "Widget")))):
                return "api"
            if last.startswith(("c", "e", "i")) and " " not in last[:2]:
                # cScript, eKey, iGpuProgram, tString
                if re.match(r"^[ceit][A-Z]", last) or re.match(r"^i[A-Z]", last) or last in {"array", "tString", "tID"}:
                    return "api"
                if re.match(r"^[ceit][A-Za-z0-9_ ]+$", last) and last[0] in "ceit" and last not in {
                    "Input Types",
                    "Terminals Overview",
                    "hps api",
                }:
                    if last[1:2].isupper() or last.startswith(("c", "e", "i")) and last[1:2].isupper():
                        return "api"
                    if re.match(r"^[cei][A-Z]", last) or last.startswith("tString") or last == "array":
                        return "api"
    if "/Areas" in t:
        return "areas"
    if "/Getting Started" in t:
        return "start"
    if "/Level Design" in t:
        editor_keys = (
            "View",
            "Toolbar",
            "Preferences",
            "Settings",
            "Information",
            "Pose",
            "Finding",
            "Compounds",
            "Color Dialog",
            "Controls",
            "Import",
        )
        if any(k in t for k in editor_keys):
            return "level-editor"
        return "level-building"
    if "/Modding" in t or t.endswith("Developer Commands"):
        return "modding"
    if "/Entities" in t:
        return "entities"
    if "/Materials" in t:
        return "materials"
    if "/Particles" in t:
        return "particles"
    if "/Sound" in t or t.endswith("/Sound"):
        return "audio"
    if "/Audition" in t:
        return "dialogue"
    if "/Modeling" in t or "/Animation" in t or "Blender" in t:
        return "assets"
    if "/Third Party" in t or t.endswith("Tools"):
        return "tools"
    if "Glossary" in t:
        return "glossary"
    if "Troubleshoot" in t:
        return "debugging"
    if "/Scripting" in t:
        return "scripting"
    if "/Tutorials" in t:
        return "scripting"
    return "generated"


def is_api_class(title: str) -> bool:
    last = title.split("/")[-1]
    if title.endswith("/array") or last == "array":
        return True
    if last in {"tString", "tID", "tid", "tstring"}:
        return True
    if "Scripting Api/" in title and not title.endswith("Scripting Api"):
        # category helper pages like Billboard, Body — treat as api category
        if re.match(r"^[A-Z]", last):
            return False
        return True
    if "/Scripting/" in title:
        if re.match(r"^[cei][A-Z]", last) or re.match(r"^e[A-Z]", last):
            return True
        if last.startswith(("cLux", "cPost", "cImGui", "cWidget", "cVector", "cColor", "cScript", "cGui")):
            return True
        if last.startswith("i") and "Interface" in last:
            return True
        if re.match(r"^i[A-Z]", last):
            return True
        if last.startswith("t") and last[1:2].isupper():
            return True
        # "cPostEffect FXAA"
        if re.match(r"^c[A-Z]", last):
            return True
        if re.match(r"^e[A-Z]", last):
            return True
    return False


def local_path(title: str) -> str:
    last = title.split("/")[-1]
    sl = slugify(last)

    if title in {"HPL3/SOMA", "HPL3"}:
        return "generated/wiki-home.md"
    if title == "HPL3/SOMA/Getting Started":
        return "start/overview.md"
    if title.startswith("HPL3/SOMA/Getting Started/"):
        return f"start/{sl}.md"
    if title == "HPL3/SOMA/Glossary":
        return "generated/glossary-source.md"
    if title == "HPL3/Troubleshooting":
        return "debugging/faq.md"
    if title.endswith("Developer Commands") or title.endswith("/Developer Commands"):
        return "modding/developer-commands.md"

    if is_api_class(title):
        return f"api/classes/{sl}.md"
    if "/Scripting/Scripting Api/" in title:
        return f"api/categories/{sl}.md"
    if title.endswith("/Scripting Api") or title.endswith("/hps api"):
        return "api/wiki-index.md"

    if "/Areas/" in title or title.endswith("/Areas"):
        if title.endswith("/Areas"):
            return "generated/areas-hub.md"
        return f"areas/{sl}.md"

    if "/Level Design/" in title:
        cat = classify(title)
        return f"{cat}/{sl}.md"
    if title.endswith("/Level Design"):
        return "generated/level-design-hub.md"

    if "/Modding/" in title:
        return f"modding/{sl}.md"
    if title.endswith("/Modding"):
        return "generated/modding-hub.md"

    if "/Entities/" in title:
        return f"entities/{sl}.md"
    if title.endswith("/Entities"):
        return "generated/entities-hub.md"

    if "/Materials/" in title or title.endswith("/Materials"):
        if title.endswith("/Materials"):
            return "generated/materials-hub.md"
        return f"materials/{sl}.md"

    if "/Particles/" in title or title.endswith("/Particles"):
        if title.endswith("/Particles"):
            return "generated/particles-hub.md"
        return f"particles/{sl}.md"

    if "/Sound" in title:
        return f"audio/{sl}.md"

    if "/Audition" in title:
        if title.endswith("/Audition"):
            return "generated/dialogue-hub.md"
        return f"dialogue/{sl}.md"

    if "/Modeling" in title or "/Animation" in title or "Blender" in title:
        if title.endswith("/Modeling") or title.endswith("/Animation"):
            return f"assets/{sl}.md"
        return f"assets/{sl}.md"

    if "/Third Party" in title:
        return f"tools/{sl}.md"

    if "/AngelScript Fundamentals" in title:
        return f"scripting/angelscript/{sl}.md"
    if "/Scripting Guide/" in title or "/Scripting/" in title:
        if title.endswith("/Scripting"):
            return "generated/scripting-hub.md"
        return f"scripting/{sl}.md"

    if "/Tutorials" in title:
        return f"scripting/{sl}.md"

    if title.startswith("Frictional Wiki:"):
        return f"about/{sl}.md"

    return f"generated/{sl}.md"


def yaml_escape(s: str) -> str:
    s = (s or "").replace("\n", " ").strip()
    if not s:
        return '""'
    if re.search(r'[:#{}[\],&*?|!<>=%@`]', s) or s[0] in "-'\"{}[]":
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
    return s


def first_paragraph(md: str) -> str:
    lines = []
    for line in md.splitlines():
        s = line.strip()
        if not s:
            if lines:
                break
            continue
        if s.startswith(("#", ">", "{", "|", "-", "*", ":", "<", "`")):
            if lines:
                break
            continue
        lines.append(s)
        if len(" ".join(lines)) > 180:
            break
    text = " ".join(lines)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]+", "", text)
    return text[:220].strip()


def convert_codedoc(wikitext: str) -> str:
    """Turn CodeDoc templates into markdown API reference."""
    text = wikitext

    # Summary table
    def summary_block(m: re.Match) -> str:
        inner = m.group(1)
        rows = []
        for item in re.finditer(r"\{\{CodeDocSummaryItem\|(.*?)\}\}", inner, re.DOTALL):
            parts = _split_top_level_pipes(item.group(1))
            # after name stripped already in group
            ret = parts[0].strip() if parts else ""
            sig = parts[1].strip() if len(parts) > 1 else ""
            desc = parts[2].strip() if len(parts) > 2 else ""
            # extract function name from [[#x|x]](params) or plain
            name_m = re.search(r"\[\[#([^\]|]+)\|([^\]]+)\]\]", sig)
            if name_m:
                name = name_m.group(2)
                params = sig.split("]]", 1)[-1]
            else:
                name = re.sub(r"\[\[|\]\]", "", sig)
                params = ""
            ret_clean = re.sub(r"\[\[/?\.?\./[^\|\]]+\|([^\]]+)\]\]", r"\1", ret)
            ret_clean = re.sub(r"\[\[([^\|\]]+)\|([^\]]+)\]\]", r"\2", ret_clean)
            ret_clean = re.sub(r"\[\[([^\]]+)\]\]", r"\1", ret_clean)
            rows.append((ret_clean, name, params, desc))
        if not rows:
            return ""
        lines = ["| Return | Function | Description |", "| --- | --- | --- |"]
        for ret, name, params, desc in rows:
            fn = f"[`{name}`](#{slugify(name)}){params}"
            d = desc if desc else "*Undocumented in the original Wiki.*"
            lines.append(f"| `{ret}` | {fn} | {d} |")
        return "\n" + "\n".join(lines) + "\n"

    text = re.sub(
        r"\{\{CodeDocSummaryTop\}\}(.*?)\{\{CodeDocSummaryBottom\}\}",
        summary_block,
        text,
        flags=re.DOTALL,
    )

    # Detail blocks
    detail_re = re.compile(
        r"\{\{CodeDocDetailTop\|([^}]*)\}\}\s*"
        r"(?:<syntaxhighlight[^>]*>(.*?)</syntaxhighlight>)?\s*"
        r"\{\{CodeDocDetailBody\|([^}]*)\}\}\s*"
        r"(?:\{\{CodeDocDetailParamStart\}\}\s*)?"
        r"((?:\{\{CodeDocDetailParam\|[^}]*\}\}\s*)*)"
        r"(?:\{\{CodeDocDetailReturn\|([^}]*)\}\})?\s*"
        r"\{\{CodeDocDetailBottom\}\}",
        re.DOTALL | re.I,
    )

    def detail_repl(m: re.Match) -> str:
        name = m.group(1).strip()
        sig = (m.group(2) or "").strip()
        body = (m.group(3) or "").strip()
        params_raw = m.group(4) or ""
        ret_raw = m.group(5) or ""
        params = []
        for p in re.finditer(r"\{\{CodeDocDetailParam\|([^}]*)\}\}", params_raw):
            parts = _split_top_level_pipes(p.group(1))
            pname = parts[0].strip() if parts else ""
            ptype = parts[1].strip() if len(parts) > 1 else ""
            pdesc = parts[2].strip() if len(parts) > 2 else ""
            params.append((pname, ptype, pdesc))
        ret_parts = _split_top_level_pipes(ret_raw) if ret_raw else []
        rtype = ret_parts[0].strip() if ret_parts else ""
        rdesc = ret_parts[1].strip() if len(ret_parts) > 1 else ""

        out = [f"### `{name}`", ""]
        if sig:
            out.append("```cpp")
            out.append(sig)
            out.append("```")
            out.append("")
        if body:
            out.append(body)
            out.append("")
        else:
            out.append(
                ":::note[Documentation status]\nUndocumented in the original Frictional Wiki. Signature preserved from the generated API dump.\n:::"
            )
            out.append("")
        if params:
            out.append("| Name | Type | Description |")
            out.append("| --- | --- | --- |")
            for pname, ptype, pdesc in params:
                out.append(
                    f"| `{pname}` | `{ptype}` | {pdesc or '—'} |"
                )
            out.append("")
        if rtype:
            extra = f" — {rdesc}" if rdesc else ""
            out.append(f"**Returns:** `{rtype}`{extra}")
            out.append("")
        return "\n".join(out)

    text = detail_re.sub(detail_repl, text)
    text = re.sub(r"\{\{ScriptingStub\}\}", "", text)
    text = re.sub(r"\{\{HPL3SOMAScriptingCategories\}\}", "", text)
    text = re.sub(r"\{\{ReferencesSection\}\}", "", text)
    text = re.sub(r"\{\{SeeMore\|[^}]*\}\}", "", text)
    text = re.sub(r"\{\{BackToTop\}\}", "", text)
    return text


def extract_functions(wikitext: str, class_name: str, href_base: str) -> list[dict]:
    items = []
    for m in re.finditer(
        r"\{\{CodeDocDetailTop\|([^}]*)\}\}\s*(?:<syntaxhighlight[^>]*>(.*?)</syntaxhighlight>)?",
        wikitext,
        re.DOTALL | re.I,
    ):
        name = m.group(1).strip()
        sig = (m.group(2) or "").strip()
        ret = ""
        params = ""
        if sig:
            sm = re.match(r"^(\S+)\s+\S+\((.*)\)$", sig.replace("\n", " ").strip())
            if sm:
                ret = sm.group(1)
                params = sm.group(2)
        documented = False
        # body after this top
        items.append(
            {
                "name": name,
                "class": class_name,
                "returnType": ret,
                "params": params,
                "signature": sig or name,
                "href": f"{href_base}#{slugify(name)}",
                "documented": documented,
            }
        )
    return items


def load_raw() -> list[dict]:
    pages = []
    seen_ids = set()
    for f in sorted(RAW_DIR.glob("*.json")):
        d = json.loads(f.read_text())
        pid = d.get("pageid")
        if pid in seen_ids:
            continue
        seen_ids.add(pid)
        if d.get("missing"):
            continue
        pages.append(d)
    return pages


def resolve_transclusions(pages: list[dict]) -> None:
    by_title = {p["title"]: p for p in pages}
    # also index requestedTitle
    for p in pages:
        if p.get("requestedTitle"):
            by_title.setdefault(p["requestedTitle"], p)
    for p in pages:
        wt = p.get("wikitext") or ""
        m = re.match(r"^\s*\{\{:([^}]+)\}\}\s*$", wt)
        if m:
            src = m.group(1).strip().replace("_", " ")
            if src in by_title and by_title[src] is not p:
                p["wikitext"] = by_title[src].get("wikitext") or wt
                p["transcludedFrom"] = src


def build_link_map(pages: list[dict]) -> dict[str, str]:
    m: dict[str, str] = {}
    for p in pages:
        title = p["title"]
        path = local_path(title)
        href = "/" + path.replace(".md", "/").replace(".mdx", "/")
        m[title] = href
        m[title.replace(" ", "_")] = href
        m[title.replace("_", " ")] = href
        if p.get("requestedTitle"):
            rt = p["requestedTitle"]
            m[rt] = href
            m[rt.replace(" ", "_")] = href
            m[rt.replace("_", " ")] = href
        if title.startswith("HPL3/SOMA/"):
            rest = title[len("HPL3/SOMA/") :]
            m["HPL3/" + rest] = href
            m["HPL3/" + rest.replace(" ", "_")] = href
        if title.startswith("HPL3/") and not title.startswith("HPL3/SOMA/"):
            rest = title[len("HPL3/") :]
            m["HPL3/SOMA/" + rest] = href
            m["HPL3/SOMA/" + rest.replace(" ", "_")] = href
        # common aliases
        last = title.split("/")[-1]
        # don't alias short last names globally
    return m


def frontmatter(p: dict, path: str, md: str, statuses: list[str]) -> str:
    title = display_title(p["title"])
    if path.startswith("api/classes/"):
        title = p["title"].split("/")[-1]
    desc = first_paragraph(md) or f"Reference for {title} from the Frictional Wiki."
    status = "verified"
    if "wip" in statuses:
        status = "wip"
    elif "outdated" in statuses:
        status = "outdated"
    elif "undocumented" in statuses:
        status = "undocumented"
    elif "incomplete" in statuses:
        status = "incomplete"
    elif "legacy" in statuses:
        status = "legacy"
    elif len((p.get("wikitext") or "")) < 80:
        status = "incomplete"
    cat = classify(p["title"])
    tags = [cat]
    if is_api_class(p["title"]):
        tags.append("api")
    lines = [
        "---",
        f"title: {yaml_escape(title)}",
        f"description: {yaml_escape(desc)}",
        f"category: {cat}",
        f"sourceUrl: {yaml_escape(p.get('sourceUrl') or '')}",
        f"sourceRevision: {p.get('revisionId') or ''}",
        f"sourceUpdated: {yaml_escape(p.get('revisionTimestamp') or '')}",
        f"lastSynced: {yaml_escape(SYNC_STAMP)}",
        f"sourceStatus: {status}",
        "generated: true",
        "tags:",
    ]
    for t in tags:
        lines.append(f"  - {t}")
    # Starlight sidebar: hide huge generated dumps from autogenerate
    if path.startswith("api/classes/") or path.startswith("generated/"):
        lines.append("sidebar:")
        lines.append("  hidden: true")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def source_footer(p: dict) -> str:
    url = p.get("sourceUrl") or ""
    rev = p.get("revisionId") or ""
    ts = p.get("revisionTimestamp") or ""
    return f"""
## Source & attribution

- Original Frictional Wiki page: [{p.get('title')}]({url})
- Revision: `{rev}`
- Source update: `{ts}`
- Last synced: `{SYNC_STAMP}`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).
"""


def convert_page(p: dict, link_map: dict[str, str]) -> str:
    wt = p.get("wikitext") or ""
    if wt.strip().upper().startswith("#REDIRECT"):
        m = re.search(r"\[\[([^\]]+)\]\]", wt)
        target = m.group(1) if m else ""
        href = link_map.get(target.replace("_", " "), "")
        if href:
            return f"This page redirects to [{target}]({href}).\n"
        return f"This page redirects to `{target}` on the original Wiki.\n"
    wt = convert_codedoc(wt)
    md = wikitext_to_markdown(wt, link_map)
    return md


def main() -> None:
    pages = load_raw()
    resolve_transclusions(pages)
    link_map = build_link_map(pages)
    NORM_DIR.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)

    manifest = []
    api_index = []
    redirects = []
    statuses_count: dict[str, int] = {}
    written = 0
    skipped_editorial = 0
    broken = []
    empty = []
    wip_pages = []
    undocumented_api = 0

    # wipe previous generated md under api/classes and generated (not editorial)
    for folder in [
        DOCS / "api" / "classes",
        DOCS / "api" / "categories",
        DOCS / "generated",
    ]:
        folder.mkdir(parents=True, exist_ok=True)

    collisions: dict[str, list[str]] = {}

    for p in pages:
        title = p["title"]
        path = local_path(title)
        collisions.setdefault(path, []).append(title)
        rel = path
        if rel in EDITOR_PAGES:
            skipped_editorial += 1
            dest = DOCS / "generated" / Path(path).name
            rel = str(dest.relative_to(DOCS))
            path = rel

        wt = p.get("wikitext") or ""
        statuses = detect_status(wt)
        if "automatically generated" in wt.lower() or "{{ScriptingStub}}" in wt:
            if "undocumented" not in statuses and is_api_class(title):
                statuses.append("undocumented")
        md = convert_page(p, link_map)
        if len(md.strip()) < 5:
            empty.append(title)

        href = "/" + path.replace(".md", "/").replace(".mdx", "/")
        funcs = extract_functions(wt, title.split("/")[-1], href.rstrip("/"))
        api_index.extend(funcs)

        fm = frontmatter(p, path, md, statuses)
        banner = ""
        if "wip" in statuses or "constructionnotice" in wt.lower() or "{{constructionNotice" in wt:
            banner = ":::caution[SOURCE STATUS: WIP]\nThis source page is marked as undergoing editing on the Frictional Wiki.\n:::\n\n"
            wip_pages.append(title)
        elif "outdated" in statuses:
            banner = ":::caution[SOURCE STATUS: Outdated]\nThis source page is marked outdated.\n:::\n\n"
        elif "undocumented" in statuses and is_api_class(title):
            banner = ":::note[SOURCE STATUS: Undocumented]\nThis API page was auto-generated on the Frictional Wiki and has no written descriptions.\n:::\n\n"

        body = fm + banner + md + source_footer(p)
        out = DOCS / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(body, encoding="utf-8")
        written += 1

        (NORM_DIR / f"{p.get('pageid') or slugify(title)}.md").write_text(md, encoding="utf-8")

        st = "imported"
        if "wip" in statuses:
            st = "wip"
        elif "undocumented" in statuses:
            st = "undocumented"
        elif "outdated" in statuses:
            st = "outdated"
        elif len(wt) < 80:
            st = "incomplete"
        statuses_count[st] = statuses_count.get(st, 0) + 1

        manifest.append(
            {
                "originalTitle": title,
                "sourceUrl": p.get("sourceUrl"),
                "pageId": p.get("pageid"),
                "revisionId": p.get("revisionId"),
                "revisionTimestamp": p.get("revisionTimestamp"),
                "localSlug": path.replace(".md", "").replace(".mdx", ""),
                "category": classify(title),
                "status": st,
                "lastSynced": SYNC_STAMP,
                "wikitextLength": len(wt),
            }
        )
        redirects.append(
            {
                "from": title,
                "fromUrl": p.get("sourceUrl"),
                "to": href,
            }
        )

        # crude broken internal wiki links that we didn't map
        for m in re.finditer(r"\[([^\]]+)\]\(https://wiki\.frictionalgames\.com/page/([^)]+)\)", md):
            broken.append({"page": title, "target": m.group(2), "label": m.group(1)})

    DATA.joinpath("source-manifest.json").write_text(
        json.dumps({"syncedAt": SYNC_STAMP, "pages": manifest}, indent=2)
    )
    DATA.joinpath("redirects.json").write_text(json.dumps(redirects, indent=2))
    DATA.joinpath("api-index.json").write_text(json.dumps(api_index, indent=2))
    src_data = ROOT / "src" / "data"
    src_data.mkdir(parents=True, exist_ok=True)
    src_data.joinpath("api-index.json").write_text(json.dumps(api_index, indent=2))
    undocumented_api = sum(1 for fn in api_index if not fn.get("documented"))
    DATA.joinpath("image-attribution.json").write_text(
        json.dumps(
            {
                "note": "Wiki images were not copied. MediaWiki file pages were not confirmed to share a reusable license distinct from Frictional Games IP. Figures are referenced by original File: URL only.",
                "images": [],
            },
            indent=2,
        )
    )
    DATA.joinpath("glossary-aliases.json").write_text(
        json.dumps(
            {
                "HPS": "script-file",
                "HPM": "map-file",
                "Area": "area",
                "Entity": "entity",
                "Prop": "prop",
                "Helper": "helper",
                "WIP Mod": "wip-mod",
                "SH Probe": "sh-probe",
                "AngelScript": "angelscript",
                "HPL3": "hpl3",
            },
            indent=2,
        )
    )

    coll = {k: v for k, v in collisions.items() if len(v) > 1}
    report = [
        "# Content status",
        "",
        f"Last sync: `{SYNC_STAMP}`",
        "",
        f"- Raw pages loaded: **{len(pages)}**",
        f"- Markdown pages written: **{written}**",
        f"- Editorial paths skipped (preserved): **{skipped_editorial}**",
        f"- Empty / near-empty conversions: **{len(empty)}**",
        f"- API functions indexed: **{len(api_index)}**",
        f"- API functions without descriptions: **{undocumented_api}**",
        f"- External-or-unmapped wiki links remaining: **{len(broken)}**",
        "",
        "## Status counts",
        "",
    ]
    for k, v in sorted(statuses_count.items(), key=lambda kv: -kv[1]):
        report.append(f"- `{k}`: {v}")
    report += ["", "## WIP / construction pages", ""]
    for t in wip_pages:
        report.append(f"- {t}")
    report += ["", "## Empty conversions", ""]
    for t in empty:
        report.append(f"- {t}")
    report += ["", "## Path collisions", ""]
    for path, titles in sorted(coll.items()):
        report.append(f"- `{path}`: {', '.join(titles)}")
    report += ["", "## Unmapped wiki links (sample)", ""]
    seen = set()
    for b in broken[:80]:
        key = b["target"]
        if key in seen:
            continue
        seen.add(key)
        report.append(f"- `{key}` (from {b['page']})")
    REPORTS.joinpath("content-status.md").write_text("\n".join(report) + "\n")
    print(f"Wrote {written} pages, {len(api_index)} API functions")
    print(f"Status: {statuses_count}")
    print(f"Report: {REPORTS / 'content-status.md'}")


if __name__ == "__main__":
    main()

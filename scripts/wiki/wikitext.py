#!/usr/bin/env python3
"""MediaWiki wikitext → Markdown converter for Frictional Wiki pages."""

from __future__ import annotations

import html
import re
from typing import Callable

NAV_TEMPLATES = {
    "menubox",
    "hpl3somagettingstarted",
    "hpl3somanav",
    "hpl3nav",
    "tocright",
    "stub",
}

STATUS_TEMPLATES = {
    "wip": "wip",
    "workinprogress": "wip",
    "outdated": "outdated",
    "deprecated": "outdated",
    "todo": "incomplete",
    "incomplete": "incomplete",
    "unused": "legacy",
}

ASIDE_TEMPLATES = {
    "tip": "tip",
    "note": "note",
    "warning": "caution",
    "caution": "caution",
    "important": "note",
    "info": "note",
}


def detect_status(wikitext: str) -> list[str]:
    statuses: list[str] = []
    low = wikitext.lower()
    for name, status in STATUS_TEMPLATES.items():
        pat = r"\{\{\s*" + re.escape(name) + r"\b"
        if re.search(pat, low):
            if status not in statuses:
                statuses.append(status)
    if "automatically generated" in low and "lacks detailed" in low:
        statuses.append("undocumented")
    if "this page is a stub" in low or "{{stub" in low:
        if "incomplete" not in statuses:
            statuses.append("incomplete")
    return statuses


def _split_top_level_pipes(s: str) -> list[str]:
    parts: list[str] = []
    buf: list[str] = []
    depth = 0
    i = 0
    while i < len(s):
        if s.startswith("[[", i) or s.startswith("{{", i):
            depth += 1
            buf.append(s[i : i + 2])
            i += 2
            continue
        if s.startswith("]]", i) or s.startswith("}}", i):
            depth = max(0, depth - 1)
            buf.append(s[i : i + 2])
            i += 2
            continue
        if s[i] == "|" and depth == 0:
            parts.append("".join(buf))
            buf = []
            i += 1
            continue
        buf.append(s[i])
        i += 1
    parts.append("".join(buf))
    return parts


def _template_name(inner: str) -> str:
    inner = inner.strip()
    if not inner:
        return ""
    name = inner.split("|", 1)[0].split(":", 1)[0].strip()
    return name.lower().replace("_", "")


def convert_templates(text: str, convert_inline: Callable[[str], str]) -> str:
    # Repeatedly expand innermost {{...}}
    pattern = re.compile(r"\{\{([^{}]+)\}\}", re.DOTALL)

    def repl(m: re.Match) -> str:
        inner = m.group(1)
        name = _template_name(inner)
        parts = _split_top_level_pipes(inner)
        body = "|".join(parts[1:]).strip() if len(parts) > 1 else ""
        key = name.replace(" ", "")
        if key in NAV_TEMPLATES or key.startswith("navbox") or key.startswith("hpl3"):
            return ""
        if key in ("clear", "toc", "notoc", "for", "main", "see"):
            if key in ("main", "see", "for") and body:
                return f"\nSee also: {convert_inline(body)}\n"
            return ""
        if key in STATUS_TEMPLATES:
            label = STATUS_TEMPLATES[key].replace("wip", "Source WIP").replace(
                "outdated", "Outdated"
            ).replace("incomplete", "Incomplete").replace("legacy", "Legacy")
            extra = convert_inline(body) if body else ""
            return f"\n:::caution[SOURCE STATUS: {label}]\n{extra}\n:::\n"
        if key in ASIDE_TEMPLATES:
            kind = ASIDE_TEMPLATES[key]
            content = convert_inline(body) if body else ""
            title = kind.capitalize()
            return f"\n:::{kind}[{title}]\n{content}\n:::\n"
        if key in ("code", "mono"):
            return f"`{body}`"
        if key in ("key", "button", "kbd"):
            return f"<kbd>{html.escape(body)}</kbd>"
        if key == "displaytitle":
            return ""
        if key.startswith("color") or key == "fontcolor":
            return convert_inline(parts[-1]) if parts else body
        if key in ("anchor", "anchorid"):
            return f'<span id="{html.escape(body)}"></span>'
        if body:
            return convert_inline(body)
        return ""

    prev = None
    while prev != text:
        prev = text
        text = pattern.sub(repl, text)
    return text


def convert_wikilinks(text: str, link_map: dict[str, str]) -> str:
    def file_repl(m: re.Match) -> str:
        inner = m.group(1)
        parts = _split_top_level_pipes(inner)
        filename = parts[0].split(":", 1)[-1].strip()
        caption = parts[-1].strip() if len(parts) > 1 else filename
        caption = re.sub(r"^(thumb|right|left|center|\d+px)\s*\|?\s*", "", caption)
        url = f"https://wiki.frictionalgames.com/page/File:{filename.replace(' ', '_')}"
        return f"\n> **Figure (original Wiki file, not inlined):** [{caption or filename}]({url})\n"

    text = re.sub(r"\[\[(?:File|Image|file|image):([^\]]+)\]\]", file_repl, text)

    def link_repl(m: re.Match) -> str:
        inner = m.group(1)
        if inner.startswith("Category:") or inner.startswith("category:"):
            return ""
        parts = inner.split("|", 1)
        target = parts[0].strip()
        label = parts[1].strip() if len(parts) > 1 else target.split("/")[-1]
        if "#" in target:
            page, anchor = target.split("#", 1)
        else:
            page, anchor = target, ""
        page = page.replace("_", " ")
        href = link_map.get(page) or link_map.get(page.replace(" ", "_"))
        if href:
            if anchor:
                href = href.rstrip("/") + "/#" + _slug_anchor(anchor)
            return f"[{label}]({href})"
        wiki_url = "https://wiki.frictionalgames.com/page/" + target.replace(" ", "_")
        return f"[{label}]({wiki_url})"

    text = re.sub(r"\[\[([^\]]+)\]\]", link_repl, text)

    def ext_repl(m: re.Match) -> str:
        url, label = m.group(1), m.group(2)
        return f"[{label.strip()}]({url})"

    text = re.sub(r"\[(https?://[^\s\]]+)\s+([^\]]+)\]", ext_repl, text)
    return text


def _slug_anchor(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s


def convert_tables(text: str) -> str:
    def table_repl(m: re.Match) -> str:
        raw = m.group(0)
        inner = raw[2:-2]  # drop {| |}
        # strip table attributes on first line
        lines = inner.split("\n")
        rows: list[list[str]] = []
        current: list[str] = []
        is_header_row = False

        def flush():
            nonlocal current, is_header_row
            if current:
                rows.append(current)
                current = []
            is_header_row = False

        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            i += 1
            if not line:
                continue
            if line.startswith("{|"):
                continue
            if line.startswith("|+"):
                continue
            if line.startswith("|-"):
                flush()
                continue
            if line.startswith("!"):
                cells = re.split(r"\s*!!\s*", line.lstrip("!").lstrip())
                cleaned = []
                for c in cells:
                    if "|" in c and not c.strip().startswith("[["):
                        # attr|content
                        c = c.split("|", 1)[-1]
                    cleaned.append(c.strip())
                if not current:
                    is_header_row = True
                current.extend(cleaned)
                continue
            if line.startswith("|"):
                if line.startswith("|}"):
                    continue
                cells = re.split(r"\s*\|\|\s*", line.lstrip("|").lstrip())
                cleaned = []
                for c in cells:
                    rawc = c.strip()
                    if rawc.startswith(("align=", "style=", "class=", "colspan=", "rowspan=", "width=")):
                        if "|" in rawc:
                            rawc = rawc.split("|", 1)[-1].strip()
                        else:
                            continue
                    cleaned.append(rawc)
                current.extend(cleaned)
        flush()
        if not rows:
            return ""
        # normalize column count
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        header = rows[0]
        body = rows[1:] if len(rows) > 1 else []
        md = []
        md.append("| " + " | ".join(_cell(c) for c in header) + " |")
        md.append("| " + " | ".join("---" for _ in header) + " |")
        for r in body:
            md.append("| " + " | ".join(_cell(c) for c in r) + " |")
        return "\n" + "\n".join(md) + "\n"

    # non-greedy tables; wiki tables shouldn't nest often
    return re.sub(r"\{\|.*?\|\}", table_repl, text, flags=re.DOTALL)


def _cell(c: str) -> str:
    c = c.replace("\n", " ").strip()
    c = c.replace("|", "\\|")
    return c or " "


def convert_headings(text: str) -> str:
    def repl(m: re.Match) -> str:
        level = len(m.group(1))
        title = m.group(2).strip().strip("=").strip()
        level = min(level, 6)
        return f"{'#' * level} {title}"

    return re.sub(r"^(={2,6})\s*(.+?)\s*\1\s*$", repl, text, flags=re.MULTILINE)


def convert_lists(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    for line in lines:
        # Wiki lists are * / # prefixes. Do not treat Markdown headings (after
        # conversion) or Starlight asides (:::tip) as lists.
        if line.startswith(":::"):
            out.append(line)
            continue
        m = re.match(r"^([*#]+)\s+(.*)$", line)
        if not m:
            out.append(line)
            continue
        marks, rest = m.group(1), m.group(2)
        indent = "  " * (len(marks) - 1)
        bullet = "1." if marks[-1] == "#" else "-"
        out.append(f"{indent}{bullet} {rest}")
    return "\n".join(out)


def convert_inline_markup(text: str) -> str:
    # nowiki
    nowiki: list[str] = []

    def save_nowiki(m: re.Match) -> str:
        nowiki.append(m.group(1))
        return f"@@NOWIKI{len(nowiki)-1}@@"

    text = re.sub(r"<nowiki>(.*?)</nowiki>", save_nowiki, text, flags=re.DOTALL | re.I)

    codes: list[str] = []

    def save_pre(m: re.Match) -> str:
        if m.lastindex and m.lastindex >= 2:
            lang = m.group(1) or ""
            body = m.group(2) or ""
        else:
            lang = ""
            body = m.group(1) or ""
        body = html.unescape(body).strip("\n")
        fence_lang = (lang or "").strip()
        fence_lang = {
            "c++": "cpp",
            "angelscript": "angelscript",
            "as": "angelscript",
            "ini": "ini",
            "xml": "xml",
            "lua": "lua",
            "text": "",
        }.get(fence_lang.lower(), fence_lang)
        codes.append(f"\n```{fence_lang}\n{body}\n```\n")
        return f"@@CODE{len(codes)-1}@@"

    text = re.sub(
        r"<syntaxhighlight[^>]*?(?:lang(?:uage)?\s*=\s*[\"']?([\w+]+)[\"']?)?[^>]*>(.*?)</syntaxhighlight>",
        save_pre,
        text,
        flags=re.DOTALL | re.I,
    )
    text = re.sub(
        r"<pre[^>]*>(.*?)</pre>",
        save_pre,
        text,
        flags=re.DOTALL | re.I,
    )

    text = re.sub(r"<code>(.*?)</code>", lambda m: f"`{m.group(1)}`", text, flags=re.DOTALL | re.I)
    text = re.sub(r"<tt>(.*?)</tt>", lambda m: f"`{m.group(1)}`", text, flags=re.DOTALL | re.I)
    text = re.sub(r"<br\s*/?>", "  \n", text, flags=re.I)
    text = re.sub(r"</?div[^>]*>", "", text, flags=re.I)
    text = re.sub(r"</?span[^>]*>", "", text, flags=re.I)
    text = re.sub(r"</?center>", "", text, flags=re.I)
    text = re.sub(r"<small>(.*?)</small>", r"\1", text, flags=re.DOTALL | re.I)

    # bold/italic
    text = re.sub(r"'''''(.*?)'''''", r"***\1***", text)
    text = re.sub(r"'''(.*?)'''", r"**\1**", text)
    text = re.sub(r"''(.*?)''", r"*\1*", text)

    # definition lists — skip Starlight asides
    def defn(m: re.Match) -> str:
        line = m.group(0)
        if line.startswith(":::"):
            return line
        return m.expand(r"**\1**\n\n\2") if m.lastindex == 2 else m.expand(r"**\1**")

    text = re.sub(r"^;(.+?):\s*(.*)$", defn, text, flags=re.MULTILINE)
    text = re.sub(r"^;(.+)$", lambda m: f"**{m.group(1)}**", text, flags=re.MULTILINE)
    text = re.sub(
        r"^:(?!:)(.*)$",
        lambda m: f"> {m.group(1)}" if not m.group(0).startswith(":::") else m.group(0),
        text,
        flags=re.MULTILINE,
    )

    # hr
    text = re.sub(r"^----+$", "\n---\n", text, flags=re.MULTILINE)

    # restore
    for i, c in enumerate(codes):
        text = text.replace(f"@@CODE{i}@@", c)
    for i, c in enumerate(nowiki):
        text = text.replace(f"@@NOWIKI{i}@@", c)
    text = html.unescape(text)
    return text


class _Match:
    def __init__(self, groups):
        self._g = groups

    def group(self, i):
        return self._g[i]


def strip_chrome(text: str) -> str:
    text = re.sub(r"__NOTOC__|__TOC__|__NOEDITSECTION__|__FORCETOC__", "", text)
    text = re.sub(r"\[\[Category:[^\]]*\]\]", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # leftover empty template braces
    text = re.sub(r"\{\{\s*\}\}", "", text)
    return text


def wikitext_to_markdown(wikitext: str, link_map: dict[str, str] | None = None) -> str:
    link_map = link_map or {}
    text = wikitext.replace("\r\n", "\n")
    # redirects handled by caller
    text = strip_chrome(text)
    text = convert_templates(text, lambda s: s)
    text = convert_wikilinks(text, link_map)
    text = convert_tables(text)
    text = convert_lists(text)
    text = convert_headings(text)
    text = convert_inline_markup(text)
    # collapse extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"

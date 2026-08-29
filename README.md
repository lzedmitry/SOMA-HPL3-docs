# SOMA / HPL3 Modding Docs

Unofficial community documentation for [SOMA](https://www.frictionalgames.com/) modding and the HPL3 editors that ship with the game.

This is **not** an official Frictional Games site. Source material is the [Frictional Wiki HPL3/SOMA tree](https://wiki.frictionalgames.com/page/HPL3/SOMA), restructured into a learning path, recipes, and a searchable API.

![Documentation home](screenshots/home.png)

Live site: _set after GitHub Pages is enabled_.

## Local development

```bash
pnpm install
pnpm dev
```

```bash
pnpm build          # static site in dist/
pnpm sync:wiki      # fetch Frictional Wiki + regenerate generated pages
pnpm check          # internal links + link audit + typecheck
pnpm test
```

`pnpm sync:wiki` does **not** overwrite editorial pages listed in `scripts/wiki/transform.py` (`EDITOR_PAGES`).

## GitHub Pages

1. Settings → Pages → select **GitHub Actions** as the source.
2. Push `main`. Workflow: `.github/workflows/deploy.yml`.

The deploy workflow derives the GitHub Pages URL, project `base` path, repository URL, and “Edit this page” URL automatically from `GITHUB_REPOSITORY`.

Wiki sync (review PR, not auto-publish): `.github/workflows/sync-wiki.yml`.

## Project structure

```
src/content/docs/     Starlight pages (guides + generated reference)
src/styles/           SOMA-inspired tokens, docs, print
src/components/       Home, API browser, stats, pipeline
scripts/wiki/         MediaWiki fetch + wikitext transform + link audit
data/                 source-manifest.json, redirects, api-index
reports/              content-status.md, link-audit.md
```

The global sidebar is a list of **section doors**. Individual Area types, editor screens, and API classes stay on their URLs and on section index pages — they are not all listed in the sidebar.

## Attribution

See [ATTRIBUTION.md](ATTRIBUTION.md) and [Licensing](src/content/docs/about/licensing.mdx).

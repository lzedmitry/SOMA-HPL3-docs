# Contributing

## Fix a factual error

1. Open the page. Check **Source & attribution** for the Wiki revision.
2. If the Wiki is wrong, fix it there first when you can, then run `pnpm sync:wiki`.
3. If only our editorial wrapping is wrong, edit the file under `src/content/docs/` that is **not** `generated: true` in frontmatter.

## Improve a guide

Edit files in `src/content/docs/start`, `recipes`, `areas/index.mdx`, etc. Do not put unique editorial text only in `generated/` — the next sync can replace those files.

## Add an example

Keep examples short. Mark invented glue as **conceptual / editorial**. Never invent an HPL3 function signature.

## Update a Wiki-derived page

`pnpm sync:wiki` fetches changed revisions. Review `reports/content-status.md`. The GitHub Action opens a PR; it does not deploy.

## Add a screenshot

Do not paste Wiki screenshots unless you have confirmed the File: page license. Prefer original screenshots you took, with author in `data/image-attribution.json`.

## Add an API description

If the Wiki has no description, you may add a clearly labeled **Community/editor note** on an editorial page. Do not write it into the generated class page as if it came from the Wiki.

## Licensing

Read [ATTRIBUTION.md](ATTRIBUTION.md) and [Licensing](src/content/docs/about/licensing.mdx). Do not claim CC BY-SA unless the Wiki publishes that again.

## Style

See [docs/STYLE_GUIDE.md](docs/STYLE_GUIDE.md).

# Video research — SOMA / HPL3

Live-validated YouTube guides mapped onto this documentation.

**This site never downloads, rehosts, or mirrors video files.** Canonical URLs are built as `https://www.youtube.com/watch?v={youtubeId}`. Validation uses the official YouTube oEmbed endpoint. Duration is omitted when oEmbed does not expose it (no `yt-dlp`, no innertube scrape, no invented numbers).

Production rule: `review === "verified"` **and** `availability === "public"`. Everything else stays in this report / `data/videos/rejected.json`.

---

## SOURCE-BACKED SEEDS

| | Count |
| --- | ---: |
| Provided | 21 IDs + 2 playlists |
| Public (oEmbed 200) | 20 |
| Unavailable | 1 (`L_6mU5oC9Lk`, oEmbed HTTP 404) |
| Metadata mismatch (wrong video, substituted ID) | 0 |
| Verified and mapped | 20 seeds + 1 playlist discovery |
| Needs review | 0 in production |

### Seed table

| Provided ID | Live title (YouTube oEmbed) | Channel | Status | Quality | Mapped docs |
| --- | --- | --- | --- | --- | --- |
| `ZIN9v0SohHo` | HPL3 Tutorial: Setting Up A Mod Entry | Draugemalf | public | recommended | modding, first mod |
| `stYqcNsdEMw` | HPL3 Tutorial - Mod Dependencies : Amnesia Assets in SOMA | Draugemalf | public | **legacy** | modding/mod-dependencies |
| `lR-4OlG4uuc` | HPL3 Tutorial - Level Editor Interface | Draugemalf | public | recommended | level-editor |
| `c_XYn2lZrk4` | Creating A Room Part 1 (static objects) | Draugemalf | public | recommended | level-building |
| `6pEmswf4puU` | Creating A Room Part 2 | Draugemalf | public | recommended | entities, decals |
| `ES31l69TT-w` | Creating A Room Part 3 | Draugemalf | public | recommended | lighting, particles, fog |
| `DzsgvNO29Cw` | Creating A Room Part 4 | Draugemalf | public | recommended | audio, soundscape |
| `B9SvLnaFdjA` | Creating A Room Part 5 | Draugemalf | public | recommended | interactables |
| `hjobOt9uGAk` | Terrain Editor | Draugemalf | public | recommended | terrain |
| `z7ORkYt9kNg` | Setting Up Monsters | Draugemalf | public | useful | entities / NPC |
| `K9cfQLO92jg` | SH Probes | Draugemalf | public | useful | lighting |
| `_v6Pp4WDIWg` | Scripting Part 1 — Basics | Draugemalf | public | recommended | scripting |
| `1aCbCk_Lgic` | Scripting Part 2 | Draugemalf | public | recommended | doors / levers / buttons |
| `7oHfje9PKNo` | Scripting Part 3 — Trigger Areas | Draugemalf | public | recommended | areas/trigger |
| `GFbnbGBqS-k` | Scripting Part 4 | Draugemalf | public | recommended | climb / ladder / sticky |
| `_lS-5mdpiNQ` | Scripting Part 5 | Draugemalf | public | useful | tools / map variables |
| `xskqeO8XfuA` | Scripting Part 6 — Timers | Draugemalf | public | recommended | scripting/timers |
| `8XKKXO9K7fI` | HPL3 Tutorials Part 4 Creating a Mod | frictionalgames | public | recommended | modding |
| `TGhwsa1k1LU` | HPL3 Tutorials Part 3 Creating a Map | frictionalgames | public | recommended | level-editor |
| `CPKtK_koYh0` | HPL3 Tutorials Part 2 Scripting Overview | frictionalgames | public | recommended | scripting |
| `L_6mU5oC9Lk` | — | — | **unavailable** | not published | — |

Titles in the table are the current YouTube titles. Forum/Wiki historical names are stored as `sourceAlias`, never as the displayed title.

`stYqcNsdEMw` is **legacy**, not recommended: it explains the HPL3 dependency system using Amnesia assets in SOMA. That is not a current packing recipe.

### Playlists

| Playlist ID | Status | Notes |
| --- | --- | --- |
| `PLwJXvfVZGcJljQs1G-rAnipVf5SeuXawX` | public | Official Frictional HPL3 series. Discovery source for `3kD4dT4DNjs`. |
| `PLwJXvfVZGcJmwkaH6JiZUrlKAv5SXwwjW` | public | Draugemalf HPL3 tutorial series (room + scripting). |

---

## Queries executed

English (taxonomy + wiki concepts):

- SOMA modding / custom story tutorial / custom mod
- SOMA Level Editor / HPL3 Level Editor / SOMA map editor
- HPL3 scripting / SOMA scripting / HPL3 AngelScript
- HPL3 Model Editor / Material Editor / Particle Editor
- SOMA terrain / HPL3 terrain / SOMA Trigger Area / HPL3 Areas
- SOMA entities / HPL3 entities
- SOMA Blender / HPL3 Blender export / SOMA Maya
- SOMA material tutorial / SOMA particles
- SOMA sound modding / SOMA Soundscape / SOMA FMOD / SOMA Audition
- SOMA lighting / HPL3 SH Probe / SOMA mod debugging
- Visibility Area / VisibilityPortal / MapTransfer / Fog Area
- Climb Area / Ladder Area / Sticky Area / Exposure / HDR / Billboards / Detail Meshes
- Voice Handler / Sequences / Timers / Level Streaming / Helpers / Terminals

Localized (no verified HPL3/SOMA tutorial added):

- RU: `SOMA моддинг`, `SOMA редактор уровней`, `HPL3 моддинг`, `SOMA скрипты`, `SOMA создание мода`
- DE: `SOMA Modding Deutsch`, `HPL3 Editor Deutsch`, `SOMA Mod erstellen`
- FR: `SOMA modding français`, `éditeur HPL3 SOMA`, `mod SOMA tutoriel`
- IT: `SOMA modding italiano`, `editor HPL3 SOMA`, `tutorial mod SOMA`
- ES: `SOMA modding español`, `editor HPL3 SOMA`, `tutorial mods SOMA`

Localized hits were gameplay, reviews, HPL2/Amnesia: The Dark Descent, or unrelated. None passed content review as a SOMA/HPL3 tutorial. Production library is English-language videos; UI copy and summaries are localized.

---

## Candidates reviewed

| Bucket | Count |
| --- | ---: |
| Source-backed seed IDs | 21 |
| Playlist items checked beyond the seed list | official Frictional Part 1 (`3kD4dT4DNjs`) |
| Localized-search false positives (not added) | gameplay / HPL2 / reviews — rejected, IDs not stored as substitutes |
| Verified SOMA/HPL3 (production) | 21 |
| Recommended | 16 |
| Useful | 3 |
| Supplementary | 0 |
| Legacy | 2 (`stYqcNsdEMw`, `3kD4dT4DNjs`) |
| Rejected HPL2/HPL1 | not entered into the production manifest |
| Unavailable | 1 (`L_6mU5oC9Lk`) |
| Unverified | 1 (`L_6mU5oC9Lk` — topic never assigned) |

Discovery `3kD4dT4DNjs` = *HPL3 Tutorials Part 1 Setting up Codelite* (frictionalgames, 2015-10-28). **Legacy**: CodeLite is one documented editor; the Wiki also documents Visual Studio Code. New independent ID, not a substitute for any dead seed.

---

## Mapping

| | Count |
| --- | ---: |
| Docs pages with at least one mapped video | 63 |
| Videos mapped to docs | 21 / 21 |
| Unmapped verified videos | 0 |

Related videos are resolved at render time from `documentationPages` in `data/videos/video-manifest.json`. Pages do not hard-code YouTube IDs.

Checker: `pnpm videos:check` (oEmbed only). CI runs it with `continue-on-error` so a YouTube outage does not fail the docs build.

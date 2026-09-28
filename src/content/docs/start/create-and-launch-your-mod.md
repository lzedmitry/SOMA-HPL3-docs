---
title: Create and Launch Your Mod
description: "In this step, you will copy SOMA's known-working example mod and launch the copy before changing it."
category: start
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod"
sourceRevision: 7115
sourceUpdated: "2026-07-30T10:47:04Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - start
---
In this step, you will copy SOMA's known-working example mod and launch the copy before changing it.

## Make your own copy
1. Open `SOMA/mods/`.
1. Copy the entire `MinimalCustomMapMod` folder.
1. Rename the copy to a short project name, such as `MyFirstMod`.
1. Open the copied `entry.hpc` in a text editor.
1. Change at least `Title`, `Author`, and `Description`. Leave `Type="StandAlone"` and `InitCfg="config/main_init.cfg"` unchanged for this tutorial.

:::caution[Caution]
Do not rename or edit the original `MinimalCustomMapMod`. Keeping a clean copy gives you a working comparison if your configuration later breaks.
:::

Your copied folder should contain at least:

```
MyFirstMod/
├── config/
│   ├── lang/
│   │   └── english.lang
│   └── main_init.cfg
├── maps/
│   └── sample_map/
│       ├── sample_map.hpm
│       ├── sample_map.hpm_*
│       └── sample_map.hps
├── entry.hpc
├── LauncherPic.png
└── resources.cfg
```

The `.hpm_*` entries above represent the map's split data files. They are part of the map and must remain beside `sample_map.hpm`.

## Launch the untouched copy
1. Run `ModLauncher.exe`, or `ModLauncher_NoSteam.exe` for a non-Steam installation.
1. Choose **Play Custom Content**.
1. Select the title you placed in `entry.hpc`.
1. Launch the mod.

The included `config/main_init.cfg` starts `sample_map.hpm` from the `maps/` folder at `PlayerStartArea_1`.

## Checkpoint
Continue only when your copied mod appears in the launcher and loads its sample map.

## If it does not work
- **The mod is absent from the launcher:** confirm the copy is inside `SOMA/mods/` and has `entry.hpc` at its root.
- **The game starts but the map does not:** restore `config/main_init.cfg`, `resources.cfg`, and the complete `maps/sample_map/` folder from the clean example.
- **You want to understand the files:** read [Creating a Mod](/modding/creating-a-mod/), [Resources Configuration](/generated/resources-configuration/), and [Launch Configuration](/generated/launch-configuration/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`
- Source update: `2026-07-30T10:47:04Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

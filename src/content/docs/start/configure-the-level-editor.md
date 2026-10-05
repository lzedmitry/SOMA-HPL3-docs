---
title: Configure the Level Editor
description: The Level Editor must know which mod you are working on. This lets it resolve your mod's resources and save work in the correct context.
category: start
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Configure_the_Level_Editor"
sourceRevision: 7116
sourceUpdated: "2026-07-30T10:47:25Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - start
---
The Level Editor must know which mod you are working on. This lets it resolve your mod's resources and save work in the correct context.

## Select the work-in-progress mod
1. Launch `LevelEditor.exe` at least once, then close it.
1. Open the HPL3 user folder inside your Documents folder.
1. Create or edit `WIPMod.cfg`.
1. Point it to the copied mod's `entry.hpc` using its full path:

```
<WIPmod Path="C:/full/path/to/SOMA/mods/MyFirstMod/entry.hpc" />
```

1. Save the file and reopen `LevelEditor.exe`.

The exact path depends on where *SOMA* is installed. Forward slashes keep the XML path easy to read.

:::note[Note]
The [SOMA Mod Manager](/tools/soma-mod-manager/) can perform this synchronization for you. Manual setup is shown here so you know which file controls it.
:::

## Checkpoint
The Level Editor title bar should include `(Working on mod)`.

## If it does not work
- Confirm the path ends at your copied `entry.hpc`, not merely the mod folder.
- Confirm the file is named exactly `WIPMod.cfg`, not `WIPMod.cfg.txt`.
- Confirm `entry.hpc` is still valid XML.
- Re-read [Setup Modding Environment](/modding/setup-modding-environment/) for custom-asset lookup directories. The bundled sample does not require you to add custom lookup directories yet.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Configure the Level Editor](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Configure_the_Level_Editor)
- Revision: `7116`
- Source update: `2026-07-30T10:47:25Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

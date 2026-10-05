---
title: Developer Commands
description: "When launching a game or a mod via a Command Prompt (CMD .bat file), you can pass optional arguments which will affect the way the mod is loaded by the game. It can be useful for mods which require custom assets and scri"
category: modding
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Developer_Commands"
sourceRevision: 5563
sourceUpdated: "2020-11-10T03:36:25Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - modding
---
When launching a game or a mod via a Command Prompt (CMD .bat file), you can pass optional arguments which will affect the way the mod is loaded by the game. It can be useful for mods which require custom assets and scripts, or if you want to customize it further than that.

## Command Line Arguments
:::note[Note]
You can add multiple arguments and combine them when launching the game. It doesn't have to be only one argument.
:::

| Argument | Default Value | Description | Example |
| --- | --- | --- | --- |
| user | `Default` | Starts the game with a different user name. | `Soma.exe -user Default_dev` |
| cfg | `config/main_init.cfg` | Changes the main config file that is used when starting the mod. | `Soma.exe -cfg config/main_init_dev.cfg` |
| mod | *No default value.* | Points to a mod entry file and launches the mod instead of the main game. Use this if you want to run your mod in dev mode. | `Soma.exe -mod "C:\SOMA\mods\myMod\entry.hpc"` |
| map | Stated at `StartMap->File` in `main_init.cfg`. | The game loads a specific map after startup. | `Soma.exe -map "mods/myMod/maps/myMap.hpm"` |
| mapfolder | Stated at StartMap->Folder in `main_init.cfg`. | Starts the game with a specific map folder. | `Soma.exe -mapfolder "mods/myMod/maps"` |
| mappos | Stated at `StartMap->Pos` in `main_init.cfg.` | Sets a specific start position to be used in a map. | `Soma.exe -map "PathToMap/myMap.hpm" -mappos "MyPos"` |
| workdir | *No default value.* | Which directory the game exe is located. Can be used to change between engine and main redist. | *No default value.* |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Developer Commands](https://wiki.frictionalgames.com/page/HPL3/SOMA/Developer_Commands)
- Revision: `5563`
- Source update: `2020-11-10T03:36:25Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

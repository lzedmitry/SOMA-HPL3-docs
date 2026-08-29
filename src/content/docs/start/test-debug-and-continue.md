---
title: Test Debug and Continue
description: "Your mod, map, and first script now work. This final step establishes a repeatable development loop and points to deeper documentation."
category: start
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Test_Debug_and_Continue"
sourceRevision: 7119
sourceUpdated: "2026-07-30T10:50:15Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - start
---
Your mod, map, and first script now work. This final step establishes a repeatable development loop and points to deeper documentation.

## Use the development loop
1. Make one small map or script change.
1. Save the changed file.
1. Return to the running game.
1. Press `F5` when the map must be restarted.
1. If the change fails, press `F1` and check **Show Error List** and **Show HPL Log** before changing anything else.

For faster testing, launch the mod in development mode with the `-mod` command-line argument:

```
Soma.exe -mod "C:\full\path\to\SOMA\mods\MyFirstMod\entry.hpc"
```

The path passed to `-mod` is the full path to the mod's `entry.hpc`. See [Developer Commands](/modding/developer-commands/) for `-map`, `-mapfolder`, `-mappos`, and other launch options.

## When something breaks
Work backward to the last passing checkpoint:

1. If the script fails, temporarily remove only your newest script change and read the first relevant error.
1. If the map fails, reopen it in the editor and check that its split `.hpm_*` files are present.
1. If the mod fails before loading the map, compare `entry.hpc`, `resources.cfg`, and `config/main_init.cfg` with the clean `MinimalCustomMapMod`.
1. If the editor cannot find mod content, recheck `WIPMod.cfg` and the `(Working on mod)` indicator.

See [Developer Debug Menu](/modding/developer-debug-menu/) for the full set of debug controls.

## Where to go next
Choose documentation by task rather than reading the entire wiki in order:

- **Build a larger environment:** [SOMA Level Design](/generated/level-design-hub/)
- **Learn map scripting:** [HPL3 Scripting Guide](/scripting/hpl3-scripting-guide/)
- **Learn programming fundamentals:** [AngelScript Fundamentals](/scripting/angelscript/angelscript-fundamentals/)
- **Understand mod configuration:** [SOMA Modding](/generated/modding-hub/)
- **Prepare for release:** [Mod Distribution](https://wiki.frictionalgames.com/page/Mod_Distribution)

## Final checkpoint
You have completed Getting Started when you can:

- launch your copied mod;
- edit and save its map;
- edit its map script and see the result;
- reload the map; and
- locate script errors and the HPL log.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Test Debug and Continue](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Test_Debug_and_Continue)
- Revision: `7119`
- Source update: `2026-07-30T10:50:15Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

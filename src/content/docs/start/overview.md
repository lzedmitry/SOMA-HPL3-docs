---
title: Getting Started
description: "This guide takes you from a working installation of SOMA to a stand-alone mod with a map you can edit and a script you have changed yourself. It uses the MinimalCustomMapMod included with the game, so you begin with a kn"
category: start
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started"
sourceRevision: 7120
sourceUpdated: "2026-07-30T10:50:35Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - start
---
This guide takes you from a working installation of *SOMA* to a stand-alone mod with a map you can edit and a script you have changed yourself. It uses the `MinimalCustomMapMod` included with the game, so you begin with a known-working configuration instead of assembling every file from scratch.

:::tip[Tip]
Complete the steps in order. Each step ends with a checkpoint. Do not continue until the checkpoint works; this keeps configuration, map, and script problems separate.
:::

## What you will make
By the end of this path, you will have:

- your own mod folder, separate from the bundled example and the base game;
- a stand-alone mod that starts directly in its map;
- the Level Editor configured to work on that mod;
- a saved change to an HPL3 `.hpm` map; and
- a changed `.hps` map script which displays `Hello World!` in-game.

No previous HPL modding experience is required. Basic programming knowledge is helpful for the scripting step, but not required for completing it.

## The path
| Step | Task | You are finished when... | Detailed reading |
| --- | --- | --- | --- |
| 1 | **[Prepare your tools](/start/prepare-your-tools/)** | *SOMA*, the Level Editor, and a text editor are ready. | [SOMA Modding](/generated/modding-hub/) |
| 2 | **[Create and launch your mod](/start/create-and-launch-your-mod/)** | Your copied mod appears in the launcher and its sample map starts. | [Creating a Mod](/modding/creating-a-mod/); [MinimalCustomMapMod](/modding/minimalcustommapmod/) |
| 3 | **[Configure the Level Editor](/start/configure-the-level-editor/)** | The editor title bar says `(Working on mod)`. | [Setup Modding Environment](/modding/setup-modding-environment/) |
| 4 | **[Edit your first map](/start/edit-your-first-map/)** | A visible map change survives saving, closing, and reopening the editor. | [Level Design](/generated/level-design-hub/); [Level Editor View](/level-editor/level-editor-view/) |
| 5 | **[Add your first script](/start/add-your-first-script/)** | `Hello World!` appears when the map starts. | [Scripting Workflow and Structure](/scripting/scripting-workflow-and-structure/); [Hello World](/scripting/hello-world/) |
| 6 | **[Test, debug, and continue](/start/test-debug-and-continue/)** | You can reload the map, find script errors, and choose the next documentation section. | [Developer Debug Menu](/modding/developer-debug-menu/); [Developer Commands](/modding/developer-commands/) |

## Ground rules
- **Work in your mod folder.** Do not edit base-game files or the original `MinimalCustomMapMod`.
- **Use relative resource paths.** Your mod should not depend on another user's installation path.
- **Keep the whole map together.** An HPL3 map consists of the main `.hpm` file and its accompanying `.hpm_*` files. Do not treat it as an old HPL2 `.map` file.
- **Test one change at a time.** First launch the untouched copy, then configure the editor, then edit the map, then edit the script.
- **Keep names simple at first.** Use letters, numbers, and underscores for folders, maps, and object names.

## If you are already experienced
The table above is the complete route. You can skip directly to any checkpoint and use the linked articles as reference. The step pages intentionally contain only the minimum context, action, expected result, and recovery information needed for a first successful mod.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started)
- Revision: `7120`
- Source update: `2026-07-30T10:50:35Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

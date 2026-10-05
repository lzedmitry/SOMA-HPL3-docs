---
title: Edit Your First Map
description: You will use the working sample as your first map and make one visible editor change. Starting from the sample avoids mixing basic editor learning with player-start and launch-configuration problems.
category: start
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Edit_Your_First_Map"
sourceRevision: 7117
sourceUpdated: "2026-07-30T10:47:43Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - start
---
You will use the working sample as your first map and make one visible editor change. Starting from the sample avoids mixing basic editor learning with player-start and launch-configuration problems.

## Open the map
1. In `LevelEditor.exe`, choose **File → Open**.
1. Open `MyFirstMod/maps/sample_map/sample_map.hpm`.
1. Move around the perspective viewport and inspect the existing room. See [Level Editor View](/level-editor/level-editor-view/) if the viewport controls are unfamiliar.

## Make one visible change
Select an existing object and move it a small, obvious distance with the translation tool. Save the map, close it, and reopen `sample_map.hpm`.

:::tip[Tip]
For the first checkpoint, change only one existing object. Add new objects, lighting, and gameplay entities after the edit-save-launch loop is proven.
:::

HPL3 stores different object categories in files beside the main map, such as `sample_map.hpm_Entity`, `sample_map.hpm_Light`, and `sample_map.hpm_StaticObject`. Keep these files together with `sample_map.hpm`.

## Test in-game
Launch your mod again and confirm that the object moved. If the old version appears, close the game and relaunch the mod to rule out cached state.

## Checkpoint
Continue when the changed object:

- remains moved after reopening the map in the editor; and
- appears in its new position in-game.

## If it does not work
- Confirm the editor title bar says `(Working on mod)`.
- Confirm you opened the map inside your copied mod, not the bundled example.
- Confirm the complete set of `.hpm` and `.hpm_*` files is writable and remains in the same folder.
- If the editor view is the problem, use [Level Editor View](/level-editor/level-editor-view/). For individual object types, use the relevant section of [SOMA Level Design](/generated/level-design-hub/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Edit Your First Map](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Edit_Your_First_Map)
- Revision: `7117`
- Source update: `2026-07-30T10:47:43Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

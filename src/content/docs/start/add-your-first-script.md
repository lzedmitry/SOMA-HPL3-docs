---
title: Add Your First Script
description: "Every map can have a map script. For the sample map, it is samplemap.hps beside samplemap.hpm."
category: start
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Add_Your_First_Script"
sourceRevision: 7183
sourceUpdated: "2026-08-31T10:55:36Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - start
---
Every map can have a map script. For the sample map, it is `sample_map.hps` beside `sample_map.hpm`.

:::note[Note]
It is highly recoomended to use Visual Studio Code with the HPL3 Language Tools extension for scripting.
:::

## Add a visible script change
#Open `MyFirstMod/maps/sample_map/sample_map.hps` in your text editor.
#Find `void OnStart()` inside the `cScrMap` class.
#Add the debug-message call between its braces:

```
void OnStart()
{
    cLux_AddDebugMessage("Hello World!");
}
```

#Save the script.
#Launch the mod. If the map was already running in development mode, press `F5` to reload it.

The text `Hello World!` should appear at the lower-left of the screen when the map starts.

:::note[Note]
Keep the generated includes, the `cScrMap : iScrMap` declaration, and the surrounding callback structure. This tutorial changes only the body of `OnStart()`.
:::

## Checkpoint
Continue when the message appears in-game after a fresh map start.

## If it does not work
*Confirm the script has the same base name and folder as the map: `sample_map.hpm` and `sample_map.hps`.
*Confirm the line ends with a semicolon and uses straight quotation marks.
*Confirm you edited the script inside your copied mod.
*Press `F1` in development mode, then use **Show Error List** or **Show HPL Log**.

Read [Scripting Workflow and Structure](/scripting/scripting-workflow-and-structure/) for the generated map-script layout and [Hello World](/scripting/hello-world/) for the focused scripting lesson.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Add Your First Script](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Add_Your_First_Script)
- Revision: `7183`
- Source update: `2026-08-31T10:55:36Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

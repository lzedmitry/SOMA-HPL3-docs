---
title: Tool
description: This area when entered by the player will hold out a specified tool from the players inventory and be holstered when exiting the area.
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Areas/Tool_Area"
sourceRevision: 6768
sourceUpdated: "2024-02-08T17:10:07Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
This area when entered by the player will hold out a specified tool from the players inventory and be holstered when exiting the area.

## Properties
> **Figure (original Wiki file, not inlined):** [A functioning Omnitool panel using an orange Tool Area](https://wiki.frictionalgames.com/page/File:Tool_area.png)

### Tool
- **ToolsToEquip**: The Tool to hold out when a player is inside the area. Must be in the players inventory.
- **ConnectedToolArea**: Additional [Tool Areas](/areas/tool-area/) that can be passed through without holstering the tool that is equipped. Areas must be at least touching.
- **LookEntities**:An entity that must be looked at to raise the tool
- **LookEntityLOS**: If the **LookEntities** must have uninterupted line of sight

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Areas/Tool Area](https://wiki.frictionalgames.com/page/HPL3/SOMA/Areas/Tool_Area)
- Revision: `6768`
- Source update: `2024-02-08T17:10:07Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

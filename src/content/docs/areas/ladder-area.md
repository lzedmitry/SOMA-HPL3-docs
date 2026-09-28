---
title: Ladder
description: The Ladder Area allows players to climb a ladder. This area will also cause the climbing hands animation. If the animation of the hands does not meet the spokes of the ladder then the area must be carefully moved while g
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/Ladder_Area"
sourceRevision: 6748
sourceUpdated: "2024-01-25T21:40:43Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
The Ladder Area allows players to climb a ladder. This area will also cause the climbing hands animation. If the animation of the hands does not meet the spokes of the ladder then the area must be carefully moved while grid snap is disabled. In order to work properly, an [InteractAux Area](/areas/interactaux-area/) with its **InteractParent** property set to the Ladder Area must be placed next to the Trigger Area, as seen in the image.

## Properties
> **Figure (original Wiki file, not inlined):** [Ladder.png](https://wiki.frictionalgames.com/page/File:Ladder.png)

The  where the player will end up when exiting the ladder from the top.
### Base
- **Material**: The type of sound effect to play while climbing
- **Exit_Top**: The [Trigger Area](/areas/trigger-area/) the players feet will be move to when exiting the ladder from the top
- **Exit_TopCrouching**: If the player should be crouched after exiting the ladder from the top
- **Exit_Bottom**: The [Trigger Area](/areas/trigger-area/) the players feet will be move to when exiting the ladder from the bottom
- **Exit_BottomCrouching**: If the player should be crouched after exiting the ladder from the bottom

### Attachment
- **ParentAttachEntity**: The name of an entity that this soundscape is parented to.
- **ParentAttachUseRotation**: If the rotation of the parent should affect the soundscape.
- **ParentAttachBody**: The name of the body in the parent entity to attach to.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/Ladder Area](https://wiki.frictionalgames.com/page/HPL3/Areas/Ladder_Area)
- Revision: `6748`
- Source update: `2024-01-25T21:40:43Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

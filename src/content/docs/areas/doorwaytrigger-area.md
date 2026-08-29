---
title: DoorwayTrigger
description: This area is useful for telling you when the player has walked into a particular part of the map. You set up a doorway with the Z-axis pointing in to the 'inside' of the room/area and away from the 'outside'. When the pl
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/DoorwayTrigger_Area"
sourceRevision: 6775
sourceUpdated: "2024-02-08T18:03:10Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
This area is useful for telling you when the player has walked into a particular part of the map. You set up a doorway with the Z-axis pointing in to the 'inside' of the room/area and away from the 'outside'. When the player walks in through the door, the DoorwayCallback is called with an *alState* parameter of 1. When the player walks out through the door, the callback is called with an *alState* of -1.

You can also link sets of doorways, which is a great way to figure out if the player is inside an irregular space. If you specify the DoorwayGroup property, then you can use the function `Doorway_PlayerIsInGroup()` to check if the player has crossed into the space delimited by these doorways. For example, if you cross any of the doorways going 'inwards' i.e. *alState == 1*, then you are in the group; crossing any going 'outwards' i.e. *alState == -1* means you are outside the group.

## Properties
### Base
- **BlockLineOfSight**: Blocks line of sight.
- **EventInstanceTag**: A tag used by the event system to group objects.
- **UserVar**: Arbitrary user variable. Acessable by calling the script function `Entity_GetVar<type>()`

### Collide Callbacks
- **CC_Entities**: A list separated by commas or spaces of all entities that can trigger the callback. *player* is the player character.
- **CC_Funcs**: A list of functions that will run when the area is triggered. Press copy to generate a callback function and copy to the clipboard

### Attachment
- **ParentAttachEntity**: The name of an entity that this soundscape is parented to.
- **ParentAttachUseRotation**: If the rotation of the parent should affect the soundscape.
- **ParentAttachBody**: The name of the body in the parent entity to attach to.
- **ParentAttachLocked**: Locks the area to the parent and disables local movement.

### DoorwayTrigger
- **DoorwayEntity**: The entities that can trigger this area
- **DoorwayGroup**: The shared group of potentially multiple doorways. Links multiple doorway areas together.
- **DoorwayCallback**: The callback to run when a player enters or exits a doorway
- **DoorwayCheckCenterOnly**: If only the center of the area should check for collisions.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/DoorwayTrigger Area](https://wiki.frictionalgames.com/page/HPL3/Areas/DoorwayTrigger_Area)
- Revision: `6775`
- Source update: `2024-02-08T18:03:10Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

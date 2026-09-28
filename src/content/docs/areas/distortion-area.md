---
title: Distortion
description: This area will apply a Distortion Effect to the player while they are in it.
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Areas/Distortion_Area"
sourceRevision: 6774
sourceUpdated: "2024-02-08T17:54:04Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
This area will apply a Distortion Effect to the player while they are in it.

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

### DistortionArea
- **EffectAmount**: The strength of the distortion. Values between 0 - 1
- **FadeInTime**: Time in seconds to fade in the distortion effect
- **FadeOutTime**: Time in seconds to fade out the distortion effect
- **Volume**: The volume of the distorted audio that plays
- **SourceEntity**: The name of an optional entity that will increase the effect as the player gets closer to it
- **SourceEntityMinDist**: The distance to the **SourceEntity** at which the effect is at its maximum
- **SourceEntityMaxDist**:The distance to the **SourceEntity** at which the effect ends. If a value of -1 is set, the size of the area will be used instead

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Areas/Distortion Area](https://wiki.frictionalgames.com/page/HPL3/SOMA/Areas/Distortion_Area)
- Revision: `6774`
- Source update: `2024-02-08T17:54:04Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

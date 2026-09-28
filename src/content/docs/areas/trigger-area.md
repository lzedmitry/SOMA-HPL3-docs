---
title: Trigger
description: "Helper Function: helperarea.hps"
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/Trigger_Area"
sourceRevision: 6755
sourceUpdated: "2024-02-01T15:01:08Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
Helper Function: [helper_area.hps](https://wiki.frictionalgames.com/page/Area_Helper)   

The Trigger area runs a callback function when an entity collides or otherwise interacts with it.

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

### Basic Callbacks
- **PlayerLookAtCallback**: A function that will run when looking at the entity. Press generate to generate a name for this text field.
- **PlayerLookAtCallbackAutoRemove**: Removes the callback after it fires once.
- **PlayerLookAtCheckCenterOfScreen**: Only counts as looked if the entity is in the center of the screen.
- **PlayerLookAtCheckRayInIntersection**: Only counts as looked at if their is a clear line of sight, i.e. not through a transparent object. *Can return false negatives, especially if **PlayerLookAtCheckCenterOfScreen** is disabled.*
- **PlayerLookAtMaxDistance**: Max distance an entity can be from the area. Values lower than 0 default to max distance.
- **PlayerLookAtCallbackDelay**: Time in seconds to delay the callback
- **PlayerInteractCallback**: Callback when the player interacts with the entity, i.e. grabbing or using. Press generate to generate a name for this text field.
- **PlayerInteractCallbackAutoRemove**: Removes the callback after it fires once.

### Interaction
Settings used when the player interacts with the entity by clicking on it.
- **CanInteractWithoutCallback**: Allows the area to be interacted with despite having an empty callback.
- **MaxFocusDistance**: Maximum distance a player can be to interact. Values lower than 0 are set to the default.
- **CustomInteraction**: The icon shown when interaction is possible.

## Callback function syntax
This is the basic syntax for a collision callback function.

```
bool FunctionName(const tString &in asParent, const tString &in asChild, int alState)
{
    if(alState == 1) // 1 = entering area, -1 = leaving area
    {
        // Insert code here
    }
    return false;
}
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/Trigger Area](https://wiki.frictionalgames.com/page/HPL3/Areas/Trigger_Area)
- Revision: `6755`
- Source update: `2024-02-01T15:01:08Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

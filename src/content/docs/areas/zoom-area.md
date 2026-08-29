---
title: Zoom
description: "The Zoom area is an area that when interacted with by the player, will temporarily center their screen on the zoom area. This is commonly used on maps, windows, signs, and posters. Text can be displayed to caption or des"
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/Zoom_Area"
sourceRevision: 6772
sourceUpdated: "2024-02-08T17:36:09Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
## Overview
The Zoom area is an area that when interacted with by the player, will temporarily center their screen on the zoom area. This is commonly used on maps, windows, signs, and posters. Text can be displayed to caption or describe the in-game object. Optionally, an imgui function can be supplied and run when the area is interacted with allowing graphics to be displayed dynamically.

## Properties
> **Figure (original Wiki file, not inlined):** [A zoom area in front of a sign](https://wiki.frictionalgames.com/page/File:Zoom_area.png)

### Base
- **BlockLineOfSight**: Blocks line of sight.
- **EventInstanceTag**: A tag used by the event system to group objects.
- **UserVar**: Arbitrary user variable. Accessible by calling the script function `Entity_GetVar<type>()`

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
### ZoomText
- **TextCategory**: The category from the lang file to use
- **TextEntry**: The Text entry in the lang file to use
- **ZoomDistance**: The distance from the center of the Zoom Area where the camera will move to
- **OnGuiFuntion**: The name of the imgui function to call to render optional graphics. Press generate to generate a name for this text field.
### Appearance
- **VerticalFOV**: The FOV the camera should be set to when interacting with the zoom area

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/Zoom Area](https://wiki.frictionalgames.com/page/HPL3/Areas/Zoom_Area)
- Revision: `6772`
- Source update: `2024-02-08T17:36:09Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

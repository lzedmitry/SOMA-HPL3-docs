---
title: Sticky
description: "= Sticky Area ="
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/Sticky_Area"
sourceRevision: 6770
sourceUpdated: "2024-02-08T17:19:13Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
= Sticky Area =

## Overview
> **Figure (original Wiki file, not inlined):** [A sticky area being used in 01_04_transport_station.hpm. Light blue = Sticky Area, Green = Interact Aux Area](https://wiki.frictionalgames.com/page/File:Sticky_area.png)

The Sticky Area is a area that can be used to allow entities to attach and detach to the area. This effect can simulate cables, computer chips, or any interactable physics entity that can be plugged in or unplugged. 

## Properties
### Base
- **MoveBody**: If the body of the entity to attach should be moved into the position of the area when attached
- **RotateBody**: If the body of the entity to attach should be rotated to match the sticky area when attached
- **AttachableBodyName**: The name and body of the entity to attach. I.e. *[entity_name]_Body_[#]*
- **PoseTime**:  The time in seconds it takes for the entity to move and rotate into place when attached
- **CheckCenterInArea**: Requires the center of the body of the entity to attach to be inside the sticky area
- **CanDetach**: If the body of the area of the entity to attach can be detached to the sticky area
- **RequiresInteraction**: If the entity requires player interaction to attach to the sticky area

### Callbacks
- **AttachFunction**: Function to call when an entity attaches to the sticky area. Press copy to generate a callback function and copy to the clipboard
- **DetachFunction**: Function to call when an entity detaches from the sticky area. Press copy to generate a callback function and copy to the clipboard

### Effects
- **AttachSound**: The sound to be played when an entity attaches to the area
- **DetachSound**: The sound to be played when an entity detaches from the area
- **AttachPS**: The particle system to be created when an entity attaches to the area
- **DetachPS**: The particle system to be created when an entity detaches from the area

### Attachment
- **ParentAttachEntity**: The name of an entity that this area is parented to.
- **ParentAttachUseRotation**: If the rotation of the parent should affect the area.
- **ParentAttachBody**: The name of the body in the parent entity to attach to.

### Springy
Springy behavior is best described as a tendency for the entity to attach to be attracted to the sticky area and for the entity to slightly resist being detached.

- **Springy_Active**: If springy behavior is enabled
- **Springy_DetachDistanceMul**: Distance multiplier for the entity to be from the center of the area to detach. 
- **Springy_ForceMul**: Force multiplier to be applied to the entity when detached
- **Springy_ReleaseTime**: Time in seconds to delay detaching the entity once the entity meets the detach criteria
- **Springy_DetachLoopSound**: A looping sound to play when in the process of detaching an entity from a sticky area

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/Sticky Area](https://wiki.frictionalgames.com/page/HPL3/Areas/Sticky_Area)
- Revision: `6770`
- Source update: `2024-02-08T17:19:13Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

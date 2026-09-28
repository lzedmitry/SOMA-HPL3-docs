---
title: Physics Body Properties
description: "This tab presents the attachment tool, its workings are explained next: There are several buttons that represent each object type that can be attached to a body. The ones that are pressed indicate that the type they repr"
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Entities/Physics_Body_Properties"
sourceRevision: 6809
sourceUpdated: "2024-05-14T05:04:22Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
### General Parameters
- **Name**: Name of the body.
- **Position**: 3D Vector storing the position in world of the center of the body.
- **Rotation**: 3D Vector storing the body rotation.
- **Scale**: 3D Vector storing the scale of the body.

#### **Body Specific**
- **Body Material**: Physics material for the body.
- **Mass**: Mass for the body. The higher the value, the heavier the body will be. A zero value means infinite.
- **Angular Damping:** “Air Friction” applied to the rotational speed of the body. Takes a float value between 0 (no damping) and 1 (max damping).
- **Linear Damping:** “Air Friction” applied to the linear speed of the body. Takes a float value between 0 (no damping) and 1 (max damping).
- **Max Angular Speed**: Maximum speed that the body can rotate with.
- **Max Linear Speed**: Maximum speed that the body can translate with.
- **Buoyancy Density Mul**: Multiplies the buoyancy effect on the body when inside a liquid body. A zero value means it will not be affected by liquid at all.
- **Blocks Sound**: Sets if the body blocks sounds.
- **Blocks Light**: Sets if the body blocks lights.
- **Continuous Collision**: If the body should use continuous collison detection or not. This is good for small bodies (or larger bodies that has one or many small colliders) that would easily stick or tunnel other bodies. It is also good for high speed bodies.
- **Can attach character**: If a character standing on the body will be attached. For example if you have a moving platform and want the character to move with it as it moves.
- **Pushed by character gravity**: If the body will be affected when a characters stands on top.
- **Collide character**: Sets whether the body should collide with the player or not.
- **Collide non character**: Sets whether the body should collide with non-player bodies or not.
- **Volatile:** If a body might disappear or for some reason leave the way open for AI. Used for bodies of mass 0.
- **Use surface effects:** If the body should use the material settings for effects (described in materials.cfg ) or not. If this is false there will not be sounds or particle effects created by impacts, scraping etc.
- **Has gravity**: Sets whether gravity affects the body or not.

#### Attachments Tab
This tab presents the attachment tool, its workings are explained next: There are several buttons that represent each object type that can be attached to a body. The ones that are pressed indicate that the type they represent will be selectable when activating the attachment tool. The 'Attach' button will start the tool, moving around the mouse while it is active will highlight objects that belong to the selectable types. Clicking on them will add them to the entities to be attached. If already attached, the object will be detached. Clicking the mouse on no object or pressing the 'Attach' button again (now 'Done') will stop the attachment tool, and all objects that are displayed as attached before doing so will become really attached to the body. The 'Clear attachments' button is self explanatory. It will just clear any attachments made.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Entities/Physics Body Properties](https://wiki.frictionalgames.com/page/HPL3/Entities/Physics_Body_Properties)
- Revision: `6809`
- Source update: `2024-05-14T05:04:22Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

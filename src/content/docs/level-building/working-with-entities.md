---
title: Working with Entities
description: "= Entities ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Working_with_Entities"
sourceRevision: 7098
sourceUpdated: "2026-07-30T09:59:41Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= Entities =

Entities are vital components for a map, be it decoration or be it gameplay wise. They are the dynamic part of the level: interactable objects, disappearing walls, anything that should not remain constant when playing through a level falls into this category.

## General Parameters
- **Name**: Name for the entity.
- **Active**: If the entity should start as active. When set to inactive, the entity will be drawn dissolved according to the "Disabled mesh coverage" setting in options.
- **Position**: 3D Vector storing the position in world.
- **Rotation**: 3D Vector storing the rotation.
- **Scale**: 3D Vector storing the scale of the placed object.
- **Entity File**: file name (.ent) for the entity.
- **Notes**: pressing this button will show any notes defined for the currently selected entity. If the button is disabled, that means there are no defined notes.
- **Pose**: if the button is enabled, it means the currently selected entity has a poseable skeleton. Pressing the button will start the entity poser mode. More on this mode [here](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:entityposer_editmode).
- **Body names**: this list will display the body names in the entity.
** **Copy name''': pressing this button will copy the body name selected in the list.

## Specific Parameters
This tab will show inputs instance variables specific to the current entity. Moving the mouse pointer over them will pop up a tip text describing them in detail.

=Entity EditMode=

Entities are vital components for a map, be it decoration or be it gameplay wise. Creation of Static Objects and Entities are very much alike, and so are creation tools for both.

The only point that differs in the Entity creation window is the Create on surface feature, that will help creating stuff on already created surfaces. The buttons next to this option indicate what kind of geometry objects will be considered by the tool (St: Static Objects, Pr: Primitives, En: Entities). The tool will try to position and align the object according to the orientation of the surface it is pointing to.

More on entities [here](https://wiki.frictionalgames.com/page/HPL2/Entities).

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Working with Entities](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Working_with_Entities)
- Revision: `7098`
- Source update: `2026-07-30T09:59:41Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

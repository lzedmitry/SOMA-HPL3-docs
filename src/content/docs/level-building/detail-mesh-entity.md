---
title: Detail Mesh Entity
description: "= DetailMeshEntities ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Detail_Mesh_Entity"
sourceRevision: 7102
sourceUpdated: "2026-07-30T10:00:43Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= DetailMeshEntities =

Detail mesh entities are useful for adding details to the geometry of a level without much impact on the performance.

## General Parameters
- **Name**: Name for the entity (non editable)
- **Position**: 3D Vector storing the position in world.
- **Rotation**: 3D Vector storing the rotation.
- **Radius**: float storing the value for the uniform scale.
- **Mesh**: file name for the entity.

## Specific Parameters
- **Diffuse color mul**: color to tint the object with.

= DetailMeshEntity EditMode =

> **Figure (original Wiki file, not inlined):** [detailmeshentity_mode.png](https://wiki.frictionalgames.com/page/File:detailmeshentity_mode.png)

This mode is used to create detail mesh entities. These are useful for adding details to a level without much impact on the performance.

** **Main category''': this ComboBox is used to select the current set of objects. Sets should map to directories under the static_objects directory in redist.

** **Subcategory''': this ComboBox will show all subsets inside the set picked previously. 

** **Object list''': all objects under the selected subcategory. Clicking on an entry will select a static object file to be used in following placements.

** **Thumbnail''': shows a little picture so you can see how the object looks like.
** **Create on surface''': when this is on, you are able to create objects on the surface of other objects, such as static objects, entities, primitives or terrain.

** **Scale settings''': this sets the scale for the object on creation. Can be set to a fixed or a random value, the latter defined by a range given by both scale inputs, min and max.

** **Rotation settings''': this sets the rotation for the object on creation. Can be set to a fixed or a random value, the latter defined by a range given by both rotate inputs, min and max.

** **Color settings''': this will define a color range from which a color will be picked for every new placed object.

More on DetailMeshEntities [here](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:DetailMeshEntities).

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Detail Mesh Entity](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Detail_Mesh_Entity)
- Revision: `7102`
- Source update: `2026-07-30T10:00:43Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

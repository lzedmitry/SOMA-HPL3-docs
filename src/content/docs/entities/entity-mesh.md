---
title: Entity Mesh
description: "= SubMeshes = Whenever a Mesh is imported into the ModelEditor, it will spawn one or several submeshes. These can be attached to bodies."
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Entities/Entity_Mesh"
sourceRevision: 7135
sourceUpdated: "2026-07-30T21:54:57Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
= SubMeshes =
Whenever a Mesh is imported into the ModelEditor, it will spawn one or several submeshes. These can be attached to bodies.

General Parameters:
- **Name**: Name of the shape.
- **Position**: Position of the shape in the world. If the mesh has a skeleton, no transformations can be applied.
- **Rotation**: 3D Vector storing the shape rotation. If the mesh has a skeleton, no transformations can be applied.
- **Scale**: 3D Vector storing the scale of the shape. If the mesh has a skeleton, no transformations can be applied.

= SubMesh Reassign Dialog =

> **Figure (original Wiki file, not inlined):** [model_editor_submesh_reassign.png](https://wiki.frictionalgames.com/page/File:model_editor_submesh_reassign.png)

This window allows the user to keep existing submesh data in the event of importing a new mesh or updating of the current one.

On the left, a list with the new submeshes will be displayed, as well as a selector for pairing with a previous submesh for each. The "Use new data" item will ignore any present parameters.

On the right, submeshes that are currently unassigned will be listed.

The Best Match button will try to find the best pairing for each submesh. At the time of writing, only triangle count will be taken into consideration.

When done, pressing the OK button will close the dialog and use the chosen parameters in the new mesh.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Entities/Entity Mesh](https://wiki.frictionalgames.com/page/HPL3/Entities/Entity_Mesh)
- Revision: `7135`
- Source update: `2026-07-30T21:54:57Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

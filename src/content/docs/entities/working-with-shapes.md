---
title: Working with Shapes
description: "= Shapes ="
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Entities/Working_with_Shapes"
sourceRevision: 7141
sourceUpdated: "2026-07-30T21:59:19Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
= Shapes =

General Parameters:

** **Name''': Name of the shape.
** **Position''': Position of the shape in the world.
** **Rotation''': 3D Vector storing the shape rotation.
** **Scale''': 3D Vector storing the scale of the shape.
Shape Specific:

** **Create body''': will create a body out of the shape. Also works when multiple shapes are selected, thus creating a multishape body.
** **Detach from body''': the shape will be removed from the body it is part of.
Best Practices:

''' Keep the Scale in all axis larger than 0.04 to make the collisions stable

= Shape EditMode =

This EditMode is used to create Shapes that will help in physics body creation. At the moment you can create four types of shapes:

- Box
- Cylinder
- Sphere
- Capsule

## Source & attribution

- Original Frictional Wiki page: [HPL3/Entities/Working with Shapes](https://wiki.frictionalgames.com/page/HPL3/Entities/Working_with_Shapes)
- Revision: `7141`
- Source update: `2026-07-30T21:59:19Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

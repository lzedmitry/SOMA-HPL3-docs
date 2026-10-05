---
title: Lens Flares
description: "= LensFlares ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Lens_Flares"
sourceRevision: 7088
sourceUpdated: "2026-07-30T09:53:19Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= LensFlares =

General Parameters:
- **Name**: Name for the lens flare object.
- **Position**: 3D Vector storing the position in world.
- **Rotation**: 3D Vector storting the rotation. Only useful when the billboard type is Axis or FixedAxis.

Specific Parameters:
- For each flare type
** **Material File''': material file for this flare type.
** **Color''': color for this flare type.
** **Size''': size for this flare type.
- Brigthness
- MultiIris count
- MultiIris texture atlas grid (subdiv)
- Use parent mesh for occlusion
- Mul glare with multiiris
- Min/max range
- Inner/outer FOV
- Glare brightness
- Glare StareAt
- Glare range
- Source size
- Size change based on distance (percent)

> **Figure (original Wiki file, not inlined):** [lensflare_mode.png](https://wiki.frictionalgames.com/page/File:lensflare_mode.png)

- Flare type: set to active if the next created lensflare object is to have this flare type.
''' Material: material for showing this type of flare
''' Color: flare color
''' Size: flare size

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Lens Flares](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Lens_Flares)
- Revision: `7088`
- Source update: `2026-07-30T09:53:19Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Terrain Texturing
description: "= Texture mode ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Terrain_Texturing"
sourceRevision: 7082
sourceUpdated: "2026-07-30T09:32:29Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= Texture mode =

This mode is used to edit the texture on the terrain.

> **Figure (original Wiki file, not inlined):** [terrain_mode_texture.png](https://wiki.frictionalgames.com/page/File:terrain_mode_texture.png)
 

As general parameters, one can set up:
- A base material, so it shows on the parts of the terrain that are not painted by blend layers. This one obviates a fade start parameter.
- Specular power
- Default layer resolution.

To be able to paint on the terrain, one (or more) blend layers must be added. A blend layer has variable resolution, which can be set in the edit mode window. It also contains four sublayers, each below the next one. A blend layer will also appear below the one created after it, so keep that in mind. 
Each sub-layer has a terrain material. A terrain material is defined by a material file, a tile amount parameter and a fade start parameter. Additionally it has a vector of 3 real numbers ranging from 0 to 1, indicating how much of each detail texture (these being defined elsewhere) will be blended with the material.

To define detail textures, one must open the Detail tab. There, you can set up to three detail textures, each one with its texture file name and scale. You can also set the fading, that will determine the distance from the camera in which the detail will be visible.

> **Figure (original Wiki file, not inlined):** [terrain_mode_texture_detail.png](https://wiki.frictionalgames.com/page/File:terrain_mode_texture_detail.png)

There are two different brushes in this submode:

Add: will paint the affected area on the target sublayer.
Erase: will remove the affected area from the target sublayer.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Terrain Texturing](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Terrain_Texturing)
- Revision: `7082`
- Source update: `2026-07-30T09:32:29Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

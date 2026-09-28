---
title: Working with Primitives
description: "= Primitives ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Working_with_Primitives"
sourceRevision: 7060
sourceUpdated: "2026-07-30T09:25:22Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= Primitives =

Primitives are basic geometrical objects that can be used to shape up map geometry along with Static Objects

## General Parameters
- **Name**: Name of the primitive.
- **Position**: 3D Vector storing the position in world of the **primitive pivot**.
- **Rotation**: 3D Vector storing the rotation.
- **Scale**: 3D Vector storing the scale of the primitive.

## Primitive Specific
- **Material**: Material file for the primitive.
- **Collides**: If enabled, the primitive will keep entities (player included) from getting through it.
- **Cast Shadows**: If enabled, the primitive will cast shadows when illuminated by a properly set up light.

## Plane Specific
- **Tile amount**: amount of repetition of the texture along the axes. The less, the bigger the texture pattern will look.
- **Tile offset**: offset on the texture coordinates.
- **Texture angle**: rotation of the texture applied on the plane.
- **Align To World Coords**: if enabled, texture coordinates will be set according to world coordinates. Useful to get seamless floors/ceilings made out of several planes.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Working with Primitives](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Working_with_Primitives)
- Revision: `7060`
- Source update: `2026-07-30T09:25:22Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Exposure Areas
description: "= Exposure Areas ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Exposure_Areas"
sourceRevision: 7093
sourceUpdated: "2026-07-30T09:56:28Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= Exposure Areas =

An area that changes the tone mapping parameters when entered. Used to simulate automatic correction of exposure that occurs when eyes get used to bright/dim lit environments.

## General Parameters
- **Name**: Name for the billboard. Should be unique for all objects in map.
- **Position**: 3D Vector storing the position in world.
- **Rotation**: 3D Vector storing the rotation.
- **Size**: 3D Vector storing the size of the area box.

## Specific Parameters
- **Exposure**: The total light that is allowed through the camera, increasing this value makes the image brighter. In the range of -10 to +10.
- **WhitePoint**: A real value that sets which value that should be considered the brightest.
- **Transition time**: The time it takes for the new exposure to apply.

= ExposureArea EditMode =

This creates ExposureArea objects, which are areas that change the tone mapping parameters when entered. Used to simulate automatic correction of exposure that occurs when eyes get used to bright/dim lit environments. The edit mode window can set what will be used by every new exposure area.

> **Figure (original Wiki file, not inlined):** [exposurearea_mode.png](https://wiki.frictionalgames.com/page/File:exposurearea_mode.png)

More on ExposureAreas [here](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:exposure_areas)

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Exposure Areas](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Exposure_Areas)
- Revision: `7093`
- Source update: `2026-07-30T09:56:28Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

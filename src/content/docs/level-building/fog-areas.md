---
title: Fog Areas
description: "= FogAreas ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Fog_Areas"
sourceRevision: 7092
sourceUpdated: "2026-07-30T09:56:11Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= FogAreas =

FogAreas are bounding boxes that apply a fog effect inside their limits

## General Parameters
- **Name**: Name of the FogArea
- **Position**: 3D Vector storing the position in the world of the FogArea center.
- **Rotation**: 3D Vector storing the rotation of the FogArea box.
- **Size**: 3D Vector storing the size of the FogArea box.

## Specific Parameters
- **Color**: color of the fog.
- **Start**:
- **End**:
- **FalloffExp**:
- **Show backside when inside**: if set, the fog effect will not affect what lies beyond the area when seen from inside it. 
- **Show backside when outside**: if set, the fog effect will not affect what lies beyond the area when seen from outside it.

=FogArea EditMode=

FogAreas are bounding boxes that apply a fog effect inside their limits.

The creation window consists only of an input to select the fog color the area will be created with.

To create an area, just click anywhere on the grid, and a 1x1x1 FogArea should appear.

More on FogAreas [here](https://wiki.frictionalgames.com/page/HPL2/Fog_Areas).

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Fog Areas](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Fog_Areas)
- Revision: `7092`
- Source update: `2026-07-30T09:56:11Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

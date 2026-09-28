---
title: Undergrowth
description: "= Undergrowth mode ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Undergrowth"
sourceRevision: 7081
sourceUpdated: "2026-07-30T09:32:12Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= Undergrowth mode =

This mode is used to give further detail to the terrain in the form of undergrowth. With this mode you will be able to create undergrowth materials and place undergrowth areas.

> **Figure (original Wiki file, not inlined):** [terrain_mode_undergrowth.png](https://wiki.frictionalgames.com/page/File:terrain_mode_undergrowth.png)

**Undergrowth Fading parameters**: will define the range where the undergrowth will be visible.

**Undergrowth material editor button**: pressing this button will open the Undegrowth material editor window. In it the user will find the needed parameters to set up a proper undergrowth material, to be used later by undergrowth areas.

The following parameters control several aspects of the creation of undergrowth areas:
- **Material**: the undergrowth material that will be used by the next undergrowth area that will be created.
- **Blend type**: this setting will determine if the next created area will either add or substract undergrowth.
- **Area type**: use this setting to select the type of the next created area out of the two available types:
** **Circle''': To place a circle, just click and hold the left mouse button on the desired spot on the terrain to define the center, then drag over the terrain to define the radius of your circle area. The creation will be done as soon as you release the left mouse button.
** **Polygon''': polygon areas are created on the terrain by placing vertices. To place a vertex, just click and release anywhere on the terrain. Polygons must be convex, so further vertex placement will be constrained to the validity of the resulting polygon. To remove the last placed vertex, click the right mouse button. To finish creating a polygon, double click or click on the first vertex.

## Undergrowth Material editor
> **Figure (original Wiki file, not inlined):** [terrain_mode_undergrowth_material.png](https://wiki.frictionalgames.com/page/File:terrain_mode_undergrowth_material.png)

### Main
- **Base Mesh**: mesh that will be used as single plant to place. Should be 1x1x1 sized.
- **Max Density**: the higher the number, the more plants will be created per square unit.
- **Align to slope amount**:

### Texture
- **Diffuse**: diffuse texture that will be mapped on the plant mesh.
- '''Transparency: texture used for transparency (?)
- '''Subdivisions: these values define how many different sections instead of the whole texture are to be randomly used.
- **Min/Max Color**: the color for each plant will be picked inside this range.

### Size
- **Base Size**: base size for every plant.
- **Min/Max Mul**: a random multiplier for the base size on each plant will be picked from the range defined by these inputs.

### Wind
- **Wind active**: toggles wind blowing effect for the material.
- The rest of the inputs control the sway effect for the plants.
** **Wind frequency''':
** **Wind amplitude''': the higher this value gets, the wider the sway movement will be.
** **Wind speed''':
** **Wind octave muls''':

### ForceField
- These inputs control the sway effect induced on the plants by a present ForceField.
** **Max force''': sets the maximum force that will be applied by an affecting ForceField.
** **Force mul''': force applied will be multiplied by this factor.
** **Frequency mul''': frequency for the affecting ForceField will be multiplied by this factor.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Undergrowth](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Undergrowth)
- Revision: `7081`
- Source update: `2026-07-30T09:32:12Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

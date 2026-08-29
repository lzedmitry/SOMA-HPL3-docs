---
title: Level Editor Toolbar
description: Here you will be able to switch between the different EditModes available in this editor. An EditMode describes the state the editor is going to work in when selected. These five EditModes can be found in both this and t
category: level-editor
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Level_Editor_Toolbar"
sourceRevision: 5218
sourceUpdated: "2020-08-27T16:15:29Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - level-editor
---
## EditMode selection bar
Here you will be able to switch between the different EditModes available in this editor. An EditMode describes the state the editor is going to work in when selected. These five EditModes can be found in both this and the Model Editor.

''' [Select EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:common:select_editmode): this mode is used to select and edit objects.
''' [Light EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:common:light_editmode): with this mode you will be able to place lights around.
''' [Billboard EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:common:billboard_editmode): use this to create Billboards. Light halos, light shafts, and some other
''' [Particle System EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:common:particlesystem_editmode): one can add Particle systems to the map with this mode.
''' [Sound EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:common:sound_editmode): used to place sound entities in the map.
''' [LensFlare EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:common:lensflare_editmode): used to create objects that will generate a lensflare effect when looked at.

The following EditModes are exclusive to the Level Editor

''' [StaticObject EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:staticobject_editmode): this, and the Primitive EditMode, are the actual building tools. StaticObjects (aka level pieces) are placed using this.
''' [Entity EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:entity_editmode): objects that are interactive, such as doors, boxes and NPCs are created here.
''' [Area EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:area_editmode): Areas are places that can be used for several ends, like linking to scripts, setting up where the player starts the map, and so on.
''' [Primitive EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:primitive_editmode): creates static geometry to be part of the map. Only Planes are currently supported.
''' [Decal EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:decal_editmode): give detail to objects by placing decals on them.
''' [FogArea EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:fogarea_editmode): similar to the Area EditMode, but will place volumes containing a fog effect.
''' [Combine EditMode](https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:Combine_editmode): useful for optimizing, creates groups of static geometry that will be loaded by the engine as a whole.
''' [LightMask EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:lightmask_editmode): creates objects that will keep light from illuminating the space outside them.
''' [ExposureArea EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:exposurearea_editmode): creates areas that will modify the camera exposure values when inside them.
''' [Combo EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:combo_editmode): used to place combo objects (compound objects saved as combos)
''' [Terrain EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:terrain_editmode): used to create and set up a terrain.
''' [DetailMeshEntity EditMode](https://wiki.frictionalgames.com/page/hpl3:tools:maineditors:level_editor:detailmeshentity_editmode): places mesh objects that can be drawn really fast, thus can be used for adding detail to the scene.

## Lower Toolbar
You can find some useful controls in this bar located at all times at the lower part of the screen.

> **Figure (original Wiki file, not inlined):** [leveleditor_lowertoolbar.png](https://wiki.frictionalgames.com/page/File:leveleditor_lowertoolbar.png)

  1. Grid Controls:
*** **Grid Plane''': cycles through the available grid planes (XZ, XY, YZ).
*** **Toggle Snap'''    (magnet button): enables/disables snapping for translation (over grid), rotation and scale.
*** **Grid Height''': height of the plane, measured on the plane normal.
*** **Snap Separation''': separation of snapping points.
  1. **Enlarge Viewport button**: will toggle enlargement of the focused viewport.
  1. Misc controls:
*** **A''': toggles global ambient lighting
*** **P''': togles global point light
*** **LT''': toggles Lock to grid for tracking in focused viewport
*** **F''': focus on currently selected object(s)
*** **I''': toggles displaying of icons.
  1. Clip Plane controls
*** **Selected clip plane''': used to select a clip plane among the available ones.
*** **Add**   /**Remove clip plane'''    (+/- buttons): adds a new clip plane / removes the selected one.
*** **Actual Plane''': cycles through the available planes (XZ, XY, YZ).
*** **Plane height''': height of the plane, measured on the plane normal.
*** **Pos**   /**Neg Button''': sets the culling side of the plane.
*** **Active''': sets whether the plane should cull objects.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Level Design/Level Editor Toolbar](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Level_Editor_Toolbar)
- Revision: `5218`
- Source update: `2020-08-27T16:15:29Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

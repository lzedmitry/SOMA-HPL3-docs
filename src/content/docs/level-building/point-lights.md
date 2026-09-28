---
title: Point Lights
description: "A point light is an omnidirectional light source. It illuminates surfaces in every direction from a single position, up to a spherical boundary defined by its radius. This page describes point lights in the SOMA editors."
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Point_Lights"
sourceRevision: 7052
sourceUpdated: "2026-07-30T08:50:34Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
A **point light** is an omnidirectional light source. It illuminates surfaces in every direction from a single position, up to a spherical boundary defined by its radius. This page describes point lights in the SOMA editors.

Point lights are useful for lamps, bulbs, candles, small illuminated controls, and soft local fill. They are available through the **Light** EditMode in both the [Level Editor](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Level_Editor:Main) and the [Model Editor](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Model_Editor:Main).

:::note[Note]
A point light only supplies the light. The visible source normally comes from a lamp entity, an emissive material, a [billboard](/level-building/billboards/), or a particle system.
:::

## Creating a point light
1. Select the **Light** EditMode from the editor sidebar.
1. Select **Point** as the light type.
1. Create the light in a viewport:
  - Click and release to create a light with a radius of one unit.
  - Click, drag, and release to set the initial radius while creating the light.
1. Switch to the **Select** EditMode and move the light to the intended source.
1. Adjust its radius, color, brightness, and falloff in the properties panel.

The wireframe sphere shown by the editor is the light's area of influence. Objects outside that sphere are not illuminated by it.

When creating a light in an orthographic viewport, its initial position is placed on that viewport's working plane. Check its position in at least one other viewport afterward.

## Main properties
The following properties are exposed for point lights by the SOMA editors.

| Property | Description |
| --- | --- |
| **Name** | The object's name. Give a light a clear, unique name if scripts need to control it. |
| **Position** | The center of the light's sphere. Place it close to the apparent light source, while keeping it out of solid geometry. |
| **Rotation** | Does not change the direction of ordinary point-light illumination. It controls the orientation of an assigned cubemap gobo. |
| **Radius** | The maximum distance reached by the light. This is also the radius of the sphere displayed in the editor. |
| **Diffuse Color** | The color emitted by the light. |
| **Brightness** | Multiplies the light's intensity. Radius and brightness solve different problems: radius controls reach, while brightness controls intensity. |
| **Falloff Power** | Shapes how the light attenuates between its center and outer radius. Higher values concentrate more of the light near its source; lower values produce a broader transition. |
| **Gobo** | An optional cubemap texture that modulates the light in different directions. |
| **Gobo Type** | Selects which lighting component the gobo modulates. |
| **Gobo Animation Mode** | Controls playback when the assigned gobo is animated. |
| **Gobo Animation Frame Time** | Sets the duration of each animation frame. |
| **Gobo Animation Start Time** | Offsets the animation's starting time, which can keep several identical animated lights from moving in perfect synchronization. |
| **Affected By SSAO** | Allows the rendered light to be affected by screen-space ambient occlusion. Compare the result in-game, since SSAO depends on the active graphics settings. |
| **Culled By Distance** | Allows the engine to stop rendering the light at sufficient distance. This should normally remain enabled. |
| **Culled By Fog** | Allows sufficiently dense fog to cull the light. |

:::note[Note]
Point lights do not have shadow settings in the SOMA editors and do not cast shadows. Shadow controls belong to [spot lights](/level-building/spot-lights/).
:::

A point light can also be connected to a [LightMask](/level-building/light-masks/). Connections are managed through the LightMask's **Connect lights** control rather than through shadow or occlusion settings on the point light.

## Recommended setup workflow
A reliable way to tune a point light is:

1. Place the visible source first, such as a lamp model and billboard.
1. Put the point light at the source, or slightly in front of its emitting surface.
1. Reduce the radius until the sphere covers only the intended space.
1. Set the color from the visible source.
1. Adjust brightness while viewing the scene from normal player positions.
1. Tune falloff only after the radius and brightness are close to final.
1. Test the result in-game with the intended exposure, post-effects, and graphics settings.

Start with the smallest radius that achieves the desired result. Increasing brightness to compensate for a poorly chosen radius often creates overexposed surfaces near the source, while increasing radius to brighten a distant surface makes the light affect unrelated geometry.

### Practical layering
A convincing fixture often uses several components:

- an emissive material to make the bulb or screen appear self-lit;
- a billboard for visible glow;
- a small point light for nearby illumination; and
- a spot light if the fixture casts a directed beam or needs shadows.

The components do not have to share the same size or intensity. A billboard describes how the source looks to the camera, whereas a point light describes how it affects nearby surfaces.

## Preventing light leaking
Point lights do not have a direction and do not cast shadows. A wall inside the light's sphere therefore does not automatically prevent surfaces on the other side from being illuminated.

To avoid leaking:

- keep the radius inside the room or region that should be lit;
- move the light away from thin walls, floors, and ceilings;
- use several smaller lights instead of one very large light;
- connect the light to a [LightMask](/level-building/light-masks/) when its influence must be confined to a box; or
- replace or supplement it with a shadow-casting spot light where physical occlusion is important.

:::tip[Tip]
Inspect the radius sphere in top, front, and side view. A light that looks contained in one viewport may cross a wall or floor in another.
:::

## Gobos
A gobo multiplies the light with a texture pattern. Point lights require a **cubemap** gobo because they emit in every direction. A normal two-dimensional spot-light gobo is not sufficient.

Rotation normally has no visible effect on an untextured point light. Once a cubemap gobo is assigned, rotating the light rotates the projected pattern around the source.

Gobos are useful for irregular illumination, moving machinery effects, or breaking up a perfectly uniform sphere. They should not be used as a substitute for containing a light; use an appropriate radius or LightMask for that.

## Flicker
Point lights can alternate between an on state and an off state without a script. Enable **Flicker Active** to expose the flicker settings.

| Property | Description |
| --- | --- |
| **On Min Length** / **On Max Length** | Random range, in seconds, for how long the light remains in its normal state. |
| **Off Min Length** / **Off Max Length** | Random range, in seconds, for how long the light remains in its off state. |
| **Off Color** | Color used during the off state. |
| **Off Radius** | Radius used during the off state. Set this to zero for a fully extinguished light, or retain a small radius for an unstable dim state. |
| **On Sound** / **Off Sound** | Optional sounds played when the corresponding transition occurs. |
| **On Particle System** / **Off Particle System** | Optional particle systems created when the corresponding transition occurs. |
| **Flicker Fade** | Blends between the two states instead of switching instantly. |
| **On Fade Min Length** / **On Fade Max Length** | Random fade-time range for entering the on state. |
| **Off Fade Min Length** / **Off Fade Max Length** | Random fade-time range for entering the off state. |

For every timing pair, the minimum value should be less than or equal to the maximum value. Very short ranges produce electrical flutter; longer ranges produce a failing lamp or intermittent power effect.

Use transition sounds and particle systems sparingly. Fast flicker settings can trigger them repeatedly in a short period.

## Level Editor and Model Editor
The Light EditMode and the core point-light properties are shared by both editors, but the saved context is different:

- In the **Level Editor**, the point light is stored directly in the map and uses map-space coordinates.
- In the **Model Editor**, the point light is part of the entity being authored. Its transform is relative to that entity and follows each placed instance.

Embedded lights are useful when illumination is an inherent part of an entity, such as a portable lamp or a machine with status lights. Map lights are preferable when the lighting must be tuned for one specific room or composition.

After adding an embedded point light in the Model Editor, place the entity in a test map and verify it in-game. The surrounding geometry, exposure settings, entity scale, and distance culling can make it look different from the isolated Model Editor preview.

## Performance
The renderer must process geometry affected by each visible light. The main cost of a point light therefore grows with the size of its sphere and the number of other light volumes overlapping it.

For efficient lighting:

- use the smallest practical radius;
- avoid stacks of large point lights covering the same room;
- keep distance culling enabled unless the light has a strong reason to remain visible;
- use a box light, SH probes, or other ambient-lighting tools for broad base illumination; and
- test performance in-game at the target quality settings.

Brightness by itself does not enlarge the affected volume. Reducing radius and then retuning brightness is often more useful than simply lowering brightness on an oversized light.

## Scripting
Scripts can identify lights by name and change properties such as visibility, brightness, radius, color, and flicker state. Use a unique, descriptive name when a particular light will be controlled at runtime.

For example, SOMA's light helper functions include `Light_FadeTo`, `Light_SetBrightness`, `Light_SetFlickerActive`, and `Light_SetVisible`. See [Scripting API: Light](/api/categories/light/).

## Troubleshooting
| Problem | Likely cause and solution |
| --- | --- |
| The light is not visible. | Check that the light radius and brightness are above zero, that the object is enabled, and that **Lights Active** is enabled in the editor preferences. Also check distance culling and any connected LightMask. |
| The bulb glows, but nearby geometry remains dark. | An emissive material or billboard does not illuminate the scene. Add or enable a light object. |
| Surfaces in the next room are illuminated. | The radius crosses the separating wall. Reduce or reposition the light, split it into smaller lights, or connect it to a LightMask. |
| Rotation appears to do nothing. | This is expected for an ordinary point light. Rotation is visually relevant when a cubemap gobo is assigned. |
| Flicker never changes the light. | Ensure **Flicker Active** is enabled and the on/off duration ranges contain useful non-zero values. |
| The light looks different in-game. | Verify the map's exposure and post-effects, the active graphics settings, SSAO, nearby probes and ambient lights, and the light's distance-culling behavior. |

## See also
- [Light EditMode](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Common:Light_EditMode)
- [Lights](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Common:Lights)
- [Spot Lights](/level-building/spot-lights/)
- [Light Masks](/level-building/light-masks/)
- [Global Spot Light](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Global_Spot_Light)
- [SH Probes](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/SH_Probes)
- [Billboards](/level-building/billboards/)

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Level Design/Point Lights](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Point_Lights)
- Revision: `7052`
- Source update: `2026-07-30T08:50:34Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

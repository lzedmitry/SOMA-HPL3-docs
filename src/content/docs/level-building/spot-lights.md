---
title: Spot Lights
description: "A spot light emits light through a directional cone or pyramid-shaped frustum. Unlike a point light, it illuminates only the space in front of it. Spot lights are also the local light type that can cast shadows in SOMA."
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Spot_Lights"
sourceRevision: 7053
sourceUpdated: "2026-07-30T08:58:16Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
A **spot light** emits light through a directional cone or pyramid-shaped frustum. Unlike a [point light](/level-building/point-lights/), it illuminates only the space in front of it. Spot lights are also the local light type that can cast shadows in SOMA.

Spot lights are useful for ceiling fixtures, flashlights, windows, searchlights, projected patterns, and any source that needs a controlled direction. They are available through the **Light** EditMode in both the [Level Editor](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Level_Editor:Main) and the [Model Editor](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Model_Editor:Main).

:::note[Note]
A spot light does not create a visible lamp or beam by itself. Use an entity or emissive material for the source, and a billboard, fog, or particle effect when the beam must be visible in the air.
:::

## Creating a spot light
1. Select the **Light** EditMode from the editor sidebar.
1. Select **Spot** as the light type.
1. Create the light using either method:
  - Click once on the grid to create a spot light at that position with its default orientation.
  - Click and drag on the grid to define the projected direction, then release and click again to define its angle away from the grid plane.
1. Switch to the **Select** EditMode.
1. Position and rotate the light so its frustum points away from the visible source.
1. Adjust its radius, field of view, aspect, near clip plane, color, brightness, and falloff.

The editor draws the light's frustum in the viewports. Check it from multiple orthographic views as well as the perspective viewport; a cone that looks correct from one direction can still cross unintended geometry on another axis.

## Shape and attenuation
These properties define the spotlight's volume and how its intensity changes inside that volume.

| Property | Description |
| --- | --- |
| **Position** | The origin of the spotlight frustum. |
| **Rotation** | Determines the direction and roll of the light. Roll is especially visible with a non-square gobo or a non-default aspect. |
| **Radius** | The maximum distance reached by the light, measured forward from its position. |
| **FOV** | The angular width of the spotlight. A small field of view produces a narrow beam; a large value produces a broad cone. The value stored in `.hpm_Light` is in radians. |
| **Aspect** | The width-to-height ratio of the projected frustum. `1` produces a square projection; values above or below `1` stretch it along one axis. |
| **Near Clip Plane** | Distance from the light position to the start of its projection frustum. Geometry closer than this plane is excluded from the projected volume. |
| **Falloff Power** | Controls attenuation over distance from the source to the radius. Higher values concentrate more light near the source; lower values retain more intensity farther along the beam. |
| **Spot Falloff Power** | Controls angular attenuation from the center of the beam toward its edges. Higher values concentrate the light more strongly around the center axis; lower values keep more intensity across the width of the cone. |

**Falloff Power** and **Spot Falloff Power** are independent. The first changes intensity along the length of the light; the second changes intensity across its width.

:::tip[Tip]
Set the radius and FOV before tuning brightness. They determine which geometry the light affects and therefore have both visual and performance consequences.
:::

## Light and gobo properties
| Property | Description |
| --- | --- |
| **Name** | The object's name. Use a clear, unique name when scripts or other editor objects need to identify the light. |
| **Diffuse Color** | The color emitted by the light. |
| **Brightness** | Multiplies the light's intensity without changing the size of its frustum. |
| **Gobo** | An optional two-dimensional texture projected through the spotlight. |
| **Gobo Type** | Selects whether the gobo modulates **Diffuse**, **Specular**, or **DiffuseSpecular** lighting. |
| **Gobo Animation Mode** | Controls playback when the assigned gobo texture is animated. |
| **Gobo Animation Frame Time** | Sets the duration of each animation frame. |
| **Gobo Animation Start Time** | Offsets the animation's starting point. Different offsets can keep repeated animated lights from moving in synchronization. |
| **Affected By SSAO** | Allows the rendered light to be affected by screen-space ambient occlusion. |
| **Culled By Distance** | Allows the engine to stop rendering the light at sufficient distance. |
| **Culled By Fog** | Allows sufficiently dense fog to cull the light. |

A gobo is often cheaper than using shadows to create a fixed pattern. Gobos work well for window frames, grilles, machinery, broken illumination, or an intentionally shaped beam.

The gobo's orientation follows the spotlight's rotation, and its projection follows the FOV and aspect. If a pattern appears stretched or rotated incorrectly, check those three settings before editing the texture.

## Shadows
Spot lights can render shadow maps for geometry inside their frustum.

| Property | Description |
| --- | --- |
| **Cast Shadows** | Enables shadow rendering for the light. |
| **Shadow Resolution** | Selects the shadow-map resolution. Higher resolution gives more detail but costs more rendering time and memory. |
| **Shadows Affect Static** | Includes static geometry in the light's shadow map. |
| **Shadows Affect Dynamic** | Includes dynamic entities in the shadow map. When enabled, the shadow map may need to be updated as dynamic objects move. |
| **Shadow Fade Range** | Sets the camera-distance range at which the light's shadows fade. Stock SOMA maps commonly use `-1` when no distance fade is wanted. |
| **Shadow Blur Amount** | Controls filtering of the shadow-map result. Increasing it softens the shadow but can reduce visible detail. |

Shadow-casting spot lights are among the more expensive elements in an indoor SOMA level. In particular, enabling **Shadows Affect Dynamic** prevents the shadow result from remaining completely static.

Use these settings deliberately:

- Disable **Cast Shadows** when a gobo or the scene composition already provides the necessary contrast.
- Disable **Shadows Affect Dynamic** when moving entities do not need to cast through this light.
- Disable **Shadows Affect Static** only when static geometry genuinely does not need to occlude it.
- Use the lowest shadow resolution that remains acceptable from normal player positions.
- Keep the radius and FOV tightly fitted to the intended region.
- Avoid several large shadow-casting frustums covering the same room.

Also disable shadow casting on individual meshes that cannot produce a useful visible shadow, such as a floor with nothing beneath it or small objects pressed against an opaque wall.

## Near clip plane
The near clip plane deserves separate attention when shadows or gobos are used. It is the front boundary of the spotlight's projection frustum.

A value that is too large can cut illumination or shadows away near the fixture. A very small value can waste shadow precision on space immediately around the source. Position the light just outside the lamp housing, then set the near clip plane so that the frustum begins beyond geometry that should not participate.

:::caution[Caution]
Do not use the near clip plane as the main way to contain a light. Use its position, rotation, radius, FOV, aspect, shadows, or a LightMask to define the intended volume.
:::

## LightMasks and leaking
A spotlight can be connected to a [LightMask](/level-building/light-masks/), which confines it to the mask's box volume. Connections are made with the LightMask's **Connect lights** control.

Use a LightMask when the spotlight frustum crosses into another room or floor even after its radius and FOV have been reasonably tightened. A mask is particularly useful for wide spot lights used as room lighting.

Before adding a mask:

- ensure the light points in the correct direction;
- reduce its radius to the required reach;
- reduce its FOV to the required spread;
- check its aspect and roll; and
- inspect the frustum from several viewports.

Shadows and LightMasks solve different problems. Shadows provide occlusion from shadow-casting geometry, while a LightMask imposes a hard spatial boundary on the connected light.

## Flicker
Spot lights use the common light flicker system. Enable **Flicker Active** to alternate between normal and off states.

| Property | Description |
| --- | --- |
| **On Min Length** / **On Max Length** | Random range, in seconds, for the duration of the normal state. |
| **Off Min Length** / **Off Max Length** | Random range, in seconds, for the duration of the off state. |
| **Off Color** | Color used during the off state. |
| **Off Radius** | Radius used during the off state. |
| **On Sound** / **Off Sound** | Optional sounds played on the corresponding transition. |
| **On Particle System** / **Off Particle System** | Optional particle systems created on the corresponding transition. |
| **Flicker Fade** | Blends between the on and off states rather than switching instantly. |
| **On Fade Min Length** / **On Fade Max Length** | Random duration range for fading into the on state. |
| **Off Fade Min Length** / **Off Fade Max Length** | Random duration range for fading into the off state. |

For each timing pair, the minimum must be less than or equal to the maximum. Avoid transition sounds or particle systems on extremely rapid flicker unless the repeated triggering is intentional.

## Level Editor and Model Editor
The core spotlight properties are shared by both editors:

- In the **Level Editor**, the light is stored in the map and uses map-space coordinates.
- In the **Model Editor**, the light becomes part of the entity and follows every placed instance.

Use an embedded spotlight when its direction and behavior inherently belong to an entity, such as a portable lamp or machine indicator. Use a map spotlight when its framing, mask, shadow cost, or brightness must be tuned for one particular space.

Always place an entity with an embedded spotlight in a test map. The isolated Model Editor preview does not reproduce the final map's exposure, fog, SSAO, LightMasks, surrounding geometry, and overlapping lights.

## Performance workflow
When optimizing a spotlight, work in this order:

1. Decide whether it needs shadows at all.
1. Tighten the radius.
1. Tighten the FOV and aspect.
1. Disable dynamic shadows if moving objects do not need to cast.
1. Select an appropriate shadow resolution.
1. Use a LightMask if the remaining frustum crosses room boundaries.
1. Test the result in-game from normal player positions.

Large radius and FOV values increase the amount of geometry inside both the light volume and its shadow frustum. A high-resolution shadow map does not correct an oversized or poorly aimed light.

## Troubleshooting
| Problem | Likely cause and solution |
| --- | --- |
| The light is not visible. | Check its rotation, radius, FOV, brightness, and near clip plane. Also check distance/fog culling, editor light preview, and any connected LightMask. |
| The light points in the wrong direction. | Rotate the light in more than one viewport. A spotlight's roll can also make a rectangular projection appear incorrectly oriented. |
| The projection is too wide or narrow. | Adjust FOV. Use aspect when only one projection axis needs to change. |
| The beam has a bright center and weak edges. | Reduce **Spot Falloff Power** for a more even angular distribution. |
| The beam loses intensity too quickly with distance. | Reduce **Falloff Power**, or reconsider the radius before increasing brightness. |
| Shadows are missing. | Enable **Cast Shadows** and the appropriate static/dynamic options. Check that the occluder and receiving surface are inside the frustum and beyond its near clip plane, and that the occluding object itself casts shadows. |
| Shadows are expensive. | Tighten radius and FOV, disable dynamic shadows where possible, reduce shadow resolution, or replace fixed shadow detail with a gobo. |
| The gobo is stretched. | Check the spotlight aspect and the source texture's proportions. |
| Light or shadows appear in an adjacent room. | Tighten the frustum, improve occluding geometry, or connect the light to a LightMask. |
| The result differs in-game. | Check exposure, fog, SSAO, graphics quality, distance culling, nearby probes and ambient lights, and dynamic objects entering the shadow frustum. |

## See also
- [Light EditMode](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Common:Light_EditMode)
- [Lights](https://wiki.frictionalgames.com/page/Hpl3:Tools:Maineditors:Common:Lights)
- [Point Lights](/level-building/point-lights/)
- [Light Masks](/level-building/light-masks/)
- [Global Spot Light](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Global_Spot_Light)
- [SH Probes](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/SH_Probes)
- [Billboards](/level-building/billboards/)
- [Indoor Level Performance](/level-building/indoor-level-performance/)

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Level Design/Spot Lights](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design/Spot_Lights)
- Revision: `7053`
- Source update: `2026-07-30T08:58:16Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

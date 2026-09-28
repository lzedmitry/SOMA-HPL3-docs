---
title: Level Settings
description: "= Level Settings window = This window holds settings for the level, such as global fog and skybox."
category: level-editor
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Level_Settings"
sourceRevision: 7068
sourceUpdated: "2026-07-30T09:26:05Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - level-editor
---
= Level Settings window =
This window holds settings for the level, such as global fog and skybox.

### Skybox settings
> **Figure (original Wiki file, not inlined):** [window_levelsettings_skybox.png](https://wiki.frictionalgames.com/page/File:window_levelsettings_skybox.png)

- **Active**: will enable or disable the skybox.
- **Color**: if no texture is set, the skybox will use a flat color defined here.
- **Texture**: loads a cubemap texture to be used as skybox.

### Global Fog settings
> **Figure (original Wiki file, not inlined):** [window_levelsettings_fog.png](https://wiki.frictionalgames.com/page/File:window_levelsettings_fog.png)

- **Active**: enables or disables the global fog.
- **Culling**: sets if the fog should cull objects that are behind the 'End' distance.
- **Start**: sets the distance to the camera where the color fading should start.
- **End**: sets the distance to the camera where the color fading should be fully done.
- **Falloff Exp**: sets the attenuation factor that will be used for the fading.
- **Color**: color for the fog.

### Decals
> **Figure (original Wiki file, not inlined):** [window_levelsettings_decals.png](https://wiki.frictionalgames.com/page/File:window_levelsettings_decals.png)

- **Global Max Triangles Per Decal**: this here will set how many triangles decal meshes will have unless individually tweaked.
- **Reset Created Decals**: this will reset all created decals to use the above value.

### Directional light
> **Figure (original Wiki file, not inlined):** [window_levelsettings_directionallight.png](https://wiki.frictionalgames.com/page/File:window_levelsettings_directionallight.png)

- **Active**: will toggle the directional light for the level.
- **Direction**: 3D vector indicating where the light will point at.
** **Get from camera''': copies the direction from the viewport camera.
- **Diffuse**: the diffuse color for the light.
- **Sky color**: objects will reflect shades of this color on their upper side.
- **Ground color**: objects will reflect shades of this color on their lower side.
- **Brightness**: brightness for the light.
- **Cast shadows**: if the light should cast shadows.
- **Shadow map bias mul**: tweak to move the shadow away from the light to remove shadow banding and artifacts.
- **Shadow map slope scale bias mul**: tweak to move triangles even further away from the light if the angle to the light is steep.
- **Shadow caster distance**: sets how far our light source will be when it comes to casting shadows. Increase to remove artifacts caused by shadows. A too high of a number will make shadows start to disappear.

### Env Particles
The inputs in this tab control the parameters for the environment particles in the level. 

> **Figure (original Wiki file, not inlined):** [Window levelsettings envparticles.png](https://wiki.frictionalgames.com/page/File:Window_levelsettings_envparticles.png)

- **Active**: will toggle the environmental particles.
- **Color**: the particles will be tinted with this color.
- **Brightness**: how bright the above color will show.
- Rest of parameters are explained in depth [here](https://wiki.frictionalgames.com/page/hpl3:engine:rendering#Environment_Particles).

### PostEffects
> **Figure (original Wiki file, not inlined):** [Window levelsettings posteffects.png](https://wiki.frictionalgames.com/page/File:Window_levelsettings_posteffects.png)

#### ToneMapping
- **MiddleGrey**: A real value that sets what should be considered the middle grey value.
- **Exposure**: The total light that is allowed through the camera, increasing this value makes the image brighter. In the range of -10 to +10.
- **WhitePoint**: A real value that sets which value that should be considered the brightest.

#### ColorGrading
- **Color Grading texture**: 3D dds texture file defining the color grading map.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Level Settings](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Level_Settings)
- Revision: `7068`
- Source update: `2026-07-30T09:26:05Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

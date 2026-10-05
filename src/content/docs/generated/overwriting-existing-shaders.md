---
title: Overwriting Existing Shaders
description: "Most shaders can be overwritten at runtime by StandAlone and AddOn mods, allowing for them to easily modify shader behavior. Here's an example mod for SOMA in both StandAlone and AddOn configuration that makes a simple e"
category: generated
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Shaders/Overwriting_Existing_Shaders"
sourceRevision: 6841
sourceUpdated: "2024-09-13T22:14:16Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - generated
sidebar:
  hidden: true
---
## Introduction
> **Figure (original Wiki file, not inlined):** [A simple shader mod that gives SOMA a classic, film noir look...](https://wiki.frictionalgames.com/page/File:Greyscale_Demonstration.jpg)
Most shaders can be overwritten at runtime by StandAlone and AddOn mods, allowing for them to easily modify shader behavior. Here's an example mod for SOMA in both [StandAlone](https://mega.nz/file/egE1CYZD#WliKF2KuCEwn2XNmt9idmGqaDv8Nr5pIFtEi2EA6ISs) and [AddOn](https://mega.nz/file/L4dEFBJJ#wAIzKE7fF0pAjpXRmDr1bzvDMTvz5mawVrKp0QvbiB8) configuration that makes a simple edit to the game's `posteffect_tonemapping_frag.hpsl` shader. After loading either version, you can see that the entire game is now in black and white!

Alternatively, vanilla shaders can be directly modified in the `core\shaders\` directory of your game install. This can be useful for more complex shader mods which edit the few shaders that cannot be reliably overwritten by normal StandAlone or AddOn mods, which are currently:

- base_vtx.hpsl
- base_frag.hpsl
- cache_terrain_diffuse_frag.hpsl
- clear_frag.hpsl
- clear_vtx.hpsl
- deferred_base_frag.hpsl
- deferred_base_vtx.hpsl
- deferred_skybox_frag.hpsl
- deferred_terrain_gbuffer_frag.hpsl
- deferred_terrain_tess_cs.hpsl
- deferred_terrain_tess_es.hpsl
- deferred_terrain_vtx.hpsl
- null_frag.hpsl
- null_frag_array.hpsl
- null_frag_array2.hpsl
- null_vtx.hpsl

These likely have special behavior in-engine that changes the way they're loaded when compared to other shaders. More testing will be needed to determine why this is the case. 

## Set Up
Edit your mod's `resources.cfg` file to include the following:

```
<Resources>
    <Directory Path="/core" AddSubDirs="true" />
</Resources>
```

GLSL shaders should be located in your mod's `core\shaders\` directory and HPSL shaders should be in `core\shaders\hpsl`. For existing shaders, your shader MUST have the same name and path as the shader you're trying to overwrite. Most of the shader list is hardcoded within the executable and there is no known way to create new GpuPrograms or delete existing ones without access to the source code. For a simple AddOn that just alters shaders, your file structure will likely look like this:

```
modFolder/
├── core/
│   ├── shaders/
│   │   ├── hpsl/
├── entry.hpc
├── resources.cfg
```

### SOMA
Beyond this, the setup process for SOMA is extremely straightforward and is as simple as placing your shaders in your mod's `core\shaders\` directory, and your changes should be reflected in-game after loading your mod. Keep in mind that not all shader code is compiled on startup and is often conditional depending on what is being rendered in the current map, so some changes will not be immediately apparent! 

### Amnesia: Rebirth and Amnesia: The Bunker
For Amnesia: Rebirth and Amnesia: The Bunker, `LoadShaderCache` MUST be set to false in your mod's user settings configuration file for your mod's custom shaders to be reflected in-game. This will likely lead to slightly degraded performance, but this doesn't seem too noticeable on modern hardware. You will need to overwrite the base game's `default_user_settings.cfg` in the config folder to automatically set `LoadShaderCache` to false (for Rebirth) OR you will need to manually instruct users to set `LoadShaderCache` to false in their .cfg file (for Bunker). 

**NOTE:** Make sure `SaveShaderCache` is set to false! This has much worse performance degradation and worse compatibility than `LoadShaderCache`, as it constantly regenerates the shadercache.xml file in `_shadersource` at runtime. This may be useful for directly editing shaders within your base install, but is unlikely to be useful for StandAlone or AddOn mods.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Shaders/Overwriting Existing Shaders](https://wiki.frictionalgames.com/page/HPL3/Shaders/Overwriting_Existing_Shaders)
- Revision: `6841`
- Source update: `2024-09-13T22:14:16Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

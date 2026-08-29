---
title: Map
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Map"
sourceRevision: 5039
sourceUpdated: "2020-08-24T20:56:14Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `bool` | [`Map_GetBillboardArray`](#map-getbillboardarray)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [array](https://wiki.frictionalgames.com/page/../../array)<[cBillboard@](https://wiki.frictionalgames.com/page/../../cBillboard)> &inout avOutBillboards) | Creates an array of billboards with a given name |
| `bool` | [`Map_GetFogAreaArray`](#map-getfogareaarray)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [array](https://wiki.frictionalgames.com/page/../../array)<[cFogArea@](https://wiki.frictionalgames.com/page/../../cFogArea)> &inout avOutFogAreas) | Creates an array of fog areas with a given name |
| `bool` | [`Map_GetLensFlareArray`](#map-getlensflarearray)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [array](https://wiki.frictionalgames.com/page/../../array)<[cLensFlare@](https://wiki.frictionalgames.com/page/../../cLensFlare)> &inout avOutLensFlares) | Creates an array of lens flares with a given name |
| `bool` | [`Map_GetLightArray`](#map-getlightarray)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [array](https://wiki.frictionalgames.com/page/../../array)<[iLight@](https://wiki.frictionalgames.com/page/../../iLight)> &inout avOutLights) | Creates an array of lights with a given name |
| `bool` | [`Map_GetParticleSystemArray`](#map-getparticlesystemarray)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [array](https://wiki.frictionalgames.com/page/../../array)<[cParticleSystem@](https://wiki.frictionalgames.com/page/../../cParticleSystem)> &inout avOutParticles) | Creates an array of particle systems with a given name |

## Function Detail
    1. `Map_GetBillboardArray`

```angelscript
bool Map_GetBillboardArray(const tString &in asName,
                           cBillboard@ &inout avOutBillboards)
```

Creates an array of billboards with a given name.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of billboards. May contain * as wildcards. |
| `avOutBillboards` | `[cBillboard@](https://wiki.frictionalgames.com/page/../../cBillboard)` | reference to array that will be filled with billboards. |

**Returns:** `bool` — array of billboards found.

    1. `Map_GetFogAreaArray`

```angelscript
bool Map_GetFogAreaArray(const tString &in asName,
                         cFogArea@ &inout avOutFogAreas)
```

Creates an array of fog areas with a given name.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of fog areas. May contain * as wildcards. |
| `avOutFogAreas` | `[cFogArea@](https://wiki.frictionalgames.com/page/../../cFogArea)` | reference to array that will be filled with fog areas. |

**Returns:** `bool` — array of fog areas found.

    1. `Map_GetLensFlareArray`

```angelscript
bool Map_GetLensFlareArray(const tString &in asName,
                           cLensFlare@ &inout avOutLensFlares)
```

Creates an array of lens flares with a given name.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lens flares. May contain * as wildcards. |
| `avOutLensFlares` | `[cLensFlare@](https://wiki.frictionalgames.com/page/../../cLensFlare)` | reference to array that will be filled with lens flares. |

**Returns:** `bool` — array of lens flares found.

    1. `Map_GetLightArray`

```angelscript
bool Map_GetLightArray(const tString &in asName,
                       iLight@ &inout avOutLights)
```

Creates an array of lights with a given name.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lights. May contain * as wildcards. |
| `avOutLights` | `[iLight@](https://wiki.frictionalgames.com/page/../../iLight)` | reference to array that will be filled with lights. |

**Returns:** `bool` — array of lights found.

    1. `Map_GetParticleSystemArray`

```angelscript
bool Map_GetParticleSystemArray(const tString &in asName,
                                cParticleSystem@ &inout avOutParticles)
```

Creates an array of particle systems with a given name.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of particle systems. May contain * as wildcards. |
| `avOutParticles` | `[cParticleSystem@](https://wiki.frictionalgames.com/page/../../cParticleSystem)` | reference to array that will be filled with particle systems. |

**Returns:** `bool`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Map](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Map)
- Revision: `5039`
- Source update: `2020-08-24T20:56:14Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

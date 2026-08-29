---
title: cScene
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cScene"
sourceRevision: 5023
sourceUpdated: "2020-08-24T20:50:52Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: undocumented
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
:::note[SOURCE STATUS: Undocumented]
This API page was auto-generated on the Frictional Wiki and has no written descriptions.
:::

Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `cCamera` | [`cScene_CreateCamera`](#cscene-createcamera)([eCameraMoveMode](https://wiki.frictionalgames.com/page/../../eCameraMoveMode) aMoveMode) | *Undocumented in the original Wiki.* |
| `cViewport` | [`cScene_CreateViewport`](#cscene-createviewport)([cCamera](https://wiki.frictionalgames.com/page/../../cCamera) @apCamera, [cWorld](https://wiki.frictionalgames.com/page/../../cWorld) @apWorld, bool abAddLast) | *Undocumented in the original Wiki.* |
| `cWorld` | [`cScene_CreateWorld`](#cscene-createworld)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `void` | [`cScene_DestroyCamera`](#cscene-destroycamera)([cCamera@](https://wiki.frictionalgames.com/page/../../cCamera) apCam) | *Undocumented in the original Wiki.* |
| `void` | [`cScene_DestroyViewport`](#cscene-destroyviewport)([cViewport@](https://wiki.frictionalgames.com/page/../../cViewport) apViewPort) | *Undocumented in the original Wiki.* |
| `void` | [`cScene_DestroyWorld`](#cscene-destroyworld)([cWorld@](https://wiki.frictionalgames.com/page/../../cWorld) apWorld) | *Undocumented in the original Wiki.* |
| `void` | [`cScene_FadeGradingTexture`](#cscene-fadegradingtexture)([cWorld@](https://wiki.frictionalgames.com/page/../../cWorld) apWorld, [iTexture@](https://wiki.frictionalgames.com/page/../../iTexture) apGrading, float afTime) | *Undocumented in the original Wiki.* |
| `cWorld` | [`cScene_LoadWorld`](#cscene-loadworld)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile, int aFlags) | *Undocumented in the original Wiki.* |
| `void` | [`cScene_Reset`](#cscene-reset)() | *Undocumented in the original Wiki.* |
| `void` | [`cScene_SetCurrentListener`](#cscene-setcurrentlistener)([cViewport@](https://wiki.frictionalgames.com/page/../../cViewport) apViewPort) | *Undocumented in the original Wiki.* |
| `cBeam` | [`cScene_ToBeam`](#cscene-tobeam)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cBillboard` | [`cScene_ToBillboard`](#cscene-tobillboard)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cForceField` | [`cScene_ToForceField`](#cscene-toforcefield)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cLensFlare` | [`cScene_ToLensFlare`](#cscene-tolensflare)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cLightBox` | [`cScene_ToLightBox`](#cscene-tolightbox)([iLight@](https://wiki.frictionalgames.com/page/../../iLight) apLight) | *Undocumented in the original Wiki.* |
| `cLightDirectional` | [`cScene_ToLightDirectional`](#cscene-tolightdirectional)([iLight@](https://wiki.frictionalgames.com/page/../../iLight) apLight) | *Undocumented in the original Wiki.* |
| `cLightPoint` | [`cScene_ToLightPoint`](#cscene-tolightpoint)([iLight@](https://wiki.frictionalgames.com/page/../../iLight) apLight) | *Undocumented in the original Wiki.* |
| `cLightSpot` | [`cScene_ToLightSpot`](#cscene-tolightspot)([iLight@](https://wiki.frictionalgames.com/page/../../iLight) apLight) | *Undocumented in the original Wiki.* |
| `cMeshEntity` | [`cScene_ToMeshEntity`](#cscene-tomeshentity)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `iRopeEntity` | [`cScene_ToRopeEntity`](#cscene-toropeentity)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cRopeEntity3D` | [`cScene_ToRopeEntity3D`](#cscene-toropeentity3d)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cRopeEntityBillboard` | [`cScene_ToRopeEntityBillboard`](#cscene-toropeentitybillboard)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cSoundEntity` | [`cScene_ToSoundEntity`](#cscene-tosoundentity)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `cSubMeshEntity` | [`cScene_ToSubMeshEntity`](#cscene-tosubmeshentity)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `bool` | [`cScene_ViewportExists`](#cscene-viewportexists)([cViewport@](https://wiki.frictionalgames.com/page/../../cViewport) apViewPort) | *Undocumented in the original Wiki.* |
| `void` | [`cScene_WorldExists`](#cscene-worldexists)([cWorld@](https://wiki.frictionalgames.com/page/../../cWorld) apWorld) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cScene_CreateCamera`

```angelscript
cCamera@ cScene_CreateCamera(eCameraMoveMode aMoveMode)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aMoveMode` | `[eCameraMoveMode](https://wiki.frictionalgames.com/page/../../eCameraMoveMode)` | — |

**Returns:** `cCamera@`

    1. `cScene_CreateViewport`

```angelscript
cViewport@ cScene_CreateViewport(cCamera @apCamera,
                                 cWorld @apWorld,
                                 bool abAddLast)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apCamera` | `[cCamera](https://wiki.frictionalgames.com/page/../../cCamera)` | — |
| `@apWorld` | `[cWorld](https://wiki.frictionalgames.com/page/../../cWorld)` | — |
| `abAddLast` | `bool` | — |

**Returns:** `cViewport@`

    1. `cScene_CreateWorld`

```angelscript
cWorld@ cScene_CreateWorld(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cWorld@`

    1. `cScene_DestroyCamera`

```angelscript
void cScene_DestroyCamera(cCamera@ apCam)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apCam` | `[cCamera@](https://wiki.frictionalgames.com/page/../../cCamera)` | — |

**Returns:** `void`

    1. `cScene_DestroyViewport`

```angelscript
void cScene_DestroyViewport(cViewport@ apViewPort)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apViewPort` | `[cViewport@](https://wiki.frictionalgames.com/page/../../cViewport)` | — |

**Returns:** `void`

    1. `cScene_DestroyWorld`

```angelscript
void cScene_DestroyWorld(cWorld@ apWorld)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apWorld` | `[cWorld@](https://wiki.frictionalgames.com/page/../../cWorld)` | — |

**Returns:** `void`

    1. `cScene_FadeGradingTexture`

```angelscript
void cScene_FadeGradingTexture(cWorld@ apWorld,
                               iTexture@ apGrading,
                               float afTime)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apWorld` | `[cWorld@](https://wiki.frictionalgames.com/page/../../cWorld)` | — |
| `apGrading` | `[iTexture@](https://wiki.frictionalgames.com/page/../../iTexture)` | — |
| `afTime` | `float` | — |

**Returns:** `void`

    1. `cScene_LoadWorld`

```angelscript
cWorld@ cScene_LoadWorld(const tString &in asFile,
                         int aFlags)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aFlags` | `int` | — |

**Returns:** `cWorld@`

    1. `cScene_Reset`

```angelscript
void cScene_Reset()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cScene_SetCurrentListener`

```angelscript
void cScene_SetCurrentListener(cViewport@ apViewPort)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apViewPort` | `[cViewport@](https://wiki.frictionalgames.com/page/../../cViewport)` | — |

**Returns:** `void`

    1. `cScene_ToBeam`

```angelscript
cBeam@ cScene_ToBeam(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cBeam@`

    1. `cScene_ToBillboard`

```angelscript
cBillboard@ cScene_ToBillboard(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cBillboard@`

    1. `cScene_ToForceField`

```angelscript
cForceField@ cScene_ToForceField(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cForceField@`

    1. `cScene_ToLensFlare`

```angelscript
cLensFlare@ cScene_ToLensFlare(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cLensFlare@`

    1. `cScene_ToLightBox`

```angelscript
cLightBox@ cScene_ToLightBox(iLight@ apLight)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apLight` | `[iLight@](https://wiki.frictionalgames.com/page/../../iLight)` | — |

**Returns:** `cLightBox@`

    1. `cScene_ToLightDirectional`

```angelscript
cLightDirectional@ cScene_ToLightDirectional(iLight@ apLight)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apLight` | `[iLight@](https://wiki.frictionalgames.com/page/../../iLight)` | — |

**Returns:** `cLightDirectional@`

    1. `cScene_ToLightPoint`

```angelscript
cLightPoint@ cScene_ToLightPoint(iLight@ apLight)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apLight` | `[iLight@](https://wiki.frictionalgames.com/page/../../iLight)` | — |

**Returns:** `cLightPoint@`

    1. `cScene_ToLightSpot`

```angelscript
cLightSpot@ cScene_ToLightSpot(iLight@ apLight)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apLight` | `[iLight@](https://wiki.frictionalgames.com/page/../../iLight)` | — |

**Returns:** `cLightSpot@`

    1. `cScene_ToMeshEntity`

```angelscript
cMeshEntity@ cScene_ToMeshEntity(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cMeshEntity@`

    1. `cScene_ToRopeEntity`

```angelscript
iRopeEntity@ cScene_ToRopeEntity(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `iRopeEntity@`

    1. `cScene_ToRopeEntity3D`

```angelscript
cRopeEntity3D@ cScene_ToRopeEntity3D(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cRopeEntity3D@`

    1. `cScene_ToRopeEntityBillboard`

```angelscript
cRopeEntityBillboard@ cScene_ToRopeEntityBillboard(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cRopeEntityBillboard@`

    1. `cScene_ToSoundEntity`

```angelscript
cSoundEntity@ cScene_ToSoundEntity(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cSoundEntity@`

    1. `cScene_ToSubMeshEntity`

```angelscript
cSubMeshEntity@ cScene_ToSubMeshEntity(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `cSubMeshEntity@`

    1. `cScene_ViewportExists`

```angelscript
bool cScene_ViewportExists(cViewport@ apViewPort)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apViewPort` | `[cViewport@](https://wiki.frictionalgames.com/page/../../cViewport)` | — |

**Returns:** `bool`

    1. `cScene_WorldExists`

```angelscript
void cScene_WorldExists(cWorld@ apWorld)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apWorld` | `[cWorld@](https://wiki.frictionalgames.com/page/../../cWorld)` | — |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cScene](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cScene)
- Revision: `5023`
- Source update: `2020-08-24T20:50:52Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

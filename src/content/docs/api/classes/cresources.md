---
title: cResources
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cResources"
sourceRevision: 5022
sourceUpdated: "2020-08-24T20:50:31Z"
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
| `bool` | [`cResources_AddLanguageFile`](#cresources-addlanguagefile)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFilePath, bool abAddResourceDirs) | *Undocumented in the original Wiki.* |
| `bool` | [`cResources_AddResourceDir`](#cresources-addresourcedir)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asDir, bool abAddSubDirectories, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asMask) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_ClearResourceDirs`](#cresources-clearresourcedirs)() | *Undocumented in the original Wiki.* |
| `void` | [`cResources_ClearTranslations`](#cresources-cleartranslations)() | *Undocumented in the original Wiki.* |
| `iFontData` | [`cResources_CreateFontData`](#cresources-createfontdata)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `iGpuShader` | [`cResources_CreateGpuShader`](#cresources-creategpushader)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alType, [cPrepParserVarContainer](https://wiki.frictionalgames.com/page/../../cPrepParserVarContainer) @apVarCont) | *Undocumented in the original Wiki.* |
| `iGpuShader` | [`cResources_CreateGpuShader`](#cresources-creategpushader)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alType) | *Undocumented in the original Wiki.* |
| `cFrameSubImage` | [`cResources_CreateImage`](#cresources-createimage)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cMaterial` | [`cResources_CreateMaterial`](#cresources-creatematerial)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cMesh` | [`cResources_CreateMesh`](#cresources-createmesh)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `iSoundData` | [`cResources_CreateSoundData`](#cresources-createsounddata)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abStream, bool abLooping, bool ab3, bool abNonBlockingLoad) | *Undocumented in the original Wiki.* |
| `cSoundEntityData` | [`cResources_CreateSoundEntityData`](#cresources-createsoundentitydata)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `iTexture` | [`cResources_CreateTexture1D`](#cresources-createtexture1d)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abUseMipMaps) | *Undocumented in the original Wiki.* |
| `iTexture` | [`cResources_CreateTexture2D`](#cresources-createtexture2d)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abUseMipMaps) | *Undocumented in the original Wiki.* |
| `iTexture` | [`cResources_CreateTexture3D`](#cresources-createtexture3d)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abUseMipMaps) | *Undocumented in the original Wiki.* |
| `iTexture` | [`cResources_CreateTextureCubeMap`](#cresources-createtexturecubemap)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abUseMipMaps) | *Undocumented in the original Wiki.* |
| `iVideoStream` | [`cResources_CreateVideo`](#cresources-createvideo)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyFontData`](#cresources-destroyfontdata)([iFontData](https://wiki.frictionalgames.com/page/../../iFontData) @apData) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyGpuShader`](#cresources-destroygpushader)([iGpuShader](https://wiki.frictionalgames.com/page/../../iGpuShader) @apShader) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyImage`](#cresources-destroyimage)([cFrameSubImage](https://wiki.frictionalgames.com/page/../../cFrameSubImage) @apData) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyMaterial`](#cresources-destroymaterial)([cMaterial](https://wiki.frictionalgames.com/page/../../cMaterial) @apMaterial) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyMesh`](#cresources-destroymesh)([cMesh@](https://wiki.frictionalgames.com/page/../../cMesh) apMesh) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroySoundData`](#cresources-destroysounddata)([iSoundData@](https://wiki.frictionalgames.com/page/../../iSoundData) apData) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroySoundEntityData`](#cresources-destroysoundentitydata)([cSoundEntityData](https://wiki.frictionalgames.com/page/../../cSoundEntityData) @apData) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyTexture`](#cresources-destroytexture)([iTexture](https://wiki.frictionalgames.com/page/../../iTexture) @apTexture) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyUnusedParticleSystems`](#cresources-destroyunusedparticlesystems)(int alMaxToKeep) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyUnusedSoundData`](#cresources-destroyunusedsounddata)(int alMaxToKeep) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyVideo`](#cresources-destroyvideo)([iVideoStream](https://wiki.frictionalgames.com/page/../../iVideoStream) @apVideo) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_DestroyXmlDocument`](#cresources-destroyxmldocument)([iXmlDocument@](https://wiki.frictionalgames.com/page/../../iXmlDocument) apDoc) | *Undocumented in the original Wiki.* |
| `tString` | [`cResources_GetMaterialPhysicsName`](#cresources-getmaterialphysicsname)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `float` | [`cResources_GetMaterialTextureAnisotropy`](#cresources-getmaterialtextureanisotropy)() | *Undocumented in the original Wiki.* |
| `int` | [`cResources_GetMaterialTextureFilter`](#cresources-getmaterialtexturefilter)() | *Undocumented in the original Wiki.* |
| `int` | [`cResources_GetMaterialTextureSizeDownScaleLevel`](#cresources-getmaterialtexturesizedownscalelevel)() | *Undocumented in the original Wiki.* |
| `bool` | [`cResources_LoadResourceDirsFile`](#cresources-loadresourcedirsfile)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile) | *Undocumented in the original Wiki.* |
| `iXmlDocument` | [`cResources_LoadXmlDocument`](#cresources-loadxmldocument)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_PreloadParticleSystem`](#cresources-preloadparticlesystem)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asDataName) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_PreloadSoundEntityData`](#cresources-preloadsoundentitydata)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abNonBlockingLoad) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_SetMaterialTextureAnisotropy`](#cresources-setmaterialtextureanisotropy)(float afX) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_SetMaterialTextureFilter`](#cresources-setmaterialtexturefilter)(int alFilter) | *Undocumented in the original Wiki.* |
| `void` | [`cResources_SetMaterialTextureSizeDownScaleLevel`](#cresources-setmaterialtexturesizedownscalelevel)(int alLevel) | *Undocumented in the original Wiki.* |
| `tWString` | [`cResources_Translate`](#cresources-translate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCat, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cResources_AddLanguageFile`

```angelscript
bool cResources_AddLanguageFile(const tString &in asFilePath,
                                bool abAddResourceDirs)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFilePath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abAddResourceDirs` | `bool` | — |

**Returns:** `bool`

    1. `cResources_AddResourceDir`

```angelscript
bool cResources_AddResourceDir(const tWString &in asDir,
                               bool abAddSubDirectories,
                               const tString &in asMask)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asDir` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `abAddSubDirectories` | `bool` | — |
| `asMask` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cResources_ClearResourceDirs`

```angelscript
void cResources_ClearResourceDirs()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cResources_ClearTranslations`

```angelscript
void cResources_ClearTranslations()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cResources_CreateFontData`

```angelscript
iFontData@ cResources_CreateFontData(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `iFontData@`

    1. `cResources_CreateGpuShader`

```angelscript
iGpuShader@ cResources_CreateGpuShader(const tString &in asName,
                                       int alType,
                                       cPrepParserVarContainer @apVarCont)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alType` | `int` | — |
| `@apVarCont` | `[cPrepParserVarContainer](https://wiki.frictionalgames.com/page/../../cPrepParserVarContainer)` | — |

**Returns:** `iGpuShader@`

    1. `cResources_CreateGpuShader`

```angelscript
iGpuShader@ cResources_CreateGpuShader(const tString &in asName,
                                       int alType)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alType` | `int` | — |

**Returns:** `iGpuShader@`

    1. `cResources_CreateImage`

```angelscript
cFrameSubImage@ cResources_CreateImage(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cFrameSubImage@`

    1. `cResources_CreateMaterial`

```angelscript
cMaterial@ cResources_CreateMaterial(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cMaterial@`

    1. `cResources_CreateMesh`

```angelscript
cMesh@ cResources_CreateMesh(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cMesh@`

    1. `cResources_CreateSoundData`

```angelscript
iSoundData@ cResources_CreateSoundData(const tString &in asName,
                                       bool abStream,
                                       bool abLooping,
                                       bool ab3,
                                       bool abNonBlockingLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abStream` | `bool` | — |
| `abLooping` | `bool` | — |
| `ab3` | `bool` | — |
| `abNonBlockingLoad` | `bool` | — |

**Returns:** `iSoundData@`

    1. `cResources_CreateSoundEntityData`

```angelscript
cSoundEntityData@ cResources_CreateSoundEntityData(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cSoundEntityData@`

    1. `cResources_CreateTexture1D`

```angelscript
iTexture@ cResources_CreateTexture1D(const tString &in asName,
                                     bool abUseMipMaps)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abUseMipMaps` | `bool` | — |

**Returns:** `iTexture@`

    1. `cResources_CreateTexture2D`

```angelscript
iTexture@ cResources_CreateTexture2D(const tString &in asName,
                                     bool abUseMipMaps)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abUseMipMaps` | `bool` | — |

**Returns:** `iTexture@`

    1. `cResources_CreateTexture3D`

```angelscript
iTexture@ cResources_CreateTexture3D(const tString &in asName,
                                     bool abUseMipMaps)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abUseMipMaps` | `bool` | — |

**Returns:** `iTexture@`

    1. `cResources_CreateTextureCubeMap`

```angelscript
iTexture@ cResources_CreateTextureCubeMap(const tString &in asName,
                                          bool abUseMipMaps)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abUseMipMaps` | `bool` | — |

**Returns:** `iTexture@`

    1. `cResources_CreateVideo`

```angelscript
iVideoStream@ cResources_CreateVideo(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `iVideoStream@`

    1. `cResources_DestroyFontData`

```angelscript
void cResources_DestroyFontData(iFontData @apData)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apData` | `[iFontData](https://wiki.frictionalgames.com/page/../../iFontData)` | — |

**Returns:** `void`

    1. `cResources_DestroyGpuShader`

```angelscript
void cResources_DestroyGpuShader(iGpuShader @apShader)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apShader` | `[iGpuShader](https://wiki.frictionalgames.com/page/../../iGpuShader)` | — |

**Returns:** `void`

    1. `cResources_DestroyImage`

```angelscript
void cResources_DestroyImage(cFrameSubImage @apData)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apData` | `[cFrameSubImage](https://wiki.frictionalgames.com/page/../../cFrameSubImage)` | — |

**Returns:** `void`

    1. `cResources_DestroyMaterial`

```angelscript
void cResources_DestroyMaterial(cMaterial @apMaterial)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apMaterial` | `[cMaterial](https://wiki.frictionalgames.com/page/../../cMaterial)` | — |

**Returns:** `void`

    1. `cResources_DestroyMesh`

```angelscript
void cResources_DestroyMesh(cMesh@ apMesh)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apMesh` | `[cMesh@](https://wiki.frictionalgames.com/page/../../cMesh)` | — |

**Returns:** `void`

    1. `cResources_DestroySoundData`

```angelscript
void cResources_DestroySoundData(iSoundData@ apData)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apData` | `[iSoundData@](https://wiki.frictionalgames.com/page/../../iSoundData)` | — |

**Returns:** `void`

    1. `cResources_DestroySoundEntityData`

```angelscript
void cResources_DestroySoundEntityData(cSoundEntityData @apData)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apData` | `[cSoundEntityData](https://wiki.frictionalgames.com/page/../../cSoundEntityData)` | — |

**Returns:** `void`

    1. `cResources_DestroyTexture`

```angelscript
void cResources_DestroyTexture(iTexture @apTexture)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apTexture` | `[iTexture](https://wiki.frictionalgames.com/page/../../iTexture)` | — |

**Returns:** `void`

    1. `cResources_DestroyUnusedParticleSystems`

```angelscript
void cResources_DestroyUnusedParticleSystems(int alMaxToKeep)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alMaxToKeep` | `int` | — |

**Returns:** `void`

    1. `cResources_DestroyUnusedSoundData`

```angelscript
void cResources_DestroyUnusedSoundData(int alMaxToKeep)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alMaxToKeep` | `int` | — |

**Returns:** `void`

    1. `cResources_DestroyVideo`

```angelscript
void cResources_DestroyVideo(iVideoStream @apVideo)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apVideo` | `[iVideoStream](https://wiki.frictionalgames.com/page/../../iVideoStream)` | — |

**Returns:** `void`

    1. `cResources_DestroyXmlDocument`

```angelscript
void cResources_DestroyXmlDocument(iXmlDocument@ apDoc)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apDoc` | `[iXmlDocument@](https://wiki.frictionalgames.com/page/../../iXmlDocument)` | — |

**Returns:** `void`

    1. `cResources_GetMaterialPhysicsName`

```angelscript
tString cResources_GetMaterialPhysicsName(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cResources_GetMaterialTextureAnisotropy`

```angelscript
float cResources_GetMaterialTextureAnisotropy()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cResources_GetMaterialTextureFilter`

```angelscript
int cResources_GetMaterialTextureFilter()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `int`

    1. `cResources_GetMaterialTextureSizeDownScaleLevel`

```angelscript
int cResources_GetMaterialTextureSizeDownScaleLevel()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `int`

    1. `cResources_LoadResourceDirsFile`

```angelscript
bool cResources_LoadResourceDirsFile(const tString &in asFile)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cResources_LoadXmlDocument`

```angelscript
iXmlDocument@ cResources_LoadXmlDocument(const tString &in asFile)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `iXmlDocument@`

    1. `cResources_PreloadParticleSystem`

```angelscript
void cResources_PreloadParticleSystem(const tString &in asDataName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asDataName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cResources_PreloadSoundEntityData`

```angelscript
void cResources_PreloadSoundEntityData(const tString &in asName,
                                       bool abNonBlockingLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abNonBlockingLoad` | `bool` | — |

**Returns:** `void`

    1. `cResources_SetMaterialTextureAnisotropy`

```angelscript
void cResources_SetMaterialTextureAnisotropy(float afX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afX` | `float` | — |

**Returns:** `void`

    1. `cResources_SetMaterialTextureFilter`

```angelscript
void cResources_SetMaterialTextureFilter(int alFilter)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alFilter` | `int` | — |

**Returns:** `void`

    1. `cResources_SetMaterialTextureSizeDownScaleLevel`

```angelscript
void cResources_SetMaterialTextureSizeDownScaleLevel(int alLevel)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alLevel` | `int` | — |

**Returns:** `void`

    1. `cResources_Translate`

```angelscript
const tWString& cResources_Translate(const tString &in asCat,
                                     const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asCat` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `const tWString&`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cResources](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cResources)
- Revision: `5022`
- Source update: `2020-08-24T20:50:31Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

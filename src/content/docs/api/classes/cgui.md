---
title: cGui
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cGui"
sourceRevision: 5017
sourceUpdated: "2020-08-24T20:48:38Z"
lastSynced: "2026-09-28T13:28:41Z"
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
| `cGuiGfxElement` | [`cGui_CreateGfxFilledRect`](#cgui-creategfxfilledrect)(const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxImage`](#cgui-creategfximage)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxImage`](#cgui-creategfximage)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxImageBuffer`](#cgui-creategfximagebuffer)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial, bool abCreateAnimation, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxTexture`](#cgui-creategfxtexture)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial, [eTextureType](https://wiki.frictionalgames.com/page/../../eTextureType) aTextureType) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxTexture`](#cgui-creategfxtexture)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial, [eTextureType](https://wiki.frictionalgames.com/page/../../eTextureType) aTextureType, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor, bool abMipMaps) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxTexture`](#cgui-creategfxtexture)([iTexture](https://wiki.frictionalgames.com/page/../../iTexture) @apTexture, bool abAutoDestroyTexture, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial) | *Undocumented in the original Wiki.* |
| `cGuiGfxElement` | [`cGui_CreateGfxTexture`](#cgui-creategfxtexture)([iTexture](https://wiki.frictionalgames.com/page/../../iTexture) @apTexture, bool abAutoDestroyTexture, [eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial) aMaterial, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avStartUV, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avEndUV) | *Undocumented in the original Wiki.* |
| `cImGui` | [`cGui_CreateImGui`](#cgui-createimgui)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [cGuiSet](https://wiki.frictionalgames.com/page/../../cGuiSet) @apSet) | *Undocumented in the original Wiki.* |
| `cGuiSet` | [`cGui_CreateSet`](#cgui-createset)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [cGuiSkin](https://wiki.frictionalgames.com/page/../../cGuiSkin) @apSkin) | *Undocumented in the original Wiki.* |
| `cGuiSkin` | [`cGui_CreateSkin`](#cgui-createskin)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile) | *Undocumented in the original Wiki.* |
| `void` | [`cGui_DestroyGfx`](#cgui-destroygfx)([cGuiGfxElement@](https://wiki.frictionalgames.com/page/../../cGuiGfxElement) apGfx) | *Undocumented in the original Wiki.* |
| `void` | [`cGui_DestroyImGui`](#cgui-destroyimgui)([cImGui@](https://wiki.frictionalgames.com/page/../../cImGui) apImGui) | *Undocumented in the original Wiki.* |
| `void` | [`cGui_DestroySet`](#cgui-destroyset)([cGuiSet](https://wiki.frictionalgames.com/page/../../cGuiSet) @apSet) | *Undocumented in the original Wiki.* |
| `cGuiSet` | [`cGui_GetFocusedSet`](#cgui-getfocusedset)() | *Undocumented in the original Wiki.* |
| `void` | [`cGui_GetImGuiIdFromName`](#cgui-getimguiidfromname)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `void` | [`cGui_GetImGuiStateVarString`](#cgui-getimguistatevarstring)([eImGuiStateVar](https://wiki.frictionalgames.com/page/../../eImGuiStateVar) aVar) | *Undocumented in the original Wiki.* |
| `cGuiSet` | [`cGui_GetSetFromName`](#cgui-getsetfromname)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `void` | [`cGui_SetFocus`](#cgui-setfocus)([cGuiSet@](https://wiki.frictionalgames.com/page/../../cGuiSet) apSet) | *Undocumented in the original Wiki.* |
| `void` | [`cGui_SetFocusByName`](#cgui-setfocusbyname)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asSetName) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cGui_CreateGfxFilledRect`

```cpp
cGuiGfxElement@ cGui_CreateGfxFilledRect(const cColor &in aColor,
                                         eGuiMaterial aMaterial)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxImage`

```cpp
cGuiGfxElement@ cGui_CreateGfxImage(const tString &in asFile,
                                    eGuiMaterial aMaterial)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxImage`

```cpp
cGuiGfxElement@ cGui_CreateGfxImage(const tString &in asFile,
                                    eGuiMaterial aMaterial,
                                    const cColor &in aColor)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxImageBuffer`

```cpp
cGuiGfxElement@ cGui_CreateGfxImageBuffer(const tString &in asFile,
                                          eGuiMaterial aMaterial,
                                          bool abCreateAnimation,
                                          const cColor &in aColor)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |
| `abCreateAnimation` | `bool` | — |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxTexture`

```cpp
cGuiGfxElement@ cGui_CreateGfxTexture(const tString &in asFile,
                                      eGuiMaterial aMaterial,
                                      eTextureType aTextureType)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |
| `aTextureType` | `[eTextureType](https://wiki.frictionalgames.com/page/../../eTextureType)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxTexture`

```cpp
cGuiGfxElement@ cGui_CreateGfxTexture(const tString &in asFile,
                                      eGuiMaterial aMaterial,
                                      eTextureType aTextureType,
                                      const cColor &in aColor,
                                      bool abMipMaps)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |
| `aTextureType` | `[eTextureType](https://wiki.frictionalgames.com/page/../../eTextureType)` | — |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |
| `abMipMaps` | `bool` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxTexture`

```cpp
cGuiGfxElement@ cGui_CreateGfxTexture(iTexture @apTexture,
                                      bool abAutoDestroyTexture,
                                      eGuiMaterial aMaterial)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apTexture` | `[iTexture](https://wiki.frictionalgames.com/page/../../iTexture)` | — |
| `abAutoDestroyTexture` | `bool` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateGfxTexture`

```cpp
cGuiGfxElement@ cGui_CreateGfxTexture(iTexture @apTexture,
                                      bool abAutoDestroyTexture,
                                      eGuiMaterial aMaterial,
                                      const cColor &in aColor,
                                      const cVector2f &in avStartUV,
                                      const cVector2f &in avEndUV)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apTexture` | `[iTexture](https://wiki.frictionalgames.com/page/../../iTexture)` | — |
| `abAutoDestroyTexture` | `bool` | — |
| `aMaterial` | `[eGuiMaterial](https://wiki.frictionalgames.com/page/../../eGuiMaterial)` | — |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |
| `avStartUV` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | — |
| `avEndUV` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | — |

**Returns:** `cGuiGfxElement@`

    1. `cGui_CreateImGui`

```cpp
cImGui@ cGui_CreateImGui(const tString &in asName,
                         cGuiSet @apSet)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `@apSet` | `[cGuiSet](https://wiki.frictionalgames.com/page/../../cGuiSet)` | — |

**Returns:** `cImGui@`

    1. `cGui_CreateSet`

```cpp
cGuiSet@ cGui_CreateSet(const tString &in asName,
                        cGuiSkin @apSkin)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `@apSkin` | `[cGuiSkin](https://wiki.frictionalgames.com/page/../../cGuiSkin)` | — |

**Returns:** `cGuiSet@`

    1. `cGui_CreateSkin`

```cpp
cGuiSkin@ cGui_CreateSkin(const tString &in asFile)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cGuiSkin@`

    1. `cGui_DestroyGfx`

```cpp
void cGui_DestroyGfx(cGuiGfxElement@ apGfx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apGfx` | `[cGuiGfxElement@](https://wiki.frictionalgames.com/page/../../cGuiGfxElement)` | — |

**Returns:** `void`

    1. `cGui_DestroyImGui`

```cpp
void cGui_DestroyImGui(cImGui@ apImGui)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apImGui` | `[cImGui@](https://wiki.frictionalgames.com/page/../../cImGui)` | — |

**Returns:** `void`

    1. `cGui_DestroySet`

```cpp
void cGui_DestroySet(cGuiSet @apSet)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apSet` | `[cGuiSet](https://wiki.frictionalgames.com/page/../../cGuiSet)` | — |

**Returns:** `void`

    1. `cGui_GetFocusedSet`

```cpp
cGuiSet@ cGui_GetFocusedSet()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `cGuiSet@`

    1. `cGui_GetImGuiIdFromName`

```cpp
void cGui_GetImGuiIdFromName(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cGui_GetImGuiStateVarString`

```cpp
void cGui_GetImGuiStateVarString(eImGuiStateVar aVar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aVar` | `[eImGuiStateVar](https://wiki.frictionalgames.com/page/../../eImGuiStateVar)` | — |

**Returns:** `void`

    1. `cGui_GetSetFromName`

```cpp
cGuiSet@ cGui_GetSetFromName(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cGuiSet@`

    1. `cGui_SetFocus`

```cpp
void cGui_SetFocus(cGuiSet@ apSet)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apSet` | `[cGuiSet@](https://wiki.frictionalgames.com/page/../../cGuiSet)` | — |

**Returns:** `void`

    1. `cGui_SetFocusByName`

```cpp
void cGui_SetFocusByName(const tString &in asSetName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asSetName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cGui](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cGui)
- Revision: `5017`
- Source update: `2020-08-24T20:48:38Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

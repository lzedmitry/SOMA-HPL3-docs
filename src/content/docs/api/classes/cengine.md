---
title: cEngine
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cEngine"
sourceRevision: 5014
sourceUpdated: "2020-08-24T20:46:46Z"
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
| `void` | [`cEngine_Exit`](#cengine-exit)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetAvgFrameTimeInMS`](#cengine-getavgframetimeinms)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetAvgLogicFrameTimeMS`](#cengine-getavglogicframetimems)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetAvgRenderFrameTimeMS`](#cengine-getavgrenderframetimems)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetAvgVariableFrameTimeMS`](#cengine-getavgvariableframetimems)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetFPS`](#cengine-getfps)() | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_GetFPSMinMax`](#cengine-getfpsminmax)(float &out afMin, float &out afMax) | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetFPSUpdateRate`](#cengine-getfpsupdaterate)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetFrameTime`](#cengine-getframetime)() | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_GetFrameTimeMinMax`](#cengine-getframetimeminmax)(float &out afMin, float &out afMax) | *Undocumented in the original Wiki.* |
| `double` | [`cEngine_GetGameTime`](#cengine-getgametime)() | *Undocumented in the original Wiki.* |
| `bool` | [`cEngine_GetLimitFPS`](#cengine-getlimitfps)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetMaxMS`](#cengine-getmaxms)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetMinMS`](#cengine-getminms)() | *Undocumented in the original Wiki.* |
| `uint` | [`cEngine_GetPerFrameUpdateSteps`](#cengine-getperframeupdatesteps)() | *Undocumented in the original Wiki.* |
| `uint` | [`cEngine_GetSceneRenderFlags`](#cengine-getscenerenderflags)() | *Undocumented in the original Wiki.* |
| `float` | [`cEngine_GetStepSize`](#cengine-getstepsize)() | *Undocumented in the original Wiki.* |
| `int` | [`cEngine_GetUpdatesPerSec`](#cengine-getupdatespersec)() | *Undocumented in the original Wiki.* |
| `bool` | [`cEngine_GetWaitIfAppOutOfFocus`](#cengine-getwaitifappoutoffocus)() | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_ResetLogicTimer`](#cengine-resetlogictimer)() | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetAllGlobalUpdatersPaused`](#cengine-setallglobalupdaterspaused)(bool abPaused) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetAllUpdatersPaused`](#cengine-setallupdaterspaused)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asContainer, bool abPaused) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetFPSUpdateRate`](#cengine-setfpsupdaterate)(float afSec) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetGlobalUpdaterPaused`](#cengine-setglobalupdaterpaused)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asUpdate, bool abPaused) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetLimitFPS`](#cengine-setlimitfps)(bool abX) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetSceneRenderFlags`](#cengine-setscenerenderflags)(uint alFlags) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetUpdaterPaused`](#cengine-setupdaterpaused)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asContainer, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asUpdate, bool abPaused) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetUpdatesPerSec`](#cengine-setupdatespersec)(int alUpdatesPerSec) | *Undocumented in the original Wiki.* |
| `void` | [`cEngine_SetWaitIfAppOutOfFocus`](#cengine-setwaitifappoutoffocus)(bool abX) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cEngine_Exit`

```cpp
void cEngine_Exit()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cEngine_GetAvgFrameTimeInMS`

```cpp
float cEngine_GetAvgFrameTimeInMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetAvgLogicFrameTimeMS`

```cpp
float cEngine_GetAvgLogicFrameTimeMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetAvgRenderFrameTimeMS`

```cpp
float cEngine_GetAvgRenderFrameTimeMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetAvgVariableFrameTimeMS`

```cpp
float cEngine_GetAvgVariableFrameTimeMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFPS`

```cpp
float cEngine_GetFPS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFPSMinMax`

```cpp
void cEngine_GetFPSMinMax(float &out afMin,
                          float &out afMax)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afMin` | `float` | — |
| `afMax` | `float` | — |

**Returns:** `void`

    1. `cEngine_GetFPSUpdateRate`

```cpp
float cEngine_GetFPSUpdateRate()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFrameTime`

```cpp
float cEngine_GetFrameTime()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFrameTimeMinMax`

```cpp
void cEngine_GetFrameTimeMinMax(float &out afMin,
                                float &out afMax)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afMin` | `float` | — |
| `afMax` | `float` | — |

**Returns:** `void`

    1. `cEngine_GetGameTime`

```cpp
double cEngine_GetGameTime()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `double`

    1. `cEngine_GetLimitFPS`

```cpp
bool cEngine_GetLimitFPS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cEngine_GetMaxMS`

```cpp
float cEngine_GetMaxMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetMinMS`

```cpp
float cEngine_GetMinMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetPerFrameUpdateSteps`

```cpp
uint cEngine_GetPerFrameUpdateSteps()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `uint`

    1. `cEngine_GetSceneRenderFlags`

```cpp
uint cEngine_GetSceneRenderFlags()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `uint`

    1. `cEngine_GetStepSize`

```cpp
float cEngine_GetStepSize()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetUpdatesPerSec`

```cpp
int cEngine_GetUpdatesPerSec()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `int`

    1. `cEngine_GetWaitIfAppOutOfFocus`

```cpp
bool cEngine_GetWaitIfAppOutOfFocus()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cEngine_ResetLogicTimer`

```cpp
void cEngine_ResetLogicTimer()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cEngine_SetAllGlobalUpdatersPaused`

```cpp
void cEngine_SetAllGlobalUpdatersPaused(bool abPaused)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `abPaused` | `bool` | — |

**Returns:** `void`

    1. `cEngine_SetAllUpdatersPaused`

```cpp
void cEngine_SetAllUpdatersPaused(const tString &in asContainer,
                                  bool abPaused)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asContainer` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abPaused` | `bool` | — |

**Returns:** `void`

    1. `cEngine_SetFPSUpdateRate`

```cpp
void cEngine_SetFPSUpdateRate(float afSec)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afSec` | `float` | — |

**Returns:** `void`

    1. `cEngine_SetGlobalUpdaterPaused`

```cpp
void cEngine_SetGlobalUpdaterPaused(const tString &in asUpdate,
                                    bool abPaused)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asUpdate` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abPaused` | `bool` | — |

**Returns:** `void`

    1. `cEngine_SetLimitFPS`

```cpp
void cEngine_SetLimitFPS(bool abX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `abX` | `bool` | — |

**Returns:** `void`

    1. `cEngine_SetSceneRenderFlags`

```cpp
void cEngine_SetSceneRenderFlags(uint alFlags)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alFlags` | `uint` | — |

**Returns:** `void`

    1. `cEngine_SetUpdaterPaused`

```cpp
void cEngine_SetUpdaterPaused(const tString &in asContainer,
                              const tString &in asUpdate,
                              bool abPaused)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asContainer` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asUpdate` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abPaused` | `bool` | — |

**Returns:** `void`

    1. `cEngine_SetUpdatesPerSec`

```cpp
void cEngine_SetUpdatesPerSec(int alUpdatesPerSec)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alUpdatesPerSec` | `int` | — |

**Returns:** `void`

    1. `cEngine_SetWaitIfAppOutOfFocus`

```cpp
void cEngine_SetWaitIfAppOutOfFocus(bool abX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `abX` | `bool` | — |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cEngine](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cEngine)
- Revision: `5014`
- Source update: `2020-08-24T20:46:46Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

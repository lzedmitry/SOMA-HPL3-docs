---
title: cEngine
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cEngine"
sourceRevision: 5014
sourceUpdated: "2020-08-24T20:46:46Z"
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

```angelscript
void cEngine_Exit()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cEngine_GetAvgFrameTimeInMS`

```angelscript
float cEngine_GetAvgFrameTimeInMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetAvgLogicFrameTimeMS`

```angelscript
float cEngine_GetAvgLogicFrameTimeMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetAvgRenderFrameTimeMS`

```angelscript
float cEngine_GetAvgRenderFrameTimeMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetAvgVariableFrameTimeMS`

```angelscript
float cEngine_GetAvgVariableFrameTimeMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFPS`

```angelscript
float cEngine_GetFPS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFPSMinMax`

```angelscript
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

```angelscript
float cEngine_GetFPSUpdateRate()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFrameTime`

```angelscript
float cEngine_GetFrameTime()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetFrameTimeMinMax`

```angelscript
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

```angelscript
double cEngine_GetGameTime()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `double`

    1. `cEngine_GetLimitFPS`

```angelscript
bool cEngine_GetLimitFPS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cEngine_GetMaxMS`

```angelscript
float cEngine_GetMaxMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetMinMS`

```angelscript
float cEngine_GetMinMS()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetPerFrameUpdateSteps`

```angelscript
uint cEngine_GetPerFrameUpdateSteps()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `uint`

    1. `cEngine_GetSceneRenderFlags`

```angelscript
uint cEngine_GetSceneRenderFlags()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `uint`

    1. `cEngine_GetStepSize`

```angelscript
float cEngine_GetStepSize()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cEngine_GetUpdatesPerSec`

```angelscript
int cEngine_GetUpdatesPerSec()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `int`

    1. `cEngine_GetWaitIfAppOutOfFocus`

```angelscript
bool cEngine_GetWaitIfAppOutOfFocus()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cEngine_ResetLogicTimer`

```angelscript
void cEngine_ResetLogicTimer()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cEngine_SetAllGlobalUpdatersPaused`

```angelscript
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

```angelscript
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

```angelscript
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

```angelscript
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

```angelscript
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

```angelscript
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

```angelscript
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

```angelscript
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

```angelscript
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
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Meter
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Meter"
sourceRevision: 5042
sourceUpdated: "2020-08-24T20:56:58Z"
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
| `void` | [`Meter_SetShakeMul`](#meter-setshakemul)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afShakeMul) | Sets the shake multiplier of the needle object in meter |
| `void` | [`Meter_SetSpeedMul`](#meter-setspeedmul)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afSpeedMul) | Sets the speed multiplier of the needle object in meter |
| `void` | [`Meter_SetState`](#meter-setstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afState, bool abFadeToState = true) | Sets the state of the needle object in meter |

## Function Detail
    1. `Meter_SetShakeMul`

```angelscript
void Meter_SetShakeMul(const tString &in asName,
                       float afShakeMul)
```

Sets the shake multiplier of the needle object in meter.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of meter object |
| `afShakeMul` | `float` | the shaking multiplier. capped at 10. |

**Returns:** `void`

    1. `Meter_SetSpeedMul`

```angelscript
void Meter_SetSpeedMul(const tString &in asName,
                       float afSpeedMul)
```

Sets the speed multiplier of the needle object in meter.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of meter object |
| `afSpeedMul` | `float` | the speed multiplier. |

**Returns:** `void`

    1. `Meter_SetState`

```angelscript
void Meter_SetState(const tString &in asName,
                    float afState,
                    bool abFadeToState = true)
```

Sets the state of the needle object in meter. Which then makes the needle move to the specified state.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of meter object |
| `afState` | `float` | percentage of where the needle should be. 0-1 (min pos - max pos). |
| `abFadeToState` | `bool` | if true then the needle will fade to state instead of skipping to it. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Meter](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Meter)
- Revision: `5042`
- Source update: `2020-08-24T20:56:58Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

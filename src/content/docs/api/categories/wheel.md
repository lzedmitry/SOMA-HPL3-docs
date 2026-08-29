---
title: Wheel
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Wheel"
sourceRevision: 5055
sourceUpdated: "2020-08-24T21:00:27Z"
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
| `float` | [`Wheel_GetCurrentAngle`](#wheel-getcurrentangle)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the angle of a wheel |
| `int` | [`Wheel_GetState`](#wheel-getstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the state of the wheel |
| `void` | [`Wheel_SetAngle`](#wheel-setangle)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afAngle, bool abAutoMove) | Sets the angle of a wheel |
| `void` | [`Wheel_SetInteractionDisablesStuck`](#wheel-setinteractiondisablesstuck)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | Sets if player interaction will disable the stuck state of a wheel |
| `void` | [`Wheel_SetStuckState`](#wheel-setstuckstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alState, bool abEffects) | Sets the stuck state of a wheel |

## Function Detail
    1. `Wheel_GetCurrentAngle`

```angelscript
float Wheel_GetCurrentAngle(const tString &in asName)
```

Gets the angle of a wheel.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of wheel. |

**Returns:** `float` — angle in radians

    1. `Wheel_GetState`

```angelscript
int Wheel_GetState(const tString &in asName)
```

Gets the state of the wheel

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of wheel. |

**Returns:** `int` — -1 = min, 0 = middle, 1 = max

    1. `Wheel_SetAngle`

```angelscript
void Wheel_SetAngle(const tString &in asName,
                    float afAngle,
                    bool abAutoMove)
```

Sets the angle of a wheel.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of wheel. |
| `afAngle` | `float` | angle to set in radians. |
| `abAutoMove` | `bool` | if the wheel should move to the angle automatically. |

**Returns:** `void`

    1. `Wheel_SetInteractionDisablesStuck`

```angelscript
void Wheel_SetInteractionDisablesStuck(const tString &in asName,
                                       bool abX)
```

Sets if player interaction will disable the stuck state of a wheel.  
effect on stuck state.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of wheel. |
| `abX` | `bool` | true = interaction disables stuck state - false = interaction has no |

**Returns:** `void`

    1. `Wheel_SetStuckState`

```angelscript
void Wheel_SetStuckState(const tString &in asName,
                         int alState,
                         bool abEffects)
```

Sets the stuck state of a wheel.  
the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of wheel. |
| `alState` | `int` | stuck state where -1 = stuck at min, 1 = stuck at max and 0 = not stuck. |
| `abEffects` | `bool` | if the change should activate effects associated with it. If false, |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Wheel](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Wheel)
- Revision: `5055`
- Source update: `2020-08-24T21:00:27Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

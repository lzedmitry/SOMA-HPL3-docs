---
title: Lever
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Lever"
sourceRevision: 5037
sourceUpdated: "2020-08-24T20:55:40Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `int` | [`Lever_GetState`](#lever-getstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the state of the lever |
| `void` | [`Lever_SetAutoMoveEnabled`](#lever-setautomoveenabled)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abAutoMove) | Enables or disables the auto move property of the lever |
| `void` | [`Lever_SetAutoMoveTarget`](#lever-setautomovetarget)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alTarget) | Sets the auto move target of the lever |
| `void` | [`Lever_SetInteractionDisablesStuck`](#lever-setinteractiondisablesstuck)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | Sets if player interaction will disable the stuck state of a lever |
| `void` | [`Lever_SetStuckState`](#lever-setstuckstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alState, bool abEffects) | Sets the stuck state of a lever |

## Function Detail
    1. `Lever_GetState`

```cpp
int Lever_GetState(const tString &in asName)
```

Gets the state of the lever

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lever. |

**Returns:** `int` — int -1 = min, 0 = middle, 1 = max

    1. `Lever_SetAutoMoveEnabled`

```cpp
void Lever_SetAutoMoveEnabled(const tString &in asName,
                              bool abAutoMove)
```

Enables or disables the auto move property of the lever.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lever. |
| `abAutoMove` | `bool` | if true, auto move will be enabled. |

**Returns:** `void`

    1. `Lever_SetAutoMoveTarget`

```cpp
void Lever_SetAutoMoveTarget(const tString &in asName,
                             int alTarget)
```

Sets the auto move target of the lever.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lever. |
| `alTarget` | `int` | -1 = min, 0 = middle, 1 = max |

**Returns:** `void`

    1. `Lever_SetInteractionDisablesStuck`

```cpp
void Lever_SetInteractionDisablesStuck(const tString &in asName,
                                       bool abX)
```

Sets if player interaction will disable the stuck state of a lever.  
effect on stuck state.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lever. |
| `abX` | `bool` | true = interaction disables stuck state - false = interaction has no |

**Returns:** `void`

    1. `Lever_SetStuckState`

```cpp
void Lever_SetStuckState(const tString &in asName,
                         int alState,
                         bool abEffects)
```

Sets the stuck state of a lever.  
the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lever. |
| `alState` | `int` | stuck state where -1 = stuck at min, 1 = stuck at max and 0 = not stuck. |
| `abEffects` | `bool` | if the change should activate effects associated with it. If false, |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Lever](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Lever)
- Revision: `5037`
- Source update: `2020-08-24T20:55:40Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

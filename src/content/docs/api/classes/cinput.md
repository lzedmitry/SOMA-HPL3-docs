---
title: cInput
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cInput"
sourceRevision: 5018
sourceUpdated: "2020-08-24T20:48:56Z"
lastSynced: "2026-10-05T14:11:59Z"
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
| `bool` | [`cInput_BecameTriggered`](#cinput-becametriggered)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_BecameTriggered`](#cinput-becametriggered)(int alId) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_CheckForInput`](#cinput-checkforinput)() | *Undocumented in the original Wiki.* |
| `cAction` | [`cInput_CreateAction`](#cinput-createaction)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alId) | *Undocumented in the original Wiki.* |
| `void` | [`cInput_DestroyAction`](#cinput-destroyaction)([cAction](https://wiki.frictionalgames.com/page/../../cAction) @apAction) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_DoubleTriggered`](#cinput-doubletriggered)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afLimit) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_DoubleTriggered`](#cinput-doubletriggered)(int alId, float afLimit) | *Undocumented in the original Wiki.* |
| `cAction` | [`cInput_GetAction`](#cinput-getaction)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cAction` | [`cInput_GetAction`](#cinput-getaction)(int alId) | *Undocumented in the original Wiki.* |
| `iEyeTracker` | [`cInput_GetEyeTracker`](#cinput-geteyetracker)() | *Undocumented in the original Wiki.* |
| `iKeyboard` | [`cInput_GetKeyboard`](#cinput-getkeyboard)() | *Undocumented in the original Wiki.* |
| `iMouse` | [`cInput_GetMouse`](#cinput-getmouse)() | *Undocumented in the original Wiki.* |
| `iSubAction` | [`cInput_InputToSubAction`](#cinput-inputtosubaction)() | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_IsTriggered`](#cinput-istriggered)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_IsTriggered`](#cinput-istriggered)(int alId) | *Undocumented in the original Wiki.* |
| `void` | [`cInput_ResetActionsToCurrentState`](#cinput-resetactionstocurrentstate)() | *Undocumented in the original Wiki.* |
| `void` | [`cInput_Update`](#cinput-update)(float afX) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_WasTriggered`](#cinput-wastriggered)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `bool` | [`cInput_WasTriggered`](#cinput-wastriggered)(int alId) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cInput_BecameTriggered`

```cpp
bool cInput_BecameTriggered(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cInput_BecameTriggered`

```cpp
bool cInput_BecameTriggered(int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |

**Returns:** `bool`

    1. `cInput_CheckForInput`

```cpp
bool cInput_CheckForInput()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cInput_CreateAction`

```cpp
cAction@ cInput_CreateAction(const tString &in asName,
                             int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alId` | `int` | — |

**Returns:** `cAction@`

    1. `cInput_DestroyAction`

```cpp
void cInput_DestroyAction(cAction @apAction)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apAction` | `[cAction](https://wiki.frictionalgames.com/page/../../cAction)` | — |

**Returns:** `void`

    1. `cInput_DoubleTriggered`

```cpp
bool cInput_DoubleTriggered(const tString &in asName,
                            float afLimit)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afLimit` | `float` | — |

**Returns:** `bool`

    1. `cInput_DoubleTriggered`

```cpp
bool cInput_DoubleTriggered(int alId,
                            float afLimit)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |
| `afLimit` | `float` | — |

**Returns:** `bool`

    1. `cInput_GetAction`

```cpp
cAction@ cInput_GetAction(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cAction@`

    1. `cInput_GetAction`

```cpp
cAction@ cInput_GetAction(int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |

**Returns:** `cAction@`

    1. `cInput_GetEyeTracker`

```cpp
iEyeTracker@ cInput_GetEyeTracker()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `iEyeTracker@`

    1. `cInput_GetKeyboard`

```cpp
iKeyboard@ cInput_GetKeyboard()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `iKeyboard@`

    1. `cInput_GetMouse`

```cpp
iMouse@ cInput_GetMouse()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `iMouse@`

    1. `cInput_InputToSubAction`

```cpp
iSubAction@ cInput_InputToSubAction()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `iSubAction@`

    1. `cInput_IsTriggered`

```cpp
bool cInput_IsTriggered(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cInput_IsTriggered`

```cpp
bool cInput_IsTriggered(int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |

**Returns:** `bool`

    1. `cInput_ResetActionsToCurrentState`

```cpp
void cInput_ResetActionsToCurrentState()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cInput_Update`

```cpp
void cInput_Update(float afX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afX` | `float` | — |

**Returns:** `void`

    1. `cInput_WasTriggered`

```cpp
bool cInput_WasTriggered(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cInput_WasTriggered`

```cpp
bool cInput_WasTriggered(int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |

**Returns:** `bool`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cInput](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cInput)
- Revision: `5018`
- Source update: `2020-08-24T20:48:56Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

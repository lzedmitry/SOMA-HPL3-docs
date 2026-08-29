---
title: SwingDoor
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/SwingDoor"
sourceRevision: 5052
sourceUpdated: "2020-08-24T20:59:24Z"
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
| `void` | [`SwingDoor_AddDoorBodyImpulse`](#swingdoor-adddoorbodyimpulse)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afImpulseAmount) | *Undocumented in the original Wiki.* |
| `bool` | [`SwingDoor_GetBlocked`](#swingdoor-getblocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks if door is blocked |
| `bool` | [`SwingDoor_GetClosed`](#swingdoor-getclosed)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks if door is closed |
| `bool` | [`SwingDoor_GetLocked`](#swingdoor-getlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks if door is locked |
| `float` | [`SwingDoor_GetOpenAmount`](#swingdoor-getopenamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Get open amount of a door |
| `int` | [`SwingDoor_GetState`](#swingdoor-getstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks the state of the door |
| `void` | [`SwingDoor_SetBlocked`](#swingdoor-setblocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abBlocked, bool abEffects) | Blocks or unblocks a SwingDoor |
| `void` | [`SwingDoor_SetClosed`](#swingdoor-setclosed)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abClosed, bool abEffects) | Sets the close state of a SwingDoor |
| `void` | [`SwingDoor_SetDisableAutoClose`](#swingdoor-setdisableautoclose)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abDisableAutoClose) | Disables or enables the automatic close functionality of a door |
| `void` | [`SwingDoor_SetLocked`](#swingdoor-setlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLocked, bool abEffects) | Locks or unlocks a SwingDoor |
| `void` | [`SwingDoor_SetOpenAmount`](#swingdoor-setopenamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afOpenAmount) | Sets the door to a specific open state instantly |

## Function Detail
    1. `SwingDoor_AddDoorBodyImpulse`

```angelscript
void SwingDoor_AddDoorBodyImpulse(const tString &in asName,
                                  float afImpulseAmount)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afImpulseAmount` | `float` | — |

**Returns:** `void`

    1. `SwingDoor_GetBlocked`

```angelscript
bool SwingDoor_GetBlocked(const tString &in asName)
```

Checks if door is blocked.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `bool` — true if the door is blocked.

    1. `SwingDoor_GetClosed`

```angelscript
bool SwingDoor_GetClosed(const tString &in asName)
```

Checks if door is closed.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `bool` — true if the door is closed.

    1. `SwingDoor_GetLocked`

```angelscript
bool SwingDoor_GetLocked(const tString &in asName)
```

Checks if door is locked.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `bool` — true if the door is locked.

    1. `SwingDoor_GetOpenAmount`

```angelscript
float SwingDoor_GetOpenAmount(const tString &in asName)
```

Get open amount of a door

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `float` — open amount of door

    1. `SwingDoor_GetState`

```angelscript
int SwingDoor_GetState(const tString &in asName)
```

Checks the state of the door.  
0 = inbetween -1 and 1.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `int` — -1 = angle is close to 0, 1 = angle is 70% or higher of max,

    1. `SwingDoor_SetBlocked`

```angelscript
void SwingDoor_SetBlocked(const tString &in asName,
                          bool abBlocked,
                          bool abEffects)
```

Blocks or unblocks a SwingDoor. A blocked door can still be opened slightly.  
If false, the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door, wildcards (*) supported. |
| `abBlocked` | `bool` | true = block door, false = unblock door. |
| `abEffects` | `bool` | if the change should activate effects associated with it. |

**Returns:** `void`

    1. `SwingDoor_SetClosed`

```angelscript
void SwingDoor_SetClosed(const tString &in asName,
                         bool abClosed,
                         bool abEffects)
```

Sets the close state of a SwingDoor.  
If false, the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door, wildcards (*) supported. |
| `abClosed` | `bool` | true = close - false = open |
| `abEffects` | `bool` | if the change should activate effects associated with it. |

**Returns:** `void`

    1. `SwingDoor_SetDisableAutoClose`

```angelscript
void SwingDoor_SetDisableAutoClose(const tString &in asName,
                                   bool abDisableAutoClose)
```

Disables or enables the automatic close functionality of a door.  
If enabled, the door will not lose any force pushing it toward its closed position.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door, wildcards (*) supported. |
| `abDisableAutoClose` | `bool` | true = disable - false = enable |

**Returns:** `void`

    1. `SwingDoor_SetLocked`

```angelscript
void SwingDoor_SetLocked(const tString &in asName,
                         bool abLocked,
                         bool abEffects)
```

Locks or unlocks a SwingDoor  
If false, the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door, wildcards (*) supported. |
| `abLocked` | `bool` | true = lock door, false = unlock door. |
| `abEffects` | `bool` | if the change should activate effects associated with it. |

**Returns:** `void`

    1. `SwingDoor_SetOpenAmount`

```angelscript
void SwingDoor_SetOpenAmount(const tString &in asName,
                             float afOpenAmount)
```

Sets the door to a specific open state instantly.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door, wildcards (*) supported. |
| `afOpenAmount` | `float` | 0 = closed, 1 = completely open. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/SwingDoor](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/SwingDoor)
- Revision: `5052`
- Source update: `2020-08-24T20:59:24Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

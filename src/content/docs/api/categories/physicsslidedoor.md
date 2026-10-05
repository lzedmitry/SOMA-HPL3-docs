---
title: PhysicsSlideDoor
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/PhysicsSlideDoor"
sourceRevision: 5046
sourceUpdated: "2020-08-24T20:57:59Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `void` | [`PhysicsSlideDoor_AutoMoveToState`](#physicsslidedoor-automovetostate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alState) | Automove physics slide door to a state |
| `bool` | [`PhysicsSlideDoor_GetClosed`](#physicsslidedoor-getclosed)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Returns true if door is closed |
| `float` | [`PhysicsSlideDoor_GetOpenAmount`](#physicsslidedoor-getopenamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Returns the open amount of the door |
| `void` | [`PhysicsSlideDoor_SetLocked`](#physicsslidedoor-setlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLocked, bool abEffects) | Sets the physics slide door as locked or unlocked |

## Function Detail
    1. `PhysicsSlideDoor_AutoMoveToState`

```cpp
void PhysicsSlideDoor_AutoMoveToState(const tString &in asName,
                                      int alState)
```

Automove physics slide door to a state.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |
| `alState` | `int` | -1=closed, 1= open |

**Returns:** `void`

    1. `PhysicsSlideDoor_GetClosed`

```cpp
bool PhysicsSlideDoor_GetClosed(const tString &in asName)
```

Returns true if door is closed.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `bool`

    1. `PhysicsSlideDoor_GetOpenAmount`

```cpp
float PhysicsSlideDoor_GetOpenAmount(const tString &in asName)
```

Returns the open amount of the door

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `float`

    1. `PhysicsSlideDoor_SetLocked`

```cpp
void PhysicsSlideDoor_SetLocked(const tString &in asName,
                                bool abLocked,
                                bool abEffects)
```

Sets the physics slide door as locked or unlocked

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |
| `abLocked` | `bool` | true = lock the door - false = unlock the door |
| `abEffects` | `bool` | true = use effects - false = do not use effects. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/PhysicsSlideDoor](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/PhysicsSlideDoor)
- Revision: `5046`
- Source update: `2020-08-24T20:57:59Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

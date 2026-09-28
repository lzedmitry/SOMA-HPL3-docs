---
title: SlideDoor
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/SlideDoor"
sourceRevision: 5050
sourceUpdated: "2020-08-24T20:58:44Z"
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
| `float` | [`SlideDoor_GetOpenAmount`](#slidedoor-getopenamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the open amount of a SlideDoor, 0 being completely closed and 1 being completely open |
| `void` | [`SlideDoor_SetClosed`](#slidedoor-setclosed)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abClosed, bool abInstant = false) | Sets the close state of a SlideDoor |
| `void` | [`SlideDoor_SetOpenableByAgent`](#slidedoor-setopenablebyagent)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | Sets if the agents should be able to open the slide door |
| `void` | [`SlideDoor_SetOpenAmount`](#slidedoor-setopenamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afOpenAmount, bool abInstant = false) | Moves a SlideDoor to a specific open amount |

## Function Detail
    1. `SlideDoor_GetOpenAmount`

```cpp
float SlideDoor_GetOpenAmount(const tString &in asName)
```

Gets the open amount of a SlideDoor, 0 being completely closed and 1 being completely open.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |

**Returns:** `float` — open amount of the door.

    1. `SlideDoor_SetClosed`

```cpp
void SlideDoor_SetClosed(const tString &in asName,
                         bool abClosed,
                         bool abInstant = false)
```

Sets the close state of a SlideDoor. Simplified version of SlideDoor_SetOpenAmount.  
new position set instantly.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |
| `abClosed` | `bool` | true = close - false = open |
| `abInstant` | `bool` | if the door should slide to the correct state or just have the |

**Returns:** `void`

    1. `SlideDoor_SetOpenableByAgent`

```cpp
void SlideDoor_SetOpenableByAgent(const tString &in asName,
                                  bool abX)
```

Sets if the agents should be able to open the slide door.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |
| `abX` | `bool` | if possible to open or not. |

**Returns:** `void`

    1. `SlideDoor_SetOpenAmount`

```cpp
void SlideDoor_SetOpenAmount(const tString &in asName,
                             float afOpenAmount,
                             bool abInstant = false)
```

Moves a SlideDoor to a specific open amount.  
new position set instantly.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the door. |
| `afOpenAmount` | `float` | the open amount to set |
| `abInstant` | `bool` | if the door should slide to the correct state or just have the |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/SlideDoor](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/SlideDoor)
- Revision: `5050`
- Source update: `2020-08-24T20:58:44Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: LevelDoor
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/LevelDoor"
sourceRevision: 5036
sourceUpdated: "2020-08-24T20:55:29Z"
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
| `bool` | [`LevelDoor_GetLocked`](#leveldoor-getlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the lock state of a level door |
| `void` | [`LevelDoor_SetLocked`](#leveldoor-setlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abState) | Sets the lock state of a level door |

## Function Detail
    1. `LevelDoor_GetLocked`

```cpp
bool LevelDoor_GetLocked(const tString &in asName)
```

Gets the lock state of a level door

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of level door. |

**Returns:** `bool` — true = locked - false = unlocked.

    1. `LevelDoor_SetLocked`

```cpp
void LevelDoor_SetLocked(const tString &in asName,
                         bool abState)
```

Sets the lock state of a level door

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of level door. |
| `abState` | `bool` | true = locked - false = unlocked. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/LevelDoor](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/LevelDoor)
- Revision: `5036`
- Source update: `2020-08-24T20:55:29Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

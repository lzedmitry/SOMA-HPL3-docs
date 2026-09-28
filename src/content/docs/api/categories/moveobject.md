---
title: MoveObject
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/MoveObject"
sourceRevision: 6817
sourceUpdated: "2024-05-30T16:23:55Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

*Note: The official documentation for these functions had a typo where it wrongly documented the use of 'afState' in the function.*

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `void` | [`MoveObject_SetState`](#moveobject-setstate)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afState) | Sets the state of the move object |
| `void` | [`MoveObject_SetStateExt`](#moveobject-setstateext)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afState, float afAcc, float afMaxSpeed, float afSlowdownDist, bool abResetSpeed) | Sets the state of the move object |

## Function Detail
    1. `MoveObject_SetState`

```cpp
void MoveObject_SetState(const tString &in asName,
                         float afState)
```

Sets the state of the move object. This makes it move to a certain postion between  
min or max pos (or outside of that is <0 or >1).

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of move object |
| `afState` | `float` | the position of the door you want to set it to (between 0.0f and 1.0f). |

**Returns:** `void`

    1. `MoveObject_SetStateExt`

```cpp
void MoveObject_SetStateExt(const tString &in asName,
                            float afState,
                            float afAcc,
                            float afMaxSpeed,
                            float afSlowdownDist,
                            bool abResetSpeed)
```

Sets the state of the move object. This makes it move to a certain postion between  
min or max pos (or outside of that is <0 or >1).  
This will also set the speeed and acc at which the movement occurs.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of move object |
| `afState` | `float` | the position of the door you want to set it to (between 0.0f and 1.0f). |
| `afAcc` | `float` | the acceleration of the movement |
| `afMaxSpeed` | `float` | the max speed. |
| `afSlowdownDist` | `float` | the distance from the state postion that it will start slowing to a halt. |
| `abResetSpeed` | `bool` | if the previous speed should be reset. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/MoveObject](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/MoveObject)
- Revision: `6817`
- Source update: `2024-05-30T16:23:55Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

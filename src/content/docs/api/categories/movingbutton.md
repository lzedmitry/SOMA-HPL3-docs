---
title: MovingButton
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/MovingButton"
sourceRevision: 5044
sourceUpdated: "2020-08-24T20:57:30Z"
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
| `void` | [`MovingButton_Blink`](#movingbutton-blink)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Makes the MovingButton blink in accordance to how it is set up in the ent file |
| `float` | [`MovingButton_GetStateAmount`](#movingbutton-getstateamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Returns the current state of the MovingButton |
| `bool` | [`MovingButton_IsDisabled`](#movingbutton-isdisabled)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks if the MovingButton is disabled (will not light up or respond to presses) |
| `bool` | [`MovingButton_IsLocked`](#movingbutton-islocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks if the MovingButton is locked |
| `bool` | [`MovingButton_IsSwitchedOn`](#movingbutton-isswitchedon)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Returns the state of the button, on/off |
| `void` | [`MovingButton_SetCanBeSwitchedOff`](#movingbutton-setcanbeswitchedoff)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abState) | Sets if the moving button can be switched off by the player or not |
| `void` | [`MovingButton_SetCanBeSwitchedOn`](#movingbutton-setcanbeswitchedon)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abState) | Sets if the moving button can be switched on by the player or not |
| `void` | [`MovingButton_SetDisabled`](#movingbutton-setdisabled)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abState, bool abUseEffects = true) | Sets the MovingButtons disabled state |
| `void` | [`MovingButton_SetLocked`](#movingbutton-setlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abState, bool abUseEffects = true) | Sets the MovingButtons locked state |
| `void` | [`MovingButton_SetReturnToOffTime`](#movingbutton-setreturntoofftime)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afTime) | Sets the time it should take for the button to return to its off state |
| `void` | [`MovingButton_SetSwitchedOn`](#movingbutton-setswitchedon)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abState, bool abEffects) | Switches a button on/off |

## Function Detail
    1. `MovingButton_Blink`

```angelscript
void MovingButton_Blink(const tString &in asName)
```

Makes the MovingButton blink in accordance to how it is set up in the ent file.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of MovingButton. |

**Returns:** `void`

    1. `MovingButton_GetStateAmount`

```angelscript
float MovingButton_GetStateAmount(const tString &in asName)
```

Returns the current state of the MovingButton

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of MovingButton. |

**Returns:** `float`

    1. `MovingButton_IsDisabled`

```angelscript
bool MovingButton_IsDisabled(const tString &in asName)
```

Checks if the MovingButton is disabled (will not light up or respond to presses).

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of MovingButton. |

**Returns:** `bool` — true = disabled, false = enabled.

    1. `MovingButton_IsLocked`

```angelscript
bool MovingButton_IsLocked(const tString &in asName)
```

Checks if the MovingButton is locked.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of MovingButton. |

**Returns:** `bool` — true = locked, false = unlocked.

    1. `MovingButton_IsSwitchedOn`

```angelscript
bool MovingButton_IsSwitchedOn(const tString &in asName)
```

Returns the state of the button, on/off.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of button. |

**Returns:** `bool` — true = on - false = off.

    1. `MovingButton_SetCanBeSwitchedOff`

```angelscript
void MovingButton_SetCanBeSwitchedOff(const tString &in asName,
                                      bool abState)
```

Sets if the moving button can be switched off by the player or not

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of button. |
| `abState` | `bool` | true = can be switched off - false = can't be switched off. |

**Returns:** `void`

    1. `MovingButton_SetCanBeSwitchedOn`

```angelscript
void MovingButton_SetCanBeSwitchedOn(const tString &in asName,
                                     bool abState)
```

Sets if the moving button can be switched on by the player or not

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of button. |
| `abState` | `bool` | true = can be switched on - false = can't be switched on. |

**Returns:** `void`

    1. `MovingButton_SetDisabled`

```angelscript
void MovingButton_SetDisabled(const tString &in asName,
                              bool abState,
                              bool abUseEffects = true)
```

Sets the MovingButtons disabled state

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of MovingButton. |
| `abState` | `bool` | true = disabled, false = not disabled |
| `abUseEffects` | `bool` | if color should fade in or be set instantly. |

**Returns:** `void`

    1. `MovingButton_SetLocked`

```angelscript
void MovingButton_SetLocked(const tString &in asName,
                            bool abState,
                            bool abUseEffects = true)
```

Sets the MovingButtons locked state

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of MovingButton. |
| `abState` | `bool` | true = locked, false = unlocked. |
| `abUseEffects` | `bool` | if color should fade in or be set instantly. |

**Returns:** `void`

    1. `MovingButton_SetReturnToOffTime`

```angelscript
void MovingButton_SetReturnToOffTime(const tString &in asName,
                                     float afTime)
```

Sets the time it should take for the button to return to its off state.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of button. |
| `afTime` | `float` | time to return to off state. |

**Returns:** `void`

    1. `MovingButton_SetSwitchedOn`

```angelscript
void MovingButton_SetSwitchedOn(const tString &in asName,
                                bool abState,
                                bool abEffects)
```

Switches a button on/off.  
the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of button. |
| `abState` | `bool` | true = on - false = off. |
| `abEffects` | `bool` | if the change should activate effects associated with it. If false, |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/MovingButton](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/MovingButton)
- Revision: `5044`
- Source update: `2020-08-24T20:57:30Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Slide
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Slide"
sourceRevision: 5049
sourceUpdated: "2020-08-24T20:58:32Z"
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
| `void` | [`Slide_AutoMoveTo`](#slide-automoveto)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afAmount) | Auto moves the slide prop to a specific amount? |
| `bool` | [`Slide_GetLocked`](#slide-getlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Get if the slide prop is locked |
| `float` | [`Slide_GetSlideAmount`](#slide-getslideamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the slide amount of a Slide prop, 0 being at it' min position and 1 being at its max |
| `cVector3f` | [`Slide_GetSlideVel`](#slide-getslidevel)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the velocity of the slide joint |
| `void` | [`Slide_SetLocked`](#slide-setlocked)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLocked, bool abEffects) | Locks/Unlocks a slide prop |
| `void` | [`Slide_SetSlideAmount`](#slide-setslideamount)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afAmount) | Sets the slide amount of a Slide prop, 0 being at it' min position and 1 being at its max |

## Function Detail
    1. `Slide_AutoMoveTo`

```angelscript
void Slide_AutoMoveTo(const tString &in asName,
                      float afAmount)
```

Auto moves the slide prop to a specific amount?

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. |
| `afAmount` | `float` | the slide amount to set. |

**Returns:** `void`

    1. `Slide_GetLocked`

```angelscript
bool Slide_GetLocked(const tString &in asName)
```

Get if the slide prop is locked.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. |

**Returns:** `bool`

    1. `Slide_GetSlideAmount`

```angelscript
float Slide_GetSlideAmount(const tString &in asName)
```

Gets the slide amount of a Slide prop, 0 being at it' min position and 1 being at its max.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. |

**Returns:** `float` — the slide amount.

    1. `Slide_GetSlideVel`

```angelscript
cVector3f Slide_GetSlideVel(const tString &in asName)
```

Gets the velocity of the slide joint.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. |

**Returns:** `cVector3f` — the vel of the slide joint.

    1. `Slide_SetLocked`

```angelscript
void Slide_SetLocked(const tString &in asName,
                     bool abLocked,
                     bool abEffects)
```

Locks/Unlocks a slide prop.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. |
| `abLocked` | `bool` | if the slide prop should be locked or not. |
| `abEffects` | `bool` | if sounds and any other effects associated with locking/unlocking should be activated |

**Returns:** `void`

    1. `Slide_SetSlideAmount`

```angelscript
void Slide_SetSlideAmount(const tString &in asName,
                          float afAmount)
```

Sets the slide amount of a Slide prop, 0 being at it' min position and 1 being at its max.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. |
| `afAmount` | `float` | the slide amount to set. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Slide](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Slide)
- Revision: `5049`
- Source update: `2020-08-24T20:58:32Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

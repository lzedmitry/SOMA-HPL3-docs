---
title: Lamp
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Lamp"
sourceRevision: 5034
sourceUpdated: "2020-08-24T20:54:38Z"
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
| `bool` | [`Lamp_GetLit`](#lamp-getlit)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Gets the lit state of a lamp |
| `void` | [`Lamp_SetFlickerActive`](#lamp-setflickeractive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abActive) | Activates or deactivates flicker on the specified lamp(s) |
| `void` | [`Lamp_SetLit`](#lamp-setlit)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLit, bool abEffects) | Sets the lit state of a lamp |
| `void` | [`Lamp_SetupFlicker`](#lamp-setupflicker)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afMinOnTime, float afMaxOnTime, float afMinOffTime, float afMaxOffTime, bool abFade = false, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asOnSound = "", const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asOffSound = "", const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asOnPS = "", const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asOffPS = "") | Sets the properties of the flicker of a lamp |

## Function Detail
    1. `Lamp_GetLit`

```angelscript
bool Lamp_GetLit(const tString &in asName)
```

Gets the lit state of a lamp.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the lamp. |

**Returns:** `bool` — if the lamp is lit.

    1. `Lamp_SetFlickerActive`

```angelscript
void Lamp_SetFlickerActive(const tString &in asName,
                           bool abActive)
```

Activates or deactivates flicker on the specified lamp(s)

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the lamp, wildcards (*) supported. |
| `abActive` | `bool` | flicker state to set. |

**Returns:** `void`

    1. `Lamp_SetLit`

```angelscript
void Lamp_SetLit(const tString &in asName,
                 bool abLit,
                 bool abEffects)
```

Sets the lit state of a lamp.  
If false, the change will not be apparent to the player.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the lamp. |
| `abLit` | `bool` | lit state to set. |
| `abEffects` | `bool` | if the change should activate effects associated with it. |

**Returns:** `void`

    1. `Lamp_SetupFlicker`

```angelscript
void Lamp_SetupFlicker(const tString &in asName,
                       float afMinOnTime,
                       float afMaxOnTime,
                       float afMinOffTime,
                       float afMaxOffTime,
                       bool abFade = false,
                       const tString &in asOnSound = "",
                       const tString &in asOffSound = "",
                       const tString &in asOnPS = "",
                       const tString &in asOffPS = "")
```

Sets the properties of the flicker of a lamp.  
with setting the lit state of the lamp. Default = false.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the lamp, wildcards (*) supported. |
| `afMinOnTime` | `float` | The minimum time the lamp will be turned on when flickering. |
| `afMaxOnTime` | `float` | The maximum time the lamp will be turned on when flickering. |
| `afMinOffTime` | `float` | The minimum time the lamp will be turned off when flickering. |
| `afMaxOffTime` | `float` | The maximum time the lamp will be turned off when flickering. |
| `abFade` | `bool` | if the lamp should fade on or off, and use any effects associated |
| `asOnSound` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | sound to play when turned on. Default = . |
| `asOffSound` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | sound to play when turned off. Default = . |
| `asOnPS` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | particle system to create when turned on. Default = . |
| `asOffPS` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | sparticle system to create when turned off. Default = . |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Lamp](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Lamp)
- Revision: `5034`
- Source update: `2020-08-24T20:54:38Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Light
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Light"
sourceRevision: 5038
sourceUpdated: "2020-08-24T20:55:54Z"
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
| `void` | [`Light_FadeTo`](#light-fadeto)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in acColor, float afRadius, float afTime) | Fades one or more lights to a specified color and radius |
| `float` | [`Light_GetBrightness`](#light-getbrightness)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName) | Gets the brightness of a light |
| `void` | [`Light_SetBrightness`](#light-setbrightness)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, float afBrightness) | Sets the brightness of one or more lights |
| `void` | [`Light_SetCastShadows`](#light-setcastshadows)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, bool abX) | Sets the casts shadow |
| `void` | [`Light_SetCheapGobo`](#light-setcheapgobo)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, bool abX) | Sets if a cheaper version of gobo rendering should be used |
| `void` | [`Light_SetFlickerActive`](#light-setflickeractive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, bool abX) | Activates or deactivates the flicker of one or more lights |
| `void` | [`Light_SetShadowBiasMul`](#light-setshadowbiasmul)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, float afBias, float afSlopeBias) | Sets the shadow bias for one or more lights |
| `void` | [`Light_SetVisible`](#light-setvisible)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLightName, bool abVisible) | Sets the visibility of one or more lights |

## Function Detail
    1. `Light_FadeTo`

```cpp
void Light_FadeTo(const tString &in asLightName,
                  const cColor &in acColor,
                  float afRadius,
                  float afTime)
```

Fades one or more lights to a specified color and radius.

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. Can contain wildcards. |
| `acColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | color to fade to. |
| `afRadius` | `float` | radius to fade to, if lower than 0, the current radius will be used. |
| `afTime` | `float` | time to fade over. |

**Returns:** `void`

    1. `Light_GetBrightness`

```cpp
float Light_GetBrightness(const tString &in asLightName)
```

Gets the brightness of a light

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. |

**Returns:** `float` — the brightness of the light

    1. `Light_SetBrightness`

```cpp
void Light_SetBrightness(const tString &in asLightName,
                         float afBrightness)
```

Sets the brightness of one or more lights

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. Can contain wildcards. |
| `afBrightness` | `float` | the brightness to set. |

**Returns:** `void`

    1. `Light_SetCastShadows`

```cpp
void Light_SetCastShadows(const tString &in asLightName,
                          bool abX)
```

Sets the casts shadow. Used only by spotlights (for now).

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the light. Can contain wildcards. |
| `abX` | `bool` | if light should cast shadows. |

**Returns:** `void`

    1. `Light_SetCheapGobo`

```cpp
void Light_SetCheapGobo(const tString &in asLightName,
                        bool abX)
```

Sets if a cheaper version of gobo rendering should be used

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. Can contain wildcards. |
| `abX` | `bool` | if cheap version should be used, off by default |

**Returns:** `void`

    1. `Light_SetFlickerActive`

```cpp
void Light_SetFlickerActive(const tString &in asLightName,
                            bool abX)
```

Activates or deactivates the flicker of one or more lights

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. Can contain wildcards. |
| `abX` | `bool` | if flicker should be active. |

**Returns:** `void`

    1. `Light_SetShadowBiasMul`

```cpp
void Light_SetShadowBiasMul(const tString &in asLightName,
                            float afBias,
                            float afSlopeBias)
```

Sets the shadow bias for one or more lights

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. Can contain wildcards. |
| `afBias` | `float` | bias mul |
| `afSlopeBias` | `float` | slope bias mul |

**Returns:** `void`

    1. `Light_SetVisible`

```cpp
void Light_SetVisible(const tString &in asLightName,
                      bool abVisible)
```

Sets the visibility of one or more lights

| Name | Type | Description |
| --- | --- | --- |
| `asLightName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of light. Can contain wildcards. |
| `abVisible` | `bool` | if light should be visible. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Light](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Light)
- Revision: `5038`
- Source update: `2020-08-24T20:55:54Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

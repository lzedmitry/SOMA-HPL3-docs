---
title: Billboard
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Billboard"
sourceRevision: 5010
sourceUpdated: "2020-08-24T20:45:19Z"
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
| `void` | [`Billboard_SetBrightness`](#billboard-setbrightness)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBillboardName, float afBrightness) | Sets the brightness of a billboard |
| `void` | [`Billboard_SetRangeMax`](#billboard-setrangemax)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBillboardName, float afRangeStart, float afRangeEnd) | Sets the max range of a billboard, getting far away will cause the billboard to fade out |
| `void` | [`Billboard_SetRangeMin`](#billboard-setrangemin)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBillboardName, float afRangeStart, float afRangeEnd) | Sets the minimum range of a billboard, getting closer will cause the billboard to fade out |
| `void` | [`Billboard_SetReflectionVisibility`](#billboard-setreflectionvisibility)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBillboardName, bool abVisibleInReflection, bool abVisibleInWorld) | Sets whether the billboard is drawn in reflections or not, and the real world or not |
| `void` | [`Billboard_SetVisible`](#billboard-setvisible)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBillboardName, bool abVisible) | Sets if a billboard should be rendered or not |

## Function Detail
    1. `Billboard_SetBrightness`

```cpp
void Billboard_SetBrightness(const tString &in asBillboardName,
                             float afBrightness)
```

Sets the brightness of a billboard

| Name | Type | Description |
| --- | --- | --- |
| `asBillboardName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of billboard. Can contain wildcards. |
| `afBrightness` | `float` | new brightness |

**Returns:** `void`

    1. `Billboard_SetRangeMax`

```cpp
void Billboard_SetRangeMax(const tString &in asBillboardName,
                           float afRangeStart,
                           float afRangeEnd)
```

Sets the max range of a billboard, getting far away will cause the billboard to fade out

| Name | Type | Description |
| --- | --- | --- |
| `asBillboardName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of billboard. Can contain wildcards. |
| `afRangeStart` | `float` | distance the object should start to fade, -1 = no fade |
| `afRangeEnd` | `float` | distance the object fade is complete, -1 = no fade |

**Returns:** `void`

    1. `Billboard_SetRangeMin`

```cpp
void Billboard_SetRangeMin(const tString &in asBillboardName,
                           float afRangeStart,
                           float afRangeEnd)
```

Sets the minimum range of a billboard, getting closer will cause the billboard to fade out

| Name | Type | Description |
| --- | --- | --- |
| `asBillboardName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of billboard. Can contain wildcards. |
| `afRangeStart` | `float` | distance the object should start to fade, -1 = no fade |
| `afRangeEnd` | `float` | distance the object fade is complete, -1 = no fade |

**Returns:** `void`

    1. `Billboard_SetReflectionVisibility`

```cpp
void Billboard_SetReflectionVisibility(const tString &in asBillboardName,
                                       bool abVisibleInReflection,
                                       bool abVisibleInWorld)
```

Sets whether the billboard is drawn in reflections or not, and the real world or not.

| Name | Type | Description |
| --- | --- | --- |
| `asBillboardName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of billboard. Can contain wildcards. |
| `abVisibleInReflection` | `bool` | whether the entity is drawn in reflections |
| `abVisibleInWorld` | `bool` | whether the entity is drawn in the real world |

**Returns:** `void`

    1. `Billboard_SetVisible`

```cpp
void Billboard_SetVisible(const tString &in asBillboardName,
                          bool abVisible)
```

Sets if a billboard should be rendered or not.

| Name | Type | Description |
| --- | --- | --- |
| `asBillboardName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of billboard. Can contain wildcards. |
| `abVisible` | `bool` | if the billboard should be visible or not. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Billboard](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Billboard)
- Revision: `5010`
- Source update: `2020-08-24T20:45:19Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

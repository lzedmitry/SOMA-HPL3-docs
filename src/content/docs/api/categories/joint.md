---
title: Joint
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Joint"
sourceRevision: 5033
sourceUpdated: "2020-08-24T20:54:25Z"
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
| `void` | [`Joint_Break`](#joint-break)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asJointName) | Breaks the specified joint |
| `float` | [`Joint_GetForceSize`](#joint-getforcesize)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asJointName) | Gets the force magnitude applied to the specified joint |
| `bool` | [`Joint_IsBroken`](#joint-isbroken)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asJointName) | Checks if the specified joint is broken |
| `void` | [`Joint_SetBreakable`](#joint-setbreakable)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asJointName, bool abBreakable) | Sets if the joint should be breakable by force or not |

## Function Detail
    1. `Joint_Break`

```angelscript
void Joint_Break(const tString &in asJointName)
```

Breaks the specified joint.

| Name | Type | Description |
| --- | --- | --- |
| `asJointName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the joint. |

**Returns:** `void`

    1. `Joint_GetForceSize`

```angelscript
float Joint_GetForceSize(const tString &in asJointName)
```

Gets the force magnitude applied to the specified joint.

| Name | Type | Description |
| --- | --- | --- |
| `asJointName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the joint. |

**Returns:** `float` — force size

    1. `Joint_IsBroken`

```angelscript
bool Joint_IsBroken(const tString &in asJointName)
```

Checks if the specified joint is broken.

| Name | Type | Description |
| --- | --- | --- |
| `asJointName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the joint. |

**Returns:** `bool` — true if the joint is broken.

    1. `Joint_SetBreakable`

```angelscript
void Joint_SetBreakable(const tString &in asJointName,
                        bool abBreakable)
```

Sets if the joint should be breakable by force or not.

| Name | Type | Description |
| --- | --- | --- |
| `asJointName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the joint. |
| `abBreakable` | `bool` | true if the joint should be breakable, false if it shouldn't. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Joint](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Joint)
- Revision: `5033`
- Source update: `2020-08-24T20:54:25Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Body
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Body"
sourceRevision: 5011
sourceUpdated: "2020-08-24T20:45:34Z"
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
| `void` | [`Body_AddForce`](#body-addforce)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBodyName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avForce, bool abLocalSpace) | Adds force to the specified body |
| `void` | [`Body_AddImpulse`](#body-addimpulse)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBodyName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avImpulse, bool abLocalSpace) | Adds an impulse to the specified body |
| `tString` | [`Body_GetEntityName`](#body-getentityname)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBodyName) | Gets the name of the entity the body belongs to |
| `void` | [`Body_SetCollides`](#body-setcollides)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBodyName, bool abCollides) | Sets whether a body collides with other bodies or not |

## Function Detail
    1. `Body_AddForce`

```angelscript
void Body_AddForce(const tString &in asBodyName,
                   const cVector3f &in avForce,
                   bool abLocalSpace)
```

Adds force to the specified body.

| Name | Type | Description |
| --- | --- | --- |
| `asBodyName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the body. |
| `avForce` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | force to add. |
| `abLocalSpace` | `bool` | if the force is in the body's local space. |

**Returns:** `void`

    1. `Body_AddImpulse`

```angelscript
void Body_AddImpulse(const tString &in asBodyName,
                     const cVector3f &in avImpulse,
                     bool abLocalSpace)
```

Adds an impulse to the specified body.

| Name | Type | Description |
| --- | --- | --- |
| `asBodyName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the body. |
| `avImpulse` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | impulse to add. |
| `abLocalSpace` | `bool` | if the impulse is in the body's local space. |

**Returns:** `void`

    1. `Body_GetEntityName`

```angelscript
tString Body_GetEntityName(const tString &in asBodyName)
```

Gets the name of the entity the body belongs to

| Name | Type | Description |
| --- | --- | --- |
| `asBodyName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the body. |

**Returns:** `tString` — Name of the entity.

    1. `Body_SetCollides`

```angelscript
void Body_SetCollides(const tString &in asBodyName,
                      bool abCollides)
```

Sets whether a body collides with other bodies or not.

| Name | Type | Description |
| --- | --- | --- |
| `asBodyName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the body. |
| `abCollides` | `bool` | if it should collide or not. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Body](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Body)
- Revision: `5011`
- Source update: `2020-08-24T20:45:34Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: cPhysics
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cPhysics"
sourceRevision: 5020
sourceUpdated: "2020-08-24T20:50:18Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: undocumented
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
:::note[SOURCE STATUS: Undocumented]
This API page was auto-generated on the Frictional Wiki and has no written descriptions.
:::

Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `iPhysicsWorld` | [`cPhysics_CreateWorld`](#cphysics-createworld)(bool abAddSurfaceData) | *Undocumented in the original Wiki.* |
| `void` | [`cPhysics_DestroyWorld`](#cphysics-destroyworld)([iPhysicsWorld@](https://wiki.frictionalgames.com/page/../../iPhysicsWorld) apWorld) | *Undocumented in the original Wiki.* |
| `float` | [`cPhysics_GetImpactDuration`](#cphysics-getimpactduration)() | *Undocumented in the original Wiki.* |
| `int` | [`cPhysics_GetMaxImpacts`](#cphysics-getmaximpacts)() | *Undocumented in the original Wiki.* |
| `void` | [`cPhysics_SetImpactDuration`](#cphysics-setimpactduration)(float afX) | *Undocumented in the original Wiki.* |
| `void` | [`cPhysics_SetMaxImpacts`](#cphysics-setmaximpacts)(int alX) | *Undocumented in the original Wiki.* |
| `iPhysicsBody` | [`cPhysics_ToBody`](#cphysics-tobody)([iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D) apEntity) | *Undocumented in the original Wiki.* |
| `iPhysicsJointBall` | [`cPhysics_ToJointBall`](#cphysics-tojointball)([iPhysicsJoint@](https://wiki.frictionalgames.com/page/../../iPhysicsJoint) apJoint) | *Undocumented in the original Wiki.* |
| `iPhysicsJointHinge` | [`cPhysics_ToJointHinge`](#cphysics-tojointhinge)([iPhysicsJoint@](https://wiki.frictionalgames.com/page/../../iPhysicsJoint) apJoint) | *Undocumented in the original Wiki.* |
| `iPhysicsJointSlider` | [`cPhysics_ToJointSlider`](#cphysics-tojointslider)([iPhysicsJoint@](https://wiki.frictionalgames.com/page/../../iPhysicsJoint) apJoint) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cPhysics_CreateWorld`

```cpp
iPhysicsWorld@ cPhysics_CreateWorld(bool abAddSurfaceData)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `abAddSurfaceData` | `bool` | — |

**Returns:** `iPhysicsWorld@`

    1. `cPhysics_DestroyWorld`

```cpp
void cPhysics_DestroyWorld(iPhysicsWorld@ apWorld)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apWorld` | `[iPhysicsWorld@](https://wiki.frictionalgames.com/page/../../iPhysicsWorld)` | — |

**Returns:** `void`

    1. `cPhysics_GetImpactDuration`

```cpp
float cPhysics_GetImpactDuration()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cPhysics_GetMaxImpacts`

```cpp
int cPhysics_GetMaxImpacts()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `int`

    1. `cPhysics_SetImpactDuration`

```cpp
void cPhysics_SetImpactDuration(float afX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afX` | `float` | — |

**Returns:** `void`

    1. `cPhysics_SetMaxImpacts`

```cpp
void cPhysics_SetMaxImpacts(int alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alX` | `int` | — |

**Returns:** `void`

    1. `cPhysics_ToBody`

```cpp
iPhysicsBody@ cPhysics_ToBody(iEntity3D@ apEntity)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEntity` | `[iEntity3D@](https://wiki.frictionalgames.com/page/../../iEntity3D)` | — |

**Returns:** `iPhysicsBody@`

    1. `cPhysics_ToJointBall`

```cpp
iPhysicsJointBall@ cPhysics_ToJointBall(iPhysicsJoint@ apJoint)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apJoint` | `[iPhysicsJoint@](https://wiki.frictionalgames.com/page/../../iPhysicsJoint)` | — |

**Returns:** `iPhysicsJointBall@`

    1. `cPhysics_ToJointHinge`

```cpp
iPhysicsJointHinge@ cPhysics_ToJointHinge(iPhysicsJoint@ apJoint)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apJoint` | `[iPhysicsJoint@](https://wiki.frictionalgames.com/page/../../iPhysicsJoint)` | — |

**Returns:** `iPhysicsJointHinge@`

    1. `cPhysics_ToJointSlider`

```cpp
iPhysicsJointSlider@ cPhysics_ToJointSlider(iPhysicsJoint@ apJoint)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apJoint` | `[iPhysicsJoint@](https://wiki.frictionalgames.com/page/../../iPhysicsJoint)` | — |

**Returns:** `iPhysicsJointSlider@`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cPhysics](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cPhysics)
- Revision: `5020`
- Source update: `2020-08-24T20:50:18Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

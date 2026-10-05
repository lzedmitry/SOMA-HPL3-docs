---
title: cSubMesh
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cSubMesh"
sourceRevision: 3720
sourceUpdated: "2020-08-06T14:21:16Z"
lastSynced: "2026-10-05T14:11:59Z"
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

## Fields
cSubMesh has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | Compile |   |   |
| [
```
cMeshCollider@
```
](https://wiki.frictionalgames.com/page/../cMeshCollider) | CreateCollider | [
```
eCollideShapeType aType
```
](https://wiki.frictionalgames.com/page/../eCollideShapeType) |   |
| [
```
iCollideShape@
```
](https://wiki.frictionalgames.com/page/../iCollideShape) | CreateCollideShape | [
```
iPhysicsWorld@ apWorld
```
](https://wiki.frictionalgames.com/page/../iPhysicsWorld) |   |
| [
```
cMeshCollider@
```
](https://wiki.frictionalgames.com/page/../cMeshCollider) | GetCollider | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetColliderNum |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetLocalTransform |   |   |
| [
```
cMaterial@
```
](https://wiki.frictionalgames.com/page/../cMaterial) | GetMaterial |   |   |
| 
```
void
```
 | GetMaterialName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetMaterialName |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetModelScale |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
iVertexBuffer@
```
](https://wiki.frictionalgames.com/page/../iVertexBuffer) | GetVertexBuffer |   |   |
| 
```
bool
```
 | IsCollideShape |   |   |
| 
```
void
```
 | SetIsCollideShape | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetLocalTransform | [
```
const cMatrixf &in a_mtxTrans
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetMaterial | [
```
cMaterial@ apMaterial
```
](https://wiki.frictionalgames.com/page/../cMaterial) |   |
| 
```
void
```
 | SetVertexBuffer | [
```
iVertexBuffer@ apVtxBuffer
```
](https://wiki.frictionalgames.com/page/../iVertexBuffer) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cSubMesh](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cSubMesh)
- Revision: `3720`
- Source update: `2020-08-06T14:21:16Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

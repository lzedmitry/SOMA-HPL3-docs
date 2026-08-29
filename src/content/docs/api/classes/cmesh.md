---
title: cMesh
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cMesh"
sourceRevision: 3677
sourceUpdated: "2020-08-06T14:11:09Z"
lastSynced: "2026-08-28T18:40:04Z"
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
cMesh has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddAnimation | [
```
cAnimation@ apAnimation
```
](https://wiki.frictionalgames.com/page/../cAnimation) |   |
| 
```
void
```
 | AddNode | [
```
cNode3D@ apNode
```
](https://wiki.frictionalgames.com/page/../cNode3D) |   |
| 
```
void
```
 | ClearAnimations | 
```
bool abDeleteAll
```
 |   |
| 
```
void
```
 | CompileBonesAndSubMeshes |   |   |
| [
```
cSubMesh@
```
](https://wiki.frictionalgames.com/page/../cSubMesh) | CreateSubMesh | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cAnimation@
```
](https://wiki.frictionalgames.com/page/../cAnimation) | GetAnimation | 
```
int alIndex
```
 |   |
| [
```
cAnimation@
```
](https://wiki.frictionalgames.com/page/../cAnimation) | GetAnimationFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetAnimationIndex | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetAnimationNum |   |   |
| 
```
float
```
 | GetBoneBoundingRadius | 
```
int alIdx
```
 |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetNode | 
```
int alIdx
```
 |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetNodeByName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetNodeNum |   |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetRootNode |   |   |
| [
```
cSkeleton@
```
](https://wiki.frictionalgames.com/page/../cSkeleton) | GetSkeleton |   |   |
| [
```
cSubMesh@
```
](https://wiki.frictionalgames.com/page/../cSubMesh) | GetSubMesh | 
```
uint alIdx
```
 |   |
| 
```
int
```
 | GetSubMeshIndex | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cSubMesh@
```
](https://wiki.frictionalgames.com/page/../cSubMesh) | GetSubMeshName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetSubMeshNum |   |   |
| 
```
int
```
 | GetTriangleCount |   |   |
| 
```
void
```
 | SetSkeleton | [
```
cSkeleton@ apSkeleton
```
](https://wiki.frictionalgames.com/page/../cSkeleton) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cMesh](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cMesh)
- Revision: `3677`
- Source update: `2020-08-06T14:11:09Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

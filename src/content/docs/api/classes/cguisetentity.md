---
title: cGuiSetEntity
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cGuiSetEntity"
sourceRevision: 3574
sourceUpdated: "2020-08-06T13:34:45Z"
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
cGuiSetEntity has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddChild | [
```
iEntity3D@ apEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D) |   |
| [
```
cBoundingVolume@+
```
](https://wiki.frictionalgames.com/page/../cBoundingVolume) | GetBoundingVolume |   |   |
| [
```
cEntity3DIterator@
```
](https://wiki.frictionalgames.com/page/../cEntity3DIterator) | GetChildIterator |   |   |
| [
```
iEntity3D@
```
](https://wiki.frictionalgames.com/page/../iEntity3D) | GetEntityParent |   |   |
| [
```
eEntityType
```
](https://wiki.frictionalgames.com/page/../eEntityType) | GetEntityType |   |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | GetID |   |   |
| [
```
cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetLocalMatrix |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLocalPosition |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
bool
```
 | GetScriptableIsSaved |   |   |
| 
```
int
```
 | GetTransformUpdateCount |   |   |
| 
```
int
```
 | GetUniqueID |   |   |
| [
```
cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetWorldMatrix |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetWorldPosition |   |   |
| 
```
bool
```
 | HasParent |   |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsChild | [
```
iEntity3D@ apEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D) |   |
| 
```
void
```
 | RemoveChild | [
```
iEntity3D@ apEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D) |   |
| 
```
void
```
 | SetActive | 
```
bool abActive
```
 |   |
| 
```
void
```
 | SetMatrix | [
```
const cMatrixf &in a_mtxTransform
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetPosition | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetScriptableIsSaved | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetWorldMatrix | [
```
const cMatrixf &in a_mtxWorldTransform
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetWorldPosition | [
```
const cVector3f &in avWorldPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | UpdateLogic | 
```
float afTimeStep
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cGuiSetEntity](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cGuiSetEntity)
- Revision: `3574`
- Source update: `2020-08-06T13:34:45Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

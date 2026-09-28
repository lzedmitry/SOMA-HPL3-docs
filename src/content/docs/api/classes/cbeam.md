---
title: cBeam
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cBeam"
sourceRevision: 3529
sourceUpdated: "2020-08-06T13:20:30Z"
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

## Fields
cBeam has no public fields.

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
| 
```
bool
```
 | CollidesWithBV | [
```
cBoundingVolume@+ apBV
```
](https://wiki.frictionalgames.com/page/../cBoundingVolume) |   |
| 
```
bool
```
 | CollidesWithFrustum | [
```
cFrustum@ apFrustum
```
](https://wiki.frictionalgames.com/page/../cFrustum) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetAxis |   |   |
| [
```
cBoundingVolume@+
```
](https://wiki.frictionalgames.com/page/../cBoundingVolume) | GetBoundingVolume |   |   |
| 
```
float
```
 | GetBrightness |   |   |
| [
```
cEntity3DIterator@
```
](https://wiki.frictionalgames.com/page/../cEntity3DIterator) | GetChildIterator |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetColor |   |   |
| 
```
float
```
 | GetCoverageAmount |   |   |
| [
```
cBeamEnd@
```
](https://wiki.frictionalgames.com/page/../cBeamEnd) | GetEnd |   |   |
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
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetIlluminationColor |   |   |
| 
```
float
```
 | GetLiquidAmount |   |   |
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
cMaterial@
```
](https://wiki.frictionalgames.com/page/../cMaterial) | GetMaterial |   |   |
| 
```
int
```
 | GetMatrixUpdateCount |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetMidPosition |   |   |
| 
```
bool
```
 | GetMultiplyAlphaWithColor |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
cBoundingVolume@+
```
](https://wiki.frictionalgames.com/page/../cBoundingVolume) | GetRenderBV |   |   |
| 
```
bool
```
 | GetRenderFlagBit | 
```
int alFlagBit
```
 |   |
| 
```
int
```
 | GetRenderFlags |   |   |
| 
```
int
```
 | GetRenderFrameCount |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetRenderName |   |   |
| [
```
eRenderableType
```
](https://wiki.frictionalgames.com/page/../eRenderableType) | GetRenderType |   |   |
| 
```
bool
```
 | GetScriptableIsSaved |   |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetSize |   |   |
| 
```
bool
```
 | GetTileHeight |   |   |
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
iVertexBuffer@
```
](https://wiki.frictionalgames.com/page/../iVertexBuffer) | GetVertexBuffer |   |   |
| 
```
bool
```
 | GetVisibleVar |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetWorldCenterPosition |   |   |
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
bool
```
 | IsOccluder |   |   |
| 
```
bool
```
 | IsStatic |   |   |
| 
```
bool
```
 | IsVisible |   |   |
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
 | SetBrightness | 
```
float afBrightness
```
 |   |
| 
```
void
```
 | SetColor | [
```
const cColor& aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetCoverageAmount | 
```
float afX
```
 |   |
| 
```
void
```
 | SetIlluminationColor | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetLiquidAmount | 
```
float afX
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
 | SetMultiplyAlphaWithColor | 
```
bool abX
```
 |   |
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
 | SetRenderFlagBit | 
```
int alFlagBit
```
,  

```
bool abSet
```
 |   |
| 
```
void
```
 | SetRenderFrameCount | 
```
int alCount
```
 |   |
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
 | SetSize | [
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetTileHeight | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetVisible | 
```
bool abVisible
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
| 
```
void
```
 | UseAutomaticLiquidAmount | 
```
float afTime = 0
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cBeam](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cBeam)
- Revision: `3529`
- Source update: `2020-08-06T13:20:30Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

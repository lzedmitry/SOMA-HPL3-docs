---
title: cForceField
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cForceField"
sourceRevision: 3561
sourceUpdated: "2020-08-06T13:30:52Z"
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
cForceField has no public fields.

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
| 
```
void
```
 | FadeOut | 
```
float afTime
```
 |   |
| 
```
void
```
 | FadeTo | 
```
float afAmount
```
,  

```
float afTime
```
 |   |
| 
```
bool
```
 | GetAutoRemove |   |   |
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
| 
```
float
```
 | GetCoverageAmount |   |   |
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
| 
```
float
```
 | GetFalloffStartRadius |   |   |
| 
```
float
```
 | GetFinalFalloffStartRadius |   |   |
| 
```
float
```
 | GetFinalForce |   |   |
| 
```
float
```
 | GetFinalFreq |   |   |
| 
```
float
```
 | GetFinalRadius |   |   |
| 
```
float
```
 | GetForce |   |   |
| 
```
float
```
 | GetFreq |   |   |
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
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
bool
```
 | GetPulsateActive |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetPulsateDecSpeed |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetPulsateForceMulMax |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetPulsateForceMulMin |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetPulsateIncSpeed |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetPulsateRadiusMulMax |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetPulsateRadiusMulMin |   |   |
| 
```
float
```
 | GetRadius |   |   |
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
| 
```
float
```
 | GetT |   |   |
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
 | SetAutoRemove | 
```
bool abX
```
 |   |
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
 | SetFalloffStartRadius | 
```
float afX
```
 |   |
| 
```
void
```
 | SetForce | 
```
float afX
```
 |   |
| 
```
void
```
 | SetFreq | 
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
 | SetPulsateActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetPulsateDecSpeed | [
```
const cVector2f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetPulsateForceMulMax | [
```
const cVector2f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetPulsateForceMulMin | [
```
const cVector2f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetPulsateIncSpeed | [
```
const cVector2f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetPulsateRadiusMulMax | [
```
const cVector2f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetPulsateRadiusMulMin | [
```
const cVector2f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetRadius | 
```
float afX
```
 |   |
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cForceField](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cForceField)
- Revision: `3561`
- Source update: `2020-08-06T13:30:52Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

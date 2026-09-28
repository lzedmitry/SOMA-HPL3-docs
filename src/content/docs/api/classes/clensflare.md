---
title: cLensFlare
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLensFlare"
sourceRevision: 3597
sourceUpdated: "2020-08-06T13:43:57Z"
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
cLensFlare has no public fields.

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
 | DisableRangeMax |   |   |
| 
```
void
```
 | DisableRangeMin |   |   |
| 
```
void
```
 | FadeIn | 
```
float afTime
```
 |   |
| 
```
void
```
 | FadeOut | 
```
float afTime
```
 |   |
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
| [
```
eLensFlareType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType) | GetFirstActiveType |   |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | GetFlareColor | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType) |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetFlareSize | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetFlareSourceSize |   |   |
| 
```
float
```
 | GetGlareBrightness |   |   |
| 
```
float
```
 | GetGlareFieldOfView |   |   |
| 
```
float
```
 | GetGlareRangeMaxEnd |   |   |
| 
```
float
```
 | GetGlareRangeMaxStart |   |   |
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
 | GetInnerFieldOfView |   |   |
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
| 
```
int
```
 | GetMultiIrisCount |   |   |
| 
```
int
```
 | GetMultiIrisSeed |   |   |
| [
```
cVector2l
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetMultiIrisTextureAtlasGrid |   |   |
| 
```
bool
```
 | GetMultiplyGlareWithMultiIris |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
float
```
 | GetOuterFieldOfView |   |   |
| 
```
float
```
 | GetRangeMaxEnd |   |   |
| 
```
float
```
 | GetRangeMaxStart |   |   |
| 
```
float
```
 | GetRangeMinEnd |   |   |
| 
```
float
```
 | GetRangeMinStart |   |   |
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
bool
```
 | GetShrinkWhenOccluded |   |   |
| 
```
float
```
 | GetSizeChangeBasedOnDistance |   |   |
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
| 
```
bool
```
 | GetUseParentMeshForOcclusion |   |   |
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
 | IsFlareActive | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType) |   |
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
 | SetAsPointLight |   |   |
| 
```
void
```
 | SetBrightness | 
```
float afX
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
 | SetFlareActive | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType),  

```
bool abValue
```
 |   |
| 
```
void
```
 | SetFlareColor | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType),  
[
```
cColor aValue
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetFlareSize | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType),  
[
```
cVector2f avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetFlareSourceSize | [
```
cVector3f avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetGlareBrightness | 
```
float afBrightness
```
 |   |
| 
```
void
```
 | SetGlareFieldOfView | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetGlareRange | 
```
float afRangeMaxStart
```
,  

```
float afRangeMaxEnd
```
 |   |
| 
```
void
```
 | SetGlareStareAt | 
```
float afGlare
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
 | SetInnerFieldOfView | 
```
float afAngle
```
 |   |
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
 | SetMaterial | [
```
eLensFlareType aType
```
](https://wiki.frictionalgames.com/page/../eLensFlareType),  
[
```
cMaterial@ apMaterial
```
](https://wiki.frictionalgames.com/page/../cMaterial) |   |
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
 | SetMultiIrisCount | 
```
int alCount
```
 |   |
| 
```
void
```
 | SetMultiIrisSeed | 
```
int alSeed
```
 |   |
| 
```
void
```
 | SetMultiIrisTextureAtlasGrid | [
```
cVector2l avMultiIrisGrid
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| 
```
void
```
 | SetMultiplyGlareWithMultiIris | 
```
bool abValue
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
 | SetOuterFieldOfView | 
```
float afAngle
```
 |   |
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
 | SetRangeMax | 
```
float afRangeMaxStart
```
,  

```
float afRangeMaxEnd
```
 |   |
| 
```
void
```
 | SetRangeMin | 
```
float afRangeMinStart
```
,  

```
float afRangeMinEnd
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
 | SetShrinkWhenOccluded | 
```
bool abValue
```
 |   |
| 
```
void
```
 | SetSizeChangeBasedOnDistance | 
```
float afPercent
```
 |   |
| 
```
void
```
 | SetUseParentMeshForOcclusion | 
```
bool abValue
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLensFlare](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLensFlare)
- Revision: `3597`
- Source update: `2020-08-06T13:43:57Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: iLight
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iLight"
sourceRevision: 3898
sourceUpdated: "2020-08-06T15:02:07Z"
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
iLight has no public fields.

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
void
```
 | AttachBillboard | [
```
cBillboard@ apBillboard
```
](https://wiki.frictionalgames.com/page/../cBillboard),  
[
```
const cColor& aBaseColor
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afBaseBrightness
```
 |   |
| 
```
void
```
 | AttachParticleSystem | [
```
cParticleSystem@ apPS
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) |   |
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
 | FadeTo | [
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afRadius
```
,  

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
| 
```
bool
```
 | GetCastShadows |   |   |
| 
```
bool
```
 | GetCastTerrainShadow |   |   |
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
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetDefaultDiffuseColor |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetDestColor |   |   |
| 
```
float
```
 | GetDestRadius |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetDiffuseColor |   |   |
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
 | GetFalloffPow |   |   |
| 
```
bool
```
 | GetFlickerActive |   |   |
| 
```
bool
```
 | GetFlickerFade |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetFlickerOffColor |   |   |
| 
```
float
```
 | GetFlickerOffFadeMaxLength |   |   |
| 
```
float
```
 | GetFlickerOffFadeMinLength |   |   |
| 
```
float
```
 | GetFlickerOffMaxLength |   |   |
| 
```
float
```
 | GetFlickerOffMinLength |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetFlickerOffPS |   |   |
| 
```
float
```
 | GetFlickerOffRadius |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetFlickerOffSound |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetFlickerOnColor |   |   |
| 
```
float
```
 | GetFlickerOnFadeMaxLength |   |   |
| 
```
float
```
 | GetFlickerOnFadeMinLength |   |   |
| 
```
float
```
 | GetFlickerOnMaxLength |   |   |
| 
```
float
```
 | GetFlickerOnMinLength |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetFlickerOnPS |   |   |
| 
```
float
```
 | GetFlickerOnRadius |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetFlickerOnSound |   |   |
| 
```
float
```
 | GetGoboAnimFrameTime |   |   |
| [
```
eTextureAnimMode
```
](https://wiki.frictionalgames.com/page/../eTextureAnimMode) | GetGoboAnimMode |   |   |
| 
```
float
```
 | GetGoboAnimStartTime |   |   |
| 
```
int
```
 | GetGoboNextFrame |   |   |
| [
```
iTexture@
```
](https://wiki.frictionalgames.com/page/../iTexture) | GetGoboTexture |   |   |
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
| [
```
eLightType
```
](https://wiki.frictionalgames.com/page/../eLightType) | GetLightType |   |   |
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
cLightMaskBox@
```
](https://wiki.frictionalgames.com/page/../cLightMaskBox) | GetMask |   |   |
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
 | GetOcclusionCullShadowCasters |   |   |
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
int
```
 | GetShadowCastersAffected |   |   |
| 
```
float
```
 | GetShadowMapBiasMul |   |   |
| 
```
float
```
 | GetShadowMapBlurAmount |   |   |
| [
```
eShadowMapResolution
```
](https://wiki.frictionalgames.com/page/../eShadowMapResolution) | GetShadowMapResolution |   |   |
| 
```
float
```
 | GetShadowMapSlopeScaleBiasMul |   |   |
| 
```
float
```
 | GetSourceRadius |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetSpecularColor |   |   |
| 
```
int
```
 | GetTransformUpdateCount |   |   |
| 
```
float
```
 | GetTranslucency |   |   |
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
 | IsFading |   |   |
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
 | RemoveBillboard | [
```
cBillboard@ apBillboard
```
](https://wiki.frictionalgames.com/page/../cBillboard) |   |
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
 | RemoveParticleSystem | [
```
cParticleSystem@ apPS
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) |   |
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
float afX
```
 |   |
| 
```
void
```
 | SetCastShadows | 
```
bool afX
```
 |   |
| 
```
void
```
 | SetCastTerrainShadow | 
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
 | SetDefaultDiffuseColor | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetDiffuseColor | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetFalloffPow | 
```
float afX
```
 |   |
| 
```
void
```
 | SetFlicker | [
```
const cColor &in aOffCol
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afOffRadius
```
,  

```
float afOnMinLength
```
,  

```
float afOnMaxLength
```
,  
[
```
const tString& asOnSound
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asOnPS
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afOffMinLength
```
,  

```
float afOffMaxLength
```
,  
[
```
const tString& asOffSound
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asOffPS
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abFade
```
,  

```
float afOnFadeMinLength
```
,  

```
float afOnFadeMaxLength
```
,  

```
float afOffFadeMinLength
```
,  

```
float afOffFadeMaxLength
```
 |   |
| 
```
void
```
 | SetFlickerActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetGoboAnimFrameTime | 
```
float afX
```
 |   |
| 
```
void
```
 | SetGoboAnimMode | [
```
eTextureAnimMode aMode
```
](https://wiki.frictionalgames.com/page/../eTextureAnimMode) |   |
| 
```
void
```
 | SetGoboAnimStartTime | 
```
float afX
```
 |   |
| 
```
void
```
 | SetGoboTexture | [
```
iTexture@ apTexture
```
](https://wiki.frictionalgames.com/page/../iTexture) |   |
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
 | SetMask | [
```
cLightMaskBox@ apMask
```
](https://wiki.frictionalgames.com/page/../cLightMaskBox) |   |
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
 | SetOcclusionCullShadowCasters | 
```
bool abX
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
 | SetShadowCastersAffected | 
```
int alX
```
 |   |
| 
```
void
```
 | SetShadowMapBiasMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetShadowMapBlurAmount | 
```
float afX
```
 |   |
| 
```
void
```
 | SetShadowMapResolution | [
```
eShadowMapResolution aQuality
```
](https://wiki.frictionalgames.com/page/../eShadowMapResolution) |   |
| 
```
void
```
 | SetShadowMapSlopeScaleBiasMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSourceRadius | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpecularColor | [
```
cColor aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetTranslucency | 
```
float afX
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
 | StopFading |   |   |
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iLight](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iLight)
- Revision: `3898`
- Source update: `2020-08-06T15:02:07Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

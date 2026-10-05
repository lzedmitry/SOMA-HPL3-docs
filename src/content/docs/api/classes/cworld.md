---
title: cWorld
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cWorld"
sourceRevision: 3757
sourceUpdated: "2020-08-06T14:31:38Z"
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
cWorld has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddBillboardToGroup | [
```
cBillboard@ apObject
```
](https://wiki.frictionalgames.com/page/../cBillboard),  
[
```
cBillboardGroup@ apGroup
```
](https://wiki.frictionalgames.com/page/../cBillboardGroup) |   |
| 
```
void
```
 | Compile | 
```
bool abCalcPhysicsWorldSize
```
 |   |
| [
```
cBeam@
```
](https://wiki.frictionalgames.com/page/../cBeam) | CreateBeam | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateBeamID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cBillboard@
```
](https://wiki.frictionalgames.com/page/../cBillboard) | CreateBillboard | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
eBillboardType aType
```
](https://wiki.frictionalgames.com/page/../eBillboardType),  
[
```
const tString &in asMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cBillboardGroup@
```
](https://wiki.frictionalgames.com/page/../cBillboardGroup) | CreateBillboardGroup | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateBillboardGroupID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateBillboardID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
eBillboardType aType
```
](https://wiki.frictionalgames.com/page/../eBillboardType),  
[
```
const tString &in asMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cClothEntity@
```
](https://wiki.frictionalgames.com/page/../cClothEntity) | CreateClothEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
iPhysicsCloth@ apCloth
```
](https://wiki.frictionalgames.com/page/../iPhysicsCloth),  
[
```
const tString &in asMaterial = ""
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateClothEntityID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
iPhysicsCloth@ apCloth
```
](https://wiki.frictionalgames.com/page/../iPhysicsCloth),  
[
```
const tString &in asMaterial = ""
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cExposureArea@
```
](https://wiki.frictionalgames.com/page/../cExposureArea) | CreateExposureArea | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateExposureAreaID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cFogArea@
```
](https://wiki.frictionalgames.com/page/../cFogArea) | CreateFogArea | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateFogAreaID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cForceField@
```
](https://wiki.frictionalgames.com/page/../cForceField) | CreateForceField | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abAutoRemove
```
,  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateForceFieldID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abAutoRemove
```
,  

```
bool abStatic
```
 |   |
| [
```
cGuiSetEntity@
```
](https://wiki.frictionalgames.com/page/../cGuiSetEntity) | CreateGuiSetEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
cGuiSet@ apSet
```
](https://wiki.frictionalgames.com/page/../cGuiSet),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateGuiSetEntityID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
cGuiSet@ apSet
```
](https://wiki.frictionalgames.com/page/../cGuiSet),  

```
bool abStatic
```
 |   |
| [
```
cLensFlare@
```
](https://wiki.frictionalgames.com/page/../cLensFlare) | CreateLensFlare | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tString& asMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateLensFlareID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tString& asMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cLightBox@
```
](https://wiki.frictionalgames.com/page/../cLightBox) | CreateLightBox | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateLightBoxID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cLightPoint@
```
](https://wiki.frictionalgames.com/page/../cLightPoint) | CreateLightPoint | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asGobo
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateLightPointID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asGobo
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cLightSpot@
```
](https://wiki.frictionalgames.com/page/../cLightSpot) | CreateLightSpot | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asGobo
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateLightSpotID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asGobo
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abStatic
```
 |   |
| [
```
cMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cMeshEntity) | CreateMeshEntity | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
cMesh@ apMesh
```
](https://wiki.frictionalgames.com/page/../cMesh),  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateMeshEntityID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
cMesh@ apMesh
```
](https://wiki.frictionalgames.com/page/../cMesh),  

```
bool abStatic
```
 |   |
| [
```
cParticleSystem@
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) | CreateParticleSystem | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asType
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abRemoveWhenDead
```
,  

```
bool abStatic
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateParticleSystemID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asType
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abRemoveWhenDead
```
,  

```
bool abStatic
```
 |   |
| [
```
iRopeEntity@
```
](https://wiki.frictionalgames.com/page/../iRopeEntity) | CreateRopeEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
eRopeType aRopeType
```
](https://wiki.frictionalgames.com/page/../eRopeType),  
[
```
iPhysicsRope@ apRope
```
](https://wiki.frictionalgames.com/page/../iPhysicsRope),  

```
int alMaxSegments
```
,  

```
int alRingSegments = 3
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateRopeEntityID | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
eRopeType aRopeType
```
](https://wiki.frictionalgames.com/page/../eRopeType),  
[
```
iPhysicsRope@ apRope
```
](https://wiki.frictionalgames.com/page/../iPhysicsRope),  

```
int alMaxSegments
```
,  

```
int alRingSegments = 3
```
 |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | CreateSoundEntity | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asSoundDataFile
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenOver
```
 |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | CreateSoundEntityEx | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asSoundDataFile
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenOver
```
,  

```
bool abNonBlockLoad
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateSoundEntityExID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asSoundDataFile
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenOver
```
,  

```
bool abNonBlockLoad
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | CreateSoundEntityID | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asSoundDataFile
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenOver
```
 |   |
| 
```
void
```
 | DestroyAllParticleSystems |   |   |
| 
```
void
```
 | DestroyAllSoundEntities |   |   |
| 
```
void
```
 | DestroyBeam | [
```
cBeam@ apObject
```
](https://wiki.frictionalgames.com/page/../cBeam) |   |
| 
```
void
```
 | DestroyBillboard | [
```
cBillboard@ apObject
```
](https://wiki.frictionalgames.com/page/../cBillboard) |   |
| 
```
void
```
 | DestroyBillboardGroup | [
```
cBillboardGroup@ apObject
```
](https://wiki.frictionalgames.com/page/../cBillboardGroup) |   |
| 
```
void
```
 | DestroyClothEntity | [
```
cClothEntity@ apCloth
```
](https://wiki.frictionalgames.com/page/../cClothEntity) |   |
| 
```
void
```
 | DestroyExposureArea | [
```
cExposureArea@ apExposureArea
```
](https://wiki.frictionalgames.com/page/../cExposureArea) |   |
| 
```
void
```
 | DestroyFogArea | [
```
cFogArea@ apFogArea
```
](https://wiki.frictionalgames.com/page/../cFogArea) |   |
| 
```
void
```
 | DestroyForceField | [
```
cForceField@ apForce
```
](https://wiki.frictionalgames.com/page/../cForceField) |   |
| 
```
void
```
 | DestroyGuiSetEntity | [
```
cGuiSetEntity@ apObject
```
](https://wiki.frictionalgames.com/page/../cGuiSetEntity) |   |
| 
```
void
```
 | DestroyLensFlare | [
```
cLensFlare@ apObject
```
](https://wiki.frictionalgames.com/page/../cLensFlare) |   |
| 
```
void
```
 | DestroyLight | [
```
iLight@ apLight
```
](https://wiki.frictionalgames.com/page/../iLight) |   |
| 
```
void
```
 | DestroyMeshEntity | [
```
cMeshEntity@ apMesh
```
](https://wiki.frictionalgames.com/page/../cMeshEntity) |   |
| 
```
void
```
 | DestroyParticleSystem | [
```
cParticleSystem@ apPS
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) |   |
| 
```
void
```
 | DestroyRopeEntity | [
```
iRopeEntity@ apRope
```
](https://wiki.frictionalgames.com/page/../iRopeEntity) |   |
| 
```
void
```
 | DestroySoundEntity | [
```
cSoundEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) |   |
| 
```
void
```
 | FadeGradingTexture | [
```
const tString &in asTexture
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
 |   |
| 
```
void
```
 | FadeInIrradianceSet | [
```
const tString &in asSetName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
 |   |
| 
```
void
```
 | FadeToneMappingExposure | 
```
float afX
```
,  

```
float afTime
```
 |   |
| 
```
void
```
 | FadeToneMappingWhiteCut | 
```
float afX
```
,  

```
float afTime
```
 |   |
| [
```
cBeam@
```
](https://wiki.frictionalgames.com/page/../cBeam) | GetBeam | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cBeam@
```
](https://wiki.frictionalgames.com/page/../cBeam) | GetBeamFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cBeamIterator@
```
](https://wiki.frictionalgames.com/page/../cBeamIterator) | GetBeamIterator |   |   |
| [
```
cBillboard@
```
](https://wiki.frictionalgames.com/page/../cBillboard) | GetBillboard | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cBillboard@
```
](https://wiki.frictionalgames.com/page/../cBillboard) | GetBillboardFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cBillboardGroup@
```
](https://wiki.frictionalgames.com/page/../cBillboardGroup) | GetBillboardGroup | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cBillboardGroup@
```
](https://wiki.frictionalgames.com/page/../cBillboardGroup) | GetBillboardGroupFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cBillboardGroupIterator@
```
](https://wiki.frictionalgames.com/page/../cBillboardGroupIterator) | GetBillboardGroupIterator |   |   |
| [
```
cBillboardIterator@
```
](https://wiki.frictionalgames.com/page/../cBillboardIterator) | GetBillboardIterator |   |   |
| [
```
cClothEntity@
```
](https://wiki.frictionalgames.com/page/../cClothEntity) | GetClothEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cClothEntity@
```
](https://wiki.frictionalgames.com/page/../cClothEntity) | GetClothEntityFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cClothEntityIterator@
```
](https://wiki.frictionalgames.com/page/../cClothEntityIterator) | GetClothEntityIterator |   |   |
| [
```
eIDSpace
```
](https://wiki.frictionalgames.com/page/../eIDSpace) | GetCurrentIDSpace |   |   |
| [
```
iTexture@
```
](https://wiki.frictionalgames.com/page/../iTexture) | GetDefaultGradingTexture |   |   |
| [
```
iTexture@
```
](https://wiki.frictionalgames.com/page/../iTexture) | GetDepthOfFieldBokehTexture |   |   |
| 
```
float
```
 | GetDepthOfFieldFalloff |   |   |
| 
```
float
```
 | GetDepthOfFieldFocusEnd |   |   |
| 
```
float
```
 | GetDepthOfFieldFocusStart |   |   |
| [
```
cLightDirectional@
```
](https://wiki.frictionalgames.com/page/../cLightDirectional) | GetDirectionalLight |   |   |
| 
```
bool
```
 | GetDirectionalLightActive |   |   |
| 
```
bool
```
 | GetDistanceCullActive |   |   |
| 
```
float
```
 | GetDistanceCullFadeSpeed |   |   |
| 
```
float
```
 | GetDistanceCullMaxRange |   |   |
| 
```
float
```
 | GetDistanceCullMinRange |   |   |
| 
```
float
```
 | GetDistanceCullRandomSize |   |   |
| 
```
float
```
 | GetDistanceCullScreenSize |   |   |
| [
```
cMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cMeshEntity) | GetDynamicMeshEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cMeshEntityIterator@
```
](https://wiki.frictionalgames.com/page/../cMeshEntityIterator) | GetDynamicMeshEntityIterator |   |   |
| [
```
iEntity3D@
```
](https://wiki.frictionalgames.com/page/../iEntity3D) | GetEntityFromID | [
```
tID aID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| 
```
int
```
 | GetEnvironmentParticleNum |   |   |
| [
```
cEnvironmentParticles@
```
](https://wiki.frictionalgames.com/page/../cEnvironmentParticles) | GetEnvironmentParticles | 
```
int i
```
 |   |
| 
```
bool
```
 | GetEnvironmentParticlesActive |   |   |
| [
```
cExposureArea@
```
](https://wiki.frictionalgames.com/page/../cExposureArea) | GetExposureArea | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cExposureArea@
```
](https://wiki.frictionalgames.com/page/../cExposureArea) | GetExposureAreaFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cExposureAreaIterator@
```
](https://wiki.frictionalgames.com/page/../cExposureAreaIterator) | GetExposureAreaIterator |   |   |
| 
```
bool
```
 | GetFogActive |   |   |
| 
```
bool
```
 | GetFogApplyAfterFogAreas |   |   |
| [
```
cFogArea@
```
](https://wiki.frictionalgames.com/page/../cFogArea) | GetFogArea | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cFogArea@
```
](https://wiki.frictionalgames.com/page/../cFogArea) | GetFogAreaFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cFogAreaIterator@
```
](https://wiki.frictionalgames.com/page/../cFogAreaIterator) | GetFogAreaIterator |   |   |
| 
```
float
```
 | GetFogBrightness |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetFogColor |   |   |
| 
```
bool
```
 | GetFogCulling |   |   |
| 
```
float
```
 | GetFogEnd |   |   |
| 
```
float
```
 | GetFogFalloffExp |   |   |
| [
```
iTexture@
```
](https://wiki.frictionalgames.com/page/../iTexture) | GetFogSkyboxTexture |   |   |
| 
```
float
```
 | GetFogStart |   |   |
| 
```
bool
```
 | GetFogUnderwater |   |   |
| 
```
bool
```
 | GetFogUseSkybox |   |   |
| [
```
cForceField@
```
](https://wiki.frictionalgames.com/page/../cForceField) | GetForceField | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cForceField@
```
](https://wiki.frictionalgames.com/page/../cForceField) | GetForceFieldFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cForceFieldIterator@
```
](https://wiki.frictionalgames.com/page/../cForceFieldIterator) | GetForceFieldIterator |   |   |
| [
```
cGuiSetEntity@
```
](https://wiki.frictionalgames.com/page/../cGuiSetEntity) | GetGuiSetEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cGuiSetEntity@
```
](https://wiki.frictionalgames.com/page/../cGuiSetEntity) | GetGuiSetEntityFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cGuiSetEntityIterator@
```
](https://wiki.frictionalgames.com/page/../cGuiSetEntityIterator) | GetGuiSetEntityIterator |   |   |
| [
```
cLensFlare@
```
](https://wiki.frictionalgames.com/page/../cLensFlare) | GetLensFlare | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cLensFlare@
```
](https://wiki.frictionalgames.com/page/../cLensFlare) | GetLensFlareFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cLensFlareIterator@
```
](https://wiki.frictionalgames.com/page/../cLensFlareIterator) | GetLensFlareIterator |   |   |
| [
```
iLight@
```
](https://wiki.frictionalgames.com/page/../iLight) | GetLight | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
iLight@
```
](https://wiki.frictionalgames.com/page/../iLight) | GetLightFromID | [
```
tID aID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cLightListIterator@
```
](https://wiki.frictionalgames.com/page/../cLightListIterator) | GetLightIterator |   |   |
| [
```
cLightMaskBoxListIterator@
```
](https://wiki.frictionalgames.com/page/../cLightMaskBoxListIterator) | GetLightMaskBoxIterator |   |   |
| [
```
cMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cMeshEntity) | GetMeshEntityFromID | [
```
tID aID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
cParticleSystem@
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) | GetParticleSystem | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cParticleSystem@
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) | GetParticleSystemFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cParticleSystemIterator@
```
](https://wiki.frictionalgames.com/page/../cParticleSystemIterator) | GetParticleSystemIterator |   |   |
| [
```
iPhysicsWorld@
```
](https://wiki.frictionalgames.com/page/../iPhysicsWorld) | GetPhysicsWorld |   |   |
| [
```
iRopeEntity@
```
](https://wiki.frictionalgames.com/page/../iRopeEntity) | GetRopeEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
iRopeEntity@
```
](https://wiki.frictionalgames.com/page/../iRopeEntity) | GetRopeEntityFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cRopeEntityIterator@
```
](https://wiki.frictionalgames.com/page/../cRopeEntityIterator) | GetRopeEntityIterator |   |   |
| 
```
bool
```
 | GetSecondaryFogActive |   |   |
| 
```
float
```
 | GetSecondaryFogBrightness |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetSecondaryFogColor |   |   |
| 
```
float
```
 | GetSecondaryFogEnd |   |   |
| 
```
float
```
 | GetSecondaryFogFalloffExp |   |   |
| 
```
float
```
 | GetSecondaryFogStart |   |   |
| 
```
bool
```
 | GetSkyBoxActive |   |   |
| 
```
float
```
 | GetSkyBoxBrightness |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetSkyBoxColor |   |   |
| [
```
iTexture@
```
](https://wiki.frictionalgames.com/page/../iTexture) | GetSkyBoxTexture |   |   |
| [
```
iVertexBuffer@
```
](https://wiki.frictionalgames.com/page/../iVertexBuffer) | GetSkyBoxVertexBuffer |   |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | GetSoundEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | GetSoundEntityFromCreationID | 
```
int alID
```
 |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | GetSoundEntityFromID | [
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
cSoundEntityIterator@
```
](https://wiki.frictionalgames.com/page/../cSoundEntityIterator) | GetSoundEntityIterator |   |   |
| [
```
cMeshEntityIterator@
```
](https://wiki.frictionalgames.com/page/../cMeshEntityIterator) | GetStaticMeshEntityIterator |   |   |
| [
```
cSubMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cSubMeshEntity) | GetSubMeshEntityFromID | [
```
tID aID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| 
```
void
```
 | GetSubMeshEntityInArea | ,  
[
```
const cVector3f &in avMin
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avMax
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| [
```
cTerrain@
```
](https://wiki.frictionalgames.com/page/../cTerrain) | GetTerrain |   |   |
| 
```
bool
```
 | GetTerrainActive |   |   |
| 
```
float
```
 | GetToneMappingExposure |   |   |
| 
```
float
```
 | GetToneMappingFadeTime |   |   |
| 
```
float
```
 | GetToneMappingKey |   |   |
| 
```
float
```
 | GetToneMappingWhiteCut |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetWorldSize |   |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsDepthOfFieldActive |   |   |
| 
```
bool
```
 | IsValid | [
```
cSoundEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) |   |
| 
```
bool
```
 | ParticleSystemExists | [
```
cParticleSystem@ apPS
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) |   |
| 
```
void
```
 | RemoveBillboardFromGroup | [
```
cBillboard@ apObject
```
](https://wiki.frictionalgames.com/page/../cBillboard),  
[
```
cBillboardGroup@ apGroup
```
](https://wiki.frictionalgames.com/page/../cBillboardGroup) |   |
| 
```
void
```
 | SetActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCurrentIDSpace | [
```
eIDSpace aSpace
```
](https://wiki.frictionalgames.com/page/../eIDSpace) |   |
| 
```
void
```
 | SetDefaultGradingTexture | [
```
iTexture@ apGrading
```
](https://wiki.frictionalgames.com/page/../iTexture) |   |
| 
```
void
```
 | SetDepthOfFieldActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDepthOfFieldBokehTexture | [
```
iTexture@ apTexture
```
](https://wiki.frictionalgames.com/page/../iTexture) |   |
| 
```
void
```
 | SetDepthOfFieldFalloff | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDepthOfFieldFocusEnd | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDepthOfFieldFocusStart | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDirectionalLightActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDistanceCullActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDistanceCullFadeSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDistanceCullMaxRange | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDistanceCullMinRange | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDistanceCullRandomSize | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDistanceCullScreenSize | 
```
float afX
```
 |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | SetEntityID | [
```
iEntity3D@ apEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D),  
[
```
tID alID
```
](https://wiki.frictionalgames.com/page/../tID) |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | SetEntityID | [
```
iEntity3D@ apEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D),  
[
```
eIDSpace aSpace
```
](https://wiki.frictionalgames.com/page/../eIDSpace),  

```
uint alLocation
```
,  

```
uint alInner
```
 |   |
| 
```
void
```
 | SetEnvironmentParticlesActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFogActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFogApplyAfterFogAreas | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFogBrightness | 
```
float afX
```
 |   |
| 
```
void
```
 | SetFogColor | [
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetFogCulling | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFogEnd | 
```
float afX
```
 |   |
| 
```
void
```
 | SetFogFalloffExp | 
```
float afX
```
 |   |
| 
```
void
```
 | SetFogSkyboxTexture | [
```
iTexture@ apTexture
```
](https://wiki.frictionalgames.com/page/../iTexture) |   |
| 
```
void
```
 | SetFogStart | 
```
float afX
```
 |   |
| 
```
void
```
 | SetFogUnderwater | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFogUseSkybox | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetMainRenderableContainerVisible | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetPhysicsWorld | [
```
iPhysicsWorld@ apWorld
```
](https://wiki.frictionalgames.com/page/../iPhysicsWorld),  

```
bool abAutoDelete
```
 |   |
| 
```
void
```
 | SetSecondaryFogActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSecondaryFogBrightness | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSecondaryFogColor | [
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetSecondaryFogEnd | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSecondaryFogFalloffExp | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSecondaryFogStart | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSkyBox | [
```
iTexture@ apTexture
```
](https://wiki.frictionalgames.com/page/../iTexture),  

```
bool abAutoDestroy
```
 |   |
| 
```
void
```
 | SetSkyBoxActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSkyBoxBrightness | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSkyBoxColor | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetTerrainActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetToneMappingKey | 
```
float afX
```
 |   |
| 
```
bool
```
 | SoundEntityExists | [
```
cSoundEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../cSoundEntity),  

```
int alCreationID
```
 |   |
| 
```
void
```
 | Update | 
```
float afTimeStep
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cWorld](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cWorld)
- Revision: `3757`
- Source update: `2020-08-06T14:31:38Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

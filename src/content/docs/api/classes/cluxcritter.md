---
title: cLuxCritter
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxCritter"
sourceRevision: 3619
sourceUpdated: "2020-08-06T13:50:19Z"
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
| Field Name | Type | Description |
| --- | --- | --- |
| mbWallAvoidDetected | 
```
bool
```
 |   |
| mfForwardRotationYOffset | 
```
float
```
 |   |
| mfMaxGravityVelocity | 
```
float
```
 |   |
| mfMaxTurnSpeed | 
```
float
```
 |   |
| mfMaxVelocity | 
```
float
```
 |   |
| mfTurnSpeedMul | 
```
float
```
 |   |
| mlAnimState | 
```
int
```
 |   |
| msIdleAnim | [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| msMoveAnim | [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| mvGravityVel | [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| mvGroundNormal | [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| mvWallAvoidNormal | [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| mvWallAvoidPosition | [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| mvWantedVel | [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddCollideCallback | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity),  
[
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddConnection | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity),  

```
bool abInvertStateSent
```
,  

```
int alStatesUsed
```
 |   |
| 
```
void
```
 | AppendAnimation | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abLoop
```
 |   |
| 
```
void
```
 | AttachToEntity | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity),  
[
```
iPhysicsBody@ apTargetBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody),  

```
bool abUseRotation
```
,  

```
bool abSnapToParent
```
,  

```
bool abLocked = false
```
 |   |
| 
```
void
```
 | AttachToSocket | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity),  
[
```
const tString &in asSocket
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abUseRotation
```
,  

```
bool abSnapToParent
```
,  

```
bool abLocked = false
```
 |   |
| 
```
void
```
 | BroadcastMessage | 
```
int alMessageId
```
,  
[
```
iLuxEntityComponent@ apSource
```
](https://wiki.frictionalgames.com/page/../iLuxEntityComponent),  
[
```
const cVector3f& avData
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
int alData
```
 |   |
| 
```
bool
```
 | CanInteract | 
```
int alType
```
,  
[
```
iPhysicsBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) |   |
| 
```
void
```
 | ChangeConnectionState | 
```
int alState
```
 |   |
| 
```
bool
```
 | CheckBodyCollision | [
```
iPhysicsBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody),  
[
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
bool
```
 | CheckCharacterCollision | [
```
iCharacterBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iCharacterBody),  
[
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
bool
```
 | CheckEntityCollision | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) |   |
| 
```
bool
```
 | CheckIsOnScreen | 
```
bool abUseRayCast
```
 |   |
| 
```
bool
```
 | CheckShapeCollision | [
```
iCollideShape@ apShape
```
](https://wiki.frictionalgames.com/page/../iCollideShape),  
[
```
const cMatrixf& a_mtxTransform
```
](https://wiki.frictionalgames.com/page/../cMatrixf),  
[
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
bool
```
 | CollidesWithPlayer |   |   |
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
const tString &in asFile
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenDone
```
,  

```
bool abAttach
```
 |   |
| [
```
cParticleSystem@
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) | CreateParticleSystemOnBone | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asFile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asBoneName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenDone
```
,  

```
bool abAttach
```
 |   |
| 
```
void
```
 | DoDamageBox | [
```
const cVector3f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avLocalOffset
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avMinMaxDamage
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afForce
```
,  

```
float afMaxImpulse
```
,  

```
int aDamageType
```
,  

```
float afHitSpeed = 2
```
,  

```
int alStrength = 0
```
,  

```
bool abCheckAgents = false
```
,  

```
bool abCheckPlayer = true
```
,  

```
bool abCheckProps = true
```
,  

```
bool abLethalForPlayer = true
```
 |   |
| 
```
void
```
 | DrawProjDebugText | [
```
const tString &in asText
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afFontSize = 16.0f
```
,  

```
bool abProjectSize = false
```
,  
[
```
eFontAlign aAlignment = eFontAlign_Left
```
](https://wiki.frictionalgames.com/page/../eFontAlign),  
[
```
const cColor &in aColor = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cVector3f &in avOffset = cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afMaxDistance = 20
```
 |   |
| 
```
void
```
 | FadeEffectBaseColor | [
```
const cColor& aDestColor
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afTime
```
 |   |
| 
```
void
```
 | FadeMeshScaleMul | [
```
const cVector3f &in avDestScale
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afTime
```
 |   |
| 
```
void
```
 | Fader_ClearAll |   |   |
| 
```
void
```
 | Fader_FadeTo | 
```
uint alID
```
,  

```
float afGoal
```
,  

```
float afTime
```
,  

```
bool abReverseAtEnd = false
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
void
```
 | Fader_FadeTo | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afGoal
```
,  

```
float afTime
```
,  

```
bool abReverseAtEnd = false
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
float
```
 | Fader_GetValue | 
```
uint alID
```
,  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
float
```
 | Fader_GetValue | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
void
```
 | Fader_Set | 
```
uint alID
```
,  

```
float afX
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
void
```
 | Fader_Set | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afX
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
void
```
 | Fader_SetPaused | 
```
uint alID
```
,  

```
bool abPaused
```
 |   |
| 
```
void
```
 | Fader_SetPaused | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abPaused
```
 |   |
| 
```
bool
```
 | GetAlignToGround |   |   |
| 
```
float
```
 | GetAngleToPlayer2D |   |   |
| 
```
float
```
 | GetAngleToPlayer3D |   |   |
| 
```
float
```
 | GetAngleToPos2D | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
float
```
 | GetAngleToPos3D | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | GetAnimationIsPlaying |   |   |
| [
```
iEntity3D@
```
](https://wiki.frictionalgames.com/page/../iEntity3D) | GetAttachEntity |   |   |
| 
```
bool
```
 | GetAutoSleep |   |   |
| [
```
cMaterial@
```
](https://wiki.frictionalgames.com/page/../cMaterial) | GetBaseMaterial |   |   |
| [
```
cBillboard@
```
](https://wiki.frictionalgames.com/page/../cBillboard) | GetBillboardFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
iPhysicsBody@
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) | GetBody | 
```
int alIdx
```
 |   |
| [
```
iPhysicsBody@
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) | GetBodyFromID | 
```
int alID
```
 |   |
| [
```
iPhysicsBody@
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) | GetBodyFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetBodyIndexFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetBodyNum |   |   |
| 
```
bool
```
 | GetCanRunOnWalls |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetClassName |   |   |
| 
```
void
```
 | GetClosestBody | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avStart
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avDir
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afRayLength
```
 |   |
| 
```
void
```
 | GetClosestCharCollider | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avStart
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avDir
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afRayLength
```
,  

```
bool abCheckDynamic
```
 |   |
| 
```
void
```
 | GetClosestEntity | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avStart
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avDir
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afRayLength
```
,  

```
int alInteractType
```
,  

```
bool abCheckLineOfSight
```
 |   |
| 
```
int
```
 | GetCurrentAnimationIndex |   |   |
| [
```
cAnimationState@
```
](https://wiki.frictionalgames.com/page/../cAnimationState) | GetCurrentAnimationState |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetDebugEyeRay | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetDebugEyeRaysNum |   |   |
| 
```
float
```
 | GetDistanceToGround | 
```
float afMaxTestDistance
```
,  

```
bool abCheckDynamic
```
,  

```
int alNumOfRays = 1
```
,  

```
float afRadius = 0.25
```
,  

```
bool abGetShortest = true
```
 |   |
| 
```
void
```
 | GetDistanceToGround | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMaxTestDistance
```
,  

```
bool abCheckDynamic
```
,  

```
int alNumOfRays = 1
```
,  

```
float afRadius = 0.25
```
,  

```
bool abGetClosest = true
```
 |   |
| 
```
float
```
 | GetDistanceToPlayer |   |   |
| 
```
float
```
 | GetDistanceToPlayer2D |   |   |
| 
```
float
```
 | GetDistanceToPos | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
float
```
 | GetDistanceToPos2D | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetEffectBaseColor |   |   |
| 
```
bool
```
 | GetEffectsActive |   |   |
| 
```
float
```
 | GetEffectsAlpha |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetEffectsOffSound |   |   |
| 
```
float
```
 | GetEffectsOffTime |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetEffectsOnSound |   |   |
| 
```
float
```
 | GetEffectsOnTime |   |   |
| 
```
bool
```
 | GetEntityIsInPlayerFOV |   |   |
| 
```
bool
```
 | GetEntityIsInPlayerLineOfSight | 
```
bool abCheckFOV
```
 |   |
| 
```
void
```
 | GetEntityIsInPlayerLineOfSight | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCheckFOV
```
 |   |
| [
```
eLuxEntityType
```
](https://wiki.frictionalgames.com/page/../eLuxEntityType) | GetEntityType |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetEventInstanceTag |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetEventTag |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetEyePostion |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetFileName |   |   |
| 
```
bool
```
 | GetForceLookAtCheck |   |   |
| 
```
float
```
 | GetHealth |   |   |
| [
```
const tID&
```
](https://wiki.frictionalgames.com/page/../tID) | GetID |   |   |
| 
```
int
```
 | GetInteractIconId | 
```
int alType
```
,  
[
```
iPhysicsBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) |   |
| 
```
bool
```
 | GetInteractionDisabled |   |   |
| 
```
bool
```
 | GetIsClosedDoor |   |   |
| 
```
bool
```
 | GetIsDoor |   |   |
| 
```
bool
```
 | GetLastCreatedSoundIsPlaying |   |   |
| [
```
cLensFlare@
```
](https://wiki.frictionalgames.com/page/../cLensFlare) | GetLensFlareFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
iLight@
```
](https://wiki.frictionalgames.com/page/../iLight) | GetLightFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | GetLightLevelAtPos | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
iLight@ apSkipLight
```
](https://wiki.frictionalgames.com/page/../iLight),  

```
float afRadiusAdd
```
 |   |
| [
```
iPhysicsBody@
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) | GetMainBody |   |   |
| [
```
cLuxMap@
```
](https://wiki.frictionalgames.com/page/../cLuxMap) | GetMap |   |   |
| [
```
cMatrixf
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetMatrix |   |   |
| 
```
float
```
 | GetMaxInteractDistance |   |   |
| [
```
cMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cMeshEntity) | GetMeshEntity |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetMeshScaleMul |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
float
```
 | GetNotRenderedCount |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetOnLoadScale |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetOnLoadTransform |   |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | GetParentId |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetParentName |   |   |
| 
```
int
```
 | GetParentType |   |   |
| [
```
cParticleSystem@
```
](https://wiki.frictionalgames.com/page/../cParticleSystem) | GetParticleSystemFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPlayerFeetPos |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPlayerHeadPos |   |   |
| 
```
bool
```
 | GetPlayerIsInFOV | 
```
float afFOV
```
,  
[
```
const cVector3f& avForward
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | GetPlayerIsInLineOfSight | 
```
float afFOV
```
,  
[
```
const cVector3f& avForward
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abCheckFOV
```
 |   |
| 
```
bool
```
 | GetPlayerIsInLineOfSight |   |   |
| 
```
void
```
 | GetPlayerIsInLineOfSight | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afFOV
```
,  
[
```
const cVector3f& avForward
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abCheckFOV
```
 |   |
| 
```
void
```
 | GetPlayerIsInLineOfSight | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | GetPlayerMovementTowardEntity |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPlayerPos |   |   |
| 
```
bool
```
 | GetPointIsInFOV | [
```
const cVector3f &in avPoint
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afFOV
```
,  
[
```
const cVector3f& avForward
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPosition |   |   |
| 
```
float
```
 | GetRelativeEyeHeight |   |   |
| 
```
bool
```
 | GetReturnBool |   |   |
| 
```
float
```
 | GetReturnFloat |   |   |
| 
```
int
```
 | GetReturnInt |   |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetReturnString |   |   |
| 
```
bool
```
 | GetSaveDataIsUpdated |   |   |
| 
```
bool
```
 | GetScriptableIsSaved |   |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | GetSoundEntityFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | GetTestCollision |   |   |
| 
```
bool
```
 | GetUseRayCollision |   |   |
| 
```
bool
```
 | GetVarBool | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | GetVarColor | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | GetVarFloat | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | GetVariableUpdateRate |   |   |
| 
```
int
```
 | GetVarInt | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetVarString | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetVarVector2f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetVarVector3f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetVoiceAttachNode |   |   |
| 
```
void
```
 | GiveDamage | 
```
float afAmount
```
,  

```
int alStrength
```
,  
[
```
const tString &in asType
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asSource
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | HasCollideCallbacks |   |   |
| 
```
bool
```
 | HasPlayerInteractCallback |   |   |
| 
```
bool
```
 | HasPlayerLookAtCallback |   |   |
| 
```
void
```
 | IncVarFloat | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afX
```
 |   |
| 
```
void
```
 | IncVarInt | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alX
```
 |   |
| 
```
void
```
 | IncVarVector2f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | IncVarVector3f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsFlying |   |   |
| 
```
bool
```
 | IsInteractedWith |   |   |
| 
```
bool
```
 | IsLookedAtByPlayer |   |   |
| 
```
bool
```
 | IsOccluder |   |   |
| 
```
bool
```
 | IsSleeping |   |   |
| 
```
void
```
 | Move_ChangeMaxSpeed | 
```
float afGoal
```
,  

```
float afAcc
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetFlockingAdd | 
```
float afCenterMul
```
,  

```
float afCenterYMul
```
,  

```
float afSeparationMul
```
,  

```
float afAlignmentMul
```
,  

```
float afCohesionMul
```
,  

```
int alMaxMemberChecks
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetStopAdd | 
```
float afAmount
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetTowardCenterAdd | 
```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetTowardPlayerAdd | 
```
bool abNormalize
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetTowardPosAdd | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abNormalize
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetTowardsGroundAdd | 
```
float afMaxHeight
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetWallAvoidAdd | 
```
float afDistanceForward
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetWanderAdd2D | 
```
float afLength
```
,  

```
float afRadius
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_GetWanderAdd3D | 
```
float afLength
```
,  

```
float afRadius
```
,  

```
float afTimeStep
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Move_Normalize | [
```
const cVector3f& avVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | OnInteract | 
```
int alType
```
,  
[
```
iPhysicsBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody),  
[
```
const cVector3f& avFocusPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const tString &in asData
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | PlayAnimation | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afFadeTime = 0.3f
```
,  

```
bool abLoop = false
```
,  

```
bool abPlayTransition = true
```
,  
[
```
const tString &in asCallback = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abGlobalSpace = false
```
 |   |
| [
```
cSoundEntity@
```
](https://wiki.frictionalgames.com/page/../cSoundEntity) | PlaySound | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asFile
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenDone
```
,  

```
bool abAttach
```
 |   |
| 
```
void
```
 | PostUpdate | 
```
float afTimeStep
```
 |   |
| 
```
void
```
 | PreloadEntityModel | [
```
const tString& asFile
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | RemoveAllConnections |   |   |
| 
```
void
```
 | RemoveCollideCallback | [
```
const tString &in asEntityName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | RemoveConnection | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | RemoveEntityAttachment |   |   |
| 
```
bool
```
 | ScriptExecute |   |   |
| 
```
bool
```
 | ScriptMethodExists | [
```
const tString &in asMethod
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | ScriptMethodExistsFast | [
```
const tString &in asMethod
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
 |   |
| 
```
bool
```
 | ScriptPrepare | [
```
const tString &in asMethod
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | ScriptPrepareFast | [
```
const tString &in asMethod
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
 |   |
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
 | SetAlignToGround | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetAnimationMessageEventCallback | [
```
const tString &in asFunc
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abAutoRemove
```
 |   |
| 
```
void
```
 | SetArgBool | 
```
int alArgNum
```
,  

```
bool abVal
```
 |   |
| 
```
void
```
 | SetArgFloat | 
```
int alArg
```
,  

```
float afX
```
 |   |
| 
```
void
```
 | SetArgInt | 
```
int alArg
```
,  

```
int alX
```
 |   |
| 
```
void
```
 | SetArgString | 
```
int alArg
```
,  
[
```
const tString& asStr
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetAutoSleep | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCanRunOnWalls | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetConnectionStateChangeCallback | [
```
const tString& asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetCurrentAnimationPaused | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetEffectBaseColor | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetEffectsActive | 
```
bool abActive
```
,  

```
bool abFadeAndPlaySounds
```
 |   |
| 
```
void
```
 | SetEventInstanceTag | [
```
const tString &in asTag
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetForceLookAtCheck | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFullGameSave | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetGroup | [
```
const tString &in asEntityName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetGroup | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) |   |
| 
```
void
```
 | SetHealth | 
```
float afX
```
 |   |
| 
```
void
```
 | SetInteractionDisabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIsClosedDoor | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIsDoor | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIsFlying | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIsInteractedWith | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIsOccluder | 
```
bool abX
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
 | SetMaxInteractDistance | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMeshScaleMul | [
```
const cVector3f &in avScale
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetNormalizeAnimationWeights | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetPlayerInteractCallback | [
```
const tString& asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenInteracted
```
 |   |
| 
```
void
```
 | SetPlayerLookAtCallback | [
```
const tString& asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abRemoveWhenLookedAt
```
,  

```
bool abCheckCenterOfScreen
```
,  

```
bool abCheckRayIntersection
```
,  

```
float afMaxDistance
```
,  

```
float afCallbackDelay
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
 | SetRecieveMessageCallback | [
```
const tString &in asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetRelativeEyeHeight | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSaveDataIsUpdated | 
```
bool abX
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
 | SetTestCollision | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetupParent | 
```
int alTypeId
```
,  
[
```
tID alId
```
](https://wiki.frictionalgames.com/page/../tID),  
[
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetUseRayCollision | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetVarBool | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abX
```
 |   |
| 
```
void
```
 | SetVarColor | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aX
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetVarFloat | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afX
```
 |   |
| 
```
void
```
 | SetVariableUpdateRate | 
```
float afX
```
 |   |
| 
```
void
```
 | SetVarInt | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alX
```
 |   |
| 
```
void
```
 | SetVarString | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asX
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetVarVector2f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetVarVector3f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | Sleep |   |   |
| 
```
void
```
 | StopAllAnimations | 
```
float afFadeTime
```
 |   |
| 
```
void
```
 | StopAnimation | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afFadeTime
```
 |   |
| 
```
void
```
 | StopAnimation | 
```
int alIdx
```
,  

```
float afFadeTime
```
 |   |
| 
```
void
```
 | Timer_Add | 
```
uint64 alID
```
,  

```
float afTime
```
,  
[
```
const tString &in asFunc = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfExist = true
```
,  

```
bool abRepeat = false
```
 |   |
| 
```
void
```
 | Timer_Add | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
,  
[
```
const tString &in asFunc = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfExist = true
```
,  

```
bool abRepeat = false
```
 |   |
| 
```
void
```
 | Timer_ClearAll |   |   |
| 
```
bool
```
 | Timer_Exists | 
```
uint64 alID
```
 |   |
| 
```
bool
```
 | Timer_Exists | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | Timer_GetTimeLeft | 
```
uint64 alID
```
 |   |
| 
```
float
```
 | Timer_GetTimeLeft | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | Timer_GetValue | 
```
uint64 alID
```
,  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
float
```
 | Timer_GetValue | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
void
```
 | Timer_Remove | 
```
uint64 alID
```
 |   |
| 
```
void
```
 | Timer_Remove | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Timer_SetPaused | 
```
uint64 alID
```
,  

```
bool abX
```
 |   |
| 
```
void
```
 | Timer_SetPaused | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abX
```
 |   |
| 
```
bool
```
 | Timer_TimeHasPassed | 
```
uint64 alID
```
,  

```
float afLength
```
 |   |
| 
```
bool
```
 | Timer_TimeHasPassed | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afLength
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
| 
```
void
```
 | UpdateEntityAttachment |   |   |
| 
```
void
```
 | VariableUpdate | 
```
float afDeltaTime
```
 |   |
| 
```
void
```
 | WakeUp |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxCritter](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxCritter)
- Revision: `3619`
- Source update: `2020-08-06T13:50:19Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

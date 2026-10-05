---
title: cLuxPlayer
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxPlayer"
sourceRevision: 3653
sourceUpdated: "2020-08-06T13:58:54Z"
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
cLuxPlayer has no public fields.

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
 | AddHealth | 
```
float afX
```
,  

```
float afMinHealth
```
 |   |
| 
```
void
```
 | AddMoveState | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
,  
[
```
const tString &in asScriptFile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asScriptClass
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddState | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
,  
[
```
const tString &in asScriptFile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asScriptClass
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddUsedLiquidArea | [
```
cLuxLiquidArea@ apArea
```
](https://wiki.frictionalgames.com/page/../cLuxLiquidArea) |   |
| 
```
void
```
 | AutomoveCharBodyTo | 
```
float afAcc
```
,  

```
float afSpeedMul
```
,  

```
float afMaxSpeed
```
,  
[
```
const cVector3f &in avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | ChangeMoveState | 
```
int alId
```
 |   |
| 
```
void
```
 | ChangeState | 
```
int alId
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
void
```
 | DisableCameraLock |   |   |
| 
```
void
```
 | EnableCameraLock | 
```
float afLocalYawMin
```
,  

```
float afLocalYawMax
```
,  

```
float afLocalPitchMin
```
,  

```
float afLocalPitchMax
```
 |   |
| 
```
void
```
 | FadeCameraAspectMulTo | 
```
float afX
```
,  

```
float afSpeed
```
 |   |
| 
```
void
```
 | FadeCameraFOVMulTo | 
```
float afX
```
,  

```
float afSpeed
```
 |   |
| 
```
void
```
 | FadeCameraFOVTo | 
```
float afTargetFOV
```
,  

```
float afSpeed
```
 |   |
| 
```
void
```
 | FadeCameraRollTo | 
```
int alId
```
,  

```
float afX
```
,  

```
float afSpeedMul
```
,  

```
float afMaxSpeed
```
 |   |
| 
```
float
```
 | GetAutoMoveTargetDistance |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetAverageMoveDirection |   |   |
| 
```
float
```
 | GetAverageMoveSpeed |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetBaseCameraPosAdd |   |   |
| [
```
cCamera@
```
](https://wiki.frictionalgames.com/page/../cCamera) | GetCamera |   |   |
| [
```
iCollideShape@
```
](https://wiki.frictionalgames.com/page/../iCollideShape) | GetCameraCollideShape |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetCameraPosAdd | 
```
int alType
```
 |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetCameraPosAddGoal | 
```
int alType
```
 |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetCameraPosAddSum |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetCameraTrackingAvgMovement |   |   |
| [
```
iCharacterBody@
```
](https://wiki.frictionalgames.com/page/../iCharacterBody) | GetCharacterBody |   |   |
| [
```
cLuxMoveState@
```
](https://wiki.frictionalgames.com/page/../cLuxMoveState) | GetCurrentMoveState |   |   |
| 
```
int
```
 | GetCurrentMoveStateId |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetCurrentMoveStateName |   |   |
| 
```
int
```
 | GetCurrentStateId |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetCurrentStateName |   |   |
| 
```
float
```
 | GetDefaultFOV |   |   |
| 
```
float
```
 | GetHealth |   |   |
| 
```
bool
```
 | GetIsLiquidAreaUsed | [
```
cLuxLiquidArea@ apArea
```
](https://wiki.frictionalgames.com/page/../cLuxLiquidArea) |   |
| 
```
float
```
 | GetLiquidHeight |   |   |
| 
```
float
```
 | GetMaxHealth |   |   |
| 
```
float
```
 | GetRotateCameraTargetDistance |   |   |
| 
```
float
```
 | GetTimeSincePhysicsObjectInteraction |   |   |
| 
```
float
```
 | GetVisibilityMaxRange |   |   |
| 
```
float
```
 | GetVisibilityRangeMul |   |   |
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

```
int aType
```
,  

```
float afMinHealth
```
,  
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
 | IsActive |   |   |
| 
```
bool
```
 | IsAutomoveCharBodyActive |   |   |
| 
```
bool
```
 | IsCameraRotateActive |   |   |
| 
```
bool
```
 | IsDead |   |   |
| 
```
bool
```
 | IsInLiquid |   |   |
| 
```
void
```
 | MoveCameraPosAdd | 
```
int alType
```
,  
[
```
const cVector3f &in avGoal
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afAcc
```
,  

```
float afSpeed
```
,  

```
float afSlowdownDist
```
 |   |
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
 | RemoveUsedLiquidArea | [
```
cLuxLiquidArea@ apArea
```
](https://wiki.frictionalgames.com/page/../cLuxLiquidArea) |   |
| 
```
void
```
 | ResetBasicProperties |   |   |
| 
```
void
```
 | ResetTimeSincePhysicsObjectInteraction |   |   |
| 
```
void
```
 | RotateCameraTowards | 
```
float afAcc
```
,  

```
float afSpeedMul
```
,  

```
float afMaxSpeed
```
,  
[
```
const cVector3f &in avLookAtPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abLocalCoord
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
 | SetAutomoveCharBodyTarget | [
```
const cVector3f &in avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetBaseCameraPosAdd | [
```
const cVector3f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetCameraPosAdd | 
```
int alType
```
,  
[
```
const cVector3f &in avVector
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetCameraRoll | 
```
int alId
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
 | SetCharacterBody | [
```
iCharacterBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iCharacterBody) |   |
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
 | SetMaxCameraTrackingAmount | 
```
int alSize
```
 |   |
| 
```
void
```
 | SetMaxHealth | 
```
float afX
```
 |   |
| 
```
void
```
 | SetRotateCameraTarget | [
```
const cVector3f &in avLookAtPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abLocalCoord
```
 |   |
| 
```
void
```
 | SetVisibilityMaxRange | 
```
int alId
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
 | SetVisibilityRangeMul | 
```
int alId
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
 | StopAutomoveCharBody |   |   |
| 
```
void
```
 | StopCameraRotate | 
```
float afDeacc
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxPlayer](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxPlayer)
- Revision: `3653`
- Source update: `2020-08-06T13:58:54Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: iCharacterBody
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iCharacterBody"
sourceRevision: 3885
sourceUpdated: "2020-08-06T14:59:13Z"
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
iCharacterBody has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
int
```
 | AddExtraSize | [
```
const cVector3f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | AddForce | [
```
const cVector3f& avForce
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | AddForceVelocity | [
```
const cVector3f &in avVel
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | AddPitch | 
```
float afX
```
 |   |
| 
```
void
```
 | AddRoll | 
```
float afX
```
 |   |
| 
```
void
```
 | AddYaw | 
```
float afX
```
 |   |
| 
```
bool
```
 | CheckCharacterFits | [
```
const cVector3f& avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abFeetPosition
```
,  

```
int alSizeIdx
```
,  
[
```
cVector3f& avOutPushBackVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | CheckRayIntersection | [
```
const cVector3f& avStart
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f& avEnd
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float& afOutDistance
```
,  
[
```
cVector3f& avOutNormalVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | GetAccurateClimbing |   |   |
| 
```
int
```
 | GetActiveSize |   |   |
| 
```
float
```
 | GetAirFriction |   |   |
| [
```
cCamera@
```
](https://wiki.frictionalgames.com/page/../cCamera) | GetCamera |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetCameraPosAdd |   |   |
| 
```
int
```
 | GetCameraSmoothPosNum |   |   |
| 
```
bool
```
 | GetCameraUpdateActive |   |   |
| 
```
bool
```
 | GetCameraUseSmoothing |   |   |
| 
```
float
```
 | GetCharacterMaxPushMass |   |   |
| 
```
float
```
 | GetCharacterPushForce |   |   |
| 
```
bool
```
 | GetCharacterPushIn2D |   |   |
| 
```
float
```
 | GetClimbForwardMul |   |   |
| 
```
float
```
 | GetClimbHeightAdd |   |   |
| 
```
bool
```
 | GetCollideCharacter |   |   |
| 
```
uint
```
 | GetCollideFlags |   |   |
| 
```
float
```
 | GetConstantContactForceMul |   |   |
| [
```
iPhysicsBody@
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) | GetCurrentBody |   |   |
| [
```
iCollideShape@
```
](https://wiki.frictionalgames.com/page/../iCollideShape) | GetCurrentShape |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetCustomGravity |   |   |
| 
```
bool
```
 | GetCustomGravityActive |   |   |
| 
```
bool
```
 | GetDeaccelerateMoveSpeedInAir |   |   |
| 
```
bool
```
 | GetDisableDiagSpeedBoost |   |   |
| [
```
iEntity3D@
```
](https://wiki.frictionalgames.com/page/../iEntity3D) | GetEntity |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetEntityOffset |   |   |
| 
```
float
```
 | GetEntityPitchAmount |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetEntityPostOffset |   |   |
| 
```
int
```
 | GetEntitySmoothPosNum |   |   |
| 
```
int
```
 | GetEntitySmoothYPosNum |   |   |
| 
```
bool
```
 | GetEntityUseSmoothing |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetFeetPosition |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetForce |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetForceVelocity |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetForward |   |   |
| [
```
iPhysicsBody@
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody) | GetGravityAttachedBody |   |   |
| [
```
iPhysicsMaterial@
```
](https://wiki.frictionalgames.com/page/../iPhysicsMaterial) | GetGravityCollideMaterial |   |   |
| 
```
float
```
 | GetGroundAngleMin |   |   |
| 
```
float
```
 | GetGroundFriction |   |   |
| [
```
tID
```
](https://wiki.frictionalgames.com/page/../tID) | GetID |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLastGroundNormal |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLastPosition |   |   |
| 
```
float
```
 | GetMass |   |   |
| 
```
float
```
 | GetMaxContactForcePerMassUnit |   |   |
| 
```
float
```
 | GetMaxGravitySpeed |   |   |
| 
```
float
```
 | GetMaxNegativeMoveSpeed | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir) |   |
| 
```
float
```
 | GetMaxNoSlideSlopeAngle |   |   |
| 
```
int
```
 | GetMaxOnGroundCount |   |   |
| 
```
float
```
 | GetMaxPositiveMoveSpeed | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir) |   |
| 
```
float
```
 | GetMaxPushForce |   |   |
| 
```
float
```
 | GetMaxPushMass |   |   |
| 
```
float
```
 | GetMaxStepSize |   |   |
| 
```
float
```
 | GetMaxStepSizeInAir |   |   |
| 
```
float
```
 | GetMoveAcc | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir) |   |
| 
```
float
```
 | GetMoveDeacc | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir) |   |
| 
```
bool
```
 | GetMovedLastUpdate |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetMoveMatrix |   |   |
| 
```
float
```
 | GetMoveOppositeDirAccMul | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir) |   |
| 
```
float
```
 | GetMoveSpeed | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir) |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
bool
```
 | GetPhysicsBodyActive |   |   |
| 
```
float
```
 | GetPitch |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPosition |   |   |
| 
```
float
```
 | GetPushImpulse |   |   |
| 
```
bool
```
 | GetPushIn2D |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetRight |   |   |
| 
```
float
```
 | GetRoll |   |   |
| 
```
bool
```
 | GetRotateYawWhenGravityAttached |   |   |
| [
```
iCollideShape@
```
](https://wiki.frictionalgames.com/page/../iCollideShape) | GetShape | 
```
int alIdx
```
 |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetSize |   |   |
| 
```
float
```
 | GetStepClimbSpeed |   |   |
| 
```
bool
```
 | GetStickToSlope |   |   |
| 
```
bool
```
 | GetTestCollision |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetUp |   |   |
| 
```
bool
```
 | GetUpdateCameraVelocity |   |   |
| 
```
bool
```
 | GetUpdateCameraYaw |   |   |
| 
```
bool
```
 | GetUseEntitySmoothYPos |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetVelocity | 
```
float afFrameTime
```
 |   |
| 
```
float
```
 | GetVelocityContactForceMul |   |   |
| 
```
float
```
 | GetYaw |   |   |
| 
```
bool
```
 | GravityIsActive |   |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsClimbing |   |   |
| 
```
bool
```
 | IsOnGround |   |   |
| 
```
void
```
 | Move | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afMul
```
 |   |
| 
```
void
```
 | ResetClimbing |   |   |
| 
```
void
```
 | SetAccurateClimbing | 
```
bool abX
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
 | SetActiveSize | 
```
int alNum
```
 |   |
| 
```
void
```
 | SetAirFriction | 
```
float afX
```
 |   |
| 
```
void
```
 | SetCamera | [
```
cCamera@ apCam
```
](https://wiki.frictionalgames.com/page/../cCamera) |   |
| 
```
void
```
 | SetCameraPosAdd | [
```
const cVector3f& avAdd
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetCameraSmoothPosNum | 
```
int alNum
```
 |   |
| 
```
void
```
 | SetCameraUpdateActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCameraUseSmoothing | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCharacterMaxPushMass | 
```
float afX
```
 |   |
| 
```
void
```
 | SetCharacterPushForce | 
```
float afX
```
 |   |
| 
```
void
```
 | SetCharacterPushIn2D | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetClimbForwardMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetClimbHeightAdd | 
```
float afX
```
 |   |
| 
```
void
```
 | SetCollideCharacter | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCollideFlags | 
```
uint alX
```
 |   |
| 
```
void
```
 | SetConstantContactForceMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetCustomGravity | [
```
const cVector3f &in avCustomGravity
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetCustomGravityActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDeaccelerateMoveSpeedInAir | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDisableDiagSpeedBoost | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetEntity | [
```
iEntity3D@ apEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D) |   |
| 
```
void
```
 | SetEntityOffset | [
```
const cMatrixf& a_mtxOffset
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetEntityPitchAmount | 
```
float afX
```
 |   |
| 
```
void
```
 | SetEntityPostOffset | [
```
const cMatrixf& a_mtxOffset
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetEntitySmoothPosNum | 
```
int alNum
```
 |   |
| 
```
void
```
 | SetEntitySmoothYPosNum | 
```
int alX
```
 |   |
| 
```
void
```
 | SetEntityUseSmoothing | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFeetPosition | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abSmooth
```
 |   |
| 
```
void
```
 | SetForce | [
```
const cVector3f& avForce
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetForceVelocity | [
```
const cVector3f &in avVel
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetGravityActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetGroundAngleMin | 
```
float afX
```
 |   |
| 
```
void
```
 | SetGroundFriction | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMass | 
```
float afMass
```
 |   |
| 
```
void
```
 | SetMaxContactForcePerMassUnit | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMaxGravitySpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMaxNegativeMoveSpeed | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afX
```
 |   |
| 
```
void
```
 | SetMaxNoSlideSlopeAngle | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetMaxOnGroundCount | 
```
int alX
```
 |   |
| 
```
void
```
 | SetMaxPositiveMoveSpeed | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afX
```
 |   |
| 
```
void
```
 | SetMaxPushForce | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMaxPushMass | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMaxStepSize | 
```
float afSize
```
 |   |
| 
```
void
```
 | SetMaxStepSizeInAir | 
```
float afSize
```
 |   |
| 
```
void
```
 | SetMoveAcc | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afX
```
 |   |
| 
```
void
```
 | SetMoveDeacc | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afX
```
 |   |
| 
```
void
```
 | SetMoveOppositeDirAccMul | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afX
```
 |   |
| 
```
void
```
 | SetMoveSpeed | [
```
eCharDir aDir
```
](https://wiki.frictionalgames.com/page/../eCharDir),  

```
float afX
```
 |   |
| 
```
void
```
 | SetPhysicsBodyActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetPitch | 
```
float afX
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
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abSmooth
```
 |   |
| 
```
void
```
 | SetPushImpulse | 
```
float afX
```
 |   |
| 
```
void
```
 | SetPushIn2D | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetRoll | 
```
float afX
```
 |   |
| 
```
void
```
 | SetRotateYawWhenGravityAttached | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetStepClimbSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetStickToSlope | 
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
 | SetUpdateCameraVelocity | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetUpdateCameraYaw | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetUseEntitySmoothYPos | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetVelocityContactForceMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetYaw | 
```
float afX
```
 |   |
| 
```
void
```
 | StopMovement |   |   |
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iCharacterBody](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iCharacterBody)
- Revision: `3885`
- Source update: `2020-08-06T14:59:13Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

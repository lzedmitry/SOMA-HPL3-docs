---
title: cLuxCharMover
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxCharMover"
sourceRevision: 3614
sourceUpdated: "2020-08-06T13:49:04Z"
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
cLuxCharMover has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddSpeedState | 
```
int alId
```
 |   |
| 
```
float
```
 | CalculateSpeedMul | 
```
float afTimeStep
```
 |   |
| [
```
iCharacterBody@
```
](https://wiki.frictionalgames.com/page/../iCharacterBody) | GetCharBody |   |   |
| [
```
iLuxEntity@
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) | GetEntity |   |   |
| 
```
bool
```
 | GetIdleExtraAnimActive |   |   |
| 
```
float
```
 | GetMaxStuckCounter |   |   |
| 
```
float
```
 | GetMoveSpeed |   |   |
| 
```
float
```
 | GetStuckCounter |   |   |
| [
```
eLuxEntityComponentType
```
](https://wiki.frictionalgames.com/page/../eLuxEntityComponentType) | GetType |   |   |
| 
```
bool
```
 | GetUseMoveStateAnimations |   |   |
| 
```
float
```
 | GetWantedSpeedAmount |   |   |
| 
```
void
```
 | LoadFromVariables | [
```
cResourceVarsObject@ apVars
```
](https://wiki.frictionalgames.com/page/../cResourceVarsObject) |   |
| 
```
void
```
 | MoveToPos | [
```
const cVector3f &in avFeetPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abSlowDownAndStopAtGoal = false
```
 |   |
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
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | PlayTrackAnimation | [
```
cLuxTrackNode@ apNode
```
](https://wiki.frictionalgames.com/page/../cLuxTrackNode) |   |
| 
```
void
```
 | ResetStuckCounter |   |   |
| 
```
void
```
 | SetBackwardAnimName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetBankingActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetBankingAngleMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetBankingMaxAngle | 
```
float afX
```
 |   |
| 
```
void
```
 | SetBankingMaxSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetBankingSpeedMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDirection | [
```
eLuxCharMoveDirection aDir
```
](https://wiki.frictionalgames.com/page/../eLuxCharMoveDirection) |   |
| 
```
void
```
 | SetDynamicObjectAvoidanceActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIdleAnimName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetIdleExtraAnimActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetIdleExtraAnimName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetMaxBackwardSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMaxForwardSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMoveSpeedAnimMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetRunAnimName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetRunToWalkSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState | 
```
int alId
```
 |   |
| 
```
void
```
 | SetSpeedState_Backward | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_Forward | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_ForwardAcc | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_ForwardDeacc | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_SidewayAcc | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_SidewayDeacc | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_Sideways | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_TurnBreakMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_TurnMaxSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedState_TurnSpeedMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetStoppedToWalkSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTurnBreakMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTurnedToGoalCallbackFunc | [
```
const tString& asFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetTurnMaxSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTurnMinBreakAngle | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTurnSpeedMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTurnStoppedToWalkSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTurnWalkToStoppedSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetupDynamicObjectAvoidance | 
```
float afMaxDistance
```
,  

```
float afMinMass
```
,  

```
float afSteerAmount
```
 |   |
| 
```
void
```
 | SetupIdleExtra | [
```
const tString &in asAnimName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMinWait
```
,  

```
float afMaxWait
```
,  

```
bool abPauseProceduralAnims
```
 |   |
| 
```
void
```
 | SetupWallAvoidance | 
```
float afRadius
```
,  

```
float afSteerAmount
```
,  

```
int alSamples
```
 |   |
| 
```
void
```
 | SetUse3DMovement | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetUseMoveStateAnimations | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetVerticalMoveSpeedExtraAnimMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetWalkAnimName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetWalkToRunSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetWalkToStoppedSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetWallAvoidanceActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | StopTurning |   |   |
| 
```
void
```
 | TurnInstantlyToAngle | 
```
float afAngle
```
 |   |
| 
```
void
```
 | TurnInstantlyToAngle | 
```
float afYaw
```
,  

```
float afPitch
```
 |   |
| 
```
void
```
 | TurnInstantlyToPos | [
```
const cVector3f &in avGoalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | TurnToAngle | 
```
float afAngle
```
 |   |
| 
```
void
```
 | TurnToAngles | 
```
float afYaw
```
,  

```
float afPitch
```
 |   |
| 
```
void
```
 | TurnToPos | [
```
const cVector3f &in avFeetPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxCharMover](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxCharMover)
- Revision: `3614`
- Source update: `2020-08-06T13:49:04Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

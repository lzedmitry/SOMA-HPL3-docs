---
title: cMeshEntity
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cMeshEntity"
sourceRevision: 3679
sourceUpdated: "2020-08-06T14:11:33Z"
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
cMeshEntity has no public fields.

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
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | AddSocket | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asAttachedBoneName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cMatrixf &in a_mtxLocalTransform
```
](https://wiki.frictionalgames.com/page/../cMatrixf),  

```
bool abRescale = true
```
 |   |
| 
```
void
```
 | AlignBodiesToSkeleton | 
```
bool abCalculateSpeed
```
 |   |
| 
```
bool
```
 | AnimationIsOver | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cMatrixf
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | CalculateTransformFromSkeleton |   |   |
| [
```
cMatrixf
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | CalculateTransformFromSkeleton | [
```
cVector3f &out apPostion
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
cVector3f &out apAngles
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | CheckColliderShapeCollision | [
```
iPhysicsWorld@ apWorld
```
](https://wiki.frictionalgames.com/page/../iPhysicsWorld),  
[
```
iCollideShape@ apShape
```
](https://wiki.frictionalgames.com/page/../iCollideShape),  
[
```
const cMatrixf& a_mtxShape
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | ClearSockets |   |   |
| [
```
cProcAnimation@
```
](https://wiki.frictionalgames.com/page/../cProcAnimation) | CreateProcAnimation | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | FadeSkeletonPhysicsWeight | 
```
float afTime
```
 |   |
| [
```
cActorAnimController@
```
](https://wiki.frictionalgames.com/page/../cActorAnimController) | GetActorAnimController |   |   |
| [
```
cAnimationState@
```
](https://wiki.frictionalgames.com/page/../cAnimationState) | GetAnimationState | 
```
int alIndex
```
 |   |
| [
```
cAnimationState@
```
](https://wiki.frictionalgames.com/page/../cAnimationState) | GetAnimationStateFromName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetAnimationStateIndex | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetAnimationStateNum |   |   |
| [
```
cBoneState@
```
](https://wiki.frictionalgames.com/page/../cBoneState) | GetBoneState | 
```
int alIndex
```
 |   |
| [
```
cBoneState@
```
](https://wiki.frictionalgames.com/page/../cBoneState) | GetBoneStateFromName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetBoneStateIndex | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetBoneStateIndexFromPtr | [
```
cBoneState@ apBoneState
```
](https://wiki.frictionalgames.com/page/../cBoneState) |   |
| 
```
int
```
 | GetBoneStateNum |   |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetBoneStateRoot |   |   |
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
cMesh@
```
](https://wiki.frictionalgames.com/page/../cMesh) | GetMesh |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetNodeState | 
```
int alIndex
```
 |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetNodeStateFromName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetNodeStateIndex | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetNodeStateNum |   |   |
| 
```
bool
```
 | GetNormalizeAnimationWeights |   |   |
| [
```
cProcAnimation@
```
](https://wiki.frictionalgames.com/page/../cProcAnimation) | GetProcAnimation | 
```
int alIdx
```
 |   |
| [
```
cProcAnimation@
```
](https://wiki.frictionalgames.com/page/../cProcAnimation) | GetProcAnimationFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetProcAnimationNum |   |   |
| 
```
bool
```
 | GetScriptableIsSaved |   |   |
| 
```
bool
```
 | GetSkeletonCollidersActive |   |   |
| 
```
bool
```
 | GetSkeletonPhysicsActive |   |   |
| 
```
bool
```
 | GetSkeletonPhysicsCanSleep |   |   |
| 
```
float
```
 | GetSkeletonPhysicsWeight |   |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetSocket | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetSocketFromIndex | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetSocketNum |   |   |
| [
```
cSubMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cSubMeshEntity) | GetSubMeshEntity | 
```
uint alIdx
```
 |   |
| 
```
int
```
 | GetSubMeshEntityIndex | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cSubMeshEntity@
```
](https://wiki.frictionalgames.com/page/../cSubMeshEntity) | GetSubMeshEntityName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetSubMeshEntityNum |   |   |
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
 | Play | 
```
int alIndex
```
,  

```
bool abLoop
```
,  

```
bool bStopPrev
```
 |   |
| 
```
void
```
 | PlayFadeTo | 
```
int alIndex
```
,  

```
bool abLoop
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
 | PlayFadeToName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abLoop
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
 | PlayName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abLoop
```
,  

```
bool bStopPrev
```
 |   |
| 
```
void
```
 | PostUpdateLogic | 
```
float afTimeStep
```
 |   |
| 
```
void
```
 | ProcPlay | 
```
int alIdx
```
,  

```
float afAnimTime
```
,  

```
bool abLoop
```
,  

```
bool abStopPrev
```
 |   |
| 
```
void
```
 | ProcPlayFadeTo | 
```
int alIndex
```
,  

```
float afAnimTime
```
,  

```
bool abLoop
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
 | ProcPlayFadeToName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afAnimTime
```
,  

```
bool abLoop
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
 | ProcPlayName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afAnimTime
```
,  

```
bool abLoop
```
,  

```
bool abStopPrev
```
 |   |
| 
```
void
```
 | ProcStop |   |   |
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
 | ResetGraphicsUpdated |   |   |
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
 | SetCoverageAmount | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDiffuseColorMul | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetDisableSleep | 
```
bool abX
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
 | SetIsOccluder | 
```
bool abX
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
 | SetNormalizeAnimationWeights | 
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
 | SetScriptableIsSaved | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSkeletonCollidersActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSkeletonPhysicsActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSkeletonPhysicsCanSleep | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSkeletonPhysicsWeight | 
```
float afX
```
 |   |
| 
```
void
```
 | SetStatic | 
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
 | Stop |   |   |
| 
```
void
```
 | UpdateAnimation | 
```
float afTimeStep
```
 |   |
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
 | UseAutomaticLiquidAmount |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cMeshEntity](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cMeshEntity)
- Revision: `3679`
- Source update: `2020-08-06T14:11:33Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

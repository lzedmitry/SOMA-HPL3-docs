---
title: cCamera
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cCamera"
sourceRevision: 3539
sourceUpdated: "2020-08-06T13:24:00Z"
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
cCamera has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddPitch | 
```
float afAngle
```
 |   |
| 
```
void
```
 | AddRoll | 
```
float afAngle
```
 |   |
| 
```
void
```
 | AddYaw | 
```
float afAngle
```
 |   |
| 
```
void
```
 | AttachEntity | [
```
iEntity3D@ aEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D) |   |
| 
```
void
```
 | ClearAttachedEntities |   |   |
| 
```
float
```
 | GetAspect |   |   |
| [
```
cNode3D@
```
](https://wiki.frictionalgames.com/page/../cNode3D) | GetAttachmentNode |   |   |
| [
```
cFrustum@+
```
](https://wiki.frictionalgames.com/page/../cFrustum) | GetExtendedFrustum |   |   |
| 
```
float
```
 | GetExtendedPitch |   |   |
| 
```
float
```
 | GetExtendedYaw |   |   |
| 
```
float
```
 | GetExtenededRoll |   |   |
| 
```
float
```
 | GetFarClipPlane |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetForward |   |   |
| 
```
float
```
 | GetFOV |   |   |
| [
```
cFrustum@+
```
](https://wiki.frictionalgames.com/page/../cFrustum) | GetFrustum |   |   |
| 
```
bool
```
 | GetInifintiveFarPlane |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetMatrix |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetMoveMatrix |   |   |
| [
```
eCameraMoveMode
```
](https://wiki.frictionalgames.com/page/../eCameraMoveMode) | GetMoveMode |   |   |
| 
```
float
```
 | GetNearClipPlane |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetOrthoViewSize |   |   |
| 
```
float
```
 | GetPitch |   |   |
| 
```
float
```
 | GetPitchMaxLimit |   |   |
| 
```
float
```
 | GetPitchMinLimit |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPosition |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetProjectionMatrix |   |   |
| [
```
eProjectionType
```
](https://wiki.frictionalgames.com/page/../eProjectionType) | GetProjectionType |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetRight |   |   |
| 
```
float
```
 | GetRoll |   |   |
| [
```
eCameraRotateMode
```
](https://wiki.frictionalgames.com/page/../eCameraRotateMode) | GetRotateMode |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetRotationMatrix |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetUp |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetVelocity |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetViewMatrix |   |   |
| 
```
float
```
 | GetYaw |   |   |
| 
```
float
```
 | GetYawMaxLimit |   |   |
| 
```
float
```
 | GetYawMinLimit |   |   |
| 
```
void
```
 | MoveForward | 
```
float afDist
```
 |   |
| 
```
void
```
 | MoveRight | 
```
float afDist
```
 |   |
| 
```
void
```
 | MoveUp | 
```
float afDist
```
 |   |
| 
```
void
```
 | RemoveEntity | [
```
iEntity3D@ aEntity
```
](https://wiki.frictionalgames.com/page/../iEntity3D) |   |
| 
```
void
```
 | ResetRotation |   |   |
| 
```
void
```
 | SetAspect | 
```
float afSpect
```
 |   |
| 
```
void
```
 | SetExtendedPitch | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetExtendedRoll | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetExtendedYaw | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetFarClipPlane | 
```
float afX
```
 |   |
| 
```
void
```
 | SetForward | [
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetFOV | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetInifintiveFarPlane | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetMoveMode | [
```
eCameraMoveMode aMode
```
](https://wiki.frictionalgames.com/page/../eCameraMoveMode) |   |
| 
```
void
```
 | SetNearClipPlane | 
```
float afX
```
 |   |
| 
```
void
```
 | SetOrthoViewSize | [
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetPitch | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetPitchLimits | 
```
float afMin
```
,  

```
float afMax
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
 | SetProjectionType | [
```
eProjectionType aType
```
](https://wiki.frictionalgames.com/page/../eProjectionType) |   |
| 
```
void
```
 | SetRight | [
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetRoll | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetRotateMode | [
```
eCameraRotateMode aMode
```
](https://wiki.frictionalgames.com/page/../eCameraRotateMode) |   |
| 
```
void
```
 | SetRotationMatrix | [
```
const cMatrixf &in a_mtxRot
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetUp | [
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetVelocity | [
```
const cVector3f &in avVel
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetYaw | 
```
float afAngle
```
 |   |
| 
```
void
```
 | SetYawLimits | 
```
float afMin
```
,  

```
float afMax
```
 |   |
| 
```
void
```
 | UnProject | [
```
cVector3f& avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
cVector3f& apDirection
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avScreenPos
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avVirtualScreenSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cCamera](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cCamera)
- Revision: `3539`
- Source update: `2020-08-06T13:24:00Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

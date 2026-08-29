---
title: iPhysicsCloth
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iPhysicsCloth"
sourceRevision: 3907
sourceUpdated: "2020-08-06T15:04:08Z"
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
iPhysicsCloth has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | ApplyForceToParticles | [
```
const cVector3f& avForce
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
cVerletParticle@ apBaseParticle
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  
[
```
const cVector3f& avOffset = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | AttachToLine | [
```
cVector3f avStart
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
cVector3f avEnd
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
int alRow
```
,  

```
int alColumnStride
```
,  

```
bool abFixedPositions = false
```
 |   |
| 
```
bool
```
 | GetActive |   |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetClothSize |   |   |
| 
```
bool
```
 | GetCollide |   |   |
| 
```
float
```
 | GetDamping |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetGravityForce |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
cVerletParticle@
```
](https://wiki.frictionalgames.com/page/../cVerletParticle) | GetParticle | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetParticleNum |   |   |
| 
```
float
```
 | GetParticleRadius |   |   |
| 
```
float
```
 | GetSlideAmount |   |   |
| 
```
int
```
 | GetUniqueID |   |   |
| 
```
int
```
 | GetUpdateCount |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetWindForce |   |   |
| 
```
void
```
 | IncUpdateCount |   |   |
| 
```
void
```
 | RemoveAttachedBody | [
```
iPhysicsBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody),  

```
bool abRemoveContainerFromBody
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
 | SetCollide | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDamping | 
```
float afX
```
 |   |
| 
```
void
```
 | SetGravityForce | [
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetParticleRadius | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSleeping | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSlideAmount | 
```
float afX
```
 |   |
| 
```
void
```
 | SetWindForce | [
```
const cVector3f avWindForce
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | UpdateLengthConstraint | [
```
cVerletParticle@ apP1
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  
[
```
cVerletParticle@ apP2
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  

```
float afLength
```
 |   |
| 
```
void
```
 | UpdateLengthConstraint | [
```
cVerletParticle@ apP1
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  
[
```
cVerletParticle@ apP2
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  

```
float afLength
```
,  

```
float afStiffness
```
 |   |
| 
```
void
```
 | UpdateLengthConstraint | [
```
cVerletParticle@ apP1
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  
[
```
cVerletParticle@ apP2
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  

```
float afMinLength
```
,  

```
float afMaxLength
```
,  

```
float afStiffness
```
 |   |
| 
```
void
```
 | UpdateLengthConstraintStretch | [
```
cVerletParticle@ apP1
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  
[
```
cVerletParticle@ apP2
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  

```
float afLength
```
,  

```
float afStiffness
```
 |   |
| 
```
void
```
 | UpdateParticleCollisionConstraint | [
```
cVerletParticle@ apPart
```
](https://wiki.frictionalgames.com/page/../cVerletParticle),  
[
```
const cVector3f& avPrevPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afRadius
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iPhysicsCloth](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iPhysicsCloth)
- Revision: `3907`
- Source update: `2020-08-06T15:04:08Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

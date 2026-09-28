---
title: iVerletParticleContainer
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iVerletParticleContainer"
sourceRevision: 3943
sourceUpdated: "2020-08-06T15:11:55Z"
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
iVerletParticleContainer has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
bool
```
 | GetActive |   |   |
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iVerletParticleContainer](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iVerletParticleContainer)
- Revision: `3943`
- Source update: `2020-08-06T15:11:55Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: iScrPlayer Interface
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iScrPlayer_Interface"
sourceRevision: 3932
sourceUpdated: "2020-08-06T15:09:44Z"
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
iScrPlayer_Interface has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | CharBody_GravityCollide | [
```
iCharacterBody@ apCharBody
```
](https://wiki.frictionalgames.com/page/../iCharacterBody),  
[
```
iPhysicsBody@ apBody
```
](https://wiki.frictionalgames.com/page/../iPhysicsBody),  
[
```
cCollideData@ apCollideData
```
](https://wiki.frictionalgames.com/page/../cCollideData) |   |
| 
```
void
```
 | CharBody_HitGround | [
```
iCharacterBody@ apCharBody
```
](https://wiki.frictionalgames.com/page/../iCharacterBody),  
[
```
const cVector3f& avVel
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | CreateWorldEntities | [
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
void
```
 | DestroyWorldEntities | [
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
float
```
 | DrawDebugOutput | [
```
cGuiSet@ apSet
```
](https://wiki.frictionalgames.com/page/../cGuiSet),  
[
```
iFontData@ apFont
```
](https://wiki.frictionalgames.com/page/../iFontData),  

```
float afStartY
```
 |   |
| [
```
cLuxPlayer@
```
](https://wiki.frictionalgames.com/page/../cLuxPlayer) | GetBase |   |   |
| 
```
int
```
 | GetCharacterState |   |   |
| 
```
void
```
 | LoadUserConfig |   |   |
| 
```
void
```
 | OnAction | 
```
int alAction
```
,  

```
bool abPressed
```
 |   |
| 
```
void
```
 | OnAnalogInput | 
```
int alAnalogId
```
,  
[
```
const cVector3f& avAmount
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | OnDraw | 
```
float afFrameTime
```
 |   |
| 
```
void
```
 | OnEnterContainer | [
```
const tString &in asOldContainer
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | OnExitPressed |   |   |
| 
```
void
```
 | OnLeaveContainer | [
```
const tString &in asNewContainer
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | OnMapEnter | [
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
void
```
 | OnMapLeave | [
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
void
```
 | OnUnderwaterEffectActive | 
```
bool abX
```
,  

```
bool abUseStartAndEndEffects
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
 | PreloadData | [
```
cLuxMap@ apMap
```
](https://wiki.frictionalgames.com/page/../cLuxMap) |   |
| 
```
void
```
 | Reset |   |   |
| 
```
void
```
 | SaveUserConfig |   |   |
| 
```
void
```
 | SetCharacterState | 
```
int alState
```
 |   |
| 
```
void
```
 | SetupStartPos | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afAngle
```
,  

```
bool abCrouching
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iScrPlayer Interface](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iScrPlayer_Interface)
- Revision: `3932`
- Source update: `2020-08-06T15:09:44Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

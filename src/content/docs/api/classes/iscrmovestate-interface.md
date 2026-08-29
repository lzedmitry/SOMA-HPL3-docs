---
title: iScrMoveState Interface
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iScrMoveState_Interface"
sourceRevision: 3931
sourceUpdated: "2020-08-06T15:09:30Z"
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
iScrMoveState_Interface has no public fields.

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
cLuxMoveState@
```
](https://wiki.frictionalgames.com/page/../cLuxMoveState) | GetBase |   |   |
| 
```
bool
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
bool
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
 | OnEnterState | 
```
int alPrevStateId
```
 |   |
| 
```
void
```
 | OnLeaveState | 
```
int alNextStateId
```
 |   |
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
 | Reset |   |   |
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iScrMoveState Interface](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iScrMoveState_Interface)
- Revision: `3931`
- Source update: `2020-08-06T15:09:30Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

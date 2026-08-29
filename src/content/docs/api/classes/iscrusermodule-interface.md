---
title: iScrUserModule Interface
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iScrUserModule_Interface"
sourceRevision: 3935
sourceUpdated: "2020-08-06T15:10:25Z"
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
iScrUserModule_Interface has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AppGotInputFocus |   |   |
| 
```
void
```
 | AppLostInputFocus |   |   |
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
| [
```
cLuxUserModule@
```
](https://wiki.frictionalgames.com/page/../cLuxUserModule) | GetBase |   |   |
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
 | OnPostRender | 
```
float afFrameTime
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
 | Update | 
```
float afTimeStep
```
 |   |
| 
```
void
```
 | VariableUpdate | 
```
float afDeltaTime
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iScrUserModule Interface](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iScrUserModule_Interface)
- Revision: `3935`
- Source update: `2020-08-06T15:10:25Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

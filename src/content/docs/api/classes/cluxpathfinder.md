---
title: cLuxPathfinder
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxPathfinder"
sourceRevision: 3652
sourceUpdated: "2020-08-06T13:58:40Z"
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
cLuxPathfinder has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddTrackNode | [
```
const tString &in asNodeName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMinWaitTime
```
,  

```
float afMaxWaitTime
```
,  
[
```
const tString &in asAnimName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abLoopAnim
```
 |   |
| 
```
bool
```
 | BuildPathNodeArrayToPos | [
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | CheckFreePath | [
```
const cVector3f& avStartPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f& avTargetPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | ClearTrackNodes |   |   |
| 
```
int
```
 | GetCurrentTrackNode |   |   |
| [
```
cLuxTrackNode@
```
](https://wiki.frictionalgames.com/page/../cLuxTrackNode) | GetCurrentTrackNodeData |   |   |
| 
```
float
```
 | GetCurrentTrackWaitTime |   |   |
| 
```
bool
```
 | GetDebugLOSCastResult | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetDebugLOSCastResultNum |   |   |
| 
```
bool
```
 | GetDebugLOSPathResult | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetDebugLOSPathResultNum |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetDebugLOSPoint | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetDebugLOSPointNum |   |   |
| [
```
iLuxEntity@
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) | GetEntity |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetNextGoalPos |   |   |
| [
```
cAINode@
```
](https://wiki.frictionalgames.com/page/../cAINode) | GetNodeAtPos | [
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afMinDistance
```
,  

```
float afMaxDistance
```
,  

```
bool abGetClosest
```
,  

```
bool abPosToNodeFreeDirectPathCheck
```
,  

```
bool abAgentToNodeFreeDirectPathCheck
```
,  
[
```
cAINode@ apSkipNode
```
](https://wiki.frictionalgames.com/page/../cAINode),  

```
int alFreePathRayNum
```
,  

```
uint alFreePathFlags
```
,  

```
bool abSkipUsedNodes
```
 |   |
| [
```
cAINode@
```
](https://wiki.frictionalgames.com/page/../cAINode) | GetNodeAtPos | [
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afMinDistance
```
,  

```
float afMaxDistance
```
,  

```
bool abGetClosest
```
,  

```
bool abPosToNodeFreeDirectPathCheck
```
,  

```
bool abAgentToNodeFreeDirectPathCheck
```
,  
[
```
cAINode@ apSkipNode
```
](https://wiki.frictionalgames.com/page/../cAINode) |   |
| [
```
cAINodeContainer@
```
](https://wiki.frictionalgames.com/page/../cAINodeContainer) | GetNodeContainer |   |   |
| [
```
cAINode@
```
](https://wiki.frictionalgames.com/page/../cAINode) | GetNodeFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cAINode@
```
](https://wiki.frictionalgames.com/page/../cAINode) | GetNodeInPosLOS | [
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afMinDistance
```
,  

```
float afMaxDistance
```
,  

```
bool abAgentToNodeFreeDirectPathCheck = false
```
 |   |
| 
```
float
```
 | GetPathNodeArrayDist | 
```
int alIdx
```
 |   |
| 
```
float
```
 | GetPathNodeArrayFullLength |   |   |
| [
```
cAINode@
```
](https://wiki.frictionalgames.com/page/../cAINode) | GetPathNodeArrayNode | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetPathNodeArraySize |   |   |
| 
```
bool
```
 | GetTrackActive |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetTrackCallback |   |   |
| 
```
bool
```
 | GetTrackLoop |   |   |
| [
```
cLuxTrackNode@
```
](https://wiki.frictionalgames.com/page/../cLuxTrackNode) | GetTrackNode | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetTrackNodeNum |   |   |
| 
```
bool
```
 | GetTrackPaused |   |   |
| 
```
float
```
 | GetTrackUpdateFreq |   |   |
| [
```
eLuxEntityComponentType
```
](https://wiki.frictionalgames.com/page/../eLuxEntityComponentType) | GetType |   |   |
| 
```
void
```
 | GoToNextTrackNode |   |   |
| 
```
bool
```
 | IsMoving |   |   |
| 
```
void
```
 | MoveTo | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afUpdateFreq
```
,  

```
bool abExactStopAtEnd
```
,  
[
```
const tString &in asResultCallback = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCallbackInMap = false
```
 |   |
| 
```
void
```
 | MoveToNode | [
```
const tString &in asNodeName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afUpdateFreq
```
,  

```
bool abExactStopAtEnd
```
,  
[
```
const tString &in asResultCallback = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCallbackInMap = false
```
 |   |
| 
```
void
```
 | ResetCurrentTrackNode |   |   |
| 
```
void
```
 | SetCurrentTrackWaitTime | 
```
float afX
```
 |   |
| 
```
void
```
 | SetEndOfPathCallbackFunc | [
```
const tString& asCallbackFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetMaxEdgeDistance | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMaxEdges | 
```
int alX
```
 |   |
| 
```
void
```
 | SetMaxHeight | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMinEdges | 
```
int alX
```
 |   |
| 
```
void
```
 | SetNodeContainerName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetNodeIsAtCenter | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetNodeName | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetTrackLoop | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetTrackPaused | 
```
bool abX
```
 |   |
| 
```
void
```
 | StartTrack | 
```
bool abLoop
```
,  

```
float afUpdateFreq
```
,  
[
```
const tString& asEndOfTrackCallback
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Stop |   |   |
| 
```
void
```
 | StopTrack |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxPathfinder](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxPathfinder)
- Revision: `3652`
- Source update: `2020-08-06T13:58:40Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: cActorAnimController
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cActorAnimController"
sourceRevision: 3524
sourceUpdated: "2020-08-06T13:18:15Z"
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
cActorAnimController has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | BeginLipsync | [
```
iLipsyncResult@ apLipsync
```
](https://wiki.frictionalgames.com/page/../iLipsyncResult) |   |
| 
```
void
```
 | PlayEmotion | [
```
const tString &in asEmotion
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDuration
```
,  

```
float afWeight = 1.0f
```
,  

```
float afFadeTime = 0.1f
```
 |   |
| 
```
void
```
 | PlayGesture | 
```
int alID
```
,  
[
```
const tString &in asGesture
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Stop | 
```
bool abFadeOut = false
```
 |   |
| 
```
void
```
 | StopLipsync |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cActorAnimController](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cActorAnimController)
- Revision: `3524`
- Source update: `2020-08-06T13:18:15Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

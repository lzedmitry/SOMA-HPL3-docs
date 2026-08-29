---
title: cAction
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cAction"
sourceRevision: 3523
sourceUpdated: "2020-08-06T13:17:51Z"
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
cAction has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddGamepadAxis | 
```
int alPadIndex
```
,  
[
```
eGamepadAxis aAxis
```
](https://wiki.frictionalgames.com/page/../eGamepadAxis),  
[
```
eGamepadAxisRange aRange
```
](https://wiki.frictionalgames.com/page/../eGamepadAxisRange),  

```
float afMinThreshold
```
,  

```
float afMaxThreshold
```
 |   |
| 
```
void
```
 | AddGamepadButton | 
```
int alPadIndex
```
,  
[
```
eGamepadButton aButton
```
](https://wiki.frictionalgames.com/page/../eGamepadButton) |   |
| 
```
void
```
 | AddGamepadHat | 
```
int alPadIndex
```
,  
[
```
eGamepadHat aHat
```
](https://wiki.frictionalgames.com/page/../eGamepadHat),  
[
```
eGamepadHatState aHatState
```
](https://wiki.frictionalgames.com/page/../eGamepadHatState) |   |
| 
```
void
```
 | AddKey | [
```
eKey aKey
```
](https://wiki.frictionalgames.com/page/../eKey) |   |
| 
```
void
```
 | AddMouseButton | [
```
eMouseButton aButton
```
](https://wiki.frictionalgames.com/page/../eMouseButton) |   |
| 
```
void
```
 | AddSubAction | [
```
iSubAction@ apSubAction
```
](https://wiki.frictionalgames.com/page/../iSubAction) |   |
| 
```
bool
```
 | BecameTriggered |   |   |
| 
```
void
```
 | ClearSubActions |   |   |
| 
```
bool
```
 | DoubleTriggered | 
```
float afLimit
```
 |   |
| 
```
int
```
 | GetId |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
iSubAction@
```
](https://wiki.frictionalgames.com/page/../iSubAction) | GetSubAction | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetSubActionNum |   |   |
| 
```
bool
```
 | IsTriggered |   |   |
| 
```
void
```
 | ResetToCurrentState |   |   |
| 
```
bool
```
 | WasTriggered |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cAction](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cAction)
- Revision: `3523`
- Source update: `2020-08-06T13:17:51Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

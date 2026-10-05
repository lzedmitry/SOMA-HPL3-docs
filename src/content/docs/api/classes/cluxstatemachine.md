---
title: cLuxStateMachine
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxStateMachine"
sourceRevision: 3666
sourceUpdated: "2020-08-06T14:07:17Z"
lastSynced: "2026-10-05T14:11:59Z"
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
cLuxStateMachine has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddState | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
 |   |
| 
```
void
```
 | AddSubState | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
 |   |
| 
```
void
```
 | AddTimer | 
```
uint64 alId
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
 | AddTimer | [
```
const tString& asId
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
 |   |
| 
```
void
```
 | ChangeState | 
```
int alState
```
 |   |
| 
```
void
```
 | ChangeSubState | 
```
int alState
```
 |   |
| [
```
cLuxEntityMessageData@
```
](https://wiki.frictionalgames.com/page/../cLuxEntityMessageData) | GetCurrentMessageData |   |   |
| 
```
int
```
 | GetCurrentState |   |   |
| 
```
int
```
 | GetCurrentSubState |   |   |
| [
```
iLuxEntity@
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) | GetEntity |   |   |
| 
```
int
```
 | GetNextState |   |   |
| 
```
int
```
 | GetNextSubState |   |   |
| 
```
int
```
 | GetPrevState |   |   |
| 
```
int
```
 | GetPrevSubState |   |   |
| [
```
eLuxEntityComponentType
```
](https://wiki.frictionalgames.com/page/../eLuxEntityComponentType) | GetType |   |   |
| 
```
void
```
 | StopTimer | 
```
uint64 alId
```
 |   |
| 
```
void
```
 | StopTimer | [
```
const tString& asId
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | TimerExists | 
```
uint64 alId
```
 |   |
| 
```
bool
```
 | TimerExists | [
```
const tString& asId
```
](https://wiki.frictionalgames.com/page/../tString) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxStateMachine](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxStateMachine)
- Revision: `3666`
- Source update: `2020-08-06T14:07:17Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

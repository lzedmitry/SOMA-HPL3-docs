---
title: cLuxUserModule
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxUserModule"
sourceRevision: 3669
sourceUpdated: "2020-08-06T14:07:52Z"
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
| Field Name | Type | Description |
| --- | --- | --- |
| mlId | 
```
int
```
 |   |

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | Fader_ClearAll |   |   |
| 
```
void
```
 | Fader_FadeTo | 
```
uint alID
```
,  

```
float afGoal
```
,  

```
float afTime
```
,  

```
bool abReverseAtEnd = false
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
void
```
 | Fader_FadeTo | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afGoal
```
,  

```
float afTime
```
,  

```
bool abReverseAtEnd = false
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
float
```
 | Fader_GetValue | 
```
uint alID
```
,  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
float
```
 | Fader_GetValue | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
void
```
 | Fader_Set | 
```
uint alID
```
,  

```
float afX
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
void
```
 | Fader_Set | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afX
```
,  

```
bool abSkipIfExists = false
```
 |   |
| 
```
void
```
 | Fader_SetPaused | 
```
uint alID
```
,  

```
bool abPaused
```
 |   |
| 
```
void
```
 | Fader_SetPaused | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abPaused
```
 |   |
| 
```
void
```
 | SetScriptableIsSaved | 
```
bool abX
```
 |   |
| 
```
void
```
 | Timer_Add | 
```
uint64 alID
```
,  

```
float afTime
```
,  
[
```
const tString &in asFunc = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfExist = true
```
,  

```
bool abRepeat = false
```
 |   |
| 
```
void
```
 | Timer_Add | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
,  
[
```
const tString &in asFunc = ""
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfExist = true
```
,  

```
bool abRepeat = false
```
 |   |
| 
```
void
```
 | Timer_ClearAll |   |   |
| 
```
bool
```
 | Timer_Exists | 
```
uint64 alID
```
 |   |
| 
```
bool
```
 | Timer_Exists | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | Timer_GetTimeLeft | 
```
uint64 alID
```
 |   |
| 
```
float
```
 | Timer_GetTimeLeft | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
float
```
 | Timer_GetValue | 
```
uint64 alID
```
,  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
float
```
 | Timer_GetValue | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMin = 0
```
,  

```
float afMax = 1
```
,  
[
```
eEasing aEasing = eEasing_Linear
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abAbsValue = false
```
 |   |
| 
```
void
```
 | Timer_Remove | 
```
uint64 alID
```
 |   |
| 
```
void
```
 | Timer_Remove | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Timer_SetPaused | 
```
uint64 alID
```
,  

```
bool abX
```
 |   |
| 
```
void
```
 | Timer_SetPaused | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abX
```
 |   |
| 
```
bool
```
 | Timer_TimeHasPassed | 
```
uint64 alID
```
,  

```
float afLength
```
 |   |
| 
```
bool
```
 | Timer_TimeHasPassed | [
```
const tString &in asID
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afLength
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxUserModule](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxUserModule)
- Revision: `3669`
- Source update: `2020-08-06T14:07:52Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

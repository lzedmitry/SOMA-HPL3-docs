---
title: cLuxDialogHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxDialogHandler"
sourceRevision: 3624
sourceUpdated: "2020-08-06T13:51:10Z"
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
cLuxDialogHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddBranch | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asNextBranch
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddBranchEvent | [
```
eLuxDialogBranchEvent aType
```
](https://wiki.frictionalgames.com/page/../eLuxDialogBranchEvent),  

```
float afVar
```
,  
[
```
const tString &in asVar
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asNewBranch
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abOnlyCheckEndOfSubject
```
 |   |
| 
```
void
```
 | AddBranchPause | 
```
float afTime
```
,  
[
```
const tString &in asCallback
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddBranchSubject | [
```
const tString &in asSubject
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asCallback
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddResponseCondition | [
```
eLuxDialogOptionCondition aCondition
```
](https://wiki.frictionalgames.com/page/../eLuxDialogOptionCondition),  
[
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alValue
```
 |   |
| 
```
void
```
 | AddResponseEvent | [
```
eLuxDialogOptionEvent aEvent
```
](https://wiki.frictionalgames.com/page/../eLuxDialogOptionEvent),  
[
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alValue
```
 |   |
| 
```
void
```
 | AddResponseOption | [
```
const tString& asEntry
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asBranch
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
,  
[
```
const tString &in asCallback
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Begin | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | CharacterIsActive | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | End | [
```
const tString &in asStartBranch
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetCharacterScene | [
```
const tString &in asCharacterName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | GetCharactersInSubject | [
```
const tString &in asSubject
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
int
```
 | GetVar | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | IncVar | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alX
```
 |   |
| 
```
void
```
 | ReturnResponseSelectChoice | 
```
int alSelectedOption
```
 |   |
| 
```
void
```
 | SetCallbackFunc | [
```
const tString &in asFunc
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetResponseTimeLimit | 
```
float afTime
```
 |   |
| 
```
void
```
 | SetVar | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alX
```
 |   |
| 
```
void
```
 | Stop | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | StopAll |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxDialogHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxDialogHandler)
- Revision: `3624`
- Source update: `2020-08-06T13:51:10Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

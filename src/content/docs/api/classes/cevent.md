---
title: cEvent
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cEvent"
sourceRevision: 3551
sourceUpdated: "2020-08-06T13:27:59Z"
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
cEvent has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddActionFactSet | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddActionFloatOp | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afValue
```
,  
[
```
eEventOpType aOpType
```
](https://wiki.frictionalgames.com/page/../eEventOpType) |   |
| 
```
void
```
 | AddActionIntOp | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alValue
```
,  
[
```
eEventOpType aOpType
```
](https://wiki.frictionalgames.com/page/../eEventOpType) |   |
| 
```
void
```
 | AddActionStringSet | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asValue
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddCriteria | [
```
const tString &in asFactName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddCriteriaFloatCompare | [
```
const tString &in asFactName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afValue
```
,  
[
```
eEventCompareType aCompareType
```
](https://wiki.frictionalgames.com/page/../eEventCompareType) |   |
| 
```
void
```
 | AddCriteriaFloatCompare | [
```
const tString &in asFactName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMin
```
,  

```
float afMax
```
,  
[
```
eEventCompareType aCompareType
```
](https://wiki.frictionalgames.com/page/../eEventCompareType) |   |
| 
```
void
```
 | AddCriteriaIntCompare | [
```
const tString &in asFactName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alValue
```
,  
[
```
eEventCompareType aCompareType
```
](https://wiki.frictionalgames.com/page/../eEventCompareType) |   |
| 
```
void
```
 | AddCriteriaIntCompare | [
```
const tString &in asFactName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alMin
```
,  

```
int alMax
```
,  
[
```
eEventCompareType aCompareType
```
](https://wiki.frictionalgames.com/page/../eEventCompareType) |   |
| 
```
void
```
 | AddCriteriaStringCompare | [
```
const tString &in asFactName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asValue
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
eEventCompareType aCompareType
```
](https://wiki.frictionalgames.com/page/../eEventCompareType) |   |
| 
```
int
```
 | GetActionNum |   |   |
| 
```
int
```
 | GetCriterionNum |   |   |
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
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetOutput |   |   |
| 
```
int
```
 | GetOutputId | 
```
int alId
```
 |   |
| 
```
void
```
 | SetOutput | [
```
const tString &in asOutput
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetOutputId | 
```
int alId
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cEvent](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cEvent)
- Revision: `3551`
- Source update: `2020-08-06T13:27:59Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

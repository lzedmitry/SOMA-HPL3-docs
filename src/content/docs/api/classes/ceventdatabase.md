---
title: cEventDatabase
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cEventDatabase"
sourceRevision: 3552
sourceUpdated: "2020-08-06T13:28:14Z"
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
cEventDatabase has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cEvent@
```
](https://wiki.frictionalgames.com/page/../cEvent) | AddEvent | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asOwner
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asTrigger
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Clear |   |   |
| [
```
cFactStateContainer@
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) | CreateFactStateContainer |   |   |
| 
```
void
```
 | DestroyFactStateContainer | [
```
cFactStateContainer@ apContainer
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) |   |
| [
```
cFactStateContainer@
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) | GetDefaultMemory |   |   |
| [
```
cEvent@
```
](https://wiki.frictionalgames.com/page/../cEvent) | GetEvent | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetEventNum |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
cEventOwner@
```
](https://wiki.frictionalgames.com/page/../cEventOwner) | GetOwner | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfNotExist
```
 |   |
| [
```
cEventScene@
```
](https://wiki.frictionalgames.com/page/../cEventScene) | GetScene | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfNotExist
```
 |   |
| [
```
cEventTrigger@
```
](https://wiki.frictionalgames.com/page/../cEventTrigger) | GetTrigger | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCreateIfNotExist
```
 |   |
| 
```
void
```
 | PerformEventActions | [
```
cEvent@ apEvent
```
](https://wiki.frictionalgames.com/page/../cEvent) |   |
| 
```
void
```
 | QueryAddFactStates | [
```
cFactStateContainer@ apFactStates
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) |   |
| 
```
void
```
 | QueryBegin | [
```
cFactStateContainer@ apCustomMemory
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) |   |
| [
```
cEvent@
```
](https://wiki.frictionalgames.com/page/../cEvent) | QueryExecute | [
```
const tString &in asOwner
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asTrigger
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asScene
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abPerformEventActions
```
 |   |
| [
```
cEvent@
```
](https://wiki.frictionalgames.com/page/../cEvent) | QueryExecuteMultiOwner | 
```
int alOwnerFlags
```
,  
[
```
const tString& asTrigger
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asScene
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abPerformEventActions
```
 |   |
| 
```
void
```
 | SetupData |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cEventDatabase](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cEventDatabase)
- Revision: `3552`
- Source update: `2020-08-06T13:28:14Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

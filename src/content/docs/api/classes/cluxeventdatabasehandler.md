---
title: cLuxEventDatabaseHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxEventDatabaseHandler"
sourceRevision: 3636
sourceUpdated: "2020-08-06T13:53:32Z"
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
cLuxEventDatabaseHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cEventDatabase@
```
](https://wiki.frictionalgames.com/page/../cEventDatabase) | GetEventDataBase |   |   |
| [
```
cEvent@
```
](https://wiki.frictionalgames.com/page/../cEvent) | Query | [
```
const tString& asOwner
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asTrigger
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
cFactStateContainer@ apExtraFacts
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) |   |
| [
```
cEvent@
```
](https://wiki.frictionalgames.com/page/../cEvent) | QueryToAll | 
```
int alOwnerFlags
```
,  
[
```
const tString &in asTrigger
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
cFactStateContainer@ apExtraFacts
```
](https://wiki.frictionalgames.com/page/../cFactStateContainer) |   |
| 
```
void
```
 | RemoveGlobalFact | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | RemoveLocalFact | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetGlobalFact | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetGlobalFactFloat | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afVal
```
 |   |
| 
```
void
```
 | SetGlobalFactInt | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alVal
```
 |   |
| 
```
void
```
 | SetGlobalFactString | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asStr
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetLocalFact | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetLocalFactFloat | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afVal
```
 |   |
| 
```
void
```
 | SetLocalFactInt | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alVal
```
 |   |
| 
```
void
```
 | SetLocalFactString | [
```
const tString &in asFact
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asStr
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | UseStandardTriggers |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxEventDatabaseHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxEventDatabaseHandler)
- Revision: `3636`
- Source update: `2020-08-06T13:53:32Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: cLuxSaveHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxSaveHandler"
sourceRevision: 3656
sourceUpdated: "2020-08-06T14:00:51Z"
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
cLuxSaveHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
bool
```
 | AutoSave | 
```
bool abSaveCheckpoint
```
,  

```
bool abDelayed = true
```
 |   |
| 
```
void
```
 | ContinueLoading | 
```
bool abDisableWaits
```
 |   |
| 
```
void
```
 | DelayedLoadGameFromFile | [
```
const tWString &in asSaveFile
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const tString &in asCallbackObject
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asCallbackFunction
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abWaitAfterHeader
```
,  

```
bool abWaitAfterLoad
```
 |   |
| 
```
void
```
 | DelayedSaveGameToFile | [
```
const tWString &in asSaveFile
```
](https://wiki.frictionalgames.com/page/../tWString),  

```
bool abSaveAsCheckpoint
```
 |   |
| 
```
void
```
 | DeleteSaveFile | [
```
const tWString &in asSaveFile
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
bool
```
 | GetSaveFiles |   |   |
| 
```
bool
```
 | GetSaveThreadActive |   |   |
| 
```
bool
```
 | HasLoadError | [
```
tString &out asError
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | IsDoneLoadingHeader |   |   |
| 
```
bool
```
 | IsDoneLoadingSavedGame |   |   |
| 
```
void
```
 | LoadGameFromFile | [
```
const tWString &in asSaveFile
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | SaveGameToFile | [
```
const tWString &in asSaveFile
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | StartLoadedGame |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxSaveHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxSaveHandler)
- Revision: `3656`
- Source update: `2020-08-06T14:00:51Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: iLowLevelGraphics
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iLowLevelGraphics"
sourceRevision: 3900
sourceUpdated: "2020-08-06T15:02:38Z"
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
iLowLevelGraphics has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | DrawBoxMinMax | [
```
const cVector3f &in avMin
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avMax
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawLine | [
```
const cVector3f &in avBegin
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avEnd
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawLineQuad | [
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawSphere | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afRadius
```
,  
[
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
int alSegments = 32
```
 |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetGraphicsInfo |   |   |
| 
```
int
```
 | GetNumDisplays |   |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetScreenSizeFloat |   |   |
| [
```
const cVector2l&
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetScreenSizeInt |   |   |
| [
```
cVector2l
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetWindowPosition |   |   |
| 
```
void
```
 | SetBrightness | 
```
float afX
```
 |   |
| 
```
void
```
 | SetDisplayMode | [
```
eDisplayMode aMode
```
](https://wiki.frictionalgames.com/page/../eDisplayMode) |   |
| 
```
void
```
 | SetVsyncMode | [
```
eVSyncMode aMode
```
](https://wiki.frictionalgames.com/page/../eVSyncMode) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iLowLevelGraphics](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iLowLevelGraphics)
- Revision: `3900`
- Source update: `2020-08-06T15:02:38Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

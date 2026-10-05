---
title: cTerrain
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cTerrain"
sourceRevision: 3724
sourceUpdated: "2020-08-06T14:22:39Z"
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
cTerrain has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
float
```
 | GetChangePatchLevelDist |   |   |
| 
```
int
```
 | GetGeometryGridNum |   |   |
| 
```
int
```
 | GetGeometryPatchSize |   |   |
| 
```
int
```
 | GetHeightMapSize |   |   |
| 
```
float
```
 | GetMaterialSpecularPower |   |   |
| 
```
float
```
 | GetMaxHeight |   |   |
| 
```
void
```
 | GetStartAndSizeInTextureGrid | [
```
const cVector2f &in avStart
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
cVector2l &out avGridStart
```
](https://wiki.frictionalgames.com/page/../cVector2l),  
[
```
cVector2l &out avGridSize
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| 
```
int
```
 | GetTextureGridNum |   |   |
| 
```
int
```
 | GetTexturePatchSize |   |   |
| 
```
float
```
 | GetUnitSize |   |   |
| 
```
bool
```
 | GetWorldPosHeightAndNormal | [
```
const cVector3f &in avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float& afHeight
```
,  
[
```
cVector3f& avNormal
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetChangePatchLevelDist | 
```
float afX
```
 |   |
| 
```
void
```
 | SetCheapMaterial | [
```
const tString &in asCheapMaterial
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afCheapMaterialMul
```
 |   |
| 
```
void
```
 | SetGeometryPatchSize | 
```
int alX
```
 |   |
| 
```
void
```
 | SetMaxHeight | 
```
float afX
```
 |   |
| 
```
void
```
 | SetTexturePatchSize | 
```
int alX
```
 |   |
| 
```
void
```
 | SetUnitSize | 
```
float afX
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cTerrain](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cTerrain)
- Revision: `3724`
- Source update: `2020-08-06T14:22:39Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

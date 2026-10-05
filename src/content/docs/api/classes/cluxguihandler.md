---
title: cLuxGuiHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxGuiHandler"
sourceRevision: 3640
sourceUpdated: "2020-08-06T13:54:49Z"
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
cLuxGuiHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AttachCameraTextureToEntity | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
iLuxEntity@ apEnt
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) |   |
| 
```
void
```
 | CreateCameraTexture | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2l &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2l),  

```
uint alFrameRate
```
,  

```
float afFOV
```
,  

```
float afNearPlane
```
,  

```
float afFarPlane
```
 |   |
| 
```
void
```
 | DestroyCameraTexture | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | GetGameHudInputFocus |   |   |
| 
```
void
```
 | SetCameraTextureMatrix | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cMatrixf &in a_mtxCamera
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetCameraTextureSettings | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afFOV
```
,  

```
float afNearPlane
```
,  

```
float afFarPlane
```
 |   |
| 
```
void
```
 | SetGameHudInputFocus | 
```
bool abX
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxGuiHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxGuiHandler)
- Revision: `3640`
- Source update: `2020-08-06T13:54:49Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

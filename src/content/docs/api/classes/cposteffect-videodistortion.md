---
title: cPostEffect VideoDistortion
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cPostEffect_VideoDistortion"
sourceRevision: 3695
sourceUpdated: "2020-08-06T14:15:39Z"
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
cPostEffect_VideoDistortion has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | GetParams | 
```
float& afAmount
```
,  

```
float &out afRandomSeed
```
,  

```
float &out afLineDensity
```
,  

```
float &out afOffsetMul
```
,  
[
```
cVector2f &out avScreenOffset
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
cVector2f &out avScreenBendAmount
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsDisabled |   |   |
| 
```
void
```
 | Reset |   |   |
| 
```
void
```
 | SetActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDisabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetParams | 
```
float afAmount
```
,  

```
float afRandomSeed
```
,  

```
float afLineDensity
```
,  

```
float afOffsetMul
```
,  
[
```
const cVector2f &in avScreenOffset
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avScreenBendAmount
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cPostEffect VideoDistortion](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cPostEffect_VideoDistortion)
- Revision: `3695`
- Source update: `2020-08-06T14:15:39Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

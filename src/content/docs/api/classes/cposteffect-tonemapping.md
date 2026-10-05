---
title: cPostEffect ToneMapping
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cPostEffect_ToneMapping"
sourceRevision: 3694
sourceUpdated: "2020-08-06T14:15:25Z"
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
cPostEffect_ToneMapping has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | FadeExposure | 
```
float afExposure
```
,  

```
float afWhiteCut
```
,  

```
float afTime
```
 |   |
| 
```
void
```
 | FadeGradingTexture | [
```
iTexture@ apGrading
```
](https://wiki.frictionalgames.com/page/../iTexture),  

```
float afTime
```
 |   |
| 
```
void
```
 | FadeWindowExposure | 
```
float afExposure
```
,  

```
float afWhiteCut
```
 |   |
| 
```
bool
```
 | GetBloomActive |   |   |
| 
```
bool
```
 | GetColorGradingActive |   |   |
| 
```
float
```
 | GetExposure |   |   |
| 
```
bool
```
 | GetFilmGrainActive |   |   |
| 
```
void
```
 | GetParams | 
```
float& afKey
```
,  

```
float& afGammaCorrection
```
,  

```
float& afFilmGrainIntensity
```
,  

```
float& afBrightPass
```
,  

```
float& afBloomWidth
```
,  
[
```
cColor& avBloomTint
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float& afBloomFalloff
```
 |   |
| 
```
float
```
 | GetTransitionTime |   |   |
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
 | SetBloomActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetColorGradingActive | 
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
 | SetFilmGrainActive | 
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
float afKey
```
,  

```
float afGammaCorrection
```
,  

```
float afFilmGrainIntensity
```
,  

```
float afBrightPass
```
,  

```
float afBloomWidth
```
,  
[
```
const cColor &in avBloomTint
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afBloomFalloff
```
 |   |
| 
```
void
```
 | SetSRGBGamma | 
```
bool abX
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cPostEffect ToneMapping](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cPostEffect_ToneMapping)
- Revision: `3694`
- Source update: `2020-08-06T14:15:25Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

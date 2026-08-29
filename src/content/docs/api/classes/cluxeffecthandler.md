---
title: cLuxEffectHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxEffectHandler"
sourceRevision: 3632
sourceUpdated: "2020-08-06T13:52:39Z"
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
cLuxEffectHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddEdgeGlowObject | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity),  
[
```
const cColor& aColor
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afAlpha
```
,  

```
float afEdgeThickness
```
,  

```
float afLightLimit
```
 |   |
| 
```
void
```
 | AddGlowObject | [
```
iLuxEntity@ apEntity
```
](https://wiki.frictionalgames.com/page/../iLuxEntity),  

```
float afAlpha
```
,  

```
float afY
```
 |   |
| 
```
void
```
 | FadeIn | 
```
float afTime
```
 |   |
| 
```
void
```
 | FadeOut | 
```
float afTime
```
 |   |
| [
```
iScrEffect_Interface@
```
](https://wiki.frictionalgames.com/page/../iScrEffect_Interface) | GetEffect | 
```
int alId
```
 |   |
| 
```
float
```
 | GetFadeAlpha |   |   |
| 
```
bool
```
 | IsFading |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxEffectHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxEffectHandler)
- Revision: `3632`
- Source update: `2020-08-06T13:52:39Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

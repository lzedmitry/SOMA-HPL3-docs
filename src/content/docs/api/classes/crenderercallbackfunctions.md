---
title: cRendererCallbackFunctions
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cRendererCallbackFunctions"
sourceRevision: 3703
sourceUpdated: "2020-08-06T14:17:41Z"
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
cRendererCallbackFunctions has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | ClearFrameBuffer | 
```
uint aFlags
```
,  

```
bool abUsePosAndSize
```
 |   |
| 
```
void
```
 | DrawCurrent | [
```
eVertexBufferDrawType aDrawType = eVertexBufferDrawType_LastEnum
```
](https://wiki.frictionalgames.com/page/../eVertexBufferDrawType),  

```
int alStart = 0
```
,  

```
int alCount = -1
```
 |   |
| 
```
void
```
 | DrawQuad | [
```
const cVector3f &in aPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avMinUV = 0
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avMaxUV = 1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
bool abInvertY = false
```
,  
[
```
const cColor &in aColor = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawWireFrame | [
```
iVertexBuffer@ apVtxBuffer
```
](https://wiki.frictionalgames.com/page/../iVertexBuffer),  
[
```
const cColor& aColor
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
int alStart = 0
```
,  

```
int alCount = -1
```
 |   |
| [
```
iLowLevelGraphics@
```
](https://wiki.frictionalgames.com/page/../iLowLevelGraphics) | GetLowLevelGfx |   |   |
| 
```
bool
```
 | SetBlendMode | [
```
eMaterialBlendMode aMode
```
](https://wiki.frictionalgames.com/page/../eMaterialBlendMode) |   |
| 
```
bool
```
 | SetChannelMode | [
```
eMaterialChannelMode aMode
```
](https://wiki.frictionalgames.com/page/../eMaterialChannelMode) |   |
| 
```
bool
```
 | SetCullActive | 
```
bool abX
```
 |   |
| 
```
bool
```
 | SetCullMode | [
```
eCullMode aMode
```
](https://wiki.frictionalgames.com/page/../eCullMode) |   |
| 
```
bool
```
 | SetDepthTest | 
```
bool abX
```
 |   |
| 
```
bool
```
 | SetDepthTestFunc | [
```
eDepthTestFunc aFunc
```
](https://wiki.frictionalgames.com/page/../eDepthTestFunc) |   |
| 
```
bool
```
 | SetDepthWrite | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFlatProjection | [
```
const cVector2f& avSize = 1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afMin = -100
```
,  

```
float afMax = 100
```
 |   |
| 
```
void
```
 | SetFlatProjectionMinMax | [
```
const cVector3f& avMin
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f& avMax
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetFrameBuffer | [
```
iFrameBuffer@ apFrameBuffer
```
](https://wiki.frictionalgames.com/page/../iFrameBuffer),  

```
bool abUsePosAndSize = false
```
 |   |
| 
```
void
```
 | SetMatrix | [
```
const cMatrixf &in apMatrix
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetModelViewMatrix | [
```
const cMatrixf &in a_mtxModelView
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetNormalFrustumProjection |   |   |
| 
```
bool
```
 | SetProgram | [
```
iGpuProgram@ apProgram
```
](https://wiki.frictionalgames.com/page/../iGpuProgram) |   |
| 
```
bool
```
 | SetScissorActive | 
```
bool abX
```
 |   |
| 
```
bool
```
 | SetScissorRect | [
```
const cVector2l &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector2l),  
[
```
const cVector2l &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2l),  

```
bool abAutoEnabling
```
 |   |
| 
```
bool
```
 | SetScissorRect | [
```
const cRect2l &in aClipRect
```
](https://wiki.frictionalgames.com/page/../cRect2l),  

```
bool abAutoEnabling
```
 |   |
| 
```
bool
```
 | SetStencilActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetTexture | 
```
int alUnit
```
,  
[
```
iTexture@ apTexture
```
](https://wiki.frictionalgames.com/page/../iTexture) |   |
| 
```
void
```
 | SetTextureRange | [
```
iTexture@ apTexture
```
](https://wiki.frictionalgames.com/page/../iTexture),  

```
int alFirstUnit
```
,  

```
int alLastUnit = kMaxTextureUnits-1
```
 |   |
| 
```
void
```
 | SetVertexBuffer | [
```
iVertexBuffer@ apVtxBuffer
```
](https://wiki.frictionalgames.com/page/../iVertexBuffer) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cRendererCallbackFunctions](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cRendererCallbackFunctions)
- Revision: `3703`
- Source update: `2020-08-06T14:17:41Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: cViewport
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cViewport"
sourceRevision: 3731
sourceUpdated: "2020-08-06T14:24:18Z"
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
cViewport has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddGuiSet | [
```
cGuiSet@ apSet
```
](https://wiki.frictionalgames.com/page/../cGuiSet) |   |
| 
```
void
```
 | AddRendererCallback | [
```
iRendererCallback@ apCallback
```
](https://wiki.frictionalgames.com/page/../iRendererCallback) |   |
| 
```
void
```
 | AddViewportCallback | [
```
iViewportCallback@ apCallback
```
](https://wiki.frictionalgames.com/page/../iViewportCallback) |   |
| [
```
cCamera@
```
](https://wiki.frictionalgames.com/page/../cCamera) | GetCamera |   |   |
| [
```
iFrameBuffer@
```
](https://wiki.frictionalgames.com/page/../iFrameBuffer) | GetFrameBuffer |   |   |
| [
```
const cVector2l&
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetPosition |   |   |
| [
```
cPostEffectComposite@
```
](https://wiki.frictionalgames.com/page/../cPostEffectComposite) | GetPostEffectComposite |   |   |
| [
```
iRenderer@
```
](https://wiki.frictionalgames.com/page/../iRenderer) | GetRenderer |   |   |
| [
```
cRenderSettings@
```
](https://wiki.frictionalgames.com/page/../cRenderSettings) | GetRenderSettings |   |   |
| [
```
const cVector2l&
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetSize |   |   |
| [
```
cPostEffect_ToneMapping@
```
](https://wiki.frictionalgames.com/page/../cPostEffect_ToneMapping) | GetToneMappingEffect |   |   |
| [
```
cWorld@
```
](https://wiki.frictionalgames.com/page/../cWorld) | GetWorld |   |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsListener |   |   |
| 
```
bool
```
 | IsVisible |   |   |
| 
```
void
```
 | RemoveGuiSet | [
```
cGuiSet@ apSet
```
](https://wiki.frictionalgames.com/page/../cGuiSet) |   |
| 
```
void
```
 | RemoveRendererCallback | [
```
iRendererCallback@ apCallback
```
](https://wiki.frictionalgames.com/page/../iRendererCallback) |   |
| 
```
void
```
 | RemoveViewportCallback | [
```
iViewportCallback@ apCallback
```
](https://wiki.frictionalgames.com/page/../iViewportCallback) |   |
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
 | SetCamera | [
```
cCamera@ apCamera
```
](https://wiki.frictionalgames.com/page/../cCamera) |   |
| 
```
void
```
 | SetFrameBuffer | [
```
iFrameBuffer@ apFrameBuffer
```
](https://wiki.frictionalgames.com/page/../iFrameBuffer) |   |
| 
```
void
```
 | SetIsListener | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetPosition | [
```
const cVector2l &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| 
```
void
```
 | SetPostEffectComposite | [
```
cPostEffectComposite@ apPostEffectComposite
```
](https://wiki.frictionalgames.com/page/../cPostEffectComposite) |   |
| 
```
void
```
 | SetRenderer | [
```
iRenderer@ apRenderer
```
](https://wiki.frictionalgames.com/page/../iRenderer) |   |
| 
```
void
```
 | SetSize | [
```
const cVector2l &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| 
```
void
```
 | SetVisible | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetWorld | [
```
cWorld@ apWorld
```
](https://wiki.frictionalgames.com/page/../cWorld),  

```
bool abResetEffects = false
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cViewport](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cViewport)
- Revision: `3731`
- Source update: `2020-08-06T14:24:18Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

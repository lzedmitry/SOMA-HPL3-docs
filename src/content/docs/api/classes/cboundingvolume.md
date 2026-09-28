---
title: cBoundingVolume
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cBoundingVolume"
sourceRevision: 3538
sourceUpdated: "2020-08-06T13:23:39Z"
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
cBoundingVolume has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLocalCenter |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLocalMax |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLocalMin |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetMax |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetMin |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPosition |   |   |
| 
```
float
```
 | GetRadius |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetSize |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetTransform |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetWorldCenter |   |   |
| 
```
void
```
 | SetLocalMinMax | [
```
const cVector3f &in mvMin
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in mvMax
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abUpdateSize = true
```
 |   |
| 
```
void
```
 | SetPosition | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetSize | [
```
const cVector3f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
bool abUpdateSize = true
```
 |   |
| 
```
void
```
 | SetTransform | [
```
const cMatrixf& a_mtxTransform
```
](https://wiki.frictionalgames.com/page/../cMatrixf),  

```
bool abUpdateSize = true
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cBoundingVolume](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cBoundingVolume)
- Revision: `3538`
- Source update: `2020-08-06T13:23:39Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

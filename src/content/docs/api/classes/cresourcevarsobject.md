---
title: cResourceVarsObject
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cResourceVarsObject"
sourceRevision: 3705
sourceUpdated: "2020-08-06T14:18:06Z"
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
cResourceVarsObject has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddVarBool | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abDefault
```
 |   |
| 
```
void
```
 | AddVarColor | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aDefault
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | AddVarFloat | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefault = 0
```
 |   |
| 
```
void
```
 | AddVarInt | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefault
```
 |   |
| 
```
void
```
 | AddVarString | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in alDefault
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AddVarVector2f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | AddVarVector3f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | GetVarBool | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abDefault
```
 |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | GetVarColor | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aDefault
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
float
```
 | GetVarFloat | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefault
```
 |   |
| 
```
int
```
 | GetVarInt | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefault
```
 |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetVarString | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asDefault
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetVarVector2f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetVarVector3f | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cResourceVarsObject](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cResourceVarsObject)
- Revision: `3705`
- Source update: `2020-08-06T14:18:06Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

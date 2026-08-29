---
title: cConfigFile
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cConfigFile"
sourceRevision: 3545
sourceUpdated: "2020-08-06T13:25:46Z"
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
cConfigFile has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | EraseAll |   |   |
| 
```
void
```
 | EraseSetting | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | EraseValue | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | GetBool | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
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
](https://wiki.frictionalgames.com/page/../cColor) | GetColor | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aDefault
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| [
```
const tWString&
```
](https://wiki.frictionalgames.com/page/../tWString) | GetFileLocation |   |   |
| 
```
float
```
 | GetFloat | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
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
 | GetInt | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
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
](https://wiki.frictionalgames.com/page/../tString) | GetString | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
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
tWString
```
](https://wiki.frictionalgames.com/page/../tWString) | GetStringW | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asDefault
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetVector2f | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
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
cVector2l
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetVector2l | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2l &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetVector3f | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| [
```
cVector3l
```
](https://wiki.frictionalgames.com/page/../cVector3l) | GetVector3l | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3l &in avDefault
```
](https://wiki.frictionalgames.com/page/../cVector3l) |   |
| 
```
bool
```
 | Load |   |   |
| 
```
bool
```
 | Save |   |   |
| 
```
void
```
 | SetBool | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abVal
```
 |   |
| 
```
void
```
 | SetColor | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aVal
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetFileLocation | [
```
const tWString &in asFile
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | SetFloat | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afVal
```
 |   |
| 
```
void
```
 | SetInt | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alVal
```
 |   |
| 
```
void
```
 | SetString | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asVal
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetVector2f | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2f &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetVector2l | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector2l &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| 
```
void
```
 | SetVector3f | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetVector3l | [
```
const tString &in asLevel
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3l &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector3l) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cConfigFile](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cConfigFile)
- Revision: `3545`
- Source update: `2020-08-06T13:25:46Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

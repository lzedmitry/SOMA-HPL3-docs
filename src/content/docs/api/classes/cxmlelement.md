---
title: cXmlElement
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cXmlElement"
sourceRevision: 3758
sourceUpdated: "2020-08-06T14:31:48Z"
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
cXmlElement has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cXmlElement@
```
](https://wiki.frictionalgames.com/page/../cXmlElement) | CreateChildElement | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cXmlText@
```
](https://wiki.frictionalgames.com/page/../cXmlText) | CreateChildText | [
```
const tString &in asText
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | GetAttributeBool | [
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
](https://wiki.frictionalgames.com/page/../cColor) | GetAttributeColor | [
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
 | GetAttributeFloat | [
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
 | GetAttributeInt | [
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
](https://wiki.frictionalgames.com/page/../tString) | GetAttributeString | [
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
](https://wiki.frictionalgames.com/page/../cVector2f) | GetAttributeVector2f | [
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
](https://wiki.frictionalgames.com/page/../cVector3f) | GetAttributeVector3f | [
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
cXmlNodeListIterator@
```
](https://wiki.frictionalgames.com/page/../cXmlNodeListIterator) | GetChildIterator |   |   |
| [
```
cXmlElement@
```
](https://wiki.frictionalgames.com/page/../cXmlElement) | GetFirstElement |   |   |
| [
```
cXmlElement@
```
](https://wiki.frictionalgames.com/page/../cXmlElement) | GetFirstElement | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cXmlText@
```
](https://wiki.frictionalgames.com/page/../cXmlText) | GetFirstText |   |   |
| [
```
cXmlText@
```
](https://wiki.frictionalgames.com/page/../cXmlText) | GetFirstText | [
```
const tString &in asText
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
iXmlNode@
```
](https://wiki.frictionalgames.com/page/../iXmlNode) | GetParent |   |   |
| [
```
eXmlNodeType
```
](https://wiki.frictionalgames.com/page/../eXmlNodeType) | GetType |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetValue |   |   |
| 
```
void
```
 | SetAttributeBool | [
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
 | SetAttributeColor | [
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
 | SetAttributeFloat | [
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
 | SetAttributeInt | [
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
 | SetAttributeString | [
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
 | SetAttributeVector2f | [
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
 | SetAttributeVector3f | [
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
 | SetValue | [
```
const tString &in asValue
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cXmlElement@
```
](https://wiki.frictionalgames.com/page/../cXmlElement) | ToElement |   |   |
| [
```
cXmlText@
```
](https://wiki.frictionalgames.com/page/../cXmlText) | ToText |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cXmlElement](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cXmlElement)
- Revision: `3758`
- Source update: `2020-08-06T14:31:48Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

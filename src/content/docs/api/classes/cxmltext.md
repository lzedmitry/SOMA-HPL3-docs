---
title: cXmlText
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cXmlText"
sourceRevision: 3760
sourceUpdated: "2020-08-06T14:32:10Z"
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
cXmlText has no public fields.

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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cXmlText](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cXmlText)
- Revision: `3760`
- Source update: `2020-08-06T14:32:10Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

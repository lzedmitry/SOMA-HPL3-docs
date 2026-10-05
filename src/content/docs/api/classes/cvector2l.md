---
title: cVector2l
description: A two dimensional vector unit whose elements are stored as integers.
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector2l"
sourceRevision: 3726
sourceUpdated: "2020-08-06T14:23:07Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A two dimensional vector unit whose elements are stored as integers.

## Constructors
| Constructor | Description |
| --- | --- |
| 
```
cVector2l(int, int)
```
 | Creates a `cVector2l` with the given element data. |

## Fields
| Field Name | Type | Description |
| --- | --- | --- |
| x | 
```
int
```
 | The integer x value of the vector. |
| y | 
```
int
```
 | The integer y value of the vector. |

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
int
```
 | GetElement | 
```
uint64 alIdx
```
 | Gets the value at the given index. (Indices 0 and 1 are equal to x and y, respectively.) |
| 
```
void
```
 | SetElement | 
```
uint64 alIdx
```
,  

```
int
```
 | Sets the value at the given index to the given value. (Indices 0 and 1 are equal to x and y, respectively.) |
| 
```
int
```
 | SqrLength |   | Returns the length-squared of the vector. |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cVector2l](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector2l)
- Revision: `3726`
- Source update: `2020-08-06T14:23:07Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

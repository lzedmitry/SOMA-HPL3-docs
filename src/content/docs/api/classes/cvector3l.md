---
title: cVector3l
description: A three dimensional vector unit whose elements are stored as integers.
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector3l"
sourceRevision: 3728
sourceUpdated: "2020-08-06T14:23:32Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A three dimensional vector unit whose elements are stored as integers.

## Constructors
| Constructor | Description |
| --- | --- |
| 
```
cVector3l(int, int, int)
```
 | Creates a `cVector3l` with the given element data. |

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
| z | 
```
int
```
 | The integer z value of the vector. |

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
 | Gets the value at the given index. (Indices 0, 1, and 2 are equal to x, y, and z, respectively.) |
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
 | Sets the value at the given index to the given value. (Indices 0, 1, and 2 are equal to x, y, and z, respectively.) |
| 
```
int
```
 | SqrLength |   | Returns the length-squared of this vector. |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cVector3l](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector3l)
- Revision: `3728`
- Source update: `2020-08-06T14:23:32Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

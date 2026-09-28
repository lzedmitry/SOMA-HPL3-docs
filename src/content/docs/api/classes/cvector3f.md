---
title: cVector3f
description: A three dimensional vector unit whose elements are stored as floats.
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector3f"
sourceRevision: 3727
sourceUpdated: "2020-08-06T14:23:18Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A three dimensional vector unit whose elements are stored as floats.

## Constructors
| Constructor | Description |
| --- | --- |
| 
```
cVector3f(float, float, float)
```
 | Creates a `cVector3f` with the given element data. |

## Fields
| Field Name | Type | Description |
| --- | --- | --- |
| x | 
```
float
```
 | The x value of the vector. |
| y | 
```
float
```
 | The y value of the vector. |
| z | 
```
float
```
 | The z value of the vector. |

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
float
```
 | GetElement | 
```
uint64 alIdx
```
 | Gets the value at the given index. (Indices 0, 1, and 2 are equal to x, y, and z, respectively.) |
| 
```
float
```
 | Length |   | Returns the length of this vector. |
| 
```
float
```
 | Normalize |   | Returns the normalization factor for this vector. (See Remarks.) |
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
float afValue
```
 | Sets the value at the given index to the given value. (Indices 0, 1, and 2 are equal to x, y, and z, respectively.) |
| 
```
float
```
 | SqrLength |   | Returns the length-squared of this vector. |

## Remarks
A normalized vector is a vector whose length is equal to one, otherwise known as a unit vector. To convert a vector into a unit vector, get the normalization factor by calling the *Normalize* function, then divide each of the vector's x, y, and z coordinates by that factor.

```
cVector3f vBaseVector(2.0, 5.0, 3.0);
float fNormFactor = vBaseVector.Normalize();
cVector3f vNormalizedVector(vBaseVector.x / fNormFactor, 
                            vBaseVector.y / fNormFactor, 
                            vBaseVector.z / fNormFactor);
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cVector3f](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector3f)
- Revision: `3727`
- Source update: `2020-08-06T14:23:18Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

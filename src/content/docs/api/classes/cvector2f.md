---
title: cVector2f
description: A two dimensional vector unit whose elements are stored as floats.
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector2f"
sourceRevision: 3725
sourceUpdated: "2020-08-06T14:22:53Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A two dimensional vector unit whose elements are stored as floats.

## Constructors
| Constructor | Description |
| --- | --- |
| 
```
cVector2f(float, float)
```
 | Creates a `cVector2f` with the given element data. |

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
 | Gets the value at the given index. (Indices 0 and 1 are equal to x and y, respectively.) |
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
float
```
 | Sets the value at the given index to the given value. (Indices 0 and 1 are equal to x and y, respectively.) |
| 
```
float
```
 | SqrLength |   | Returns the length-squared of this vector. |

## Remarks
A normalized vector is a vector whose length is equal to one, otherwise known as a unit vector. To convert a vector into a unit vector, get the normalization factor by calling the *Normalize* function, then divide each of the vector's x and y coordinates by that factor.

```
cVector2f vBaseVector(2.0, 5.0);
float fNormFactor = vBaseVector.Normalize();
cVector2f vNormalizedVector(vBaseVector.x / fNormFactor, 
                            vBaseVector.y / fNormFactor);
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cVector2f](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cVector2f)
- Revision: `3725`
- Source update: `2020-08-06T14:22:53Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

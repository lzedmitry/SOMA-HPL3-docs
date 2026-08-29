---
title: cMatrixf
description: "A 4x4 matrix which stores its elements as floats. It is frequently used in transformation-related functions. (i.e. translation, rotation, scale, etc.)"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cMatrixf"
sourceRevision: 3676
sourceUpdated: "2020-08-06T14:10:02Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A 4x4 matrix which stores its elements as floats. It is frequently used in transformation-related functions. (i.e. translation, rotation, scale, etc.)

## Constructors
| Constructor | Description |
| --- | --- |
| 
```
cMatrixf()
```
 | Creates a matrix with default values. |
| 
```
cMatrixf(cVector4f, cVector4f, cVector4f, cVector4f)
```
 | Creates a matrix using the given vectors as column data. |
| 
```
cMatrixf(float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float)
```
 | Creates a matrix using the given values as cell data. |

## Fields
cMatrixf has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
float
```
 | GetElement | 
```
uint64
```
,  

```
uint64
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetForward |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetRight |   |   |
| [
```
cMatrixf
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetRotation |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetTranslation |   |   |
| [
```
cMatrixf
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | GetTranspose |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetUp |   |   |
| 
```
void
```
 | SetForward | [
```
const cVector3f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetRight | [
```
const cVector3f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetRotation | 
```
float afXX
```
,  

```
float afXY
```
,  

```
float afXZ
```
,  

```
float afYX
```
,  

```
float afYY
```
,  

```
float afYZ
```
,  

```
float afZX
```
,  

```
float afZY
```
,  

```
float afZZ
```
 |   |
| 
```
void
```
 | SetRotation | [
```
const cMatrixf &in a_mtxRot
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetTranslation | [
```
const cVector3f &in avTrans
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetUp | [
```
const cVector3f &in avVec
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |

## Remarks
To retrieve a value from a matrix, use the `GetElement` function above. The parameters for the `GetElement` function use the format GetElement(columnIndex, rowIndex).

```
cMatrixf m1(cVector4f(0, 1, 2, 3), 
            cVector4f(4, 5, 6, 7), 
	        cVector4f(8, 9, 10, 11), 
	        cVector4f(12, 13, 14, 15));

float f = m1.GetElement(1, 2);

// value of f: 9
```

To do matrix computations, use the [cMath_MatrixXXX](https://wiki.frictionalgames.com/page/cmath_matrixslerp) family of functions.

```
cMatrixf m1(cVector4f(1, 1, 1, 1), 
            cVector4f(2, 2, 2, 2), 
            cVector4f(3, 3, 3, 3), 
            cVector4f(4, 4, 4, 4));

cMatrixf m2(cVector4f(5, 5, 5, 5), 
            cVector4f(6, 6, 6, 6), 
            cVector4f(7, 7, 7, 7), 
            cVector4f(8, 8, 8, 8));
            
cMatrixf m3 = cMath_MatrixMul(m1, m2);

// value of m3: { 26,  26,  26,  26,
//                52,  52,  52,  52,
//                78,  78,  78,  78,
//                104, 104, 104, 104 }
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cMatrixf](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cMatrixf)
- Revision: `3676`
- Source update: `2020-08-06T14:10:02Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

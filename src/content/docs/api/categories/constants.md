---
title: Constants
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Constants"
sourceRevision: 5077
sourceUpdated: "2020-08-24T22:41:30Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Constant Summary
| Return | Function | Description |
| --- | --- | --- |
| `cColor` | [`cColor_Blue`](#ccolor-blue) | The RGBA value of blue. |
| `cColor` | [`cColor_Green`](#ccolor-green) | The RGBA value of green. |
| `cColor` | [`cColor_Red`](#ccolor-red) | The RGBA value of red. |
| `cColor` | [`cColor_White`](#ccolor-white) | The RGBA value of white. |
| `float` | [`cMath_Epsilon`](#cmath-epsilon) | The value of correction for small floating point numbers. |
| `float` | [`cMath_Pi`](#cmath-pi) | Approximate value of pi. |
| `float` | [`cMath_PiDiv2`](#cmath-pidiv2) | Approximate value of pi divided by 2. |
| `float` | [`cMath_PiDiv4`](#cmath-pidiv4) | Approximate value of pi divided by 4. |
| `float` | [`cMath_PiMul2`](#cmath-pimul2) | Approximate value of pi multiplied by 2. |
| `float` | [`cMath_Sqrt2`](#cmath-sqrt2) | Approximate value of the square root of 2 |
| `cMatrixf` | [`cMatrixf_Identity`](#cmatrixf-identity) | The identity matrix. |
| `cMatrixf` | [`cMatrixf_Zero`](#cmatrixf-zero) | A zero-filled matrix. |
| `cQuaternion` | [`cQuaternion_Identity`](#cquaternion-identity) | The quaternion identity. |
| `cVector2f` | [`cVector2f_Down`](#cvector2f-down) | The down-facing 2D vector. |
| `cVector2f` | [`cVector2f_Left`](#cvector2f-left) | The left-facing 2D vector. |
| `cVector2f` | [`cVector2f_MinusOne`](#cvector2f-minusone) | A negative-one-filled 2D vector. |
| `cVector2f` | [`cVector2f_One`](#cvector2f-one) | A one-filled 2D vector. |
| `cVector2f` | [`cVector2f_Right`](#cvector2f-right) | The right-facing 2D vector. |
| `cVector2f` | [`cVector2f_Up`](#cvector2f-up) | The up-facing 2D vector. |
| `cVector2f` | [`cVector2f_Zero`](#cvector2f-zero) | A zero-filled 2D vector. |
| `cVector2l` | [`cVector2l_MinusOne`](#cvector2l-minusone) | A negative-one-filled 2D vector. |
| `cVector3f` | [`cVector3f_Back`](#cvector3f-back) | The backward-facing 3D vector. |
| `cVector3f` | [`cVector3f_Down`](#cvector3f-down) | The down-facing 3D vector. |
| `cVector3f` | [`cVector3f_Forward`](#cvector3f-forward) | The forward-facing 3D vector. |
| `cVector3f` | [`cVector3f_Left`](#cvector3f-left) | The left-facing 3D vector. |
| `cVector3f` | [`cVector3f_MinusOne`](#cvector3f-minusone) | A negative-one-filled 3D vector. |
| `cVector3f` | [`cVector3f_One`](#cvector3f-one) | A one-filled 3D vector. |
| `cVector3f` | [`cVector3f_Right`](#cvector3f-right) | The right-facing 3D vector. |
| `cVector3f` | [`cVector3f_Up`](#cvector3f-up) | The up-facing 3D vector. |
| `cVector3f` | [`cVector3f_Zero`](#cvector3f-zero) | A zero-filled 3D vector. |
| `cVector4f` | [`cVector4f_MinusOne`](#cvector4f-minusone) | A negative-one-filled 4D vector. |
| `cVector4f` | [`cVector4f_One`](#cvector4f-one) | A one-filled 4D vector. |
| `cVector4f` | [`cVector4f_Zero`](#cvector4f-zero) | A zero-filled 4D vector. |
| `tID` | [`tID_Invalid`](#tid-invalid) | The static value of an invalid tID. |

## Constant Detail
    1. `cColor_Blue`

```angelscript
const cColor cColor_Blue = cColor(0.0, 0.0, 1.0, 1.0)
```

The RGBA value of blue.

    1. `cColor_Green`

```angelscript
const cColor cColor_Green = cColor(0.0, 1.0, 0.0, 1.0)
```

The RGBA value of green.

    1. `cColor_Red`

```angelscript
const cColor cColor_Red = cColor(1.0, 0.0, 0.0, 1.0)
```

The RGBA value of red.

    1. `cColor_White`

```angelscript
const cColor cColor_White = cColor(1.0, 1.0, 1.0, 1.0)
```

The RGBA value of white.

    1. `cMath_Epsilon`

```angelscript
const float cMath_Epsilon = 0.0001
```

The value of correction for small floating point numbers.

When two floats are subtracted, floating point errors can make the result not exact. (i.e. 3.0 - 2.0 == 1.0 may not strictly be true.) As such, if the difference between two floats is less than the value of cMath_Epsilon, those two floats can be considered equal.

    1. `cMath_Pi`

```angelscript
const float cMath_Pi = 3.141593
```

Approximate value of pi.

    1. `cMath_PiDiv2`

```angelscript
const float cMath_PiDiv2
```

Approximate value of pi divided by 2.

    1. `cMath_PiDiv4`

```angelscript
const float cMath_PiDiv4
```

Approximate value of pi divided by 4.

    1. `cMath_PiMul2`

```angelscript
const float cMath_PiMul2
```

Approximate value of pi multiplied by 2.

    1. `cMath_Sqrt2`

```angelscript
const float cMath_Sqrt2
```

Approximate value of the square root of 2.

    1. `cMatrixf_Identity`

```angelscript
const cMatrixf cMatrixf_Identity = cMatrixf(1.0, 0.0, 0.0, 0.0,
                                            0.0, 1.0, 0.0, 0.0,
                                            0.0, 0.0, 1.0, 0.0,
                                            0.0, 0.0, 0.0, 1.0)
```

The identity matrix.

    1. `cMatrixf_Zero`

```angelscript
const cMatrixf cMatrixf_Zero = cMatrixf(0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0,
                                        0.0, 0.0, 0.0, 0.0)
```

A zero-filled matrix.

    1. `cQuaternion_Identity`

```angelscript
const cQuaternion cQuaternion_Identity = cQuaternion(0.0, 0.0, 0.0, 1.0)
```

The quaternion identity.

    1. `cVector2f_Down`

```angelscript
const cVector2f cVector2f_Down = cVector2f(0.0, -1.0)
```

The down-facing 2D vector.

    1. `cVector2f_Left`

```angelscript
const cVector2f cVector2f_Left = cVector2f(-1.0, 0.0)
```

The left-facing 2D vector.

    1. `cVector2f_MinusOne`

```angelscript
const cVector2f cVector2f_MinusOne = cVector2f(-1.0, -1.0)
```

A negative-one-filled 2D vector.

    1. `cVector2f_One`

```angelscript
const cVector2f cVector2f_One = cVector2f(1.0, 1.0)
```

A one-filled 2D vector.

    1. `cVector2f_Right`

```angelscript
const cVector2f cVector2f_Right = cVector2f(1.0, 0.0)
```

The right-facing 2D vector.

    1. `cVector2f_Up`

```angelscript
const cVector2f cVector2f_Up = cVector2f(0.0, 1.0)
```

The up-facing 2D vector.

    1. `cVector2f_Zero`

```angelscript
const cVector2f cVector2f_Zero = cVector2f(0.0, 0.0)
```

A zero-filled 2D vector.

    1. `cVector2l_MinusOne`

```angelscript
const cVector2l cVector2l_MinusOne = cVector2l(-1, -1)
```

A negative-one-filled 2D vector.

    1. `cVector3f_Back`

```angelscript
const cVector3f cVector3f_Back = cVector3f(0.0, 0.0, -1.0)
```

The backward-facing 3D vector.

    1. `cVector3f_Down`

```angelscript
const cVector3f cVector3f_Down = cVector3f(0.0, -1.0, 0.0)
```

The down-facing 3D vector.

    1. `cVector3f_Forward`

```angelscript
const cVector3f cVector3f_Forward = cVector3f(0.0, 0.0, 1.0)
```

The forward-facing 3D vector.

    1. `cVector3f_Left`

```angelscript
const cVector3f cVector3f_Left = cVector3f(-1.0, 0.0, 0.0)
```

The left-facing 3D vector.

    1. `cVector3f_MinusOne`

```angelscript
const cVector3f cVector3f_MinusOne = cVector3f(-1.0, -1.0, -1.0)
```

A negative-one-filled 3D vector.

    1. `cVector3f_One`

```angelscript
const cVector3f cVector3f_One = cVector3f(1.0, 1.0, 1.0)
```

A one-filled 3D vector.

    1. `cVector3f_Right`

```angelscript
const cVector3f cVector3f_Right = cVector3f(1.0, 0.0, 0.0)
```

The right-facing 3D vector.

    1. `cVector3f_Up`

```angelscript
const cVector3f cVector3f_Up = cVector3f(0.0, 1.0, 0.0)
```

The up-facing 3D vector.

    1. `cVector3f_Zero`

```angelscript
const cVector3f cVector3f_Zero = cVector3f(0.0, 0.0, 0.0)
```

A zero-filled 3D vector.

    1. `cVector4f_MinusOne`

```angelscript
const cVector4f cVector4f_MinusOne = cVector4f(-1.0, -1.0, -1.0, -1.0)
```

A negative-one-filled 4D vector.

    1. `cVector4f_One`

```angelscript
const cVector4f cVector4f_One = cVector4f(1.0, 1.0, 1.0, 1.0)
```

A one-filled 4D vector.

    1. `cVector4f_Zero`

```angelscript
const cVector4f cVector4f_Zero = cVector4f(0.0, 0.0, 0.0, 0.0)
```

A zero-filled 4D vector.

    1. `tID_Invalid`

```angelscript
const tID tID_Invalid
```

The static value of an invalid tID.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Constants](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Constants)
- Revision: `5077`
- Source update: `2020-08-24T22:41:30Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

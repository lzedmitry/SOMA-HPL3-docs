---
title: Math
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Math"
sourceRevision: 5041
sourceUpdated: "2020-08-24T20:56:47Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `void` | [`Math_CatmullRom`](#math-catmullrom)([cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &out avResult, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avP0, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avP1, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avP2, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avP3, float afFract) | A function that gives you a point along a spline made up of four points |

## Function Detail
    1. `Math_CatmullRom`

```cpp
void Math_CatmullRom(cVector3f &out avResult,
                     const cVector3f &in avP0,
                     const cVector3f &in avP1,
                     const cVector3f &in avP2,
                     const cVector3f &in avP3,
                     float afFract)
```

A function that gives you a point along a spline made up of four points. The spline is guaranteed to hit the second and third points.

| Name | Type | Description |
| --- | --- | --- |
| `avResult` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | the resulting point on the spline. |
| `avP0` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | the first point. |
| `avP1` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | the second point. |
| `avP2` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | the third point. |
| `avP3` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | the fourth point. |
| `afFract` | `float` | the normalized distance along the spline to check. 0 is at the second point, 1 is at the third point. Should not go out of the range 0-1. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Math](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Math)
- Revision: `5041`
- Source update: `2020-08-24T20:56:47Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

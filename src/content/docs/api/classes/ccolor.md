---
title: cColor
description: A four-channel color unit which stores float-based RGBA data. Color channel values are stored using a 0.0 - 1.0 range.
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cColor"
sourceRevision: 3544
sourceUpdated: "2020-08-06T13:25:08Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A four-channel color unit which stores float-based RGBA data. Color channel values are stored using a 0.0 - 1.0 range.

## Constructors
| Constructor | Description |
| --- | --- |
| 
```
cColor()
```
 | Creates a color with a default value of opaque black. |
| 
```
cColor(float, float)
```
 | Creates a color with the first parameter given to all the RGB values (the color will be a shade of grey) and the second parameter given to the alpha channel. |
| 
```
cColor(float, float, float)
```
 | Creates an opaque color using the given values as RGB data. |
| 
```
cColor(float, float, float, float)
```
 | Creates a color using the given values as RGBA data. |

## Fields
| Field Name | Type | Description |
| --- | --- | --- |
| r | 
```
float
```
 | The value of the red channel. |
| g | 
```
float
```
 | The value of the green channel. |
| b | 
```
float
```
 | The value of the blue channel. |
| a | 
```
float
```
 | The value of the alpha channel. |

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | ToLinearSpace | 
```
const float afPower,
```
  

```
const bool abCorrectAlpha,
```
  

```
const
```
 | Returns the color converted into the linear space. (See remarks.) |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | ToSRGB | 
```
const bool abCorrectAlpha,
```
  

```
const
```
 | Returns the color converted into the [sRGB](https://wiki.frictionalgames.com/page/wikipedia:sRGB) space. (See remarks. |

## Remarks
Read [this post on StackOverflow](http://stackoverflow.com/questions/12524623/what-are-the-practical-differences-when-working-with-colors-in-a-linear-vs-a-no) for an explanation on the differences between the linear color space and the sRGB color space.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cColor](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cColor)
- Revision: `3544`
- Source update: `2020-08-06T13:25:08Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

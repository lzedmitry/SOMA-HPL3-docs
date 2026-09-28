---
title: cImGui
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cImGui"
sourceRevision: 3579
sourceUpdated: "2020-08-06T13:38:38Z"
lastSynced: "2026-09-28T13:28:41Z"
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
cImGui has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
bool
```
 | ActionIsDown | [
```
eImGuiAction aAction
```
](https://wiki.frictionalgames.com/page/../eImGuiAction),  

```
bool abCheckIfUsed = false
```
 |   |
| 
```
bool
```
 | ActionTriggered | [
```
eImGuiAction aAction
```
](https://wiki.frictionalgames.com/page/../eImGuiAction),  

```
bool abCheckIfUsed = false
```
 |   |
| 
```
void
```
 | AddItemGfx | [
```
const cImGuiGfx &in aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
void
```
 | AddItemString | [
```
const tWString &in asStr
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | AddItemStringList | [
```
const tWString &in asStrList
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | AddLayoutHorizontalSpace | 
```
float afWidth
```
,  

```
float afHeight = 0
```
 |   |
| 
```
void
```
 | AddLayoutVerticalSpace | 
```
float afHeight
```
 |   |
| 
```
void
```
 | AddLineStripVertex | [
```
const cVector2f& avVertex
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | AddTimer | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
 |   |
| 
```
void
```
 | Begin | 
```
float afTimeStep
```
 |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | CalcWidgetSize | [
```
const cVector2f &in avArgSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avDefaultSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | CheckBecamePressedAction | 
```
bool abCheckConfirm
```
,  

```
bool abCheckMouseLeft
```
 |   |
| 
```
bool
```
 | CheckCurrentWidgetBecamePressed | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCheckConfirm
```
,  

```
bool abCheckMouseLeft
```
 |   |
| 
```
bool
```
 | CheckCurrentWidgetIsPressed | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abCheckConfirm
```
,  

```
bool abCheckMouseLeft
```
 |   |
| 
```
bool
```
 | CheckIsPressedAction | 
```
bool abCheckConfirm
```
,  

```
bool abCheckMouseLeft
```
 |   |
| 
```
bool
```
 | CheckMouseHasMoved |   |   |
| 
```
bool
```
 | CheckMouseOver | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | ClearItems |   |   |
| 
```
void
```
 | ClearPrevData |   |   |
| 
```
void
```
 | ClearStates |   |   |
| 
```
void
```
 | ClipAreaBegin | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | ClipAreaEnd |   |   |
| 
```
void
```
 | DestroyAssets |   |   |
| 
```
bool
```
 | DoButton | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cImGuiButtonData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiButtonData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoButton | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoCheckBox | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  

```
bool abDefaultChecked
```
,  
[
```
const cImGuiCheckBoxData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiCheckBoxData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoCheckBox | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  

```
bool abDefaultChecked
```
,  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoFrame | [
```
const cImGuiFrameData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiFrameData),  
[
```
const cVector3f& avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoFrame | [
```
const cVector3f& avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoGauge | [
```
const cImGuiGaugeData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiGaugeData),  

```
float afFillAmount
```
,  
[
```
const cVector3f& avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoGauge | 
```
float afFillAmount
```
,  
[
```
const cVector3f& avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoImage | [
```
const cImGuiGfx &in aGfxImage
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoLabel | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cImGuiLabelData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiLabelData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afFontSizeMul = 1
```
 |   |
| 
```
void
```
 | DoLabel | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afFontSizeMul = 1
```
 |   |
| 
```
void
```
 | DoMouse | [
```
const cImGuiGfx& aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cVector3f &in avOffset = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
int
```
 | DoMultiSelect | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefaultSelectedItem
```
,  
[
```
const cImGuiMultiSelectData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiMultiSelectData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
int
```
 | DoMultiSelect | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefaultSelectedItem
```
,  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
int
```
 | DoMultiToggle | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefaultSelectedItem
```
,  

```
uint alColumnNum
```
,  
[
```
const cVector2f &in avSpacing
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cImGuiButtonData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiButtonData),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
int
```
 | DoMultiToggle | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefaultSelectedItem
```
,  

```
uint alColumnNum
```
,  
[
```
const cVector2f &in avSpacing
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoRepeatButton | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cImGuiButtonData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiButtonData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoRepeatButton | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | DoSliderHorizontal | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefaultValue
```
,  

```
float afMin
```
,  

```
float afMax
```
,  

```
float afStepSize
```
,  
[
```
const cImGuiSliderData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiSliderData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | DoSliderHorizontal | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefaultValue
```
,  

```
float afMin
```
,  

```
float afMax
```
,  

```
float afStepSize = -1
```
,  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | DoSliderVertical | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefaultValue
```
,  

```
float afMin
```
,  

```
float afMax
```
,  

```
float afStepSize
```
,  
[
```
const cImGuiSliderData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiSliderData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | DoSliderVertical | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefaultValue
```
,  

```
float afMin
```
,  

```
float afMax
```
,  

```
float afStepSize = -1
```
,  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | DoTextFrame | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cVector2f &in avEdgeSpacing
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afRowSpace
```
,  

```
float afStartRowOffset
```
,  
[
```
const cImGuiTextFrameData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiTextFrameData),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | DoTextFrame | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cVector2f &in avEdgeSpacing
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afRowSpace
```
,  

```
float afStartRowOffset
```
,  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoToggleButton | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  

```
bool abDefaultChecked
```
,  
[
```
const cImGuiButtonData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiButtonData),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
bool
```
 | DoToggleButton | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  

```
bool abDefaultChecked
```
,  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | DoWindowEnd |   |   |
| 
```
void
```
 | DoWindowStart | [
```
const tWString& asCaption
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cImGuiWindowData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiWindowData),  
[
```
const cVector3f& avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
bool abClip = true
```
 |   |
| 
```
void
```
 | DoWindowStart | [
```
const tWString& asCaption
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cVector3f& avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
bool abClip = true
```
 |   |
| 
```
void
```
 | DrawAlignedGfx | [
```
const cImGuiGfx& aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
eImGuiAlign aAlignment
```
](https://wiki.frictionalgames.com/page/../eImGuiAlign),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cColor& aCol = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColTopLeft = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColTopRight = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColBotRight = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColBotLeft = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawAll |   |   |
| 
```
void
```
 | DrawAndClearLineStrip | 
```
float afZ
```
,  

```
float afThickness
```
,  
[
```
const cColor& aCol = cColor_White
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cImGuiGfx& aGfx = cImGuiGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
void
```
 | DrawFont | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
const cImGuiFont& aFont
```
](https://wiki.frictionalgames.com/page/../cImGuiFont),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
eFontAlign aAlign
```
](https://wiki.frictionalgames.com/page/../eFontAlign),  
[
```
const cVector2f &in avSizeMul = 1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cColor &in aColMul = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawFrame | [
```
const cImGuiFrameGfx& aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiFrameGfx),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cColor &in aCol = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawGfx | [
```
const cImGuiGfx& aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cColor &in aCol = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColTopLeft = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColTopRight = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColBotRight = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aColBotLeft = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawLine | [
```
const cVector2f &in avStart
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avEnd
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afZ
```
,  

```
float afThickness = 1.0f
```
,  
[
```
const cColor &in aCol = cColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cImGuiGfx& aGfx = cImGuiGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
void
```
 | End |   |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | FadeOscillateColor | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aStart
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
const cColor &in aGoal
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afTime
```
,  
[
```
eEasing aType = eEasing_QuadInOut
```
](https://wiki.frictionalgames.com/page/../eEasing) |   |
| 
```
float
```
 | FadeOscillateFloat | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afStart
```
,  

```
float afGoal
```
,  

```
float afTime
```
,  
[
```
eEasing aType = eEasing_QuadInOut
```
](https://wiki.frictionalgames.com/page/../eEasing) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | FadeOscillateVector3f | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avStart
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector3f &in avGoal
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afTime
```
,  
[
```
eEasing aType = eEasing_QuadInOut
```
](https://wiki.frictionalgames.com/page/../eEasing) |   |
| 
```
bool
```
 | FadeOver | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | FadeStateColor | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aGoalVal
```
](https://wiki.frictionalgames.com/page/../cColor),  

```
float afTime
```
,  
[
```
eEasing aType = eEasing_QuadInOut
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abReplaceIfExist = true
```
 |   |
| 
```
void
```
 | FadeStateFloat | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afGoalVal
```
,  

```
float afTime
```
,  
[
```
eEasing aType = eEasing_QuadInOut
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abReplaceIfExist = true
```
 |   |
| 
```
void
```
 | FadeStateVector3f | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avGoalVal
```
](https://wiki.frictionalgames.com/page/../cVector3f),  

```
float afTime
```
,  
[
```
eEasing aType = eEasing_QuadInOut
```
](https://wiki.frictionalgames.com/page/../eEasing),  

```
bool abReplaceIfExist = true
```
 |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetCurrentGroupPos |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetCurrentGroupSize |   |   |
| [
```
const cImGuiButtonData&
```
](https://wiki.frictionalgames.com/page/../cImGuiButtonData) | GetDefaultButton |   |   |
| [
```
const cImGuiCheckBoxData&
```
](https://wiki.frictionalgames.com/page/../cImGuiCheckBoxData) | GetDefaultCheckBox |   |   |
| [
```
const cImGuiFrameData&
```
](https://wiki.frictionalgames.com/page/../cImGuiFrameData) | GetDefaultFrame |   |   |
| [
```
const cImGuiGaugeData&
```
](https://wiki.frictionalgames.com/page/../cImGuiGaugeData) | GetDefaultGauge |   |   |
| [
```
const cImGuiLabelData&
```
](https://wiki.frictionalgames.com/page/../cImGuiLabelData) | GetDefaultLabel |   |   |
| [
```
const cImGuiMultiSelectData&
```
](https://wiki.frictionalgames.com/page/../cImGuiMultiSelectData) | GetDefaultMultiSelect |   |   |
| 
```
float
```
 | GetDefaultOrCurrentFloat | 
```
uint64 alDefaultVarId
```
,  

```
uint64 alCurrentVarId
```
,  

```
float afDefaultValue
```
 |   |
| 
```
int
```
 | GetDefaultOrCurrentInt | 
```
uint64 alDefaultVarId
```
,  

```
uint64 alCurrentVarId
```
,  

```
int alDefaultValue
```
 |   |
| [
```
const cImGuiSliderData&
```
](https://wiki.frictionalgames.com/page/../cImGuiSliderData) | GetDefaultSliderHorizontal |   |   |
| [
```
const cImGuiSliderData&
```
](https://wiki.frictionalgames.com/page/../cImGuiSliderData) | GetDefaultSliderVertical |   |   |
| [
```
const cImGuiTextFrameData&
```
](https://wiki.frictionalgames.com/page/../cImGuiTextFrameData) | GetDefaultTextFrame |   |   |
| [
```
const cImGuiWindowData&
```
](https://wiki.frictionalgames.com/page/../cImGuiWindowData) | GetDefaultWindow |   |   |
| 
```
float
```
 | GetFontLength | [
```
const cImGuiFont &in aFont
```
](https://wiki.frictionalgames.com/page/../cImGuiFont),  

```
float afSizeMul
```
,  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | GetFontWordWrapRows | [
```
const cImGuiFont &in aFont
```
](https://wiki.frictionalgames.com/page/../cImGuiFont),  

```
float afSizeMul
```
,  
[
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString),  

```
float afLineWidth
```
 |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetGfxSize | [
```
const cImGuiGfx &in aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
uint64
```
 | GetIdFromNameAndCheckCollision | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alTableIdx
```
 |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetMousePosition |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetMousePosition3D |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetMouseRel |   |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetMouseRel3D |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
cGuiSet@
```
](https://wiki.frictionalgames.com/page/../cGuiSet) | GetSet |   |   |
| 
```
bool
```
 | GetShowMouse |   |   |
| 
```
bool
```
 | GetShowMouseAutomatically |   |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | GetStateColor | 
```
uint64 alId
```
,  
[
```
const cColor &in aDefault = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | GetStateColor | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cColor &in aDefault = cColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
float
```
 | GetStateFloat | 
```
uint64 alId
```
,  

```
float afDefault = 0.0f
```
 |   |
| 
```
float
```
 | GetStateFloat | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afDefault = 0.0f
```
 |   |
| 
```
int
```
 | GetStateInt | 
```
uint64 alId
```
,  

```
int alDefault = 0
```
 |   |
| 
```
int
```
 | GetStateInt | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alDefault = 0
```
 |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetStateVector3f | 
```
uint64 alId
```
,  
[
```
const cVector3f &in avDefault = 0.0f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| [
```
cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetStateVector3f | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avDefault = cVector3f
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
float
```
 | GetTimeCount |   |   |
| 
```
float
```
 | GetTimeStep |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetUsedFontSize | [
```
const cImGuiFont &in aFont
```
](https://wiki.frictionalgames.com/page/../cImGuiFont) |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetUsedGfxSize | [
```
const cImGuiGfx &in aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cVector2f &in avCustomSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | GroupBegin | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = 0
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
bool abClip = false
```
 |   |
| 
```
void
```
 | GroupEnd |   |   |
| 
```
void
```
 | IncStateColor | 
```
uint64 alId
```
,  
[
```
const cColor &in aVal
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | IncStateColor | [
```
const tString &in asVarName
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
 | IncStateFloat | 
```
uint64 alId
```
,  

```
float afVal
```
 |   |
| 
```
void
```
 | IncStateFloat | [
```
const tString &in asVarName
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
 | IncStateInt | 
```
uint64 alId
```
,  

```
int alVal
```
 |   |
| 
```
void
```
 | IncStateInt | [
```
const tString &in asVarName
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
 | IncStateVector3f | 
```
uint64 alId
```
,  
[
```
const cVector3f &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | IncStateVector3f | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
bool
```
 | IsFading | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | IsFirstRun |   |   |
| 
```
void
```
 | LayoutBegin | [
```
eImGuiLayout aType
```
](https://wiki.frictionalgames.com/page/../eImGuiLayout),  
[
```
const cVector3f &in avPos = 0
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize = -1
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avSpacing = 0
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | LayoutEnd |   |   |
| 
```
void
```
 | LockMouseFocus |   |   |
| 
```
bool
```
 | MouseFocusIsLocked |   |   |
| 
```
void
```
 | PopModifiers |   |   |
| 
```
bool
```
 | PrevBecameInFocus |   |   |
| 
```
bool
```
 | PrevBecamePressed |   |   |
| 
```
bool
```
 | PrevInFocus |   |   |
| 
```
bool
```
 | PrevMouseOver |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | PrevPosition |   |   |
| 
```
bool
```
 | PrevPressed |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | PrevSize |   |   |
| 
```
bool
```
 | PrevUpdated |   |   |
| 
```
bool
```
 | PrevWasInFocus |   |   |
| 
```
void
```
 | PushModifiers |   |   |
| 
```
bool
```
 | RepeatTimer | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afTime
```
 |   |
| 
```
void
```
 | ResetModifiers |   |   |
| 
```
void
```
 | SendAction | [
```
eImGuiAction aAction
```
](https://wiki.frictionalgames.com/page/../eImGuiAction),  

```
bool abDown
```
,  

```
bool abTriggered
```
 |   |
| 
```
void
```
 | SendMousePosition | [
```
const cVector2l &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector2l),  
[
```
const cVector2l &in avRel
```
](https://wiki.frictionalgames.com/page/../cVector2l) |   |
| 
```
void
```
 | SendMouseVirtualPosition | [
```
const cVector2f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avRel
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetAlignment | [
```
eImGuiAlign aAlign
```
](https://wiki.frictionalgames.com/page/../eImGuiAlign) |   |
| 
```
void
```
 | SetDefaultButton | [
```
const cImGuiButtonData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiButtonData) |   |
| 
```
void
```
 | SetDefaultCheckBox | [
```
const cImGuiCheckBoxData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiCheckBoxData) |   |
| 
```
void
```
 | SetDefaultFont | [
```
const cImGuiFont &in aFont
```
](https://wiki.frictionalgames.com/page/../cImGuiFont) |   |
| 
```
void
```
 | SetDefaultFrame | [
```
const cImGuiFrameData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiFrameData) |   |
| 
```
void
```
 | SetDefaultGauge | [
```
const cImGuiGaugeData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiGaugeData) |   |
| 
```
void
```
 | SetDefaultLabel | [
```
const cImGuiLabelData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiLabelData) |   |
| 
```
void
```
 | SetDefaultMouse | [
```
const cImGuiGfx &in aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
void
```
 | SetDefaultMultiSelect | [
```
const cImGuiMultiSelectData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiMultiSelectData) |   |
| 
```
void
```
 | SetDefaultSliderHorizontal | [
```
const cImGuiSliderData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiSliderData) |   |
| 
```
void
```
 | SetDefaultSliderVertical | [
```
const cImGuiSliderData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiSliderData) |   |
| 
```
void
```
 | SetDefaultTextFrame | [
```
const cImGuiTextFrameData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiTextFrameData) |   |
| 
```
void
```
 | SetDefaultWindow | [
```
const cImGuiWindowData& aData
```
](https://wiki.frictionalgames.com/page/../cImGuiWindowData) |   |
| 
```
void
```
 | SetDrawUIDebugBoxes | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFocus | [
```
const tString &in asWidgetName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetModColorMul | [
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetModGfx | [
```
const cImGuiGfx &in aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
void
```
 | SetModRotateAngle | 
```
float afX
```
 |   |
| 
```
void
```
 | SetModRotateCustomPivot | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetModRotatePivot | [
```
const cVector2f &in avPivot
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetModTextColorMul | [
```
const cColor &in aCol
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetModUISizeHoriExpansion | 
```
float afNeg
```
,  

```
float afPos
```
 |   |
| 
```
void
```
 | SetModUISizeVertExpansion | 
```
float afNeg
```
,  

```
float afPos
```
 |   |
| 
```
void
```
 | SetModUseInput | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetModUseUIPos | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetShowMouse | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetShowMouseAutomatically | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetStateColor | 
```
uint64 alId
```
,  
[
```
const cColor &in aVal
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetStateColor | [
```
const tString &in asVarName
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
 | SetStateFloat | 
```
uint64 alId
```
,  

```
float afVal
```
 |   |
| 
```
void
```
 | SetStateFloat | [
```
const tString &in asVarName
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
 | SetStateInt | 
```
uint64 alId
```
,  

```
int alVal
```
 |   |
| 
```
void
```
 | SetStateInt | [
```
const tString &in asVarName
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
 | SetStateVector3f | 
```
uint64 alId
```
,  
[
```
const cVector3f &in avVal
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetStateVector3f | [
```
const tString &in asVarName
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
 | SetUIMoveGroupFlags | 
```
int alGroupFlags
```
 |   |
| 
```
void
```
 | SetUIMoveWrapMode | [
```
eImGuiWrap aWrap
```
](https://wiki.frictionalgames.com/page/../eImGuiWrap) |   |
| 
```
void
```
 | SetUpAlignment | [
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
cVector3f& avAlignedPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
eImGuiAlign aAlignment
```
](https://wiki.frictionalgames.com/page/../eImGuiAlign) |   |
| 
```
void
```
 | SetupWidgetRect | [
```
const cVector3f &in avInPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avInSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
cVector3f &out avOutPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
cVector2f &out avOutSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cVector2f &in avDefaultSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const cImGuiGfx& aGfx
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx) |   |
| 
```
void
```
 | StopFade | [
```
const tString &in asVarName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | StopTimer | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | TimerExists | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | TimerOver | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cImGui](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cImGui)
- Revision: `3579`
- Source update: `2020-08-06T13:38:38Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

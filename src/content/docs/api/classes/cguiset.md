---
title: cGuiSet
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cGuiSet"
sourceRevision: 3573
sourceUpdated: "2020-08-06T13:34:31Z"
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
cGuiSet has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cWidgetButton@
```
](https://wiki.frictionalgames.com/page/../cWidgetButton) | CreateWidgetButton | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abToggleable
```
,  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetCheckBox@
```
](https://wiki.frictionalgames.com/page/../cWidgetCheckBox) | CreateWidgetCheckBox | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetComboBox@
```
](https://wiki.frictionalgames.com/page/../cWidgetComboBox) | CreateWidgetComboBox | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetContextMenu@
```
](https://wiki.frictionalgames.com/page/../cWidgetContextMenu) | CreateWidgetContextMenu | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetDummy@
```
](https://wiki.frictionalgames.com/page/../cWidgetDummy) | CreateWidgetDummy | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetFrame@
```
](https://wiki.frictionalgames.com/page/../cWidgetFrame) | CreateWidgetFrame | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
bool abDrawFrame
```
,  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abHScrollBar
```
,  

```
bool abVScrollBar
```
,  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetGroup@
```
](https://wiki.frictionalgames.com/page/../cWidgetGroup) | CreateWidgetGroup | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetImage@
```
](https://wiki.frictionalgames.com/page/../cWidgetImage) | CreateWidgetImage | [
```
const tString& asFile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
eGuiMaterial aMaterial
```
](https://wiki.frictionalgames.com/page/../eGuiMaterial),  

```
bool abAnimate
```
,  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetLabel@
```
](https://wiki.frictionalgames.com/page/../cWidgetLabel) | CreateWidgetLabel | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetListBox@
```
](https://wiki.frictionalgames.com/page/../cWidgetListBox) | CreateWidgetListBox | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetMainMenu@
```
](https://wiki.frictionalgames.com/page/../cWidgetMainMenu) | CreateWidgetMainMenu | [
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetMenuItem@
```
](https://wiki.frictionalgames.com/page/../cWidgetMenuItem) | CreateWidgetMenuItem | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetMultiPropertyListBox@
```
](https://wiki.frictionalgames.com/page/../cWidgetMultiPropertyListBox) | CreateWidgetMultiPropertyListBox | [
```
const cVector3f &in avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetSlider@
```
](https://wiki.frictionalgames.com/page/../cWidgetSlider) | CreateWidgetSlider | [
```
eWidgetSliderOrientation aOrientation
```
](https://wiki.frictionalgames.com/page/../eWidgetSliderOrientation),  
[
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
int alMaxValue
```
,  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetTabFrame@
```
](https://wiki.frictionalgames.com/page/../cWidgetTabFrame) | CreateWidgetTabFrame | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abAllowHScroll
```
,  

```
bool abAllowVScroll
```
,  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetTextBox@
```
](https://wiki.frictionalgames.com/page/../cWidgetTextBox) | CreateWidgetTextBox | [
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
eWidgetTextBoxInputType aeType
```
](https://wiki.frictionalgames.com/page/../eWidgetTextBoxInputType),  

```
float afNumericAdd
```
,  

```
bool abShowButtons
```
,  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
cWidgetWindow@
```
](https://wiki.frictionalgames.com/page/../cWidgetWindow) | CreateWidgetWindow | 
```
int alFlags
```
,  
[
```
const cVector3f& avLocalPos
```
](https://wiki.frictionalgames.com/page/../cVector3f),  
[
```
const cVector2f& avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  
[
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iWidget@ apParent
```
](https://wiki.frictionalgames.com/page/../iWidget),  
[
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | DestroyAllWidgets |   |   |
| 
```
void
```
 | DestroyWidget | [
```
iWidget@ apWidget
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abDestroyChildren
```
 |   |
| 
```
void
```
 | DrawFont | [
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iFontData@ apFont
```
](https://wiki.frictionalgames.com/page/../iFontData),  
[
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
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawFontEx | [
```
const tWString& asText
```
](https://wiki.frictionalgames.com/page/../tWString),  
[
```
iFontData@ apFont
```
](https://wiki.frictionalgames.com/page/../iFontData),  
[
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
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
eFontAlign aAlign
```
](https://wiki.frictionalgames.com/page/../eFontAlign),  
[
```
eGuiMaterial aMaterial
```
](https://wiki.frictionalgames.com/page/../eGuiMaterial) |   |
| 
```
void
```
 | DrawGfx | [
```
cGuiGfxElement@ apGfx
```
](https://wiki.frictionalgames.com/page/../cGuiGfxElement),  
[
```
const cVector3f& avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | DrawGfx | [
```
cGuiGfxElement@ apGfx
```
](https://wiki.frictionalgames.com/page/../cGuiGfxElement),  
[
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
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | DrawGfx | [
```
cGuiGfxElement@ apGfx
```
](https://wiki.frictionalgames.com/page/../cGuiGfxElement),  
[
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
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor),  
[
```
eGuiMaterial aMaterial
```
](https://wiki.frictionalgames.com/page/../eGuiMaterial),  

```
float afRotationAngle
```
,  

```
bool abUseCustomPivot
```
,  
[
```
const cVector3f &in avCustomPivot
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | Get3DSize |   |   |
| [
```
const cMatrixf&
```
](https://wiki.frictionalgames.com/page/../cMatrixf) | Get3DTransform |   |   |
| [
```
iWidget@
```
](https://wiki.frictionalgames.com/page/../iWidget) | GetAttentionWidget |   |   |
| 
```
bool
```
 | GetCullBackface |   |   |
| [
```
cGuiGfxElement@
```
](https://wiki.frictionalgames.com/page/../cGuiGfxElement) | GetCurrentPointer |   |   |
| 
```
bool
```
 | GetDrawMouse |   |   |
| 
```
int
```
 | GetDrawPriority |   |   |
| [
```
iWidget@
```
](https://wiki.frictionalgames.com/page/../iWidget) | GetFocusedWidget |   |   |
| 
```
bool
```
 | GetMouseMovementEnabled |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetMousePos |   |   |
| 
```
float
```
 | GetMouseZ |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
bool
```
 | GetRootWidgetClips |   |   |
| [
```
cGuiSkin@
```
](https://wiki.frictionalgames.com/page/../cGuiSkin) | GetSkin |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetVirtualSize |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetVirtualSizeOffset |   |   |
| [
```
iWidget@
```
](https://wiki.frictionalgames.com/page/../iWidget) | GetWidgetFromName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | HasFocus |   |   |
| 
```
bool
```
 | Is3D |   |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
bool
```
 | IsValidWidget | [
```
iWidget@ apWidget
```
](https://wiki.frictionalgames.com/page/../iWidget) |   |
| 
```
void
```
 | RemoveWindow | [
```
cWidgetWindow@ apWin
```
](https://wiki.frictionalgames.com/page/../cWidgetWindow) |   |
| 
```
void
```
 | ResetMouseOver |   |   |
| 
```
void
```
 | Set3DSize | [
```
const cVector3f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | Set3DTransform | [
```
const cMatrixf &in a_mtxTransform
```
](https://wiki.frictionalgames.com/page/../cMatrixf) |   |
| 
```
void
```
 | SetActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetAttentionWidget | [
```
iWidget@ apWidget
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abClearFocus
```
 |   |
| 
```
void
```
 | SetCullBackface | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCurrentPointer | [
```
cGuiGfxElement@ apGfx
```
](https://wiki.frictionalgames.com/page/../cGuiGfxElement) |   |
| 
```
void
```
 | SetDrawMouse | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDrawPriority | 
```
int alPrio
```
 |   |
| 
```
void
```
 | SetFocusedWidget | [
```
iWidget@ apWidget
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abCheckForValidity = false
```
 |   |
| 
```
void
```
 | SetIs3D | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetLastWindowZ | 
```
float afX
```
 |   |
| 
```
void
```
 | SetMouseMovementEnabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetMouseZ | 
```
float afZ
```
 |   |
| 
```
void
```
 | SetRootWidgetClips | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetSkin | [
```
cGuiSkin@ apSkin
```
](https://wiki.frictionalgames.com/page/../cGuiSkin) |   |
| 
```
void
```
 | SetVirtualSize | [
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
float afMinZ
```
,  

```
float afMaxZ
```
,  
[
```
const cVector2f &in avOffset
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetWindowOnTop | [
```
cWidgetWindow@ apWin
```
](https://wiki.frictionalgames.com/page/../cWidgetWindow) |   |
| 
```
void
```
 | ShowContextMenu | [
```
cWidgetContextMenu@ apMenu
```
](https://wiki.frictionalgames.com/page/../cWidgetContextMenu),  
[
```
const cVector3f &in avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cGuiSet](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cGuiSet)
- Revision: `3573`
- Source update: `2020-08-06T13:34:31Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

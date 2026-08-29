---
title: cWidgetTreeView
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cWidgetTreeView"
sourceRevision: 3755
sourceUpdated: "2020-08-06T14:31:05Z"
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
cWidgetTreeView has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| [
```
cWidgetTreeItem@
```
](https://wiki.frictionalgames.com/page/../cWidgetTreeItem) | AddItem | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| [
```
cGuiGlobalShortcut@
```
](https://wiki.frictionalgames.com/page/../cGuiGlobalShortcut) | AddShortcut | 
```
int alKeyModifiers
```
,  
[
```
eKey aKey
```
](https://wiki.frictionalgames.com/page/../eKey),  
[
```
eGuiMessage aMsg = eGuiMessage_ButtonPressed
```
](https://wiki.frictionalgames.com/page/../eGuiMessage),  
[
```
const cGuiMessageData &in aData = cGuiMessageData
```
](https://wiki.frictionalgames.com/page/../cGuiMessageData),  

```
bool abBypassVisibility = true
```
,  

```
bool abBypassEnabled = true
```
 |   |
| 
```
void
```
 | AttachChild | [
```
iWidget@ apChild
```
](https://wiki.frictionalgames.com/page/../iWidget) |   |
| 
```
void
```
 | CenterGlobalPositionInSet |   |   |
| 
```
void
```
 | ClearItems |   |   |
| 
```
bool
```
 | ClipsGraphics |   |   |
| 
```
bool
```
 | GetCallbacksDisabled |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetChildrenOffset |   |   |
| 
```
bool
```
 | GetClipActive |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetColorMul |   |   |
| [
```
const cColor&
```
](https://wiki.frictionalgames.com/page/../cColor) | GetDefaultFontColor |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetDefaultFontSize |   |   |
| [
```
iFontData@
```
](https://wiki.frictionalgames.com/page/../iFontData) | GetDefaultFontType |   |   |
| [
```
iWidget@
```
](https://wiki.frictionalgames.com/page/../iWidget) | GetFocusNavigation | [
```
eUIArrow aDir
```
](https://wiki.frictionalgames.com/page/../eUIArrow) |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetGlobalPosition |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetLocalPosition |   |   |
| 
```
bool
```
 | GetMouseIsOver |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| [
```
iWidget@
```
](https://wiki.frictionalgames.com/page/../iWidget) | GetParent |   |   |
| [
```
cGuiGfxElement@
```
](https://wiki.frictionalgames.com/page/../cGuiGfxElement) | GetPointerGfx |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetScrollAmount |   |   |
| [
```
cGuiSet@
```
](https://wiki.frictionalgames.com/page/../cGuiSet) | GetSet |   |   |
| [
```
const cVector2f&
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetSize |   |   |
| [
```
const tWString&
```
](https://wiki.frictionalgames.com/page/../tWString) | GetText |   |   |
| [
```
const tWString&
```
](https://wiki.frictionalgames.com/page/../tWString) | GetToolTip |   |   |
| [
```
iWidget@
```
](https://wiki.frictionalgames.com/page/../iWidget) | GetToolTipWidget |   |   |
| [
```
eWidgetType
```
](https://wiki.frictionalgames.com/page/../eWidgetType) | GetType |   |   |
| 
```
int
```
 | GetUserValue |   |   |
| 
```
bool
```
 | HasFocus |   |   |
| 
```
bool
```
 | HasFocusNavigation |   |   |
| 
```
void
```
 | Init |   |   |
| 
```
bool
```
 | IsConnectedTo | [
```
iWidget@ apWidget
```
](https://wiki.frictionalgames.com/page/../iWidget),  

```
bool abIsStartWidget = true
```
 |   |
| 
```
bool
```
 | IsConnectedToChildren |   |   |
| 
```
bool
```
 | IsEnabled |   |   |
| 
```
bool
```
 | IsGlobalKeyPressListener |   |   |
| 
```
bool
```
 | IsGlobalUIInputListener |   |   |
| 
```
bool
```
 | IsRightUnderMouse |   |   |
| 
```
bool
```
 | IsVisible |   |   |
| 
```
bool
```
 | PointIsInside | [
```
const cVector2f &in avPoint
```
](https://wiki.frictionalgames.com/page/../cVector2f),  

```
bool abOnlyClipped
```
 |   |
| 
```
bool
```
 | ProcessMessage | [
```
eGuiMessage aMessage
```
](https://wiki.frictionalgames.com/page/../eGuiMessage),  
[
```
const cGuiMessageData &in aData
```
](https://wiki.frictionalgames.com/page/../cGuiMessageData),  

```
bool abSkipVisCheck = false
```
,  

```
bool abSkipEnabledCheck = false
```
 |   |
| 
```
void
```
 | RemoveChild | [
```
iWidget@ apChild
```
](https://wiki.frictionalgames.com/page/../iWidget) |   |
| 
```
void
```
 | SetAffectedByScroll | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetCallbacksDisabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetChildrenOffset | [
```
const cVector3f &in
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetClipActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetColorMul | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetConnectedToChildren | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetDefaultFontColor | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetDefaultFontSize | [
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetDefaultFontType | [
```
iFontData@ apFont
```
](https://wiki.frictionalgames.com/page/../iFontData) |   |
| 
```
void
```
 | SetEnabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetFocusNavigation | [
```
eUIArrow aDir
```
](https://wiki.frictionalgames.com/page/../eUIArrow),  
[
```
iWidget@ apWidget
```
](https://wiki.frictionalgames.com/page/../iWidget) |   |
| 
```
void
```
 | SetGlobalKeyPressListener | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetGlobalPosition | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetGlobalUIInputListener | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetName | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetPosition | [
```
const cVector3f &in avPos
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetScrollAmount | [
```
const cVector3f &in avX
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetSize | [
```
const cVector2f &in avSize
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
void
```
 | SetText | [
```
const tWString &in asText
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | SetToolTip | [
```
const tWString &in asToolTip
```
](https://wiki.frictionalgames.com/page/../tWString) |   |
| 
```
void
```
 | SetToolTipEnabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetUserValue | 
```
int alX
```
 |   |
| 
```
void
```
 | SetVisible | 
```
bool abX
```
 |   |
| 
```
void
```
 | Update | 
```
float afTimeStep
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cWidgetTreeView](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cWidgetTreeView)
- Revision: `3755`
- Source update: `2020-08-06T14:31:05Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

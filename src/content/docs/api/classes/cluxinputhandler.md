---
title: cLuxInputHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxInputHandler"
sourceRevision: 3643
sourceUpdated: "2020-08-06T13:56:09Z"
lastSynced: "2026-10-05T14:11:59Z"
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
cLuxInputHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddKeyboardLayoutKey | [
```
eKey aKey
```
](https://wiki.frictionalgames.com/page/../eKey),  
[
```
eLuxKeyboardLayoutType aType
```
](https://wiki.frictionalgames.com/page/../eLuxKeyboardLayoutType),  
[
```
const cImGuiGfx& aGfxKey
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cImGuiLabelData& aLabelKey
```
](https://wiki.frictionalgames.com/page/../cImGuiLabelData) |   |
| 
```
void
```
 | AddKeyboardLayoutRange | [
```
eKey aFirstKey
```
](https://wiki.frictionalgames.com/page/../eKey),  
[
```
eKey aLastKey
```
](https://wiki.frictionalgames.com/page/../eKey),  
[
```
eLuxKeyboardLayoutType aType
```
](https://wiki.frictionalgames.com/page/../eLuxKeyboardLayoutType),  
[
```
const cImGuiGfx& aGfxKey
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cImGuiLabelData& aLabelKey
```
](https://wiki.frictionalgames.com/page/../cImGuiLabelData) |   |
| 
```
void
```
 | AddPresetToProfile | [
```
const tString &in asProfile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asPreset
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | ClearKeyboardLayout |   |   |
| 
```
void
```
 | CreateAction | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
,  

```
bool abConfigurable
```
,  
[
```
const tString &in asCat
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | CreateActionInput | [
```
const tString &in asInputType
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alActionId
```
 |   |
| 
```
void
```
 | CreateAnalogAction | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
,  

```
bool abConfigurable
```
,  
[
```
const tString &in asCat
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alAxis
```
,  

```
float afMul
```
,  

```
int alAnalogId
```
 |   |
| 
```
void
```
 | CreateAnalogGamepadAction | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
,  
[
```
const tString &in asCat
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alAnalogId
```
,  

```
float afSmoothness
```
,  

```
int alDirectionLimit
```
 |   |
| 
```
void
```
 | CreateAnalogGamepadActionInput | [
```
const tString &in asInputType
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alActionId
```
 |   |
| 
```
void
```
 | CreateDebugAction | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alId
```
 |   |
| 
```
void
```
 | CreateGamepadProfile | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asPrefix
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | FetchGamepadInputLayoutString | [
```
const tString& asInputName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
tString& asPrefixName
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
tString& asLayoutString
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetActionName | 
```
int alId
```
,  

```
bool abAnalog
```
 |   |
| 
```
void
```
 | GetActionsAssociatedToGamepadControl | [
```
const tString& asProfile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asPreset
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString& asControl
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
tString& asActions
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | GetGamepadMappingAction | 
```
int alId
```
,  

```
int &out alAction
```
,  
[
```
tString &out asPrimary
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool &out abAnalog
```
 |   |
| 
```
int
```
 | GetGamepadMappingActionNum |   |   |
| 
```
float
```
 | GetGamepadSensitivity |   |   |
| 
```
bool
```
 | GetGamepadWasLastDeviceUsed |   |   |
| 
```
int
```
 | GetLastUsedGamepadIndex | 
```
float afTimeLimit = -1.0f
```
 |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetLatestKeyPressed |   |   |
| 
```
float
```
 | GetMouseSensitivity |   |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetRelMousePos |   |   |
| 
```
bool
```
 | GetSmoothMouse |   |   |
| [
```
cVector2f
```
](https://wiki.frictionalgames.com/page/../cVector2f) | GetSmoothMousePos | [
```
const cVector2f &in avRelPosMouse
```
](https://wiki.frictionalgames.com/page/../cVector2f) |   |
| 
```
float
```
 | GetTimeSinceGamepadWasUsed | 
```
int alID
```
 |   |
| 
```
bool
```
 | IsGamepadConnected |   |   |
| 
```
bool
```
 | IsYAxisInverted |   |   |
| 
```
void
```
 | LoadKeyConfig |   |   |
| 
```
void
```
 | ResetSmoothMousePos |   |   |
| 
```
void
```
 | SetGamepadColor | 
```
int alDevice
```
,  
[
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetGamepadMapping | [
```
const tString &in asProfile
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asPreset
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetGamepadSensitivity | 
```
float afX
```
 |   |
| 
```
void
```
 | SetKeyboardLayoutDefaults | [
```
const cImGuiGfx& aGfxKey
```
](https://wiki.frictionalgames.com/page/../cImGuiGfx),  
[
```
const cImGuiLabelData& aLabelKey
```
](https://wiki.frictionalgames.com/page/../cImGuiLabelData) |   |
| 
```
void
```
 | SetMaxSmoothMousePos | 
```
int alX
```
 |   |
| 
```
void
```
 | SetMouseLayout |   |   |
| 
```
void
```
 | SetMouseSensitivity | 
```
float afX
```
 |   |
| 
```
void
```
 | SetPrevSmoothMousePosMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetPrimaryGamepad | 
```
int alDevice
```
 |   |
| 
```
void
```
 | SetRumble | 
```
int alDevice
```
,  

```
float afStrength
```
,  

```
float afDuration
```
 |   |
| 
```
void
```
 | SetSmoothMouse | 
```
bool abX
```
 |   |
| 
```
bool
```
 | WasAnalogueInputFromPad |   |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxInputHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxInputHandler)
- Revision: `3643`
- Source update: `2020-08-06T13:56:09Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

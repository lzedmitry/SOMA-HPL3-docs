---
title: iGamepad
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iGamepad"
sourceRevision: 3892
sourceUpdated: "2020-08-06T15:01:03Z"
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
iGamepad has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
bool
```
 | AxesUpdated |   |   |
| 
```
bool
```
 | ButtonIsDown | [
```
eGamepadButton aButton
```
](https://wiki.frictionalgames.com/page/../eGamepadButton) |   |
| 
```
bool
```
 | ButtonIsPressed |   |   |
| 
```
bool
```
 | ButtonIsReleased |   |   |
| 
```
float
```
 | GetAxisDeadZoneRadiusValue |   |   |
| 
```
float
```
 | GetAxisValue | [
```
eGamepadAxis aAxis
```
](https://wiki.frictionalgames.com/page/../eGamepadAxis) |   |
| [
```
cVector2l
```
](https://wiki.frictionalgames.com/page/../cVector2l) | GetBallAbsPos | [
```
eGamepadBall aBall
```
](https://wiki.frictionalgames.com/page/../eGamepadBall) |   |
| [
```
cGamepadInputData
```
](https://wiki.frictionalgames.com/page/../cGamepadInputData) | GetButton |   |   |
| [
```
cColor
```
](https://wiki.frictionalgames.com/page/../cColor) | GetColorLED |   |   |
| [
```
tString
```
](https://wiki.frictionalgames.com/page/../tString) | GetGamepadName |   |   |
| [
```
eGamepadHatState
```
](https://wiki.frictionalgames.com/page/../eGamepadHatState) | GetHatCurrentState | [
```
eGamepadHat aHat
```
](https://wiki.frictionalgames.com/page/../eGamepadHat) |   |
| [
```
cGamepadInputData
```
](https://wiki.frictionalgames.com/page/../cGamepadInputData) | GetHatState |   |   |
| [
```
cGamepadInputData
```
](https://wiki.frictionalgames.com/page/../cGamepadInputData) | GetInputUpdate |   |   |
| 
```
int
```
 | GetNumAxes |   |   |
| 
```
int
```
 | GetNumBalls |   |   |
| 
```
int
```
 | GetNumButtons |   |   |
| 
```
int
```
 | GetNumHats |   |   |
| [
```
cGamepadInputData
```
](https://wiki.frictionalgames.com/page/../cGamepadInputData) | GetReleasedButton |   |   |
| [
```
cGamepadInputData
```
](https://wiki.frictionalgames.com/page/../cGamepadInputData) | GetUpdatedAxis |   |   |
| 
```
bool
```
 | HasInputUpdates |   |   |
| 
```
bool
```
 | HatIsInState | [
```
eGamepadHat aHat
```
](https://wiki.frictionalgames.com/page/../eGamepadHat),  
[
```
eGamepadHatState aState
```
](https://wiki.frictionalgames.com/page/../eGamepadHatState) |   |
| 
```
bool
```
 | HatsChanged |   |   |
| 
```
void
```
 | SetAxisDeadZoneRadiusValue | 
```
float afValue
```
 |   |
| 
```
void
```
 | SetColorLED | [
```
const cColor &in aColor
```
](https://wiki.frictionalgames.com/page/../cColor) |   |
| 
```
void
```
 | SetRumble | 
```
float afValue
```
,  

```
int alMillisec
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iGamepad](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iGamepad)
- Revision: `3892`
- Source update: `2020-08-06T15:01:03Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

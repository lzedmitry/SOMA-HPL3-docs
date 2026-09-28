---
title: cSoundEntry
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cSoundEntry"
sourceRevision: 3718
sourceUpdated: "2020-08-06T14:20:45Z"
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
cSoundEntry has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | FadeIn | 
```
float afVolumeMul
```
,  

```
float afSpeed
```
 |   |
| 
```
void
```
 | FadeOut | 
```
float afSpeed
```
 |   |
| 
```
void
```
 | FadeSpeedMulTo | 
```
float afDestMul
```
,  

```
float afSpeed
```
 |   |
| 
```
void
```
 | FadeVolumeMulTo | 
```
float afDestMul
```
,  

```
float afSpeed
```
 |   |
| 
```
float
```
 | GetAudibility |   |   |
| [
```
eSoundEntryDataType
```
](https://wiki.frictionalgames.com/page/../eSoundEntryDataType) | GetDataType |   |   |
| 
```
float
```
 | GetElapsedTime |   |   |
| 
```
int
```
 | GetId |   |   |
| 
```
float
```
 | GetMaxDistance |   |   |
| 
```
float
```
 | GetMinDistance |   |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetName |   |   |
| 
```
float
```
 | GetParamMax | 
```
int alIdx
```
 |   |
| 
```
float
```
 | GetParamMin | 
```
int alIdx
```
 |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetParamName | 
```
int alIdx
```
 |   |
| 
```
int
```
 | GetParamNum |   |   |
| 
```
float
```
 | GetParamValue | 
```
int alIdx
```
 |   |
| 
```
bool
```
 | GetPaused |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetPosition |   |   |
| 
```
bool
```
 | GetPostionIsHeadRelative |   |   |
| 
```
bool
```
 | GetReverbActive |   |   |
| 
```
float
```
 | GetReverbAmount |   |   |
| 
```
float
```
 | GetSpeakerSpread |   |   |
| 
```
float
```
 | GetSpeed |   |   |
| 
```
float
```
 | GetSpeedMul |   |   |
| 
```
bool
```
 | GetStopDisabled |   |   |
| 
```
float
```
 | GetTotalTime |   |   |
| [
```
eSoundEntryType
```
](https://wiki.frictionalgames.com/page/../eSoundEntryType) | GetType |   |   |
| 
```
float
```
 | GetVolume |   |   |
| 
```
float
```
 | GetVolumeMul |   |   |
| 
```
bool
```
 | Is3D |   |   |
| 
```
bool
```
 | IsFirstTime |   |   |
| 
```
bool
```
 | IsOneShot |   |   |
| 
```
bool
```
 | IsPlaying |   |   |
| 
```
bool
```
 | IsPriorityReleased |   |   |
| 
```
bool
```
 | IsVirtual |   |   |
| 
```
void
```
 | SetBlockable | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetBlockVolumeMul | 
```
float afX
```
 |   |
| 
```
void
```
 | SetElapsedTime | 
```
float afTime
```
 |   |
| 
```
void
```
 | SetParam | [
```
const tString& asName
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afValue
```
 |   |
| 
```
void
```
 | SetParam | 
```
int alIdx
```
,  

```
float afValue
```
 |   |
| 
```
void
```
 | SetPaused | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetPosition | [
```
const cVector3f &in avPosition
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetPostionIsHeadRelative | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetReverbActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetReverbAmount | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeakerSpread | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeed | 
```
float afX
```
 |   |
| 
```
void
```
 | SetSpeedMul | 
```
float afMul
```
 |   |
| 
```
void
```
 | SetStopDisabled | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetVelocity | [
```
const cVector3f &in avVelocity
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetVolume | 
```
float afX
```
 |   |
| 
```
void
```
 | SetVolumeMul | 
```
float afMul
```
 |   |
| 
```
void
```
 | Stop | 
```
bool abPlayEnd
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cSoundEntry](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cSoundEntry)
- Revision: `3718`
- Source update: `2020-08-06T14:20:45Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

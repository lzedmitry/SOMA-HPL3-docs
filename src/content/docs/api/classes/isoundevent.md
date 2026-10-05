---
title: iSoundEvent
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iSoundEvent"
sourceRevision: 3938
sourceUpdated: "2020-08-06T15:10:51Z"
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
iSoundEvent has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
float
```
 | GetAudibility |   |   |
| [
```
iSoundEventData@
```
](https://wiki.frictionalgames.com/page/../iSoundEventData) | GetData |   |   |
| 
```
float
```
 | GetElapsedTime |   |   |
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
 | GetParam | 
```
int alIdx
```
 |   |
| 
```
float
```
 | GetParam | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
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
 | GetTotalTime |   |   |
| [
```
const cVector3f&
```
](https://wiki.frictionalgames.com/page/../cVector3f) | GetVelocity |   |   |
| 
```
float
```
 | GetVolume |   |   |
| 
```
bool
```
 | Is3D |   |   |
| 
```
bool
```
 | IsLoading |   |   |
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
void
```
 | SetMaxDistance | 
```
float fMax
```
 |   |
| 
```
void
```
 | SetMinDistance | 
```
float fMin
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
 | SetParam | [
```
const tString &in asName
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
const cVector3f& avPos
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
float afSpeed
```
 |   |
| 
```
void
```
 | SetVelocity | [
```
const cVector3f& avVel
```
](https://wiki.frictionalgames.com/page/../cVector3f) |   |
| 
```
void
```
 | SetVolume | 
```
float afVolume
```
 |   |
| 
```
void
```
 | Start |   |   |
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

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/iSoundEvent](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/iSoundEvent)
- Revision: `3938`
- Source update: `2020-08-06T15:10:51Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

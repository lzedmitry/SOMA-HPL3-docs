---
title: cLuxBarkMachine
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxBarkMachine"
sourceRevision: 3612
sourceUpdated: "2020-08-06T13:48:32Z"
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
cLuxBarkMachine has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddState | 
```
int alId
```
 |   |
| 
```
void
```
 | ChangeState | 
```
int alId
```
 |   |
| [
```
iLuxEntity@
```
](https://wiki.frictionalgames.com/page/../iLuxEntity) | GetEntity |   |   |
| [
```
eLuxEntityComponentType
```
](https://wiki.frictionalgames.com/page/../eLuxEntityComponentType) | GetType |   |   |
| 
```
bool
```
 | IsActive |   |   |
| 
```
void
```
 | PlayVoice | [
```
const tString &in asSubject
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alPrio
```
,  

```
float afMinDistance = -1
```
,  

```
float afMaxDistance = -1
```
,  

```
float afMaxPlayerListeningRange = -1
```
 |   |
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
 | SetState_SoundBark | [
```
const tString &in asSound
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMinBetweenTime
```
,  

```
float afMaxBetweenTime
```
,  

```
bool abWaitForSoundToBeDone
```
 |   |
| 
```
void
```
 | SetState_VoiceBark | [
```
const tString &in asSubject
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afMinBetweenTime
```
,  

```
float afMaxBetweenTime
```
,  

```
bool abWaitForSoundToBeDone
```
,  

```
int alPrio = 0
```
,  

```
float afMinDistance = -1
```
,  

```
float afMaxDistance = -1
```
,  

```
float afMaxPlayerListeningRange = -1
```
 |   |
| 
```
void
```
 | SetupVoice | [
```
const tString &in asCharacter
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abUse3D
```
,  

```
float afDefaultMinDistance
```
,  

```
float afDefaultMaxDistance
```
,  

```
float afDefaultMaxPlayerListeningRange
```
 |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxBarkMachine](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxBarkMachine)
- Revision: `3612`
- Source update: `2020-08-06T13:48:32Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

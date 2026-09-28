---
title: cLuxVoiceHandler
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxVoiceHandler"
sourceRevision: 3044
sourceUpdated: "2020-08-04T01:58:10Z"
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
cLuxVoiceHandler has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
void
```
 | AddCharacterSpeakingCallback | [
```
const tString &in asCharacter
```
](https://wiki.frictionalgames.com/page/../tString),  
[
```
const tString &in asCallback
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | AdvanceFromCurrentSound | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | AnySceneIsActive |   |   |
| 
```
bool
```
 | CharacterIsSpeaking | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | FadeSceneVolumeTo | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString),  

```
float afVolume
```
,  

```
float afTime
```
 |   |
| 
```
void
```
 | GetSpectrumFromScene | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alNumSamples = 64
```
 |   |
| 
```
void
```
 | GetSpectrumFromSpeakingCharacter | [
```
const tString &in asCharacter
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alNumSamples = 64
```
 |   |
| 
```
int
```
 | GetSubjectLineNumber | [
```
const tString& asSubject
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| [
```
const tString&
```
](https://wiki.frictionalgames.com/page/../tString) | GetSubjectSceneName | [
```
const tString& asSubject
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | GetUnderwaterEffectsActive |   |   |
| 
```
bool
```
 | Play | [
```
const tString& asSubject
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alSpecificLine
```
,  
[
```
const tString& asCallback
```
](https://wiki.frictionalgames.com/page/../tString),  

```
int alPrio
```
 |   |
| 
```
void
```
 | RemoveCharacterSpeakingCallback | [
```
const tString &in asCharacter
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | SceneInvolvingCharacterIsActive | [
```
const tString &in asCharacter
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | SceneIsActive | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetFocusScene | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SetPaused | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString),  

```
bool abX
```
 |   |
| 
```
void
```
 | SetPausedAll | 
```
bool abX
```
 |   |
| 
```
void
```
 | SetUnderwaterEffectsActive | 
```
bool abX
```
 |   |
| 
```
void
```
 | SkipCurrentLine | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | SkipCurrentSound | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | Stop | [
```
const tString &in asScene
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
void
```
 | StopAll |   |   |
| 
```
bool
```
 | SubjectExists | [
```
const tString& asSubject
```
](https://wiki.frictionalgames.com/page/../tString) |   |
| 
```
bool
```
 | SubjectIsPlaying | [
```
const tString &in asName
```
](https://wiki.frictionalgames.com/page/../tString) |   |

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/cLuxVoiceHandler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/cLuxVoiceHandler)
- Revision: `3044`
- Source update: `2020-08-04T01:58:10Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

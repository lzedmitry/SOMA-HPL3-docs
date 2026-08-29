---
title: cSound
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cSound"
sourceRevision: 5025
sourceUpdated: "2020-08-24T20:51:28Z"
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

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `bool` | [`cSound_CheckSoundIsBlocked`](#csound-checksoundisblocked)(const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avSoundPosition) | *Undocumented in the original Wiki.* |
| `iSoundEvent` | [`cSound_CreateEvent`](#csound-createevent)([iSoundEventData@](https://wiki.frictionalgames.com/page/../../iSoundEventData) apData, bool abNonBlockingLoad) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_DestroyEvent`](#csound-destroyevent)([iSoundEvent@](https://wiki.frictionalgames.com/page/../../iSoundEvent) apEvent) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_DestroyUnusedData`](#csound-destroyunuseddata)(int alMaxAmount, int alMaxAge, bool abRemoveUnusedProjects, bool abRemovePreloaded) | *Undocumented in the original Wiki.* |
| `int` | [`cSound_FadeGlobalSpeed`](#csound-fadeglobalspeed)(float afDestSpeed, float afSpeed, uint mAffectedTypes, int alId, bool abDestroyIdAtDest) | *Undocumented in the original Wiki.* |
| `int` | [`cSound_FadeGlobalVolume`](#csound-fadeglobalvolume)(float afDestVolume, float afSpeed, uint mAffectedTypes, int alId, bool abDestroyIdAtDest) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_FadeHighPassFilter`](#csound-fadehighpassfilter)(float afDestCutOff, float afDestResonance, float afTime, uint mAffectedTypes) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_FadeLowPassFilter`](#csound-fadelowpassfilter)(float afDestCutOff, float afDestResonance, float afTime, uint mAffectedTypes) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_FadeMusicVolumeMul`](#csound-fademusicvolumemul)(float afDest, float afSpeed) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_FadeOutAll`](#csound-fadeoutall)(uint mTypes, float afFadeSpeed, bool abDisableStop) | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_GetEntry`](#csound-getentry)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `tString` | [`cSound_GetEventCategory_Gui`](#csound-geteventcategory-gui)() | *Undocumented in the original Wiki.* |
| `tString` | [`cSound_GetEventCategory_World`](#csound-geteventcategory-world)() | *Undocumented in the original Wiki.* |
| `tString` | [`cSound_GetEventCategory_WorldClean`](#csound-geteventcategory-worldclean)() | *Undocumented in the original Wiki.* |
| `iSoundEventData` | [`cSound_GetEventData`](#csound-geteventdata)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asInternalPath, bool abLoadData, bool abNonBlockingLoad) | *Undocumented in the original Wiki.* |
| `iSoundEventProject` | [`cSound_GetEventProject`](#csound-geteventproject)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `uint` | [`cSound_GetEventSystemMemoryUsed`](#csound-geteventsystemmemoryused)() | *Undocumented in the original Wiki.* |
| `float` | [`cSound_GetGlobalSpeed`](#csound-getglobalspeed)([eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aType) | *Undocumented in the original Wiki.* |
| `float` | [`cSound_GetGlobalSpeedFromId`](#csound-getglobalspeedfromid)(int alId) | *Undocumented in the original Wiki.* |
| `float` | [`cSound_GetGlobalVolume`](#csound-getglobalvolume)([eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aType) | *Undocumented in the original Wiki.* |
| `float` | [`cSound_GetGlobalVolumeFromId`](#csound-getglobalvolumefromid)(int alId) | *Undocumented in the original Wiki.* |
| `float` | [`cSound_GetMusicVolumeMul`](#csound-getmusicvolumemul)() | *Undocumented in the original Wiki.* |
| `bool` | [`cSound_GetSilent`](#csound-getsilent)() | *Undocumented in the original Wiki.* |
| `bool` | [`cSound_IsPlaying`](#csound-isplaying)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `bool` | [`cSound_IsValid`](#csound-isvalid)([cSoundEntry](https://wiki.frictionalgames.com/page/../../cSoundEntry) @apEntry, int alID) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_PauseAll`](#csound-pauseall)(uint mTypes) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_PauseMusic`](#csound-pausemusic)() | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_Play`](#csound-play)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLoop, float afVolume, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avPos, float afMinDist, float afMaxDist, [eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aEntryType, bool abRelative, bool ab3D, int alPriorityModifier, bool abStream, bool abNonBlockedLoad) | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_Play3D`](#csound-play3d)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLoop, float afVolume, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avPos, float afMinDist, float afMaxDist, [eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aEntryType, bool abRelative, int alPriorityModifier, bool abStream, bool abNonBlockedLoad) | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_PlayGui`](#csound-playgui)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLoop, float afVolume, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avPos, [eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aEntryType) | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_PlayGuiStream`](#csound-playguistream)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFileName, bool abLoop, float afVolume, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avPos, [eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aEntryType) | *Undocumented in the original Wiki.* |
| `bool` | [`cSound_PlayMusic`](#csound-playmusic)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFileName, float afVolume, float afVolumeFadeStepSize, float afFreq, float afFreqFadeStepSize, bool abLoop, bool abResume) | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_PlaySoundEntityGui`](#csound-playsoundentitygui)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abLoop, float afVolume, [eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType) aEntryType, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avPos) | *Undocumented in the original Wiki.* |
| `cSoundEntry` | [`cSound_PlaySoundEvent`](#csound-playsoundevent)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asInternalPath, float afVolume, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avPos, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avOrientation, bool abNonBlockLoad) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_PreloadGroup`](#csound-preloadgroup)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asInternalPath, bool abNonBlockingLoad, bool abSubGroups) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_PreloadProject`](#csound-preloadproject)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abNonBlockingLoad) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_ResumeAll`](#csound-resumeall)(uint mTypes) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_ResumeMusic`](#csound-resumemusic)() | *Undocumented in the original Wiki.* |
| `void` | [`cSound_SetEventCategory_Gui`](#csound-seteventcategory-gui)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCat) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_SetEventCategory_World`](#csound-seteventcategory-world)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCat) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_SetEventCategory_WorldClean`](#csound-seteventcategory-worldclean)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCat) | *Undocumented in the original Wiki.* |
| `int` | [`cSound_SetGlobalSpeed`](#csound-setglobalspeed)(float afSpeed, uint mAffectedTypes, int alId) | *Undocumented in the original Wiki.* |
| `int` | [`cSound_SetGlobalVolume`](#csound-setglobalvolume)(float afVolume, uint mAffectedTypes, int alId) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_SetMusicVolumeMul`](#csound-setmusicvolumemul)(float afMul) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_SetSilent`](#csound-setsilent)(bool abX) | *Undocumented in the original Wiki.* |
| `bool` | [`cSound_Stop`](#csound-stop)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abPlayEnd) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_StopAll`](#csound-stopall)(uint mTypes, bool abPlayEnd) | *Undocumented in the original Wiki.* |
| `void` | [`cSound_StopMusic`](#csound-stopmusic)(float afFadeStepSize) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cSound_CheckSoundIsBlocked`

```angelscript
bool cSound_CheckSoundIsBlocked(const cVector3f &in avSoundPosition)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `avSoundPosition` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |

**Returns:** `bool`

    1. `cSound_CreateEvent`

```angelscript
iSoundEvent@ cSound_CreateEvent(iSoundEventData@ apData,
                                bool abNonBlockingLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apData` | `[iSoundEventData@](https://wiki.frictionalgames.com/page/../../iSoundEventData)` | — |
| `abNonBlockingLoad` | `bool` | — |

**Returns:** `iSoundEvent@`

    1. `cSound_DestroyEvent`

```angelscript
void cSound_DestroyEvent(iSoundEvent@ apEvent)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `apEvent` | `[iSoundEvent@](https://wiki.frictionalgames.com/page/../../iSoundEvent)` | — |

**Returns:** `void`

    1. `cSound_DestroyUnusedData`

```angelscript
void cSound_DestroyUnusedData(int alMaxAmount,
                              int alMaxAge,
                              bool abRemoveUnusedProjects,
                              bool abRemovePreloaded)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alMaxAmount` | `int` | — |
| `alMaxAge` | `int` | — |
| `abRemoveUnusedProjects` | `bool` | — |
| `abRemovePreloaded` | `bool` | — |

**Returns:** `void`

    1. `cSound_FadeGlobalSpeed`

```angelscript
int cSound_FadeGlobalSpeed(float afDestSpeed,
                           float afSpeed,
                           uint mAffectedTypes,
                           int alId,
                           bool abDestroyIdAtDest)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afDestSpeed` | `float` | — |
| `afSpeed` | `float` | — |
| `mAffectedTypes` | `uint` | — |
| `alId` | `int` | — |
| `abDestroyIdAtDest` | `bool` | — |

**Returns:** `int`

    1. `cSound_FadeGlobalVolume`

```angelscript
int cSound_FadeGlobalVolume(float afDestVolume,
                            float afSpeed,
                            uint mAffectedTypes,
                            int alId,
                            bool abDestroyIdAtDest)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afDestVolume` | `float` | — |
| `afSpeed` | `float` | — |
| `mAffectedTypes` | `uint` | — |
| `alId` | `int` | — |
| `abDestroyIdAtDest` | `bool` | — |

**Returns:** `int`

    1. `cSound_FadeHighPassFilter`

```angelscript
void cSound_FadeHighPassFilter(float afDestCutOff,
                               float afDestResonance,
                               float afTime,
                               uint mAffectedTypes)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afDestCutOff` | `float` | — |
| `afDestResonance` | `float` | — |
| `afTime` | `float` | — |
| `mAffectedTypes` | `uint` | — |

**Returns:** `void`

    1. `cSound_FadeLowPassFilter`

```angelscript
void cSound_FadeLowPassFilter(float afDestCutOff,
                              float afDestResonance,
                              float afTime,
                              uint mAffectedTypes)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afDestCutOff` | `float` | — |
| `afDestResonance` | `float` | — |
| `afTime` | `float` | — |
| `mAffectedTypes` | `uint` | — |

**Returns:** `void`

    1. `cSound_FadeMusicVolumeMul`

```angelscript
void cSound_FadeMusicVolumeMul(float afDest,
                               float afSpeed)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afDest` | `float` | — |
| `afSpeed` | `float` | — |

**Returns:** `void`

    1. `cSound_FadeOutAll`

```angelscript
void cSound_FadeOutAll(uint mTypes,
                       float afFadeSpeed,
                       bool abDisableStop)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `mTypes` | `uint` | — |
| `afFadeSpeed` | `float` | — |
| `abDisableStop` | `bool` | — |

**Returns:** `void`

    1. `cSound_GetEntry`

```angelscript
cSoundEntry@ cSound_GetEntry(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_GetEventCategory_Gui`

```angelscript
const tString& cSound_GetEventCategory_Gui()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `const tString&`

    1. `cSound_GetEventCategory_World`

```angelscript
const tString& cSound_GetEventCategory_World()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `const tString&`

    1. `cSound_GetEventCategory_WorldClean`

```angelscript
const tString& cSound_GetEventCategory_WorldClean()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `const tString&`

    1. `cSound_GetEventData`

```angelscript
iSoundEventData@ cSound_GetEventData(const tString &in asInternalPath,
                                     bool abLoadData,
                                     bool abNonBlockingLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asInternalPath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abLoadData` | `bool` | — |
| `abNonBlockingLoad` | `bool` | — |

**Returns:** `iSoundEventData@`

    1. `cSound_GetEventProject`

```angelscript
iSoundEventProject@ cSound_GetEventProject(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `iSoundEventProject@`

    1. `cSound_GetEventSystemMemoryUsed`

```angelscript
uint cSound_GetEventSystemMemoryUsed()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `uint`

    1. `cSound_GetGlobalSpeed`

```angelscript
float cSound_GetGlobalSpeed(eSoundEntryType aType)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |

**Returns:** `float`

    1. `cSound_GetGlobalSpeedFromId`

```angelscript
float cSound_GetGlobalSpeedFromId(int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |

**Returns:** `float`

    1. `cSound_GetGlobalVolume`

```angelscript
float cSound_GetGlobalVolume(eSoundEntryType aType)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |

**Returns:** `float`

    1. `cSound_GetGlobalVolumeFromId`

```angelscript
float cSound_GetGlobalVolumeFromId(int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alId` | `int` | — |

**Returns:** `float`

    1. `cSound_GetMusicVolumeMul`

```angelscript
float cSound_GetMusicVolumeMul()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cSound_GetSilent`

```angelscript
bool cSound_GetSilent()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cSound_IsPlaying`

```angelscript
bool cSound_IsPlaying(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cSound_IsValid`

```angelscript
bool cSound_IsValid(cSoundEntry @apEntry,
                    int alID)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `@apEntry` | `[cSoundEntry](https://wiki.frictionalgames.com/page/../../cSoundEntry)` | — |
| `alID` | `int` | — |

**Returns:** `bool`

    1. `cSound_PauseAll`

```angelscript
void cSound_PauseAll(uint mTypes)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `mTypes` | `uint` | — |

**Returns:** `void`

    1. `cSound_PauseMusic`

```angelscript
void cSound_PauseMusic()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cSound_Play`

```angelscript
cSoundEntry@ cSound_Play(const tString &in asName,
                         bool abLoop,
                         float afVolume,
                         const cVector3f &in avPos,
                         float afMinDist,
                         float afMaxDist,
                         eSoundEntryType aEntryType,
                         bool abRelative,
                         bool ab3D,
                         int alPriorityModifier,
                         bool abStream,
                         bool abNonBlockedLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abLoop` | `bool` | — |
| `afVolume` | `float` | — |
| `avPos` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |
| `afMinDist` | `float` | — |
| `afMaxDist` | `float` | — |
| `aEntryType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |
| `abRelative` | `bool` | — |
| `ab3D` | `bool` | — |
| `alPriorityModifier` | `int` | — |
| `abStream` | `bool` | — |
| `abNonBlockedLoad` | `bool` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_Play3D`

```angelscript
cSoundEntry@ cSound_Play3D(const tString &in asName,
                           bool abLoop,
                           float afVolume,
                           const cVector3f &in avPos,
                           float afMinDist,
                           float afMaxDist,
                           eSoundEntryType aEntryType,
                           bool abRelative,
                           int alPriorityModifier,
                           bool abStream,
                           bool abNonBlockedLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abLoop` | `bool` | — |
| `afVolume` | `float` | — |
| `avPos` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |
| `afMinDist` | `float` | — |
| `afMaxDist` | `float` | — |
| `aEntryType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |
| `abRelative` | `bool` | — |
| `alPriorityModifier` | `int` | — |
| `abStream` | `bool` | — |
| `abNonBlockedLoad` | `bool` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_PlayGui`

```angelscript
cSoundEntry@ cSound_PlayGui(const tString &in asName,
                            bool abLoop,
                            float afVolume,
                            const cVector3f &in avPos,
                            eSoundEntryType aEntryType)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abLoop` | `bool` | — |
| `afVolume` | `float` | — |
| `avPos` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |
| `aEntryType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_PlayGuiStream`

```angelscript
cSoundEntry@ cSound_PlayGuiStream(const tString &in asFileName,
                                  bool abLoop,
                                  float afVolume,
                                  const cVector3f &in avPos,
                                  eSoundEntryType aEntryType)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFileName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abLoop` | `bool` | — |
| `afVolume` | `float` | — |
| `avPos` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |
| `aEntryType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_PlayMusic`

```angelscript
bool cSound_PlayMusic(const tString &in asFileName,
                      float afVolume,
                      float afVolumeFadeStepSize,
                      float afFreq,
                      float afFreqFadeStepSize,
                      bool abLoop,
                      bool abResume)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asFileName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afVolume` | `float` | — |
| `afVolumeFadeStepSize` | `float` | — |
| `afFreq` | `float` | — |
| `afFreqFadeStepSize` | `float` | — |
| `abLoop` | `bool` | — |
| `abResume` | `bool` | — |

**Returns:** `bool`

    1. `cSound_PlaySoundEntityGui`

```angelscript
cSoundEntry@ cSound_PlaySoundEntityGui(const tString &in asName,
                                       bool abLoop,
                                       float afVolume,
                                       eSoundEntryType aEntryType,
                                       const cVector3f &in avPos)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abLoop` | `bool` | — |
| `afVolume` | `float` | — |
| `aEntryType` | `[eSoundEntryType](https://wiki.frictionalgames.com/page/../../eSoundEntryType)` | — |
| `avPos` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_PlaySoundEvent`

```angelscript
cSoundEntry@ cSound_PlaySoundEvent(const tString &in asInternalPath,
                                   float afVolume,
                                   const cVector3f &in avPos,
                                   const cVector3f &in avOrientation,
                                   bool abNonBlockLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asInternalPath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afVolume` | `float` | — |
| `avPos` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |
| `avOrientation` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |
| `abNonBlockLoad` | `bool` | — |

**Returns:** `cSoundEntry@`

    1. `cSound_PreloadGroup`

```angelscript
void cSound_PreloadGroup(const tString &in asInternalPath,
                         bool abNonBlockingLoad,
                         bool abSubGroups)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asInternalPath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abNonBlockingLoad` | `bool` | — |
| `abSubGroups` | `bool` | — |

**Returns:** `void`

    1. `cSound_PreloadProject`

```angelscript
void cSound_PreloadProject(const tString &in asName,
                           bool abNonBlockingLoad)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abNonBlockingLoad` | `bool` | — |

**Returns:** `void`

    1. `cSound_ResumeAll`

```angelscript
void cSound_ResumeAll(uint mTypes)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `mTypes` | `uint` | — |

**Returns:** `void`

    1. `cSound_ResumeMusic`

```angelscript
void cSound_ResumeMusic()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `void`

    1. `cSound_SetEventCategory_Gui`

```angelscript
void cSound_SetEventCategory_Gui(const tString &in asCat)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asCat` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cSound_SetEventCategory_World`

```angelscript
void cSound_SetEventCategory_World(const tString &in asCat)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asCat` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cSound_SetEventCategory_WorldClean`

```angelscript
void cSound_SetEventCategory_WorldClean(const tString &in asCat)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asCat` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cSound_SetGlobalSpeed`

```angelscript
int cSound_SetGlobalSpeed(float afSpeed,
                          uint mAffectedTypes,
                          int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afSpeed` | `float` | — |
| `mAffectedTypes` | `uint` | — |
| `alId` | `int` | — |

**Returns:** `int`

    1. `cSound_SetGlobalVolume`

```angelscript
int cSound_SetGlobalVolume(float afVolume,
                           uint mAffectedTypes,
                           int alId)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afVolume` | `float` | — |
| `mAffectedTypes` | `uint` | — |
| `alId` | `int` | — |

**Returns:** `int`

    1. `cSound_SetMusicVolumeMul`

```angelscript
void cSound_SetMusicVolumeMul(float afMul)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afMul` | `float` | — |

**Returns:** `void`

    1. `cSound_SetSilent`

```angelscript
void cSound_SetSilent(bool abX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `abX` | `bool` | — |

**Returns:** `void`

    1. `cSound_Stop`

```angelscript
bool cSound_Stop(const tString &in asName,
                 bool abPlayEnd)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abPlayEnd` | `bool` | — |

**Returns:** `bool`

    1. `cSound_StopAll`

```angelscript
void cSound_StopAll(uint mTypes,
                    bool abPlayEnd)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `mTypes` | `uint` | — |
| `abPlayEnd` | `bool` | — |

**Returns:** `void`

    1. `cSound_StopMusic`

```angelscript
void cSound_StopMusic(float afFadeStepSize)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afFadeStepSize` | `float` | — |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cSound](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cSound)
- Revision: `5025`
- Source update: `2020-08-24T20:51:28Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

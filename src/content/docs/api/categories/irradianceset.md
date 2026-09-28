---
title: IrradianceSet
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/IrradianceSet"
sourceRevision: 5032
sourceUpdated: "2020-08-24T20:54:11Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `void` | [`IrradianceSet_FadeIn`](#irradianceset-fadein)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asSet, float afTime) | Fades in the specified set on all probes belonging to it |
| `void` | [`IrradianceSet_FadeInSingleProbe`](#irradianceset-fadeinsingleprobe)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asProbe, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asSet, float afTime) | Fades in the specified set on a specific probe |

## Function Detail
    1. `IrradianceSet_FadeIn`

```cpp
void IrradianceSet_FadeIn(const tString &in asSet,
                          float afTime)
```

Fades in the specified set on all probes belonging to it. This also fades out the currently active set for these probes.

| Name | Type | Description |
| --- | --- | --- |
| `asSet` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | set to fade in. |
| `afTime` | `float` | how long it should take until the fade is done. |

**Returns:** `void`

    1. `IrradianceSet_FadeInSingleProbe`

```cpp
void IrradianceSet_FadeInSingleProbe(const tString &in asProbe,
                                     const tString &in asSet,
                                     float afTime)
```

Fades in the specified set on a specific probe. This also fades out the currently active set for these probes.

| Name | Type | Description |
| --- | --- | --- |
| `asProbe` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the probe to fade in the set on. Wildcards (*) supported. |
| `asSet` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | set to fade in. |
| `afTime` | `float` | how long it should take until the fade is done. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/IrradianceSet](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/IrradianceSet)
- Revision: `5032`
- Source update: `2020-08-24T20:54:11Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

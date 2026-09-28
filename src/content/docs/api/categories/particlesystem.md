---
title: ParticleSystem
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/ParticleSystem"
sourceRevision: 5045
sourceUpdated: "2020-08-24T20:57:46Z"
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
| `void` | [`ParticleSystem_AttachToEntity`](#particlesystem-attachtoentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName) | Attaches a particle system to an entity |
| `cParticleSystem` | [`ParticleSystem_CreateAtEntity`](#particlesystem-createatentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSFile, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntity, bool abAttach) | Creates a particle system at entity |
| `cParticleSystem` | [`ParticleSystem_CreateAtEntityExt`](#particlesystem-createatentityext)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSFile, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntity, bool abAttach, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in acColor, float afBrightness = 1.0f, bool abFadeAtDistance = false, float afFadeMinEnd = 1.0f, float afFadeMinStart = 2.0f, float afFadeMaxStart = 100.0f, float afFadeMaxEnd = 110.0f) | Creates a particle system at entity with extra options |
| `void` | [`ParticleSystem_Destroy`](#particlesystem-destroy)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName) | Destroy a particle system |
| `bool` | [`ParticleSystem_Exists`](#particlesystem-exists)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName) | Returns true or false if a given particle system exists |
| `void` | [`ParticleSystem_Preload`](#particlesystem-preload)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFile) | Preload particle system data |
| `void` | [`ParticleSystem_SetActive`](#particlesystem-setactive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, bool abActive) | Activates or deactivates a particle system |
| `void` | [`ParticleSystem_SetBrightness`](#particlesystem-setbrightness)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, float afBrightness) | Sets the brightness of a particle system |
| `void` | [`ParticleSystem_SetColor`](#particlesystem-setcolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in acColor) | Sets the color of a particle system |
| `void` | [`ParticleSystem_SetVisible`](#particlesystem-setvisible)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPSName, bool abVisible) | Sets the visibility of a particle system |

## Function Detail
    1. `ParticleSystem_AttachToEntity`

```cpp
void ParticleSystem_AttachToEntity(const tString &in asPSName,
                                   const tString &in asEntityName)
```

Attaches a particle system to an entity.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system, can contain wildcards(*). |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to attach the particle system to. |

**Returns:** `void`

    1. `ParticleSystem_CreateAtEntity`

```cpp
cParticleSystem@ ParticleSystem_CreateAtEntity(const tString &in asPSName,
                                               const tString &in asPSFile,
                                               const tString &in asEntity,
                                               bool abAttach)
```

Creates a particle system at entity.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system entity to be created. |
| `asPSFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | .ps file to create particle system from. |
| `asEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | entity to create particle system at. Can be "player". |
| `abAttach` | `bool` | whether the particle system should be attached to the entity it is created at. |

**Returns:** `cParticleSystem@` — cParticleSystem, the created particle system or null if the function fails.

    1. `ParticleSystem_CreateAtEntityExt`

```cpp
cParticleSystem@ ParticleSystem_CreateAtEntityExt(const tString &in asPSName,
                                                  const tString &in asPSFile,
                                                  const tString &in asEntity,
                                                  bool abAttach,
                                                  const cColor &in acColor,
                                                  float afBrightness = 1.0f,
                                                  bool abFadeAtDistance = false,
                                                  float afFadeMinEnd = 1.0f,
                                                  float afFadeMinStart = 2.0f,
                                                  float afFadeMaxStart = 100.0f,
                                                  float afFadeMaxEnd = 110.0f)
```

Creates a particle system at entity with extra options.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system entity to be created. |
| `asPSFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | .ps file to create particle system from. |
| `asEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | entity to create particle system at. Can be "player". |
| `abAttach` | `bool` | whether the particle system should be attached to the entity it is created at. |
| `acColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | color of the particle system. |
| `afBrightness` | `float` | brightness of the particle system. |
| `abFadeAtDistance` | `bool` | if the particles should fade depending on distance from the player. |
| `afFadeMinEnd` | `float` | when the player is closer than this, the particles are invisible. |
| `afFadeMinStart` | `float` | distance to the player where the particles will start fading if the player gets closer. |
| `afFadeMaxStart` | `float` | distance to the player where the particles will start fading if the player gets further away. |
| `afFadeMaxEnd` | `float` | when the player is further away than this, the particles are invisible. |

**Returns:** `cParticleSystem@` — the created particle system or null if the function fails.

    1. `ParticleSystem_Destroy`

```cpp
void ParticleSystem_Destroy(const tString &in asPSName)
```

Destroy a particle system. Can contain wildcards.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system entity to be destroyed. |

**Returns:** `void`

    1. `ParticleSystem_Exists`

```cpp
bool ParticleSystem_Exists(const tString &in asPSName)
```

Returns true or false if a given particle system exists

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system. Can contain wildcards. |

**Returns:** `bool`

    1. `ParticleSystem_Preload`

```cpp
void ParticleSystem_Preload(const tString &in asFile)
```

Preload particle system data

| Name | Type | Description |
| --- | --- | --- |
| `asFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | file to preload |

**Returns:** `void`

    1. `ParticleSystem_SetActive`

```cpp
void ParticleSystem_SetActive(const tString &in asPSName,
                              bool abActive)
```

Activates or deactivates a particle system.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system. Can contain wildcards. |
| `abActive` | `bool` | if is should be set to active. |

**Returns:** `void`

    1. `ParticleSystem_SetBrightness`

```cpp
void ParticleSystem_SetBrightness(const tString &in asPSName,
                                  float afBrightness)
```

Sets the brightness of a particle system.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system. Can contain wildcards. |
| `afBrightness` | `float` | the color to set |

**Returns:** `void`

    1. `ParticleSystem_SetColor`

```cpp
void ParticleSystem_SetColor(const tString &in asPSName,
                             const cColor &in acColor)
```

Sets the color of a particle system.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system. Can contain wildcards. |
| `acColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | the color to set |

**Returns:** `void`

    1. `ParticleSystem_SetVisible`

```cpp
void ParticleSystem_SetVisible(const tString &in asPSName,
                               bool abVisible)
```

Sets the visibility of a particle system.

| Name | Type | Description |
| --- | --- | --- |
| `asPSName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the particle system. Can contain wildcards. |
| `abVisible` | `bool` | if is should be set to visible or not. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/ParticleSystem](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/ParticleSystem)
- Revision: `5045`
- Source update: `2020-08-24T20:57:46Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

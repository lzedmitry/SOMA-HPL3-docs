---
title: Readable
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Readable"
sourceRevision: 5048
sourceUpdated: "2020-08-24T20:58:22Z"
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
| `void` | [`Readable_SetCloseCallback`](#readable-setclosecallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCallback) | Sets the close callback of a readable prop |
| `void` | [`Readable_SetOpenEntityFile`](#readable-setopenentityfile)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityFile) | Sets the open entity file of the readable prop |

## Function Detail
    1. `Readable_SetCloseCallback`

```cpp
void Readable_SetCloseCallback(const tString &in asName,
                               const tString &in asCallback)
```

Sets the close callback of a readable prop.  
Syntax for callback function: void FuncName(const tString &in asEntity).

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of readable prop |
| `asCallback` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the callback function |

**Returns:** `void`

    1. `Readable_SetOpenEntityFile`

```cpp
void Readable_SetOpenEntityFile(const tString &in asName,
                                const tString &in asEntityFile)
```

Sets the open entity file of the readable prop

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of readable prop |
| `asEntityFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the new entity file name |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Readable](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Readable)
- Revision: `5048`
- Source update: `2020-08-24T20:58:22Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: LensFlare
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/LensFlare"
sourceRevision: 5035
sourceUpdated: "2020-08-24T20:55:13Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - api
---
Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!

## Summary
| Return | Function | Description |
| --- | --- | --- |
| `void` | [`LensFlare_SetVisible`](#lensflare-setvisible)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asLensFlareName, bool abVisible) | Sets if a lens flare should be rendered or not |

## Function Detail
    1. `LensFlare_SetVisible`

```cpp
void LensFlare_SetVisible(const tString &in asLensFlareName,
                          bool abVisible)
```

Sets if a lens flare should be rendered or not.

| Name | Type | Description |
| --- | --- | --- |
| `asLensFlareName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of lens flare. Can contain wildcards. |
| `abVisible` | `bool` | if the lens flare should be visible or not. |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/LensFlare](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/LensFlare)
- Revision: `5035`
- Source update: `2020-08-24T20:55:13Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

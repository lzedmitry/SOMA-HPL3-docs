---
title: Tool
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Tool"
sourceRevision: 5054
sourceUpdated: "2020-08-24T21:00:15Z"
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
| `tString` | [`Tool_GetHandAnimationSuffix`](#tool-gethandanimationsuffix)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Returns the hand animation prefix specified for the tool |
| `void` | [`Tool_PickUp`](#tool-pickup)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abEquipTool, bool abCallback) | Adds the specified tool to the player's inventory |
| `void` | [`Tool_SetAutoHideAfterPickup`](#tool-setautohideafterpickup)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | Sets if a tool should be hidden automatically after getting picked up and being displayed for a brief moment |
| `void` | [`Tool_SetHighlightActive`](#tool-sethighlightactive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | Sets if a tool should have the highlight effect when looked at |

## Function Detail
    1. `Tool_GetHandAnimationSuffix`

```cpp
tString Tool_GetHandAnimationSuffix(const tString &in asName)
```

Returns the hand animation prefix specified for the tool.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the tool entity. |

**Returns:** `tString` — the tool's hand animation prefix.

    1. `Tool_PickUp`

```cpp
void Tool_PickUp(const tString &in asName,
                 bool abEquipTool,
                 bool abCallback)
```

Adds the specified tool to the player's inventory. Similar to calling the entity interact on the tool entity, but with more control.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the tool entity to pickup. |
| `abEquipTool` | `bool` | if the tool should be equipped immediately. If the tool has AutoHide active it will still autohide after a while. |
| `abCallback` | `bool` | if the tool's pickup callback should be executed. |

**Returns:** `void`

    1. `Tool_SetAutoHideAfterPickup`

```cpp
void Tool_SetAutoHideAfterPickup(const tString &in asName,
                                 bool abX)
```

Sets if a tool should be hidden automatically after getting picked up and being displayed for a brief moment

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the tool |
| `abX` | `bool` | if it should autohide |

**Returns:** `void`

    1. `Tool_SetHighlightActive`

```cpp
void Tool_SetHighlightActive(const tString &in asName,
                             bool abX)
```

Sets if a tool should have the highlight effect when looked at.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the tool |
| `abX` | `bool` | if it shoudl get highlighted |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Tool](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Tool)
- Revision: `5054`
- Source update: `2020-08-24T21:00:15Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

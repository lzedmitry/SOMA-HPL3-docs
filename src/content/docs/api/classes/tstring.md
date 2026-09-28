---
title: tString
description: "A tString is the HPL3 type for storing strings, or sequences of characters. They are created through use of a string literal, or a series of characters surrounded by quotation marks ( \" )."
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/tString"
sourceRevision: 3952
sourceUpdated: "2020-08-06T15:13:33Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - api
  - api
sidebar:
  hidden: true
---
A `tString` is the HPL3 type for storing strings, or sequences of characters. They are created through use of a string literal, or a series of characters surrounded by quotation marks ( " ).

```
tString sStr = "This is a string.";
```

## Fields
tString has no public fields.

## Functions
| Return Type | Function Name | Parameters | Description |
| --- | --- | --- | --- |
| 
```
uint64
```
 | length |   | Returns the length of the tString. |
| 
```
void
```
 | resize | 
```
uint64 alLength
```
 | Resizes the tString, removing characters and adding null characters as necessary. |

## Remarks
A thing to note is that a `tString` is essentially a wrapper for an array of characters, meaning that you can retrieve characters within a `tString` by using square bracket ( [ ] ) syntax. (Characters in the HPL3 engine are represented by unsigned 8-bit integers, or `uint8`.)

```
uint8 c = sStr[1];
```

A `tString` is [null-terminated](https://wiki.frictionalgames.com/page/wikipedia:Null-terminated_string), meaning that when a `tString` is read (for example, in a `cLux_AddDebugMessage` function), the `tString` will only process its characters until it reaches a null-character, and characters after the null-character, if any, are ignored.

```
sStr.resize(5);
sStr[0] = 'H';
sStr[1] = 'i';
sStr[2] = '\0'; // This is a null-character
sStr[3] = 'Q';
sStr[4] = '9';
cLux_AddDebugMessage(sStr);

// The message as printed: 
// Hi
```

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/tString](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/tString)
- Revision: `3952`
- Source update: `2020-08-06T15:13:33Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: cString
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cString"
sourceRevision: 5026
sourceUpdated: "2020-08-24T20:51:45Z"
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
| `tString` | [`cString_AddSlashAtEnd`](#cstring-addslashatend)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPath) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_AddSlashAtEndW`](#cstring-addslashatendw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asPath) | *Undocumented in the original Wiki.* |
| `bool` | [`cString_CheckWildcardStrings`](#cstring-checkwildcardstrings)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asWildcardStr, [array](https://wiki.frictionalgames.com/page/../../array)<[tString](https://wiki.frictionalgames.com/page/../../tString)> &in avSubStringArray) | *Undocumented in the original Wiki.* |
| `int` | [`cString_CountCharsInString`](#cstring-countcharsinstring)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aChar) | *Undocumented in the original Wiki.* |
| `int` | [`cString_CountCharsInStringW`](#cstring-countcharsinstringw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aChar) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_Get16BitFromArray`](#cstring-get16bitfromarray)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asArray) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_GetFileExt`](#cstring-getfileext)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_GetFileExtW`](#cstring-getfileextw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_GetFileName`](#cstring-getfilename)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_GetFileNameW`](#cstring-getfilenamew)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_GetFilePath`](#cstring-getfilepath)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_GetFilePathTopFolder`](#cstring-getfilepathtopfolder)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_GetFilePathTopFolderW`](#cstring-getfilepathtopfolderw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_GetFilePathW`](#cstring-getfilepathw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetFirstCharPos`](#cstring-getfirstcharpos)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, int8 alChar) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetFirstStringPos`](#cstring-getfirststringpos)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aChar) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetFirstStringPosW`](#cstring-getfirststringposw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aChar) | *Undocumented in the original Wiki.* |
| `void` | [`cString_GetFloatVec`](#cstring-getfloatvec)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asData, [array](https://wiki.frictionalgames.com/page/../../array)<float> &inout avOutFloats, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asSepp) | *Undocumented in the original Wiki.* |
| `uint` | [`cString_GetHash`](#cstring-gethash)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr) | *Undocumented in the original Wiki.* |
| `uint64` | [`cString_GetHash64`](#cstring-gethash64)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr) | *Undocumented in the original Wiki.* |
| `uint64` | [`cString_GetHash64W`](#cstring-gethash64w)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asStr) | *Undocumented in the original Wiki.* |
| `uint` | [`cString_GetHashW`](#cstring-gethashw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asStr) | *Undocumented in the original Wiki.* |
| `void` | [`cString_GetIntVec`](#cstring-getintvec)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asData, [array](https://wiki.frictionalgames.com/page/../../array)<int> &inout avOutInts, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asSepp) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_GetLastChar`](#cstring-getlastchar)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetLastCharPos`](#cstring-getlastcharpos)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, int8 alChar) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_GetLastCharW`](#cstring-getlastcharw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetLastStringPos`](#cstring-getlaststringpos)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aChar) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetLastStringPosW`](#cstring-getlaststringposw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aChar) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_GetNumericSuffix`](#cstring-getnumericsuffix)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr) | *Undocumented in the original Wiki.* |
| `float` | [`cString_GetNumericSuffixFloat`](#cstring-getnumericsuffixfloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, float afDefault = 0) | *Undocumented in the original Wiki.* |
| `float` | [`cString_GetNumericSuffixFloatW`](#cstring-getnumericsuffixfloatw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, float afDefault = 0) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetNumericSuffixInt`](#cstring-getnumericsuffixint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, int alDefault = 0) | *Undocumented in the original Wiki.* |
| `int` | [`cString_GetNumericSuffixIntW`](#cstring-getnumericsuffixintw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, int alDefault = 0) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_GetNumericSuffixW`](#cstring-getnumericsuffixw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asStr) | *Undocumented in the original Wiki.* |
| `void` | [`cString_GetStringVec`](#cstring-getstringvec)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asData, [array](https://wiki.frictionalgames.com/page/../../array)<[tString](https://wiki.frictionalgames.com/page/../../tString)> &inout avOutStrings, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asSepp) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_RemoveSlashAtEnd`](#cstring-removeslashatend)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asPath) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_RemoveSlashAtEndW`](#cstring-removeslashatendw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asPath) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_ReplaceCharTo`](#cstring-replacecharto)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asOldChar, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asNewChar) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_ReplaceCharToW`](#cstring-replacechartow)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asOldChar, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asNewChar) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_ReplaceStringTo`](#cstring-replacestringto)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asOldString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asNewString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_ReplaceStringToW`](#cstring-replacestringtow)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asOldString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asNewString) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_S16BitToUTF8`](#cstring-s16bittoutf8)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in awsString) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_SetFileExt`](#cstring-setfileext)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aExt) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_SetFileExtW`](#cstring-setfileextw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aExt) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_SetFilePath`](#cstring-setfilepath)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aPath) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_SetFilePathW`](#cstring-setfilepathw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString, const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aPath) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_Sub`](#cstring-sub)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asString, int alStart, int alCount = -1) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_SubW`](#cstring-subw)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in asString, int alStart, int alCount = -1) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_To16Char`](#cstring-to16char)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asString) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_To8Char`](#cstring-to8char)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in awsString) | *Undocumented in the original Wiki.* |
| `bool` | [`cString_ToBool`](#cstring-tobool)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, bool abDefault) | *Undocumented in the original Wiki.* |
| `cColor` | [`cString_ToColor`](#cstring-tocolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aDefault) | *Undocumented in the original Wiki.* |
| `float` | [`cString_ToFloat`](#cstring-tofloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, float afDefault) | *Undocumented in the original Wiki.* |
| `int` | [`cString_ToInt`](#cstring-toint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, int alDefault) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_ToLowerCase`](#cstring-tolowercase)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_ToLowerCaseW`](#cstring-tolowercasew)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `cMatrixf` | [`cString_ToMatrixf`](#cstring-tomatrixf)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf) &in a_mtxDefault) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_ToString`](#cstring-tostring)(float afX, int alNumOfDecimals = -1, bool abRemoveZeros = false) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_ToString`](#cstring-tostring)(int alX, int alPaddingZeros) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_ToStringW`](#cstring-tostringw)(float afX, int alNumOfDecimals = -1, bool abRemoveZeros = false) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_ToStringW`](#cstring-tostringw)(int alX, int alPaddingZeros) | *Undocumented in the original Wiki.* |
| `tString` | [`cString_ToUpperCase`](#cstring-touppercase)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in aString) | *Undocumented in the original Wiki.* |
| `tWString` | [`cString_ToUpperCaseW`](#cstring-touppercasew)(const [tWString](https://wiki.frictionalgames.com/page/../../tWString) &in aString) | *Undocumented in the original Wiki.* |
| `cVector2f` | [`cString_ToVector2f`](#cstring-tovector2f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avDefault) | *Undocumented in the original Wiki.* |
| `cVector2l` | [`cString_ToVector2l`](#cstring-tovector2l)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cVector2l](https://wiki.frictionalgames.com/page/../../cVector2l) &in avDefault) | *Undocumented in the original Wiki.* |
| `cVector3f` | [`cString_ToVector3f`](#cstring-tovector3f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avDefault) | *Undocumented in the original Wiki.* |
| `cVector3l` | [`cString_ToVector3l`](#cstring-tovector3l)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cVector3l](https://wiki.frictionalgames.com/page/../../cVector3l) &in avDefault) | *Undocumented in the original Wiki.* |
| `cVector4f` | [`cString_ToVector4f`](#cstring-tovector4f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asStr, const [cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f) &in avDefault) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cString_AddSlashAtEnd`

```angelscript
tString cString_AddSlashAtEnd(const tString &in asPath)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asPath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_AddSlashAtEndW`

```angelscript
tWString cString_AddSlashAtEndW(const tWString &in asPath)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asPath` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_CheckWildcardStrings`

```angelscript
bool cString_CheckWildcardStrings(const tString &in asStr,
                                  const tString &in asWildcardStr,
                                  tString &in avSubStringArray)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asWildcardStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avSubStringArray` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cString_CountCharsInString`

```angelscript
int cString_CountCharsInString(const tString &in aString,
                               const tString &in aChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aChar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `int`

    1. `cString_CountCharsInStringW`

```angelscript
int cString_CountCharsInStringW(const tWString &in aString,
                                const tWString &in aChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `aChar` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `int`

    1. `cString_Get16BitFromArray`

```angelscript
tWString cString_Get16BitFromArray(const tString &in asArray)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asArray` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tWString`

    1. `cString_GetFileExt`

```angelscript
tString cString_GetFileExt(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_GetFileExtW`

```angelscript
tWString cString_GetFileExtW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_GetFileName`

```angelscript
tString cString_GetFileName(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_GetFileNameW`

```angelscript
tWString cString_GetFileNameW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_GetFilePath`

```angelscript
tString cString_GetFilePath(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_GetFilePathTopFolder`

```angelscript
tString cString_GetFilePathTopFolder(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_GetFilePathTopFolderW`

```angelscript
tWString cString_GetFilePathTopFolderW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_GetFilePathW`

```angelscript
tWString cString_GetFilePathW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_GetFirstCharPos`

```angelscript
int cString_GetFirstCharPos(const tString &in aString,
                            int8 alChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alChar` | `int8` | — |

**Returns:** `int`

    1. `cString_GetFirstStringPos`

```angelscript
int cString_GetFirstStringPos(const tString &in aString,
                              const tString &in aChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aChar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `int`

    1. `cString_GetFirstStringPosW`

```angelscript
int cString_GetFirstStringPosW(const tWString &in aString,
                               const tWString &in aChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `aChar` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `int`

    1. `cString_GetFloatVec`

```angelscript
void cString_GetFloatVec(const tString &in asData,
                         float &inout avOutFloats,
                         const tString &in asSepp)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asData` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avOutFloats` | `float` | — |
| `asSepp` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cString_GetHash`

```angelscript
uint cString_GetHash(const tString &in asStr)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `uint`

    1. `cString_GetHash64`

```angelscript
uint64 cString_GetHash64(const tString &in asStr)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `uint64`

    1. `cString_GetHash64W`

```angelscript
uint64 cString_GetHash64W(const tWString &in asStr)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `uint64`

    1. `cString_GetHashW`

```angelscript
uint cString_GetHashW(const tWString &in asStr)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `uint`

    1. `cString_GetIntVec`

```angelscript
void cString_GetIntVec(const tString &in asData,
                       int &inout avOutInts,
                       const tString &in asSepp)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asData` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avOutInts` | `int` | — |
| `asSepp` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cString_GetLastChar`

```angelscript
tString cString_GetLastChar(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_GetLastCharPos`

```angelscript
int cString_GetLastCharPos(const tString &in aString,
                           int8 alChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alChar` | `int8` | — |

**Returns:** `int`

    1. `cString_GetLastCharW`

```angelscript
tWString cString_GetLastCharW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_GetLastStringPos`

```angelscript
int cString_GetLastStringPos(const tString &in aString,
                             const tString &in aChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aChar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `int`

    1. `cString_GetLastStringPosW`

```angelscript
int cString_GetLastStringPosW(const tWString &in aString,
                              const tWString &in aChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `aChar` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `int`

    1. `cString_GetNumericSuffix`

```angelscript
tString cString_GetNumericSuffix(const tString &in asStr)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_GetNumericSuffixFloat`

```angelscript
float cString_GetNumericSuffixFloat(const tString &in aString,
                                    float afDefault = 0)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afDefault` | `float` | — |

**Returns:** `float`

    1. `cString_GetNumericSuffixFloatW`

```angelscript
float cString_GetNumericSuffixFloatW(const tWString &in aString,
                                     float afDefault = 0)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `afDefault` | `float` | — |

**Returns:** `float`

    1. `cString_GetNumericSuffixInt`

```angelscript
int cString_GetNumericSuffixInt(const tString &in aString,
                                int alDefault = 0)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alDefault` | `int` | — |

**Returns:** `int`

    1. `cString_GetNumericSuffixIntW`

```angelscript
int cString_GetNumericSuffixIntW(const tWString &in aString,
                                 int alDefault = 0)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `alDefault` | `int` | — |

**Returns:** `int`

    1. `cString_GetNumericSuffixW`

```angelscript
tWString cString_GetNumericSuffixW(const tWString &in asStr)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_GetStringVec`

```angelscript
void cString_GetStringVec(const tString &in asData,
                          tString &inout avOutStrings,
                          const tString &in asSepp)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asData` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avOutStrings` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asSepp` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cString_RemoveSlashAtEnd`

```angelscript
tString cString_RemoveSlashAtEnd(const tString &in asPath)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asPath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_RemoveSlashAtEndW`

```angelscript
tWString cString_RemoveSlashAtEndW(const tWString &in asPath)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asPath` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_ReplaceCharTo`

```angelscript
tString cString_ReplaceCharTo(const tString &in aString,
                              const tString &in asOldChar,
                              const tString &in asNewChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asOldChar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asNewChar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_ReplaceCharToW`

```angelscript
tWString cString_ReplaceCharToW(const tWString &in aString,
                                const tWString &in asOldChar,
                                const tWString &in asNewChar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `asOldChar` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `asNewChar` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_ReplaceStringTo`

```angelscript
tString cString_ReplaceStringTo(const tString &in aString,
                                const tString &in asOldString,
                                const tString &in asNewString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asOldString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asNewString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_ReplaceStringToW`

```angelscript
tWString cString_ReplaceStringToW(const tWString &in aString,
                                  const tWString &in asOldString,
                                  const tWString &in asNewString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `asOldString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `asNewString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_S16BitToUTF8`

```angelscript
tString cString_S16BitToUTF8(const tWString &in awsString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `awsString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tString`

    1. `cString_SetFileExt`

```angelscript
tString cString_SetFileExt(const tString &in aString,
                           const tString &in aExt)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aExt` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_SetFileExtW`

```angelscript
tWString cString_SetFileExtW(const tWString &in aString,
                             const tWString &in aExt)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `aExt` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_SetFilePath`

```angelscript
tString cString_SetFilePath(const tString &in aString,
                            const tString &in aPath)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aPath` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_SetFilePathW`

```angelscript
tWString cString_SetFilePathW(const tWString &in aString,
                              const tWString &in aPath)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `aPath` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_Sub`

```angelscript
tString cString_Sub(const tString &in asString,
                    int alStart,
                    int alCount = -1)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alStart` | `int` | — |
| `alCount` | `int` | — |

**Returns:** `tString`

    1. `cString_SubW`

```angelscript
tWString cString_SubW(const tWString &in asString,
                      int alStart,
                      int alCount = -1)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |
| `alStart` | `int` | — |
| `alCount` | `int` | — |

**Returns:** `tWString`

    1. `cString_To16Char`

```angelscript
tWString cString_To16Char(const tString &in asString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tWString`

    1. `cString_To8Char`

```angelscript
tString cString_To8Char(const tWString &in awsString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `awsString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tString`

    1. `cString_ToBool`

```angelscript
bool cString_ToBool(const tString &in asStr,
                    bool abDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abDefault` | `bool` | — |

**Returns:** `bool`

    1. `cString_ToColor`

```angelscript
cColor cString_ToColor(const tString &in asStr,
                       const cColor &in aDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aDefault` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |

**Returns:** `cColor`

    1. `cString_ToFloat`

```angelscript
float cString_ToFloat(const tString &in asStr,
                      float afDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afDefault` | `float` | — |

**Returns:** `float`

    1. `cString_ToInt`

```angelscript
int cString_ToInt(const tString &in asStr,
                  int alDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alDefault` | `int` | — |

**Returns:** `int`

    1. `cString_ToLowerCase`

```angelscript
tString cString_ToLowerCase(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_ToLowerCaseW`

```angelscript
tWString cString_ToLowerCaseW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_ToMatrixf`

```angelscript
cMatrixf cString_ToMatrixf(const tString &in asStr,
                           const cMatrixf &in a_mtxDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `a_mtxDefault` | `[cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf)` | — |

**Returns:** `cMatrixf`

    1. `cString_ToString`

```angelscript
tString cString_ToString(float afX,
                         int alNumOfDecimals = -1,
                         bool abRemoveZeros = false)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afX` | `float` | — |
| `alNumOfDecimals` | `int` | — |
| `abRemoveZeros` | `bool` | — |

**Returns:** `tString`

    1. `cString_ToString`

```angelscript
tString cString_ToString(int alX,
                         int alPaddingZeros)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alX` | `int` | — |
| `alPaddingZeros` | `int` | — |

**Returns:** `tString`

    1. `cString_ToStringW`

```angelscript
tWString cString_ToStringW(float afX,
                           int alNumOfDecimals = -1,
                           bool abRemoveZeros = false)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afX` | `float` | — |
| `alNumOfDecimals` | `int` | — |
| `abRemoveZeros` | `bool` | — |

**Returns:** `tWString`

    1. `cString_ToStringW`

```angelscript
tWString cString_ToStringW(int alX,
                           int alPaddingZeros)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alX` | `int` | — |
| `alPaddingZeros` | `int` | — |

**Returns:** `tWString`

    1. `cString_ToUpperCase`

```angelscript
tString cString_ToUpperCase(const tString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cString_ToUpperCaseW`

```angelscript
tWString cString_ToUpperCaseW(const tWString &in aString)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aString` | `[tWString](https://wiki.frictionalgames.com/page/../../tWString)` | — |

**Returns:** `tWString`

    1. `cString_ToVector2f`

```angelscript
cVector2f cString_ToVector2f(const tString &in asStr,
                             const cVector2f &in avDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avDefault` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | — |

**Returns:** `cVector2f`

    1. `cString_ToVector2l`

```angelscript
cVector2l cString_ToVector2l(const tString &in asStr,
                             const cVector2l &in avDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avDefault` | `[cVector2l](https://wiki.frictionalgames.com/page/../../cVector2l)` | — |

**Returns:** `cVector2l`

    1. `cString_ToVector3f`

```angelscript
cVector3f cString_ToVector3f(const tString &in asStr,
                             const cVector3f &in avDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avDefault` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |

**Returns:** `cVector3f`

    1. `cString_ToVector3l`

```angelscript
cVector3l cString_ToVector3l(const tString &in asStr,
                             const cVector3l &in avDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avDefault` | `[cVector3l](https://wiki.frictionalgames.com/page/../../cVector3l)` | — |

**Returns:** `cVector3l`

    1. `cString_ToVector4f`

```angelscript
cVector4f cString_ToVector4f(const tString &in asStr,
                             const cVector4f &in avDefault)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asStr` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avDefault` | `[cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f)` | — |

**Returns:** `cVector4f`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cString](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cString)
- Revision: `5026`
- Source update: `2020-08-24T20:51:45Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

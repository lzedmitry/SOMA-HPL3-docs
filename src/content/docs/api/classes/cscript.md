---
title: cScript
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cScript"
sourceRevision: 5024
sourceUpdated: "2020-08-24T20:51:08Z"
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
| `bool` | [`cScript_GetGlobalArgBool`](#cscript-getglobalargbool)(int alIdx) | *Undocumented in the original Wiki.* |
| `cColor` | [`cScript_GetGlobalArgColor`](#cscript-getglobalargcolor)(int alIdx) | *Undocumented in the original Wiki.* |
| `float` | [`cScript_GetGlobalArgFloat`](#cscript-getglobalargfloat)(int alIdx) | *Undocumented in the original Wiki.* |
| `tID` | [`cScript_GetGlobalArgID`](#cscript-getglobalargid)(int alIdx) | *Undocumented in the original Wiki.* |
| `int` | [`cScript_GetGlobalArgInt`](#cscript-getglobalargint)(int alIdx) | *Undocumented in the original Wiki.* |
| `cMatrixf` | [`cScript_GetGlobalArgMatrix`](#cscript-getglobalargmatrix)(int alIdx) | *Undocumented in the original Wiki.* |
| `tString` | [`cScript_GetGlobalArgString`](#cscript-getglobalargstring)(int alIdx) | *Undocumented in the original Wiki.* |
| `cVector2f` | [`cScript_GetGlobalArgVector2f`](#cscript-getglobalargvector2f)(int alIdx) | *Undocumented in the original Wiki.* |
| `cVector3f` | [`cScript_GetGlobalArgVector3f`](#cscript-getglobalargvector3f)(int alIdx) | *Undocumented in the original Wiki.* |
| `cVector4f` | [`cScript_GetGlobalArgVector4f`](#cscript-getglobalargvector4f)(int alIdx) | *Undocumented in the original Wiki.* |
| `bool` | [`cScript_GetGlobalReturnBool`](#cscript-getglobalreturnbool)() | *Undocumented in the original Wiki.* |
| `cColor` | [`cScript_GetGlobalReturnColor`](#cscript-getglobalreturncolor)() | *Undocumented in the original Wiki.* |
| `float` | [`cScript_GetGlobalReturnFloat`](#cscript-getglobalreturnfloat)() | *Undocumented in the original Wiki.* |
| `tID` | [`cScript_GetGlobalReturnID`](#cscript-getglobalreturnid)() | *Undocumented in the original Wiki.* |
| `int` | [`cScript_GetGlobalReturnInt`](#cscript-getglobalreturnint)() | *Undocumented in the original Wiki.* |
| `cMatrixf` | [`cScript_GetGlobalReturnMatrix`](#cscript-getglobalreturnmatrix)() | *Undocumented in the original Wiki.* |
| `tString` | [`cScript_GetGlobalReturnString`](#cscript-getglobalreturnstring)() | *Undocumented in the original Wiki.* |
| `cVector2f` | [`cScript_GetGlobalReturnVector2f`](#cscript-getglobalreturnvector2f)() | *Undocumented in the original Wiki.* |
| `cVector3f` | [`cScript_GetGlobalReturnVector3f`](#cscript-getglobalreturnvector3f)() | *Undocumented in the original Wiki.* |
| `cVector4f` | [`cScript_GetGlobalReturnVector4f`](#cscript-getglobalreturnvector4f)() | *Undocumented in the original Wiki.* |
| `bool` | [`cScript_GetGlobalVarBool`](#cscript-getglobalvarbool)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cColor` | [`cScript_GetGlobalVarColor`](#cscript-getglobalvarcolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `float` | [`cScript_GetGlobalVarFloat`](#cscript-getglobalvarfloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `tID` | [`cScript_GetGlobalVarID`](#cscript-getglobalvarid)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `int` | [`cScript_GetGlobalVarInt`](#cscript-getglobalvarint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cMatrixf` | [`cScript_GetGlobalVarMatrix`](#cscript-getglobalvarmatrix)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `tString` | [`cScript_GetGlobalVarString`](#cscript-getglobalvarstring)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cVector2f` | [`cScript_GetGlobalVarVector2f`](#cscript-getglobalvarvector2f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cVector3f` | [`cScript_GetGlobalVarVector3f`](#cscript-getglobalvarvector3f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `cVector4f` | [`cScript_GetGlobalVarVector4f`](#cscript-getglobalvarvector4f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | *Undocumented in the original Wiki.* |
| `bool` | [`cScript_RunGlobalFunc`](#cscript-runglobalfunc)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asObjName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asClassName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFuncName) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgBool`](#cscript-setglobalargbool)(int alIdx, bool abX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgColor`](#cscript-setglobalargcolor)(int alIdx, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgFloat`](#cscript-setglobalargfloat)(int alIdx, float afX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgID`](#cscript-setglobalargid)(int alIdx, [tID](https://wiki.frictionalgames.com/page/../../tID) alX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgInt`](#cscript-setglobalargint)(int alIdx, int alX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgMatrix`](#cscript-setglobalargmatrix)(int alIdx, const [cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf) &in a_mtxX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgString`](#cscript-setglobalargstring)(int alIdx, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVar) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgVector2f`](#cscript-setglobalargvector2f)(int alIdx, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgVector3f`](#cscript-setglobalargvector3f)(int alIdx, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalArgVector4f`](#cscript-setglobalargvector4f)(int alIdx, const [cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnBool`](#cscript-setglobalreturnbool)(bool abX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnColor`](#cscript-setglobalreturncolor)(const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnFloat`](#cscript-setglobalreturnfloat)(float afX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnID`](#cscript-setglobalreturnid)([tID](https://wiki.frictionalgames.com/page/../../tID) alX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnInt`](#cscript-setglobalreturnint)(int alX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnMatrix`](#cscript-setglobalreturnmatrix)(const [cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf) &in a_mtxX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnString`](#cscript-setglobalreturnstring)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVar) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnVector2f`](#cscript-setglobalreturnvector2f)(const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnVector3f`](#cscript-setglobalreturnvector3f)(const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalReturnVector4f`](#cscript-setglobalreturnvector4f)(const [cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarBool`](#cscript-setglobalvarbool)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarColor`](#cscript-setglobalvarcolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarFloat`](#cscript-setglobalvarfloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, float afX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarID`](#cscript-setglobalvarid)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, [tID](https://wiki.frictionalgames.com/page/../../tID) alX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarInt`](#cscript-setglobalvarint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, int alX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarMatrix`](#cscript-setglobalvarmatrix)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf) &in a_mtxX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarString`](#cscript-setglobalvarstring)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVar) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarVector2f`](#cscript-setglobalvarvector2f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarVector3f`](#cscript-setglobalvarvector3f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avX) | *Undocumented in the original Wiki.* |
| `void` | [`cScript_SetGlobalVarVector4f`](#cscript-setglobalvarvector4f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f) &in avX) | *Undocumented in the original Wiki.* |

## Function Detail
    1. `cScript_GetGlobalArgBool`

```angelscript
bool cScript_GetGlobalArgBool(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `bool`

    1. `cScript_GetGlobalArgColor`

```angelscript
cColor cScript_GetGlobalArgColor(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `cColor`

    1. `cScript_GetGlobalArgFloat`

```angelscript
float cScript_GetGlobalArgFloat(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `float`

    1. `cScript_GetGlobalArgID`

```angelscript
tID cScript_GetGlobalArgID(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `tID`

    1. `cScript_GetGlobalArgInt`

```angelscript
int cScript_GetGlobalArgInt(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `int`

    1. `cScript_GetGlobalArgMatrix`

```angelscript
cMatrixf cScript_GetGlobalArgMatrix(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `cMatrixf`

    1. `cScript_GetGlobalArgString`

```angelscript
tString cScript_GetGlobalArgString(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `tString`

    1. `cScript_GetGlobalArgVector2f`

```angelscript
cVector2f cScript_GetGlobalArgVector2f(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `cVector2f`

    1. `cScript_GetGlobalArgVector3f`

```angelscript
cVector3f cScript_GetGlobalArgVector3f(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `cVector3f`

    1. `cScript_GetGlobalArgVector4f`

```angelscript
cVector4f cScript_GetGlobalArgVector4f(int alIdx)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |

**Returns:** `cVector4f`

    1. `cScript_GetGlobalReturnBool`

```angelscript
bool cScript_GetGlobalReturnBool()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `bool`

    1. `cScript_GetGlobalReturnColor`

```angelscript
cColor cScript_GetGlobalReturnColor()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `cColor`

    1. `cScript_GetGlobalReturnFloat`

```angelscript
float cScript_GetGlobalReturnFloat()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `float`

    1. `cScript_GetGlobalReturnID`

```angelscript
tID cScript_GetGlobalReturnID()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `tID`

    1. `cScript_GetGlobalReturnInt`

```angelscript
int cScript_GetGlobalReturnInt()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `int`

    1. `cScript_GetGlobalReturnMatrix`

```angelscript
cMatrixf cScript_GetGlobalReturnMatrix()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `cMatrixf`

    1. `cScript_GetGlobalReturnString`

```angelscript
const tString& cScript_GetGlobalReturnString()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `const tString&`

    1. `cScript_GetGlobalReturnVector2f`

```angelscript
cVector2f cScript_GetGlobalReturnVector2f()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `cVector2f`

    1. `cScript_GetGlobalReturnVector3f`

```angelscript
cVector3f cScript_GetGlobalReturnVector3f()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `cVector3f`

    1. `cScript_GetGlobalReturnVector4f`

```angelscript
cVector4f cScript_GetGlobalReturnVector4f()
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

**Returns:** `cVector4f`

    1. `cScript_GetGlobalVarBool`

```angelscript
bool cScript_GetGlobalVarBool(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cScript_GetGlobalVarColor`

```angelscript
cColor cScript_GetGlobalVarColor(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cColor`

    1. `cScript_GetGlobalVarFloat`

```angelscript
float cScript_GetGlobalVarFloat(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `float`

    1. `cScript_GetGlobalVarID`

```angelscript
tID cScript_GetGlobalVarID(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tID`

    1. `cScript_GetGlobalVarInt`

```angelscript
int cScript_GetGlobalVarInt(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `int`

    1. `cScript_GetGlobalVarMatrix`

```angelscript
cMatrixf cScript_GetGlobalVarMatrix(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cMatrixf`

    1. `cScript_GetGlobalVarString`

```angelscript
tString cScript_GetGlobalVarString(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `tString`

    1. `cScript_GetGlobalVarVector2f`

```angelscript
cVector2f cScript_GetGlobalVarVector2f(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cVector2f`

    1. `cScript_GetGlobalVarVector3f`

```angelscript
cVector3f cScript_GetGlobalVarVector3f(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cVector3f`

    1. `cScript_GetGlobalVarVector4f`

```angelscript
cVector4f cScript_GetGlobalVarVector4f(const tString &in asName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `cVector4f`

    1. `cScript_RunGlobalFunc`

```angelscript
bool cScript_RunGlobalFunc(const tString &in asObjName,
                           const tString &in asClassName,
                           const tString &in asFuncName)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asObjName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asClassName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asFuncName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `bool`

    1. `cScript_SetGlobalArgBool`

```angelscript
void cScript_SetGlobalArgBool(int alIdx,
                              bool abX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `abX` | `bool` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgColor`

```angelscript
void cScript_SetGlobalArgColor(int alIdx,
                               const cColor &in aX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `aX` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgFloat`

```angelscript
void cScript_SetGlobalArgFloat(int alIdx,
                               float afX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `afX` | `float` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgID`

```angelscript
void cScript_SetGlobalArgID(int alIdx,
                            tID alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `alX` | `[tID](https://wiki.frictionalgames.com/page/../../tID)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgInt`

```angelscript
void cScript_SetGlobalArgInt(int alIdx,
                             int alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `alX` | `int` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgMatrix`

```angelscript
void cScript_SetGlobalArgMatrix(int alIdx,
                                const cMatrixf &in a_mtxX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `a_mtxX` | `[cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgString`

```angelscript
void cScript_SetGlobalArgString(int alIdx,
                                const tString &in asVar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `asVar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgVector2f`

```angelscript
void cScript_SetGlobalArgVector2f(int alIdx,
                                  const cVector2f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `avX` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgVector3f`

```angelscript
void cScript_SetGlobalArgVector3f(int alIdx,
                                  const cVector3f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `avX` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalArgVector4f`

```angelscript
void cScript_SetGlobalArgVector4f(int alIdx,
                                  const cVector4f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alIdx` | `int` | — |
| `avX` | `[cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnBool`

```angelscript
void cScript_SetGlobalReturnBool(bool abX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `abX` | `bool` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnColor`

```angelscript
void cScript_SetGlobalReturnColor(const cColor &in aX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `aX` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnFloat`

```angelscript
void cScript_SetGlobalReturnFloat(float afX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `afX` | `float` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnID`

```angelscript
void cScript_SetGlobalReturnID(tID alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alX` | `[tID](https://wiki.frictionalgames.com/page/../../tID)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnInt`

```angelscript
void cScript_SetGlobalReturnInt(int alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `alX` | `int` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnMatrix`

```angelscript
void cScript_SetGlobalReturnMatrix(const cMatrixf &in a_mtxX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `a_mtxX` | `[cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnString`

```angelscript
void cScript_SetGlobalReturnString(const tString &in asVar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asVar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnVector2f`

```angelscript
void cScript_SetGlobalReturnVector2f(const cVector2f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `avX` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnVector3f`

```angelscript
void cScript_SetGlobalReturnVector3f(const cVector3f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `avX` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalReturnVector4f`

```angelscript
void cScript_SetGlobalReturnVector4f(const cVector4f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `avX` | `[cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarBool`

```angelscript
void cScript_SetGlobalVarBool(const tString &in asName,
                              bool abX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `abX` | `bool` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarColor`

```angelscript
void cScript_SetGlobalVarColor(const tString &in asName,
                               const cColor &in aX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `aX` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarFloat`

```angelscript
void cScript_SetGlobalVarFloat(const tString &in asName,
                               float afX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `afX` | `float` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarID`

```angelscript
void cScript_SetGlobalVarID(const tString &in asName,
                            tID alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alX` | `[tID](https://wiki.frictionalgames.com/page/../../tID)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarInt`

```angelscript
void cScript_SetGlobalVarInt(const tString &in asName,
                             int alX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `alX` | `int` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarMatrix`

```angelscript
void cScript_SetGlobalVarMatrix(const tString &in asName,
                                const cMatrixf &in a_mtxX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `a_mtxX` | `[cMatrixf](https://wiki.frictionalgames.com/page/../../cMatrixf)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarString`

```angelscript
void cScript_SetGlobalVarString(const tString &in asName,
                                const tString &in asVar)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `asVar` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarVector2f`

```angelscript
void cScript_SetGlobalVarVector2f(const tString &in asName,
                                  const cVector2f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avX` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarVector3f`

```angelscript
void cScript_SetGlobalVarVector3f(const tString &in asName,
                                  const cVector3f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avX` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | — |

**Returns:** `void`

    1. `cScript_SetGlobalVarVector4f`

```angelscript
void cScript_SetGlobalVarVector4f(const tString &in asName,
                                  const cVector4f &in avX)
```

:::note[Documentation status]
Undocumented in the original Frictional Wiki. Signature preserved from the generated API dump.
:::

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | — |
| `avX` | `[cVector4f](https://wiki.frictionalgames.com/page/../../cVector4f)` | — |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/cScript](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/cScript)
- Revision: `5024`
- Source update: `2020-08-24T20:51:08Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

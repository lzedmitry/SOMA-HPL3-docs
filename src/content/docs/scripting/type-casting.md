---
title: Type Casting
description: "An implicit conversion is inserted automatically by the compiler when the required target type is unambiguous and the conversion is allowed:"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Type_Casting"
sourceRevision: 7046
sourceUpdated: "2026-07-30T08:21:01Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

## Implicit and explicit conversion
An **implicit conversion** is inserted automatically by the compiler when the required target type is unambiguous and the conversion is allowed:

```
int lCount = 5;
float fCount = lCount;
```

An **explicit conversion** states the desired target type in the script:

```
float fProgress = 7.8f;
int lWholeSteps = int(fProgress);
```

Explicit casts are useful when:

- information may be lost;
- several conversions are possible;
- an enum is involved;
- converting a base-class or interface handle to a derived type; or
- the intended arithmetic type would otherwise be unclear.

:::tip[Tip]
Prefer an explicit cast whenever it makes the intended type or loss of precision easier to see.
:::

## Numeric casts
Primitive numeric types are converted with syntax resembling a function call:

```
int lValue = int(fValue);
uint lIndex = uint(lSignedIndex);
float fValue = float(lValue);
double fPreciseValue = double(fValue);
```

The name before the parentheses is the destination type.

### Integer and floating-point division
An important use of numeric casting is controlling division. Dividing two integers performs integer division:

```
int lResult = 5 / 2; // 2
```

Cast at least one operand to a floating-point type when the fractional result is required:

```
float fResult = float(5) / 2; // 2.5

int lCurrent = 5;
int lMaximum = 8;
float fRatio = float(lCurrent) / float(lMaximum);
```

This pattern is common when an integer count is used to calculate an animation amount, percentage, normalized position, or interpolation factor.

### Floating point to integer
Converting a floating-point value to an integer removes its fractional part:

```
float fTime = 12.75f;
int lWholeSeconds = int(fTime); // 12
```

This is a conversion, not general-purpose rounding. Use a function such as `cMath_Round` or `cMath_RoundToInt` when the desired behavior is to round instead of simply discarding the fractional part.

### Narrowing and signedness
Converting to a type with a smaller range, or converting between signed and unsigned types, can change the value:

```
int lSigned = -1;
uint lUnsigned = uint(lSigned);
```

The cast above does not make a negative index valid. Validate the source value before converting it:

```
if(lSigned < 0)
	return;

uint lIndex = uint(lSigned);
```

:::caution[Caution]
Do not use a cast as a substitute for range checking. Values outside the destination type's range may wrap, truncate, or otherwise produce an unintended result.
:::

## Enum casts
Enums are named integer values. HPL3 commonly stores or transfers them through functions which use `int`, then converts the integer back to the enum type:

```
int lStoredState = cScript_GetGlobalArgInt(0);
eCrossHairState state = eCrossHairState(lStoredState);
```

An enum can also be converted to an integer:

```
int lStoredState = int(state);
```

This is useful for global arguments, entity variables, configuration values, array indexing, or arithmetic on sequential enum values.

### Validate external enum values
Casting an integer to an enum does not guarantee that the integer matches one of the enum's named constants:

```
int lStoredState = cScript_GetGlobalArgInt(0);

if(lStoredState < int(eCrossHairState_None) ||
   lStoredState >= int(eCrossHairState_LastEnum))
{
	lStoredState = int(eCrossHairState_None);
}

eCrossHairState state = eCrossHairState(lStoredState);
```

The exact valid range depends on the enum. Some HPL3 enums include a `LastEnum` member for bounds checking, while others do not.

Always include a `default` case when switching on a value that may have come from a file, entity variable, save data, or another untrusted integer source:

```
switch(state)
{
	case eCrossHairState_None:
		break;

	case eCrossHairState_PushButton:
		break;

	default:
		cLux_AddDebugMessage("Unsupported crosshair state: " + int(state));
		break;
}
```

## Object-handle casts
Object handles can be cast between compatible reference types with `cast<Type>`:

```
TargetType@ pTarget = cast<TargetType>(pSource);
```

Unlike a value conversion, a reference cast does not copy or create the object. The returned handle refers to the same object through another compatible class or interface.

### Upcasting
Converting a derived-class handle to a base-class or implemented-interface handle is called **upcasting**. It is safe and is normally implicit:

```
class cBase
{
	void BaseMethod() {}
}

class cDerived : cBase
{
	void DerivedMethod() {}
}

cDerived derived;
cBase@ pBase = @derived;
```

The object is still a `cDerived` instance, but only the members exposed by `cBase` are available through `pBase`.

HPL3 uses this pattern when a function accepts a common base type or interface. A GUI callback, for example, may receive `iWidget@` even when the actual widget is a button, label, image, or window.

### Downcasting
Converting a base-class or interface handle to a more specific derived type is called **downcasting**. It must be explicit because the object may not actually have the requested type:

```
void OnPressButton(iWidget@ apWidget, cGuiMessageData@ apData)
{
	cWidgetButton@ pButton = cast<cWidgetButton>(apWidget);

	if(pButton is null)
	{
		cLux_AddDebugMessage("The callback widget is not a button");
		return;
	}

	pButton.SetText(cString_To16Char("Pressed"));
}
```

If `apWidget` refers to a compatible `cWidgetButton`, the cast returns a valid handle to that same widget. If it refers to another widget type, the cast returns `null`.

:::caution[Caution]
Always check a downcast before accessing type-specific members unless the object's exact type is already guaranteed by the API contract and surrounding code.
:::

## Casting HPL3 entities
Many entity functions return the common base type `iLuxEntity@`. A cast or typed helper is required to use members belonging to a more specific entity class:

```
iLuxEntity@ pEntity = Map_GetEntity("MyProp");
cLuxProp@ pProp = cast<cLuxProp>(pEntity);

if(pProp is null)
{
	cLux_AddDebugMessage("MyProp was not found or is not a prop");
	return;
}

// Use cLuxProp-specific members here.
```

When a typed lookup already exists, prefer it:

```
cLuxProp@ pProp = Map_GetProp("MyProp");

if(pProp is null)
	return;
```

A typed lookup documents the expected type, performs the relevant filtering or conversion in one place, and avoids retrieving an unrelated object only to reject it afterward.

## HPL3 typed conversion helpers
HPL3 provides helper functions for several common engine-class conversions. Examples include:

| Source handle | Target handle | Helper |
| --- | --- | --- |
| `iLuxEntity@` | `cLuxProp@` | `cLux_ToProp` |
| `iLuxEntity@` | `cLuxArea@` | `cLux_ToArea` |
| `iLuxEntity@` | `cLuxAgent@` | `cLux_ToAgent` |
| `iLuxEntity@` | `cLuxCritter@` | `cLux_ToCritter` |
| `iPhysicsJoint@` | `iPhysicsJointHinge@` | `cPhysics_ToJointHinge` |
| `iPhysicsJoint@` | `iPhysicsJointSlider@` | `cPhysics_ToJointSlider` |
| `iPhysicsJoint@` | `iPhysicsJointBall@` | `cPhysics_ToJointBall` |

These helpers return a compatible typed handle or `null`:

```
iPhysicsJoint@ pJoint = mBaseObj.GetJoint(0);
iPhysicsJointHinge@ pHinge = cPhysics_ToJointHinge(pJoint);

if(pHinge is null)
{
	cLux_AddDebugMessage("Expected a hinge joint");
	return;
}

float fMaxAngle = pHinge.GetMaxAngle();
```

Prefer the HPL3 conversion helper when one exists. It makes the intended engine relationship explicit and may perform engine-specific checks in addition to the AngelScript type conversion.

:::tip[Tip]
Retrieve or convert once, store the typed result in a local handle, check it, and then use it. Avoid performing the same cast repeatedly.
:::

## Casting user modules and interfaces
User modules are commonly retrieved through a generic module interface and cast to the interface implemented by the specific module:

```
iScrUserModule_Interface@ pModule =
	cLux_GetUserModuleFromID(eModuleType_DescriptionHandler);

iScrDescriptionHandler_Interface@ pDescription =
	cast<iScrDescriptionHandler_Interface>(pModule);

if(pDescription is null)
{
	cLux_AddDebugMessage("DescriptionHandler module is unavailable");
	return;
}
```

The requested interface must actually be implemented by the module object. A cast cannot add an interface or functionality that the underlying object does not have.

When many scripts need the same module operation, place the retrieval, cast, and validation inside a helper function rather than repeating it in every map script.

## Value casts and constructors
The syntax `Type(expression)` is also used to construct value objects:

```
cVector2f vSize = cVector2f(320, 200);
cColor color = cColor(1, 0.5f, 0.25f, 1);
```

For primitive and enum types, this syntax is normally described as an explicit cast. For class types, it may instead call:

- a constructor accepting the source type;
- a registered conversion constructor;
- an `opConv` or `opImplConv` conversion operator; or
- another conversion behavior supplied by HPL3.

The result is a new value or object instance rather than another handle to the original object.

Do not confuse this with `cast<Type>(handle)`, which performs a reference cast and returns a handle to the same compatible object.

## Casts do not change the object
An object-handle cast changes only the type through which the script views the object:

```
iWidget@ pWidget = mpGUI.GetWidgetFromName("ConfirmButton");
cWidgetButton@ pButton = cast<cWidgetButton>(pWidget);

if(pButton !is null && pWidget is pButton)
{
	// Both handles refer to the same widget instance.
}
```

The cast:

- does not rename or replace the object;
- does not duplicate it;
- does not change its actual runtime class;
- does not extend its lifetime beyond the normal handle and HPL3 ownership rules; and
- does not make an incompatible object compatible.

## Common mistakes
| Mistake | Correct approach |
| --- | --- |
| Expecting integer division to produce a fraction. | Cast an operand to `float` before division. |
| Using `int(fValue)` when rounding is intended. | Use `cMath_Round`, `cMath_RoundToInt`, or other deliberate rounding logic. |
| Casting a negative value to `uint` without validation. | Check the range before converting signedness. |
| Assuming an integer-to-enum cast validates the value. | Check the enum's valid range and include a `default` case. |
| Accessing a downcast handle immediately. | Store the result and check it with `is null`. |
| Assuming a cast creates a new object. | A reference cast returns another handle to the same object. |
| Casting a broad entity lookup when a typed helper already exists. | Prefer functions such as `Map_GetProp` or `cLux_ToProp`. |
| Repeating the same cast several times. | Cast once, validate once, and reuse the typed local handle. |
| Using a cast to force unrelated types together. | Change the design or use a common base class/interface implemented by the actual object. |

## See Also
- [Object Handles](/scripting/object-handles/)
- [Object Instances vs Object Handles](/scripting/object-instances-vs-object-handles/)
- [Working with Classes](/scripting/working-with-classes/)
- [Variables and Types - AngelScript](/scripting/angelscript/chapter-3-variables-and-types/)
- [Operators and Expressions - AngelScript](/scripting/angelscript/chapter-4-operators-and-expressions/)
- [Classes - AngelScript](/scripting/angelscript/chapter-8-classes/)

HPL3/Scripting/Scripting Guide/Object Instances vs Object Handles|Object Instances vs Object Handles|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting Guide/Conclusion - Advanced|Conclusion - Advanced

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Type Casting](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Type_Casting)
- Revision: `7046`
- Source update: `2026-07-30T08:21:01Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

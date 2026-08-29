---
title: Object Handles
description: "Most HPL3 objects are retrieved from an API or helper function rather than constructed directly. The function's return type shows whether it returns a handle. For example, MapGetEntity returns iLuxEntity@:"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Object_Handles"
sourceRevision: 7044
sourceUpdated: "2026-07-30T08:01:48Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

## Retrieving an object
Most HPL3 objects are retrieved from an API or helper function rather than constructed directly. The function's return type shows whether it returns a handle. For example, `Map_GetEntity` returns `iLuxEntity@`:

```
void MoveEntity()
{
	iLuxEntity@ pEntity = Map_GetEntity("MyEntity");

	if(pEntity is null)
	{
		cLux_AddDebugMessage("Could not find MyEntity");
		return;
	}

	pEntity.SetPosition(cVector3f(55, 5, 25));
}
```

The compiler can infer that the returned object should be assigned to the handle, so the extra handle symbol is not required during initialization.

Once a handle refers to an object, its members are accessed with the normal member access operator (`.`). AngelScript automatically accesses the object to which the handle refers:

```
tString sName = pEntity.GetName();
cVector3f vPosition = pEntity.GetPosition();
```

## Null handles
The special value `null` means that a handle does not refer to an object. A handle can be null because:

- it has not been assigned yet;
- a lookup function did not find a matching object;
- a cast failed;
- an HPL3-owned object was destroyed or became unavailable; or
- the handle was deliberately cleared.

Use the identity operators `is` and `!is` when checking handles:

```
if(pEntity is null)
{
	// The handle is empty.
}

if(pEntity !is null)
{
	// The handle currently refers to an object.
}
```

:::caution[Caution]
Do not access members through a null handle. Always check the result of a lookup when failure is possible. A missing map object, an incorrect name, or an incompatible cast can otherwise cause a script warning or runtime error.
:::

## Handle assignment
More than one handle can refer to the same object. Changing the object through either handle changes that same underlying object:

```
iLuxEntity@ pFirst = Map_GetEntity("MyEntity");
iLuxEntity@ pSecond;

@pSecond = @pFirst;

if(pSecond !is null)
	pSecond.SetActive(false);
```

The `@` placed before an expression means "use the handle itself." It makes it explicit that `pSecond` should be rebound to the same object as `pFirst`.

The compiler can infer handle assignment in many contexts:

```
iLuxEntity@ pEntity = Map_GetEntity("MyEntity");
```

For later reassignment, using the explicit form makes the intention clear:

```
@pEntity = Map_GetEntity("OtherEntity");
@pEntity = null;
```

This distinction matters because an ordinary `=` expression can mean "assign to the referenced object" for types that implement an assignment operator, while `@=` always rebinds the handle.

## Comparing handles
Use `is` and `!is` to test whether two handles refer to the exact same object:

```
iLuxEntity@ pFirst = Map_GetEntity("FirstEntity");
iLuxEntity@ pSecond = Map_GetEntity("SecondEntity");

if(pFirst is pSecond)
{
	// Both handles refer to the same object.
}
```

The operators `==` and `!=` may perform a value comparison defined by the object's class. They should not be used when the intention is to compare object identity.

## Handles in functions
Handles can be used as function parameters and return values:

```
void MoveTo(iLuxEntity@ apEntity, const cVector3f &in avPosition)
{
	if(apEntity is null)
		return;

	apEntity.SetPosition(avPosition);
}

iLuxEntity@ FindEntity(const tString &in asName)
{
	iLuxEntity@ pEntity = Map_GetEntity(asName);

	if(pEntity is null)
		return null;

	return pEntity;
}
```

A handle parameter gives the function access to the same underlying object. The function can therefore call methods which change that object.

The handle itself is passed by value. Rebinding the parameter to another object does not rebind the caller's handle. Passing the handle variable by reference is only required when the function must change which object the caller's handle refers to.

## Handles, inheritance, and casting
A handle to a base class or interface can refer to a compatible derived object. HPL3 uses this frequently; for example, `Map_GetEntity` returns the base type `iLuxEntity@`, while the actual object may be a prop, area, agent, or another entity type.

When functionality from a more specific type is needed, cast the handle and check the result:

```
iLuxEntity@ pEntity = Map_GetEntity("MyProp");
cLuxProp@ pProp = cast<cLuxProp>(pEntity);

if(pProp is null)
{
	cLux_AddDebugMessage("MyProp is not a compatible prop");
	return;
}

// Use cLuxProp-specific methods here.
```

An incompatible cast returns a null handle. See [Type Casting](/scripting/type-casting/) for more information.

## Handles in arrays
An array may store object handles:

```
array<iLuxEntity@> vEntities;
Map_GetEntityArray("Lamp_*", vEntities);

for(uint i = 0; i < vEntities.length(); ++i)
{
	iLuxEntity@ pEntity = vEntities[i];

	if(pEntity !is null)
		pEntity.SetActive(false);
}
```

Each element in `array<iLuxEntity@>` is a handle to an entity. Copying one of its elements creates another handle to the same entity; it does not copy the entity.

Do not confuse an *array of handles* with a *handle to an array*:

```
array<iLuxEntity@> vEntities; // An array whose elements are entity handles.
array<tString>@ pNames;       // A handle which can refer to an array object.
```

A handle to an array can be useful when several variables should operate on the same array rather than on separate copies.

## Object lifetime in HPL3
For script-declared reference types, AngelScript keeps track of handles to an object. The object can remain alive while a valid handle still refers to it, and releasing the final handle allows it to be destroyed.

HPL3 also exposes objects owned by the engine, such as entities, physics bodies, lights, particle systems, textures, GUI objects, and world objects. Their lifetime is controlled by the relevant HPL3 subsystem. A script handle to one of these objects must not be assumed to keep it alive. It may become invalid when, for example:

- the object is destroyed;
- the map or entity data is reloaded;
- the player leaves the map;
- a temporary particle system or sound removes itself; or
- a resource is explicitly destroyed.

Use engine handles as short-lived access variables, and reacquire objects when their lifetime may have changed.

When explicitly destroying a resource, clear stored handles to it:

```
if(pTexture !is null)
{
	cResources_DestroyTexture(pTexture);
	@pTexture = null;
}
```

:::caution[Caution]
A non-null check proves only that the handle currently contains a reference. It is not a permanent guarantee that an HPL3-owned object will remain valid after the engine destroys or reloads it.
:::

## Persistent references and `tID`
Do not rely on a raw handle to an HPL3-owned map or world object as persistent saved state. The shipped game scripts normally store the object's `tID`, then retrieve a temporary handle when the object is needed:

```
class cTargetData
{
	tID mTargetID = tID_Invalid;

	void SetTarget(iLuxEntity@ apEntity)
	{
		mTargetID = apEntity is null ? tID_Invalid : apEntity.GetID();
	}

	iLuxEntity@ GetTarget()
	{
		if(mTargetID == tID_Invalid)
			return null;

		return cLux_ID_Entity(mTargetID);
	}

	void Update()
	{
		iLuxEntity@ pTarget = GetTarget();

		if(pTarget is null)
		{
			mTargetID = tID_Invalid;
			return;
		}

		// Use pTarget only after validating it.
	}
}
```

The typed `cLux_ID_*` functions return null if the ID cannot be resolved as the requested type. For example, `cLux_ID_Entity`, `cLux_ID_Body`, `cLux_ID_Light`, and `cLux_ID_Prop` each return a corresponding object handle.

Raw engine handles stored as class fields are generally transient. In classes which participate in HPL3's save system, mark such fields `[nosave]` and reconstruct them when required:

```
[nosave] iPhysicsBody@ mpBody = null;
tID mBodyID = tID_Invalid;
```

:::tip[Tip]
A useful rule is: use a local object handle while working with an object now; store a `tID` when the reference must survive over time or through save/load.
:::

## Common mistakes
| Mistake | Correct approach |
| --- | --- |
| Calling a method immediately after a lookup which may fail. | Store the returned handle and check it with `is null`. |
| Using `== null` or `!= null`. | Use `is null` or `!is null`. |
| Expecting a second handle to contain a copy of the object. | Both handles refer to the same object; create a new instance if an independent object is required. |
| Using an ordinary assignment when the intention is to rebind a handle. | Use explicit handle assignment, such as `@pTarget = @pOther;`. |
| Keeping a raw handle to an engine-owned object as saved or long-lived state. | Store its `tID`, resolve it when needed, and validate the returned handle. |
| Assuming a successful base-to-derived cast. | Check the resulting handle for `null`. |
| Confusing `array<Type@>` with `array<Type>@`. | The first is an array of handles; the second is a handle to an array. |

## See Also
- [Object Instances vs Object Handles](/scripting/object-instances-vs-object-handles/)
- [Type Casting](/scripting/type-casting/)
- [ID Handles](/scripting/id-handles/)
- [Classes - AngelScript](/scripting/angelscript/chapter-8-classes/)

HPL3/Scripting/Scripting Guide/Working with Classes|Working with Classes|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting Guide/Object Instances vs Object Handles|Object Instances vs Object Handles

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Object Handles](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Object_Handles)
- Revision: `7044`
- Source update: `2026-07-30T08:01:48Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

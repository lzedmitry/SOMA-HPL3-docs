---
title: Object Instances vs Object Handles
description: "For an instantiable object type, a declaration without @ creates an object variable:"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Object_Instances_vs_Object_Handles"
sourceRevision: 7045
sourceUpdated: "2026-07-30T08:08:44Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

## Object variables
For an instantiable object type, a declaration without `@` creates an object variable:

```
class cCounter
{
	int mlValue;
}

void Example()
{
	cCounter counter;
	counter.mlValue = 10;
}
```

The `counter` variable owns an instance of `cCounter`. It is constructed when the declaration is reached and destroyed when its lifetime ends, unless a handle keeps a reference to it.

Unlike a handle, an initialized object variable is not optional and cannot be set to `null`. Its identity does not change during its lifetime. Assigning another object to it copies data into the existing instance:

```
cCounter first;
first.mlValue = 10;

cCounter second;
second = first;

second.mlValue = 20;

// first.mlValue is still 10.
// second.mlValue is 20.
```

For script-declared classes, AngelScript automatically supplies an assignment operator which copies each member unless the class defines its own `opAssign`.

## Object handles
A declaration with `@` creates a handle:

```
cCounter@ pCounter;
```

This does not create a `cCounter` instance. The handle is initially `null` and must be made to refer to an existing or newly created object:

```
cCounter counter;
cCounter@ pCounter = @counter;

pCounter.mlValue = 30;

// counter.mlValue is now 30 because pCounter refers to counter.
```

Several handles may refer to the same instance:

```
cCounter counter;

cCounter@ pFirst = @counter;
cCounter@ pSecond = @counter;

pFirst.mlValue = 50;

// pSecond.mlValue and counter.mlValue are also 50.
```

The handles are separate variables, but the object behind them is shared.

## Value assignment versus handle assignment
The assignment operator `=` normally operates on object values. For script classes, it copies the source instance's members into the destination instance:

```
second = first;
```

The handle assignment operator `@=` changes which object a handle refers to:

```
@pCurrent = @first;
@pCurrent = @second;
@pCurrent = null;
```

Rebinding `pCurrent` does not copy, modify, or destroy `first` or `second`. It only changes the reference stored in `pCurrent`.

AngelScript can infer handle assignment in many declarations and function calls:

```
iLuxEntity@ pEntity = Map_GetEntity("MyEntity");
```

When reassigning an existing handle, writing the leading `@` explicitly makes the intended operation unambiguous.

## Complete comparison
| Property | Object variable | Object handle |
| --- | --- | --- |
| Example declaration | `cCounter counter;` | `cCounter@ pCounter;` |
| Creates an instance | Yes, for an instantiable type. | No. |
| Default state | A constructed object. | `null`. |
| Assignment | Copies or assigns object data using `=`. | Rebinds the reference using `@=`. |
| Can be null | No, after successful construction. | Yes. |
| Can alias another variable's instance | No. | Yes. |
| Member access | `counter.Method()` | `pCounter.Method()` |
| Identity comparison | Take handles to the objects when identity must be compared. | Use `is` and `!is`. |
| Typical HPL3 use | Independent script data and value-like utility objects. | Entities, bodies, lights, resources, GUI objects, polymorphism, and optional references. |

## Value types and reference types
AngelScript distinguishes between **value types** and **reference types**.

### Value types
Value types directly contain their data. Assigning a value type creates an independent copy. Primitive types such as `int`, `float`, and `bool` are value types and cannot have object handles.

HPL3 also registers many utility classes as value-like types. Vectors, colors, matrices, and IDs are normally passed or stored as values:

```
cVector3f firstPosition = cVector3f(1, 2, 3);
cVector3f secondPosition = firstPosition;

secondPosition.x = 10;

// firstPosition.x is still 1.
```

Whether an application-registered object type supports handles is decided by HPL3. Do not assume that `@` can be used with every class shown in the scripting API.

### Reference types
Reference types are created separately in memory and may be accessed through handles. All script-declared classes are reference types. Many HPL3 engine classes are also exposed as reference types.

Engine objects are usually retrieved as handles:

```
iLuxEntity@ pEntity = Map_GetEntity("MyEntity");
iPhysicsBody@ pBody;

if(pEntity !is null)
	@pBody = pEntity.GetMainBody();
```

Classes such as `iLuxEntity` represent engine-owned objects. They are normally obtained from HPL3 rather than instantiated directly in a map script.

:::note[Note]
Reference type does not mean that every variable is automatically a nullable handle. A script-class object variable declared without `@` still creates and owns an instance; adding `@` creates a separately rebindable, nullable handle.
:::

## Copying script-class instances
The automatically generated assignment operator for a script class copies each member:

```
class cSettings
{
	float mfVolume;
	bool mbEnabled;
}

cSettings original;
original.mfVolume = 0.5f;
original.mbEnabled = true;

cSettings copy;
copy = original;

copy.mfVolume = 1.0f;

// original.mfVolume is still 0.5f.
```

A class may implement `opAssign` to define different assignment behavior. HPL3 application types may also provide their own assignment operators, so the exact meaning of value assignment ultimately belongs to the type.

### Shallow copies of handle members
Copying an object does not necessarily duplicate every object to which its members refer. If a class contains a handle, the generated assignment operator copies that handle:

```
class cTarget
{
	int mlValue;
}

class cContainer
{
	cTarget@ mpTarget;
}

cTarget target;

cContainer first;
@first.mpTarget = @target;

cContainer second;
second = first;

second.mpTarget.mlValue = 25;

// first.mpTarget and second.mpTarget still refer to the same target.
// target.mlValue is now 25.
```

This is called a **shallow copy**. The `cContainer` data was copied, but the target object was not duplicated. A true independent or **deep copy** must be implemented explicitly by constructing new referenced objects and copying their contents.

## Function parameters
The same distinction applies when passing objects to functions.

Passing an object by value gives the function a copy:

```
void ChangeCopy(cCounter counter)
{
	counter.mlValue = 100;
}
```

Passing a handle gives the function access to the same instance:

```
void ChangeOriginal(cCounter@ pCounter)
{
	if(pCounter !is null)
		pCounter.mlValue = 100;
}
```

Passing a value object by constant reference avoids a copy while preventing assignment through that parameter:

```
float GetDistanceFromOrigin(const cVector3f &in avPosition)
{
	return avPosition.Length();
}
```

HPL3 functions commonly use `const Type &in` for strings, vectors, colors, matrices, and other value objects which only need to be read.

:::note[Note]
A handle parameter is itself passed by value. The called function can modify the shared object, but rebinding its local parameter does not rebind the caller's handle.
:::

## Instances and handles in arrays
An array declaration also determines whether it stores instances or handles:

```
array<cCounter> counters;   // Stores counter instances.
array<cCounter@> targets;   // Stores handles to counter instances.
```

An array of instances owns independent elements. Reading an element into another object variable copies it:

```
cCounter copy;
copy = counters[0];

copy.mlValue = 5;

// counters[0].mlValue was not changed.
```

To edit the actual instance inside the array through an alias, take a handle to that element:

```
cCounter@ pCounter = @counters[0];
pCounter.mlValue = 5;

// counters[0].mlValue is now 5.
```

This pattern is used by the shipped HPL3 scripts when updating class instances stored in arrays:

```
for(uint i = 0; i < mvShakes.size(); ++i)
{
	cLuxEffect_ShakeInstance@ pShake = @mvShakes[i];
	pShake.mfTime -= afTimeStep;
}
```

An array of handles behaves differently. Its elements may be `null`, and several elements can refer to the same object:

```
array<iLuxEntity@> vEntities;
vEntities.push_back(Map_GetEntity("EntityA"));
vEntities.push_back(Map_GetEntity("EntityA"));

// Both elements may refer to the same map entity.
```

## Choosing between an instance and a handle
Use an object instance when:

- the variable should own independent data;
- copying the object's state is the desired behavior;
- the value must always exist rather than being optional; or
- working with an HPL3 value type such as a vector, color, matrix, or ID.

Use an object handle when:

- referring to an object which already exists;
- several parts of the script must share the same object;
- `null` is a useful "no object" state;
- working with HPL3-owned entities, physics objects, resources, or GUI objects;
- using a base class or interface to refer to different derived types; or
- modifying an existing instance stored inside a container.

For a long-lived reference to an HPL3-owned world object, store its `tID` and resolve a temporary handle when needed. See [Object Handles](/scripting/object-handles/#persistent-references-and-tid) and [ID Handles](/scripting/id-handles/).

## Common mistakes
| Mistake | Result | Correct approach |
| --- | --- | --- |
| Expecting `second = first` to make `second` an alias. | The destination receives copied object data. | Declare a handle and use `@second = @first`. |
| Expecting a handle assignment to copy the object. | Both handles refer to one shared instance. | Create another instance and use value assignment when an independent copy is needed. |
| Changing a copied array element and expecting the array to change. | Only the local copy changes. | Take a handle to the element with `@array[index]`, or assign the changed value back. |
| Assuming an object copy is always deep. | Handle members in the copy still refer to the original referenced objects. | Implement explicit deep-copy behavior when required. |
| Declaring an engine interface as a local instance. | The type may be abstract, non-instantiable, or engine-owned. | Retrieve the object through an HPL3 function and store the returned handle. |
| Using a handle where independent state is required. | Changes made through any alias affect the shared object. | Store an instance or create an explicit copy. |
| Keeping a raw engine-object handle as persistent saved state. | The referenced engine object may be destroyed or reconstructed. | Store a `tID`, resolve it when needed, and validate the returned handle. |

## See Also
- [Object Handles](/scripting/object-handles/)
- [Type Casting](/scripting/type-casting/)
- [ID Handles](/scripting/id-handles/)
- [Classes - AngelScript](/scripting/angelscript/chapter-8-classes/)
- [Miscellaneous AngelScript Features](/scripting/angelscript/chapter-9-miscellaneous-angelscript-features/)

HPL3/Scripting/Scripting Guide/Object Handles|Object Handles|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting Guide/Type Casting|Type Casting

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Object Instances vs Object Handles](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Object_Instances_vs_Object_Handles)
- Revision: `7045`
- Source update: `2026-07-30T08:08:44Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

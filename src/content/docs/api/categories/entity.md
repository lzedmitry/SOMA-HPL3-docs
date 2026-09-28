---
title: Entity
description: "Have some helpful descriptions to add to this class? Edit this page and add your insight to the Wiki!"
category: api
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Entity"
sourceRevision: 5007
sourceUpdated: "2020-08-24T20:40:43Z"
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
| `bool` | [`Entity_AddCollideCallback`](#entity-addcollidecallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asParentName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asChildName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asFunction) | Add a callback for when entities (objects, areas etc) collide and/or collides with the player |
| `void` | [`Entity_AddForce`](#entity-addforce)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avForce, bool abLocalSpace, bool abOnlyMainBody) | Adds force to the entity |
| `void` | [`Entity_AddForceFromEntity`](#entity-addforcefromentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asForceEntityName, float afForce, bool abOnlyMainBody) | Adds force to the entity away from another entity |
| `void` | [`Entity_AddImpulse`](#entity-addimpulse)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avImpulse, bool abLocalSpace, bool abOnlyMainBody) | Adds an impulse to the entity |
| `void` | [`Entity_AddImpulseFromEntity`](#entity-addimpulsefromentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asImpulseEntityName, float afImpulse, bool abOnlyMainBody) | Adds an impulse to the entity away from another entity |
| `void` | [`Entity_AddTorque`](#entity-addtorque)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avTorque, bool abLocalSpace, bool abOnlyMainBody) | Adds torque to an entity to provide some angular velocity |
| `bool` | [`Entity_AttachToEntity`](#entity-attachtoentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asParentName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asParentBodyName, bool abUseRotation, bool abSnapToParent = false, bool abLocked = false) | Attaches the entity to another entity |
| `bool` | [`Entity_AttachToSocket`](#entity-attachtosocket)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asParentName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asParentSocketName, bool abUseRotation, bool abSnapToParent = true) | Attaches the entity to another entity |
| `void` | [`Entity_CallEntityInteract`](#entity-callentityinteract)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asBodyName = "", const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avFocusBodyOffset = cVector3f_Zero, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asData = "") | Calls OnInteract on the specified entity |
| `void` | [`Entity_Connect`](#entity-connect)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asMainEntity, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asConnectEntity, bool abInvertStateSent, int alStatesUsed) | Creates a connection between two entities |
| `iLuxEntity` | [`Entity_CreateAtEntity`](#entity-createatentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asNewEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityFile, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asTargetEntityName, bool abFullGameSave) | Creates an entity at another entity |
| `iLuxEntity` | [`Entity_CreateAtEntityExt`](#entity-createatentityext)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asNewEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityFile, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asTargetEntityName, bool abFullGameSave, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avScale, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avOffsetPosition, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avOffsetRotation, bool abLocalOffset) | Creates an entity at another entity with extra options |
| `void` | [`Entity_Destroy`](#entity-destroy)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Destroys an entity of a given name |
| `bool` | [`Entity_EntityIsInFront`](#entity-entityisinfront)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asTargetEntity, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asForwardEntity) | Returns true if the specified entity is in front of the other entity |
| `bool` | [`Entity_Exists`](#entity-exists)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Check if an entity exists in the level |
| `bool` | [`Entity_Exists`](#entity-exists)([tID](https://wiki.frictionalgames.com/page/../../tID) aID) | Check if an entity exists in the level |
| `void` | [`Entity_FadeEffectBaseColor`](#entity-fadeeffectbasecolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor, float afTime) | Fades the base color of the effects |
| `void` | [`Entity_FadeProcAnimationSpeed`](#entity-fadeprocanimationspeed)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimationName, float afSpeed, float afTime) | Fade the speed of a proc animation |
| `bool` | [`Entity_GetAutoSleep`](#entity-getautosleep)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Get if an entity automatically falls asleep when it isnt active |
| `cVector3f` | [`Entity_GetBodyOffset`](#entity-getbodyoffset)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName) | Returns the offset from centre specified in the |
| `bool` | [`Entity_GetCollide`](#entity-getcollide)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityA, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityB) | Checks for collision between two specific entities |
| `cVector3f` | [`Entity_GetDeltaToEntity`](#entity-getdeltatoentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityA, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityB) | Gets the direction and distance between two entities |
| `bool` | [`Entity_GetVarBool`](#entity-getvarbool)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity boolean variable |
| `cColor` | [`Entity_GetVarColor`](#entity-getvarcolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity color variable |
| `float` | [`Entity_GetVarFloat`](#entity-getvarfloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity float variable |
| `int` | [`Entity_GetVarInt`](#entity-getvarint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity integer variable |
| `tString` | [`Entity_GetVarString`](#entity-getvarstring)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity string variable |
| `cVector2f` | [`Entity_GetVarVector2f`](#entity-getvarvector2f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity vector2f variable |
| `cVector3f` | [`Entity_GetVarVector3f`](#entity-getvarvector3f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName) | Get value of an entity vector3f variable |
| `void` | [`Entity_IncVarFloat`](#entity-incvarfloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, float afX) | Add a value to the current value of an entity float variable |
| `void` | [`Entity_IncVarInt`](#entity-incvarint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, int alX) | Add a value to the current value of an entity integer variable |
| `void` | [`Entity_IncVarVector2f`](#entity-incvarvector2f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avX) | Add a value to the current value of an entity vector2f variable |
| `void` | [`Entity_IncVarVector3f`](#entity-incvarvector3f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avX) | Add a value to the current value of an entity vector3f variable |
| `bool` | [`Entity_IsActive`](#entity-isactive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Get if an entity is active (visible and functioning) or not |
| `bool` | [`Entity_IsInPlayerFOV`](#entity-isinplayerfov)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntity) | Returns true if the object is within the player's field of view |
| `bool` | [`Entity_IsInteractedWith`](#entity-isinteractedwith)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Checks if the entity is being interacted with |
| `bool` | [`Entity_IsOccluder`](#entity-isoccluder)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Get if an entity is an occluder |
| `bool` | [`Entity_IsSleeping`](#entity-issleeping)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Check if an entity is asleep |
| `void` | [`Entity_PlaceAtEntity`](#entity-placeatentity)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asTargetEntity, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avOffset = cVector3f_Zero, bool abAlignRotation = false, bool abUseEntFileCenter = false) | Places the specified entity at another entity |
| `void` | [`Entity_PlayAnimation`](#entity-playanimation)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimation, float afFadeTime = 0.1f, bool abLoop = false, bool abPlayTransition = true, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCallback = "") | Plays an animation on the entity |
| `bool` | [`Entity_PlayerIsInFront`](#entity-playerisinfront)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Returns true if the player is in front of the specified entity |
| `void` | [`Entity_PlayProcAnimation`](#entity-playprocanimation)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimation, float afLength, bool abLoop = false, float afAmountFadeTime = 0.1, float afSpeedFadeTime = -1.0f) | Plays a procedural animation on the entity |
| `void` | [`Entity_Preload`](#entity-preload)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityFile) | Preloads an entity |
| `void` | [`Entity_RemoveAllConnections`](#entity-removeallconnections)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asMainEntity) | Removes all connections on an entity |
| `bool` | [`Entity_RemoveCollideCallback`](#entity-removecollidecallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asParentName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asChildName) | Remove a callback for when entities (objects, areas etc) collide and/or collide with the player |
| `void` | [`Entity_RemoveConnection`](#entity-removeconnection)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asMainEntity) | Removes a specific connection on an entity |
| `bool` | [`Entity_RemoveEntityAttachment`](#entity-removeentityattachment)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Removes an attachment to another entity if the entity(ies) has one |
| `void` | [`Entity_SetActive`](#entity-setactive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abActive) | Set if entity is active (visible and functioning) or not |
| `void` | [`Entity_SetAnimationMessageEventCallback`](#entity-setanimationmessageeventcallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCallbackFunc, bool abAutoRemove) | Sets a callback for the message events in the currently playing animation |
| `void` | [`Entity_SetAnimationPaused`](#entity-setanimationpaused)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimationName, bool abPaused = true) | Pause or unpause an animation on the specified entity |
| `void` | [`Entity_SetAnimationRelativeTimePosition`](#entity-setanimationrelativetimeposition)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimationName, float afTimePos) | Sets the relative time position of a specific animation |
| `void` | [`Entity_SetAutoSleep`](#entity-setautosleep)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abX) | Sets if the entity should sleep automatically when it need no updating |
| `void` | [`Entity_SetCollide`](#entity-setcollide)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, bool abActive) | Turn off or on collision for all the bodies in the given entity |
| `void` | [`Entity_SetCollideCharacter`](#entity-setcollidecharacter)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, bool abActive) | Turn off or on character collision for all the bodies in the given entity |
| `void` | [`Entity_SetColorMul`](#entity-setcolormul)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor) | Set the color mul of the entity |
| `void` | [`Entity_SetConnectionStateChangeCallback`](#entity-setconnectionstatechangecallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCallback) | Sets the callback for when the connection state changes on an entity |
| `void` | [`Entity_SetEffectBaseColor`](#entity-seteffectbasecolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aColor) | Sets the base color of the effects |
| `void` | [`Entity_SetEffectsActive`](#entity-seteffectsactive)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, bool abActive, bool abFadeAndPlaySounds) | Activates or deactivates the effects on a entity |
| `void` | [`Entity_SetInteractionDisabled`](#entity-setinteractiondisabled)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, bool abX) | Sets if the player can interact with an entity or not |
| `void` | [`Entity_SetIsOccluder`](#entity-setisoccluder)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName, bool abOccluder) | Set if entity is an occluder |
| `void` | [`Entity_SetMaxInteractionDistance`](#entity-setmaxinteractiondistance)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, float afDistance) | Change the max interaction distance of an entity from the default/entity configured distance |
| `void` | [`Entity_SetPlayerInteractCallback`](#entity-setplayerinteractcallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCallback, bool abRemoveWhenInteracted) | Sets the callback for when the player interacts with a specific entity |
| `void` | [`Entity_SetPlayerLookAtCallback`](#entity-setplayerlookatcallback)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asCallback, bool abRemoveWhenLookedAt = true, bool abCheckCenterOfScreen = true, bool abCheckRayIntersection = true, float afMaxDistance = -1, float afCallbackDelay = 0) | Sets the callback for when the player looks at or turns away from a specific entity |
| `void` | [`Entity_SetProcAnimationPaused`](#entity-setprocanimationpaused)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimationName, bool abPaused = true) | Pause or unpause a procedural animation on the specified entity |
| `void` | [`Entity_SetProcAnimationSpeed`](#entity-setprocanimationspeed)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimationName, float afSpeed) | Sets the speed of a proc animation |
| `void` | [`Entity_SetReflectionVisibility`](#entity-setreflectionvisibility)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, bool abVisibleInReflection, bool abVisibleInWorld) | Sets whether the entity is drawn in reflections or not, and the real world or not |
| `void` | [`Entity_SetVarBool`](#entity-setvarbool)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, bool abX) | Sets the value of an entity boolean variable |
| `void` | [`Entity_SetVarColor`](#entity-setvarcolor)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, const [cColor](https://wiki.frictionalgames.com/page/../../cColor) &in aX) | Sets the value of an entity color variable |
| `void` | [`Entity_SetVarFloat`](#entity-setvarfloat)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, float afX) | Sets the value of an entity variable |
| `void` | [`Entity_SetVarInt`](#entity-setvarint)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, int alX) | Sets the value of an entity integer variable |
| `void` | [`Entity_SetVarString`](#entity-setvarstring)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asX) | Sets the value of an entity string variable |
| `void` | [`Entity_SetVarVector2f`](#entity-setvarvector2f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, const [cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f) &in avX) | Sets the value of an entity vector2f variable |
| `void` | [`Entity_SetVarVector3f`](#entity-setvarvector3f)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asVarName, const [cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f) &in avX) | Sets the value of an entity vector3f variable |
| `void` | [`Entity_Sleep`](#entity-sleep)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Forces the entity to sleep (disabling Update/PostUpdate) |
| `void` | [`Entity_StopAnimation`](#entity-stopanimation)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName) | Stops any currently playing animation on the specified entity |
| `void` | [`Entity_StopProcAnimation`](#entity-stopprocanimation)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asEntityName, const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asAnimation, float afFadeTime = 0.1f) | Stops a procedural animation on the specified entity |
| `void` | [`Entity_WakeUp`](#entity-wakeup)(const [tString](https://wiki.frictionalgames.com/page/../../tString) &in asName) | Forces the entity to wake up (enabling Update/PostUpdate) |

## Function Detail
    1. `Entity_AddCollideCallback`

```cpp
bool Entity_AddCollideCallback(const tString &in asParentName,
                               const tString &in asChildName,
                               const tString &in asFunction)
```

Add a callback for when entities (objects, areas etc) collide and/or collides with the player.  
Collision include "uncolliding" (objects just stopped colliding) as well.  
Wildcard(s) * can be used in names to check for collisions.  
Syntax for callback function: bool FunctionName(const tString &in asParent, const tString &in asChild, int alState).  
- asParent Name of the parent entity in the collision.  
- asChild Name of the child entity in the collision.  
- alState 1 = colliding, -1 = was colliding in previous frame, not anymore.  
Return false = callback is removed, true = callback can trigger again.

| Name | Type | Description |
| --- | --- | --- |
| `asParentName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | always "player" for player collisions, else first entity name. |
| `asChildName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity or second entity to check for collision. |
| `asFunction` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the callback function when something collides/uncollides. |

**Returns:** `bool` — .

    1. `Entity_AddForce`

```cpp
void Entity_AddForce(const tString &in asEntityName,
                     const cVector3f &in avForce,
                     bool abLocalSpace,
                     bool abOnlyMainBody)
```

Adds force to the entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `avForce` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | force to add. |
| `abLocalSpace` | `bool` | true = force is added relative to the rotation of the entity - false = force is added in world space |
| `abOnlyMainBody` | `bool` | true = force is added only to the main body of the entity - false = force is added to all bodies in the entity |

**Returns:** `void`

    1. `Entity_AddForceFromEntity`

```cpp
void Entity_AddForceFromEntity(const tString &in asEntityName,
                               const tString &in asForceEntityName,
                               float afForce,
                               bool abOnlyMainBody)
```

Adds force to the entity away from another entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to add force to. Wildcard(s) * are supported. |
| `asForceEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to push away from. |
| `afForce` | `float` | force magnitude, negative attracts the entity to the force entity. |
| `abOnlyMainBody` | `bool` | true = force is added only to the main body of the entity - false = force is added to all bodies in the entity |

**Returns:** `void`

    1. `Entity_AddImpulse`

```cpp
void Entity_AddImpulse(const tString &in asEntityName,
                       const cVector3f &in avImpulse,
                       bool abLocalSpace,
                       bool abOnlyMainBody)
```

Adds an impulse to the entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `avImpulse` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | impulse to add. |
| `abLocalSpace` | `bool` | true = impulse is added relative to the rotation of the entity - false = impulse is added in world space |
| `abOnlyMainBody` | `bool` | true = impulse is added only to the main body of the entity - false = impulse is added to all bodies in the entity |

**Returns:** `void`

    1. `Entity_AddImpulseFromEntity`

```cpp
void Entity_AddImpulseFromEntity(const tString &in asEntityName,
                                 const tString &in asImpulseEntityName,
                                 float afImpulse,
                                 bool abOnlyMainBody)
```

Adds an impulse to the entity away from another entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to add impulse to. Wildcard(s) * are supported. |
| `asImpulseEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to push away from. |
| `afImpulse` | `float` | impulse magnitude, negative attracts the entity to the impulse entity. |
| `abOnlyMainBody` | `bool` | true = impulse is added only to the main body of the entity - false = impulse is added to all bodies in the entity |

**Returns:** `void`

    1. `Entity_AddTorque`

```cpp
void Entity_AddTorque(const tString &in asEntityName,
                      const cVector3f &in avTorque,
                      bool abLocalSpace,
                      bool abOnlyMainBody)
```

Adds torque to an entity to provide some angular velocity

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to add impulse to. Wildcard(s) * are supported. |
| `avTorque` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | provide a vector3 for the desired direction |
| `abLocalSpace` | `bool` | use local space for the entity |
| `abOnlyMainBody` | `bool` | true = impulse is added only to the main body of the entity - false = impulse is added to all bodies in the entity |

**Returns:** `void`

    1. `Entity_AttachToEntity`

```cpp
bool Entity_AttachToEntity(const tString &in asName,
                           const tString &in asParentName,
                           const tString &in asParentBodyName,
                           bool abUseRotation,
                           bool abSnapToParent = false,
                           bool abLocked = false)
```

Attaches the entity to another entity. If already attached, it will be removed before attaching to new

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to be attached to another, Wildcard(s) * are supported |
| `asParentName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | The entity to attach to. |
| `asParentBodyName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the local (as it is in ent file) of the body. Use  for just using the main body. |
| `abUseRotation` | `bool` | if the attached entity should be rotated along witht the parent. |
| `abSnapToParent` | `bool` | if the attached entity should snap to the center of the body, or if it should use its relative world position as offset |
| `abLocked` | `bool` | if the attached object should be locked to the parent - fixes precision issues |

**Returns:** `bool`

    1. `Entity_AttachToSocket`

```cpp
bool Entity_AttachToSocket(const tString &in asName,
                           const tString &in asParentName,
                           const tString &in asParentSocketName,
                           bool abUseRotation,
                           bool abSnapToParent = true)
```

Attaches the entity to another entity. If already attached, it will be removed before attaching to new

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to be attached to another, Wildcard(s) * are supported |
| `asParentName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | The entity to attach to. |
| `asParentSocketName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the socket setup in the mesh or model editor. this is attached to a bone in the skeleton |
| `abUseRotation` | `bool` | if the attached entity should be rotated along witht the parent. |
| `abSnapToParent` | `bool` | if the attached entity should snap to the center of the socket, or if it should use its relative world position as offset |

**Returns:** `bool`

    1. `Entity_CallEntityInteract`

```cpp
void Entity_CallEntityInteract(const tString &in asName,
                               const tString &in asBodyName = "",
                               const cVector3f &in avFocusBodyOffset = cVector3f_Zero,
                               const tString &in asData = "")
```

Calls OnInteract on the specified entity.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asBodyName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the body to interact with if "" then it's the main body. |
| `avFocusBodyOffset` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | focus point on the body. |
| `asData` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | optional data needed for interaction. |

**Returns:** `void` — true if the position is in front of the entity.

    1. `Entity_Connect`

```cpp
void Entity_Connect(const tString &in asName,
                    const tString &in asMainEntity,
                    const tString &in asConnectEntity,
                    bool abInvertStateSent,
                    int alStatesUsed)
```

Creates a connection between two entities.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the connection. |
| `asMainEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the entity to add the connection to. Wildcard(s) * are supported. |
| `asConnectEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the entity to connect to the main entity. |
| `abInvertStateSent` | `bool` | if the state changes should be sent inverted. |
| `alStatesUsed` | `int` | states sent by main entity, 0 = all states, 1 = only max, -1 = only min. |

**Returns:** `void`

    1. `Entity_CreateAtEntity`

```cpp
iLuxEntity@ Entity_CreateAtEntity(const tString &in asNewEntityName,
                                  const tString &in asEntityFile,
                                  const tString &in asTargetEntityName,
                                  bool abFullGameSave)
```

Creates an entity at another entity.

| Name | Type | Description |
| --- | --- | --- |
| `asNewEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to be created. |
| `asEntityFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the .ent file of the entity to be created. |
| `asTargetEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the target entity. |
| `abFullGameSave` | `bool` | if ALL properties should be saved for the created entity. |

**Returns:** `iLuxEntity@`

    1. `Entity_CreateAtEntityExt`

```cpp
iLuxEntity@ Entity_CreateAtEntityExt(const tString &in asNewEntityName,
                                     const tString &in asEntityFile,
                                     const tString &in asTargetEntityName,
                                     bool abFullGameSave,
                                     const cVector3f &in avScale,
                                     const cVector3f &in avOffsetPosition,
                                     const cVector3f &in avOffsetRotation,
                                     bool abLocalOffset)
```

Creates an entity at another entity with extra options.

| Name | Type | Description |
| --- | --- | --- |
| `asNewEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to be created. |
| `asEntityFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the .ent file of the entity to be created. |
| `asTargetEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the target entity. |
| `abFullGameSave` | `bool` | if ALL properties should be saved for the created entity. |
| `avScale` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | the scale of the created entity, where cVector3f(1, 1, 1) is the default size. |
| `avOffsetPosition` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | an offset from the target object's position. |
| `avOffsetRotation` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | an offset from the target object's rotation. |
| `abLocalOffset` | `bool` | true = offset position and rotation are relative to the target object's rotation, false = offset position and rotation are relative to the world. |

**Returns:** `iLuxEntity@` — new iLuxEntity object.

    1. `Entity_Destroy`

```cpp
void Entity_Destroy(const tString &in asName)
```

Destroys an entity of a given name.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to be destroyed, can contain wildcards to destroy multiple entities. |

**Returns:** `void`

    1. `Entity_EntityIsInFront`

```cpp
bool Entity_EntityIsInFront(const tString &in asTargetEntity,
                            const tString &in asForwardEntity)
```

Returns true if the specified entity is in front of the other entity.  
The function assumes the entity's z-axis points forward. Anything less than 90  
degrees offset from the forward vector counts as "in front".

| Name | Type | Description |
| --- | --- | --- |
| `asTargetEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to check if in front of the other. |
| `asForwardEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of entity which forward vector and position will be checked against. |

**Returns:** `bool` — bool true if the target entity is in front.

    1. `Entity_Exists`

```cpp
bool Entity_Exists(const tString &in asName)
```

Check if an entity exists in the level.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to search for. |

**Returns:** `bool` — if entity exists.

    1. `Entity_Exists`

```cpp
bool Entity_Exists(tID aID)
```

Check if an entity exists in the level.

| Name | Type | Description |
| --- | --- | --- |
| `aID` | `[tID](https://wiki.frictionalgames.com/page/../../tID)` | the id of the entity to search for. |

**Returns:** `bool` — if entity exists.

    1. `Entity_FadeEffectBaseColor`

```cpp
void Entity_FadeEffectBaseColor(const tString &in asEntityName,
                                const cColor &in aColor,
                                float afTime)
```

Fades the base color of the effects

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. Wildcard(s) * are supported. |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | the color all effects will be faded to |
| `afTime` | `float` | time the fade takes. |

**Returns:** `void`

    1. `Entity_FadeProcAnimationSpeed`

```cpp
void Entity_FadeProcAnimationSpeed(const tString &in asEntityName,
                                   const tString &in asAnimationName,
                                   float afSpeed,
                                   float afTime)
```

Fade the speed of a proc animation.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimationName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation. |
| `afSpeed` | `float` | target speed (measured in full loops per second). |
| `afTime` | `float` | time to fade over. |

**Returns:** `void`

    1. `Entity_GetAutoSleep`

```cpp
bool Entity_GetAutoSleep(const tString &in asName)
```

Get if an entity automatically falls asleep when it isnt active

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity. |

**Returns:** `bool` — if sleeping or not.

    1. `Entity_GetBodyOffset`

```cpp
cVector3f Entity_GetBodyOffset(const tString &in asEntityName)
```

Returns the offset from centre specified in the .ent file. Only works for props.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |

**Returns:** `cVector3f` — the offset

    1. `Entity_GetCollide`

```cpp
bool Entity_GetCollide(const tString &in asEntityA,
                       const tString &in asEntityB)
```

Checks for collision between two specific entities. Wildcard(s) * are NOT supported!

| Name | Type | Description |
| --- | --- | --- |
| `asEntityA` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | first entity. |
| `asEntityB` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | second entity. |

**Returns:** `bool`

    1. `Entity_GetDeltaToEntity`

```cpp
cVector3f Entity_GetDeltaToEntity(const tString &in asEntityA,
                                  const tString &in asEntityB)
```

Gets the direction and distance between two entities

| Name | Type | Description |
| --- | --- | --- |
| `asEntityA` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | entity to calculate delta from |
| `asEntityB` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | entity to caluclate delta to |

**Returns:** `cVector3f` — delta between the entities, delta = direction * distance = entity_b_pos - entity_a_pos

    1. `Entity_GetVarBool`

```cpp
bool Entity_GetVarBool(const tString &in asEntityName,
                       const tString &in asVarName)
```

Get value of an entity boolean variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the boolean variable. |

**Returns:** `bool`

    1. `Entity_GetVarColor`

```cpp
cColor Entity_GetVarColor(const tString &in asEntityName,
                          const tString &in asVarName)
```

Get value of an entity color variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the color variable. |

**Returns:** `cColor`

    1. `Entity_GetVarFloat`

```cpp
float Entity_GetVarFloat(const tString &in asEntityName,
                         const tString &in asVarName)
```

Get value of an entity float variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the float variable. |

**Returns:** `float`

    1. `Entity_GetVarInt`

```cpp
int Entity_GetVarInt(const tString &in asEntityName,
                     const tString &in asVarName)
```

Get value of an entity integer variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector3f variable. |

**Returns:** `int`

    1. `Entity_GetVarString`

```cpp
tString Entity_GetVarString(const tString &in asEntityName,
                            const tString &in asVarName)
```

Get value of an entity string variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the string variable. |

**Returns:** `tString`

    1. `Entity_GetVarVector2f`

```cpp
cVector2f Entity_GetVarVector2f(const tString &in asEntityName,
                                const tString &in asVarName)
```

Get value of an entity vector2f variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector2f variable. |

**Returns:** `cVector2f`

    1. `Entity_GetVarVector3f`

```cpp
cVector3f Entity_GetVarVector3f(const tString &in asEntityName,
                                const tString &in asVarName)
```

Get value of an entity vector3f variable.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector3f variable. |

**Returns:** `cVector3f`

    1. `Entity_IncVarFloat`

```cpp
void Entity_IncVarFloat(const tString &in asEntityName,
                        const tString &in asVarName,
                        float afX)
```

Add a value to the current value of an entity float variable. Wildcard(s) * are supported for EntityName.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the float variable. |
| `afX` | `float` | value to be added to variable. |

**Returns:** `void`

    1. `Entity_IncVarInt`

```cpp
void Entity_IncVarInt(const tString &in asEntityName,
                      const tString &in asVarName,
                      int alX)
```

Add a value to the current value of an entity integer variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the integer variable. |
| `alX` | `int` | value to be added to variable. |

**Returns:** `void`

    1. `Entity_IncVarVector2f`

```cpp
void Entity_IncVarVector2f(const tString &in asEntityName,
                           const tString &in asVarName,
                           const cVector2f &in avX)
```

Add a value to the current value of an entity vector2f variable. Wildcard(s) * are supported for EntityName.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector2f variable. |
| `avX` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | value to be added to variable. |

**Returns:** `void`

    1. `Entity_IncVarVector3f`

```cpp
void Entity_IncVarVector3f(const tString &in asEntityName,
                           const tString &in asVarName,
                           const cVector3f &in avX)
```

Add a value to the current value of an entity vector3f variable. Wildcard(s) * are supported for EntityName.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector3f variable. |
| `avX` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | value to be added to variable. |

**Returns:** `void`

    1. `Entity_IsActive`

```cpp
bool Entity_IsActive(const tString &in asName)
```

Get if an entity is active (visible and functioning) or not.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity. |

**Returns:** `bool` — if active or not.

    1. `Entity_IsInPlayerFOV`

```cpp
bool Entity_IsInPlayerFOV(const tString &in asEntity)
```

Returns true if the object is within the player's field of view. This does not take into account line of sight.

| Name | Type | Description |
| --- | --- | --- |
| `asEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to check. |

**Returns:** `bool` — true if the entity is in the player's field of view.

    1. `Entity_IsInteractedWith`

```cpp
bool Entity_IsInteractedWith(const tString &in asName)
```

Checks if the entity is being interacted with.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |

**Returns:** `bool` — if the entity is being interacted with

    1. `Entity_IsOccluder`

```cpp
bool Entity_IsOccluder(const tString &in asName)
```

Get if an entity is an occluder

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity. |

**Returns:** `bool` — if entity is an occluder

    1. `Entity_IsSleeping`

```cpp
bool Entity_IsSleeping(const tString &in asName)
```

Check if an entity is asleep

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity. |

**Returns:** `bool` — if sleeping or not.

    1. `Entity_PlaceAtEntity`

```cpp
void Entity_PlaceAtEntity(const tString &in asEntityName,
                          const tString &in asTargetEntity,
                          const cVector3f &in avOffset = cVector3f_Zero,
                          bool abAlignRotation = false,
                          bool abUseEntFileCenter = false)
```

Places the specified entity at another entity. Optionally aligning its rotation with the target entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asTargetEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | entity to place at. |
| `avOffset` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | world offset from the target entity to place at. |
| `abAlignRotation` | `bool` | if true the entity will be given the same rotation as the target entity. |
| `abUseEntFileCenter` | `bool` | if true the entity's center specified in the ent file will be used for placement (only works for props). |

**Returns:** `void`

    1. `Entity_PlayAnimation`

```cpp
void Entity_PlayAnimation(const tString &in asEntityName,
                          const tString &in asAnimation,
                          float afFadeTime = 0.1f,
                          bool abLoop = false,
                          bool abPlayTransition = true,
                          const tString &in asCallback = "")
```

Plays an animation on the entity  
Syntax for callback function: void Func(const tString &in asEntityName, const tString &in asAnimName)

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimation` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation to play. |
| `afFadeTime` | `float` | time to fade in animation. |
| `abLoop` | `bool` | if the animation should loop. |
| `abPlayTransition` | `bool` | If a transition animation (given such exist) should be be played before. |
| `asCallback` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | (optional) name of callback function. |

**Returns:** `void`

    1. `Entity_PlayerIsInFront`

```cpp
bool Entity_PlayerIsInFront(const tString &in asName)
```

Returns true if the player is in front of the specified entity.  
The function assumes the entity's z-axis points forward. Anything less than 90  
degrees offset from the forward vector counts as "in front".

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity to check if in front of the other. |

**Returns:** `bool` — true if the target entity is in front.

    1. `Entity_PlayProcAnimation`

```cpp
void Entity_PlayProcAnimation(const tString &in asEntityName,
                              const tString &in asAnimation,
                              float afLength,
                              bool abLoop = false,
                              float afAmountFadeTime = 0.1,
                              float afSpeedFadeTime = -1.0f)
```

Plays a procedural animation on the entity

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimation` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation to play. |
| `afLength` | `float` | time it takes to play the animation (can be negative to play it in reverse!) |
| `abLoop` | `bool` | if the animation should loop. |
| `afAmountFadeTime` | `float` | time to fade in animation. |
| `afSpeedFadeTime` | `float` | time to fade in the speed of the animation (use this for looping animations to avoid skipping). |

**Returns:** `void`

    1. `Entity_Preload`

```cpp
void Entity_Preload(const tString &in asEntityFile)
```

Preloads an entity

| Name | Type | Description |
| --- | --- | --- |
| `asEntityFile` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity file to preload |

**Returns:** `void`

    1. `Entity_RemoveAllConnections`

```cpp
void Entity_RemoveAllConnections(const tString &in asMainEntity)
```

Removes all connections on an entity.

| Name | Type | Description |
| --- | --- | --- |
| `asMainEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the entity to remove all connections on. Wildcard(s) * are supported. |

**Returns:** `void`

    1. `Entity_RemoveCollideCallback`

```cpp
bool Entity_RemoveCollideCallback(const tString &in asParentName,
                                  const tString &in asChildName)
```

Remove a callback for when entities (objects, areas etc) collide and/or collide with the player.  
Wildcard(s) * can be used in names.

| Name | Type | Description |
| --- | --- | --- |
| `asParentName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | always "player" for player callbacks, else first entity name. |
| `asChildName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity or second entity. |

**Returns:** `bool` — .

    1. `Entity_RemoveConnection`

```cpp
void Entity_RemoveConnection(const tString &in asName,
                             const tString &in asMainEntity)
```

Removes a specific connection on an entity.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the connection to remove. |
| `asMainEntity` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the entity to remove the connection from. Wildcard(s) * are supported. |

**Returns:** `void`

    1. `Entity_RemoveEntityAttachment`

```cpp
bool Entity_RemoveEntityAttachment(const tString &in asName)
```

Removes an attachment to another entity if the entity(ies) has one.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to be no longer attached to another, Wildcard(s) * are supported |

**Returns:** `bool`

    1. `Entity_SetActive`

```cpp
void Entity_SetActive(const tString &in asName,
                      bool abActive)
```

Set if entity is active (visible and functioning) or not.

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity, Wildcard(s) * are supported |
| `abActive` | `bool` | true = entity becomes active - false = entity becomes inactive |

**Returns:** `void`

    1. `Entity_SetAnimationMessageEventCallback`

```cpp
void Entity_SetAnimationMessageEventCallback(const tString &in asEntityName,
                                             const tString &in asCallbackFunc,
                                             bool abAutoRemove)
```

Sets a callback for the message events in the currently playing animation.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asCallbackFunc` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the callback function. Syntx void Func(const tString &in asEntityName, const tString &in asAnimName, int alMessageEventID) (last arg is for future usage) |
| `abAutoRemove` | `bool` | If the callback is removed once triggered. |

**Returns:** `void`

    1. `Entity_SetAnimationPaused`

```cpp
void Entity_SetAnimationPaused(const tString &in asEntityName,
                               const tString &in asAnimationName,
                               bool abPaused = true)
```

Pause or unpause an animation on the specified entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimationName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation. |
| `abPaused` | `bool` | true to pause, false to resume |

**Returns:** `void`

    1. `Entity_SetAnimationRelativeTimePosition`

```cpp
void Entity_SetAnimationRelativeTimePosition(const tString &in asEntityName,
                                             const tString &in asAnimationName,
                                             float afTimePos)
```

Sets the relative time position of a specific animation.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimationName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation. |
| `afTimePos` | `float` | a value between 0 and 1, where 0 is the start of the animation and 1 is the end. |

**Returns:** `void`

    1. `Entity_SetAutoSleep`

```cpp
void Entity_SetAutoSleep(const tString &in asName,
                         bool abX)
```

Sets if the entity should sleep automatically when it need no updating

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity, Wildcard(s) * are supported |
| `abX` | `bool` | true = Entity will sleep automatically - false = entity will not sleep automatically |

**Returns:** `void`

    1. `Entity_SetCollide`

```cpp
void Entity_SetCollide(const tString &in asEntityName,
                       bool abActive)
```

Turn off or on collision for all the bodies in the given entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `abActive` | `bool` | true = collision on, false = collision off. |

**Returns:** `void`

    1. `Entity_SetCollideCharacter`

```cpp
void Entity_SetCollideCharacter(const tString &in asEntityName,
                                bool abActive)
```

Turn off or on character collision for all the bodies in the given entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `abActive` | `bool` | true = collision on, false = collision off. |

**Returns:** `void`

    1. `Entity_SetColorMul`

```cpp
void Entity_SetColorMul(const tString &in asEntityName,
                        const cColor &in aColor)
```

Set the color mul of the entity

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | color to set color mul to |

**Returns:** `void`

    1. `Entity_SetConnectionStateChangeCallback`

```cpp
void Entity_SetConnectionStateChangeCallback(const tString &in asEntityName,
                                             const tString &in asCallback)
```

Sets the callback for when the connection state changes on an entity  
Syntax for callback function: void FunctionName(string &in asEntityName, int alState).

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to get the callback. Wildcard(s) * are supported. |
| `asCallback` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the callback function. |

**Returns:** `void`

    1. `Entity_SetEffectBaseColor`

```cpp
void Entity_SetEffectBaseColor(const tString &in asEntityName,
                               const cColor &in aColor)
```

Sets the base color of the effects

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. Wildcard(s) * are supported. |
| `aColor` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | the color all effects will be multiplied with |

**Returns:** `void`

    1. `Entity_SetEffectsActive`

```cpp
void Entity_SetEffectsActive(const tString &in asEntityName,
                             bool abActive,
                             bool abFadeAndPlaySounds)
```

Activates or deactivates the effects on a entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `abActive` | `bool` | true = activates effects - false = deactivates effects. |
| `abFadeAndPlaySounds` | `bool` | if effects should fade in/out and sounds play. |

**Returns:** `void`

    1. `Entity_SetInteractionDisabled`

```cpp
void Entity_SetInteractionDisabled(const tString &in asEntityName,
                                   bool abX)
```

Sets if the player can interact with an entity or not.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity, Wildcard(s) * are supported |
| `abX` | `bool` | true = interaction disabled - false = interaction enabled. |

**Returns:** `void`

    1. `Entity_SetIsOccluder`

```cpp
void Entity_SetIsOccluder(const tString &in asName,
                          bool abOccluder)
```

Set if entity is an occluder

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity, Wildcard(s) * are supported |
| `abOccluder` | `bool` | true = object is occluder |

**Returns:** `void`

    1. `Entity_SetMaxInteractionDistance`

```cpp
void Entity_SetMaxInteractionDistance(const tString &in asEntityName,
                                      float afDistance)
```

Change the max interaction distance of an entity from the default/entity configured distance.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity, Wildcard(s) * are supported |
| `afDistance` | `float` | distance in meters that the entity can be interacted from. |

**Returns:** `void`

    1. `Entity_SetPlayerInteractCallback`

```cpp
void Entity_SetPlayerInteractCallback(const tString &in asEntityName,
                                      const tString &in asCallback,
                                      bool abRemoveWhenInteracted)
```

Sets the callback for when the player interacts with a specific entity.  
Syntax for callback function: void FunctionName(string &in asEntityName).

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to get the callback. Wildcard(s) * are supported. |
| `asCallback` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the callback function. |
| `abRemoveWhenInteracted` | `bool` | if the callback should be removed after it has been called. |

**Returns:** `void`

    1. `Entity_SetPlayerLookAtCallback`

```cpp
void Entity_SetPlayerLookAtCallback(const tString &in asEntityName,
                                    const tString &in asCallback,
                                    bool abRemoveWhenLookedAt = true,
                                    bool abCheckCenterOfScreen = true,
                                    bool abCheckRayIntersection = true,
                                    float afMaxDistance = -1,
                                    float afCallbackDelay = 0)
```

Sets the callback for when the player looks at or turns away from a specific entity.  
Syntax for callback function: void FunctionName(const tString &in asEntityName, int alState). alState is 1 if the player looks at the entity and -1 if the player stops looking.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the entity to get the callback. Wildcard(s) * are supported. |
| `asCallback` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | the name of the callback function. If set to  will remove a previously set callback |
| `abRemoveWhenLookedAt` | `bool` | if the callback should be removed after it has been called. |
| `abCheckCenterOfScreen` | `bool` | if the entity counts as looked at only when at the center of the screen. |
| `abCheckRayIntersection` | `bool` | if the entity counts as looked at only if there is a clear line of sight to it. Note that this can return false negatives, especially when not checking center of screen. |
| `afMaxDistance` | `float` | max distance at which the entity must be for the callback to be triggered. |
| `afCallbackDelay` | `float` | time the player needs to look at the entity for the entity to trigger (in seconds). |

**Returns:** `void`

    1. `Entity_SetProcAnimationPaused`

```cpp
void Entity_SetProcAnimationPaused(const tString &in asEntityName,
                                   const tString &in asAnimationName,
                                   bool abPaused = true)
```

Pause or unpause a procedural animation on the specified entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimationName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation. |
| `abPaused` | `bool` | true to pause, false to resume |

**Returns:** `void`

    1. `Entity_SetProcAnimationSpeed`

```cpp
void Entity_SetProcAnimationSpeed(const tString &in asEntityName,
                                  const tString &in asAnimationName,
                                  float afSpeed)
```

Sets the speed of a proc animation.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimationName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the animation. |
| `afSpeed` | `float` | speed to set. |

**Returns:** `void`

    1. `Entity_SetReflectionVisibility`

```cpp
void Entity_SetReflectionVisibility(const tString &in asEntityName,
                                    bool abVisibleInReflection,
                                    bool abVisibleInWorld)
```

Sets whether the entity is drawn in reflections or not, and the real world or not.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the prop. Wildcard(s) * are supported. |
| `abVisibleInReflection` | `bool` | whether the entity is drawn in reflections |
| `abVisibleInWorld` | `bool` | whether the entity is drawn in the real world |

**Returns:** `void`

    1. `Entity_SetVarBool`

```cpp
void Entity_SetVarBool(const tString &in asEntityName,
                       const tString &in asVarName,
                       bool abX)
```

Sets the value of an entity boolean variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the boolean variable. |
| `abX` | `bool` | new value for the variable. |

**Returns:** `void`

    1. `Entity_SetVarColor`

```cpp
void Entity_SetVarColor(const tString &in asEntityName,
                        const tString &in asVarName,
                        const cColor &in aX)
```

Sets the value of an entity color variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the color variable. |
| `aX` | `[cColor](https://wiki.frictionalgames.com/page/../../cColor)` | new value for the variable. |

**Returns:** `void`

    1. `Entity_SetVarFloat`

```cpp
void Entity_SetVarFloat(const tString &in asEntityName,
                        const tString &in asVarName,
                        float afX)
```

Sets the value of an entity variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the string variable. |
| `afX` | `float` | new value for the variable. |

**Returns:** `void`

    1. `Entity_SetVarInt`

```cpp
void Entity_SetVarInt(const tString &in asEntityName,
                      const tString &in asVarName,
                      int alX)
```

Sets the value of an entity integer variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the integer variable. |
| `alX` | `int` | new value for the variable. |

**Returns:** `void`

    1. `Entity_SetVarString`

```cpp
void Entity_SetVarString(const tString &in asEntityName,
                         const tString &in asVarName,
                         const tString &in asX)
```

Sets the value of an entity string variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the string variable. |
| `asX` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | new value for the variable. |

**Returns:** `void`

    1. `Entity_SetVarVector2f`

```cpp
void Entity_SetVarVector2f(const tString &in asEntityName,
                           const tString &in asVarName,
                           const cVector2f &in avX)
```

Sets the value of an entity vector2f variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector2f variable. |
| `avX` | `[cVector2f](https://wiki.frictionalgames.com/page/../../cVector2f)` | new value for the variable. |

**Returns:** `void`

    1. `Entity_SetVarVector3f`

```cpp
void Entity_SetVarVector3f(const tString &in asEntityName,
                           const tString &in asVarName,
                           const cVector3f &in avX)
```

Sets the value of an entity vector3f variable. Wildcard(s) * are supported for EntityName.	*

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. |
| `asVarName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the vector3f variable. |
| `avX` | `[cVector3f](https://wiki.frictionalgames.com/page/../../cVector3f)` | new value for the variable. |

**Returns:** `void`

    1. `Entity_Sleep`

```cpp
void Entity_Sleep(const tString &in asName)
```

Forces the entity to sleep (disabling Update/PostUpdate). Has no effect if it is already sleeping

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity, Wildcard(s) * are supported |

**Returns:** `void`

    1. `Entity_StopAnimation`

```cpp
void Entity_StopAnimation(const tString &in asEntityName)
```

Stops any currently playing animation on the specified entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |

**Returns:** `void`

    1. `Entity_StopProcAnimation`

```cpp
void Entity_StopProcAnimation(const tString &in asEntityName,
                              const tString &in asAnimation,
                              float afFadeTime = 0.1f)
```

Stops a procedural animation on the specified entity.

| Name | Type | Description |
| --- | --- | --- |
| `asEntityName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `asAnimation` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | name of the entity. Wildcard(s) * are supported. |
| `afFadeTime` | `float` | the time it takes to fade out. |

**Returns:** `void`

    1. `Entity_WakeUp`

```cpp
void Entity_WakeUp(const tString &in asName)
```

Forces the entity to wake up (enabling Update/PostUpdate). Has no effect if it is already awake

| Name | Type | Description |
| --- | --- | --- |
| `asName` | `[tString](https://wiki.frictionalgames.com/page/../../tString)` | Name of the entity, Wildcard(s) * are supported |

**Returns:** `void`

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Scripting Api/Entity](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api/Entity)
- Revision: `5007`
- Source update: `2020-08-24T20:40:43Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Entity Components
description: "= Entity Components ="
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Entity_Components"
sourceRevision: 4774
sourceUpdated: "2020-08-21T11:09:04Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
= Entity Components =

## Overview
What follows here is an overview of all the different entity components that are present. Entity components are used to extend the functionality of any derived *iLuxEntity* class.

To add a module simply call the creation function in the SetupAfterLoad() call in the entity script file. It is often required to save a handle to the returned class as well.

## CharMover
**Creation function:** *cLuxCharMover@ cLux_CreateEntityComponent_CharMover(iLuxEntity @apEntity, iCharacterBody @apCharBody)*

### General
This is used to more easily move around a character body. It controls movement forward, rotation and very simple avoidance behaviors.

## PathFinder
**Creation function:** *cLuxPathFinder@ cLux_CreateEntityComponent_PathFinder(iLuxEntity @apEntity)*

### General
This is used to add pathfinding capabilities. It relies on Path nodes being placed in the map and usually works together with CharMover (but this is not needed). 

## StateMachine
**Creation function:** *cLuxPathFinder@ cLux_CreateEntityComponent_StateMachine(iLuxEntity @apEntity)*

### General
This adds a state machine to the entity. It can be used for pretty much every thing but is mainly used for AI purposes.

It is important to note that there can only be ONE statemachine in a class!

To use the statemachine, you need to create states right after having created the module. It is very important that all states are always created in the same order for all entities using the same script file (basically meaning you should not dynamically create states during the update loop or similar). For instance:

```
@mpStateMachine = cLux_CreateEntityComponent_StateMachine(mBaseObj);
mpStateMachine.AddState("Idle", eState_Idle);
mpStateMachine.AddState("Move", eState_Move);
mpStateMachine.AddState("Stop", eState_Stop);
```

Every state has a couple of actions (methods really) that are called in response to different events. These are:

**Enter()**   
Called when the state is started.  
**Leave()**   
Called when the state is over. This is called before Enter of the new state!  
**Update(float afTimeStep)**   
Called every update.  
**SubStateOver(int alSubStateId)**   
Called when a sub state is over. More on substates below.  
**Message(int alMessageId)**   
This is any entity message that is intercepted. Can also be a custom message.  
**TimerUp(int alTimerId)**   
When a timer is over.

For each state, each of these functions get a name based on the syntax like this:  
*void State_[StateName]_[Action]*   
For instance the *Enter()* action in the state "Idle" is:

```
void State_Idle_Enter()
```

Note that you only have to define the actions that you want, so for instance a Stop state might only be something like:

```
void State_Stop_Enter() {
 //Stop the character
}
void State_Stop_Leave() {
 //Make the character move again
}
```

And skip Update, etc. (This is actually the best practice too!)

### Sub State
A sub state is just like a state that runs along side the normal state. What makes it different is that they only last as long as the state that started it. Also sub states cannot change the normal state, only what the next substate will be. It can be sort of seen a smaller state machine inside a state. The sub states are created just like normal states but using the *AddSubState(tString, int)* method instead. Also note that substates can be shared between all of the states. They only belong to the a state in the sense that a sub state started in state X will only run while state X is active.

The function syntax for sub states is:  
*void SubState_[StateName]_[Action]* For example:

```
void SubState_ThrowObject_Enter()
```

When a sub state is over, the state that started it has the action *SubStateOver(int alSubStateId)* called, where *alSubStateId* contains the id of the sub state.

Sub state has all the same actions as the normal state except for SubStateOver(int alSubStateId)

Another important feature of sub states is that there does not have to be one set. So it is okay to do:

```
 mpStateMachine.ChangeSubState(-1)
```

which set no state at all as sub state. This is actually the default setting when ever a new normal state is started.

### Default State
The default state is a state that can be used by both normal states and sub states. To add it just write a state function with the name "Default" instead of a state name. (This means a state cannot be named "Default".) Then this function will be called if the current state does not contain it. So for instance if you have something like:

```
void State_Default_Update(float afTimeStep){
...
}

void State_State1_Update(float afTimeStep){
...
}
```

If the state machine is currently in *State1* then the *Update* for *State1* will be called. However, if the current state is *State2* and it does not have an implemention of *Update*, the *Default* version of *Update* will be called.

There is a special case for *State_Default_Message*. This is also called if the state specific function returns false.

### Timers
Timers are used to check if a certain amount of time has passed. They are only valid for the state that started it, so if a timer is active when state changes, then it becomes removed. Also, state and sub state do not share timers. So if sub state "ThrowObject" starts a timer, then *TimerUp* will only be called in the sub state, and not the normal state. Timers are started with *StartTimer(int alId, float afTime)* in the state machine and can be stopped with *StopTimer(int alId)*.

## SoundListener
**Creation function:** *cLuxSoundListener @ cLux_CreateEntityComponent_SoundListener (iLuxEntity @apEntity)*

### General
This makes the entity into a sound listener and it will now receive the event message eLuxEntityMessage_SoundHeard (mvX=postion and mlX=Prio) whenever a sound of a specific type is played (specified in "sounds/ai_reaction_sounds.dat", or whatever is set in the game.cfg) or an event is broadcasted (Sound_CreateAIEventAtEntity()). 

If attached to an Agent, then setting SensesActive to false disables the listener too.

Also note that footstep sounds are not sound entities and thus do not generate event automatically. Therefore the MoveState does a special broadcast of the events (properties are the top).

### Properties
There are two properties that regulate how the listener reacts to sounds.

**Radius**  
This is used when checking if the listener overlaps with a sound event. Position is gotten by calling GetPosition() in the Entity (In Agents, center of the char collider) and defualt is 0.5 meters. This can be extended to make a listener get better hearing.  
*Reason we do not calculate any volume is because it becomes a bit vague and hard to keep track of, this is a more robust and easy to understand system.*

**MinHearPrio**  
The minimum prio a sound must have for the listener to hear it. Usually common sounds like small object physics impacts have 0, walking steps 1 and running 2.  Can also be good to change this depending on state to set the alertness of an entity.

### Debugging
You can check Show Sound AI Events in the debug window to see two sphere drawn of each triggered event. The red sphere notes the center and the white one the range.
### The File
The ai_reaction_sounds.dat file is basically just an xml file where you set which sounds should generate events and how the genreated event should look like. Important to note that the sound types are parsed from top to bottom when the game is parsed. This means that if a sound applies to many types, the top one will be chosen. This could come in handy for special cases.

The properties are as follows:

**SubStrings**  
A list of strings, separated by space and/or comma, that the sound's data name (NOT its entity name) must contain.

**Radius**  
The radius of the generated event.

**Prio**  
As listners can be setup to not hear sounds below a certain prio, this can be used to exclude certain listeners. Listener AI also often use this to see what sound to check out if more than one are heard (largest prio picked).

**Params**  
A type can have many params, but it almost always is enough with one. You can set MinValue to see cull out certain sounds and note that this can be used to have different radius on a sound depending on a param (several types, same substrings, but different param min values). Just makes sure to have the largest min values first! (Otherwise they will never get picked).  
If a name for the param is not set, then index is used instead.

## HeadTracker
**Creation function:** *cLuxHeadTracker @ cLux_CreateEntityComponent_HeadTracker(iLuxEntity @apEntity)*

### General
This will make the entity's head follow a certain target. The HeadTracker component needs to be setup loading up the bones that make up the neck and how much influence they have on each other. This can be done manually through the Setup() method, or by reading the variables in the .ent file using the LoadFromVariables() method.

## ForceEmitter
**Creation function:** *cLuxForceEmitter @ cLux_CreateEntityComponent_ForceEmitter(iLuxEntity @apEntity)*

### General
This will give the entity a force field (cForceField) which makes certain things in the game world (such as undergrowth) animate and react to its presence . If MaxForceSpeed is higher than 0 it will also vary in strength depending on the speed of the MainBody (or character if set).

## BarkMachine
**Creation function:** *cLuxBarkMachine   @ cLux_CreateEntityComponent_BarkMachine  (iLuxEntity @apEntity)*

### General
This creates a component that can have one or more states with random sounds or voice quips (barks). It is meant to be used with entities that require different sounds/voices to be randomly played depending on which state it is in.

## BackboneTail
**Creation function:** *cLuxBackboneTail   @ cLux_CreateEntityComponent_BackboneTail  (iLuxEntity @apEntity)*

### General
When this is added, the backbone of the entity (as defined in the ent file) will be bent as the entity moves along. It is meant to be used by things like fishes, etc to get more natural like movement, but can of course be used for whatever. The BackboneTail component needs to be setup loading up the bones that make up the tail and how much influence they have on each other. This can be done manually through the Setup() method, or by reading the variables in the .ent file using the LoadFromVariables() method.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Entity Components](https://wiki.frictionalgames.com/page/HPL3/Scripting/Entity_Components)
- Revision: `4774`
- Source update: `2020-08-21T11:09:04Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Input Types
description: Input types (InputHandlertypes.hps) is a script consisting of two Shared Enum classes which can be considered as a list of possible actions.
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Input_Types"
sourceRevision: 6225
sourceUpdated: "2021-09-14T01:57:39Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
## What are Input types?
Input types *(InputHandler_types.hps)* is a script consisting of two Shared **Enum classes** which can be considered as a list of possible actions.

?<sub>Be sure to use them correctly as trying to add own Enum Class while trying to use them as a part of gameplay should not work.</sub>?

Names of these classes are somewhat self-explanatory:

## eAction
- Button-like action (fixed step)

### Handler
These interactions are directly handled by *"OnAction ( alAction, abPressed )"*. However the game some of these actions later converts to Analog type and then handles just like [eAnalogTypes](/scripting/input-types/#eanalogtypes)

#### Params:
##### (int)   alAction
*Number representation <sub>(?of input type position?)</sub> in eAction
**addressable using one of the **eAction enum** entries

##### (bool)   abPressed
*Has it been pressed?

#### Typical use

```
void OnAction(int alAction, bool abPressed)
	{	
		///////////////////////////////////
		// Flashlight
		if(abPressed && alAction==eAction_Flashlight)
		{
			
			SetFlashlightOn(!mbFlashlightOn);
		}
	}
```
code that takes care of FlashLight. <u>(- script/player/Player.hps)</u>

## eAnalogTypes
- Joystick-like action (Analog step)

### Handler
These are being handled by functions *"OnAnalogInput ( alAnalogID, avAmount )"* .

#### Params:
*(int)   alAnalogId
**number representation <sub>(?of input type position?)</sub> in eAnalogTypes
***addressable using one of the **eAnalogTypes enum** entries
*(cVector3f)   avAmount
**3D vector <sub>(?Basket class?)</sub> with parameters:
***X
***Y
***Z
**Values of [-1.0f ; 1.0f]

#### Typical use

```
	void OnAnalogInput(int alAnalogId, const cVector3f &in avAmount)
	{
         //....................
         //////////////////////
         // Move
         if(alAnalogId == eAnalogType_Move || alAnalogId == eAnalogType_GamepadMove)
		{
			iCharacterBody@ pCharBody = mBaseObj.GetCharacterBody();
			float fLength = avAmount.Length();
			
			if(fLength > 0.1f)
			{
				//////////////////////////////
				// Lean
				if(mbAnalogLeanPressed)
				{
					Lean(avAmount.x);		
				}
				//////////////////////////////
				// Movement
				else
				{
					if(cMath_Abs(avAmount.y) > 0.001f)
						pCharBody.Move(eCharDir_Forward, avAmount.y);
				
					if(cMath_Abs(avAmount.x) > 0.001f)
						pCharBody.Move(eCharDir_Right, avAmount.x);
				}
			}
		}
         //....................
	}
```
Here you can see also already mentioned analog type *(eAnalogType_Move)* that was earlier sampled and quantized from *eAction_Forward / _Backward / _Right / _Left*, by other script. <u>(- script/player/Player.hps)</u>

## Uses
This class could be considered a Weak Spot in case you ever wanted to do some new player implementations or to make your game controllable by virtually anything.

With a slight combination of [Input Handler](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Input_Handler) and [Player](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Player_Overview) scripts even [implementing a Microphone is possible.](https://youtu.be/ZS0fIS2qrSA)

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Scripting/Input Types](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Input_Types)
- Revision: `6225`
- Source update: `2021-09-14T01:57:39Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

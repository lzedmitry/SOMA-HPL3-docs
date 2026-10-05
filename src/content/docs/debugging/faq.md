---
title: Troubleshooting
description: Turn this into a category
category: debugging
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Troubleshooting"
sourceRevision: 4747
sourceUpdated: "2020-08-21T09:45:25Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: wip
generated: true
tags:
  - debugging
---
:::caution[SOURCE STATUS: WIP]
This source page is marked as undergoing editing on the Frictional Wiki.
:::

:::caution[SOURCE STATUS: Incomplete]
Turn this into a category
:::

:::caution[SOURCE STATUS: Source WIP]

:::

=FAQ=

## Engine
**Q: Wait, so there are two HPL3 engines? One for SOMA and one for Amnesia: Rebirth? This is confusing**

A: Frictional Games' in-house engine, HPL, improves and evolves with each game they release. Each version of the engine is usually very coupled with the game it released with, and was designed specifically for that game in mind. As such, some features differ from game to game, even if some games are labeled under the same version of the engine. That is why each game has its own categories and documentation, instead of global documentation for the entire engine.

## Scripting
**Q:  When an entity with many bodies is attached to a sticky area it doesn't work to make it a static collider?**   

A: Use a timer so it is set to static collider half a second or so after it has attached to the sticky area. The sticky area and static colliders overlaps in usage of some physics settings, so the sticky area needs to be done before you set the body as static.

**Q: MoveObject does not work properly with an entity with two or more bodies?**   

A: Specify which body to move by adding it to MainPhysicsBody in the model editor → entity settings → Class → Prop_MoveObject.

**Q: Using a function returning a value from C++ (such as GetName() ) as an argument to a callback doesn't give the callback the correct value.**   

A: Use a temporary variable to store the value in before using it as an argument.

**Q:** **Oh no! One of my levers have weird interaction. It won't move, or it suddenly inverts the mouse movement!**   

A: Lever interaction is tricky. First try changing the entity's MoveDirection. If that doesn't help and the problem only occurs when the lever is almost at its max or min position, try limiting the range of the joint in the .ent file.

## Audio
**Q: My voice subject never ends or never jumps to next sound/line, why?**   
Check so that "End After Extra Effect" is not checked in the sound's properties. (you need to enable advanced mode and press the down arrow by the sound to see this). If that is the case, the audio file you are playing might be looping and therefore never quitting!

## GUI
**Q: Why can't I render something to a GUI?**   
A: Try these steps

#Make sure the material for the GUI sub mesh is transparent. Ask modeller to double check if unsure
#Ensure that correct Submesh is set up using the model editor
#Ensure that you are not changing the material of the Submesh in code (For instance, the keypad in 0.6 changes its ilum texture, but the specific mesh must be called)
#Is your GUI's draw function being called? Put a cLux_AddDebugMessage in there as a test and it should iterate every frame.
#Has the GUI been set as inactive either in the editor or in script with Terminal_SetGuiActive?
#Finally, make sure you are rendering something simple like a label to start before trying to implement a full blown GUI!

## Modeling
**Q: I have created a socket but it is not following along with the skeleton**   
A: Make sure that you have not created the socket on a controller bone. These are not used by the engine and will remain at the same postion. Normally you can spot them by the "_Ctrl" suffix. To fix, just create the socket at some other bone.

'''Q: My export to detail meshes are 100x larger than usual  
'''
A: You might be using a new exporter that has these issues. in export settings set the units to "Centimeter"

## Particles
**Q:  Particles does not fade in and out even though I have configured max and min distance?**   
A: Check the colour setting for the particle and make sure that the alpha is not lowered. If the particle should be fainter, fade it with the colour setting instead (changing from white towards black makes the particle less visible). The alpha can then be left at full and the distance fade will work properly.

## Level Editing
**Q: After loading a map I can't pan the camera only rotate?**    
A: The Controller mode is probably set to Fly. Set it back to Maya by clicking on View button at the top left → Controller → Maya.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Troubleshooting](https://wiki.frictionalgames.com/page/HPL3/Troubleshooting)
- Revision: `4747`
- Source update: `2020-08-21T09:45:25Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

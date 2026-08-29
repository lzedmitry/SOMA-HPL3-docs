---
title: Camera Animation
description: "These areas are ased as a camera viewpoint in a camera animation. The camera animation system is used to move the player camera along a specific path while still allowing some degree of interaction. The animation, once s"
category: areas
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Areas/Camera_Animation_Area"
sourceRevision: 5547
sourceUpdated: "2020-11-09T21:10:42Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - areas
---
These areas are ased as a camera viewpoint in a camera animation. The camera animation system is used to move the player camera along a specific path while still allowing some degree of interaction. The animation, once started via script, will move the camera between areas with the same base name.

The areas are used in conjunction with their respective helper scripts. 
The helper function prefixes are: **CameraAnimation_, CameraAnimationNode_**

## Instructions
To use the system, place CameraAnimation nodes (Area → CameraAnimation) in the scene and give each of them the name of the animation followed by an underscore and their placement within the animation (such as WakeUpAnimation_1, WakeUpAnimation_2 etc). Note that if you duplicate (Ctrl-D) a node, the duplicate will automatically get the next available number as its suffix.

Make sure to set the time parameters on the nodes, or else the camera will just teleport, as the default times are 0 (although that might be wanted in some cases).

Rotate the nodes so that their Z-axes point in the direction you want the camera to look at that part of the animation.

In script, call the helper function `CameraAnimation_Begin()` to start the animation. In our example, the argument to put in the function would be "WakeUpAnimation".

## Area (Animation node) properties
| Property | Description |
| --- | --- |
| MaxYaw/MaxPitch | Dictates how far the player is allowed to rotate the camera away from the target forward rotation. This value is interpolated between nodes. |
| LookSpeedMultiplier | How fast the player can rotate the camera. |
| ForwardTime | The time it takes to move from this node to the next at full speed forward. |
| BackwardTime | The time it takes to move from the next node to this one at full reverse speed. |
| AutoMovement | Dictates how the animation behaves when no movement input is given, or when movement input is disabled. 0 stops movement, 1 is as if given full forward speed (animation will finish after [ForwardTime] seconds), -1 is as if given full reverse speed. |
| LookMoveDistance | The length between this node and the next the player can move just by looking toward the next node, given as a value between 0 and 1. |
| LookMoveMaxAngle | The maximum angle away from the next node the player can look and still move forward. Only valid if LookMoveDistance > 0. |
| InteractiveMovement | If checked, the player can control the movement between this node and the next. If unchecked, the AutoMovement property has complete control over the movement and should not be set to 0. |
| CrouchOnExit | If checked, the player will automatically crouch if the animation is ended at this node. |
| InitToCamera | If checked, the node is given the orientation of the camera when the animation starts. This is very useful when you want the animation to have a smooth beginning, or you want to make sure the player is returned to where they were when the end node is reached. |
| UsePlayerEyeline | If ticked, instead of using the Y-value of the node itself, the camera system uses the Y-value that the player's eyeline should be at that point (i.e. from the ground/floor upwards). |
| CallbackFunc | Function in the level script that should be called when reaching this node. The syntax is bool FuncName(const tString &in asEntity, int alDirection), where asEntity is the name of the node and alDirection is 1 if moving forward and -1 if moving backward. |

## Important Functions
| Function | Description |
| --- | --- |
| CameraAnimation_Begin | Start a camera animation. |
| CameraAnimation_End | Stop a camera animation. |
| CameraAnimationNode_SetAutoMove | Allows you to pause or continue animation at a particular node. |
| CameraAnimationNode_SetInteractiveMovement | Allows you to enable the player to progress within a particular node. |

Asides from these functions, there are getters and setters for the available parameters.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Areas/Camera Animation Area](https://wiki.frictionalgames.com/page/HPL3/Areas/Camera_Animation_Area)
- Revision: `5547`
- Source update: `2020-11-09T21:10:42Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

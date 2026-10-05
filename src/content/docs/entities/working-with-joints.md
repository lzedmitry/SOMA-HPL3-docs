---
title: Working with Joints
description: "= Joints = Joints are used to constrain the movement between to bodies. They are a very powerful tool and can be used to do a lot of stuff such as lamps that can sway back and forth, drawers that can be interacted with a"
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Entities/Working_with_Joints"
sourceRevision: 7142
sourceUpdated: "2026-07-30T21:59:51Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
= Joints =
Joints are used to constrain the movement between to bodies. They are a very powerful tool and can be used to do a lot of stuff such as lamps that can sway back and forth, drawers that can be interacted with and even a car with wheels and suspenders.

All joints are made up from an anchor (also called pivot point) and an axis (also called pin direction), these have different meanings for the different joint types and describe the constraint. All bodies also have some limits to limit the constraint. If all of these values are set to 0 the limit is disabled. It can also be set if the two bodies on the joint will collide or not.

General Parameters:
- **Name**
- **Position**
- **Rotation**

Base Joint Parameters:
- **Set Parent Body button**: Press and click on a body to set it as parent body for the joint.
- **Set Child Body button**: Press and click on a body to set it as child body for the joint. Note that a joint must always have a child body.
- **Sticky Min Limit**
- **Sticky Max Limit**
- **Limit Step Count**
- **Breakable**: Set if the joint should break.
- **Break Force**: Force that should be applied on the joint for it to break (if Breakable is set).

Joint Sound Parameters:
- **Move Type**
- **Move Sound**
- **Min Speed**
- **Min Freq**
- **Min Freq Speed**
- **Min Volume**
- **Max Speed**
- **Max Freq**
- **Max Freq Speed**
- **Max Volume**
- **Middle Speed**
- **Middle Volume**
- **Break Sound**
- **Min Limit Sound**
- **Min Speed**
- **Max Speed**
- **Max Limit Sound**
- **Min Speed**
- **Max Speed**

Specific Parameters for Ball Joint:

[ball-and-socket.jpg](https://wiki.frictionalgames.com/page/ball-and-socket.jpg)

- **Max Cone Angle**: This is the maximum angle between Body1(Parent) and the axis. Has value from 0 – 180.
- **Max Twist Angle**: This is the maximum angle that bodies can twist relative to each other. Has a value from 0 – 180.

Specific Parameters for Hinge Joint:

[hinge.jpg](https://wiki.frictionalgames.com/page/hinge.jpg)

- **Min Angle** & **Max Angle**: Maximum and minimum angle between the bodies relative to the start position. Max angle is in the positive direction and min in the negative. To get the positive direction place your thumb on your right hand in the direction of the axis. Now bend your fingers towards your palm, the direction in which you fingers are pointing is the direction of the positive angle. In mathematics this is called the right hand rule. Valid values are 0 – 179.

Specific Parameters for Slider Joint:

[slider.jpg](https://wiki.frictionalgames.com/page/slider.jpg)

- **Min Distance** & **Max Distance**: Picture the anchor as attached to Body1(Parent). When the anchor is moved in the distance of the axis the distance gets larger and when it moves in the other way it gets negative (and smaller). At the start position the distance is 0.

Specific Parameters for Screw Joint:
- **Min Distance** & **Max Distance**: This joint works exactly as the slider but it can spin around the axis.

= Joint EditMode =

To build more complex physics setups, you will need to add joints to your models. This way you will be able to create stuff like doors, tables with drawers, levers and so on.

There are four types of joints that can be created at the moment:
- Ball
- Hinge
- Screw
- Slider

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Entities/Working with Joints](https://wiki.frictionalgames.com/page/HPL3/SOMA/Entities/Working_with_Joints)
- Revision: `7142`
- Source update: `2026-07-30T21:59:51Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

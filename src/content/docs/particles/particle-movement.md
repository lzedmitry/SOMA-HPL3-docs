---
title: Particle Movement
description: Reference for Particle Movement from the Frictional Wiki.
category: particles
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Particles/Particle_Movement"
sourceRevision: 7158
sourceUpdated: "2026-07-30T22:15:18Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - particles
---
### Movement
- **Velocity type**: The way in which the starting velocity is generated.
- **Box velocity**: The same as box start but with velocity instead.
- **Sphere Velocity**: The same as sphere start but with velocity instead.
- **Coord system**: The way in which the particles are related to the world and the object the system is attached to (if any). In world all the particles have an individual postion that does change depending on the parent object. In local however the particle position is dependant on the parent object so if that the particle moves and turns along with the parent.
- **Uses direction**: If the direction of the start velocity depends on the way the particle system is “facing” (with no rotation it faces up). This is useful for systems like steam where the system has a direction.
- **Gravity Type**: The type of gravity being applied to the particles.
** **None''': No gravity it applied.
** **Vector''': The gravity acceleration is applied.
** **Centre''': The particles are drawn towards the centre of the particle system with Gravity Acceleration Y as acceleration.
- **Gravity Acceleration**: Used differently according by the gravity type.
- **Acceleration**: Acceleration applied to all bodies.
- **Speed multiplier**: How much the speed is multiplied by each second. For example, 0.5 means that the speed halfed each second. 2 means it is doubled each second.
- **Maximum speed**: The maximum speed that the particles can reach.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Particles/Particle Movement](https://wiki.frictionalgames.com/page/HPL3/Particles/Particle_Movement)
- Revision: `7158`
- Source update: `2026-07-30T22:15:18Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Particle Start
description: Reference for Particle Start from the Frictional Wiki.
category: particles
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Particles/Particle_Start"
sourceRevision: 7157
sourceUpdated: "2026-07-30T22:15:07Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - particles
---
### Start
- **Start type**: Sets what method to use to generate the start position of the particles in the emitter.
- **Box start**: A box start is created using an x, y and z min and max value. The collection of particles will get the shape of a box.
- **Sphere start**: The positions are generated using an angle interval and the min and max value for the radius. You can think of it like this; an arrow start pointing up. This arrow is then rotated around the X axis (red) using a value between min and max. After that the arrow is rotated by the y axis (blue). The arrow will now be pointing in a specific direction and in this direction a position is created at a distance from center according to a number generated from min/max radius.

> **Figure (original Wiki file, not inlined):** [spherestart.jpg](https://wiki.frictionalgames.com/page/File:spherestart.jpg)

## Source & attribution

- Original Frictional Wiki page: [HPL3/Particles/Particle Start](https://wiki.frictionalgames.com/page/HPL3/Particles/Particle_Start)
- Revision: `7157`
- Source update: `2026-07-30T22:15:07Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

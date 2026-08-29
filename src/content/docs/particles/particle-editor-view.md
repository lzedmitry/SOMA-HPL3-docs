---
title: Particle Editor View
description: "= Particle Editor = The Particle Editor is used to create Particle Systems to be used in maps or entities."
category: particles
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Particles/Particle_Editor_View"
sourceRevision: 7155
sourceUpdated: "2026-07-30T22:13:51Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - particles
---
= Particle Editor =
The Particle Editor is used to create Particle Systems to be used in maps or entities.

## Foreword
### Min and Max values
A lot of values in this editor have both a min and max. This means that when the value is applied to a particle a value between min and max is randomly selected.

### Fading
Fading can be used to fade in and/or out some property like size or colour. The fading works like this. There are three relative values that are relative to the start value of the particle. The names for these values are start, middle and end and are used in that order. There are also two times that are relative to the life of the particle, for example if a particle has 2 seconds life time and the middle time is 0.5 then this occurs after 1 second (0.5 * 2). The first time is called middle time and this is when the start value is entirely faded from start to middle. The middle length is how long the middle value lasts. After middle time + middle length the middle value is faded to the end value.

## Overview
When run, the first screen we get to see is like this:

> **Figure (original Wiki file, not inlined):** [particle_editor.png](https://wiki.frictionalgames.com/page/File:particle_editor.png)

Each part of the screen has a specific function, as follows:

## Main Menu
This is a menu bar, just like in any other windowed application. Available options for this particular editor are as follows:

- **File**
** **New''': This command will reset the Particle System to an empty one, and the editor to a default state as well.
** **Open''': This will load a Particle System file (.ps) in the editor.
** **Save''': Use this to save your work to a file in disk. Will ask for a file name when no file has been created.
** **Save As''': This will also save your work, but will ask for a file name everytime it is called.
** **Open Recent''': This will show a list of up to 10 files that have been recently loaded or saved.
** **Quit''': This will exit the program.
- **Edit**
- **View**

## Source & attribution

- Original Frictional Wiki page: [HPL3/Particles/Particle Editor View](https://wiki.frictionalgames.com/page/HPL3/Particles/Particle_Editor_View)
- Revision: `7155`
- Source update: `2026-07-30T22:13:51Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

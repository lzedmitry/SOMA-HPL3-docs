---
title: Animation Principles
description: "= Animation - Lipsync ="
category: assets
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Modeling/Animation_Principles"
sourceRevision: 7128
sourceUpdated: "2026-07-30T21:12:44Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - assets
---
= Animation - Lipsync =

### Introduction
This tutorial was written for anybody working on animations that want a character to automatically lipsync. Lipsyncing is a technique used to move the mouth of a character to match the dialogue it is speaking. How the mouth should move is calculated in the code using the voice recording of the dialogue as well as a written transcript. This takes the line and converts it into phonemic characters. These are then converted into visemes which are used to move the mouth. The visemes has to be created by hand and that is what this tutorial will detail.

### Visemes
A viseme is a position that the mouth has when making a sound. We use a 3rd party imlementation from Annosoft. They have three different viseme mappings that can be used, each of different quality. The best quality comes from using 17 Visemes.

These pages show which visemes are needed and how to rig them.

[http://www.annosoft.com/docs/Visemes17.html](http://www.annosoft.com/docs/Visemes17.html) 

[http://www.annosoft.com/docs/Visemes12.html](http://www.annosoft.com/docs/Visemes12.html) 

[http://www.annosoft.com/docs/Visemes9.html](http://www.annosoft.com/docs/Visemes9.html) 

The visemes should be saved in "entity/animations/visemes/"

**Setting up** 

When the visemes are created they need to be setup in the ModelEditor.

''' Open the entitiy file in the ModelEditor
''' Click on Entity Settings > Animations
''' Add a new animation for each Viseme
''' Select the .dae_anim file for a Viseme
''' Name the animation after the number of visemes and the order of the annosoft website documentation. Using the naming convention Visemes_<Quality>_<ID>
''' Ex)  [http://www.annosoft.com/docs/Visemes17.html](http://www.annosoft.com/docs/Visemes17.html) Frame 1 (AA) should be named Visemes_17_1
''' When all of the visems has been setup the engine takes care of the rest

### Lipsync Tool
Can be used to edit the anno files. More to come…

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Modeling/Animation Principles](https://wiki.frictionalgames.com/page/HPL3/SOMA/Modeling/Animation_Principles)
- Revision: `7128`
- Source update: `2026-07-30T21:12:44Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Sounds
description: "= Sounds ="
category: level-building
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Level_Design/Sounds"
sourceRevision: 7090
sourceUpdated: "2026-07-30T09:54:39Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - level-building
---
= Sounds =

General Parameters:
- **Name**: Name of the sound. Should be unique for all objects in map.
- **Active**
- **Position**: 3D Vector storing the position in world.

Specific Parameters:
- **Sound Entity file**: .snt file to be used by the sound.
- **Use defaults**: if active, volume and Min/Max Distance values will be read from the .snt file.
- **Min Distance** / **Max Distance**: Distances that will determine the space in which the sound will be faded out. Inside the radius defined by Min Distance the sound will have full volume.
- **Volume**: value for full volume. Should be a real number in the [0, 1] range.

=Sound EditMode=

This EditMode is used to create Sound Entities in the map. These are used to add ambience sound, static sounds like water flowing, or pretty much any sound you want.

To create a Sound Entity, just click on the grid when this EditMode is active. This will create an "empty" Sound Entity, meaning it is just a container.
Optionally, you can set up the .snt file that will be used by the newly created Sound Entity, in the only input that shows on the EditMode window. 

Have into account that these options will be valid for objects created right after changing them, so any Sound Entity that is already created will keep its settings.

More on sounds [here](https://wiki.frictionalgames.com/page/HPL2/Sounds).

= Sound Browser window =
This window helps when having to pick sounds. It can work in two different modes:

- Sound Entity

> **Figure (original Wiki file, not inlined):** [sound_entity.png](https://wiki.frictionalgames.com/page/File:sound_entity.png)

** **Full path input''': This input will display the current full path, will show each step in the path as a row in the open list. Clicking on a row will make the dialog navigate to that folder.
** **Up button''': will make the dialog navigate to the parent folder.
** **Directory and file listing'''

- Sound Event

> **Figure (original Wiki file, not inlined):** [sound_event.png](https://wiki.frictionalgames.com/page/File:sound_event.png)

** Two boxes will show up, left one will list available **Sound Projects** (or sound banks) and **Sound Groups** (pretty much like subdirectories) in a tree fashion. The one at the right will show **Sound Events''' (sounds actually) present inside the picked Group. To use one of them, just select it there.

These are common for both modes.
- **Play button**: will play a sample of the picked sound.
- **Load file name**: The name of the file to load.
- **Load button**: Will try to load the given file name and close. 
- **Cancel button**: Will just close the dialog.

## Source & attribution

- Original Frictional Wiki page: [HPL3/Level Design/Sounds](https://wiki.frictionalgames.com/page/HPL3/Level_Design/Sounds)
- Revision: `7090`
- Source update: `2026-07-30T09:54:39Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Model Editor Outline
description: "= Outline window ="
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Entities/Model_Editor_Outline"
sourceRevision: 4969
sourceUpdated: "2020-08-23T19:59:56Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
= Outline window =

The Outline window is a nice tool to edit attachments indirectly. When brought up, all objects in the scene will be listed in it.
Shapes belonging to bodies can be kept from being listed, this can be toggled with the "Hide connected shapes" input.

> **Figure (original Wiki file, not inlined):** [outline01.jpg](https://wiki.frictionalgames.com/page/File:outline01.jpg)

Depending on the type of object selected, additional commands will be displayed on it.

### Bodies and bones
For bodies and bones, the "Edit Attachments" command will appear. 

> **Figure (original Wiki file, not inlined):** [outline02.jpg](https://wiki.frictionalgames.com/page/File:outline02.jpg)

When clicked, a helper attachments window will pop up, where you can select the objects that you wish to be attached to this body or bone.

> **Figure (original Wiki file, not inlined):** [outline03.jpg](https://wiki.frictionalgames.com/page/File:outline03.jpg)

### Joints
Joint objects will show four commands, which are "Attach Parent", "Detach Parent", "Attach Child" and "Detach Child", with "Parent" and "Child" meaning parent body and child body respectively. The "Attach" ones will pop up a helper window just like with bodies and bones, only difference is these displaying bodies.

> **Figure (original Wiki file, not inlined):** [outline05.jpg](https://wiki.frictionalgames.com/page/File:outline05.jpg)

### Rest of objects
Any object other than the above will show a Detach command, which will detach it from its parent body or bone if attached at all.

> **Figure (original Wiki file, not inlined):** [outline04.jpg](https://wiki.frictionalgames.com/page/File:outline04.jpg)

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Entities/Model Editor Outline](https://wiki.frictionalgames.com/page/HPL3/SOMA/Entities/Model_Editor_Outline)
- Revision: `4969`
- Source update: `2020-08-23T19:59:56Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

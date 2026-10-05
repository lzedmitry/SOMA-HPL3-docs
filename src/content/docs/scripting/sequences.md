---
title: Sequences
description: "As you can see, SequenceDoStepAndPause() in there actually pauses the whole sequence until some external event - in this case the callback from the voice playing code - calls SequenceStatesResume() and asks it to continu"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Sequences"
sourceRevision: 4325
sourceUpdated: "2020-08-14T11:23:41Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

As you can see, `Sequence_DoStepAndPause()` in there actually pauses the whole sequence until some external event - in this case the callback from the voice playing code - calls `SequenceStates_Resume()` and asks it to continue.

To start the sequence, you just call the sequence function once with an empty argument when you want it to trigger:
```
Sequence_Alert("");
```
No need to call it every frame or anything! Once started, timers will automatically make sure that the sequence steps get followed when they need to be.

:::tip[Tip]
Since sequences are totally independent of each other, you could run multiple sequences in parallel.
:::

## See Also
*[Sequences Helper](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Sequences_Helper) - SOMA
*[Sequences Helper](https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Scripting/Sequences_Helper) - Amnesia: Rebirth

HPL3/Scripting/Scripting_Guide/Timers|Timers|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting_Guide/Local and Global Variables|Local and Global Variables

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Sequences](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Sequences)
- Revision: `4325`
- Source update: `2020-08-14T11:23:41Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

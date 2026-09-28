---
title: Timers
description: "If you will execute this code, the player will jump very high after five seconds once the map has been loaded."
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Timers"
sourceRevision: 4320
sourceUpdated: "2020-08-14T10:52:48Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

### Breakdown
*We called the function and gave it three arguments: The internal name of the timer (`JumpVeryHigh`), the time in seconds (`5`) of the timer, and the function callback which will be called once the timer is done (`Timer_JumpVeryHigh`).
*Our timer callback is called `Timer_JumpVeryHigh` and has one parameter called `asTimer` - this is the internal name of the timer. In our case, the internal name will be `JumpVeryHigh`.
*Inside the timer callback, we use our helper function which makes the player jump very high.

If you will execute this code, the player will jump very high after five seconds once the map has been loaded.

:::note[Note]
You can have much more controls on timers than what was explained here. For a list of the full functions, check the Map Helper page of SOMA or Amnesia: Rebirth.
:::

Timers are very easy to use as you can see, and it will help us to understand the concept of Sequences in next chapter.

## See Also
*[Map Helper](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Map_Helper) - SOMA
*[Map Helper](https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Scripting/Map_Helper) - Amnesia: Rebirth

HPL3/Scripting/Scripting_Guide/The Update method|The Update method|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting_Guide/Sequences|Sequences

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Timers](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Timers)
- Revision: `4320`
- Source update: `2020-08-14T10:52:48Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

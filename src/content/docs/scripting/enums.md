---
title: Enums
description: "The following example demonstrates use of enum variable:"
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Enums"
sourceRevision: 4636
sourceUpdated: "2020-08-16T19:40:49Z"
lastSynced: "2026-09-28T13:28:41Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
|   |   |
| --- | --- |

## Using Enums
The following example demonstrates use of `enum` variable:
```
enum WeekDay
{
   Day_Sun,
   Day_Mon, 
   Day_Tue,
   Day_Wed,
   Day_Thu,
   Day_Fri,
   Day_Sat
}

//--------------------------------------------------

class cScrMap : iScrMap
{
	////////////////////////////
	// Run first time starting map
	void OnStart()
	{
		WeekDay currentDay = Day_Mon;
		cLux_AddDebugMessage("The current day is: " + currentDay);
	}
```

When the above code is run, the number 1 will be printed to the screen, because the internal value of `Day_Mon` is 1.
### In HPL3
Enums are mostly required as a parameter for existing HPL3 functions. One of the most common function which uses an enum is `Music_Play`. For example:
```
Music_Play("MyMusicFile.ogg", 1.0f, false, eMusicPrio_BgAmb);
```

The last parameter, `eMusicPrio_BgAmb`, is a value of the enum `eMusicPrio`. 

## See Also
- [Enums - AngelScript](/scripting/angelscript/chapter-9-miscellaneous-angelscript-features/#enums)

HPL3/Scripting/Scripting_Guide/Local and Global Variables|Local and Global Variables|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting_Guide/Conclusion - Basic|Conclusion

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Enums](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Enums)
- Revision: `4636`
- Source update: `2020-08-16T19:40:49Z`
- Last synced: `2026-09-28T13:28:41Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

---
title: Scripting Workflow and Structure
description: This article describes the scripting workflow in HPL3 and the basic structure of a map script file.
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Scripting_Workflow_and_Structure"
sourceRevision: 5502
sourceUpdated: "2020-11-07T13:05:31Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
This article describes the scripting workflow in HPL3 and the basic structure of a map script file.

## Introduction
A level script should not be thought of as a file for programming. A level script should be written and read as though it is a story, or a sequence of events if you wish. In the level script you are crafting the experience for the user and the script should be read as the manuscript of that experience.

:::note[Note]
If the level script file contains rows of code that does not match the above description, then the rows of code does not belong in the level script, they belong in a [helper file](https://wiki.frictionalgames.com/page/HPL3/Scripting/Helper_Files) or even deeper down in the hierarchy of script files.
:::

The game has been made to provide feedback during the scripting process relay information as frequently as possible. 

## Scripting Workflow
When running the game / mod from the developer menu, the script will be reloaded every time you task-switch from CodeLite to any other editor. 

When making smaller changes in code that are constantly updated, then simply task switch to see your new code in action.

Inside the developer debug menu, you can also turn on `[Reload Script Constantly](/modding/developer-debug-menu/#reload_script_constantly)` which checks for script updates as soon as you save the code. It can be useful if you have two monitors and such, or if you want a very fast feedback loop.
If there are any updates that require the map to restart, meaning any initialization or properties in the map, then you of course need to reload by pressing F5.

## Scripting Structure
The editor generates a new script file when saving a new map. Expand the box to view the script file.
{{expandBox|

```
#include "interfaces/Map_Interface.hps"
#include "base/Inputhandler_Types.hps"

#include "helpers/helper_map.hps"
#include "helpers/helper_props.hps"
#include "helpers/helper_effects.hps"
#include "helpers/helper_audio.hps"
#include "helpers/helper_imgui.hps"
#include "helpers/helper_sequences.hps"
#include "helpers/helper_game.hps"
#include "helpers/helper_modules.hps"
#include "helpers/helper_ai.hps"

//--------------------------------------------------
/*Place any global values here. These must be const variables as they will not be saved*/
/*This is also the place for enums and classes, but these should be avoided whenever possible*/
//--------------------------------------------------

class cScrMap : iScrMap
{
    //--------------------------------------------
    //////////////////////////////////////////////////////////////////////////////////////////
    // ==============
    // MAIN CALLBACKS
    // ==============
    //{///////////////////////////////////////////////////////////////////////////////////////
    //-------------------------------------------------------
    ////////////////////////////
    // Set up map environment
    void Setup() {}

    //-------------------------------------------------------

    ////////////////////////////
    // Run first time starting map
    void OnStart() {}

    //-------------------------------------------------------

    ////////////////////////////
    // Run when entering map
    void OnEnter() {}

    //-------------------------------------------------------

    ////////////////////////////
    // Run when leaving map
    void OnLeave() {}

    //-------------------------------------------------------

    ////////////////////////////
    // The player has died.
    void OnPlayerKilled(int alRecentDeaths, const tString&in asSource) {}

    //-------------------------------------------------------

    ////////////////////////////
    // To get when player makes input (mostly used for debug)
    void OnAction(int alAction, bool abPressed) {}

    //-------------------------------------------------------

    ////////////////////////////
    // This only used for pure debug purposes when info needs to printed.
    float DrawDebugOutput(cGuiSet @apSet,iFontData @apFont,float afY) { return afY; }
    
    //-------------------------------------------------------
    //} END MAIN CALLBACKS
    //////////////////////////////////////////////////////////////////////////////////////////
    // ==============
    // MAIN FUNCTIONS
    // ==============
    //{///////////////////////////////////////////////////////////////////////////////////////
    //-------------------------------------------------------
    /*Put any variables that are used in more than one scene here.*/
    //-------------------------------------------------------
    /*Put any functions that are used in more than one scene here.*/
    //-------------------------------------------------------
    //} END MAIN FUNCTIONS
    //////////////////////////////////////////////////////////////////////////////////////////
    // ==============
    // SCENE X *NAME OF SCENE*
    // ==============
    //{//////////////////////////////////////////////////////////////////////////////////////
         /////////////////////////////////////////
         // General
         //{//////////////////////////////////////

        //-------------------------------------------------------

        /*Put any variables that are used by many events in Scene X here.*/

        //-------------------------------------------------------

        /*Put any functions that are used in more than one event in Scene X here.*/

        //-------------------------------------------------------

        //} END General

         /////////////////////////////////////////
         // Event *Name Of Event*
         //{//////////////////////////////////////

         //-------------------------------------------------------

         /*Put any variables that are only used in Scene X, Event X here.*/

         //-------------------------------------------------------

         /*Put any functions that are only used in Scene X, Event X here.*/

         //-------------------------------------------------------

         //} END Event *Name Of Event*

     //} END SCENE X
}
```

}} 

For now, let's have a quick look of the overall structure of the file, from top to bottom. 

*Includes section
*Class declaration
*Main functions
*Types and variables
*Callback functions and comments

Since your code can get quite big, it is important that the same structure is maintained. This way it makes it easier for you and others to find what they need to do to change something, and this is what comments are for.

Anything that has been marked as a comment is ignored by the game, so you can type in whatever you want without worrying that it will screw up the program.

## See Also
*[Developer Debug Menu](/modding/developer-debug-menu/)
*[Level Scripting - Best Practices](/scripting/level-scripting-best-practices/)

HPL3/Scripting/Scripting_Guide/Setting up CodeLite|Setting up CodeLite|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting_Guide/Hello World|Hello World

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Scripting Workflow and Structure](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Scripting_Workflow_and_Structure)
- Revision: `5502`
- Source update: `2020-11-07T13:05:31Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

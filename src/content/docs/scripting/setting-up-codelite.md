---
title: Setting up CodeLite
description: This is a quick guide on how to set-up the third party scripting tool - CodeLite.
category: scripting
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Setting_up_CodeLite"
sourceRevision: 4361
sourceUpdated: "2020-08-14T23:42:41Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - scripting
---
This is a quick guide on how to set-up the third party scripting tool - CodeLite.
## CodeLite - Introduction
As mentioned, scripting in HPL3 can look a lot like regular programming, but less complicated.

Because of that, we need tools that will be able to aid us when we write our code. For HPL2, Notepad++ or even Notepad were enough for that. This time around, something more powerful is needed.

CodeLite is very much like a text editor, but much more programming-oriented than Notepad++. It is the tool used officially by Frictional Games to develop their HPL3 games. Here are some of the relevant features of CodeLite:

***Code documentation on the fly**
***Code autocompletion and smart code suggestion**
***Fast and easy way to navitgate through large script files**
***The ability to run the game from CodeLite**

For the scripting guide, CodeLite 12.0.0 will be used, which is the latest stable release that can work with HPL3 without any errors or bugs. 

> **Figure (original Wiki file, not inlined):** [Codelite-window.png](https://wiki.frictionalgames.com/page/File:Codelite-window.png)
 

## Setting-up CodeLite
This section explains how to configure CodeLite so it can be suitable for HPL3 scripting, how to create a workspace and a project, and how to import the script files.

:::note[Note]
You must install CodeLite on the same disk as the game you want to mod. For example, if Amnesia: Rebirth is installed on disk C:, you have to install CodeLite on C: as well.
:::

#[Download the optimized color theme](https://wiki.frictionalgames.com/page/CodeLite#Optimized_Color_Theme)
#[Download and install CodeLite version 12.0.0.](https://downloads.codelite.org/ReleaseArchive.php)
#**Launch CodeLite and configure:**
##`Settings → Code Completion → General`:
##*Add `;*.hps` at the end of the `Additional file extensions to parse` list.
##*Enable `Keep function signature un-formatted.`
##*Enable  `Re-parse on workspace loaded`.
##`Settings → Code Completion → Colouring`: Enable `Apply context aware colouring`.
##`Settings → Code Completion → CTags → Search Paths`: Click `Add...`, navigate to the game folder and select the `script` folder.
##`Settings → Colours and Fonts...`: Click on `Import settings from a zip archive` and select the `CodeLiteColorSettings.zip` file.
##Configure the rest of CodeLite to your liking.
#**Create a new workspace:** Create a folder inside your game directory and name it `_src`. Go to the `Workspace` menu and click on `New Workspace...`. Save the workspace inside the `_src` folder.
#**Create a new project:** `Right click on the workspace → New → New Project`. Select `Others → Non-code project`. Give the project a name (For example: "soma"). Leave the rest as default.
#**Add a folder to the project:** Right-click on the project and choose `New Virtual Folder`. Name it `_api`.
#**Add the game script files:** 
##Right-click on `_api → Add An Existing File...`, add the file `hps_api.hps` from the game folder (If the file does not appear in your game folder, launch the game, and the file will appear).
##Right-click on the project and choose `Import Files From Directory`. Navigate to the game folder and select it. In the next window, check the boxes for the folders: `maps, script, mods` and click ok.

**Lastly, go to `Workspace` and click on `Parse Workspace`.**

That should be it, you should now have three top folders in your project and a lot of sub-folders with various script files.
Start typing something, for example `Entity_` and a list should appear showing all the functions that begin with `Entity_` and the documentation for each selected function.

:::note[Note]
If the list disappears, you can make it re-appear again by pressing `ctrl-space`. If you want to bring up hints when inside the () of a function, press `ctrl-shift-space`.
:::

  

:::caution[Caution]
CodeLite won't update automatically the location of workspace files. If you moved them outside of CodeLite, you will need to re-add  them. The same goes for creating new file after setting up a workspace
:::

## Launching the Game From CodeLite
One additional thing you can do is to launch the game or your mod in dev mode through CodeLite itself. 

To do this, right click on your project and go to settings. Then Click on `Customize → Custom Build`.
Turn on `Enable Custom Build`. In the working directory, select the game folder.

Now you will need to add the command that launches the game or the mod. For example, a command that launches the main game of SOMA in dev mode will look like this:

```
Soma.exe -user Dev -cfg config/main_init_dev.cfg
```

Add the command to the `Build` section in the table.

> **Figure (original Wiki file, not inlined):** [Codelite custom build.png](https://wiki.frictionalgames.com/page/File:Codelite_custom_build.png)
 

For more information about available commands, visit the [Developer Commands](/modding/developer-commands/) article.

**Now, all you need to do is to press F7, and the game will run!**

## Issues & Info
*Write `Class@ object`  and not `Class @object`, the latter will screw up coloring.
*If you lose coloring / code completion and can't get it back, re-parse the workspace: `Parse Workspace`.
*Parameters with `&in` might break the coloring of function parameters, but will have no other side-effects.

HPL3/Scripting/Scripting_Guide/What is scripting in HPL3?|What is scripting in HPL3?|HPL3/Scripting/HPL3 Scripting Guide|HPL3 Scripting Guide|HPL3/Scripting/Scripting_Guide/Scripting Workflow and Structure|Scripting Workflow and Structure

## Source & attribution

- Original Frictional Wiki page: [HPL3/Scripting/Scripting Guide/Setting up CodeLite](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Setting_up_CodeLite)
- Revision: `4361`
- Source update: `2020-08-14T23:42:41Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

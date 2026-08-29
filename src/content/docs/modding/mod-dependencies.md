---
title: Mod Dependencies
description: "Mod dependencies provide a solution for sharing mod contents across multiple other mods. A few mods could depend on a parent mod to derive assets and other content from, instead of including it in their own mod."
category: modding
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Modding/Mod_Dependencies"
sourceRevision: 7033
sourceUpdated: "2026-03-14T21:56:05Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - modding
---
Mod dependencies provide a solution for sharing mod contents across multiple other mods. A few mods could depend on a parent mod to derive assets and other content from, instead of including it in their own mod.

  
Mod dependencies are currently broken in Amnesia: Rebirth and Soma. They work for Amnesia: The Bunker

## When to Use Mod Dependencies
*The main occasion to use Mod Dependencies is when you want to distribute assets packs which include models, textures, materials, scripts, etc for people to use freely in their own mods.
*Mod dependencies can help to reduce the mod size you want to distribute, as a big portion of the assets themselves are not actually included in the mod, but come from an external source.

> **Figure (original Wiki file, not inlined):** [Mod-dependencies-diagarm.png](https://wiki.frictionalgames.com/page/File:Mod-dependencies-diagarm.png)

:::note[Note]
The level editor will be able to pick on mod dependencies and will load the assets if there are any.
:::

## Setting Up a Mod Dependency
In order to turn a regular mod into a mod dependency, the mod's [entry file](/modding/creating-a-mod/#mod_entry_file) needs to have a special attribute called `UID`. This is used so other mods can reference your mod as a dependency. The convention of naming a UID is the form `provider_name.mod_name`. For example, if the mod creator is named `steve` and the mod name is called `Castle Assets Pack`, the `UID` for the mod will be `steve.castle_assets_pack`. 

In order to set a `UID` manually for a mod:

#Open the mod's entry [entry file](/modding/creating-a-mod/#mod_entry_file).
#Inside, add an attribute called `UID` and give it a name:
```
<?xml version="1.0" encoding="UTF-8"?>
<Content Version="1.0"
	Type="StandAlone"
	Title="Your mod name here"
	Author="Your name here"
	Description="Mod description here"
    
    UID="my_uid"
	
	LauncherPic="LauncherPic.png"
	InitCfg="config/main_init.cfg"
/>
```

Now you can use the mod as a dependency for other mods.

If your dependency has custom modules, it is recommended to not include `modules.cfg` and `ModuleInterfaces_Custom.hps`. Instead have the mod which uses the dependency include the necessary changes to those files within itself.
Having those files both inside the dependency and the mod that uses it could cause errors. 

:::note[Note]
Your dependency can have dependencies of its own as well.
:::

## Using a Mod Dependency
In order to use a mod dependency, the [entry file](/modding/creating-a-mod/#mod_entry_file) of the mod which uses the dependency needs to have a special attribute called `Dependencies`. It is a list of `UIDs` separated by commas.

In order to set `Dependencies` manually for a mod:

#Open the entry [entry file](/modding/creating-a-mod/#mod_entry_file) of the mod you want to add a dependency to.
#Inside, add an attribute called `Dependencies` and list the `UID`(s): 
```
<?xml version="1.0" encoding="UTF-8"?>
<Content Version="1.0"
	Type="StandAlone"
	Title="Your mod name here"
	Author="Your name here"
	Description="Mod description here"
    
    Dependencies="my_uid"
	
	LauncherPic="LauncherPic.png"
	InitCfg="config/main_init.cfg"
/>
```

Now your mod loads the mod dependency with the `UID` of "`my_uid`".

## See Also
*[Creating a Mod](/modding/creating-a-mod/)
*[Resources Configuration](/generated/resources-configuration/)

## Source & attribution

- Original Frictional Wiki page: [HPL3/Modding/Mod Dependencies](https://wiki.frictionalgames.com/page/HPL3/Modding/Mod_Dependencies)
- Revision: `7033`
- Source update: `2026-03-14T21:56:05Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

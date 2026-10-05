---
title: Setup Modding Environment
description: "In order to have a smooth modding development experience, SOMA is needed to be configured into proper development environment."
category: modding
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/SOMA/Modding/Setup_Modding_Environment"
sourceRevision: 6808
sourceUpdated: "2024-05-08T16:54:34Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - modding
---
In order to have a smooth modding development experience, SOMA is needed to be configured into proper development environment.

:::note[Note]
Each section described in this article can either be configured manually (creating or editing the files yourself) or to be configured automatically, using the SOMA Mod Manager application.
:::

## Setting up the Editors
Your mod might have custom assets. In order to make the editors (Level Editor, Model Editor, etc) to load your mod's assets, it needs to be configured into a special mode called "WIP Mod". 

:::tip[Tip]
Even if your mod doesn't have any custom assets, it's a good practice to configure the Level Editor anyway, just so you won't have to deal with it in the future should you decide to add custom assets.
:::
 

### WIP Mod - Manual Configuration
#Navigate to `My Documents/HPL3`. You need to open one of the editors at least once in order to see the HPL3 folder inside your document folder.
#Inside that folder, create a file called `WIPMod.cfg`.
#Paste the following into the file, and save:

```
<WIPmod Path="Full_Path_To_Mod/entry.hpc" />
```

(Of course, you will have to change the path in order to suit your own location of the mod).

### WIP Mod - Automatic Configuration
You can use the [HPL3 Mod Manager](/tools/hpl3-mod-manager/) in order to perform an automatic sync of the editors to your mod, which pretty much does the manual step for you.

### Final Step
If your mod indeed has custom assets, you need to make sure the editors can add them to their look up list. 

#In your mod's folder, create a new folder and name it `editor`.
#Inside that folder, create a file called `lookupdirs.cfg`.
#Create a new `<Directories>` xml tag inside the file.
#Add a list of directories which include your custom assets. The directory has to be associated with a category. The allowed categories are:
#*`StaticObjects`
#*`Entities`
#*`Billboards`
#*`Particles`
#*`Sounds`
#*`DetailMeshes`

Example file:

```
<Directories>
	<Dir Category="StaticObjects" Path="static_objects/" />
	<Dir Category="Entities" Path="entities/" />
	<Dir Category="Billboards" Path="billboards/" />
	<Dir Category="Particles" Path="particles/" />
	<Dir Category="Sounds" Path="sounds/" />
</Directories>
```

If all the above is done correctly, a `(Working on mod)` text should appear on the title bar of HPL3 editors when run.

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Modding/Setup Modding Environment](https://wiki.frictionalgames.com/page/HPL3/SOMA/Modding/Setup_Modding_Environment)
- Revision: `6808`
- Source update: `2024-05-08T16:54:34Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

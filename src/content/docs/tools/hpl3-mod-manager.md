---
title: HPL3 Mod Manager
description: This page details third-party software which is not affiliated with Frictional Games.
category: tools
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Third_Party_Tools/HPL3_Mod_Manager"
sourceRevision: 7034
sourceUpdated: "2026-04-24T11:30:15Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - tools
---
> **Figure (original Wiki file, not inlined):** [The HPL3 Mod Manager](https://wiki.frictionalgames.com/page/File:Hpl3_mod_manager.png)

:::note[Note]
This page details third-party software which is not affiliated with Frictional Games.
:::

  

:::note[Note]
This application is open source. View the repository on [GitLab](https://gitlab.com/TiManGames/hpl3-mod-configurator).
:::

The HPL3 Mod Manager is an application intended to make it easier to manage and configure *HPL3*  mods. It removes the need to manually tamper with configuration files and keeps everything in one place so that it can be easily modified.

**Features:**

*Seamlessly support all HPL3 Games: SOMA, Amnesia: Rebirth, and Amnesia: The Bunker.
*Automatically scan your game folder for mods and effortlessly load them into the manager.

*Add or create new [mod entries](https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Modding/Creating_a_Mod#Mod_Entry_File).
*Edit mod information: Name, Author, Description, Thumbnail Photo, Mod Type, and Hot Load (Bunker only).
*Manage [mod resources](/generated/resources-configuration/) and [mod dependencies](/modding/mod-dependencies/).
*[Sync your mod](https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Modding/Setup_Modding_Environment) to the Level Editor: If your mod has any custom assets, the level editor will automatically load it after it's synced.
*Create a [custom .dev launch file](https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Modding/Creating_a_Mod) that will load your mod with your custom scripts and assets

## Download
:::note[Note]
This application requires a modern Java Runtime. Ensure you have the latest version installed, or simply download the installer exe.
:::

| Application | Upload Date | SHA | VirusTotal |
| --- | --- | --- | --- |
| [Hpl3ModManagerSetup.exe](https://mega.nz/file/KkoFxAKB#z5pRO1Lt0TZZwG0gkZKed8PUrls43xBIwz4iP8_mBV8) | 8 June, 2023 | 8ac8d373835469e83b31f9c6dc9dfc6bf15283ba4d15049e5edec2de5c95dc12 | [Results](https://www.virustotal.com/gui/file/8ac8d373835469e83b31f9c6dc9dfc6bf15283ba4d15049e5edec2de5c95dc12/detection) |

The application can be run from anywhere on your computer, but it is recommended to place it in the main game folder.

=Mod Manager Guide=

## Installation and first run
1. Download the Mod Manager from this page.
1. Place it somewhere convenient (for example inside the game’s root folder).
1. Make sure the game folder has a `mods` directory. Create it if it does not exist.
1. Run `HPL3 Mod Manager`.

### Game Directory field
At the top left:

- Click the `...` button and select the **game root folder** (where the main game executable is).
- When set, the Mod Manager scans `<GameDir>\mods\` and populates the **Mod List** with any folder that contains an `entry.hpc`.

To switch between SOMA, Rebirth and The Bunker, change the **Game Directory**.  
The **Mod List** will refresh for the selected game.

---

## Main window layout
### Left pane: Game & Mod list
- **Game Directory** – absolute path to the current game.
- **Mod List** – all detected mods under `mods/`. Columns:
  - **Name** – mod title.
  - **Type** – usually `STANDALONE`.
- Bottom buttons:
  - **Load Mod** – manually load a mod from a folder.
  - **New Mod** – create a new mod entry.
  - **Open Mod Folder** – open the folder of the currently selected mod.
  - **Remove Mod** – remove the selected mod from the list (does not delete files).

### Right pane: Mod information
For the selected mod:

- **Mod Directory** – absolute path to this mod’s folder (under `mods/`).
- **Name** – display name of the mod.
- **Author**
- **Description**
- **Thumbnail** – image used by the launcher (usually a PNG in the mod folder).
- **Dependencies**
  - Button: **Manage Dependencies…** – opens dependency dialog.
- **Resources**
  - Button: **Manage Resources…** – opens resources and editor look‐up dialog.
- **Mod Type**
  - Dropdown – typically `StandAlone`.
- **Hot Load** (The Bunker only)
  - Special flag used by The Bunker. Leave disabled unless you know you need it.
- Bottom buttons:
  - **Create dev .bat**
  - **Sync Editor**
  - **Save**

Typical workflow:

1. Select a mod in the **Mod List**.
1. Change settings in **Mod information**.
1. Press **Save** to write changes to disk.

---

## Creating a new mod
Use this for a brand new mod/custom story.

1. Set **Game Directory** to the game you are targeting.
1. Click **New Mod**.
1. In the **Mod information** panel:
  1. Click `...` next to **Mod Directory**.
  1. Choose a **new folder inside `mods`** (for example: `...\Amnesia The Bunker\mods\my_mod`).
    1. The folder name is used by the game in `-mod local:my_mod`.
  1. Fill in **Name**, **Author** and **Description**.
  1. Choose a **Thumbnail** (for example a PNG image stored in the mod folder).
  1. Set **Mod Type** to `StandAlone`.
  1. For The Bunker, leave **Hot Load** unchecked unless a specific guide instructs otherwise.
1. Click **Save**.

The manager now creates a basic `entry.hpc` for the mod.  
You still need to create the usual mod structure (e.g. `config/`, `maps/`, `script/`, etc.) exactly as for a manually created mod.

---

## Importing an existing mod
If you already have a mod:

1. Place the mod folder under `<GameDir>\mods\`.
1. If it is not automatically listed:
  1. Click **Load Mod**.
  1. Select the folder that contains `entry.hpc`.
1. The mod now appears in the **Mod List** and can be edited like any other mod.

---

## Editing mod metadata (entry.hpc)
The fields in the **Mod information** panel map directly to attributes in `entry.hpc`:

- **Name** → `Title`
- **Author** → `Author`
- **Description** → language-specific description fields (e.g. `Description_english`)
- **Thumbnail** → path to the launcher image file (relative to the mod root)
- **Mod Type** → `Type` (commonly `StandAlone`)
- **Hot Load** → The Bunker specific attribute
- The manager also assumes a default init config (for example `config/main_init.cfg`) that follows the standard mod templates.

Pressing **Save** updates `entry.hpc` with the values from the UI.

---

## Managing dependencies
The **Manage Dependencies…** button opens the dependency dialog.  
This dialog edits two things in `entry.hpc`:

- The mod’s own UID.
- The list of dependency UIDs.

Note: At the engine level, mod dependencies are currently only functional in **Amnesia: The Bunker**. In SOMA and Amnesia: Rebirth the dependency feature is broken, so do not rely on it there.

### Mod UID
- **Mod UID** field – defines the mod’s unique identifier (`UID`).
- Naming convention: `authorname.mod_name` (for example `frictionalgames.standardmode`).

Pick something that is globally unique.  
Once other mods depend on this UID, you should not change it.

### Adding dependencies
To add dependencies:

1. In the dependency dialog click **Add**.
1. Enter the UID of the mod you depend on (exactly as written in that mod’s UID field).
1. Repeat for additional dependencies.
1. Click **Save** in the dependency dialog.
1. Click **Save** again in the main window.

The manager will write something of the form:

```
<Content
    UID="your.uid"
    Dependencies="other.uid,another.uid">
    ...
</Content>
```

---

## Managing resources
Click **Manage Resources…** to open the Mod Resources dialog.  
This dialog controls:

- The mod’s **runtime resources list** (`resources.cfg`).
- The **editor lookup directories** (`editor/lookupdirs.cfg`).

### Mod Resources table (resources.cfg)
The upper table corresponds to `<Directory>` elements in `resources.cfg`.

Typical setup:

1. Click **Add** for each directory you want the game to load resources from.
1. Use paths starting with `/` relative to the mod folder, for example:
  1. `/config`
  1. `/maps`
  1. `/script`
  1. `/static_objects`
1. The manager will create the corresponding `<Directory>` entries and typically sets `AddSubDirs="true"`.
1. Click **Save** in the dialog, then **Save** in the main window.

Resulting `resources.cfg` will be similar to:

```
<Resources>
    <Directory Path="/config"         AddSubDirs="true" />
    <Directory Path="/maps"           AddSubDirs="true" />
    <Directory Path="/script"         AddSubDirs="true" />
    <Directory Path="/static_objects" AddSubDirs="true" />
</Resources>
```

Adjust paths to match your own folder structure.

### Editor Resources (lookupdirs.cfg)
The lower part of the dialog configures the Editor lookup directories.  
Each checkbox + text field pair maps to a category in `editor/lookupdirs.cfg`.

For each type of asset your mod uses:

- Tick the relevant checkbox:
  - **Static Objects**
  - **Entities**
  - **Billboards**
  - **Particles**
  - **Sounds**
- Enter the relative directory where those assets live, for example:
  - `static_objects/`
  - `entities/`
  - `billboards/`
  - `particles/`
  - `sounds/`

The manager will create entries like:

```
<Directories>
    <Dir Category="StaticObjects" Path="static_objects/" />
    <Dir Category="Entities"      Path="entities/" />
    <Dir Category="Billboards"    Path="billboards/" />
    <Dir Category="Particles"     Path="particles/" />
    <Dir Category="Sounds"        Path="sounds/" />
</Directories>
```

Click **Save** in the resources dialog, then **Save** again in the main window.

---

## Sync Editor (WIP mod setup)
The **Sync Editor** button sets up the mod as the current “WIP mod” for the editors and updates the lookup directories.

Normally this requires manually:

- Creating `My Documents/HPL3/WIPMod.cfg` with a path to the mod’s `entry.hpc`.
- Creating or editing `editor/lookupdirs.cfg` in the mod folder.

With the Mod Manager:

1. Configure your **Mod Resources** and **Editor Resources** as described above.
1. Select your mod in the **Mod List**.
1. Click **Sync Editor**.

The manager then:

- Writes `WIPMod.cfg` in the user’s documents folder so the editors work on this mod.
- Writes/updates `editor/lookupdirs.cfg` using the Editor Resources you configured.

After this, opening the Level Editor should indicate that it is working on your mod and your custom assets should appear in the browser.

---

## Create dev .bat
The recommended dev workflow is to run the game executable with parameters such as:

- `-mod local:<mod_folder_name>`
- `-user Dev`
- Possibly a dev init config (for example `-cfg config/main_init_dev.cfg`)

Instead of writing a batch file by hand:

1. Select your mod in the **Mod List**.
1. Click **Create dev .bat**.

The manager generates a `.bat` file in the game directory that:

- Launches the correct game executable.
- Passes the appropriate `-mod local:<YourModFolder>` argument.
- Adds dev-related arguments according to the recommended setup.

Use that batch file whenever you want to test the mod with dev options enabled.

---

## Game-specific notes
### SOMA
- Same Mod Manager workflow.
- No use for Bunker-specific options like Hot Load.

### Amnesia: Rebirth
- Standalone mods only.
- The engine’s mod dependency system is currently broken; do not rely on dependencies for Rebirth mods.

### Amnesia: The Bunker
- Mod dependencies are supported and functional.
- For simple custom stories, keep **Hot Load** disabled unless you have a specific reason or guide instructing you to enable it.

---

## Source & attribution

- Original Frictional Wiki page: [HPL3/Third Party Tools/HPL3 Mod Manager](https://wiki.frictionalgames.com/page/HPL3/Third_Party_Tools/HPL3_Mod_Manager)
- Revision: `7034`
- Source update: `2026-04-24T11:30:15Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

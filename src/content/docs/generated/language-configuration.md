---
title: Language Configuration
description: "When displaying any kind of text on the screen (For example, when picking up a note and reading it), the mod refers to a file in which that text information is stored in. That file is called a language file. Each languag"
category: generated
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Language_Configuration"
sourceRevision: 5481
sourceUpdated: "2020-11-06T20:34:44Z"
lastSynced: "2026-08-28T18:40:04Z"
sourceStatus: verified
generated: true
tags:
  - generated
sidebar:
  hidden: true
---
:::caution[SOURCE STATUS: WIP]
This source page is marked as undergoing editing on the Frictional Wiki.
:::

When displaying any kind of text on the screen (For example, when picking up a note and reading it), the mod refers to a file in which that text information is stored in. That file is called a **language file**. Each language has their own language files. For example, if your mod has English and Czech translations, you will have separate English and Czech language files.
:::note[Note]
Not every mod requires a language file. Only if your mod has notes, messages, translations and so on, it should have its own language file.
:::

## Setting Up Language Files
When configuring a language for a mod, you need to have two separate files: a base language file, and a main language file. For example, if your mod has English and Czech languages, you will have 4 language files in total. A language file's extension ends with `.lang`

The content of a language files is divided into **categories**, each category holds language **entries**. A language entry holds the actual text information. The following is an example of a simple language file:
```
<LANGUAGE>
      <Category Name="HelloWorld">
           <Entry Name="HelloWorld">Hello World!</Entry>
      </Category >
</LANGUAGE>
```

| Attribute | Description |
| --- | --- |
| LANGUAGE | Each language file begins and closes with a `<LANGUAGE>` tag. |
| Category | A language category. Inside, all of the language entries will be listed. |
| Category Name | A category must have an internal name so it can be picked up by the game script and read data from. |
| Entry | A language entry tag. This holds the actual text information `Hello World!` |
| Entry Name | The name of the entry. Each entry needs to have a name attribute so the game will be able to read the text from it. |

:::tip[Tip]
Look at the structure of the main game's language files and try to mimic that in your own language file. There is no need to guess how to properly structure it if the main game already offers a solution for that.
:::

### Base Language File
The base language file holds text related to the main menu, key configuration, and general menu messages. It has a prefix `base_` in the name. For example, a base English language file will be named like this: `base_english.lang`.

**The file should be located inside the mod's `config` folder, unless specified otherwise in the [Launch Configuration file](/generated/launch-configuration/).**

:::note[Note]
Unless you are going to have a custom menu, or going to add new input keys to your mod, there is no need for your mod to have a base language file.
:::

### Main Language File
The main language file holds text related to in-game readables (such as notes), level names, game hints, item descriptions, etc. The name of file depends on the language it refers to. For example, an main English language file will be named like this: `english.lang`.

**The file should be located inside the mod's `config/lang` folder, unless specified otherwise in the [Launch Configuration file](/generated/launch-configuration/).**

### Overriding Existing Language File Categories
It is possible to override the main game's language categories and entries. It is useful if you want to change default values for certain text, or if you want to add new entries to a category. To override a main game language category simply create the same category in your own language file.

:::note[Note]
If you do not need to change the content of a certain category in your language file, do not copy it.
:::

#### Example
*Main game `english.lang` language file:*
```
  <CATEGORY Name="GameOver">
	<Entry Name="DefaultMessage">You died</Entry>
	<Entry Name="PressToContinue">Press any button to try again...</Entry>
  </CATEGORY>
```
*Mod's `english.lang` language file:*
```
  <CATEGORY Name="GameOver">
	<Entry Name="DefaultMessage">You are dead. Not big surprise.</Entry>
	<Entry Name="PressToContinue">press to continue or something idk</Entry>
  </CATEGORY>
```
The game will use our custom `GameOver` category instead of the category from the main game language file, because we override it in our language file.

## Editing Language Files
This is a work in progress section.
The best way to create, edit, and modify language entries and language files, is to use the Language Editor. This editor comes with the game installation and is named `LangEditor.exe`.

### Loading a Language File
### Adding a Language Category
### Adding a Language Entry

## Source & attribution

- Original Frictional Wiki page: [HPL3/Language Configuration](https://wiki.frictionalgames.com/page/HPL3/Language_Configuration)
- Revision: `5481`
- Source update: `2020-11-06T20:34:44Z`
- Last synced: `2026-08-28T18:40:04Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

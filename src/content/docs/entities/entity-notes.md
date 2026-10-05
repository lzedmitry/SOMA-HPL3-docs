---
title: Entity Notes
description: 1. Open the entity in the Model Editor. 1. Open the Notes window. 1. Type the information in its text box. 1. Close the window and save the entity.
category: entities
sourceUrl: "https://wiki.frictionalgames.com/page/HPL3/Entities/Entity_Notes"
sourceRevision: 7343
sourceUpdated: "2026-10-02T17:34:21Z"
lastSynced: "2026-10-05T14:11:59Z"
sourceStatus: verified
generated: true
tags:
  - entities
---
**Entity Notes** are free-form authoring notes attached to an entity file. They are intended for information that another level designer should see when using the entity, rather than for text shown to the player during gameplay.

> **Figure (original Wiki file, not inlined):** [window_entitynotes.png](https://wiki.frictionalgames.com/page/File:window_entitynotes.png)

## Adding a note
1. Open the entity in the Model Editor.
1. Open the **Notes** window.
1. Type the information in its text box.
1. Close the window and save the entity.

No separate confirmation step is required in the Notes window; saving the entity commits the current note along with the rest of the entity data.

Useful notes include setup requirements, intended orientation, required companion objects, known limitations, and warnings about entity variables. Keep them short enough to read while placing the entity.

## Storage
When a note is present, the Model Editor stores it as a top-level element in the `.ent` file:

```
<Notes Content="Place against a wall and align the main body with the floor." />
```

The `Notes` element is separate from `ModelData`, `UserDefinedVariables`, and `EditorSession`. Most shipped entities omit it because they have no authoring note. All three inspected HPL3 Model Editor and Level Editor builds contain support for the `Notes` element and its `Content` field.

In the Level Editor, the note can be read through the entity-notes interface when working with an entity of that type. Entity Notes are therefore documentation for editors; they are not the same as a readable note, journal entry, localization key, or an entity type's gameplay variable named “Note.”

## See also
- [Entity Settings](/entities/entity-settings/)
- [Model Editor View](/entities/model-editor-view/)

## Source & attribution

- Original Frictional Wiki page: [HPL3/Entities/Entity Notes](https://wiki.frictionalgames.com/page/HPL3/Entities/Entity_Notes)
- Revision: `7343`
- Source update: `2026-10-02T17:34:21Z`
- Last synced: `2026-10-05T14:11:59Z`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. Content is derived from the [Frictional Wiki](https://wiki.frictionalgames.com/page/HPL3/SOMA). See [Licensing](/about/licensing/).

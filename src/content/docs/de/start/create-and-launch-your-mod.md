---
title: "Mod anlegen und starten"
description: "Kopieren Sie das funktionierende SOMA-Beispiel und starten Sie die Kopie, bevor Sie etwas ändern."
category: start
sourceStatus: verified
translation:
  locale: de
  sourceLocale: en
  sourceRevision: 1
  translationRevision: 1
  status: current
---

In diesem Schritt kopieren Sie das funktionierende SOMA-Beispiel und starten die Kopie, **bevor** Sie etwas ändern.

## Eigene Kopie anlegen
1. Öffnen Sie `SOMA/mods/`.
1. Kopieren Sie den gesamten Ordner `MinimalCustomMapMod`.
1. Benennen Sie die Kopie in einen kurzen Projektnamen um, z. B. `MyFirstMod`.
1. Öffnen Sie die kopierte `entry.hpc` in einem Texteditor.
1. Ändern Sie mindestens `Title`, `Author` und `Description`. Lassen Sie `Type="StandAlone"` und `InitCfg="config/main_init.cfg"` für dieses Tutorial unverändert.

:::caution[Caution]
Original `MinimalCustomMapMod` nicht umbenennen oder editieren. Eine saubere Kopie ist der Vergleich, wenn die Konfiguration später bricht.
:::

Der kopierte Ordner muss mindestens enthalten:

```
MyFirstMod/
├── config/
│   ├── lang/
│   │   └── english.lang
│   └── main_init.cfg
├── maps/
│   └── sample_map/
│       ├── sample_map.hpm
│       ├── sample_map.hpm_*
│       └── sample_map.hps
├── entry.hpc
├── LauncherPic.png
└── resources.cfg
```

Die `.hpm_*`-Einträge sind die geteilten Map-Daten. Sie gehören zur Map und müssen neben `sample_map.hpm` bleiben.

## Unveränderte Kopie starten
1. `ModLauncher.exe` ausführen, oder `ModLauncher_NoSteam.exe` ohne Steam.
1. **Play Custom Content** wählen.
1. Den Title aus `entry.hpc` wählen.
1. Den Mod starten.

Die mitgelieferte `config/main_init.cfg` startet `sample_map.hpm` aus `maps/` bei `PlayerStartArea_1`.

## Checkpoint
Erst weiter, wenn der kopierte Mod im Launcher erscheint und seine Sample-Map lädt.

## Wenn es nicht geht
- **Mod fehlt im Launcher:** Kopie liegt in `SOMA/mods/` und hat `entry.hpc` im Root.
- **Spiel startet, Map nicht:** `config/main_init.cfg`, `resources.cfg` und den kompletten Ordner `maps/sample_map/` aus dem sauberen Beispiel wiederherstellen.
- **Dateien verstehen:** [Creating a Mod](/de/modding/creating-a-mod/), [Resources Configuration](/de/generated/resources-configuration/), [Launch Configuration](/de/generated/launch-configuration/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. See [Licensing](/de/about/licensing/).

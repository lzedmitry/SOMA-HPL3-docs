---
title: "Creare e avviare la mod"
description: "Copia l’esempio funzionante di SOMA e avvia la copia prima di modificarla."
category: start
sourceStatus: verified
translation:
  locale: it
  sourceLocale: en
  sourceRevision: 1
  translationRevision: 1
  status: current
---

In questo passo copi l’esempio funzionante di SOMA e avvii la copia **prima** di modificarla.

## Fai la tua copia
1. Apri `SOMA/mods/`.
1. Copia l’intera cartella `MinimalCustomMapMod`.
1. Rinomina la copia con un nome di progetto breve, ad esempio `MyFirstMod`.
1. Apri l’`entry.hpc` copiato in un editor di testo.
1. Cambia almeno `Title`, `Author` e `Description`. Lascia `Type="StandAlone"` e `InitCfg="config/main_init.cfg"` invariati per questo tutorial.

:::caution[Caution]
Non rinominare né modificare l’originale `MinimalCustomMapMod`. Una copia pulita serve da confronto se la configurazione si rompe.
:::

La cartella copiata deve contenere almeno:

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

Le voci `.hpm_*` sono i dati spezzati della mappa. Fanno parte della mappa e devono restare accanto a `sample_map.hpm`.

## Avvia la copia intatta
1. Esegui `ModLauncher.exe`, oppure `ModLauncher_NoSteam.exe` senza Steam.
1. Scegli **Play Custom Content**.
1. Seleziona il title messo in `entry.hpc`.
1. Avvia la mod.

Il `config/main_init.cfg` incluso avvia `sample_map.hpm` da `maps/` in `PlayerStartArea_1`.

## Checkpoint
Continua solo quando la mod copiata compare nel launcher e carica la mappa di esempio.

## Se non funziona
- **La mod manca dal launcher:** la copia è in `SOMA/mods/` e ha `entry.hpc` nella root.
- **Il gioco parte ma la mappa no:** ripristina `config/main_init.cfg`, `resources.cfg` e l’intera cartella `maps/sample_map/` dall’esempio pulito.
- **Capire i file:** [Creating a Mod](/it/modding/creating-a-mod/), [Resources Configuration](/it/generated/resources-configuration/), [Launch Configuration](/it/generated/launch-configuration/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. See [Licensing](/it/about/licensing/).

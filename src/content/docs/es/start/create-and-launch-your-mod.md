---
title: "Crear y lanzar tu mod"
description: "Copia el ejemplo funcional de SOMA y lanza la copia antes de cambiarla."
category: start
sourceStatus: verified
translation:
  locale: es
  sourceLocale: en
  sourceRevision: 1
  translationRevision: 1
  status: current
---

En este paso copias el ejemplo funcional de SOMA y lanzas la copia **antes** de cambiarla.

## Haz tu propia copia
1. Abre `SOMA/mods/`.
1. Copia la carpeta `MinimalCustomMapMod` entera.
1. Renombra la copia con un nombre de proyecto corto, por ejemplo `MyFirstMod`.
1. Abre el `entry.hpc` copiado en un editor de texto.
1. Cambia al menos `Title`, `Author` y `Description`. Deja `Type="StandAlone"` e `InitCfg="config/main_init.cfg"` sin cambios para este tutorial.

:::caution[Caution]
No renombres ni edites el `MinimalCustomMapMod` original. Una copia limpia sirve de comparación si la configuración se rompe después.
:::

La carpeta copiada debe contener al menos:

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

Las entradas `.hpm_*` son los datos partidos del mapa. Forman parte del mapa y deben quedarse junto a `sample_map.hpm`.

## Lanza la copia intacta
1. Ejecuta `ModLauncher.exe`, o `ModLauncher_NoSteam.exe` sin Steam.
1. Elige **Play Custom Content**.
1. Selecciona el title que pusiste en `entry.hpc`.
1. Lanza el mod.

El `config/main_init.cfg` incluido arranca `sample_map.hpm` desde `maps/` en `PlayerStartArea_1`.

## Checkpoint
Sigue solo cuando el mod copiado aparece en el launcher y carga su mapa de ejemplo.

## Si no funciona
- **El mod no aparece en el launcher:** la copia está en `SOMA/mods/` y tiene `entry.hpc` en la raíz.
- **El juego arranca pero el mapa no:** restaura `config/main_init.cfg`, `resources.cfg` y la carpeta completa `maps/sample_map/` desde el ejemplo limpio.
- **Entender los archivos:** [Creating a Mod](/es/modding/creating-a-mod/), [Resources Configuration](/es/generated/resources-configuration/), [Launch Configuration](/es/generated/launch-configuration/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. See [Licensing](/es/about/licensing/).

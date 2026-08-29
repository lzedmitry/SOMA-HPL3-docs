---
title: "Créer et lancer votre mod"
description: "Copiez l’exemple fonctionnel de SOMA et lancez la copie avant de la modifier."
category: start
sourceStatus: verified
translation:
  locale: fr
  sourceLocale: en
  sourceRevision: 1
  translationRevision: 1
  status: current
---

Dans cette étape, vous copiez l’exemple fonctionnel de SOMA et lancez la copie **avant** de la modifier.

## Faire votre copie
1. Ouvrez `SOMA/mods/`.
1. Copiez tout le dossier `MinimalCustomMapMod`.
1. Renommez la copie avec un nom de projet court, par exemple `MyFirstMod`.
1. Ouvrez le `entry.hpc` copié dans un éditeur de texte.
1. Changez au moins `Title`, `Author` et `Description`. Laissez `Type="StandAlone"` et `InitCfg="config/main_init.cfg"` inchangés pour ce tutoriel.

:::caution[Caution]
Ne renommez pas et n’éditez pas l’original `MinimalCustomMapMod`. Une copie propre sert de comparaison si la configuration casse plus tard.
:::

Le dossier copié doit contenir au moins :

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

Les `.hpm_*` sont les données séparées de la map. Elles font partie de la map et doivent rester à côté de `sample_map.hpm`.

## Lancer la copie intacte
1. Exécutez `ModLauncher.exe`, ou `ModLauncher_NoSteam.exe` hors Steam.
1. Choisissez **Play Custom Content**.
1. Sélectionnez le title placé dans `entry.hpc`.
1. Lancez le mod.

Le `config/main_init.cfg` inclus démarre `sample_map.hpm` depuis `maps/` à `PlayerStartArea_1`.

## Checkpoint
Continuez seulement lorsque le mod copié apparaît dans le lanceur et charge sa map d’exemple.

## Si ça ne marche pas
- **Le mod est absent du lanceur :** la copie est dans `SOMA/mods/` et a `entry.hpc` à sa racine.
- **Le jeu démarre mais pas la map :** restaurez `config/main_init.cfg`, `resources.cfg` et le dossier complet `maps/sample_map/` depuis l’exemple propre.
- **Comprendre les fichiers :** [Creating a Mod](/fr/modding/creating-a-mod/), [Resources Configuration](/fr/generated/resources-configuration/), [Launch Configuration](/fr/generated/launch-configuration/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. See [Licensing](/fr/about/licensing/).

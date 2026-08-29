---
title: "Создать и запустить мод"
description: "Скопируйте рабочий пример SOMA и запустите копию до любых правок."
category: start
sourceStatus: verified
translation:
  locale: ru
  sourceLocale: en
  sourceRevision: 1
  translationRevision: 1
  status: current
---

В этом шаге вы копируете рабочий пример мода SOMA и запускаете копию **до** любых правок.

## Сделайте свою копию
1. Откройте `SOMA/mods/`.
1. Скопируйте папку `MinimalCustomMapMod` целиком.
1. Переименуйте копию в короткое имя проекта, например `MyFirstMod`.
1. Откройте скопированный `entry.hpc` в текстовом редакторе.
1. Измените как минимум `Title`, `Author` и `Description`. Для этого туториала оставьте `Type="StandAlone"` и `InitCfg="config/main_init.cfg"` без изменений.

:::caution[Caution]
Не переименовывайте и не правьте оригинал `MinimalCustomMapMod`. Чистая копия нужна для сравнения, если конфигурация позже сломается.
:::

Скопированная папка должна содержать как минимум:

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

Записи `.hpm_*` выше — разделённые данные карты. Они часть карты и должны оставаться рядом с `sample_map.hpm`.

## Запустите нетронутую копию
1. Запустите `ModLauncher.exe` или `ModLauncher_NoSteam.exe` для установки без Steam.
1. Выберите **Play Custom Content**.
1. Выберите title, который вы указали в `entry.hpc`.
1. Запустите мод.

Включённый `config/main_init.cfg` стартует `sample_map.hpm` из папки `maps/` в `PlayerStartArea_1`.

## Checkpoint
Продолжайте только когда скопированный мод виден в лаунчере и загружает свою sample-карту.

## Если не работает
- **Мода нет в лаунчере:** копия должна лежать в `SOMA/mods/` и иметь `entry.hpc` в корне.
- **Игра стартует, карта нет:** восстановите `config/main_init.cfg`, `resources.cfg` и полный `maps/sample_map/` из чистого примера.
- **Нужно понять файлы:** [Creating a Mod](/ru/modding/creating-a-mod/), [Resources Configuration](/ru/generated/resources-configuration/), [Launch Configuration](/ru/generated/launch-configuration/).

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. See [Licensing](/ru/about/licensing/).

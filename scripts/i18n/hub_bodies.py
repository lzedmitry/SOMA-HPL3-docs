"""Translated TIER 1–2 hub bodies. Identifiers stay English. Links are English paths."""

from __future__ import annotations

HUBS: dict[str, dict[str, str]] = {}

SRC = {
    "ru": "Источники",
    "de": "Quellen",
    "fr": "Sources",
    "it": "Fonti",
    "es": "Fuentes",
}
REL = {
    "ru": "Связанное",
    "de": "Siehe auch",
    "fr": "Voir aussi",
    "it": "Correlati",
    "es": "Relacionado",
}


def _row(href: str, label: str, hint: str) -> str:
    return f'<div class="catalog-row"><a href="{href}">{label}</a><span>{hint}</span></div>\n'


def _put(slug: str, **langs: str) -> None:
    HUBS[slug] = langs


# ---------------------------------------------------------------------------
# First mod (wiki step) — full structure, five locales
# ---------------------------------------------------------------------------
_CREATE = {
    "lead": {
        "ru": "В этом шаге вы копируете рабочий пример мода SOMA и запускаете копию **до** любых правок.",
        "de": "In diesem Schritt kopieren Sie das funktionierende SOMA-Beispiel und starten die Kopie, **bevor** Sie etwas ändern.",
        "fr": "Dans cette étape, vous copiez l’exemple fonctionnel de SOMA et lancez la copie **avant** de la modifier.",
        "it": "In questo passo copi l’esempio funzionante di SOMA e avvii la copia **prima** di modificarla.",
        "es": "En este paso copias el ejemplo funcional de SOMA y lanzas la copia **antes** de cambiarla.",
    },
    "h_copy": {
        "ru": "Сделайте свою копию",
        "de": "Eigene Kopie anlegen",
        "fr": "Faire votre copie",
        "it": "Fai la tua copia",
        "es": "Haz tu propia copia",
    },
    "steps": {
        "ru": [
            "Откройте `SOMA/mods/`.",
            "Скопируйте папку `MinimalCustomMapMod` целиком.",
            "Переименуйте копию в короткое имя проекта, например `MyFirstMod`.",
            "Откройте скопированный `entry.hpc` в текстовом редакторе.",
            'Измените как минимум `Title`, `Author` и `Description`. Для этого туториала оставьте `Type="StandAlone"` и `InitCfg="config/main_init.cfg"` без изменений.',
        ],
        "de": [
            "Öffnen Sie `SOMA/mods/`.",
            "Kopieren Sie den gesamten Ordner `MinimalCustomMapMod`.",
            "Benennen Sie die Kopie in einen kurzen Projektnamen um, z. B. `MyFirstMod`.",
            "Öffnen Sie die kopierte `entry.hpc` in einem Texteditor.",
            'Ändern Sie mindestens `Title`, `Author` und `Description`. Lassen Sie `Type="StandAlone"` und `InitCfg="config/main_init.cfg"` für dieses Tutorial unverändert.',
        ],
        "fr": [
            "Ouvrez `SOMA/mods/`.",
            "Copiez tout le dossier `MinimalCustomMapMod`.",
            "Renommez la copie avec un nom de projet court, par exemple `MyFirstMod`.",
            "Ouvrez le `entry.hpc` copié dans un éditeur de texte.",
            'Changez au moins `Title`, `Author` et `Description`. Laissez `Type="StandAlone"` et `InitCfg="config/main_init.cfg"` inchangés pour ce tutoriel.',
        ],
        "it": [
            "Apri `SOMA/mods/`.",
            "Copia l’intera cartella `MinimalCustomMapMod`.",
            "Rinomina la copia con un nome di progetto breve, ad esempio `MyFirstMod`.",
            "Apri l’`entry.hpc` copiato in un editor di testo.",
            'Cambia almeno `Title`, `Author` e `Description`. Lascia `Type="StandAlone"` e `InitCfg="config/main_init.cfg"` invariati per questo tutorial.',
        ],
        "es": [
            "Abre `SOMA/mods/`.",
            "Copia la carpeta `MinimalCustomMapMod` entera.",
            "Renombra la copia con un nombre de proyecto corto, por ejemplo `MyFirstMod`.",
            "Abre el `entry.hpc` copiado en un editor de texto.",
            'Cambia al menos `Title`, `Author` y `Description`. Deja `Type="StandAlone"` e `InitCfg="config/main_init.cfg"` sin cambios para este tutorial.',
        ],
    },
    "caution": {
        "ru": "Не переименовывайте и не правьте оригинал `MinimalCustomMapMod`. Чистая копия нужна для сравнения, если конфигурация позже сломается.",
        "de": "Original `MinimalCustomMapMod` nicht umbenennen oder editieren. Eine saubere Kopie ist der Vergleich, wenn die Konfiguration später bricht.",
        "fr": "Ne renommez pas et n’éditez pas l’original `MinimalCustomMapMod`. Une copie propre sert de comparaison si la configuration casse plus tard.",
        "it": "Non rinominare né modificare l’originale `MinimalCustomMapMod`. Una copia pulita serve da confronto se la configurazione si rompe.",
        "es": "No renombres ni edites el `MinimalCustomMapMod` original. Una copia limpia sirve de comparación si la configuración se rompe después.",
    },
    "tree_intro": {
        "ru": "Скопированная папка должна содержать как минимум:",
        "de": "Der kopierte Ordner muss mindestens enthalten:",
        "fr": "Le dossier copié doit contenir au moins :",
        "it": "La cartella copiata deve contenere almeno:",
        "es": "La carpeta copiada debe contener al menos:",
    },
    "sidecars": {
        "ru": "Записи `.hpm_*` выше — разделённые данные карты. Они часть карты и должны оставаться рядом с `sample_map.hpm`.",
        "de": "Die `.hpm_*`-Einträge sind die geteilten Map-Daten. Sie gehören zur Map und müssen neben `sample_map.hpm` bleiben.",
        "fr": "Les `.hpm_*` sont les données séparées de la map. Elles font partie de la map et doivent rester à côté de `sample_map.hpm`.",
        "it": "Le voci `.hpm_*` sono i dati spezzati della mappa. Fanno parte della mappa e devono restare accanto a `sample_map.hpm`.",
        "es": "Las entradas `.hpm_*` son los datos partidos del mapa. Forman parte del mapa y deben quedarse junto a `sample_map.hpm`.",
    },
    "h_launch": {
        "ru": "Запустите нетронутую копию",
        "de": "Unveränderte Kopie starten",
        "fr": "Lancer la copie intacte",
        "it": "Avvia la copia intatta",
        "es": "Lanza la copia intacta",
    },
    "launch": {
        "ru": [
            "Запустите `ModLauncher.exe` или `ModLauncher_NoSteam.exe` для установки без Steam.",
            "Выберите **Play Custom Content**.",
            "Выберите title, который вы указали в `entry.hpc`.",
            "Запустите мод.",
        ],
        "de": [
            "`ModLauncher.exe` ausführen, oder `ModLauncher_NoSteam.exe` ohne Steam.",
            "**Play Custom Content** wählen.",
            "Den Title aus `entry.hpc` wählen.",
            "Den Mod starten.",
        ],
        "fr": [
            "Exécutez `ModLauncher.exe`, ou `ModLauncher_NoSteam.exe` hors Steam.",
            "Choisissez **Play Custom Content**.",
            "Sélectionnez le title placé dans `entry.hpc`.",
            "Lancez le mod.",
        ],
        "it": [
            "Esegui `ModLauncher.exe`, oppure `ModLauncher_NoSteam.exe` senza Steam.",
            "Scegli **Play Custom Content**.",
            "Seleziona il title messo in `entry.hpc`.",
            "Avvia la mod.",
        ],
        "es": [
            "Ejecuta `ModLauncher.exe`, o `ModLauncher_NoSteam.exe` sin Steam.",
            "Elige **Play Custom Content**.",
            "Selecciona el title que pusiste en `entry.hpc`.",
            "Lanza el mod.",
        ],
    },
    "initcfg": {
        "ru": "Включённый `config/main_init.cfg` стартует `sample_map.hpm` из папки `maps/` в `PlayerStartArea_1`.",
        "de": "Die mitgelieferte `config/main_init.cfg` startet `sample_map.hpm` aus `maps/` bei `PlayerStartArea_1`.",
        "fr": "Le `config/main_init.cfg` inclus démarre `sample_map.hpm` depuis `maps/` à `PlayerStartArea_1`.",
        "it": "Il `config/main_init.cfg` incluso avvia `sample_map.hpm` da `maps/` in `PlayerStartArea_1`.",
        "es": "El `config/main_init.cfg` incluido arranca `sample_map.hpm` desde `maps/` en `PlayerStartArea_1`.",
    },
    "checkpoint": {
        "ru": "Продолжайте только когда скопированный мод виден в лаунчере и загружает свою sample-карту.",
        "de": "Erst weiter, wenn der kopierte Mod im Launcher erscheint und seine Sample-Map lädt.",
        "fr": "Continuez seulement lorsque le mod copié apparaît dans le lanceur et charge sa map d’exemple.",
        "it": "Continua solo quando la mod copiata compare nel launcher e carica la mappa di esempio.",
        "es": "Sigue solo cuando el mod copiado aparece en el launcher y carga su mapa de ejemplo.",
    },
    "fail": {
        "ru": (
            "**Мода нет в лаунчере:** копия должна лежать в `SOMA/mods/` и иметь `entry.hpc` в корне.",
            "**Игра стартует, карта нет:** восстановите `config/main_init.cfg`, `resources.cfg` и полный `maps/sample_map/` из чистого примера.",
            "**Нужно понять файлы:** [Creating a Mod](/modding/creating-a-mod/), [Resources Configuration](/generated/resources-configuration/), [Launch Configuration](/generated/launch-configuration/).",
        ),
        "de": (
            "**Mod fehlt im Launcher:** Kopie liegt in `SOMA/mods/` und hat `entry.hpc` im Root.",
            "**Spiel startet, Map nicht:** `config/main_init.cfg`, `resources.cfg` und den kompletten Ordner `maps/sample_map/` aus dem sauberen Beispiel wiederherstellen.",
            "**Dateien verstehen:** [Creating a Mod](/modding/creating-a-mod/), [Resources Configuration](/generated/resources-configuration/), [Launch Configuration](/generated/launch-configuration/).",
        ),
        "fr": (
            "**Le mod est absent du lanceur :** la copie est dans `SOMA/mods/` et a `entry.hpc` à sa racine.",
            "**Le jeu démarre mais pas la map :** restaurez `config/main_init.cfg`, `resources.cfg` et le dossier complet `maps/sample_map/` depuis l’exemple propre.",
            "**Comprendre les fichiers :** [Creating a Mod](/modding/creating-a-mod/), [Resources Configuration](/generated/resources-configuration/), [Launch Configuration](/generated/launch-configuration/).",
        ),
        "it": (
            "**La mod manca dal launcher:** la copia è in `SOMA/mods/` e ha `entry.hpc` nella root.",
            "**Il gioco parte ma la mappa no:** ripristina `config/main_init.cfg`, `resources.cfg` e l’intera cartella `maps/sample_map/` dall’esempio pulito.",
            "**Capire i file:** [Creating a Mod](/modding/creating-a-mod/), [Resources Configuration](/generated/resources-configuration/), [Launch Configuration](/generated/launch-configuration/).",
        ),
        "es": (
            "**El mod no aparece en el launcher:** la copia está en `SOMA/mods/` y tiene `entry.hpc` en la raíz.",
            "**El juego arranca pero el mapa no:** restaura `config/main_init.cfg`, `resources.cfg` y la carpeta completa `maps/sample_map/` desde el ejemplo limpio.",
            "**Entender los archivos:** [Creating a Mod](/modding/creating-a-mod/), [Resources Configuration](/generated/resources-configuration/), [Launch Configuration](/generated/launch-configuration/).",
        ),
    },
}

TREE = """```
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
"""

_create: dict[str, str] = {}
for loc in ("ru", "de", "fr", "it", "es"):
    steps = "\n".join(f"1. {s}" for s in _CREATE["steps"][loc])
    launch = "\n".join(f"1. {s}" for s in _CREATE["launch"][loc])
    fails = "\n".join(f"- {s}" for s in _CREATE["fail"][loc])
    _create[loc] = f"""{_CREATE["lead"][loc]}

## {_CREATE["h_copy"][loc]}
{steps}

:::caution[Caution]
{_CREATE["caution"][loc]}
:::

{_CREATE["tree_intro"][loc]}

{TREE}
{_CREATE["sidecars"][loc]}

## {_CREATE["h_launch"][loc]}
{launch}

{_CREATE["initcfg"][loc]}

## Checkpoint
{_CREATE["checkpoint"][loc]}

## { {"ru": "Если не работает", "de": "Wenn es nicht geht", "fr": "Si ça ne marche pas", "it": "Se non funziona", "es": "Si no funciona"}[loc] }
{fails}

## Source & attribution

- Original Frictional Wiki page: [HPL3/SOMA/Getting Started/Create and Launch Your Mod](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started/Create_and_Launch_Your_Mod)
- Revision: `7115`

This is unofficial community documentation and is not affiliated with or endorsed by Frictional Games. See [Licensing](/about/licensing/).
"""
_put("start/create-and-launch-your-mod", **_create)


# Remaining hubs live in hubs_rest / hubs_more / hubs_catalog / hubs_last.
# terminology is packed in hubs_rest.py (this file only holds create-and-launch).

"""Remaining TIER 1–2 hub bodies."""

HUBS: dict[str, dict[str, str]] = {}


def P(slug: str, **langs: str) -> None:
    HUBS[slug] = langs


def R(href: str, label: str, hint: str) -> str:
    return f'<div class="catalog-row"><a href="{href}">{label}</a><span>{hint}</span></div>'


# ---- terminology ----
TERM_TABLE = """
| Term | Meaning |
| --- | --- |
| **HPL3** | {hpl3} |
| **Mod** | {mod} |
| **Stand-alone mod** | {standalone} |
| **Add-on** | {addon} |
| **`.hpc`** | {hpc} |
| **`.hpm`** | {hpm} |
| **`.hps`** | {hps} |
| **Area** | {area} |
| **Entity** | {entity} |
| **Prop** | {prop} |
| **Agent** | {agent} |
| **Critter** | {critter} |
| **Static object** | {static} |
| **Helper** | {helper} |
| **WIP mod** | {wip} |
| **SH probe** | {sh} |
| **ID handle** | {idhandle} |
| **User module** | {umod} |
"""

P(
    "start/terminology",
    ru="""Эти термины появляются до того, как исходная Wiki их объясняет. Полные статьи: [Glossary](/glossary/).
"""
    + TERM_TABLE.format(
        hpl3="Движок Frictional, как он поставляется с SOMA. Редакторы + runtime AngelScript.",
        mod="Дополнительный контент в своей папке, загружается через `entry.hpc`.",
        standalone="Мод со своими картами; запускается из SOMA mod launcher.",
        addon="Мод, который может ехать вместе со stand-alone модом.",
        hpc="Файл входа мода.",
        hpm="Файл уровня/карты. Держите компаньоны `.hpm_*`.",
        hps="Исходник AngelScript. Скрипты карты лежат рядом с картой.",
        area="Невидимый объём — система ввода/вывода движка.",
        entity="Объект мира с поведением. Большинство интерактивных — **props**.",
        prop="Entity, с которым может взаимодействовать игрок или скрипт.",
        agent="Entity врага / NPC.",
        critter="Мелкое фоновое существо без полного agent-скрипта.",
        static="Mesh коллизии/вида без поведения Entity.",
        helper="Общий include `.hps` из скриптов карты. Wiki перечисляет категории; большинство *страниц* helper так и не написали.",
        wip="Мод в разработке. Wiki использует это в документах лаунчера.",
        sh="Spherical-harmonic lighting probe. Ссылка с Level Design; страница SOMA — redlink.",
        idhandle="Идентичность объекта движка из скрипта. См. [ID Handles](/scripting/id-handles/).",
        umod="Скриптовый модуль, встроенный в игру. См. [User modules](/scripting/user-modules-overview/).",
    )
    + """
:::note
Исходная страница Glossary — stub и всё ещё marked under construction. Определения выше остаются внутри того, что говорят эта страница и соседние статьи.
:::

## Связанное

- [Glossary](/glossary/)
- [Areas overview](/areas/)
- [Entities](/entities/)
""",
    de="""Das sind die Begriffe, die auftauchen, bevor das Original-Wiki sie erklärt. Längere Einträge: [Glossary](/glossary/).
"""
    + TERM_TABLE.format(
        hpl3="Frictionals Engine, wie sie mit SOMA ausgeliefert wird. Editoren + AngelScript-Runtime.",
        mod="Extra-Inhalt im eigenen Ordner, geladen über `entry.hpc`.",
        standalone="Ein Mod mit eigenen Maps; Start über den SOMA-Mod-Launcher.",
        addon="Ein Mod, der mit einem Stand-alone-Mod mitlaufen kann.",
        hpc="Mod-Entry-Datei.",
        hpm="Level/Map-Datei. `.hpm_*`-Begleiter behalten.",
        hps="AngelScript-Quelle. Map-Skripte liegen neben der Map.",
        area="Unsichtbares Volumen als Ein-/Ausgabesystem der Engine.",
        entity="Weltobjekt mit Verhalten. Die meisten interaktiven sind **props**.",
        prop="Entity, mit der Spieler oder Skript interagieren können.",
        agent="Gegner-/NPC-Entity.",
        critter="Kleines Hintergrundwesen ohne volles Agent-Skript.",
        static="Kollisions-/Visual-Mesh ohne Entity-Verhalten.",
        helper="Geteiltes `.hps`-Include aus Map-Skripten. Das Wiki listet Kategorien; die meisten Helper-*Seiten* wurden nie geschrieben.",
        wip="Mod in Entwicklung. Das Wiki nutzt das in Launcher/Setup-Docs.",
        sh="Spherical-harmonic lighting probe. Verlinkt von Level Design; SOMA-Seite ist ein Redlink.",
        idhandle="Engine-Objektidentität aus dem Skript. Siehe [ID Handles](/scripting/id-handles/).",
        umod="Skriptmodul, das ins Spiel eingehängt wird. Siehe [User modules](/scripting/user-modules-overview/).",
    )
    + """
:::note
Die Original-Glossary-Seite ist ein Stub und steht noch unter construction. Die Definitionen oben bleiben in dem, was diese Seite und die umgebenden Artikel tatsächlich sagen.
:::

## Siehe auch

- [Glossary](/glossary/)
- [Areas overview](/areas/)
- [Entities](/entities/)
""",
    fr="""Ce sont les termes qui apparaissent avant que le Wiki d’origine ne les explique. Entrées longues : [Glossary](/glossary/).
"""
    + TERM_TABLE.format(
        hpl3="Moteur Frictional livré avec SOMA. Éditeurs + runtime AngelScript.",
        mod="Contenu extra dans son propre dossier, chargé via `entry.hpc`.",
        standalone="Un mod avec ses propres maps ; lancé depuis le SOMA mod launcher.",
        addon="Un mod qui peut accompagner un stand-alone mod.",
        hpc="Fichier d’entrée du mod.",
        hpm="Fichier de niveau/map. Garder ses compagnons `.hpm_*`.",
        hps="Source AngelScript. Les scripts de map sont à côté de la map.",
        area="Volume invisible, système d’entrée/sortie du moteur.",
        entity="Objet du monde avec un comportement. La plupart des interactifs sont des **props**.",
        prop="Entity avec laquelle le joueur ou un script peut interagir.",
        agent="Entity ennemi / NPC.",
        critter="Petite créature de fond sans script agent complet.",
        static="Mesh collision/visuel sans comportement Entity.",
        helper="Include `.hps` partagé depuis les scripts de map. Le Wiki liste des catégories ; la plupart des *pages* helper n’ont jamais été écrites.",
        wip="Mod encore en développement. Le Wiki l’utilise dans les docs launcher/setup.",
        sh="Spherical-harmonic lighting probe. Lié depuis Level Design ; la page SOMA est un redlink.",
        idhandle="Identité d’objet moteur depuis le script. Voir [ID Handles](/scripting/id-handles/).",
        umod="Module de script branché dans le jeu. Voir [User modules](/scripting/user-modules-overview/).",
    )
    + """
:::note
La page Glossary d’origine est un stub encore marked under construction. Les définitions ci-dessus restent dans ce que cette page et les articles autour disent réellement.
:::

## Voir aussi

- [Glossary](/glossary/)
- [Areas overview](/areas/)
- [Entities](/entities/)
""",
    it="""Questi sono i termini che compaiono prima che il Wiki originale li spieghi. Voci lunghe: [Glossary](/glossary/).
"""
    + TERM_TABLE.format(
        hpl3="Motore Frictional come spedito con SOMA. Editor + runtime AngelScript.",
        mod="Contenuto extra nella propria cartella, caricato via `entry.hpc`.",
        standalone="Una mod con le proprie mappe; avviata dal SOMA mod launcher.",
        addon="Una mod che può viaggiare insieme a una stand-alone.",
        hpc="File di entry della mod.",
        hpm="File di livello/mappa. Tieni i companion `.hpm_*`.",
        hps="Sorgente AngelScript. Gli script di mappa stanno accanto alla mappa.",
        area="Volume invisibile, sistema di input/output del motore.",
        entity="Oggetto di mondo con comportamento. La maggior parte degli interattivi sono **props**.",
        prop="Entity con cui il giocatore o uno script possono interagire.",
        agent="Entity nemico / NPC.",
        critter="Piccola creatura di sfondo senza uno script agent completo.",
        static="Mesh di collisione/visuale senza comportamento Entity.",
        helper="Include `.hps` condiviso dagli script di mappa. Il Wiki elenca categorie; la maggior parte delle *pagine* helper non è mai stata scritta.",
        wip="Mod ancora in sviluppo. Il Wiki lo usa nei documenti launcher/setup.",
        sh="Spherical-harmonic lighting probe. Collegato da Level Design; la pagina SOMA è un redlink.",
        idhandle="Identità dell’oggetto motore dallo script. Vedi [ID Handles](/scripting/id-handles/).",
        umod="Modulo di script agganciato nel gioco. Vedi [User modules](/scripting/user-modules-overview/).",
    )
    + """
:::note
La pagina Glossary originale è uno stub ancora marked under construction. Le definizioni sopra restano dentro ciò che quella pagina e gli articoli intorno dicono davvero.
:::

## Correlati

- [Glossary](/glossary/)
- [Areas overview](/areas/)
- [Entities](/entities/)
""",
    es="""Estos son los términos que aparecen antes de que el Wiki original los explique. Entradas largas: [Glossary](/glossary/).
"""
    + TERM_TABLE.format(
        hpl3="Motor de Frictional tal como se envía con SOMA. Editores + runtime AngelScript.",
        mod="Contenido extra en su propia carpeta, cargado vía `entry.hpc`.",
        standalone="Un mod con sus propios mapas; se lanza desde el SOMA mod launcher.",
        addon="Un mod que puede ir junto a un stand-alone.",
        hpc="Archivo de entrada del mod.",
        hpm="Archivo de nivel/mapa. Conserva los companion `.hpm_*`.",
        hps="Fuente AngelScript. Los scripts de mapa viven junto al mapa.",
        area="Volumen invisible, sistema de entrada/salida del motor.",
        entity="Objeto de mundo con comportamiento. La mayoría de los interactivos son **props**.",
        prop="Entity con la que el jugador o un script pueden interactuar.",
        agent="Entity enemigo / NPC.",
        critter="Criatura de fondo pequeña sin un script agent completo.",
        static="Mesh de colisión/visual sin comportamiento Entity.",
        helper="Include `.hps` compartido desde scripts de mapa. El Wiki lista categorías; la mayoría de las *páginas* helper nunca se escribieron.",
        wip="Un mod aún en desarrollo. El Wiki lo usa en docs de launcher/setup.",
        sh="Spherical-harmonic lighting probe. Enlazado desde Level Design; la página SOMA es un redlink.",
        idhandle="Identidad de objeto del motor desde script. Véase [ID Handles](/scripting/id-handles/).",
        umod="Módulo de script enganchado en el juego. Véase [User modules](/scripting/user-modules-overview/).",
    )
    + """
:::note
La página Glossary original es un stub y sigue marked under construction. Las definiciones de arriba se quedan dentro de lo que esa página y los artículos de alrededor dicen de verdad.
:::

## Relacionado

- [Glossary](/glossary/)
- [Areas overview](/areas/)
- [Entities](/entities/)
""",
)

# Generic compact hubs — same catalogs as English, translated prose.

def catalog(rows: list[tuple[str, str, str]]) -> str:
    inner = "\n".join(R(*r) for r in rows)
    return f'<div class="catalog-group">\n{inner}\n</div>\n'


P(
    "recipes/first-mod",
    ru="""## Цель

Папка stand-alone мода, которая появляется в лаунчере SOMA и стартует свою sample-карту.

## Требования

SOMA установлена, по [Prepare your tools](/start/prepare-your-tools/).

## Шаги

Следуйте [Create and launch your mod](/start/create-and-launch-your-mod/) по порядку. Та страница — чеклист. Подробности: [Creating a mod](/modding/creating-a-mod/) и [MinimalCustomMapMod](/modding/minimalcustommapmod/).

## Ожидаемый результат

Скопированный мод есть в лаунчере, sample-карта запускается.

## Почему это работает

В комплекте уже есть рабочий `entry.hpc` + `resources.cfg` + карта. Копирование избавляет от сборки этих файлов по памяти.

## Типичный сбой

Правка оригинального примера или базовой игры. Работайте в копии.

## Relevant reference

- [Creating a mod](/modding/creating-a-mod/)
- [Launcher](/modding/soma-mod-launcher/)
""",
    de="""## Ziel

Ein Stand-alone-Mod-Ordner, der im SOMA-Launcher erscheint und seine Sample-Map startet.

## Voraussetzungen

SOMA installiert, siehe [Prepare your tools](/start/prepare-your-tools/).

## Schritte

Folgen Sie [Create and launch your mod](/start/create-and-launch-your-mod/) der Reihe nach. Diese Seite ist die Checkliste. Details: [Creating a mod](/modding/creating-a-mod/) und [MinimalCustomMapMod](/modding/minimalcustommapmod/).

## Erwartetes Ergebnis

Der kopierte Mod steht im Launcher und die Sample-Map läuft.

## Warum es funktioniert

Das mitgelieferte Beispiel ist ein bekannt-funktionierendes `entry.hpc` + `resources.cfg` + Map. Kopieren vermeidet, diese Dateien aus dem Gedächtnis zusammenzubauen.

## Häufiger Fehler

Das Originalbeispiel oder das Basis-Spiel editieren. In der Kopie arbeiten.

## Relevant reference

- [Creating a mod](/modding/creating-a-mod/)
- [Launcher](/modding/soma-mod-launcher/)
""",
    fr="""## Objectif

Un dossier de mod stand-alone qui apparaît dans le lanceur SOMA et démarre sa map d’exemple.

## Prérequis

SOMA installé, selon [Prepare your tools](/start/prepare-your-tools/).

## Étapes

Suivez [Create and launch your mod](/start/create-and-launch-your-mod/) dans l’ordre. Cette page est la checklist. Détails : [Creating a mod](/modding/creating-a-mod/) et [MinimalCustomMapMod](/modding/minimalcustommapmod/).

## Résultat attendu

Le mod copié est dans le lanceur et la map d’exemple tourne.

## Pourquoi ça marche

L’exemple fourni est un `entry.hpc` + `resources.cfg` + map connus pour fonctionner. Le copier évite d’assembler ces fichiers de mémoire.

## Échec courant

Éditer l’exemple original ou le jeu de base. Travaillez dans la copie.

## Relevant reference

- [Creating a mod](/modding/creating-a-mod/)
- [Launcher](/modding/soma-mod-launcher/)
""",
    it="""## Obiettivo

Una cartella mod stand-alone che compare nel launcher di SOMA e avvia la mappa di esempio.

## Requisiti

SOMA installato, secondo [Prepare your tools](/start/prepare-your-tools/).

## Passi

Segui [Create and launch your mod](/start/create-and-launch-your-mod/) in ordine. Quella pagina è la checklist. Dettagli: [Creating a mod](/modding/creating-a-mod/) e [MinimalCustomMapMod](/modding/minimalcustommapmod/).

## Risultato atteso

La mod copiata è nel launcher e la mappa di esempio parte.

## Perché funziona

L’esempio incluso è un `entry.hpc` + `resources.cfg` + mappa noti per funzionare. Copiarlo evita di assemblare quei file a memoria.

## Fallimento comune

Modificare l’esempio originale o il gioco base. Lavora nella copia.

## Relevant reference

- [Creating a mod](/modding/creating-a-mod/)
- [Launcher](/modding/soma-mod-launcher/)
""",
    es="""## Objetivo

Una carpeta de mod stand-alone que aparece en el launcher de SOMA y arranca su mapa de ejemplo.

## Requisitos

SOMA instalado, según [Prepare your tools](/start/prepare-your-tools/).

## Pasos

Sigue [Create and launch your mod](/start/create-and-launch-your-mod/) en orden. Esa página es la checklist. Detalles: [Creating a mod](/modding/creating-a-mod/) y [MinimalCustomMapMod](/modding/minimalcustommapmod/).

## Resultado esperado

El mod copiado está en el launcher y el mapa de ejemplo corre.

## Por qué funciona

El ejemplo incluido es un `entry.hpc` + `resources.cfg` + mapa que ya funciona. Copiarlo evita armar esos archivos de memoria.

## Fallo habitual

Editar el ejemplo original o el juego base. Trabaja en la copia.

## Relevant reference

- [Creating a mod](/modding/creating-a-mod/)
- [Launcher](/modding/soma-mod-launcher/)
""",
)

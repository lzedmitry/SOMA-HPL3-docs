"""Remaining catalog hubs (areas, scripting, level-building, etc.)."""

from __future__ import annotations

HUBS: dict[str, dict[str, str]] = {}
SRC = dict(ru="Источники", de="Quellen", fr="Sources", it="Fonti", es="Fuentes")
REL = dict(ru="Связанное", de="Siehe auch", fr="Voir aussi", it="Correlati", es="Relacionado")


def row(href: str | None, label: str, hint: str) -> str:
    if href:
        left = f'<a href="{href}">{label}</a>'
    else:
        left = f"<span>{label}</span>"
    return f'<div class="catalog-row">{left}<span>{hint}</span></div>'


def group(rows: list[tuple]) -> str:
    inner = []
    for item in rows:
        if len(item) == 3:
            inner.append(row(*item))
        else:
            inner.append(row(item[0], item[1], item[2]))
    return '<div class="catalog-group">\n' + "\n".join(inner) + "\n</div>\n"


def close(locale: str, related: list[str], sources: list[str]) -> str:
    out = [f"## {REL[locale]}", ""]
    out.extend(f"- {x}" for x in related)
    out += ["", f"## {SRC[locale]}", ""]
    out.extend(f"- {x}" for x in sources)
    return "\n".join(out) + "\n"


def pack(slug: str, data: dict[str, str]) -> None:
    HUBS[slug] = data


# Shared catalogs (labels = identifiers where required)
AREAS_CORE = [
    ("/areas/playerstart-area/", "PlayerStart", "Player spawn position."),
    ("/areas/trigger-area/", "Trigger", "Generic callback volume. Start here."),
    ("/areas/doorwaytrigger-area/", "DoorwayTrigger", "Doorway-related trigger volume."),
    ("/areas/pathnode-area/", "PathNode", "AI path node."),
    ("/areas/sticky-area/", "Sticky", "Attaches bodies. FAQ: wait a timer before making the body a static collider."),
    ("/areas/interactaux-area/", "InteractAux", "Auxiliary interaction volume."),
]
AREAS_ENV = [
    ("/areas/fog-area/", "Fog", "Local fog. Also level-wide fog in Level Settings."),
    ("/areas/soundscape-area/", "Soundscape", "Local soundscape. See Audio."),
    ("/areas/camera-animation-area/", "Camera Animation", "Camera animation volume."),
    ("/areas/ambient-light-area/", "Ambient Light", "Local ambient light volume."),
    (None, 'Liquid <span class="legacy-tag">Wiki redlink</span>', "Listed on the hub. No article."),
    (None, 'Exposure <span class="legacy-tag">Wiki redlink</span>', 'Related: <a href="/level-building/exposure-areas/">Exposure Areas (level design)</a>.'),
]
AREAS_PLAYER = [
    ("/areas/climb-area/", "Climb", "Climb volume."),
    ("/areas/crawl-area/", "Crawl", "Crawl volume."),
    ("/areas/hide-area/", "Hide", "Hide volume."),
    ("/areas/ladder-area/", "Ladder", "Ladder volume."),
    ("/areas/zoom-area/", "Zoom", "Zoom volume."),
]
AREAS_TECH = [
    (None, 'Visibility <span class="legacy-tag">Wiki redlink</span>', "Listed on the hub. No article."),
    (None, 'VisibilityPortal <span class="legacy-tag">Wiki redlink</span>', "Listed on the hub. No article."),
    (None, 'MapTransfer <span class="legacy-tag">Wiki redlink</span>', "Listed on the hub. No article."),
]
AREAS_SOMA = [
    ("/areas/tool-area/", "Tool", "SOMA tool interaction volume."),
    (None, 'Sit <span class="legacy-tag">Wiki redlink</span>', "Game-specific Area. No article."),
    ("/areas/distortion-area/", "Distortion", "SOMA distortion volume."),
    ("/areas/datamine-area/", "Datamine", "SOMA datamine volume."),
    ("/areas/agentrepel-area/", "AgentRepel", "Repels agents."),
]
AREAS_LEGACY = [
    ("/areas/description-area/", "Description", "Marked unused on the hub. Page exists."),
    (None, 'DatamineAudioSource <span class="legacy-tag">Unused, redlink</span>', "Listed unused. No article."),
    (None, 'DatamineAnimNode <span class="legacy-tag">Unused, redlink</span>', "Listed unused. No article."),
    (None, 'PosNode <span class="legacy-tag">Unused, redlink</span>', "Listed unused. No article."),
    (None, 'Rope <span class="legacy-tag">Unused, redlink</span>', "Listed unused. No article."),
]

LEAD_AREAS = {
    "ru": " **Area** — невидимый кубоид в уровне. Исходный хаб Areas называет Area основной системой Input/Output HPL3 и каркасом каждого уровня.",
    "de": "Eine **Area** ist ein unsichtbares Quader im Level. Der originale Areas-Hub nennt Areas das Haupt-Ein-/Ausgabesystem von HPL3.",
    "fr": "Une **Area** est un cuboïde invisible dans le niveau. Le hub Areas d’origine appelle les Areas le système d’entrée/sortie principal de HPL3.",
    "it": "Un’**Area** è un cuboide invisibile nel livello. L’hub Areas originale chiama le Area il sistema di input/output principale di HPL3.",
    "es": "Un **Area** es un cuboide invisible en el nivel. El hub Areas original llama a las Area el sistema principal de entrada/salida de HPL3.",
}
USE_AREAS = {
    "ru": "Ставьте Area, когда что-то должно случиться, потому что игрок (или другая Entity) вошёл в объём, посмотрел на что-то, или сам объём — эффект (fog, soundscape, exposure).",
    "de": "Nutzen Sie sie, wenn etwas passieren soll, weil der Spieler (oder eine andere Entity) ein Volumen betreten hat, etwas angesehen hat, oder weil das Volumen selbst ein Effekt ist (Fog, Soundscape, Exposure).",
    "fr": "Utilisez-les quand quelque chose doit arriver parce que le joueur (ou une autre Entity) est entré dans un volume, a regardé quelque chose, ou parce que le volume lui-même est un effet (fog, soundscape, exposure).",
    "it": "Usale quando qualcosa deve succedere perché il giocatore (o un’altra Entity) è entrato in un volume, ha guardato qualcosa, o perché il volume stesso è un effetto (fog, soundscape, exposure).",
    "es": "Úsalas cuando algo deba ocurrir porque el jugador (u otra Entity) entró en un volumen, miró algo, o porque el volumen mismo es un efecto (fog, soundscape, exposure).",
}
FLOW_AREAS = {
    "ru": "1. Поставьте Area в Level Editor (инструмент Areas).\n2. Дайте имя. Имя простое: скрипты ищут по имени.\n3. Заполните свойства, которые тип реально документирует (collide callbacks, attachment, look-at, type-specific fields).\n4. Если стреляет скрипт — callback на `.hps` карты (или helper file).\n5. Проверьте в игре. Если не срабатывает: [Trigger Area](/areas/trigger-area/) collide-callback и [Troubleshooting](/debugging/).",
    "de": "1. Area im Level Editor platzieren (Areas-Werkzeug).\n2. Benennen. Namen einfach halten; Skripte suchen per Name.\n3. Eigenschaften füllen, die der Typ tatsächlich dokumentiert (collide callbacks, attachment, look-at, typspezifische Felder).\n4. Wenn Skript feuert: Callback auf die Map-`.hps` (oder eine Helper-Datei).\n5. In-game testen. Wenn nichts feuert: [Trigger Area](/areas/trigger-area/) Collide-Callback-Notizen und [Troubleshooting](/debugging/).",
    "fr": "1. Placez l’Area dans le Level Editor (outil Areas).\n2. Nommez-la. Nom simple ; les scripts la cherchent par nom.\n3. Remplissez les propriétés que le type documente vraiment (collide callbacks, attachment, look-at, champs spécifiques).\n4. Si ça déclenche du script, mettez le callback sur le `.hps` de la map (ou un helper file).\n5. Testez in-game. S’il ne tire jamais : notes collide-callback de [Trigger Area](/areas/trigger-area/) et [Troubleshooting](/debugging/).",
    "it": "1. Piazza l’Area nel Level Editor (strumento Areas).\n2. Dallle un nome. Nome semplice; gli script la cercano per nome.\n3. Compila le proprietà che il tipo documenta davvero (collide callbacks, attachment, look-at, campi specifici).\n4. Se spara script, metti il callback sulla `.hps` della mappa (o un helper file).\n5. Testa in-game. Se non parte mai: note collide-callback di [Trigger Area](/areas/trigger-area/) e [Troubleshooting](/debugging/).",
    "es": "1. Coloca el Area en el Level Editor (herramienta Areas).\n2. Ponle nombre. Nombre simple; los scripts lo buscan por nombre.\n3. Rellena las propiedades que el tipo documenta de verdad (collide callbacks, attachment, look-at, campos específicos).\n4. Si dispara script, pon el callback en el `.hps` del mapa (o un helper file).\n5. Prueba in-game. Si nunca dispara: notas de collide-callback de [Trigger Area](/areas/trigger-area/) y [Troubleshooting](/debugging/).",
}

pack(
    "areas",
    {
        loc: f"""{LEAD_AREAS[loc]}

<p class="section-kicker">03 // AREAS &nbsp; REF 03.10</p>

{USE_AREAS[loc]}

:::caution[SOURCE STATUS: WIP]
{wip}
:::

## {hflow}

{FLOW_AREAS[loc]}

{helper}

## Core

{group(AREAS_CORE)}

## Environment

{group(AREAS_ENV)}

## Player

{group(AREAS_PLAYER)}

## Technical

{group(AREAS_TECH)}

## SOMA

{group(AREAS_SOMA)}

## Legacy / unused

{group(AREAS_LEGACY)}

{close(loc, ["[Scripting](/scripting/)", "[Common patterns](/scripting/common-patterns/)", "[Soundscape and audio](/audio/)", "[Level settings (global fog)](/level-editor/level-settings/)", "[Recipe: enter an Area](/recipes/enter-area/)"], ["[HPL3/SOMA/Areas](https://wiki.frictionalgames.com/page/HPL3/SOMA/Areas)", "Individual `HPL3/Areas/*` and `HPL3/SOMA/Areas/*` articles"])}
"""
        for loc, wip, hflow, helper in [
            ("ru", "Исходный хаб Areas SOMA помечен как undergoing major editing. Несколько типов перечислены, но статьи нет (redlink). Эти строки помечены ниже. Параметры не выдуманы.", "Типовой workflow", "Helper file из статьи Trigger: `helper_area.hps`. Отдельных **страниц** helper нет (redlink); см. [Helpers](/scripting/helpers/)."),
            ("de", "Der originale SOMA-Areas-Hub ist als undergoing major editing markiert. Mehrere Typen sind gelistet, haben aber keinen Artikel (Redlinks). Parameter werden hier nicht erfunden.", "Typischer Workflow", "Helper-Datei laut Trigger-Artikel: `helper_area.hps`. Eigene Helper-**Seiten** sind Redlinks; siehe [Helpers](/scripting/helpers/)."),
            ("fr", "Le hub Areas SOMA d’origine est marked as undergoing major editing. Plusieurs types sont listés sans article (redlinks). Leurs paramètres ne sont pas inventés ici.", "Workflow typique", "Fichier helper nommé par l’article Trigger : `helper_area.hps`. Les **pages** helper dédiées sont des redlinks ; voir [Helpers](/scripting/helpers/)."),
            ("it", "L’hub Areas SOMA originale è marked as undergoing major editing. Diversi tipi sono elencati ma non hanno articolo (redlink). I parametri non sono inventati qui.", "Workflow tipico", "Helper file nominato dall’articolo Trigger: `helper_area.hps`. Le **pagine** helper dedicate sono redlink; vedi [Helpers](/scripting/helpers/)."),
            ("es", "El hub Areas de SOMA original está marked as undergoing major editing. Varios tipos están listados pero no tienen artículo (redlinks). Los parámetros no se inventan aquí.", "Workflow típico", "Helper file que nombra el artículo Trigger: `helper_area.hps`. Las **páginas** helper dedicadas son redlinks; véase [Helpers](/scripting/helpers/)."),
        ]
    },
)

SCRIPT_START = [
    ("/scripting/what-is-scripting-in-hpl3/", "What is scripting?", "Where .hps files live and what they drive."),
    ("/scripting/scripting-workflow-and-structure/", "Workflow and structure", "Generated cScrMap layout."),
    ("/scripting/hello-world/", "Hello World", "cLux_AddDebugMessage."),
    ("/scripting/the-onaction-method/", "OnAction", "Input callback."),
    ("/scripting/the-update-method/", "Update", "Per-frame callback."),
    ("/scripting/timers/", "Timers", "Delayed work."),
    ("/scripting/sequences/", "Sequences", "Ordered beats."),
    ("/scripting/helper-files/", "Helper files", "Includes; not the missing helper articles."),
    ("/scripting/angelscript/angelscript-fundamentals/", "AngelScript fundamentals", "Language chapters."),
]

pack(
    "scripting",
    {
        loc: f"""{lead}

<p class="section-kicker">04 // SCRIPTING &nbsp; REF 04.00</p>

## {hstart}

{group(SCRIPT_START)}

## {hpat}

{pat}

## {harch}

- [ID handles](/scripting/id-handles/)
- [Entity components](/scripting/entity-components/)
- [Level scripting best practices](/scripting/level-scripting-best-practices/)
- [User modules](/scripting/user-modules-overview/)
- [Helpers index](/scripting/helpers/) — Wiki lists 14 helper categories; the pages themselves are redlinks
- [API reference](/api/)

## GUI, player, AI, effects

- [GUI overview](/generated/gui/)
- [Terminals](/scripting/terminals-overview/)
- {undoc}

{close(loc, [], ["[HPL3/SOMA/Scripting](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting)", "[HPL3 Scripting Guide](https://wiki.frictionalgames.com/page/HPL3/Scripting/HPL3_Scripting_Guide)"])}
"""
        for loc, lead, hstart, hpat, pat, harch, undoc in [
            ("ru", "Логика карт SOMA — AngelScript в файлах `.hps`. Карта `sample_map.hpm` грузит `sample_map.hps` рядом. Шаг Getting Started меняет только `OnStart()` внутри сгенерированного класса `cScrMap`.", "Начать скрипты", "Типовые приёмы", "Подтверждено в scripting guide и Getting Started — не выдумано. Полная таблица: [Common patterns](/scripting/common-patterns/).", "Архитектура", "Группы user-module на хабе Scripting (Menu, Energy, Hands, Datamine, Distortion, …) **не были написаны** как статьи. Здесь они остаются undocumented."),
            ("de", "SOMA-Map-Logik ist AngelScript in `.hps`-Dateien. Eine Map `sample_map.hpm` lädt `sample_map.hps` daneben. Der Getting-Started-Skriptschritt ändert nur `OnStart()` in der generierten Klasse `cScrMap`.", "Mit Scripting beginnen", "Übliche Muster", "Bestätigt im Scripting Guide und Getting Started — nicht erfunden. Volle Tabelle: [Common patterns](/scripting/common-patterns/).", "Architektur", "User-Module-Gruppen auf dem Scripting-Hub (Menu, Energy, Hands, Datamine, Distortion, …) wurden **nicht als Artikel geschrieben**. Sie bleiben hier undokumentiert."),
            ("fr", "La logique de map SOMA est de l’AngelScript dans des fichiers `.hps`. Une map `sample_map.hpm` charge `sample_map.hps` à côté. L’étape script de Getting Started ne change que `OnStart()` dans la classe générée `cScrMap`.", "Commencer le scripting", "Motifs courants", "Confirmé dans le scripting guide et Getting Started — pas inventé. Table complète : [Common patterns](/scripting/common-patterns/).", "Architecture", "Les groupes user-module listés sur le hub Scripting (Menu, Energy, Hands, Datamine, Distortion, …) **n’ont pas été écrits** comme articles. Ils restent undocumented ici."),
            ("it", "La logica di mappa SOMA è AngelScript in file `.hps`. Una mappa `sample_map.hpm` carica `sample_map.hps` accanto. Il passo script di Getting Started cambia solo `OnStart()` nella classe generata `cScrMap`.", "Iniziare lo scripting", "Schemi comuni", "Confermato nella scripting guide e in Getting Started — non inventato. Tabella completa: [Common patterns](/scripting/common-patterns/).", "Architettura", "I gruppi user-module elencati sull’hub Scripting (Menu, Energy, Hands, Datamine, Distortion, …) **non sono stati scritti** come articoli. Restano undocumented qui."),
            ("es", "La lógica de mapa de SOMA es AngelScript en archivos `.hps`. Un mapa `sample_map.hpm` carga `sample_map.hps` al lado. El paso de script de Getting Started solo cambia `OnStart()` dentro de la clase generada `cScrMap`.", "Empezar scripting", "Patrones comunes", "Confirmado en la scripting guide y Getting Started — no inventado. Tabla completa: [Common patterns](/scripting/common-patterns/).", "Arquitectura", "Los grupos user-module listados en el hub Scripting (Menu, Energy, Hands, Datamine, Distortion, …) **no se escribieron** como artículos. Aquí siguen undocumented."),
        ]
    },
)

# Remaining simpler hubs
LB_BASICS = [
    ("/level-building/working-with-primitives/", "Primitives", "Box / plane / cylinder geometry in the map."),
    ("/level-building/working-with-static-objects/", "Static objects", "Non-interactive mesh pieces."),
    ("/level-building/working-with-entities/", "Entities in the level", "Place Model Editor objects into the map."),
    ("/level-building/detail-meshes/", "Detail meshes", "Scatter / decoration meshes."),
    ("/level-building/detail-mesh-entity/", "Detail mesh entity", "Entity wrapper for detail meshes."),
    ("/level-editor/compounds/", "Compounds", "Group objects in the Level Editor."),
]
LB_WORLD = [
    ("/level-building/lights-overview/", "Lights", "Overview of light types."),
    ("/level-building/point-lights/", "Point lights", "Omnidirectional lights."),
    ("/level-building/spot-lights/", "Spot lights", "Directed lights."),
    ("/level-building/light-masks/", "Light masks", "Restrict light to geometry."),
    ("/level-building/terrain-editor-overview/", "Terrain", "Height map, painting, texturing, undergrowth."),
    ("/level-building/fog-areas/", "Fog", "Local volumes. Also [Fog Area](/areas/fog-area/)."),
    ("/level-building/billboards/", "Billboards", "Camera-facing sprites."),
    ("/level-building/lens-flares/", "Lens flares", "Flare objects."),
    ("/level-building/decals/", "Decals", "Projected surface detail."),
    ("/level-building/particles/", "Particles (level)", "Place particle systems."),
    ("/level-building/sounds/", "Sounds (level)", "Place sound entities."),
    ("/generated/color-grading/", "Color grading", "Shared HPL3 page."),
]
LB_TECH = [
    ("/level-building/indoor-level-performance/", "Indoor performance", "Indoor notes from the Wiki."),
    ("/level-building/outdoor-level-performance/", "Outdoor performance", "Outdoor notes from the Wiki."),
    ("/level-building/exposure-areas/", "Exposure areas", "Level-design exposure volumes."),
    (None, 'Visibility / MapTransfer <span class="legacy-tag">Wiki redlink</span>', "Named on the Areas hub. No articles."),
]

pack(
    "level-building",
    {
        loc: f"""{lead}

<p class="section-kicker">03 // LEVEL BUILDING &nbsp; REF 03.00</p>

## {hb}

{group(LB_BASICS)}

{red}

## {hw}

{group(LB_WORLD)}

{glob}

## {ht}

{group(LB_TECH)}

{close(loc, ["[Areas](/areas/)", "[Recipes](/recipes/)", "[Editor reference](/editors/)"], ["[HPL3/SOMA/Level Design](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design)"])}
"""
        for loc, lead, hb, red, hw, glob, ht in [
            ("ru", "Когда редактор привязан к моду, это слой world-building. Хром редактора: [Level Editor](/level-editor/) и [Editor reference](/editors/).", "Основы", "«Your first playable room» и «Combos» на исходном хабе — redlink.", "Мир", "Global spot light, SH probes, HDR, environment particles, creating terrain — **Wiki redlink**. Здесь не заполнены.", "Technical / optimization"),
            ("de", "Wenn der Editor am Mod hängt, ist das die World-Building-Schicht. Editor-Chrome unter [Level Editor](/level-editor/) und [Editor reference](/editors/).", "Grundlagen", "„Your first playable room“ und „Combos“ sind Redlinks auf dem Original-Hub.", "Welt", "Global spot light, SH probes, HDR, environment particles, creating terrain — **Wiki-Redlinks**. Hier nicht gefüllt.", "Technik / Optimierung"),
            ("fr", "Une fois l’éditeur attaché au mod, c’est la couche world-building. Le chrome éditeur est sous [Level Editor](/level-editor/) et [Editor reference](/editors/).", "Bases", "« Your first playable room » et « Combos » sont des redlinks sur le hub d’origine.", "Monde", "Global spot light, SH probes, HDR, environment particles, creating terrain — **redlinks Wiki**. Pas remplis ici.", "Technique / optimisation"),
            ("it", "Quando l’editor è collegato alla mod, questo è lo strato di world-building. Il chrome dell’editor sta sotto [Level Editor](/level-editor/) e [Editor reference](/editors/).", "Basi", "«Your first playable room» e «Combos» sono redlink sull’hub originale.", "Mondo", "Global spot light, SH probes, HDR, environment particles, creating terrain — **Wiki redlink**. Non riempiti qui.", "Tecnica / ottimizzazione"),
            ("es", "Cuando el editor está atado al mod, esta es la capa de world-building. El chrome del editor vive en [Level Editor](/level-editor/) y [Editor reference](/editors/).", "Básicos", "«Your first playable room» y «Combos» son redlinks en el hub original.", "Mundo", "Global spot light, SH probes, HDR, environment particles, creating terrain — **Wiki redlinks**. No se rellenan aquí.", "Técnico / optimización"),
        ]
    },
)

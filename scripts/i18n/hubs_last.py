"""Last TIER 1–2 hubs: debugging, glossary, recipes, helpers, entities, materials, particles, audio, dialogue."""

from __future__ import annotations

HUBS: dict[str, dict[str, str]] = {}
SRC = dict(ru="Источники", de="Quellen", fr="Sources", it="Fonti", es="Fuentes")
REL = dict(ru="Связанное", de="Siehe auch", fr="Voir aussi", it="Correlati", es="Relacionado")


def close(locale: str, related: list[str], sources: list[str]) -> str:
    out = [f"## {REL[locale]}", ""]
    out.extend(f"- {x}" for x in related)
    out += ["", f"## {SRC[locale]}", ""]
    out.extend(f"- {x}" for x in sources)
    return "\n".join(out) + "\n"


def pack(slug: str, data: dict[str, str]) -> None:
    HUBS[slug] = data


pack(
    "debugging",
    {
        loc: f"""{lead}

## {hfast}

1. {s1}
2. {s2}
3. {s3}
4. {s4}
5. {s5}

## {hsym}

| Symptom | Start here |
| --- | --- |
| {t1} | [Creating a mod](/modding/creating-a-mod/), [Launcher](/modding/soma-mod-launcher/), entry file name `entry.hpc` |
| {t2} | Same, plus [FAQ](/debugging/faq/) |
| {t3} | [Setup environment](/modding/setup-modding-environment/) — title bar must say `(Working on mod)` |
| Missing resources | [resources.cfg](/modding/creating-a-mod/), [Resources configuration](/generated/resources-configuration/) |
| Script compile error | [Add your first script](/start/add-your-first-script/), error list, [Hello World](/scripting/hello-world/) |
| {t4} | Keep `.hpm` and `.hpm_*` together |
| Entity not found | [Finding objects](/level-editor/finding-objects/), names in script vs editor |
| Area does not trigger | [Trigger Area](/areas/trigger-area/) — `CC_Entities` must include `player` if the player should fire it |
| Sound not playing | [Playing sounds](/audio/playing-sounds/), [Soundscape](/areas/soundscape-area/) |
| Texture / material | [Materials](/materials/) — many type pages are missing on the Wiki |
| Broken references | Re-open the editor on the mod; relative paths only |
| Performance | [Indoor](/level-building/indoor-level-performance/), [Outdoor](/level-building/outdoor-level-performance/) |
| Sticky area + static collider | [FAQ](/debugging/faq/) — wait on a timer |
| MoveObject and multi-body entities | [FAQ](/debugging/faq/) — `MainPhysicsBody` |
| Callback gets a wrong C++ return | [FAQ](/debugging/faq/) — store in a temporary |
| Lever interaction inverts | [FAQ](/debugging/faq/) |

{close(loc, [], ["Getting Started recovery sections", "[HPL3/Troubleshooting](https://wiki.frictionalgames.com/page/HPL3/Troubleshooting)", "[Developer Debug Menu](https://wiki.frictionalgames.com/page/HPL3/SOMA/Modding/Developer_Debug_Menu)"])}
"""
        for loc, lead, hfast, s1, s2, s3, s4, s5, hsym, t1, t2, t3, t4 in [
            ("ru", "Если шаг Getting Started падает — остановитесь там. Исходный путь сделан так, чтобы сбои лаунчера, редактора, карты и скрипта оставались разделимыми.", "Быстрый путь", "Убедитесь, что вы в **скопированном моде**, не в `MinimalCustomMapMod` и не в базовой игре.", "Запуск из SOMA mod launcher.", "В development mode нажмите **F1**: Show Error List, Show HPL Log ([Debug menu](/modding/developer-debug-menu/)).", "После правки скрипта **F5** перезагружает карту.", "Читайте [Developer commands](/modding/developer-commands/).", "Симптомы", "Мода нет в списке", "Мод не запускается", "Редактор не видит ассеты мода", "Карта не грузится"),
            ("de", "Wenn ein Getting-Started-Schritt scheitert, dort anhalten. Der Originalpfad trennt Launcher-, Editor-, Map- und Skriptfehler.", "Schnellpfad", "Bestätigen Sie, dass Sie in **Ihrer kopierten Mod** sind, nicht `MinimalCustomMapMod` und nicht das Basis-Spiel.", "Vom SOMA-Mod-Launcher starten.", "Im Development-Modus **F1**: Show Error List, Show HPL Log ([Debug menu](/modding/developer-debug-menu/)).", "**F5** lädt die Map nach einer Skriptänderung neu.", "[Developer commands](/modding/developer-commands/) lesen.", "Symptome", "Mod erscheint nicht", "Mod startet nicht", "Editor sieht keine Mod-Assets", "Map lädt nicht"),
            ("fr", "Si une étape de Getting Started échoue, arrêtez-vous là. Le parcours d’origine sépare les pannes launcher, éditeur, map et script.", "Chemin rapide", "Confirmez que vous êtes dans **votre mod copié**, pas `MinimalCustomMapMod` et pas le jeu de base.", "Lancer depuis le SOMA mod launcher.", "En development mode, **F1** : Show Error List, Show HPL Log ([Debug menu](/modding/developer-debug-menu/)).", "**F5** recharge la map après un changement de script.", "Lire [Developer commands](/modding/developer-commands/).", "Symptômes", "Le mod n’apparaît pas", "Le mod ne lance pas", "L’éditeur ne voit pas les assets du mod", "La map ne charge pas"),
            ("it", "Se un passo di Getting Started fallisce, fermati lì. Il percorso originale tiene separati i fallimenti di launcher, editor, mappa e script.", "Percorso veloce", "Conferma di essere nella **mod copiata**, non `MinimalCustomMapMod` e non il gioco base.", "Avvia dal SOMA mod launcher.", "In development mode premi **F1**: Show Error List, Show HPL Log ([Debug menu](/modding/developer-debug-menu/)).", "**F5** ricarica la mappa dopo un cambio di script.", "Leggi [Developer commands](/modding/developer-commands/).", "Sintomi", "La mod non compare", "La mod non si avvia", "L’editor non vede gli asset della mod", "La mappa non carica"),
            ("es", "Si un paso de Getting Started falla, párate ahí. El camino original separa fallos de launcher, editor, mapa y script.", "Camino rápido", "Confirma que estás en **tu mod copiado**, no `MinimalCustomMapMod` ni el juego base.", "Lanza desde el SOMA mod launcher.", "En development mode pulsa **F1**: Show Error List, Show HPL Log ([Debug menu](/modding/developer-debug-menu/)).", "**F5** recarga el mapa tras un cambio de script.", "Lee [Developer commands](/modding/developer-commands/).", "Síntomas", "El mod no aparece", "El mod no lanza", "El editor no ve assets del mod", "El mapa no carga"),
        ]
    },
)

pack(
    "glossary",
    {
        loc: f"""{lead}

## A

**Add-on** — {addon}

**Agent** — {agent}

**AngelScript** — {angelscript}

**Area** — {area}

## C

**Critter** — {critter}

## E

**Entity** — {entity}

**entry.hpc** — {hpc}

## H

**Helper** — {helper}

**HPL3** — {hpl3}

**HPM** — {hpm}

**HPS** — {hps}

## I

**ID handle** — {idh}

## M

**Mod** — {mod}

## P

**Prop** — {prop}

## R

**resources.cfg** — {res}

## S

**SH probe** — {sh}

**Stand-alone mod** — {stand}

**Static object** — {static}

## W

**WIP (source)** — {wips}

**WIP mod** — {wipm}

## Aliases

| Alias | See |
| --- | --- |
| Custom story | Stand-alone mod |
| Map script | `.hps` next to `.hpm` |
| Trigger | [Trigger Area](/areas/trigger-area/) |
| Soundscape | [Soundscape Area](/areas/soundscape-area/) |

{close(loc, [], ["[HPL3/SOMA/Glossary](https://wiki.frictionalgames.com/page/HPL3/SOMA/Glossary)"])}
"""
        for loc, lead, addon, agent, angelscript, area, critter, entity, hpc, helper, hpl3, hpm, hps, idh, mod, prop, res, sh, stand, static, wips, wipm in [
            ("ru", "Исходный [Glossary source](/generated/glossary-source/) помечен stub / under construction. Ниже только термины, которые эта страница или статьи Getting Started / Areas / Modding уже используют.", "Мод, который может идти вместе со stand-alone. См. [Creating a mod](/modding/creating-a-mod/).", "Entity врага/NPC.", "Язык скриптов `.hps`.", "Невидимый кубоид — I/O-объём HPL3. См. [Areas](/areas/).", "Мелкое фоновое существо без полного agent-скрипта.", "Объект мира с поведением. См. [Entities](/entities/).", "Файл входа мода.", "Общий include скрипта. Механизм: [Helper files](/scripting/helper-files/). Постраничные статьи helper: отсутствуют.", "Движок, с которым вышла SOMA. Не автоматически то же, что поздняя Amnesia «HPL3». См. [What is HPL3?](/start/what-is-hpl3/).", "Файл карты (`.hpm` + `.hpm_*`).", "Исходник AngelScript (`.hps`).", "Идентичность объекта движка из скрипта. [ID Handles](/scripting/id-handles/).", "Дополнительный контент в своей папке.", "Интерактивная Entity. Большинство Entity — props.", "Говорит движку, какие каталоги ресурсов искать.", "Spherical-harmonic lighting probe. Названа на хабе Level Design; статья SOMA — redlink.", "Мод с кастомными картами из SOMA mod launcher. В stub Glossary также custom story.", "Mesh для коллизии/вида без поведения Entity.", "Страница Wiki всё ещё переписывается. На импортированных страницах: `SOURCE STATUS: WIP`.", "Мод в разработке, в документах лаунчера."),
            ("de", "Die originale [Glossary source](/generated/glossary-source/) ist als Stub / under construction markiert. Darunter nur Begriffe, die diese Seite oder Getting Started / Areas / Modding bereits nutzen.", "Ein Mod, der mit einem Stand-alone-Mod mitlaufen kann. Siehe [Creating a mod](/modding/creating-a-mod/).", "Gegner-/NPC-Entity.", "Sprache der `.hps`-Skripte.", "Unsichtbarer Quader als I/O-Volumen von HPL3. Siehe [Areas](/areas/).", "Kleines Hintergrundwesen ohne volles Agent-Skript.", "Weltobjekt mit Verhalten. Siehe [Entities](/entities/).", "Mod-Entry-Datei.", "Geteiltes Skript-Include. Mechanismus: [Helper files](/scripting/helper-files/). Pro-Helper-Wiki-Seiten: fehlen.", "Engine, mit der SOMA ausgeliefert wurde. Nicht automatisch dasselbe wie späteres Amnesia-„HPL3“. Siehe [What is HPL3?](/start/what-is-hpl3/).", "Map-Datei (`.hpm` + `.hpm_*`).", "AngelScript-Quelle (`.hps`).", "Skriptidentität für ein Engine-Objekt. [ID Handles](/scripting/id-handles/).", "Extra-Inhalt im eigenen Ordner.", "Interaktive Entity. Die meisten Entities sind Props.", "Sagt der Engine, welche Ressourcenverzeichnisse zu durchsuchen sind.", "Spherical-harmonic lighting probe. Auf dem Level-Design-Hub genannt; SOMA-Artikel ist ein Redlink.", "Custom-Map-Mod, gestartet aus dem SOMA-Mod-Launcher. Im Glossary-Stub auch custom story genannt.", "Mesh für Kollision/Visuals ohne Entity-Verhalten.", "Wiki-Seite wird noch umgeschrieben. Auf importierten Seiten: `SOURCE STATUS: WIP`.", "Mod in Entwicklung, in Launcher/Setup-Docs."),
            ("fr", "La [Glossary source](/generated/glossary-source/) d’origine est marked stub / under construction. Ci-dessous uniquement les termes que cette page ou Getting Started / Areas / Modding utilisent déjà.", "Un mod qui peut tourner avec un stand-alone. Voir [Creating a mod](/modding/creating-a-mod/).", "Entity ennemi/NPC.", "Langage des scripts `.hps`.", "Cuboïde invisible, volume I/O de HPL3. Voir [Areas](/areas/).", "Petite créature de fond sans script agent complet.", "Objet du monde avec comportement. Voir [Entities](/entities/).", "Fichier d’entrée du mod.", "Include de script partagé. Mécanisme : [Helper files](/scripting/helper-files/). Pages Wiki par helper : absentes.", "Moteur livré avec SOMA. Pas automatiquement le même que l’« HPL3 » Amnesia plus tardif. Voir [What is HPL3?](/start/what-is-hpl3/).", "Fichier de map (`.hpm` + `.hpm_*`).", "Source AngelScript (`.hps`).", "Identité script d’un objet moteur. [ID Handles](/scripting/id-handles/).", "Contenu extra dans son propre dossier.", "Entity interactive. La plupart des Entity sont des props.", "Indique au moteur quels répertoires de ressources chercher.", "Spherical-harmonic lighting probe. Nommée sur le hub Level Design ; l’article SOMA est un redlink.", "Mod de maps custom lancé depuis le SOMA mod launcher. Aussi appelé custom story dans le stub Glossary.", "Mesh collision/visuel sans comportement Entity.", "Page Wiki encore en réécriture. Sur les pages importées : `SOURCE STATUS: WIP`.", "Mod en développement, dans les docs launcher/setup."),
            ("it", "La [Glossary source](/generated/glossary-source/) originale è marked stub / under construction. Sotto solo i termini che quella pagina o Getting Started / Areas / Modding già usano.", "Una mod che può girare insieme a una stand-alone. Vedi [Creating a mod](/modding/creating-a-mod/).", "Entity nemico/NPC.", "Linguaggio degli script `.hps`.", "Cuboide invisibile, volume I/O di HPL3. Vedi [Areas](/areas/).", "Piccola creatura di sfondo senza script agent completo.", "Oggetto di mondo con comportamento. Vedi [Entities](/entities/).", "File di entry della mod.", "Include di script condiviso. Meccanismo: [Helper files](/scripting/helper-files/). Pagine Wiki per helper: mancanti.", "Motore con cui è uscita SOMA. Non automaticamente lo stesso «HPL3» di Amnesia successiva. Vedi [What is HPL3?](/start/what-is-hpl3/).", "File mappa (`.hpm` + `.hpm_*`).", "Sorgente AngelScript (`.hps`).", "Identità script di un oggetto motore. [ID Handles](/scripting/id-handles/).", "Contenuto extra nella propria cartella.", "Entity interattiva. La maggior parte delle Entity sono props.", "Dice al motore quali directory di risorse cercare.", "Spherical-harmonic lighting probe. Nominata sull’hub Level Design; l’articolo SOMA è un redlink.", "Mod di mappe custom avviata dal SOMA mod launcher. Nel stub Glossary anche custom story.", "Mesh di collisione/visuale senza comportamento Entity.", "Pagina Wiki ancora in riscrittura. Sulle pagine importate: `SOURCE STATUS: WIP`.", "Mod in sviluppo, nei documenti launcher/setup."),
            ("es", "La [Glossary source](/generated/glossary-source/) original está marked stub / under construction. Abajo solo términos que esa página o Getting Started / Areas / Modding ya usan.", "Un mod que puede ir junto a un stand-alone. Véase [Creating a mod](/modding/creating-a-mod/).", "Entity enemigo/NPC.", "Lenguaje de los scripts `.hps`.", "Cuboide invisible, volumen I/O de HPL3. Véase [Areas](/areas/).", "Criatura de fondo pequeña sin script agent completo.", "Objeto de mundo con comportamiento. Véase [Entities](/entities/).", "Archivo de entrada del mod.", "Include de script compartido. Mecanismo: [Helper files](/scripting/helper-files/). Páginas Wiki por helper: faltan.", "Motor con el que salió SOMA. No automáticamente el mismo «HPL3» de Amnesia posterior. Véase [What is HPL3?](/start/what-is-hpl3/).", "Archivo de mapa (`.hpm` + `.hpm_*`).", "Fuente AngelScript (`.hps`).", "Identidad de script de un objeto del motor. [ID Handles](/scripting/id-handles/).", "Contenido extra en su propia carpeta.", "Entity interactiva. La mayoría de Entity son props.", "Le dice al motor qué directorios de recursos buscar.", "Spherical-harmonic lighting probe. Nombrada en el hub Level Design; el artículo SOMA es un redlink.", "Mod de mapas custom lanzado desde el SOMA mod launcher. En el stub Glossary también custom story.", "Mesh de colisión/visual sin comportamiento Entity.", "Página Wiki aún reescribiéndose. En páginas importadas: `SOURCE STATUS: WIP`.", "Mod en desarrollo, en docs de launcher/setup."),
        ]
    },
)

pack(
    "recipes",
    {
        loc: f"""{lead}

| {want} | Recipe |
| --- | --- |
| {r1} | [First mod](/recipes/first-mod/) |
| {r2} | [PlayerStart](/recipes/player-start/) |
| {r3} | [Enter Area](/recipes/enter-area/) |
| {r4} | [First script](/recipes/first-script/) |
| {r5} | [Timer](/recipes/timer/) |
| {r6} | [Debug a script](/recipes/debug-script/) |
| {r7} | [Fog](/recipes/fog/) |
| {r8} | [Play a sound](/recipes/play-sound/) |
| {r9} | [Import a model](/recipes/import-model/) |
| {r10} | [Interactive entity](/recipes/interactive-entity/) |
| {r11} | [Material](/recipes/create-material/) |
| {r12} | [Particle](/recipes/particle/) |
| {r13} | [Indoor](/level-building/indoor-level-performance/), [Outdoor](/level-building/outdoor-level-performance/) |

{omit}
"""
        for loc, lead, want, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, omit in [
            ("ru", "Это не второй API. Рецепты сшивают страницы, которые у вас уже есть.", "Хочу…", "Создать первый мод", "Поставить игрока", "Реакция на вход в объём", "Напечатать Hello World", "Использовать timer", "Отладить скрипт", "Атмосфера fog", "Проиграть звук", "Импортировать модель", "Сделать Entity интерактивной", "Создать материал", "Базовый particle", "Оптимизировать indoor / outdoor", "Рецепты, которым нужны недокументированные шаги Wiki (sequences в полном катсцене, SH probes, Sit Area, списки функций helper), намеренно опущены."),
            ("de", "Das ist keine zweite API. Rezepte verbinden Seiten, die Sie schon haben.", "Ich will…", "Meinen ersten Mod anlegen", "Den Spieler irgendwo starten", "Reagieren, wenn der Spieler ein Volumen betritt", "Hello World ausgeben", "Einen Timer nutzen", "Ein Skript debuggen", "Atmosphäre mit Fog", "Einen Sound abspielen", "Ein Modell importieren", "Eine Entity interaktiv machen", "Ein Material anlegen", "Ein Basis-Particle", "Indoor / Outdoor optimieren", "Rezepte, die undokumentierte Wiki-Schritte bräuchten (Sequences in einem vollen Cutscene, SH probes, Sit Area, Helper-Funktionslisten), sind absichtlich weggelassen."),
            ("fr", "Ce n’est pas une seconde API. Les recettes recousent des pages que vous avez déjà.", "Je veux…", "Créer mon premier mod", "Faire démarrer le joueur quelque part", "Réagir quand le joueur entre dans un volume", "Afficher Hello World", "Utiliser un timer", "Déboguer un script", "Créer de l’atmosphère avec du fog", "Jouer un son", "Importer un modèle", "Rendre une Entity interactive", "Créer un matériau", "Faire un particle de base", "Optimiser indoor / outdoor", "Les recettes qui exigeraient des étapes Wiki non documentées (sequences dans une cutscene complète, SH probes, Sit Area, listes de fonctions helper) sont omises exprès."),
            ("it", "Non è una seconda API. Le ricette cuciono pagine che hai già.", "Voglio…", "Creare la mia prima mod", "Far partire il giocatore da qualche parte", "Reagire quando il giocatore entra in un volume", "Stampare Hello World", "Usare un timer", "Debuggare uno script", "Creare atmosfera con fog", "Riprodurre un suono", "Importare un modello", "Rendere interattiva un’Entity", "Creare un materiale", "Fare un particle di base", "Ottimizzare indoor / outdoor", "Le ricette che richiederebbero passi Wiki non documentati (sequences in una cutscene piena, SH probes, Sit Area, elenchi di funzioni helper) sono omesse di proposito."),
            ("es", "Esto no es una segunda API. Las recetas cosen páginas que ya tienes.", "Quiero…", "Crear mi primer mod", "Arrancar al jugador en un sitio", "Reaccionar cuando el jugador entra en un volumen", "Imprimir Hello World", "Usar un timer", "Depurar un script", "Crear atmósfera con fog", "Reproducir un sonido", "Importar un modelo", "Hacer una Entity interactiva", "Crear un material", "Hacer un particle básico", "Optimizar indoor / outdoor", "Las recetas que exigirían pasos Wiki no documentados (sequences en un corte completo, SH probes, Sit Area, listas de funciones helper) se omiten a propósito."),
        ]
    },
)

HELPER_ROWS = """
| Helper | Wiki link status | Typical use (from the name / hub only) |
| --- | --- | --- |
| Game Helper | Redlink | Game-wide helpers |
| Map Helper | Redlink | Map helpers |
| Player Helper | Redlink | Player helpers |
| Audio Helper | Redlink | Audio helpers — see also [Audio](/audio/) |
| Effects Helper | Redlink | Screen/world effects |
| Areas Helper | Redlink | The Trigger article names `helper_area.hps` |
| AI Helper | Redlink | Agents / pathing |
| Modules Helper | Redlink | User modules |
| Physics Helper | Redlink | Bodies / joints |
| Props Helper | Redlink | Prop entities |
| Sequences Helper | Redlink | Sequence playback |
| General Helper | Redlink (hub spelling: "Geneal Helper") | General utilities |
| ImGui Helper | Redlink | ImGui wrappers — see `cImGui` in the [API](/api/) |
| EventDB Helper | Redlink | Event database |
"""

pack(
    "scripting/helpers",
    {
        loc: f"""{lead}

:::note[Documentation status]
{note}
:::

## {hcats}

{HELPER_ROWS}

## {hinstead}

- {a}
- {b}
- {c}

{close(loc, [], ["[HPL3/SOMA/Scripting](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting) hub table", "[HPL3/Scripting/Scripting Guide/Helper Files](https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Helper_Files)", "[HPL3/Areas/Trigger Area](https://wiki.frictionalgames.com/page/HPL3/Areas/Trigger_Area) (`helper_area.hps`)"])}
"""
        for loc, lead, note, hcats, hinstead, a, b, c in [
            ("ru", "Хаб Scripting SOMA перечисляет эти группы helper и указывает на файлы `helper_*.hps`. **Ни одной постраничной статьи helper на Wiki нет** (redlink). [Helper Files](/scripting/helper-files/) объясняет механизм include. Он не документирует каждую функцию этих файлов.", "Undocumented в исходной Frictional Wiki. Таблица — каталог имён, которые хаб уже напечатал. Сигнатуры функций здесь не выдуманы.", "Категории, названные хабом", "Что можно сделать вместо этого", "Читать [Helper Files](/scripting/helper-files/) — как работают include.", "Открыть файлы `helper_*.hps`, которые идут с SOMA — Wiki их не воспроизводит.", "Искать в [API](/api/) `cLux_`, `Entity_`, `Map_`, `Prop_`, когда нужны функции движка, а не helper."),
            ("de", "Der SOMA-Scripting-Hub listet diese Helper-Gruppen und zeigt auf `helper_*.hps`. **Keine der Helper-Wiki-Seiten existiert** (Redlinks). [Helper Files](/scripting/helper-files/) erklärt den Include-Mechanismus. Es dokumentiert nicht jede Funktion in diesen Dateien.", "Im originalen Frictional Wiki undokumentiert. Die Tabelle ist ein Katalog der Namen, die der Hub bereits gedruckt hat. Funktionssignaturen werden hier nicht erfunden.", "Vom Hub genannte Kategorien", "Was Sie stattdessen tun können", "[Helper Files](/scripting/helper-files/) lesen — wie Includes funktionieren.", "Die mit SOMA gelieferten `helper_*.hps` öffnen — das Wiki reproduziert sie nicht.", "Die [API](/api/) nach `cLux_`, `Entity_`, `Map_`, `Prop_` durchsuchen, wenn Sie Engine-Funktionen statt Helper brauchen."),
            ("fr", "Le hub Scripting SOMA liste ces groupes helper et pointe vers `helper_*.hps`. **Aucune des pages Wiki par helper n’existe** (redlinks). [Helper Files](/scripting/helper-files/) explique le mécanisme d’include. Il ne documente pas chaque fonction de ces fichiers.", "Non documenté dans le Frictional Wiki d’origine. La table est un catalogue de noms que le hub a déjà imprimés. Les signatures de fonction ne sont pas inventées ici.", "Catégories nommées par le hub", "Que faire à la place", "Lire [Helper Files](/scripting/helper-files/) pour le fonctionnement des includes.", "Ouvrir les `helper_*.hps` livrés avec SOMA — le Wiki ne les reproduit pas.", "Chercher dans l’[API](/api/) `cLux_`, `Entity_`, `Map_`, `Prop_` quand vous voulez des fonctions moteur plutôt que des helpers."),
            ("it", "L’hub Scripting SOMA elenca questi gruppi helper e punta a `helper_*.hps`. **Nessuna delle pagine Wiki per helper esiste** (redlink). [Helper Files](/scripting/helper-files/) spiega il meccanismo include. Non documenta ogni funzione di quei file.", "Undocumented nel Frictional Wiki originale. La tabella è un catalogo di nomi che l’hub ha già stampato. Le firme di funzione non sono inventate qui.", "Categorie nominate dall’hub", "Cosa fare invece", "Leggi [Helper Files](/scripting/helper-files/) per come funzionano gli include.", "Apri i file `helper_*.hps` che arrivano con SOMA — il Wiki non li riproduce.", "Cerca nell’[API](/api/) `cLux_`, `Entity_`, `Map_`, `Prop_` quando ti servono funzioni del motore piuttosto che helper."),
            ("es", "El hub Scripting de SOMA lista estos grupos helper y apunta a `helper_*.hps`. **Ninguna de las páginas Wiki por helper existe** (redlinks). [Helper Files](/scripting/helper-files/) explica el mecanismo include. No documenta cada función de esos archivos.", "Undocumented en el Frictional Wiki original. La tabla es un catálogo de nombres que el hub ya imprimió. Las firmas de función no se inventan aquí.", "Categorías que nombra el hub", "Qué hacer en su lugar", "Lee [Helper Files](/scripting/helper-files/) para cómo funcionan los includes.", "Abre los `helper_*.hps` que vienen con SOMA — el Wiki no los reproduce.", "Busca en la [API](/api/) `cLux_`, `Entity_`, `Map_`, `Prop_` cuando necesites funciones del motor en vez de helpers."),
        ]
    },
)

pack(
    "entities",
    {
        loc: f"""{lead}

<p class="section-kicker">05 // ENTITIES &nbsp; REF 05.10</p>

## Model Editor

- [Entities overview](/entities/entities-overview/)
- [Model Editor view](/entities/model-editor-view/)
- [Outline](/entities/model-editor-outline/)
- [Entity settings](/entities/entity-settings/)
- [Entity notes](/entities/entity-notes/)
- [Mesh](/entities/entity-mesh/)
- [Rig](/entities/entity-rig/)
- [Entity types](/entities/entity-types/)
- [Preview settings](/entities/model-preview-settings/)
- [Shapes](/entities/working-with-shapes/)

## {hphys}

- [Physics body properties](/entities/physics-body-properties/)
- [Joints](/entities/working-with-joints/)
- [Adding animations](/entities/adding-animations-to-entities/)

{place}

{close(loc, ["[Asset pipeline](/assets/)", "[Props in the API](/api/categories/prop/)", "[Recipe: interactive entity](/recipes/interactive-entity/)"], ["[HPL3/SOMA/Entities](https://wiki.frictionalgames.com/page/HPL3/SOMA/Entities)", "[HPL3/Entities/Entities Overview](https://wiki.frictionalgames.com/page/HPL3/Entities/Entities_Overview)"])}
"""
        for loc, lead, hphys, place in [
            ("ru", " **Entity** — объект мира с поведением. Большинство интерактивных — **props**. Agent — Entity врага/NPC. Critter — мелкое фоновое существо.", "Физика и анимация", "Размещайте Entity на карте через [Working with entities](/level-building/working-with-entities/)."),
            ("de", "Eine **Entity** ist ein Weltobjekt mit Verhalten. Die meisten interaktiven sind **Props**. Agents sind NPC-/Gegner-Entities. Critters sind kleine Hintergrundwesen.", "Physik und Animation", "Entities in der Map platzieren mit [Working with entities](/level-building/working-with-entities/)."),
            ("fr", "Une **Entity** est un objet du monde avec un comportement. La plupart des interactifs sont des **props**. Les Agent sont des Entity NPC/ennemi. Les Critter sont de petites créatures de fond.", "Physique et animation", "Placez les Entity dans la map avec [Working with entities](/level-building/working-with-entities/)."),
            ("it", "Un’**Entity** è un oggetto di mondo con comportamento. La maggior parte degli interattivi sono **props**. Gli Agent sono Entity NPC/nemico. I Critter sono piccole creature di sfondo.", "Fisica e animazione", "Piazza le Entity nella mappa con [Working with entities](/level-building/working-with-entities/)."),
            ("es", "Una **Entity** es un objeto de mundo con comportamiento. La mayoría de las interactivas son **props**. Los Agent son Entity NPC/enemigo. Los Critter son criaturas de fondo pequeñas.", "Física y animación", "Coloca Entity en el mapa con [Working with entities](/level-building/working-with-entities/)."),
        ]
    },
)

pack(
    "materials",
    {
        loc: f"""{lead}

<p class="section-kicker">05 // MATERIALS &nbsp; REF 05.20</p>

## {hexist}

- [Materials overview](/materials/materials-overview/)
- [Engine materials](/materials/engine-materials/)
- [Working with materials](/materials/working-with-materials/)
- [Material Editor view](/materials/materials-editor-view/)
- [Material specific variables](/materials/material-specific-variables/) — {empty}
- [Translucent](/materials/translucent/) — {only}

## {hnamed}

{hub}

**Types:** Decal, Projected UV, Solid Diffuse, Terrain, Terrain Decal, Water.

**Blend modes:** Add, Mul, Mulx2, Alpha, PremulAlpha.

**Also listed, no page:** Texture maps, Physics material, UV animations, Texture units.

{close(loc, ["[Asset pipeline](/assets/)", "[Entities](/entities/)", "[Recipe: create a material](/recipes/create-material/)"], ["[HPL3/Materials](https://wiki.frictionalgames.com/page/HPL3/Materials)", "[HPL3/SOMA/Materials](https://wiki.frictionalgames.com/page/HPL3/SOMA/Materials)"])}
"""
        for loc, lead, hexist, empty, only, hnamed, hub in [
            ("ru", "Материалы соединяют текстуры и шейдеры. Хаб Materials SOMA подключает общую категорию HPL3 Materials, помеченную under construction.", "Что есть", "страница есть, но в источнике пустая", "единственная статья *типа* материала, которая существует", "Названо на хабе, статьи нет", "Хаб это перечисляет. **Страницы Wiki нет**. Параметры здесь не выдуманы."),
            ("de", "Materials kombinieren Texturen und Shader. Der SOMA-Materials-Hub transkludiert die gemeinsame HPL3-Materials-Kategorie, die under construction markiert ist.", "Was existiert", "Seite existiert, ist in der Quelle aber leer", "der einzige Material-*Typ*-Artikel, der existiert", "Auf dem Hub genannt, kein Artikel", "Der Hub listet das. **Keine Wiki-Seite**. Parameter werden hier nicht erfunden."),
            ("fr", "Les matériaux combinent textures et shaders. Le hub Materials SOMA transclut la catégorie HPL3 Materials partagée, marked under construction.", "Ce qui existe", "la page existe mais est vide dans la source", "le seul article de *type* de matériau qui existe", "Nommés sur le hub, pas d’article", "Le hub les liste. **Pas de page Wiki**. Les paramètres ne sont pas inventés ici."),
            ("it", "I materiali combinano texture e shader. L’hub Materials SOMA transclude la categoria HPL3 Materials condivisa, marked under construction.", "Cosa esiste", "la pagina esiste ma è vuota nella fonte", "l’unico articolo di *tipo* materiale che esiste", "Nominati sull’hub, nessun articolo", "L’hub li elenca. **Nessuna pagina Wiki**. I parametri non sono inventati qui."),
            ("es", "Los materiales combinan texturas y shaders. El hub Materials de SOMA transcluye la categoría HPL3 Materials compartida, marked under construction.", "Qué existe", "la página existe pero está vacía en la fuente", "el único artículo de *tipo* de material que existe", "Nombrados en el hub, sin artículo", "El hub los lista. **No hay página Wiki**. Los parámetros no se inventan aquí."),
        ]
    },
)

pack(
    "particles",
    {
        loc: f"""{lead}

<p class="section-kicker">05 // PARTICLES &nbsp; REF 05.30</p>

## {hpath}

1. [Working with particles](/particles/working-with-particles/)
2. [Particle Editor view](/particles/particle-editor-view/)
3. [Emitter management](/particles/emitter-management/)
4. [General](/particles/particle-general/)
5. [Start state](/particles/particle-start/)
6. [Movement](/particles/particle-movement/)
7. [Rendering](/particles/particle-rendering/)
8. [Color](/particles/particle-color/)
9. [Rotation](/particles/particle-rotation/)
10. [Collision](/particles/particle-collision/)

**Redlinks on the hub:** Particles Overview, Particle Editor Controls.

## {hdbg}

{dbg}

{close(loc, ["[Recipe: basic particle](/recipes/particle/)", "[API: ParticleSystem](/api/categories/particlesystem/)"], ["[HPL3/Particles](https://wiki.frictionalgames.com/page/HPL3/Particles)"])}
"""
        for loc, lead, hpath, hdbg, dbg in [
            ("ru", "Системы частиц правят в Particle Editor и ставят на уровни. Хаб Particles SOMA подключает общую категорию HPL3 Particles (under construction).", "Путь обучения (страницы, которые есть)", "Чеклист отладки", "Если particle в игре ничего не делает, Wiki не даёт отдельного чеклиста. Пройдите страницы выше по порядку и убедитесь, что emitter реально стоит на уровне ([Particles in the level](/level-building/particles/)). Не додумывайте недостающие значения."),
            ("de", "Partikelsysteme werden im Particle Editor bearbeitet und in Levels platziert. Der SOMA-Particles-Hub transkludiert die gemeinsame HPL3-Particles-Kategorie (under construction).", "Lernpfad (Seiten, die existieren)", "Debug-Checkliste", "Wenn ein Particle in-game nichts tut, gibt das Wiki keine eigene Checkliste. Die Seiten oben der Reihe nach gehen und prüfen, dass der Emitter wirklich im Level liegt ([Particles in the level](/level-building/particles/)). Fehlende Werte nicht annehmen."),
            ("fr", "Les systèmes de particules s’éditent dans le Particle Editor et se placent dans les niveaux. Le hub Particles SOMA transclut la catégorie HPL3 Particles partagée (under construction).", "Parcours (pages qui existent)", "Checklist de débogage", "Quand un particle ne fait rien in-game, le Wiki n’offre pas de checklist dédiée. Parcourez les pages ci-dessus dans l’ordre et confirmez que l’emitter est réellement placé dans le niveau ([Particles in the level](/level-building/particles/)). N’inventez pas les valeurs manquantes."),
            ("it", "I sistemi di particelle si editano nel Particle Editor e si piazzano nei livelli. L’hub Particles SOMA transclude la categoria HPL3 Particles condivisa (under construction).", "Percorso (pagine che esistono)", "Checklist di debug", "Quando un particle in-game non fa nulla, il Wiki non dà una checklist dedicata. Percorri le pagine sopra in ordine e conferma che l’emitter sia davvero piazzato nel livello ([Particles in the level](/level-building/particles/)). Non assumere valori mancanti."),
            ("es", "Los sistemas de partículas se editan en el Particle Editor y se colocan en niveles. El hub Particles de SOMA transcluye la categoría HPL3 Particles compartida (under construction).", "Ruta de aprendizaje (páginas que existen)", "Checklist de depuración", "Cuando un particle no hace nada in-game, el Wiki no da una checklist dedicada. Recorre las páginas de arriba en orden y confirma que el emitter está realmente colocado en el nivel ([Particles in the level](/level-building/particles/)). No asumas valores que faltan."),
        ]
    },
)

pack(
    "audio",
    {
        loc: f"""{lead}

## {hexist}

- [Working with / playing sounds](/audio/playing-sounds/)
- [FMOD Designer 2010](/audio/working-with-fmod-designer-2010/)
- [Sounds in the level](/level-building/sounds/)
- [Soundscape Area](/areas/soundscape-area/)
- [Audio helper](/scripting/helpers/) — {cat}

{tools}

{close(loc, ["[Recipe: play a sound](/recipes/play-sound/)", "[API: cSound](/api/) (filter `cSound`)"], ["[HPL3/SOMA/Sound](https://wiki.frictionalgames.com/page/HPL3/SOMA/Sound)", "[HPL3/Sound/Playing Sounds](https://wiki.frictionalgames.com/page/HPL3/Sound/Playing_Sounds)"])}
"""
        for loc, lead, hexist, cat, tools in [
            ("ru", "Хаб Sound SOMA — under construction. Он указывает на несколько страниц, которых нет (`Sound Overview`, `Playing Music`).", "Что есть", "только имя категории; статьи нет", "Инструменты, названные хабом: FMOD Designer 2010 (legacy), Audacity. См. [Tools](/tools/)."),
            ("de", "Der SOMA-Sound-Hub ist under construction. Er zeigt auf mehrere Seiten, die nicht existieren (`Sound Overview`, `Playing Music`).", "Was existiert", "nur Kategoriename; kein Artikel", "Vom Hub genannte Tools: FMOD Designer 2010 (Legacy), Audacity. Siehe [Tools](/tools/)."),
            ("fr", "Le hub Sound SOMA est under construction. Il pointe vers plusieurs pages qui n’existent pas (`Sound Overview`, `Playing Music`).", "Ce qui existe", "nom de catégorie seulement ; pas d’article", "Outils nommés par le hub : FMOD Designer 2010 (legacy), Audacity. Voir [Tools](/tools/)."),
            ("it", "L’hub Sound SOMA è under construction. Punta a diverse pagine che non esistono (`Sound Overview`, `Playing Music`).", "Cosa esiste", "solo nome di categoria; nessun articolo", "Strumenti nominati dall’hub: FMOD Designer 2010 (legacy), Audacity. Vedi [Tools](/tools/)."),
            ("es", "El hub Sound de SOMA está under construction. Apunta a varias páginas que no existen (`Sound Overview`, `Playing Music`).", "Qué existe", "solo nombre de categoría; sin artículo", "Herramientas que nombra el hub: FMOD Designer 2010 (legacy), Audacity. Véase [Tools](/tools/)."),
        ]
    },
)

pack(
    "dialogue",
    {
        loc: f"""{lead}

- [Audition overview](/dialogue/audition-overview/)
- [Lip sync](/dialogue/lip-sync/)
- [Voice handler overview](/dialogue/voice-handler-overview/)

{extra}

## {hflow}

{flow}

{close(loc, ["[Audio](/audio/)", "[Lip sync on entities](/dialogue/lip-sync/)"], ["[HPL3/SOMA/Audition](https://wiki.frictionalgames.com/page/HPL3/SOMA/Audition)"])}
"""
        for loc, lead, extra, hflow, flow in [
            ("ru", "Голосовая работа в SOMA идёт через Audition. Страницы, которые есть:", "Исходный хаб Audition также называет Conversations, Voice Settings и Voice Subjects частью системы. Отдельных статей на эти имена в импортированном дереве не было; это термины обзорных страниц, не отдельные мануалы.", "Workflow (только шаги, которые обзоры подтверждают)", "Voice file → Audition → conversation / subject setup, как на этих страницах → триггер в игре (script или Area — см. handler overview, не выдумывайте имя callback, которого Wiki не печатает)."),
            ("de", "Voice-Arbeit in SOMA läuft über Audition. Seiten, die existieren:", "Der originale Audition-Hub nennt auch Conversations, Voice Settings und Voice Subjects als Teil des Systems. Eigene Artikel für diese Namen waren im Importbaum nicht; Begriffe der Übersicht, keine Extra-Handbücher.", "Workflow (nur Schritte, die die Overviews tragen)", "Voice file → Audition → Conversation-/Subject-Setup wie auf diesen Seiten → Trigger im Spiel (Skript oder Area — siehe Handler-Overview, keinen callback-Namen annehmen, den das Wiki nicht druckt)."),
            ("fr", "Le travail voix dans SOMA passe par Audition. Pages qui existent :", "Le hub Audition d’origine nomme aussi Conversations, Voice Settings et Voice Subjects. Pas d’articles dédiés dans l’arbre importé ; ce sont des termes des overviews, pas des manuels extra.", "Workflow (uniquement les étapes que les overviews supportent)", "Fichier voix → Audition → conversation / subject setup décrit sur ces pages → trigger in-game (script ou Area — voir le handler overview, n’inventez pas un nom de callback que le Wiki n’imprime pas)."),
            ("it", "Il lavoro vocale in SOMA passa da Audition. Pagine che esistono:", "L’hub Audition originale nomina anche Conversations, Voice Settings e Voice Subjects. Articoli dedicati a quei nomi non c’erano nell’albero importato; sono termini delle overview, non manuali extra.", "Workflow (solo i passi che le overview supportano)", "File voce → Audition → conversation / subject setup descritto in quelle pagine → trigger in gioco (script o Area — vedi l’handler overview, non assumere un nome di callback che il Wiki non stampa)."),
            ("es", "El trabajo de voz en SOMA pasa por Audition. Páginas que existen:", "El hub Audition original también nombra Conversations, Voice Settings y Voice Subjects. No había artículos dedicados a esos nombres en el árbol importado; son términos de las overviews, no manuales extra.", "Workflow (solo pasos que sostienen las overviews)", "Archivo de voz → Audition → conversation / subject setup descrito en esas páginas → trigger in-game (script o Area — véase el handler overview, no asumas un nombre de callback que el Wiki no imprime)."),
        ]
    },
)

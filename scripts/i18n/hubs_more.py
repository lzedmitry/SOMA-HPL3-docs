"""Catalog-style TIER 1–2 hubs. Prose translated; identifiers and paths stay English."""

from __future__ import annotations

HUBS: dict[str, dict[str, str]] = {}

SRC = dict(ru="Источники", de="Quellen", fr="Sources", it="Fonti", es="Fuentes")
REL = dict(ru="Связанное", de="Siehe auch", fr="Voir aussi", it="Correlati", es="Relacionado")


def row(href: str, label: str, hint: str) -> str:
    return f'<div class="catalog-row"><a href="{href}">{label}</a><span>{hint}</span></div>'


def group(rows: list[tuple[str, str, str]]) -> str:
    return '<div class="catalog-group">\n' + "\n".join(row(*r) for r in rows) + "\n</div>\n"


def pack(slug: str, blocks: dict[str, str]) -> None:
    HUBS[slug] = blocks


def close(locale: str, related: list[str], sources: list[str]) -> str:
    out = [f"## {REL[locale]}", ""]
    out.extend(f"- {x}" for x in related)
    out += ["", f"## {SRC[locale]}", ""]
    out.extend(f"- {x}" for x in sources)
    out.append("")
    return "\n".join(out)


# ----- modding -----
pack(
    "modding",
    {
        loc: "\n".join(
            [
                lead,
                "",
                f"## {h1}",
                "",
                "1. [Creating a mod](/modding/creating-a-mod/) — types, folder tree, `entry.hpc`, `resources.cfg`",
                "2. [MinimalCustomMapMod](/modding/minimalcustommapmod/) — the Getting Started base",
                "3. [MinimalAddOnMod](/modding/minimaladdonmod/)",
                "4. [SOMA Mod Launcher](/modding/soma-mod-launcher/)",
                "5. [Setup modding environment](/modding/setup-modding-environment/) — Level Editor on the mod",
                "6. [Mod dependencies](/modding/mod-dependencies/)",
                "",
                f"## {h2}",
                "",
                "- [Developer commands](/modding/developer-commands/)",
                "- [Developer debug menu](/modding/developer-debug-menu/)",
                "- [Non-safe mode menu](/modding/non-safe-mode-menu/)",
                "- [Language configuration](/generated/language-configuration/)",
                "- [Launch configuration](/generated/launch-configuration/)",
                "- [Resources configuration](/generated/resources-configuration/)",
                "",
                f"## {h3}",
                "",
                dist,
                "",
                close(
                    loc,
                    ["[Getting Started](/start/)", "[Tools](/tools/)", "[Troubleshooting](/debugging/)"],
                    ["[HPL3/SOMA/Modding](https://wiki.frictionalgames.com/page/HPL3/SOMA/Modding)"],
                ),
            ]
        )
        for loc, lead, h1, h2, h3, dist in [
            (
                "ru",
                "Мод SOMA — это папка, которую видит лаунчер. Игра поставляет два рабочих примера: `MinimalCustomMapMod` и `MinimalAddOnMod`. Копируйте один из них, а не собирайте файлы с нуля.",
                "Создание мода",
                "Пока вы работаете",
                "Дистрибуция",
                "Исходный хаб Modding ссылается на несколько страниц, которых **нет** на Wiki (redlink): best practices, online presence, teamwork, repositories, content usage, pre-publication, distribution. Эти темы здесь не выдуманы. Используйте [Creating a mod](/modding/creating-a-mod/) и свой процесс упаковки, не забывая атрибуцию ([Licensing](/about/licensing/)).",
            ),
            (
                "de",
                "Ein SOMA-Mod ist ein Ordner, den der Launcher sehen kann. Das Spiel liefert zwei bekannte Beispiele: `MinimalCustomMapMod` und `MinimalAddOnMod`. Kopieren Sie eines davon, statt Dateien von Null zusammenzubauen.",
                "Einen Mod anlegen",
                "Während der Arbeit",
                "Distribution",
                "Der originale Modding-Hub verlinkt mehrere Seiten, die auf dem Wiki **nicht existieren** (Redlinks). Diese Themen werden hier nicht erfunden. Nutzen Sie [Creating a mod](/modding/creating-a-mod/) plus Ihren eigenen Packprozess und Attribution ([Licensing](/about/licensing/)).",
            ),
            (
                "fr",
                "Un mod SOMA est un dossier que le lanceur peut voir. Le jeu livre deux exemples connus : `MinimalCustomMapMod` et `MinimalAddOnMod`. Copiez-en un au lieu d’assembler les fichiers from scratch.",
                "Créer un mod",
                "Pendant le travail",
                "Distribution",
                "Le hub Modding d’origine pointe vers plusieurs pages qui **n’existent pas** sur le Wiki (redlinks). Ces sujets ne sont pas inventés ici. Utilisez [Creating a mod](/modding/creating-a-mod/) et votre propre packaging, avec l’attribution ([Licensing](/about/licensing/)).",
            ),
            (
                "it",
                "Una mod SOMA è una cartella che il launcher può vedere. Il gioco fornisce due esempi noti: `MinimalCustomMapMod` e `MinimalAddOnMod`. Copiane uno invece di assemblare i file da zero.",
                "Creare una mod",
                "Mentre lavori",
                "Distribuzione",
                "L’hub Modding originale punta a diverse pagine che **non esistono** sul Wiki (redlink). Quegli argomenti non sono inventati qui. Usa [Creating a mod](/modding/creating-a-mod/) e il tuo packaging, con l’attribuzione ([Licensing](/about/licensing/)).",
            ),
            (
                "es",
                "Un mod de SOMA es una carpeta que el launcher puede ver. El juego trae dos ejemplos conocidos: `MinimalCustomMapMod` y `MinimalAddOnMod`. Copia uno de ellos en vez de armar archivos desde cero.",
                "Crear un mod",
                "Mientras trabajas",
                "Distribución",
                "El hub Modding original enlaza varias páginas que **no existen** en el Wiki (redlinks). Esos temas no se inventan aquí. Usa [Creating a mod](/modding/creating-a-mod/) y tu propio empaquetado, con atribución ([Licensing](/about/licensing/)).",
            ),
        ]
    },
)

# ----- level-editor -----
pack(
    "level-editor",
    {
        loc: f"""{lead}

<p class="section-kicker">02 // LEVEL EDITOR &nbsp; REF 02.10</p>

## Interface

- [View](/level-editor/level-editor-view/)
- [Toolbar](/level-editor/level-editor-toolbar/)
- [Preferences](/level-editor/level-editor-preferences/)
- [Color dialog](/level-editor/level-editor-color-dialog/)
- [Finding objects](/level-editor/finding-objects/)
- [Pose editor](/level-editor/pose-editor/)
- [Entity poser](/level-editor/entity-poser/)
- [Compounds](/level-editor/compounds/)

## {hprop}

- [Level settings](/level-editor/level-settings/) — skybox and global fog
- [Level information](/level-editor/level-information/)

{controls}

## {hthen}

[Building levels](/level-building/) {then}. {alled}

{close(loc, ["[Configure the Level Editor](/start/configure-the-level-editor/)", "[Edit your first map](/start/edit-your-first-map/)", "[Areas](/areas/)"], ["[HPL3/SOMA/Level Design](https://wiki.frictionalgames.com/page/HPL3/SOMA/Level_Design)"])}
"""
        for loc, lead, hprop, controls, hthen, then, alled in [
            (
                "ru",
                "Level Editor правит карты `.hpm`. Привяжите его к моду до размещения объектов. Checkpoint из Getting Started: в заголовке `(Working on mod)`.",
                "Свойства уровня",
                "Отдельной SOMA-страницы Controls на хабе нет (redlink). Пока используйте View + Toolbar.",
                "Дальше — сборка карты",
                "для primitives, statics, lights, terrain, эффектов и производительности. Все редакторы:",
                "[Editor reference](/editors/).",
            ),
            (
                "de",
                "Der Level Editor bearbeitet `.hpm`-Maps. Hängen Sie ihn an Ihren Mod, bevor Sie Objekte platzieren. Checkpoint: Titelleiste `(Working on mod)`.",
                "Level-Eigenschaften",
                "Controls als eigene SOMA-Seite ist ein Redlink. Nutzen Sie View + Toolbar, bis der Artikel existiert.",
                "Dann die Map bauen",
                "für Primitives, Statics, Lights, Terrain, Effekte und Performance. Alle Editoren:",
                "[Editor reference](/editors/).",
            ),
            (
                "fr",
                "Le Level Editor édite les maps `.hpm`. Attachez-le à votre mod avant de placer des objets. Checkpoint : barre de titre `(Working on mod)`.",
                "Propriétés du niveau",
                "Controls comme page SOMA dédiée est un redlink. Utilisez View + Toolbar tant que l’article n’existe pas.",
                "Ensuite construire la map",
                "pour primitives, statics, lights, terrain, effets et performance. Tous les éditeurs :",
                "[Editor reference](/editors/).",
            ),
            (
                "it",
                "Il Level Editor modifica le mappe `.hpm`. Collegalo alla mod prima di piazzare oggetti. Checkpoint: barra del titolo `(Working on mod)`.",
                "Proprietà del livello",
                "Controls come pagina SOMA dedicata è un redlink. Usa View + Toolbar finché l’articolo non esiste.",
                "Poi costruisci la mappa",
                "per primitives, statics, lights, terrain, effetti e performance. Tutti gli editor:",
                "[Editor reference](/editors/).",
            ),
            (
                "es",
                "El Level Editor edita mapas `.hpm`. Átalo a tu mod antes de colocar objetos. Checkpoint: barra de título `(Working on mod)`.",
                "Propiedades del nivel",
                "Controls como página SOMA dedicada es un redlink. Usa View + Toolbar hasta que exista el artículo.",
                "Luego construir el mapa",
                "para primitives, statics, lights, terrain, efectos y rendimiento. Todos los editores:",
                "[Editor reference](/editors/).",
            ),
        ]
    },
)

# ----- assets / about / api / glossary / recipes / others: compact intros -----

pack(
    "assets",
    {
        loc: f"""<p class="section-kicker">05 // ASSETS &nbsp; REF 05.00</p>

{lead}

<Pipeline />

## Modeling

{group([
    ("/assets/modeling-overview/", "Modeling overview", h1),
    ("/assets/exporting-models/", "Exporting models", h2),
    ("/assets/blender-hpl3-export-plugin/", "Blender export plugin", h3),
    ("/assets/animation/", "Animation", h4),
    ("/assets/animation-principles/", "Animation principles", h5),
    ("/entities/adding-animations-to-entities/", "Animations on entities", h6),
])}

{maya}

## {then_h}

- [Materials](/materials/)
- [Entities & Model Editor](/entities/)
- [Particles](/particles/)
- [Audio](/audio/)
- [Import a model (recipe)](/recipes/import-model/)
- [Create an interactive entity (recipe)](/recipes/interactive-entity/)

{close(loc, [], [
    "[HPL3/SOMA/Modeling](https://wiki.frictionalgames.com/page/HPL3/SOMA/Modeling)",
    "[HPL3/SOMA/Animation](https://wiki.frictionalgames.com/page/HPL3/SOMA/Animation)",
    "[HPL3/Entities/Entities Overview](https://wiki.frictionalgames.com/page/HPL3/Entities/Entities_Overview)",
])}
"""
        for loc, lead, h1, h2, h3, h4, h5, h6, maya, then_h in [
            ("ru", "Конвейер, который подтверждают страницы modeling / entity / material:", "Как HPL3 ждёт mesh.", "Шаг экспорта в форматы движка.", "Именованный сторонний экспортёр.", "Хаб анимации SOMA.", "Принципы, которые Wiki реально написала.", "Провода клипов в Model Editor.", "Отдельного дерева Maya для SOMA нет. Если шага нет на этих страницах, здесь его нет.", "Дальше"),
            ("de", "Pipeline, die die originalen Modeling-/Entity-/Material-Seiten tragen:", "Wie HPL3 Meshes erwartet.", "Exportschritt in die Engine-Formate.", "Benannter Drittanbieter-Exporter.", "SOMA-Animations-Hub.", "Prinzipien, die das Wiki wirklich geschrieben hat.", "Clips im Model Editor verdrahten.", "Maya-spezifische Seiten sind kein eigener SOMA-Baum. Fehlt ein Schritt auf diesen Seiten, steht er hier nicht.", "Dann"),
            ("fr", "Pipeline que les pages modeling / entity / material d’origine supportent :", "Comment HPL3 attend les meshes.", "Étape d’export vers les formats moteur.", "Exporteur tiers nommé.", "Hub animation SOMA.", "Principes que le Wiki a réellement écrits.", "Brancher les clips dans le Model Editor.", "Les pages Maya ne forment pas un arbre SOMA séparé. Si une étape n’est pas sur ces pages, elle n’est pas remplie ici.", "Ensuite"),
            ("it", "Pipeline che le pagine modeling / entity / material originali supportano:", "Come HPL3 si aspetta le mesh.", "Passo di export nei formati del motore.", "Exporter di terze parti nominato.", "Hub animazione SOMA.", "Principi che il Wiki ha davvero scritto.", "Collegare i clip nel Model Editor.", "Le pagine Maya non sono un albero SOMA separato. Se un passo non è su quelle pagine, qui non c’è.", "Poi"),
            ("es", "Pipeline que sostienen las páginas originales de modeling / entity / material:", "Cómo HPL3 espera las meshes.", "Paso de export a los formatos del motor.", "Exportador de terceros con nombre.", "Hub de animación SOMA.", "Principios que el Wiki sí escribió.", "Cablear clips en el Model Editor.", "Las páginas de Maya no son un árbol SOMA aparte. Si un paso no está en esas páginas, aquí no se rellena.", "Luego"),
        ]
    },
)

pack(
    "about",
    {
        loc: f"""{lead}

<p class="section-kicker">00 // ABOUT &nbsp; REF 00.02</p>

## {hcounts}

<DocStats />

## {hdid}

- {d1}
- {d2}
- {d3}
- {d4}

## {hdidnot}

- {n1}
- {n2}
- {n3}

## {hsrc}

{canonical}

{footer}

## {hlic}

{lic}

## {hcon}

{con}
"""
        for loc, lead, hcounts, hdid, d1, d2, d3, d4, hdidnot, n1, n2, n3, hsrc, canonical, footer, hlic, lic, hcon, con in [
            ("ru", "Это **неофициальная документация сообщества** по моддингу SOMA и редакторам HPL3, которые идут с игрой. Сайт не связан с Frictional Games и не одобрен ими.", "Счётчики (последняя синхронизация Wiki)", "Что сделано", "Импортировано дерево `HPL3/SOMA` и общие страницы `HPL3/`, которые этому дереву нужны", "Amnesia: Rebirth и The Bunker не включены", "Дерево перегруппировано в путь обучения, рецепты и searchable API", "Отсутствующие статьи Wiki остались отсутствующими, с явной пометкой undocumented/redlink", "Чего нет", "Выдуманных сигнатур AngelScript, шорткатов редактора или параметров материалов", "Встроенных картинок Wiki (лицензия File: не подтверждена)", "Заявления, что это официальное руководство", "Источник", "Канонический технический источник: [Frictional Wiki — HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA).", "Каждая импортированная страница держит футер «Source & attribution» с title, URL и revision.", "Лицензия", "См. [Licensing](/about/licensing/). Живая Wiki подчиняется EULA и дисклеймерам Frictional, не лицензии CC-BY-SA сайта.", "Участие", "См. [Contributing](/about/contributing/)."),
            ("de", "Das ist **inoffizielle Community-Dokumentation** für SOMA-Modding und die HPL3-Editoren, die mit dem Spiel kommen. Nicht von Frictional Games unterstützt.", "Zählungen (letzte Wiki-Synchronisation)", "Was wir getan haben", "`HPL3/SOMA`-Baum und die gemeinsamen `HPL3/`-Seiten importiert, die dieser Baum braucht", "Amnesia: Rebirth und The Bunker weggelassen", "Baum in Lernpfad, Rezepte und durchsuchbare API umgruppiert", "Fehlende Wiki-Artikel fehlen weiter, mit undocumented/redlink-Markierung", "Was wir nicht getan haben", "AngelScript-Signaturen, Editor-Shortcuts oder Materialparameter erfinden", "Wiki-Bilder einbetten (File:-Lizenz unklar)", "Behaupten, dies sei das offizielle Handbuch", "Quelle", "Kanonische technische Quelle: [Frictional Wiki — HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA).", "Jede importierte Seite behält einen „Source & attribution“-Footer mit Title, URL und Revision.", "Lizenz", "Siehe [Licensing](/about/licensing/). Das Live-Wiki unterliegt Frictionals EULA, nicht einer CC-BY-SA-Site-Lizenz.", "Mitwirken", "Siehe [Contributing](/about/contributing/)."),
            ("fr", "Ceci est une **documentation communautaire non officielle** pour le modding SOMA et les éditeurs HPL3 livrés avec le jeu. Non affilié à Frictional Games.", "Comptes (dernière synchro Wiki)", "Ce que nous avons fait", "Importé l’arbre `HPL3/SOMA` et les pages `HPL3/` partagées dont cet arbre a besoin", "Amnesia: Rebirth et The Bunker exclus", "Arbre regroupé en parcours d’apprentissage, recettes et API interrogeable", "Articles Wiki manquants restent manquants, avec une marque undocumented/redlink", "Ce que nous n’avons pas fait", "Inventer des signatures AngelScript, des raccourcis d’éditeur ou des paramètres matériau", "Intégrer les images Wiki (licence File: non confirmée)", "Prétendre que c’est le manuel officiel", "Source", "Source technique canonique : [Frictional Wiki — HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA).", "Chaque page importée garde un pied « Source & attribution » avec title, URL et revision.", "Licence", "Voir [Licensing](/about/licensing/). Le Wiki live est régi par l’EULA Frictional, pas une licence CC-BY-SA de site.", "Contribuer", "Voir [Contributing](/about/contributing/)."),
            ("it", "Questa è **documentazione community non ufficiale** per il modding di SOMA e gli editor HPL3 che arrivano col gioco. Non affiliata a Frictional Games.", "Conteggi (ultima sync Wiki)", "Cosa abbiamo fatto", "Importato l’albero `HPL3/SOMA` e le pagine `HPL3/` condivise di cui quell’albero ha bisogno", "Amnesia: Rebirth e The Bunker esclusi", "Albero raggruppato in percorso di apprendimento, ricette e API cercabile", "Articoli Wiki mancanti restano mancanti, con marca undocumented/redlink", "Cosa non abbiamo fatto", "Inventare firme AngelScript, scorciatoie dell’editor o parametri materiale", "Incorporare immagini Wiki (licenza File: non confermata)", "Sostenere che questo sia il manuale ufficiale", "Fonte", "Fonte tecnica canonica: [Frictional Wiki — HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA).", "Ogni pagina importata tiene un footer «Source & attribution» con title, URL e revision.", "Licenza", "Vedi [Licensing](/about/licensing/). Il Wiki live è governato dall’EULA Frictional, non da una licenza CC-BY-SA del sito.", "Contribuire", "Vedi [Contributing](/about/contributing/)."),
            ("es", "Esta es **documentación comunitaria no oficial** para el modding de SOMA y los editores HPL3 que vienen con el juego. No afiliada a Frictional Games.", "Cuentas (última sync del Wiki)", "Qué hicimos", "Importamos el árbol `HPL3/SOMA` y las páginas `HPL3/` compartidas que ese árbol necesita", "Amnesia: Rebirth y The Bunker fuera", "Reagrupamos el árbol en ruta de aprendizaje, recetas y API buscable", "Los artículos Wiki que faltan siguen faltando, con marca undocumented/redlink", "Qué no hicimos", "Inventar firmas AngelScript, atajos del editor o parámetros de material", "Incrustar imágenes del Wiki (licencia File: no confirmada)", "Afirmar que esto es el manual oficial", "Fuente", "Fuente técnica canónica: [Frictional Wiki — HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA).", "Cada página importada guarda un pie «Source & attribution» con title, URL y revision.", "Licencia", "Véase [Licensing](/about/licensing/). El Wiki en vivo se rige por el EULA de Frictional, no por una licencia CC-BY-SA del sitio.", "Contribuir", "Véase [Contributing](/about/contributing/)."),
        ]
    },
)

pack(
    "api",
    {
        loc: f"""<p class="section-kicker">04 // API &nbsp; REF 04.90</p>

{lead}

{filt}

<ApiBrowser />

## {how}

{each}

{types}

{helpers}

{close(loc, ["[Scripting guide](/scripting/)", "[Common patterns](/scripting/common-patterns/)", "[Helpers](/scripting/helpers/)"], ["[HPL3/SOMA/Scripting/Scripting Api](https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Scripting_Api)"])}
"""
        for loc, lead, filt, how, each, types, helpers in [
            ("ru", "Этот индекс собран из сгенерированных страниц `CodeDoc` Wiki в `HPL3/SOMA/Scripting`. У большинства функций **нет описания** в исходной Wiki. Сигнатура, имена параметров и типы возврата сохранены. Ничего не додумано.", "Фильтр — простой текст по имени, классу и сигнатуре. Работают и `cScript_`, и `GetGlobalArg`.", "Как читать страницу класса", "Каждая страница класса/категории держит: таблицу функций, сигнатуру (AngelScript), таблицу параметров и пометку «Undocumented», если на Wiki не было текста.", "Связанные типы (`tString`, `cVector3f`, …) — отдельные страницы классов, если они были на Wiki.", "Игровые группы helper (`Entity`, `Prop`, `Map`, `Light`, …) живут в [api/categories](/api/categories/entity/)."),
            ("de", "Dieser Index stammt aus den generierten Wiki-`CodeDoc`-Seiten unter `HPL3/SOMA/Scripting`. Die meisten Funktionsrümpfe haben **keine Beschreibung**. Signatur, Parameternamen und Rückgabetypen bleiben. Nichts wird geraten.", "Der Filter ist Klartext über Name, Klasse und Signatur. `cScript_` und `GetGlobalArg` funktionieren beide.", "Klassenseite lesen", "Jede Klassen-/Kategorieseite behält: Funktionstabelle, Signatur (AngelScript), Parametertabelle und „Undocumented“, wenn das Wiki keinen Text hatte.", "Verwandte Typen (`tString`, `cVector3f`, …) sind eigene Klassenseiten, wenn das Wiki sie hatte.", "Gameplay-Helper-Gruppen (`Entity`, `Prop`, `Map`, `Light`, …) liegen unter [api/categories](/api/categories/entity/)."),
            ("fr", "Cet index est construit à partir des pages `CodeDoc` générées du Wiki sous `HPL3/SOMA/Scripting`. La plupart des corps de fonction n’ont **aucune description**. Signature, noms de paramètres et types de retour sont conservés.", "Le filtre est du texte brut sur nom, classe et signature. `cScript_` et `GetGlobalArg` marchent tous les deux.", "Lire une page de classe", "Chaque page classe/catégorie garde : tableau de fonctions, signature (AngelScript), tableau de paramètres, et une note « Undocumented » si le Wiki n’avait pas de texte.", "Les types liés (`tString`, `cVector3f`, …) sont des pages de classe séparées quand le Wiki les avait.", "Les groupes helper gameplay (`Entity`, `Prop`, `Map`, `Light`, …) sont sous [api/categories](/api/categories/entity/)."),
            ("it", "Questo indice è costruito dalle pagine `CodeDoc` generate del Wiki sotto `HPL3/SOMA/Scripting`. La maggior parte dei corpi di funzione **non ha descrizione**. Firma, nomi parametro e tipi di ritorno restano.", "Il filtro è testo semplice su nome, classe e firma. Funzionano sia `cScript_` sia `GetGlobalArg`.", "Come leggere una pagina di classe", "Ogni pagina classe/categoria tiene: tabella funzioni, firma (AngelScript), tabella parametri e nota «Undocumented» se il Wiki non aveva testo.", "I tipi correlati (`tString`, `cVector3f`, …) sono pagine di classe separate quando il Wiki le aveva.", "I gruppi helper di gameplay (`Entity`, `Prop`, `Map`, `Light`, …) stanno sotto [api/categories](/api/categories/entity/)."),
            ("es", "Este índice se arma con las páginas `CodeDoc` generadas del Wiki bajo `HPL3/SOMA/Scripting`. La mayoría de cuerpos de función **no tienen descripción**. Se conservan firma, nombres de parámetro y tipos de retorno.", "El filtro es texto plano sobre nombre, clase y firma. Funcionan `cScript_` y `GetGlobalArg`.", "Cómo leer una página de clase", "Cada página de clase/categoría guarda: tabla de funciones, firma (AngelScript), tabla de parámetros y nota «Undocumented» si el Wiki no tenía texto.", "Los tipos relacionados (`tString`, `cVector3f`, …) son páginas de clase aparte cuando el Wiki las tenía.", "Los grupos helper de gameplay (`Entity`, `Prop`, `Map`, `Light`, …) viven en [api/categories](/api/categories/entity/)."),
        ]
    },
)

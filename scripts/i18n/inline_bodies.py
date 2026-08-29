"""Homepage, Video library, Translations coverage, and Quickstart bodies."""

from __future__ import annotations

INDEX = "<HomeDashboard />\n"

VIDEOS = {
    "ru": """<p class="section-kicker">01 // VIDEO GUIDES &nbsp; REF 01.80</p>

Это **проверенные публичные** туториалы, привязанные к страницам этой документации. Заголовки — текущие названия на YouTube. Воспроизведение остаётся на YouTube (`youtube-nocookie.com` при встроенном проигрывании).

Ролики HPL2 / Amnesia: The Dark Descent не числятся как туториалы SOMA. Legacy-пункты, которые объясняют переносимый механизм HPL3, говорят об этом в строке предупреждения.

<VideoLibrary />

## Источники

- Ссылки на туториалы Frictional Wiki и два публичных плейлиста HPL3
- Живая проверка YouTube oEmbed (`pnpm videos:check`)
""",
    "de": """<p class="section-kicker">01 // VIDEO GUIDES &nbsp; REF 01.80</p>

Das sind **geprüfte öffentliche** Tutorials, die zu den Docs auf dieser Site gehören. Titel sind die aktuellen YouTube-Titel. Wiedergabe bleibt auf YouTube (`youtube-nocookie.com` bei Inline-Play).

HPL2- / Amnesia: The Dark Descent-Videos stehen nicht als SOMA-Tutorials. Legacy-Einträge, die einen übertragbaren HPL3-Mechanismus erklären, sagen das in der Warnzeile.

<VideoLibrary />

## Quellen

- Tutorial-Links des Frictional Wiki und die zwei öffentlichen HPL3-Playlists
- Live-YouTube-oEmbed-Check (`pnpm videos:check`)
""",
    "fr": """<p class="section-kicker">01 // VIDEO GUIDES &nbsp; REF 01.80</p>

Ce sont des tutoriels **publics vérifiés** qui correspondent aux docs de ce site. Les titres sont les titres YouTube actuels. La lecture reste sur YouTube (`youtube-nocookie.com` en lecture intégrée).

Les vidéos HPL2 / Amnesia: The Dark Descent ne figurent pas comme tutoriels SOMA. Les entrées Legacy qui expliquent un mécanisme HPL3 transférable le disent dans la ligne d’avertissement.

<VideoLibrary />

## Sources

- Liens tutoriels du Frictional Wiki et les deux playlists HPL3 publiques
- Contrôle oEmbed YouTube en direct (`pnpm videos:check`)
""",
    "it": """<p class="section-kicker">01 // VIDEO GUIDES &nbsp; REF 01.80</p>

Queste sono tutorial **pubbliche verificate** collegate alle docs di questo sito. I titoli sono i titoli YouTube attuali. La riproduzione resta su YouTube (`youtube-nocookie.com` in riproduzione inline).

I video HPL2 / Amnesia: The Dark Descent non sono elencati come tutorial SOMA. Le voci Legacy che spiegano un meccanismo HPL3 trasferibile lo dicono nella riga di avviso.

<VideoLibrary />

## Fonti

- Link tutorial del Frictional Wiki e le due playlist HPL3 pubbliche
- Controllo oEmbed YouTube live (`pnpm videos:check`)
""",
    "es": """<p class="section-kicker">01 // VIDEO GUIDES &nbsp; REF 01.80</p>

Estos son tutoriales **públicos verificados** ligados a las docs de este sitio. Los títulos son los títulos actuales de YouTube. La reproducción sigue en YouTube (`youtube-nocookie.com` si se reproduce en la página).

Los vídeos de HPL2 / Amnesia: The Dark Descent no se listan como tutoriales de SOMA. Los ítems Legacy que explican un mecanismo HPL3 transferible lo dicen en la línea de aviso.

<VideoLibrary />

## Fuentes

- Enlaces de tutoriales del Frictional Wiki y las dos playlists públicas de HPL3
- Comprobación oEmbed de YouTube en vivo (`pnpm videos:check`)
""",
}

TRANS = {
    "ru": """<p class="section-kicker">00 // TRANSLATIONS &nbsp; REF 00.04</p>

Английский — каноническая документация SOMA / HPL3. Другие языки сначала переводят обучающие страницы TIER 1 и хабы TIER 2. Технические идентификаторы остаются по-английски в каждой локали: `Area`, `Entity`, `OnStart`, `.hps`, `cScript_GetGlobalArgBool`.

Если страница ещё не переведена, переключатель языка оставляет вас на этой теме (fallback Starlight) и показывает короткое уведомление. Он не сбрасывает на главную локали.

## Покрытие

Счётчики берутся из `data/translation-manifest.json`, не из зашитых процентов.

<TranslationsCoverage />

## Что переводится первым

**TIER 1** — главная, Быстрый старт, Первый мод, Термины, Настройка мода, Level Editor, Сборка уровней, Areas, Скрипты, Отладка, Конвейер ассетов, Глоссарий.

**TIER 2** — Рецепты, Helpers, Entities, Materials, Particles, Audio, Dialogue, индекс API, библиотека видео.

**TIER 3** — полные страницы классов API, legacy-справочник, индекс Original Wiki. Английский, пока нет перевода.

## Связанное

- [Статус документации](/about/)
- [Участие](/about/contributing/)
""",
    "de": """<p class="section-kicker">00 // TRANSLATIONS &nbsp; REF 00.04</p>

Englisch ist die kanonische SOMA / HPL3-Dokumentation. Andere Sprachen übersetzen zuerst TIER-1-Lernseiten und TIER-2-Hubs. Technische Bezeichner bleiben in jeder Locale Englisch: `Area`, `Entity`, `OnStart`, `.hps`, `cScript_GetGlobalArgBool`.

Ist eine Seite noch nicht übersetzt, hält der Sprachumschalter Sie auf dem Thema (Starlight-Fallback) und zeigt einen kurzen Hinweis. Er wirft Sie nicht auf die Locale-Startseite.

## Abdeckung

Zählungen kommen aus `data/translation-manifest.json`, nicht aus fest kodierten Prozenten.

<TranslationsCoverage />

## Was zuerst übersetzt wird

**TIER 1** — Startseite, Schnellstart, Erster Mod, Terminologie, Mod-Setup, Level Editor, Level bauen, Areas, Scripting, Debugging, Asset-Pipeline, Glossar.

**TIER 2** — Rezepte, Helpers, Entities, Materials, Particles, Audio, Dialogue, API-Index, Videobibliothek.

**TIER 3** — volle API-Klassenseiten, Legacy-Referenz, Original-Wiki-Index. Englisch, bis eine Übersetzung existiert.

## Siehe auch

- [Dokumentationsstatus](/about/)
- [Mitwirken](/about/contributing/)
""",
    "fr": """<p class="section-kicker">00 // TRANSLATIONS &nbsp; REF 00.04</p>

L’anglais est la documentation canonique SOMA / HPL3. Les autres langues traduisent d’abord les pages d’apprentissage TIER 1 et les hubs TIER 2. Les identifiants techniques restent en anglais dans chaque locale : `Area`, `Entity`, `OnStart`, `.hps`, `cScript_GetGlobalArgBool`.

Si une page n’est pas encore traduite, le sélecteur de langue vous garde sur ce sujet (fallback Starlight) et affiche un avis compact. Il ne vous jette pas sur la page d’accueil de la locale.

## Couverture

Les comptes viennent de `data/translation-manifest.json`, pas de pourcentages en dur.

<TranslationsCoverage />

## Ce qui est traduit en premier

**TIER 1** — accueil, Démarrage rapide, Premier mod, Terminologie, Réglage du mod, Level Editor, Construire des niveaux, Areas, Scripting, Dépannage, Pipeline d’assets, Glossaire.

**TIER 2** — Recettes, Helpers, Entities, Materials, Particles, Audio, Dialogue, index API, bibliothèque vidéo.

**TIER 3** — pages de classes API complètes, référence legacy, index Wiki d’origine. Anglais tant qu’il n’y a pas de traduction.

## Voir aussi

- [État de la documentation](/about/)
- [Contribuer](/about/contributing/)
""",
    "it": """<p class="section-kicker">00 // TRANSLATIONS &nbsp; REF 00.04</p>

L’inglese è la documentazione canonica SOMA / HPL3. Le altre lingue traducono prima le pagine di apprendimento TIER 1 e gli hub TIER 2. Gli identificatori tecnici restano in inglese in ogni locale: `Area`, `Entity`, `OnStart`, `.hps`, `cScript_GetGlobalArgBool`.

Se una pagina non è ancora tradotta, il selettore lingua ti tiene su quell’argomento (fallback Starlight) e mostra un avviso compatto. Non ti scaraventa sulla home della locale.

## Copertura

I conteggi arrivano da `data/translation-manifest.json`, non da percentuali hardcoded.

<TranslationsCoverage />

## Cosa si traduce per primo

**TIER 1** — home, Avvio rapido, Prima mod, Terminologia, Setup della mod, Level Editor, Costruire livelli, Areas, Scripting, Debug, Pipeline degli asset, Glossario.

**TIER 2** — Ricette, Helpers, Entities, Materials, Particles, Audio, Dialogue, indice API, libreria video.

**TIER 3** — pagine complete delle classi API, riferimento legacy, indice Wiki originale. Inglese finché non esiste una traduzione.

## Correlati

- [Stato della documentazione](/about/)
- [Contribuire](/about/contributing/)
""",
    "es": """<p class="section-kicker">00 // TRANSLATIONS &nbsp; REF 00.04</p>

El inglés es la documentación canónica de SOMA / HPL3. Los demás idiomas traducen primero las páginas de aprendizaje TIER 1 y los hubs TIER 2. Los identificadores técnicos siguen en inglés en cada locale: `Area`, `Entity`, `OnStart`, `.hps`, `cScript_GetGlobalArgBool`.

Si una página aún no está traducida, el selector de idioma te deja en ese tema (fallback de Starlight) y muestra un aviso compacto. No te tira a la portada del locale.

## Cobertura

Las cuentas salen de `data/translation-manifest.json`, no de porcentajes fijos.

<TranslationsCoverage />

## Qué se traduce primero

**TIER 1** — inicio, Inicio rápido, Primer mod, Terminología, Configuración del mod, Level Editor, Construir niveles, Areas, Scripting, Diagnóstico, Pipeline de assets, Glosario.

**TIER 2** — Recetas, Helpers, Entities, Materials, Particles, Audio, Dialogue, índice API, biblioteca de vídeos.

**TIER 3** — páginas completas de clases API, referencia legacy, índice Wiki original. Inglés hasta que exista una traducción.

## Relacionado

- [Estado de la documentación](/about/)
- [Contribuir](/about/contributing/)
""",
}

START = {
    "ru": """Этот сайт неофициальный. Он перегруппировывает дерево [Frictional Wiki HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA), чтобы новый моддер шёл по одному пути, а опытный мог сразу открыть справочник.

<p class="section-kicker">01 // START &nbsp; REF 01.00</p>

## Что вы сделаете

К концу этого пути у вас будет:

- своя папка мода, скопированная из `MinimalCustomMapMod`, не из пустого каталога
- stand-alone мод, который стартует в своей sample-карте
- Level Editor, привязанный к этому моду
- сохранённое изменение карты HPL3 `.hpm`
- скрипт карты `.hps`, который печатает `Hello World!`

## Путь

<div class="catalog-group">
<div class="catalog-row"><a href="/start/prepare-your-tools/">1. Подготовить инструменты</a><span>SOMA, Level Editor и текстовый редактор запускаются.</span></div>
<div class="catalog-row"><a href="/start/create-and-launch-your-mod/">2. Создать и запустить</a><span>Скопированный мод появляется в лаунчере; стартует sample-карта.</span></div>
<div class="catalog-row"><a href="/start/configure-the-level-editor/">3. Настроить редактор</a><span>В заголовке окна написано <code>(Working on mod)</code>.</span></div>
<div class="catalog-row"><a href="/start/edit-your-first-map/">4. Править первую карту</a><span>Видимое изменение переживает save, close и reopen.</span></div>
<div class="catalog-row"><a href="/start/add-your-first-script/">5. Добавить первый скрипт</a><span><code>Hello World!</code> появляется при старте карты.</span></div>
<div class="catalog-row"><a href="/start/test-debug-and-continue/">6. Проверить и продолжить</a><span>Reload, найти ошибки скрипта, выбрать следующий раздел.</span></div>
</div>

:::note[Порядок]
Каждый шаг заканчивается checkpoint. Не перескакивайте к скриптам, если редактор всё ещё смотрит на ассеты базовой игры.
:::

## Перед началом

- Работайте в **своей** папке мода. Не правьте файлы базовой игры и оригинал `MinimalCustomMapMod`.
- Карта HPL3 — это файл `.hpm` **плюс** sidecar `.hpm_*`. Это не `.map` из HPL2.
- Имена: буквы, цифры, подчёркивания.

Если вы уже выпускаете моды SOMA, переходите к [Куда дальше](/start/where-next/) или откройте [справочник API](/api/).

## Контекст

- [Что такое HPL3?](/start/what-is-hpl3/)
- [Что можно менять](/start/what-can-be-modified/)
- [Термины](/start/terminology/)
- [Обзор Getting Started](/start/overview/)

## Источники

- [HPL3/SOMA/Getting Started](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started) (rev. 7120)
""",
    "de": """Diese Site ist inoffiziell. Sie ordnet den Baum [Frictional Wiki HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA) so, dass ein neuer Modder einem Pfad folgen kann und ein erfahrener direkt in die Referenz springt.

<p class="section-kicker">01 // START &nbsp; REF 01.00</p>

## Was Sie bauen

Am Ende dieses Pfads haben Sie:

- Ihren eigenen Mod-Ordner, kopiert von `MinimalCustomMapMod`, nicht aus einem leeren Verzeichnis
- einen Stand-alone-Mod, der in seiner Sample-Map startet
- den Level Editor, der an diesen Mod gebunden ist
- eine gespeicherte Änderung an einer HPL3-`.hpm`-Map
- ein `.hps`-Map-Skript, das `Hello World!` ausgibt

## Der Pfad

<div class="catalog-group">
<div class="catalog-row"><a href="/start/prepare-your-tools/">1. Werkzeuge vorbereiten</a><span>SOMA, Level Editor und ein Texteditor laufen.</span></div>
<div class="catalog-row"><a href="/start/create-and-launch-your-mod/">2. Anlegen und starten</a><span>Der kopierte Mod erscheint im Launcher; die Sample-Map startet.</span></div>
<div class="catalog-row"><a href="/start/configure-the-level-editor/">3. Editor einrichten</a><span>Die Titelleiste sagt <code>(Working on mod)</code>.</span></div>
<div class="catalog-row"><a href="/start/edit-your-first-map/">4. Erste Map bearbeiten</a><span>Eine sichtbare Änderung überlebt Save, Close und Reopen.</span></div>
<div class="catalog-row"><a href="/start/add-your-first-script/">5. Erstes Skript</a><span><code>Hello World!</code> erscheint, wenn die Map startet.</span></div>
<div class="catalog-row"><a href="/start/test-debug-and-continue/">6. Testen und weiter</a><span>Reload, Skriptfehler finden, nächsten Abschnitt wählen.</span></div>
</div>

:::note[Reihenfolge]
Jeder Schritt endet mit einem Checkpoint. Nicht zum Scripting springen, wenn der Editor noch Basis-Spiel-Assets sieht.
:::

## Bevor Sie anfangen

- Arbeiten Sie in **Ihrem** Mod-Ordner. Basis-Spieldateien und das Original `MinimalCustomMapMod` nicht ändern.
- Eine HPL3-Map ist die `.hpm`-Datei **plus** ihre `.hpm_*`-Sidecars. Kein HPL2-`.map`.
- Namen: Buchstaben, Zahlen, Unterstriche.

Wenn Sie bereits SOMA-Mods ausliefern, weiter zu [Wohin als Nächstes](/start/where-next/) oder [API-Referenz](/api/).

## Kontext

- [Was ist HPL3?](/start/what-is-hpl3/)
- [Was sich ändern lässt](/start/what-can-be-modified/)
- [Terminologie](/start/terminology/)
- [Getting-Started-Überblick](/start/overview/)

## Quellen

- [HPL3/SOMA/Getting Started](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started) (rev. 7120)
""",
    "fr": """Ce site n’est pas officiel. Il réorganise l’arbre [Frictional Wiki HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA) pour qu’un nouveau moddeur suive un parcours, et qu’un expérimenté saute à la référence.

<p class="section-kicker">01 // START &nbsp; REF 01.00</p>

## Ce que vous ferez

À la fin de ce parcours vous aurez :

- votre propre dossier de mod, copié depuis `MinimalCustomMapMod`, pas depuis un répertoire vide
- un mod stand-alone qui démarre dans sa map d’exemple
- le Level Editor attaché à ce mod
- un changement enregistré sur une map HPL3 `.hpm`
- un script de map `.hps` qui affiche `Hello World!`

## Le parcours

<div class="catalog-group">
<div class="catalog-row"><a href="/start/prepare-your-tools/">1. Préparer les outils</a><span>SOMA, le Level Editor et un éditeur de texte se lancent.</span></div>
<div class="catalog-row"><a href="/start/create-and-launch-your-mod/">2. Créer et lancer</a><span>Le mod copié apparaît dans le lanceur ; la map d’exemple démarre.</span></div>
<div class="catalog-row"><a href="/start/configure-the-level-editor/">3. Configurer l’éditeur</a><span>La barre de titre indique <code>(Working on mod)</code>.</span></div>
<div class="catalog-row"><a href="/start/edit-your-first-map/">4. Modifier votre première map</a><span>Un changement visible survit à save, close et reopen.</span></div>
<div class="catalog-row"><a href="/start/add-your-first-script/">5. Ajouter votre premier script</a><span><code>Hello World!</code> apparaît au démarrage de la map.</span></div>
<div class="catalog-row"><a href="/start/test-debug-and-continue/">6. Tester et continuer</a><span>Reload, trouver les erreurs de script, choisir la suite.</span></div>
</div>

:::note[Ordre]
Chaque étape se termine par un checkpoint. Ne sautez pas au scripting si l’éditeur regarde encore les assets du jeu de base.
:::

## Avant de commencer

- Travaillez dans **votre** dossier de mod. Ne modifiez pas les fichiers du jeu de base ni l’original `MinimalCustomMapMod`.
- Une map HPL3 est le fichier `.hpm` **plus** ses sidecars `.hpm_*`. Ce n’est pas un `.map` HPL2.
- Noms : lettres, chiffres, underscores.

Si vous livrez déjà des mods SOMA, passez à [La suite](/start/where-next/) ou ouvrez la [référence API](/api/).

## Contexte

- [Qu’est-ce que HPL3 ?](/start/what-is-hpl3/)
- [Ce qui peut être modifié](/start/what-can-be-modified/)
- [Terminologie](/start/terminology/)
- [Aperçu Getting Started](/start/overview/)

## Sources

- [HPL3/SOMA/Getting Started](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started) (rev. 7120)
""",
    "it": """Questo sito non è ufficiale. Riorganizza l’albero [Frictional Wiki HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA) così un nuovo modder segue un percorso e uno esperto salta al riferimento.

<p class="section-kicker">01 // START &nbsp; REF 01.00</p>

## Cosa farai

Alla fine di questo percorso avrai:

- la tua cartella della mod, copiata da `MinimalCustomMapMod`, non da una directory vuota
- una mod stand-alone che parte nella sua mappa di esempio
- il Level Editor agganciato a quella mod
- una modifica salvata a una mappa HPL3 `.hpm`
- uno script di mappa `.hps` che stampa `Hello World!`

## Il percorso

<div class="catalog-group">
<div class="catalog-row"><a href="/start/prepare-your-tools/">1. Preparare gli strumenti</a><span>SOMA, Level Editor e un editor di testo si avviano.</span></div>
<div class="catalog-row"><a href="/start/create-and-launch-your-mod/">2. Creare e avviare</a><span>La mod copiata compare nel launcher; parte la mappa di esempio.</span></div>
<div class="catalog-row"><a href="/start/configure-the-level-editor/">3. Configurare l’editor</a><span>La barra del titolo dice <code>(Working on mod)</code>.</span></div>
<div class="catalog-row"><a href="/start/edit-your-first-map/">4. Modificare la prima mappa</a><span>Un cambiamento visibile sopravvive a save, close e reopen.</span></div>
<div class="catalog-row"><a href="/start/add-your-first-script/">5. Aggiungere il primo script</a><span><code>Hello World!</code> compare all’avvio della mappa.</span></div>
<div class="catalog-row"><a href="/start/test-debug-and-continue/">6. Testare e continuare</a><span>Reload, trovare errori di script, scegliere la sezione successiva.</span></div>
</div>

:::note[Ordine]
Ogni passo finisce con un checkpoint. Non saltare allo scripting se l’editor guarda ancora gli asset del gioco base.
:::

## Prima di iniziare

- Lavora nella **tua** cartella della mod. Non modificare i file del gioco base né l’originale `MinimalCustomMapMod`.
- Una mappa HPL3 è il file `.hpm` **più** i sidecar `.hpm_*`. Non è un `.map` HPL2.
- Nomi: lettere, numeri, underscore.

Se pubblichi già mod di SOMA, vai a [Dove andare dopo](/start/where-next/) o apri il [riferimento API](/api/).

## Contesto

- [Cos’è HPL3?](/start/what-is-hpl3/)
- [Cosa si può modificare](/start/what-can-be-modified/)
- [Terminologia](/start/terminology/)
- [Panoramica Getting Started](/start/overview/)

## Fonti

- [HPL3/SOMA/Getting Started](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started) (rev. 7120)
""",
    "es": """Este sitio no es oficial. Reorganiza el árbol [Frictional Wiki HPL3/SOMA](https://wiki.frictionalgames.com/page/HPL3/SOMA) para que un modder nuevo siga un camino y uno experimentado salte a la referencia.

<p class="section-kicker">01 // START &nbsp; REF 01.00</p>

## Qué vas a hacer

Al final de este camino tendrás:

- tu propia carpeta de mod, copiada de `MinimalCustomMapMod`, no de un directorio vacío
- un mod stand-alone que arranca en su mapa de ejemplo
- el Level Editor ligado a ese mod
- un cambio guardado en un mapa HPL3 `.hpm`
- un script de mapa `.hps` que imprime `Hello World!`

## El camino

<div class="catalog-group">
<div class="catalog-row"><a href="/start/prepare-your-tools/">1. Preparar herramientas</a><span>SOMA, el Level Editor y un editor de texto arrancan.</span></div>
<div class="catalog-row"><a href="/start/create-and-launch-your-mod/">2. Crear y lanzar</a><span>El mod copiado aparece en el launcher; arranca el mapa de ejemplo.</span></div>
<div class="catalog-row"><a href="/start/configure-the-level-editor/">3. Configurar el editor</a><span>La barra de título dice <code>(Working on mod)</code>.</span></div>
<div class="catalog-row"><a href="/start/edit-your-first-map/">4. Editar tu primer mapa</a><span>Un cambio visible sobrevive a save, close y reopen.</span></div>
<div class="catalog-row"><a href="/start/add-your-first-script/">5. Añadir tu primer script</a><span><code>Hello World!</code> aparece al arrancar el mapa.</span></div>
<div class="catalog-row"><a href="/start/test-debug-and-continue/">6. Probar y continuar</a><span>Reload, encontrar errores de script, elegir la siguiente sección.</span></div>
</div>

:::note[Orden]
Cada paso termina con un checkpoint. No saltes a scripting si el editor sigue mirando assets del juego base.
:::

## Antes de empezar

- Trabaja en **tu** carpeta de mod. No edites archivos del juego base ni el `MinimalCustomMapMod` original.
- Un mapa HPL3 es el archivo `.hpm` **más** sus sidecars `.hpm_*`. No es un `.map` de HPL2.
- Nombres: letras, números, guiones bajos.

Si ya publicas mods de SOMA, pasa a [Qué sigue](/start/where-next/) o abre la [referencia API](/api/).

## Contexto

- [¿Qué es HPL3?](/start/what-is-hpl3/)
- [Qué se puede modificar](/start/what-can-be-modified/)
- [Terminología](/start/terminology/)
- [Resumen Getting Started](/start/overview/)

## Fuentes

- [HPL3/SOMA/Getting Started](https://wiki.frictionalgames.com/page/HPL3/SOMA/Getting_Started) (rev. 7120)
""",
}


def for_locale(locale: str) -> dict[str, str]:
    return {
        "index": INDEX,
        "videos": VIDEOS[locale],
        "about/translations": TRANS[locale],
        "start": START[locale],
    }

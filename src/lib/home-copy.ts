import type { AppLocale } from "./locale";

type HomeCopy = {
  kicker: string;
  facility: string;
  titleHtml: string;
  lede: string;
  search: string;
  jumpStart: string;
  jumpApi: string;
  jumpAreas: string;
  jumpDebug: string;
  startHere: string;
  iWantTo: string;
  reference: string;
  status: string;
  steps: { href: string; title: string; small: string }[];
  wants: { href: string; title: string; small: string }[];
  refs: { href: string; title: string; smallKey?: "api" | "areas" | "entities" | "materials" | "editors" | "glossary" }[];
};

const COPY: Record<AppLocale, HomeCopy> = {
  en: {
    kicker: "SOMA / HPL3 MODDING ARCHIVE",
    facility: "PATHOS-II // COMMUNITY TECHNICAL DOCUMENTATION",
    titleHtml: "SOMA / HPL3<br />Modding documentation",
    lede: "Learn the tools. Build levels. Script HPL3. Restructured from the Frictional Wiki — not an official Frictional Games site.",
    search: "Search documentation",
    jumpStart: "Start here",
    jumpApi: "API reference",
    jumpAreas: "Areas",
    jumpDebug: "Troubleshooting",
    startHere: "01 // Start here",
    iWantTo: "02 // I want to",
    reference: "03 // Reference",
    status: "04 // Documentation status",
    steps: [
      { href: "start/prepare-your-tools/", title: "Prepare tools", small: "SOMA, Level Editor, a text editor. Do not start from an empty folder." },
      { href: "start/create-and-launch-your-mod/", title: "Create a mod", small: "Copy MinimalCustomMapMod, give it an entry file, launch it." },
      { href: "start/configure-the-level-editor/", title: "Open the editor", small: "Title bar must say (Working on mod) before you touch a map." },
      { href: "start/edit-your-first-map/", title: "Build a map", small: "Change something visible, save, reopen. Keep the .hpm sidecar files together." },
      { href: "start/add-your-first-script/", title: "Write a script", small: "OnStart + cLux_AddDebugMessage(\"Hello World!\") on the map .hps file." },
      { href: "start/test-debug-and-continue/", title: "Debug", small: "F5 reload, F1 debug menu, error list. Then pick the next system." },
      { href: "start/where-next/", title: "Continue", small: "Areas, lighting, entities, helpers, materials — in that order if you are new." },
    ],
    wants: [
      { href: "start/create-and-launch-your-mod/", title: "Create a mod", small: "Copy the bundled example." },
      { href: "level-building/", title: "Build a level", small: "Primitives, statics, lights, fog." },
      { href: "scripting/", title: "Write scripts", small: "AngelScript, .hps, callbacks, timers." },
      { href: "assets/", title: "Import a model", small: "Export → material → entity → map." },
      { href: "materials/", title: "Create a material", small: "Material Editor, documented types." },
      { href: "audio/", title: "Add sound", small: "Sound entities, FMOD, soundscape." },
      { href: "particles/", title: "Make particles", small: "Emitters, start, movement, render." },
      { href: "debugging/", title: "Debug a mod", small: "Launch, resources, script errors." },
    ],
    refs: [
      { href: "api/", title: "API", smallKey: "api" },
      { href: "areas/", title: "Areas", smallKey: "areas" },
      { href: "entities/", title: "Entities", smallKey: "entities" },
      { href: "materials/", title: "Materials", smallKey: "materials" },
      { href: "editors/", title: "Editors", smallKey: "editors" },
      { href: "glossary/", title: "Glossary", smallKey: "glossary" },
    ],
  },
  ru: {
    kicker: "SOMA / HPL3 АРХИВ МОДДИНГА",
    facility: "PATHOS-II // СООБЩЕСТВО, ТЕХНИЧЕСКАЯ ДОКУМЕНТАЦИЯ",
    titleHtml: "SOMA / HPL3<br />Документация по моддингу",
    lede: "Инструменты. Уровни. Скрипты HPL3. Перегруппировано с Frictional Wiki — это не официальный сайт Frictional Games.",
    search: "Искать в документации",
    jumpStart: "Начать",
    jumpApi: "Справочник API",
    jumpAreas: "Areas",
    jumpDebug: "Отладка",
    startHere: "01 // Начать здесь",
    iWantTo: "02 // Мне нужно",
    reference: "03 // Справочник",
    status: "04 // Статус документации",
    steps: [
      { href: "start/prepare-your-tools/", title: "Подготовить инструменты", small: "SOMA, Level Editor, текстовый редактор. Не начинайте с пустой папки." },
      { href: "start/create-and-launch-your-mod/", title: "Создать мод", small: "Скопируйте MinimalCustomMapMod, заполните entry-файл, запустите." },
      { href: "start/configure-the-level-editor/", title: "Открыть редактор", small: "В заголовке должно быть (Working on mod), прежде чем трогать карту." },
      { href: "start/edit-your-first-map/", title: "Собрать карту", small: "Видимое изменение, сохранение, повторное открытие. Файлы .hpm_* держите рядом." },
      { href: "start/add-your-first-script/", title: "Написать скрипт", small: "OnStart + cLux_AddDebugMessage(\"Hello World!\") в .hps карты." },
      { href: "start/test-debug-and-continue/", title: "Отладить", small: "F5 — перезагрузка, F1 — debug menu, список ошибок. Затем следующий раздел." },
      { href: "start/where-next/", title: "Дальше", small: "Areas, освещение, Entity, Helper, материалы — в этом порядке для новичков." },
    ],
    wants: [
      { href: "start/create-and-launch-your-mod/", title: "Создать мод", small: "Скопировать готовый пример." },
      { href: "level-building/", title: "Собрать уровень", small: "Primitives, statics, lights, fog." },
      { href: "scripting/", title: "Писать скрипты", small: "AngelScript, .hps, callback, timers." },
      { href: "assets/", title: "Импортировать модель", small: "Export → material → entity → map." },
      { href: "materials/", title: "Сделать материал", small: "Material Editor, задокументированные типы." },
      { href: "audio/", title: "Добавить звук", small: "Sound entities, FMOD, soundscape." },
      { href: "particles/", title: "Частицы", small: "Emitter, start, movement, render." },
      { href: "debugging/", title: "Отладить мод", small: "Запуск, resources, ошибки скрипта." },
    ],
    refs: [
      { href: "api/", title: "API", smallKey: "api" },
      { href: "areas/", title: "Areas", smallKey: "areas" },
      { href: "entities/", title: "Entities", smallKey: "entities" },
      { href: "materials/", title: "Materials", smallKey: "materials" },
      { href: "editors/", title: "Editors", smallKey: "editors" },
      { href: "glossary/", title: "Глоссарий", smallKey: "glossary" },
    ],
  },
  de: {
    kicker: "SOMA / HPL3 MODDING-ARCHIV",
    facility: "PATHOS-II // COMMUNITY-TECHNIKDOKUMENTATION",
    titleHtml: "SOMA / HPL3<br />Modding-Dokumentation",
    lede: "Werkzeuge lernen. Level bauen. HPL3 skripten. Umstrukturiert aus dem Frictional Wiki — keine offizielle Frictional-Games-Site.",
    search: "Dokumentation durchsuchen",
    jumpStart: "Hier starten",
    jumpApi: "API-Referenz",
    jumpAreas: "Areas",
    jumpDebug: "Fehlerbehebung",
    startHere: "01 // Hier starten",
    iWantTo: "02 // Ich will",
    reference: "03 // Referenz",
    status: "04 // Dokumentationsstatus",
    steps: [
      { href: "start/prepare-your-tools/", title: "Werkzeuge vorbereiten", small: "SOMA, Level Editor, Texteditor. Nicht mit einem leeren Ordner beginnen." },
      { href: "start/create-and-launch-your-mod/", title: "Mod anlegen", small: "MinimalCustomMapMod kopieren, Entry-Datei setzen, starten." },
      { href: "start/configure-the-level-editor/", title: "Editor öffnen", small: "Titelleiste muss (Working on mod) zeigen, bevor eine Map angefasst wird." },
      { href: "start/edit-your-first-map/", title: "Map bauen", small: "Sichtbare Änderung, speichern, neu öffnen. .hpm-Begleitdateien zusammenhalten." },
      { href: "start/add-your-first-script/", title: "Skript schreiben", small: "OnStart + cLux_AddDebugMessage(\"Hello World!\") in der Map-.hps." },
      { href: "start/test-debug-and-continue/", title: "Debuggen", small: "F5 Reload, F1 Debug-Menü, Error List. Dann das nächste System." },
      { href: "start/where-next/", title: "Weiter", small: "Areas, Lighting, Entities, Helpers, Materials — in dieser Reihenfolge als Einstieg." },
    ],
    wants: [
      { href: "start/create-and-launch-your-mod/", title: "Mod anlegen", small: "Das mitgelieferte Beispiel kopieren." },
      { href: "level-building/", title: "Level bauen", small: "Primitives, Statics, Lights, Fog." },
      { href: "scripting/", title: "Skripte schreiben", small: "AngelScript, .hps, Callbacks, Timer." },
      { href: "assets/", title: "Modell importieren", small: "Export → Material → Entity → Map." },
      { href: "materials/", title: "Material anlegen", small: "Material Editor, dokumentierte Typen." },
      { href: "audio/", title: "Sound hinzufügen", small: "Sound-Entities, FMOD, Soundscape." },
      { href: "particles/", title: "Partikel", small: "Emitter, Start, Movement, Render." },
      { href: "debugging/", title: "Mod debuggen", small: "Start, Resources, Skriptfehler." },
    ],
    refs: [
      { href: "api/", title: "API", smallKey: "api" },
      { href: "areas/", title: "Areas", smallKey: "areas" },
      { href: "entities/", title: "Entities", smallKey: "entities" },
      { href: "materials/", title: "Materials", smallKey: "materials" },
      { href: "editors/", title: "Editors", smallKey: "editors" },
      { href: "glossary/", title: "Glossar", smallKey: "glossary" },
    ],
  },
  fr: {
    kicker: "SOMA / HPL3 ARCHIVE DE MODDING",
    facility: "PATHOS-II // DOCUMENTATION TECHNIQUE COMMUNAUTAIRE",
    titleHtml: "SOMA / HPL3<br />Documentation de modding",
    lede: "Apprendre les outils. Construire des niveaux. Scripter HPL3. Réorganisé depuis le Frictional Wiki — ce n’est pas un site officiel Frictional Games.",
    search: "Rechercher dans la documentation",
    jumpStart: "Commencer",
    jumpApi: "Référence API",
    jumpAreas: "Areas",
    jumpDebug: "Dépannage",
    startHere: "01 // Commencer ici",
    iWantTo: "02 // Je veux",
    reference: "03 // Référence",
    status: "04 // État de la documentation",
    steps: [
      { href: "start/prepare-your-tools/", title: "Préparer les outils", small: "SOMA, Level Editor, éditeur de texte. Ne partez pas d’un dossier vide." },
      { href: "start/create-and-launch-your-mod/", title: "Créer un mod", small: "Copier MinimalCustomMapMod, renseigner l’entrée, lancer." },
      { href: "start/configure-the-level-editor/", title: "Ouvrir l’éditeur", small: "La barre de titre doit afficher (Working on mod) avant de toucher une map." },
      { href: "start/edit-your-first-map/", title: "Construire une map", small: "Changement visible, enregistrement, réouverture. Garder les fichiers .hpm_* ensemble." },
      { href: "start/add-your-first-script/", title: "Écrire un script", small: "OnStart + cLux_AddDebugMessage(\"Hello World!\") dans le .hps de la map." },
      { href: "start/test-debug-and-continue/", title: "Déboguer", small: "F5 rechargement, F1 debug menu, liste d’erreurs. Puis le système suivant." },
      { href: "start/where-next/", title: "Continuer", small: "Areas, éclairage, entities, helpers, materials — dans cet ordre si vous débutez." },
    ],
    wants: [
      { href: "start/create-and-launch-your-mod/", title: "Créer un mod", small: "Copier l’exemple fourni." },
      { href: "level-building/", title: "Construire un niveau", small: "Primitives, statics, lights, fog." },
      { href: "scripting/", title: "Écrire des scripts", small: "AngelScript, .hps, callbacks, timers." },
      { href: "assets/", title: "Importer un modèle", small: "Export → material → entity → map." },
      { href: "materials/", title: "Créer un matériau", small: "Material Editor, types documentés." },
      { href: "audio/", title: "Ajouter du son", small: "Sound entities, FMOD, soundscape." },
      { href: "particles/", title: "Particules", small: "Emitters, start, movement, render." },
      { href: "debugging/", title: "Déboguer un mod", small: "Lancement, resources, erreurs de script." },
    ],
    refs: [
      { href: "api/", title: "API", smallKey: "api" },
      { href: "areas/", title: "Areas", smallKey: "areas" },
      { href: "entities/", title: "Entities", smallKey: "entities" },
      { href: "materials/", title: "Materials", smallKey: "materials" },
      { href: "editors/", title: "Editors", smallKey: "editors" },
      { href: "glossary/", title: "Glossaire", smallKey: "glossary" },
    ],
  },
  it: {
    kicker: "SOMA / HPL3 ARCHIVIO MODDING",
    facility: "PATHOS-II // DOCUMENTAZIONE TECNICA DELLA COMMUNITY",
    titleHtml: "SOMA / HPL3<br />Documentazione di modding",
    lede: "Impara gli strumenti. Costruisci livelli. Scripta HPL3. Riorganizzato dal Frictional Wiki — non è un sito ufficiale Frictional Games.",
    search: "Cerca nella documentazione",
    jumpStart: "Inizia qui",
    jumpApi: "Riferimento API",
    jumpAreas: "Areas",
    jumpDebug: "Risoluzione problemi",
    startHere: "01 // Inizia qui",
    iWantTo: "02 // Voglio",
    reference: "03 // Riferimento",
    status: "04 // Stato della documentazione",
    steps: [
      { href: "start/prepare-your-tools/", title: "Preparare gli strumenti", small: "SOMA, Level Editor, editor di testo. Non partire da una cartella vuota." },
      { href: "start/create-and-launch-your-mod/", title: "Creare una mod", small: "Copiare MinimalCustomMapMod, compilare l’entry, avviare." },
      { href: "start/configure-the-level-editor/", title: "Aprire l’editor", small: "La barra del titolo deve dire (Working on mod) prima di toccare una mappa." },
      { href: "start/edit-your-first-map/", title: "Costruire una mappa", small: "Cambio visibile, salvataggio, riapertura. Tenere insieme i file .hpm_*." },
      { href: "start/add-your-first-script/", title: "Scrivere uno script", small: "OnStart + cLux_AddDebugMessage(\"Hello World!\") nel .hps della mappa." },
      { href: "start/test-debug-and-continue/", title: "Debug", small: "F5 reload, F1 debug menu, elenco errori. Poi il sistema successivo." },
      { href: "start/where-next/", title: "Continuare", small: "Areas, lighting, entities, helpers, materials — in quest’ordine se sei all’inizio." },
    ],
    wants: [
      { href: "start/create-and-launch-your-mod/", title: "Creare una mod", small: "Copiare l’esempio incluso." },
      { href: "level-building/", title: "Costruire un livello", small: "Primitives, statics, lights, fog." },
      { href: "scripting/", title: "Scrivere script", small: "AngelScript, .hps, callback, timer." },
      { href: "assets/", title: "Importare un modello", small: "Export → material → entity → map." },
      { href: "materials/", title: "Creare un materiale", small: "Material Editor, tipi documentati." },
      { href: "audio/", title: "Aggiungere suono", small: "Sound entities, FMOD, soundscape." },
      { href: "particles/", title: "Particelle", small: "Emitter, start, movement, render." },
      { href: "debugging/", title: "Debuggare una mod", small: "Avvio, resources, errori di script." },
    ],
    refs: [
      { href: "api/", title: "API", smallKey: "api" },
      { href: "areas/", title: "Areas", smallKey: "areas" },
      { href: "entities/", title: "Entities", smallKey: "entities" },
      { href: "materials/", title: "Materials", smallKey: "materials" },
      { href: "editors/", title: "Editors", smallKey: "editors" },
      { href: "glossary/", title: "Glossario", smallKey: "glossary" },
    ],
  },
  es: {
    kicker: "SOMA / HPL3 ARCHIVO DE MODDING",
    facility: "PATHOS-II // DOCUMENTACIÓN TÉCNICA DE LA COMUNIDAD",
    titleHtml: "SOMA / HPL3<br />Documentación de modding",
    lede: "Aprende las herramientas. Construye niveles. Scripta HPL3. Reorganizado desde el Frictional Wiki — no es un sitio oficial de Frictional Games.",
    search: "Buscar en la documentación",
    jumpStart: "Empezar aquí",
    jumpApi: "Referencia API",
    jumpAreas: "Areas",
    jumpDebug: "Diagnóstico",
    startHere: "01 // Empieza aquí",
    iWantTo: "02 // Quiero",
    reference: "03 // Referencia",
    status: "04 // Estado de la documentación",
    steps: [
      { href: "start/prepare-your-tools/", title: "Preparar herramientas", small: "SOMA, Level Editor, editor de texto. No empieces en una carpeta vacía." },
      { href: "start/create-and-launch-your-mod/", title: "Crear un mod", small: "Copia MinimalCustomMapMod, rellena el entry, lánzalo." },
      { href: "start/configure-the-level-editor/", title: "Abrir el editor", small: "La barra de título debe decir (Working on mod) antes de tocar un mapa." },
      { href: "start/edit-your-first-map/", title: "Construir un mapa", small: "Cambio visible, guardar, reabrir. Mantén juntos los .hpm_*." },
      { href: "start/add-your-first-script/", title: "Escribir un script", small: "OnStart + cLux_AddDebugMessage(\"Hello World!\") en el .hps del mapa." },
      { href: "start/test-debug-and-continue/", title: "Depurar", small: "F5 recarga, F1 debug menu, lista de errores. Luego el siguiente sistema." },
      { href: "start/where-next/", title: "Continuar", small: "Areas, iluminación, entities, helpers, materials — en ese orden si empiezas." },
    ],
    wants: [
      { href: "start/create-and-launch-your-mod/", title: "Crear un mod", small: "Copiar el ejemplo incluido." },
      { href: "level-building/", title: "Construir un nivel", small: "Primitives, statics, lights, fog." },
      { href: "scripting/", title: "Escribir scripts", small: "AngelScript, .hps, callbacks, timers." },
      { href: "assets/", title: "Importar un modelo", small: "Export → material → entity → map." },
      { href: "materials/", title: "Crear un material", small: "Material Editor, tipos documentados." },
      { href: "audio/", title: "Añadir sonido", small: "Sound entities, FMOD, soundscape." },
      { href: "particles/", title: "Partículas", small: "Emitters, start, movement, render." },
      { href: "debugging/", title: "Depurar un mod", small: "Lanzamiento, resources, errores de script." },
    ],
    refs: [
      { href: "api/", title: "API", smallKey: "api" },
      { href: "areas/", title: "Areas", smallKey: "areas" },
      { href: "entities/", title: "Entities", smallKey: "entities" },
      { href: "materials/", title: "Materials", smallKey: "materials" },
      { href: "editors/", title: "Editors", smallKey: "editors" },
      { href: "glossary/", title: "Glosario", smallKey: "glossary" },
    ],
  },
};

const REF_SMALL: Record<NonNullable<HomeCopy["refs"][number]["smallKey"]>, Record<AppLocale, string>> = {
  api: {
    en: "generated function signatures.",
    ru: "сгенерированных сигнатур функций.",
    de: "generierte Funktionssignaturen.",
    fr: "signatures de fonctions générées.",
    it: "firme di funzione generate.",
    es: "firmas de función generadas.",
  },
  areas: {
    en: "Triggers, PlayerStart, fog, SOMA volumes.",
    ru: "Trigger, PlayerStart, fog, тома SOMA.",
    de: "Trigger, PlayerStart, Fog, SOMA-Volumen.",
    fr: "Trigger, PlayerStart, fog, volumes SOMA.",
    it: "Trigger, PlayerStart, fog, volumi SOMA.",
    es: "Trigger, PlayerStart, fog, volúmenes SOMA.",
  },
  entities: {
    en: "Model Editor, types, physics, joints.",
    ru: "Model Editor, типы, физика, joints.",
    de: "Model Editor, Typen, Physik, Joints.",
    fr: "Model Editor, types, physique, joints.",
    it: "Model Editor, tipi, fisica, joints.",
    es: "Model Editor, tipos, física, joints.",
  },
  materials: {
    en: "What exists — and Wiki redlinks.",
    ru: "Что есть — и redlink Wiki.",
    de: "Was existiert — und Wiki-Redlinks.",
    fr: "Ce qui existe — et les redlinks Wiki.",
    it: "Cosa esiste — e i redlink Wiki.",
    es: "Qué existe — y redlinks del Wiki.",
  },
  editors: {
    en: "Level, Model, Material, Particle, Audition.",
    ru: "Level, Model, Material, Particle, Audition.",
    de: "Level, Model, Material, Particle, Audition.",
    fr: "Level, Model, Material, Particle, Audition.",
    it: "Level, Model, Material, Particle, Audition.",
    es: "Level, Model, Material, Particle, Audition.",
  },
  glossary: {
    en: "Area, Entity, Prop, HPS, HPM, helper.",
    ru: "Area, Entity, Prop, HPS, HPM, helper.",
    de: "Area, Entity, Prop, HPS, HPM, Helper.",
    fr: "Area, Entity, Prop, HPS, HPM, helper.",
    it: "Area, Entity, Prop, HPS, HPM, helper.",
    es: "Area, Entity, Prop, HPS, HPM, helper.",
  },
};

export function homeCopy(locale: AppLocale): HomeCopy {
  return COPY[locale] || COPY.en;
}

export function refSmall(key: NonNullable<HomeCopy["refs"][number]["smallKey"]>, locale: AppLocale, count?: number): string {
  const text = REF_SMALL[key][locale] || REF_SMALL[key].en;
  if (key === "api" && typeof count === "number") {
    return `${count} ${text}`;
  }
  return text;
}

import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

const base = process.env.BASE_PATH || "/";
const site = process.env.SITE_URL || "http://localhost:8080";
const githubRepoUrl = process.env.GITHUB_REPO_URL;
const editBaseUrl = process.env.EDIT_BASE_URL;

function assetUrl(file) {
  const s = String(site).replace(/\/$/, "");
  const b = !base || base === "/" ? "" : `/${String(base).replace(/^\/|\/$/g, "")}`;
  return `${s}${b}/${file.replace(/^\//, "")}`;
}

function iconHref(file) {
  const b = !base || base === "/" ? "/" : `/${String(base).replace(/^\/|\/$/g, "")}/`;
  return `${b}${file.replace(/^\//, "")}`.replace(/\/{2,}/g, "/");
}

function walkHast(node, visit) {
  if (!node || typeof node !== "object") return;
  visit(node);
  if (Array.isArray(node.children)) {
    for (const child of node.children) walkHast(child, visit);
  }
}

/** Prefix root-absolute href/src with Astro `base` so project GitHub Pages work. */
function rehypePrefixBase(basePath) {
  const prefix = !basePath || basePath === "/" ? "" : String(basePath).replace(/\/$/, "");
  return () => (tree) => {
    if (!prefix) return;
    walkHast(tree, (node) => {
      if (node.type !== "element" || !node.properties) return;
      for (const attr of ["href", "src"]) {
        const value = node.properties[attr];
        if (typeof value !== "string") continue;
        if (!value.startsWith("/") || value.startsWith("//")) continue;
        if (value === prefix || value.startsWith(`${prefix}/`)) continue;
        node.properties[attr] = `${prefix}${value}`;
      }
    });
  };
}

const tr = (ru, de, fr, it, es) => ({ ru, de, fr, it, es });

export default defineConfig({
  site,
  base,
  trailingSlash: "always",
  markdown: {
    rehypePlugins: [rehypePrefixBase(base)],
  },
  integrations: [
    starlight({
      title: "SOMA / HPL3 Docs",
      description:
        "Unofficial community documentation for SOMA modding and the HPL3 engine.",
      defaultLocale: "root",
      locales: {
        root: { label: "English", lang: "en" },
        ru: { label: "Русский", lang: "ru" },
        de: { label: "Deutsch", lang: "de" },
        fr: { label: "Français", lang: "fr" },
        it: { label: "Italiano", lang: "it" },
        es: { label: "Español", lang: "es" },
      },
      routeMiddleware: "./src/routeMiddleware.ts",
      logo: {
        src: "./src/assets/mark.svg",
        alt: "SOMA HPL3 Docs",
        replacesTitle: true,
      },
      social: githubRepoUrl
        ? [{ icon: "github", label: "GitHub", href: githubRepoUrl }]
        : [],
      editLink: editBaseUrl ? { baseUrl: editBaseUrl } : false,
      customCss: [
        "@fontsource/ibm-plex-sans/400.css",
        "@fontsource/ibm-plex-sans/500.css",
        "@fontsource/ibm-plex-sans/600.css",
        "@fontsource/ibm-plex-sans-condensed/500.css",
        "@fontsource/ibm-plex-sans-condensed/600.css",
        "@fontsource/ibm-plex-mono/400.css",
        "@fontsource/ibm-plex-mono/500.css",
        "./src/styles/tokens.css",
        "./src/styles/global.css",
        "./src/styles/docs.css",
        "./src/styles/print.css",
      ],
      components: {
        Head: "./src/components/Head.astro",
        SiteTitle: "./src/components/SiteTitle.astro",
        Header: "./src/components/Header.astro",
        Footer: "./src/components/Footer.astro",
        PageTitle: "./src/components/PageTitle.astro",
        TableOfContents: "./src/components/TableOfContents.astro",
        MobileMenuToggle: "./src/components/MobileMenuToggle.astro",
        ThemeSelect: "./src/components/Empty.astro",
        ThemeProvider: "./src/components/ThemeProvider.astro",
        Banner: "./src/components/SourceBanner.astro",
        LanguageSelect: "./src/components/LanguageSelect.astro",
        FallbackContentNotice: "./src/components/FallbackContentNotice.astro",
      },
      pagination: true,
      lastUpdated: false,
      credits: false,
      pagefind: true,
      expressiveCode: {
        themes: ["houston", "houston"],
        shiki: {
          langAlias: {
            angelscript: "cpp",
          },
        },
        styleOverrides: {
          borderRadius: "2px",
          borderWidth: "1px",
          frames: {
            shadowColor: "transparent",
          },
        },
      },
      head: [
        {
          tag: "meta",
          attrs: { name: "theme-color", content: "#071012" },
        },
        {
          tag: "link",
          attrs: { rel: "icon", type: "image/svg+xml", href: iconHref("favicon.svg") },
        },
        {
          tag: "link",
          attrs: { rel: "manifest", href: iconHref("manifest.webmanifest") },
        },
        {
          tag: "meta",
          attrs: { property: "og:image", content: assetUrl("og.jpg") },
        },
        {
          tag: "meta",
          attrs: { name: "twitter:card", content: "summary_large_image" },
        },
        {
          tag: "meta",
          attrs: { name: "twitter:image", content: assetUrl("og.jpg") },
        },
      ],
      sidebar: [
        {
          label: "Start",
          translations: tr("Старт", "Start", "Démarrage", "Inizio", "Inicio"),
          items: [
            { label: "Quickstart", slug: "start", translations: tr("Быстрый старт", "Schnellstart", "Démarrage rapide", "Avvio rapido", "Inicio rápido") },
            { label: "First mod", slug: "start/create-and-launch-your-mod", translations: tr("Первый мод", "Erster Mod", "Premier mod", "Prima mod", "Primer mod") },
            { label: "Terminology", slug: "start/terminology", translations: tr("Термины", "Terminologie", "Terminologie", "Terminologia", "Terminología") },
            { label: "Video guides", slug: "videos", translations: tr("Видеогайды", "Videoguides", "Guides vidéo", "Guide video", "Guías de vídeo") },
          ],
        },
        {
          label: "Create",
          translations: tr("Создание", "Erstellen", "Créer", "Creare", "Crear"),
          items: [
            { label: "Mod setup", slug: "modding", translations: tr("Настройка мода", "Mod-Setup", "Réglage du mod", "Setup della mod", "Configuración del mod") },
            { label: "Level Editor", slug: "level-editor" },
            { label: "Building levels", slug: "level-building", translations: tr("Сборка уровней", "Level bauen", "Construire des niveaux", "Costruire livelli", "Construir niveles") },
            { label: "Areas & triggers", slug: "areas", translations: tr("Areas и триггеры", "Areas & Trigger", "Areas et triggers", "Areas e trigger", "Areas y triggers") },
            { label: "Debugging", slug: "debugging", translations: tr("Отладка", "Debugging", "Débogage", "Debug", "Depuración") },
          ],
        },
        {
          label: "Script",
          translations: tr("Скрипты", "Skript", "Script", "Script", "Script"),
          items: [
            { label: "Scripting guide", slug: "scripting", translations: tr("Руководство по скриптам", "Scripting-Leitfaden", "Guide de scripting", "Guida allo scripting", "Guía de scripting") },
            { label: "Common patterns", slug: "scripting/common-patterns", translations: tr("Типовые приёмы", "Übliche Muster", "Motifs courants", "Schemi comuni", "Patrones comunes") },
            { label: "Helpers", slug: "scripting/helpers" },
            { label: "API reference", slug: "api", translations: tr("Справочник API", "API-Referenz", "Référence API", "Riferimento API", "Referencia API") },
          ],
        },
        {
          label: "Assets",
          translations: tr("Ассеты", "Assets", "Assets", "Asset", "Assets"),
          items: [
            { label: "Asset pipeline", slug: "assets", translations: tr("Конвейер ассетов", "Asset-Pipeline", "Pipeline d’assets", "Pipeline degli asset", "Pipeline de assets") },
            { label: "Entities", slug: "entities" },
            { label: "Materials", slug: "materials", translations: tr("Материалы", "Materials", "Matériaux", "Materiali", "Materiales") },
            { label: "Particles", slug: "particles", translations: tr("Частицы", "Partikel", "Particules", "Particelle", "Partículas") },
            { label: "Audio", slug: "audio" },
            { label: "Dialogue", slug: "dialogue", translations: tr("Диалог", "Dialog", "Dialogue", "Dialoghi", "Diálogo") },
          ],
        },
        {
          label: "Reference",
          translations: tr("Справочник", "Referenz", "Référence", "Riferimento", "Referencia"),
          items: [
            { label: "Editor reference", slug: "editors", translations: tr("Справочник редакторов", "Editor-Referenz", "Référence éditeurs", "Riferimento editor", "Referencia de editores") },
            { label: "Tools", slug: "tools", translations: tr("Инструменты", "Werkzeuge", "Outils", "Strumenti", "Herramientas") },
            { label: "Recipes", slug: "recipes", translations: tr("Рецепты", "Rezepte", "Recettes", "Ricette", "Recetas") },
            { label: "Glossary", slug: "glossary", translations: tr("Глоссарий", "Glossar", "Glossaire", "Glossario", "Glosario") },
            { label: "Original Wiki index", slug: "wiki-index", translations: tr("Индекс Wiki", "Original-Wiki-Index", "Index Wiki d’origine", "Indice Wiki originale", "Índice Wiki original") },
          ],
        },
        {
          label: "About",
          translations: tr("О сайте", "Über", "À propos", "Informazioni", "Acerca de"),
          items: [
            { label: "Documentation status", slug: "about", translations: tr("Статус документации", "Dokumentationsstatus", "État de la documentation", "Stato della documentazione", "Estado de la documentación") },
            { label: "Translations", slug: "about/translations", translations: tr("Переводы", "Übersetzungen", "Traductions", "Traduzioni", "Traducciones") },
            { label: "Contributing", slug: "about/contributing", translations: tr("Участие", "Mitwirken", "Contribuer", "Contribuire", "Contribuir") },
            { label: "Licensing", slug: "about/licensing", translations: tr("Лицензии", "Lizenz", "Licences", "Licenze", "Licencias") },
          ],
        },
      ],
    }),
  ],
  vite: {
    server: {
      host: "0.0.0.0",
      port: 8080,
      strictPort: true,
    },
    preview: {
      host: "127.0.0.1",
      port: 8081,
      strictPort: true,
    },
  },
});

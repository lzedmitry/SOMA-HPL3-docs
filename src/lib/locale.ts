import { withBase } from "./base";
import translationManifest from "../../data/translation-manifest.json";

export const LOCALE_META = [
  { id: "en", starlight: "root", label: "English", htmlLang: "en", short: "EN" },
  { id: "ru", starlight: "ru", label: "Русский", htmlLang: "ru", short: "RU" },
  { id: "de", starlight: "de", label: "Deutsch", htmlLang: "de", short: "DE" },
  { id: "fr", starlight: "fr", label: "Français", htmlLang: "fr", short: "FR" },
  { id: "it", starlight: "it", label: "Italiano", htmlLang: "it", short: "IT" },
  { id: "es", starlight: "es", label: "Español", htmlLang: "es", short: "ES" },
] as const;

export type AppLocale = (typeof LOCALE_META)[number]["id"];

export const CONTENT_LOCALES: AppLocale[] = ["ru", "de", "fr", "it", "es"];

type LocaleRow = { revision?: string | number; status?: string } | null;

type ManifestFile = {
  generatedAt?: string;
  englishPageCount?: number;
  pages: Record<string, Partial<Record<AppLocale, LocaleRow>>>;
};

const file = translationManifest as ManifestFile;
const pages = file.pages || {};

export function appLocale(starlightLocale: string | undefined): AppLocale {
  if (!starlightLocale || starlightLocale === "root" || starlightLocale === "en") return "en";
  const hit = LOCALE_META.find((l) => l.starlight === starlightLocale);
  return hit ? hit.id : "en";
}

/** Collection id → canonical English slug (`start`, `areas/trigger-area`). */
export function englishSlug(entryId: string): string {
  let trimmed = String(entryId || "")
    .replace(/^(ru|de|fr|it|es)\//, "")
    .replace(/\/index$/, "")
    .replace(/^index$/, "");
  if (!trimmed || (CONTENT_LOCALES as string[]).includes(trimmed)) return "index";
  return trimmed;
}

export function isTranslated(slug: string, locale: AppLocale): boolean {
  if (locale === "en") return true;
  const row = pages[normalizeSlug(slug)];
  const loc = row?.[locale];
  return Boolean(loc && loc.status && loc.status !== "missing");
}

export function translationStatus(slug: string, locale: AppLocale): string {
  if (locale === "en") return "current";
  const row = pages[normalizeSlug(slug)];
  return String(row?.[locale]?.status || "missing");
}

export function normalizeSlug(slug: string): string {
  const clean = String(slug || "")
    .replace(/^\/+|\/+$/g, "")
    .replace(/\/index$/, "");
  return clean === "" ? "index" : clean;
}

/**
 * Path for a docs slug in a locale.
 * Non-English locales always use the locale prefix. Starlight serves English
 * fallback content at that URL when a translation file does not exist.
 */
export function localeHref(slug: string, locale: AppLocale): string {
  const key = normalizeSlug(slug);
  if (locale === "en") {
    return withBase(key === "index" ? "/" : `${key}/`);
  }
  return withBase(key === "index" ? `${locale}/` : `${locale}/${key}/`);
}

export function englishHref(slug: string): string {
  return localeHref(slug, "en");
}

export function localeMeta(id: AppLocale) {
  return LOCALE_META.find((l) => l.id === id) || LOCALE_META[0];
}

export type CoverageRow = {
  locale: AppLocale;
  label: string;
  translated: number;
  current: number;
  outdated: number;
  missing: number;
  total: number;
  percent: number;
};

export function coverageRows(): CoverageRow[] {
  const slugs = Object.keys(pages);
  const total = file.englishPageCount || slugs.length;
  return CONTENT_LOCALES.map((locale) => {
    let current = 0;
    let outdated = 0;
    for (const slug of slugs) {
      const status = pages[slug]?.[locale]?.status;
      if (status === "current") current += 1;
      else if (status === "outdated") outdated += 1;
    }
    const translated = current + outdated;
    const missing = Math.max(0, total - translated);
    return {
      locale,
      label: localeMeta(locale).label,
      translated,
      current,
      outdated,
      missing,
      total,
      percent: total === 0 ? 0 : Math.round((translated / total) * 1000) / 10,
    };
  });
}

export function translatedSlugs(locale: AppLocale): string[] {
  return Object.keys(pages).filter((slug) => isTranslated(slug, locale));
}

import manifest from "../../data/videos/video-manifest.json";
import type { AppLocale } from "./locale";

export type VideoQuality = "recommended" | "useful" | "supplementary" | "legacy";

export type VideoTimestamp = { start: number; label: string };

export type VideoRecord = {
  youtubeId: string;
  url: string;
  title: string;
  channel: string;
  channelUrl?: string;
  published?: string;
  duration?: number;
  language: string;
  subtitles?: string[];
  topics: string[];
  documentationPages: string[];
  series?: string;
  seriesPart?: number;
  quality: VideoQuality;
  availability: string;
  review: string;
  verifiedAt: string;
  seed?: boolean;
  sourceAlias?: string;
  warnings?: string[];
  timestamps?: VideoTimestamp[];
  descriptions?: Partial<Record<AppLocale, string>>;
};

const all = (manifest as { videos: VideoRecord[] }).videos;

const QUALITY_RANK: Record<VideoQuality, number> = {
  recommended: 0,
  useful: 1,
  supplementary: 2,
  legacy: 3,
};

export const VIDEO_TOPICS = [
  { id: "level-editor", label: "Level Editor" },
  { id: "level-building", label: "Building levels" },
  { id: "areas", label: "Areas" },
  { id: "scripting", label: "Scripting" },
  { id: "assets", label: "Assets" },
  { id: "entities", label: "Entities" },
  { id: "materials", label: "Materials" },
  { id: "particles", label: "Particles" },
  { id: "audio", label: "Audio" },
  { id: "dialogue", label: "Dialogue" },
  { id: "debugging", label: "Debugging" },
  { id: "mod-setup", label: "Mod setup" },
  { id: "terrain", label: "Terrain" },
  { id: "lighting", label: "Lighting" },
] as const;

export function canonicalWatchUrl(id: string, start?: number): string {
  const base = `https://www.youtube.com/watch?v=${id}`;
  return start && start > 0 ? `${base}&t=${Math.floor(start)}s` : base;
}

export function privacyEmbedUrl(id: string, start?: number): string {
  const t = start && start > 0 ? `?start=${Math.floor(start)}` : "";
  return `https://www.youtube-nocookie.com/embed/${id}${t}`;
}

export function productionVideos(): VideoRecord[] {
  return all.filter((v) => v.review === "verified" && v.availability === "public");
}

export function videosForPage(slug: string, locale: AppLocale = "en", limit = 3): VideoRecord[] {
  const key = slug.replace(/^\/+|\/+$/g, "") || "index";
  const matches = productionVideos().filter((v) => v.documentationPages.includes(key));
  matches.sort((a, b) => compareVideos(a, b, locale));
  return matches.slice(0, limit);
}

export function videoCountForPage(slug: string): number {
  const key = slug.replace(/^\/+|\/+$/g, "") || "index";
  return productionVideos().filter((v) => v.documentationPages.includes(key)).length;
}

export function filterVideos(opts: {
  query?: string;
  topic?: string;
  quality?: string;
  language?: string;
  locale?: AppLocale;
}): VideoRecord[] {
  const q = (opts.query || "").trim().toLowerCase();
  const locale = opts.locale || "en";
  const out = productionVideos().filter((v) => {
    if (opts.topic && !v.topics.includes(opts.topic) && !v.documentationPages.some((p) => p === opts.topic || p.startsWith(`${opts.topic}/`))) {
      return false;
    }
    if (opts.quality && v.quality !== opts.quality) return false;
    if (opts.language && opts.language !== "all") {
      if (opts.language === "other") {
        if (["en", "ru", "de", "fr", "it", "es"].includes(v.language)) return false;
      } else if (v.language !== opts.language && !v.subtitles?.some((s) => s === opts.language || s.startsWith(`${opts.language}-`))) {
        return false;
      }
    }
    if (q) {
      const hay = `${v.title} ${v.channel} ${v.sourceAlias || ""} ${v.topics.join(" ")} ${describe(v, locale)}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  });
  out.sort((a, b) => compareVideos(a, b, locale));
  return out;
}

function compareVideos(a: VideoRecord, b: VideoRecord, locale: AppLocale): number {
  const langA = languageScore(a, locale);
  const langB = languageScore(b, locale);
  if (langA !== langB) return langA - langB;
  const q = QUALITY_RANK[a.quality] - QUALITY_RANK[b.quality];
  if (q !== 0) return q;
  return (a.seriesPart ?? 99) - (b.seriesPart ?? 99);
}

function languageScore(v: VideoRecord, locale: AppLocale): number {
  if (v.language === locale) return 0;
  if (v.subtitles?.some((s) => s === locale || s.startsWith(`${locale}-`))) return 1;
  if (v.language === "en") return 2;
  return 3;
}

export function formatDuration(seconds?: number): string | null {
  if (!seconds || seconds < 1) return null;
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m}:${String(s).padStart(2, "0")}`;
}

export function describe(v: VideoRecord, locale: AppLocale): string {
  return v.descriptions?.[locale] || v.descriptions?.en || "";
}

export function productionStats() {
  const vids = productionVideos();
  const pages = new Set<string>();
  for (const v of vids) for (const p of v.documentationPages) pages.add(p);
  return {
    total: vids.length,
    recommended: vids.filter((v) => v.quality === "recommended").length,
    useful: vids.filter((v) => v.quality === "useful").length,
    supplementary: vids.filter((v) => v.quality === "supplementary").length,
    legacy: vids.filter((v) => v.quality === "legacy").length,
    pagesWithVideos: pages.size,
  };
}

export { all as allVideoRecords };

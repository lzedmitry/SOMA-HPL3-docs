#!/usr/bin/env node
/**
 * Live-validate production YouTube IDs via oEmbed.
 * Does not download video, audio, or thumbnails.
 */
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "../..");
const MANIFEST = join(ROOT, "data/videos/video-manifest.json");
const REJECTED = join(ROOT, "data/videos/rejected.json");

export function canonicalWatchUrl(id, start) {
  const base = `https://www.youtube.com/watch?v=${encodeURIComponent(id)}`;
  return start && start > 0 ? `${base}&t=${Math.floor(start)}s` : base;
}

export function oembedUrl(id) {
  return `https://www.youtube.com/oembed?format=json&url=${encodeURIComponent(canonicalWatchUrl(id))}`;
}

export function classifyOembedStatus(httpStatus, body) {
  if (httpStatus === 200) {
    try {
      const data = typeof body === "string" ? JSON.parse(body) : body;
      if (data && data.title && data.author_name) return { availability: "public", title: data.title, channel: data.author_name };
    } catch {
      return { availability: "validation-error", reason: "oEmbed JSON parse failed" };
    }
    return { availability: "validation-error", reason: "oEmbed missing title" };
  }
  if (httpStatus === 401 || httpStatus === 403) return { availability: "private", reason: `HTTP ${httpStatus}` };
  if (httpStatus === 404) return { availability: "unavailable", reason: "HTTP 404" };
  return { availability: "validation-error", reason: `HTTP ${httpStatus}` };
}

async function fetchOembed(id) {
  const res = await fetch(oembedUrl(id), { headers: { Accept: "application/json" } });
  const text = await res.text();
  return { httpStatus: res.status, ...classifyOembedStatus(res.status, text) };
}

function loadJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

export async function checkManifest({ fetchOne = fetchOembed, manifestPath = MANIFEST, rejectedPath = REJECTED } = {}) {
  const manifest = loadJson(manifestPath);
  const rejected = loadJson(rejectedPath);
  const videos = manifest.videos || [];
  const results = [];
  let failedRecommended = 0;
  let failedProduction = 0;
  for (const v of videos) {
    const live = await fetchOne(v.youtubeId);
    const row = {
      youtubeId: v.youtubeId,
      expectedAvailability: v.availability,
      liveAvailability: live.availability,
      liveTitle: live.title || null,
      storedTitle: v.title,
      quality: v.quality,
      review: v.review,
      reason: live.reason || null,
    };
    if (v.review === "verified" && v.availability === "public" && live.availability !== "public") {
      failedProduction += 1;
      if (v.quality === "recommended") failedRecommended += 1;
    }
    results.push(row);
  }
  const rejectedIds = new Set((rejected.items || []).map((x) => x.youtubeId));
  return { results, failedProduction, failedRecommended, rejectedIds: [...rejectedIds], checkedAt: new Date().toISOString() };
}

const isMain = process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1];
if (isMain) {
  const report = await checkManifest();
  mkdirSync(join(ROOT, "reports"), { recursive: true });
  const md = [
    "# Video check",
    "",
    `Checked: ${report.checkedAt}`,
    `Production failures: ${report.failedProduction}`,
    `Recommended failures: ${report.failedRecommended}`,
    "",
    "| ID | stored title | live | status |",
    "| --- | --- | --- | --- |",
    ...report.results.map((r) => `| ${r.youtubeId} | ${r.storedTitle.replace(/\|/g, "/")} | ${r.liveTitle || "—"} | ${r.liveAvailability}${r.reason ? ` (${r.reason})` : ""} |`),
    "",
  ].join("\n");
  writeFileSync(join(ROOT, "reports/video-check.md"), md);
  console.log(`Checked ${report.results.length} videos. Production failures: ${report.failedProduction}.`);
  if (report.failedRecommended > 0) {
    console.error("Recommended video(s) are no longer public.");
    process.exit(1);
  }
  if (report.failedProduction > 0) process.exit(2);
}

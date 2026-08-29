import manifest from "../../data/source-manifest.json";
import api from "../data/api-index.json";

type SourcePage = { status?: string };
type Manifest = { syncedAt?: string; pages: SourcePage[] };

const m = manifest as Manifest;
const functions = api as unknown[];

export function getDocsStats() {
  const pages = m.pages || [];
  let wip = 0;
  let undocumented = 0;
  for (const page of pages) {
    const status = (page.status || "").toLowerCase();
    if (status === "wip") wip += 1;
    if (status === "undocumented") undocumented += 1;
  }
  const synced = m.syncedAt ? m.syncedAt.slice(0, 10) : "unknown";
  return {
    sourcePages: pages.length,
    apiFunctions: functions.length,
    wip,
    undocumented,
    syncedAt: synced,
  };
}

/**
 * Wiki sync entry (TypeScript wrapper).
 * Usage: pnpm sync:wiki
 * Implementation: Python MediaWiki importer in scripts/wiki/.
 */
import { spawnSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const dry = process.argv.includes("--dry-run");
const fetch = spawnSync("python3", ["scripts/wiki/fetch_wiki.py"], {
  cwd: root,
  stdio: "inherit",
});
if (fetch.status) process.exit(fetch.status ?? 1);
if (dry) {
  console.log("dry-run: fetch complete, skipping transform");
  process.exit(0);
}
const transform = spawnSync("python3", ["scripts/wiki/transform.py"], {
  cwd: root,
  stdio: "inherit",
});
process.exit(transform.status ?? 1);

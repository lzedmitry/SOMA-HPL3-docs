import { describe, it } from "node:test";
import assert from "node:assert/strict";
import { canonicalWatchUrl, oembedUrl, classifyOembedStatus } from "./check.mjs";

describe("videos:check helpers", () => {
  it("builds a canonical watch URL from an id", () => {
    assert.equal(canonicalWatchUrl("7oHfje9PKNo"), "https://www.youtube.com/watch?v=7oHfje9PKNo");
    assert.equal(canonicalWatchUrl("7oHfje9PKNo", 42), "https://www.youtube.com/watch?v=7oHfje9PKNo&t=42s");
  });

  it("does not invent ids or use non-YouTube hosts", () => {
    const url = canonicalWatchUrl("abc_DEF-123");
    assert.match(url, /^https:\/\/www\.youtube\.com\/watch\?v=abc_DEF-123$/);
    assert.ok(!url.includes("youtu.be/mirror"));
  });

  it("points oEmbed at the official YouTube endpoint", () => {
    const url = oembedUrl("ZIN9v0SohHo");
    assert.ok(url.startsWith("https://www.youtube.com/oembed?format=json&url="));
    assert.ok(url.includes("watch%3Fv%3DZIN9v0SohHo") || url.includes("watch?v=ZIN9v0SohHo"));
  });

  it("classifies oEmbed HTTP statuses", () => {
    const ok = classifyOembedStatus(200, JSON.stringify({ title: "Hello", author_name: "Draugemalf" }));
    assert.equal(ok.availability, "public");
    assert.equal(ok.title, "Hello");
    assert.equal(classifyOembedStatus(404, "").availability, "unavailable");
    assert.equal(classifyOembedStatus(403, "").availability, "private");
    assert.equal(classifyOembedStatus(500, "").availability, "validation-error");
  });
});

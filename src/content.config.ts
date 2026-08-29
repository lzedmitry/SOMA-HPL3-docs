import { defineCollection, z } from "astro:content";
import { docsLoader, i18nLoader } from "@astrojs/starlight/loaders";
import { docsSchema, i18nSchema } from "@astrojs/starlight/schema";

export const collections = {
  docs: defineCollection({
    loader: docsLoader(),
    schema: docsSchema({
      extend: z.object({
        sourceUrl: z.string().optional(),
        sourceRevision: z.union([z.string(), z.number()]).optional(),
        sourceUpdated: z.string().optional(),
        lastSynced: z.string().optional(),
        sourceStatus: z.string().optional(),
        category: z.string().optional(),
        difficulty: z.string().optional(),
        generated: z.boolean().optional(),
        tags: z.array(z.string()).optional(),
        derivedFrom: z.array(z.string()).optional(),
        translation: z
          .object({
            locale: z.string(),
            sourceLocale: z.string().default("en"),
            sourceRevision: z.union([z.string(), z.number()]).optional(),
            translationRevision: z.union([z.string(), z.number()]).optional(),
            status: z.enum(["current", "outdated", "missing"]).default("current"),
          })
          .optional(),
      }),
    }),
  }),
  i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
};

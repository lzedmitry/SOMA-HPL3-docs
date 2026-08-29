import { defineRouteMiddleware } from "@astrojs/starlight/route-data";

export const onRequest = defineRouteMiddleware((context) => {
  if (context.locals.starlightRoute.isFallback) {
    context.locals.starlightRoute.entry.data.pagefind = false;
  }
});

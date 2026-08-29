# Link audit

Classification of markdown links in `src/content/docs`.
This report does **not** rewrite pages. Wiki URLs that the importer could not map locally stay as intentional source links or missing-source-page.

## Counts

| Category | Count | Meaning |
| --- | ---: | --- |
| resolved-local | 2929 | Internal path that exists |
| intentional-external | 734 | Wiki/source or third-party URL kept on purpose |
| shared-HPL3 | 863 | Shared HPL3 Wiki URL; a local page may exist |
| missing-source-page | 8680 | Wiki target not in the import (often a redlink) |
| legacy-dokuwiki | 117 | Old `:hpl3:` / doku-style path |
| media-file | 97 | File: / Image: (not inlined) |
| special-page | 3 | MediaWiki Special:/Help: |
| unsupported-namespace | 1 | Category/Template/User/Talk |
| anchor-only | 2105 | Same-page `#anchor` |
| broken | 0 | Internal path with no matching page |

**Total classified:** 15529

## Notable missing Wiki targets

These names were called out in the original hub pages. They are **not** local defects if the Wiki never published the article.

- `HPL3/Areas/MapTransfer Area` — missing-source-page (no Wiki article / not imported)
- `HPL3/Areas/Visibility Area` — missing-source-page (no Wiki article / not imported)
- `HPL3/Level Design/Creating Terrain` — missing-source-page (no Wiki article / not imported)
- `HPL3/Level Design/Environment Particles` — missing-source-page (no Wiki article / not imported)
- `HPL3/Level Design/HDR` — missing-source-page (no Wiki article / not imported)
- `HPL3/Scripting/Scripting Conventions` — missing-source-page (no Wiki article / not imported)
- `HPL3/Sound/Playing Music` — missing-source-page (no Wiki article / not imported)

## Samples

### resolved-local

- `src/content/docs/404.md → /`
- `src/content/docs/404.md → /start/`
- `src/content/docs/404.md → /api/`
- `src/content/docs/404.md → /`
- `src/content/docs/404.md → /wiki-index/`
- `src/content/docs/scripting/timers.md → /about/licensing/`
- `src/content/docs/scripting/conclusion-basic.md → /about/licensing/`
- `src/content/docs/scripting/working-with-classes.md → /scripting/angelscript/chapter-8-classes/`
- `src/content/docs/scripting/working-with-classes.md → /about/licensing/`
- `src/content/docs/scripting/calling-functions-and-function-callbacks.md → /about/licensing/`
- `src/content/docs/scripting/the-update-method.md → /about/licensing/`
- `src/content/docs/scripting/amnesia-style-inventory-script-reference.md → /about/licensing/`

### intentional-external

- `src/content/docs/scripting/amnesia-style-inventory-script-reference.md → http://steamcommunity.com/sharedfiles/filedetails/?id=541404608`
- `src/content/docs/scripting/amnesia-style-inventory-script-reference.md → http://www.moddb.com/mods/amnesia-style-inventory-management-system`
- `src/content/docs/scripting/amnesia-style-inventory-script-reference.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Tutorials/Scripting/Amnesia-Style_Inventory_Script_Reference`
- `src/content/docs/scripting/setting-up-codelite.md → https://downloads.codelite.org/ReleaseArchive.php`
- `src/content/docs/scripting/index.mdx → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting`
- `src/content/docs/scripting/input-types.md → https://youtu.be/ZS0fIS2qrSA`
- `src/content/docs/scripting/input-types.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Input_Types`
- `src/content/docs/scripting/setting-up-visual-studio-code.md → https://marketplace.visualstudio.com/items?itemName=TiManGames.hpl3-language-tools`
- `src/content/docs/scripting/setting-up-visual-studio-code.md → https://github.com/TiManGames/hpl3-language-tools/releases`
- `src/content/docs/scripting/setting-up-visual-studio-code.md → https://github.com/TiManGames/hpl3-language-tools`
- `src/content/docs/scripting/setting-up-visual-studio-code.md → https://github.com/TiManGames/hpl3-language-tools/issues`
- `src/content/docs/scripting/terminals-overview.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Terminals_Overview`

### shared-HPL3

- `src/content/docs/scripting/timers.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Timers`
- `src/content/docs/scripting/timers.md → https://wiki.frictionalgames.com/page/HPL3/SOMA`
- `src/content/docs/scripting/conclusion-basic.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Conclusion_-_Basic`
- `src/content/docs/scripting/conclusion-basic.md → https://wiki.frictionalgames.com/page/HPL3/SOMA`
- `src/content/docs/scripting/working-with-classes.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Working_with_Classes`
- `src/content/docs/scripting/working-with-classes.md → https://wiki.frictionalgames.com/page/HPL3/SOMA`
- `src/content/docs/scripting/calling-functions-and-function-callbacks.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Calling_Functions_and_Function_Callbacks`
- `src/content/docs/scripting/calling-functions-and-function-callbacks.md → https://wiki.frictionalgames.com/page/HPL3/SOMA`
- `src/content/docs/scripting/the-update-method.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/The_Update_method`
- `src/content/docs/scripting/the-update-method.md → https://wiki.frictionalgames.com/page/HPL3/SOMA`
- `src/content/docs/scripting/amnesia-style-inventory-script-reference.md → https://wiki.frictionalgames.com/page/HPL3/SOMA`
- `src/content/docs/scripting/object-handles.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/Object_Handles`

### missing-source-page

- `src/content/docs/scripting/timers.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Map_Helper`
- `src/content/docs/scripting/timers.md → https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Scripting/Map_Helper`
- `src/content/docs/scripting/what-is-scripting-in-hpl3.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Scripting_Guide/What_is_scripting_in_HPL3?`
- `src/content/docs/scripting/setting-up-codelite.md → https://wiki.frictionalgames.com/page/CodeLite#Optimized_Color_Theme`
- `src/content/docs/scripting/scripting-workflow-and-structure.md → https://wiki.frictionalgames.com/page/HPL3/Scripting/Helper_Files`
- `src/content/docs/scripting/input-types.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Input_Handler`
- `src/content/docs/scripting/input-types.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Player_Overview`
- `src/content/docs/scripting/terminals-overview.md → https://www.frictionalgames.com/forum/thread-31645.html`
- `src/content/docs/scripting/terminals-overview.md → https://wiki.frictionalgames.com/hpl3/community/hpl3_getting_started`
- `src/content/docs/scripting/sequences.md → https://wiki.frictionalgames.com/page/HPL3/SOMA/Scripting/Sequences_Helper`
- `src/content/docs/scripting/sequences.md → https://wiki.frictionalgames.com/page/HPL3/Amnesia:_Rebirth/Scripting/Sequences_Helper`
- `src/content/docs/materials/materials-overview.md → https://wiki.frictionalgames.com/page/HPL3/Materials/Physics_Material`

### legacy-dokuwiki

- `src/content/docs/scripting/level-scripting-best-practices.md → https://wiki.frictionalgames.com/page/:hpl3:3rdparty:codelite`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/hpl3:engine:model_export#modelling`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#solid_diffuse`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#decal`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#projecteduv`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#soliddiffuse`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#terrain`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#terraindecal`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#translucent`
- `src/content/docs/materials/materials-editor-view.md → https://wiki.frictionalgames.com/page/hpl3:engine:materials#water`
- `src/content/docs/entities/model-editor-view.md → https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:save_dialog`
- `src/content/docs/entities/model-editor-view.md → https://wiki.frictionalgames.com/page/:hpl3:tools:maineditors:level_editor:load_dialog`

### media-file

- `src/content/docs/scripting/setting-up-codelite.md → https://wiki.frictionalgames.com/page/File:Codelite-window.png`
- `src/content/docs/scripting/setting-up-codelite.md → https://wiki.frictionalgames.com/page/File:Codelite_custom_build.png`
- `src/content/docs/scripting/terminals-overview.md → https://wiki.frictionalgames.com/page/File:capture.png`
- `src/content/docs/scripting/hello-world.md → https://wiki.frictionalgames.com/page/File:Debug_message_tut.png`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans01.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans02.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans03.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans04.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans05.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans06.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans07.jpg`
- `src/content/docs/materials/translucent.md → https://wiki.frictionalgames.com/page/File:material_trans08.jpg`

### special-page

- `src/content/docs/about/frictional-wiki-about.md → https://wiki.frictionalgames.com/page/Help:Contents`
- `src/content/docs/about/frictional-wiki-about.md → https://wiki.frictionalgames.com/page/Special:RecentChanges`
- `src/content/docs/about/frictional-wiki-about.md → https://wiki.frictionalgames.com/page/Special:NewPages`

### unsupported-namespace

- `src/content/docs/scripting/tutorials.md → https://wiki.frictionalgames.com/page/User:TiMan`

### anchor-only

- `src/content/docs/api/wiki-index.md → #constants-ccolor-blue-ccolor-blue`
- `src/content/docs/api/wiki-index.md → #constants-ccolor-green-ccolor-green`
- `src/content/docs/api/wiki-index.md → #constants-ccolor-red-ccolor-red`
- `src/content/docs/api/wiki-index.md → #constants-ccolor-white-ccolor-white`
- `src/content/docs/api/wiki-index.md → #constants-cmath-epsilon-cmath-epsilon`
- `src/content/docs/api/wiki-index.md → #constants-cmath-pi-cmath-pi`
- `src/content/docs/api/wiki-index.md → #constants-cmath-pidiv2-cmath-pidiv2`
- `src/content/docs/api/wiki-index.md → #constants-cmath-pidiv4-cmath-pidiv4`
- `src/content/docs/api/wiki-index.md → #constants-cmath-pimul2-cmath-pimul2`
- `src/content/docs/api/wiki-index.md → #constants-cmath-sqrt2-cmath-sqrt2`
- `src/content/docs/api/wiki-index.md → #constants-cmatrixf-identity-cmatrixf-identity`
- `src/content/docs/api/wiki-index.md → #constants-cmatrixf-zero-cmatrixf-zero`


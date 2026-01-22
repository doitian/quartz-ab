# Quartz Configuration

This directory contains Quartz configuration files and patches.

## Configuration Files

- **`quartz.config.ts`** - Main Quartz configuration (site title, base URL, theme, plugins)
- **`quartz.layout.ts`** - Page layout configuration (components, navigation)

## Patches

### quartz-shortest-path.patch

This patch fixes the shortest path resolution for wikilinks in Quartz to be fully compatible with Obsidian.

**What it fixes:**
The original implementation only matched exact filenames when using the "shortest" path strategy. For example, a link like `[[bft-consensus/fundamentals]]` would not resolve correctly if the file was at `content/bft-consensus-analysis/bft-consensus/fundamentals.md`.

**How it works:**
The patch modifies the `transformLink` function in `quartz/util/path.ts` to:
1. Split the target path into segments (e.g., `["bft-consensus", "fundamentals"]`)
2. Match slugs by comparing path segments from the end
3. If a slug ends with the target path segments, it's considered a match

This allows Obsidian-style wikilinks with partial paths to work correctly:
- `[[fundamentals]]` → matches `bft-consensus-analysis/bft-consensus/fundamentals.md`
- `[[bft-consensus/fundamentals]]` → matches `bft-consensus-analysis/bft-consensus/fundamentals.md`
- Both resolve to the same file if there's only one match

**Application:**
The patch is automatically applied during the GitHub Actions build process. See `.github/workflows/deploy.yml` for details.

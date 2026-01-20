# Quartz AB

This repository is an Obsidian vault that is published to GitHub Pages using [Quartz](https://quartz.jzhao.xyz/).

## Structure

- **`content/`** - Markdown files for the Obsidian vault
- **`quartz/`** - Quartz static site generator (git submodule)
- **`config/`** - Quartz configuration files
- **`.obsidian/`** - Obsidian vault configuration

## Local Development

### Prerequisites

- [Obsidian](https://obsidian.md/) for editing notes
- [Node.js](https://nodejs.org/) v22 or higher for building the site

### Opening in Obsidian

1. Open Obsidian
2. Click "Open folder as vault"
3. Select this repository directory

### Building the Site Locally

```bash
# Initialize the quartz submodule
git submodule update --init --recursive

# Install dependencies
cd quartz
npm ci

# Copy config files
cp ../config/quartz.config.ts .
cp ../config/quartz.layout.ts .

# Build the site
npx quartz build --directory ../content

# Serve locally
npx quartz build --serve --directory ../content
```

## Publishing

The site is automatically built and deployed to GitHub Pages when changes are pushed to the `main` branch.

## Configuration

- **`config/quartz.config.ts`** - Main Quartz configuration (site title, base URL, theme, plugins)
- **`config/quartz.layout.ts`** - Page layout configuration (components, navigation)
- **`.obsidian/app.json`** - Obsidian vault settings

## License

See [LICENSE](LICENSE) for details.

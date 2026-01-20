# Setup Guide

This repository has been configured as an Obsidian vault with Quartz for publishing to GitHub Pages.

## What was created

### 1. Content Directory (`content/`)
Contains the Obsidian vault markdown files:
- `index.md` - Main landing page
- `About.md` - About page
- `Notes/Sample Note.md` - Example note with markdown features

### 2. Quartz Submodule (`quartz/`)
The Quartz static site generator is added as a git submodule from https://github.com/jackyzha0/quartz

### 3. Configuration Directory (`config/`)
Contains Quartz configuration files:
- `quartz.config.ts` - Main configuration (site title, URL, theme, plugins)
- `quartz.layout.ts` - Layout and component configuration

### 4. Obsidian Configuration (`.obsidian/`)
Vault settings for Obsidian:
- `app.json` - Application settings
- `core-plugins.json` - Enabled core plugins

Note: Workspace files are excluded via `.gitignore` to avoid conflicts between different users.

### 5. GitHub Actions Workflow (`.github/workflows/deploy.yml`)
Automated deployment pipeline that:
- Triggers on push to `main` branch
- Checks out the repository with submodules
- Installs Node.js v22 and dependencies
- Copies config files to quartz directory
- Builds the site from `content/` directory
- Deploys to GitHub Pages

### 6. Git Configuration
- `.gitignore` - Excludes build artifacts, dependencies, and temporary files
- `.gitmodules` - Defines the quartz submodule

## Next Steps

### To use this vault in Obsidian:
1. Clone this repository with submodules:
   ```bash
   git clone --recursive https://github.com/doitian/quartz-ab.git
   ```
2. Open Obsidian
3. Choose "Open folder as vault"
4. Select the repository directory

### To enable GitHub Pages:
1. Go to repository Settings → Pages
2. Under "Build and deployment", select:
   - Source: GitHub Actions
3. Push changes to the `main` branch to trigger deployment

### To add more content:
1. Create new markdown files in the `content/` directory
2. Use Obsidian wikilinks: `[[Page Name]]`
3. Organize files in subdirectories as needed
4. Commit and push to deploy

### To customize the site:
Edit the configuration files in `config/`:
- Modify site title, colors, fonts in `quartz.config.ts`
- Adjust page layout and components in `quartz.layout.ts`

## Configuration Highlights

- **Site Title**: Quartz AB
- **Base URL**: doitian.github.io/quartz-ab
- **Theme**: Light and dark mode with customizable colors
- **Features**:
  - Single Page Application (SPA) mode
  - Popovers for link previews
  - Full-text search
  - Graph view
  - Backlinks
  - Table of contents
  - Syntax highlighting
  - Obsidian-flavored markdown

## Troubleshooting

### Submodule not initialized
If the `quartz/` directory is empty, run:
```bash
git submodule update --init --recursive
```

### Build requires Node.js v22
Make sure you have Node.js v22 or higher installed for local development. The GitHub Actions workflow uses Node.js v22.

### Changes not appearing on GitHub Pages
1. Check the Actions tab for workflow runs
2. Ensure GitHub Pages is configured to use GitHub Actions
3. Verify the workflow completed successfully

## Resources

- [Quartz Documentation](https://quartz.jzhao.xyz/)
- [Obsidian Documentation](https://help.obsidian.md/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

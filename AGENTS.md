# Wikilink Strategy for Quartz Obsidian Compatibility

## Strategy

Use Quartz's `markdownLinkResolution: "shortest"` without patching quartz code.

**For unique filenames:** Use basename only
```markdown
[[fundamentals]]  ✅
[[bft-consensus/fundamentals]]  ❌
```

**For non-unique filenames:** Use full path inside `content/`
```markdown
[[bft-consensus-analysis/logic-models/overview]]  ✅
[[logic-models/overview]]  ❌
[[overview]]  ❌
```

## Current Non-Unique Files
- `index.md` - root and bft-consensus-analysis
- `overview.md` - logic-models and provable-broadcast

## Rules
- ❌ No patching quartz source code
- ❌ No `.md` extensions in wikilinks
- ✅ Use basename for unique files
- ✅ Use full path from `content/` for duplicates

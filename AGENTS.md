# Wikilink Strategy for Quartz Obsidian Compatibility

## Strategy

Use Quartz's `markdownLinkResolution: "absolute"` strategy.

**All wikilinks use full path from `content/` directory with page title as display text:**

```markdown
[[bft-consensus-analysis/bft-consensus/fundamentals|BFT Consensus Fundamentals]]  ✅
[[fundamentals]]  ❌ (basename only - not used)
[[bft-consensus/fundamentals]]  ❌ (partial path - not used)
```

## Rules
- ❌ No patching quartz source code
- ❌ No `.md` extensions in wikilinks
- ❌ No relative paths (`../` or `./`)
- ✅ Always use full absolute path from `content/` directory
- ✅ Always include page title as display text: `[[path|Title]]`

## Examples

```markdown
# Good:
[[bft-consensus-analysis/logic-models/overview|Logic Models for Distributed Systems]]
[[bft-consensus-analysis/glossary|Glossary: BFT Consensus, Provable Broadcast, and Logic Models]]
[[index|Welcome to Quartz AB]]

# Bad:
[[overview]]  # Missing path and title
[[logic-models/overview]]  # Partial path
[[../overview|Overview]]  # Relative path
```

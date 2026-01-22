# Agent Instructions for Quartz AB Repository

## Wikilink Strategy for Quartz Obsidian Compatibility

### Strategy

Use Quartz's `markdownLinkResolution: "absolute"` strategy.

**All wikilinks use full path from `content/` directory with descriptive display text:**

```markdown
[[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]]  ✅
[[fundamentals]]  ❌ (basename only - not used)
[[bft-consensus/fundamentals]]  ❌ (partial path - not used)
```

### Rules
- ❌ No `.md` extensions in wikilinks
- ❌ No relative paths (`../` or `./`)
- ✅ Always use full absolute path from `content/` directory
- ✅ Use natural, concise display text that flows well in context
- ✅ Display text can be shorter than page title for better readability

### Examples

```markdown
# Good - concise, natural display text:
[[bft-consensus-analysis/logic-models/overview|Logic Models Overview]]
[[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]]
[[bft-consensus-analysis/glossary|Glossary]]
[[bft-consensus-analysis/bft-consensus/protocols/pbft|PBFT]]

# Also good - more descriptive when needed:
[[bft-consensus-analysis/integration/relationships|Three-Way Connections]]
[[bft-consensus-analysis/provable-broadcast/applications|Real-World Usage in Blockchain & DLT]]

# Bad:
[[overview]]  # Missing path
[[logic-models/overview|Logic Models for Distributed Systems]]  # Partial path
[[../overview|Overview]]  # Relative path
```

### Display Text Guidelines

- Use concise names in lists: `[[path|PBFT]]` not `[[path|PBFT: Practical Byzantine Fault Tolerance]]`
- Use descriptive text that fits the sentence context
- Shorter is often better for readability
- Can differ from the actual page title if it makes the text flow better

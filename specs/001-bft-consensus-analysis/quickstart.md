# Quickstart Guide: BFT Consensus Analysis Knowledge Base

**Feature**: 001-bft-consensus-analysis  
**Date**: 2026-01-21  
**Audience**: Researchers, practitioners, and students learning about BFT consensus, provable broadcast, and formal verification

---

## Welcome!

This knowledge base explores the relationships between three critical areas of distributed systems:

1. **Byzantine Fault Tolerant (BFT) Consensus** - Protocols that reach agreement despite malicious failures
2. **Provable Broadcast** - Communication primitives with cryptographic delivery proofs
3. **Logic Models** - Formal frameworks for specifying and verifying consensus properties

Whether you're a blockchain developer, distributed systems researcher, or formal methods practitioner, this guide will help you navigate the content effectively.

---

## Quick Navigation

### Start Here

Choose your entry point based on your background and goals:

| Your Background | Recommended Starting Point | Why |
|----------------|---------------------------|-----|
| **New to distributed systems** | [[bft-consensus/fundamentals]] | Build foundational understanding |
| **Blockchain developer** | [[provable-broadcast/applications]] | See practical applications first |
| **Formal verification engineer** | [[logic-models/overview]] | Start with verification frameworks |
| **Experienced with consensus** | [[integration/relationships]] | Dive into synthesis |
| **Want a specific protocol** | [[bft-consensus/protocols/protocol-comparison]] | Compare protocols side-by-side |
| **Just browsing** | [[index]] | High-level overview with links |

---

## Learning Paths

### Path 1: Fundamentals First (Recommended for Beginners)

**Goal**: Build understanding from the ground up

1. Read [[glossary]] to familiarize yourself with key terms
2. Start with [[bft-consensus/fundamentals]] to understand consensus basics
3. Learn about [[bft-consensus/byzantine-failures]] to understand the threat model
4. Explore [[provable-broadcast/reliable-broadcast]] to grasp broadcast primitives
5. Progress to [[provable-broadcast/provable-broadcast]] to see the enhancement
6. Study specific protocols: [[bft-consensus/protocols/pbft]] → [[bft-consensus/protocols/honeybadger-bft]]
7. Understand formal methods via [[logic-models/knowledge-framework]]
8. Synthesize knowledge in [[integration/relationships]]

**Time Estimate**: 4-6 hours for thorough reading

---

### Path 2: Protocol-Centric (For Practitioners)

**Goal**: Understand practical BFT protocols and their trade-offs

1. Skim [[bft-consensus/fundamentals]] for context
2. Read [[bft-consensus/protocols/protocol-comparison]] for high-level comparison
3. Deep dive into protocols relevant to your work:
   - [[bft-consensus/protocols/pbft]] - Classic, widely studied
   - [[bft-consensus/protocols/honeybadger-bft]] - Asynchronous, robust
   - [[bft-consensus/protocols/hotstuff]] - Linear complexity, modern
4. Understand the broadcast mechanisms they use: [[provable-broadcast/overview]]
5. See integration in action: [[integration/case-studies/honeybadger-complete]]
6. Apply to design: [[integration/design-framework]]

**Time Estimate**: 3-4 hours

---

### Path 3: Formal Verification Focus (For Researchers)

**Goal**: Learn how to formally verify consensus protocols

1. Review [[logic-models/overview]] for framework introduction
2. Study [[logic-models/knowledge-framework]] (Halpern-Moses foundations)
3. Learn temporal logic: [[logic-models/temporal-logic]]
4. Understand verification techniques: [[logic-models/formal-verification]]
5. See verification applied to protocols: [[integration/case-studies/honeybadger-complete]]
6. Explore advanced: [[logic-models/threshold-automata]]

**Time Estimate**: 5-7 hours (more if diving into formal proofs)

---

### Path 4: Broadcast Mechanisms Deep Dive

**Goal**: Master broadcast primitives from basic to advanced

1. Start with [[provable-broadcast/reliable-broadcast]]
2. Progress to [[provable-broadcast/byzantine-reliable-broadcast]]
3. Understand the key innovation: [[provable-broadcast/provable-broadcast]]
4. Compare approaches: [[provable-broadcast/vs-reliable-broadcast]]
5. See real-world usage: [[provable-broadcast/applications]]
6. Study properties formally: [[provable-broadcast/properties]]
7. See integration with consensus: [[integration/relationships]]

**Time Estimate**: 2-3 hours

---

## Using the Knowledge Base

### Obsidian Features

This knowledge base is designed for [Obsidian](https://obsidian.md/), a powerful markdown editor with:

- **Wikilinks**: Click `[[note-name]]` to navigate between notes
- **Graph View**: Visualize connections between notes (View → Open Graph View)
- **Backlinks**: See which notes reference the current note (right sidebar)
- **Search**: Find content across all notes (Cmd/Ctrl + Shift + F)
- **Tags**: Filter notes by tags like `#bft`, `#broadcast`, `#safety`

### Navigation Tips

1. **Use the Graph View**: See clusters of related topics
2. **Follow Wikilinks**: Each note links to related concepts
3. **Check Backlinks**: Discover related content you might have missed
4. **Use Search**: Find specific terms or concepts
5. **Filter by Tags**: Use tags in YAML frontmatter to group notes

### Understanding Note Structure

Every note follows this pattern:

```markdown
---
[YAML frontmatter with metadata]
---

# Title

[Brief overview]

## Prerequisites
[What to read first]

## Main Content
[Detailed explanation]

## Examples
[Concrete instances]

## See Also
[Related notes]
```

**Tip**: Check the `prerequisites` section to ensure you have the background knowledge.

---

## Finding What You Need

### By Topic

| Topic | Main Entry Point |
|-------|-----------------|
| BFT Consensus | [[bft-consensus/fundamentals]] |
| Safety Properties | [[bft-consensus/properties/safety-properties]] |
| Liveness Properties | [[bft-consensus/properties/liveness-properties]] |
| PBFT Protocol | [[bft-consensus/protocols/pbft]] |
| HoneyBadgerBFT | [[bft-consensus/protocols/honeybadger-bft]] |
| HotStuff | [[bft-consensus/protocols/hotstuff]] |
| Provable Broadcast | [[provable-broadcast/provable-broadcast]] |
| Reliable Broadcast | [[provable-broadcast/reliable-broadcast]] |
| Knowledge Framework | [[logic-models/knowledge-framework]] |
| Temporal Logic | [[logic-models/temporal-logic]] |
| Formal Verification | [[logic-models/formal-verification]] |
| Integration | [[integration/relationships]] |

### By Question

| Question | Navigate To |
|----------|-------------|
| What is Byzantine fault tolerance? | [[bft-consensus/fundamentals]] |
| Why can BFT only tolerate f < n/3 faults? | [[bft-consensus/properties/fault-tolerance-threshold]] |
| How does PBFT work? | [[bft-consensus/protocols/pbft]] |
| What's the difference between PBFT and HotStuff? | [[bft-consensus/protocols/protocol-comparison]] |
| What is provable broadcast? | [[provable-broadcast/provable-broadcast]] |
| How is it different from reliable broadcast? | [[provable-broadcast/vs-reliable-broadcast]] |
| Where is provable broadcast used? | [[provable-broadcast/applications]] |
| How do I formally verify a consensus protocol? | [[logic-models/formal-verification]] |
| What is common knowledge in distributed systems? | [[logic-models/knowledge-framework]] |
| How do BFT, broadcast, and logic models relate? | [[integration/relationships]] |
| Can I see a complete analysis of a real protocol? | [[integration/case-studies/honeybadger-complete]] |

### By Difficulty Level

Use tags to filter by complexity:

- `#introductory` - Accessible to those new to the topic
- `#intermediate` - Requires some background knowledge
- `#advanced` - Deep technical or mathematical content

**Search in Obsidian**: Use `tag:#introductory` in search bar

---

## Key Concepts & Terminology

Before diving in, familiarize yourself with these essential terms (see [[glossary]] for full definitions):

- **Byzantine Failure**: Arbitrary or malicious behavior by faulty nodes (not just crashes)
- **Consensus**: Agreement among distributed nodes on a single value
- **Safety**: "Something bad never happens" (e.g., no two nodes decide differently)
- **Liveness**: "Something good eventually happens" (e.g., a decision is eventually made)
- **f < n/3**: Byzantine fault tolerance threshold (can tolerate up to f faults in n nodes)
- **Provable Broadcast**: Broadcast with cryptographic proof of delivery
- **Delivery Certificate**: Proof that a supermajority of nodes received a message
- **Common Knowledge**: Everyone knows X, everyone knows that everyone knows X, recursively
- **Temporal Logic**: Logic for expressing properties over time (e.g., "eventually" or "always")

---

## External Resources

This knowledge base synthesizes information from authoritative sources:

### Primary Sources

- **Decentralized Thoughts** (decentralizedthoughts.github.io): Blog on distributed systems and consensus
- **arXiv cs/0006009**: Halpern & Moses, "Knowledge and common knowledge in a distributed environment"
- **Original Protocol Papers**: PBFT (Castro & Liskov), HoneyBadgerBFT (Miller et al.), HotStuff (Yin et al.)

See [[references]] for the complete bibliography with links.

### Recommended External Reading

- **Textbooks**:
  - "Introduction to Reliable and Secure Distributed Programming" by Cachin, Guerraoui, Rodrigues
  - "Distributed Algorithms" by Nancy Lynch
- **Surveys**:
  - "Reaching Consensus in the Byzantine Empire" (comprehensive BFT survey)
- **Tutorials**:
  - Decentralized Thoughts series on consensus

---

## How to Contribute or Extend

If you're maintaining this knowledge base:

### Adding New Content

1. **Choose the right location**: See [[contracts/directory-structure]]
2. **Use the note schema**: See [[contracts/note-schema]]
3. **Follow naming conventions**: Use kebab-case (e.g., `new-protocol.md`)
4. **Add YAML frontmatter**: Include required fields (title, type, tags, dates, status)
5. **Link generously**: Connect to related notes using wikilinks
6. **Update central files**: Add entries to `glossary.md`, `references.md` as needed
7. **Update comparisons**: If adding a protocol, update `protocol-comparison.md`

### Quality Standards

- **Cite sources**: Use [[references]] for all technical claims
- **Provide examples**: Include concrete instances, not just abstractions
- **Use diagrams**: Mermaid diagrams for sequences, flows, structures
- **Be accessible**: Start with intuition before formal definitions
- **Link prerequisites**: Help readers follow learning paths

---

## Getting Help

### Within the Knowledge Base

- **Glossary**: [[glossary]] - Definitions of technical terms
- **References**: [[references]] - Full citations and external links
- **Index**: [[index]] - Overview and main navigation

### Common Issues

| Problem | Solution |
|---------|----------|
| "This note assumes knowledge I don't have" | Check the `Prerequisites` section for suggested reading order |
| "I don't understand the formal notation" | See [[glossary]] for notation explanations; start with accessible notes tagged `#introductory` |
| "Wikilink doesn't resolve" | The note may not exist yet; check [[index]] for available content |
| "Too much detail, I just want the overview" | Look for "overview" or "fundamentals" notes in each domain |
| "Not enough detail, I want the math" | Look for notes with `#advanced` tag or sections titled "Formal Specification" |

---

## Success Metrics: Have You Learned?

After exploring the knowledge base, you should be able to:

✅ **Explain the difference** between crash failures and Byzantine failures  
✅ **Describe why** BFT consensus can only tolerate f < n/3 faults  
✅ **Compare** PBFT, HoneyBadgerBFT, and HotStuff on key dimensions  
✅ **Explain** how provable broadcast differs from reliable broadcast  
✅ **Identify scenarios** where provable broadcast is needed vs. overkill  
✅ **Express consensus properties** using temporal logic notation  
✅ **Understand** the role of common knowledge in distributed systems  
✅ **Trace how** a protocol like HoneyBadgerBFT uses BFT principles, provable broadcast, and can be formally verified  
✅ **Apply** the design framework to evaluate a new consensus protocol

If you can do most of these, congratulations—you've mastered the integrated perspective this knowledge base provides!

---

## Next Steps

Ready to begin? Choose your path:

- **Beginner**: Start with [[bft-consensus/fundamentals]]
- **Practitioner**: Jump to [[bft-consensus/protocols/protocol-comparison]]
- **Researcher**: Explore [[logic-models/overview]]
- **Curious**: Browse [[index]] and follow what interests you

---

## Version Information

- **Knowledge Base Version**: 1.0
- **Last Updated**: 2026-01-21
- **Content Status**: Planning phase complete, implementation in progress

---

## See Also

- [[index]] - Main navigation hub
- [[glossary]] - Technical terminology
- [[references]] - Bibliography
- [[contracts/note-schema]] - Metadata standards
- [[contracts/directory-structure]] - File organization

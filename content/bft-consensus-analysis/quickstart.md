---
title: "Quickstart Guide: BFT Consensus Analysis Knowledge Base"
type: guide
tags: [quickstart, navigation, learning-paths, getting-started]
created: 2026-01-21
updated: 2026-01-22
status: complete
difficulty: beginner
related:
  - "[[index|Welcome to Quartz AB]]"
  - "[[bft-consensus-analysis/glossary|Glossary]]"
  - "[[bft-consensus-analysis/references|References]]"
---

# Quickstart Guide: BFT Consensus Analysis Knowledge Base

**Feature**: 001-bft-consensus-analysis  
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
| **New to distributed systems** | [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]] | Build foundational understanding |
| **Blockchain developer** | [[bft-consensus-analysis/provable-broadcast/applications|Real-World Usage in Blockchain & DLT]] | See practical applications first |
| **Formal verification engineer** | [[bft-consensus-analysis/logic-models/overview|Logic Models Overview]] | Start with verification frameworks |
| **Experienced with consensus** | [[bft-consensus-analysis/integration/relationships|Three-Way Connections]] | Dive into synthesis |
| **Want a specific protocol** | [[bft-consensus-analysis/bft-consensus/protocols/protocol-comparison|Protocol Comparison]] | Compare protocols side-by-side |
| **Just browsing** | [[index|Welcome to Quartz AB]] | High-level overview with links |

---

## Learning Paths

### Path 1: Fundamentals First (Recommended for Beginners)

**Goal**: Build understanding from the ground up

1. Read [[bft-consensus-analysis/glossary|Glossary]] to familiarize yourself with key terms
2. Start with [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]] to understand consensus basics
3. Learn about [[bft-consensus-analysis/bft-consensus/byzantine-failures|Byzantine Failures]] to understand the threat model
4. Explore [[bft-consensus-analysis/provable-broadcast/reliable-broadcast|Reliable Broadcast]] to grasp broadcast primitives
5. Progress to [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]] to see the enhancement
6. Study specific protocols: [[bft-consensus-analysis/bft-consensus/protocols/pbft|PBFT]] → [[bft-consensus-analysis/bft-consensus/protocols/honeybadger-bft|HoneyBadgerBFT]]
7. Understand formal methods via [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]]
8. Synthesize knowledge in [[bft-consensus-analysis/integration/relationships|Three-Way Connections]]

**Time Estimate**: 4-6 hours for thorough reading

---

### Path 2: Protocol-Centric (For Practitioners)

**Goal**: Understand practical BFT protocols and their trade-offs

1. Skim [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]] for context
2. Read [[bft-consensus-analysis/bft-consensus/protocols/protocol-comparison|Protocol Comparison]] for high-level comparison
3. Deep dive into protocols relevant to your work:
   - [[bft-consensus-analysis/bft-consensus/protocols/pbft|PBFT]] - Classic, widely studied
   - [[bft-consensus-analysis/bft-consensus/protocols/honeybadger-bft|HoneyBadgerBFT]] - Asynchronous, robust
   - [[bft-consensus-analysis/bft-consensus/protocols/hotstuff|HotStuff]] - Linear complexity, modern
4. Understand the broadcast mechanisms they use: [[bft-consensus-analysis/provable-broadcast/overview|Provable Broadcast Overview]]
5. See integration in action: [[bft-consensus-analysis/integration/case-studies/honeybadger-complete|HoneyBadgerBFT Complete Analysis]]
6. Apply to design: [[bft-consensus-analysis/integration/design-framework|Applying All Three Perspectives]]

**Time Estimate**: 3-4 hours

---

### Path 3: Formal Verification Focus (For Researchers)

**Goal**: Learn how to formally verify consensus protocols

1. Review [[bft-consensus-analysis/logic-models/overview|Logic Models Overview]] for framework introduction
2. Study [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]] (Halpern-Moses foundations)
3. Learn temporal logic: [[bft-consensus-analysis/logic-models/temporal-logic|Expressing Safety & Liveness]]
4. Understand verification techniques: [[bft-consensus-analysis/logic-models/formal-verification|Formal Verification Techniques]]
5. See verification applied to protocols: [[bft-consensus-analysis/integration/case-studies/honeybadger-complete|HoneyBadgerBFT Complete Analysis]]
6. Explore advanced: [[bft-consensus-analysis/logic-models/threshold-automata|Threshold Automata]]

**Time Estimate**: 5-7 hours (more if diving into formal proofs)

---

### Path 4: Broadcast Mechanisms Deep Dive

**Goal**: Master broadcast primitives from basic to advanced

1. Start with [[bft-consensus-analysis/provable-broadcast/reliable-broadcast|Reliable Broadcast]]
2. Progress to [[bft-consensus-analysis/provable-broadcast/byzantine-reliable-broadcast|Byzantine Reliable Broadcast]]
3. Understand the key innovation: [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]]
4. Compare approaches: [[bft-consensus-analysis/provable-broadcast/vs-reliable-broadcast|Provable vs Reliable Broadcast]]
5. See real-world usage: [[bft-consensus-analysis/provable-broadcast/applications|Real-World Usage in Blockchain & DLT]]
6. Study properties formally: [[bft-consensus-analysis/provable-broadcast/properties|Provable Broadcast Properties]]
7. See integration with consensus: [[bft-consensus-analysis/integration/relationships|Three-Way Connections]]

**Time Estimate**: 2-3 hours

---

## Using the Knowledge Base

### Obsidian Features

This knowledge base is designed for [Obsidian](https://obsidian.md/), a powerful markdown editor with:

- **Wikilinks**: Click `[[full/path/to/note|Note Title]]` to navigate between notes
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
| BFT Consensus | [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]] |
| Safety Properties | [[bft-consensus-analysis/bft-consensus/properties/safety-properties|Safety]] |
| Liveness Properties | [[bft-consensus-analysis/bft-consensus/properties/liveness-properties|Liveness]] |
| PBFT Protocol | [[bft-consensus-analysis/bft-consensus/protocols/pbft|PBFT]] |
| HoneyBadgerBFT | [[bft-consensus-analysis/bft-consensus/protocols/honeybadger-bft|HoneyBadgerBFT]] |
| HotStuff | [[bft-consensus-analysis/bft-consensus/protocols/hotstuff|HotStuff]] |
| Provable Broadcast | [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]] |
| Reliable Broadcast | [[bft-consensus-analysis/provable-broadcast/reliable-broadcast|Reliable Broadcast]] |
| Knowledge Framework | [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]] |
| Temporal Logic | [[bft-consensus-analysis/logic-models/temporal-logic|Expressing Safety & Liveness]] |
| Formal Verification | [[bft-consensus-analysis/logic-models/formal-verification|Formal Verification Techniques]] |
| Integration | [[bft-consensus-analysis/integration/relationships|Three-Way Connections]] |

### By Question

| Question | Navigate To |
|----------|-------------|
| What is Byzantine fault tolerance? | [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]] |
| Why can BFT only tolerate f < n/3 faults? | [[bft-consensus-analysis/bft-consensus/properties/fault-tolerance-threshold|Fault Tolerance Threshold: Why f < n/3 for Byzantine Failures]] |
| How does PBFT work? | [[bft-consensus-analysis/bft-consensus/protocols/pbft|PBFT]] |
| What's the difference between PBFT and HotStuff? | [[bft-consensus-analysis/bft-consensus/protocols/protocol-comparison|Protocol Comparison]] |
| What is provable broadcast? | [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]] |
| How is it different from reliable broadcast? | [[bft-consensus-analysis/provable-broadcast/vs-reliable-broadcast|Provable vs Reliable Broadcast]] |
| Where is provable broadcast used? | [[bft-consensus-analysis/provable-broadcast/applications|Real-World Usage in Blockchain & DLT]] |
| How do I formally verify a consensus protocol? | [[bft-consensus-analysis/logic-models/formal-verification|Formal Verification Techniques]] |
| What is common knowledge in distributed systems? | [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]] |
| How do BFT, broadcast, and logic models relate? | [[bft-consensus-analysis/integration/relationships|Three-Way Connections]] |
| Can I see a complete analysis of a real protocol? | [[bft-consensus-analysis/integration/case-studies/honeybadger-complete|HoneyBadgerBFT Complete Analysis]] |

### By Difficulty Level

Use tags to filter by complexity:

- `#introductory` - Accessible to those new to the topic
- `#intermediate` - Requires some background knowledge
- `#advanced` - Deep technical or mathematical content

**Search in Obsidian**: Use `tag:#introductory` in search bar

---

## Key Concepts & Terminology

Before diving in, familiarize yourself with these essential terms (see [[bft-consensus-analysis/glossary|Glossary]] for full definitions):

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

See [[bft-consensus-analysis/references|References]] for the complete bibliography with links.

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

1. **Choose the right location**: See [[contracts/directory-structure|contracts/directory-structure]]
2. **Use the note schema**: See [[contracts/note-schema|contracts/note-schema]]
3. **Follow naming conventions**: Use kebab-case (e.g., `new-protocol.md`)
4. **Add YAML frontmatter**: Include required fields (title, type, tags, dates, status)
5. **Link generously**: Connect to related notes using wikilinks
6. **Update central files**: Add entries to `glossary.md`, `references.md` as needed
7. **Update comparisons**: If adding a protocol, update `protocol-comparison.md`

### Quality Standards

- **Cite sources**: Use [[bft-consensus-analysis/references|References]] for all technical claims
- **Provide examples**: Include concrete instances, not just abstractions
- **Use diagrams**: Mermaid diagrams for sequences, flows, structures
- **Be accessible**: Start with intuition before formal definitions
- **Link prerequisites**: Help readers follow learning paths

---

## Getting Help

### Within the Knowledge Base

- **Glossary**: [[bft-consensus-analysis/glossary|Glossary]] - Definitions of technical terms
- **References**: [[bft-consensus-analysis/references|References]] - Full citations and external links
- **Index**: [[index|Welcome to Quartz AB]] - Overview and main navigation

### Common Issues

| Problem | Solution |
|---------|----------|
| "This note assumes knowledge I don't have" | Check the `Prerequisites` section for suggested reading order |
| "I don't understand the formal notation" | See [[bft-consensus-analysis/glossary|Glossary]] for notation explanations; start with accessible notes tagged `#introductory` |
| "Wikilink doesn't resolve" | The note may not exist yet; check [[index|Welcome to Quartz AB]] for available content |
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

- **Beginner**: Start with [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]]
- **Practitioner**: Jump to [[bft-consensus-analysis/bft-consensus/protocols/protocol-comparison|Protocol Comparison]]
- **Researcher**: Explore [[bft-consensus-analysis/logic-models/overview|Logic Models Overview]]
- **Curious**: Browse [[index|Welcome to Quartz AB]] and follow what interests you

---

## Version Information

- **Knowledge Base Version**: 1.0
- **Last Updated**: 2026-01-21
- **Content Status**: Planning phase complete, implementation in progress

---

## See Also

- [[index|Welcome to Quartz AB]] - Main navigation hub
- [[bft-consensus-analysis/glossary|Glossary]] - Technical terminology
- [[bft-consensus-analysis/references|References]] - Bibliography
- [[contracts/note-schema|contracts/note-schema]] - Metadata standards
- [[contracts/directory-structure|contracts/directory-structure]] - File organization

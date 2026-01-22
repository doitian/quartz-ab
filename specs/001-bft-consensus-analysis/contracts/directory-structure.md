# Directory Structure Contract

**Feature**: 001-bft-consensus-analysis  
**Purpose**: Define the file organization and naming conventions for the BFT Consensus Analysis knowledge base

---

## Root Structure

```
content/bft-consensus-analysis/
├── index.md                          # Entry point and navigation hub
├── glossary.md                       # Technical terms across all domains
├── references.md                     # Central bibliography
│
├── bft-consensus/                    # BFT Consensus domain
│   ├── fundamentals.md
│   ├── byzantine-failures.md
│   ├── properties/
│   │   ├── safety-properties.md
│   │   ├── liveness-properties.md
│   │   └── fault-tolerance-threshold.md
│   └── protocols/
│       ├── pbft.md
│       ├── honeybadger-bft.md
│       ├── hotstuff.md
│       └── protocol-comparison.md
│
├── provable-broadcast/               # Provable Broadcast domain
│   ├── overview.md
│   ├── properties.md
│   ├── reliable-broadcast.md
│   ├── byzantine-reliable-broadcast.md
│   ├── provable-broadcast.md
│   ├── vs-reliable-broadcast.md
│   └── applications.md
│
├── logic-models/                     # Logic Models domain
│   ├── overview.md
│   ├── knowledge-framework.md
│   ├── temporal-logic.md
│   ├── threshold-automata.md
│   ├── formal-verification.md
│   └── proof-techniques.md
│
└── integration/                      # Integration & Synthesis
    ├── relationships.md
    ├── case-studies/
    │   ├── honeybadger-complete.md
    │   └── dag-rider-analysis.md
    └── design-framework.md
```

---

## Naming Conventions

### File Names

- **Use kebab-case**: `byzantine-failures.md`, `provable-broadcast.md`
- **Be descriptive**: File name should indicate content clearly
- **Avoid abbreviations**: Spell out terms (except well-known acronyms like BFT, PBFT)
- **Suffix**: All files end in `.md` (Markdown)

**Examples:**
- ✅ `honeybadger-bft.md` (clear, descriptive)
- ✅ `vs-reliable-broadcast.md` (comparison indicated by "vs")
- ❌ `hb.md` (too abbreviated)
- ❌ `comparison.md` (not specific enough)

### Directory Names

- **Use kebab-case**: `bft-consensus`, `provable-broadcast`, `logic-models`
- **Plural for collections**: `protocols/`, `properties/`, `case-studies/`
- **Singular for single topics**: `integration/` (conceptual area, not a collection)

---

## Content Organization Principles

### 1. Conceptual Hierarchy

```
General → Specific
Domain → Sub-domain → Individual Topics
```

**Example:**
```
bft-consensus/ (domain)
  ├── fundamentals.md (general concepts)
  └── protocols/ (sub-domain)
      └── pbft.md (specific instance)
```

### 2. Separation of Concerns

Each directory represents a distinct conceptual area:

- **`bft-consensus/`**: Protocols and properties
- **`provable-broadcast/`**: Communication primitives
- **`logic-models/`**: Formal frameworks and verification
- **`integration/`**: Cross-domain synthesis

**Rule**: A note belongs in ONE primary location. Use wikilinks for cross-references.

### 3. Entry Points

Key navigation hubs:

- **`index.md`**: Global entry point, links to all major areas
- **`bft-consensus/fundamentals.md`**: Entry to BFT domain
- **`provable-broadcast/overview.md`**: Entry to broadcast domain
- **`logic-models/overview.md`**: Entry to logic models domain
- **`integration/relationships.md`**: Entry to synthesis

Each domain should have a clear "start here" note.

---

## Mandatory Files

These files MUST exist in the knowledge base:

### Root Level

1. **`index.md`**
   - Overall introduction
   - Links to all major sections
   - Quick-start guide
   - Visual map of the knowledge base

2. **`glossary.md`**
   - Alphabetical list of technical terms
   - Brief definitions with links to detailed notes
   - Format: `**Term**: Definition. See [[detailed-note]]`

3. **`references.md`**
   - Bibliographic entries for all cited sources
   - Standard format (author, year, title, publication/URL)
   - Assigned keys for citation (e.g., `halpern-moses-2000`)

### BFT Consensus Domain

4. **`bft-consensus/fundamentals.md`**
   - Core concepts: consensus, Byzantine failures, safety, liveness
   - Foundation for understanding protocols

5. **`bft-consensus/byzantine-failures.md`**
   - Failure models: crash vs. Byzantine
   - Attack vectors and tolerance bounds

6. At least **3 protocol notes** (per spec requirements):
   - `protocols/pbft.md`
   - `protocols/honeybadger-bft.md`
   - `protocols/hotstuff.md`

7. **`protocols/protocol-comparison.md`**
   - Side-by-side comparison of protocols
   - Trade-offs and use cases

### Provable Broadcast Domain

8. **`provable-broadcast/overview.md`**
   - Introduction to broadcast primitives
   - Evolution from reliable → provable

9. **`provable-broadcast/properties.md`**
   - Validity, agreement, integrity, provability
   - Formal definitions

10. **`provable-broadcast/vs-reliable-broadcast.md`**
    - Explicit comparison per spec requirement (FR-004)

11. **`provable-broadcast/applications.md`**
    - Modern uses in blockchain/DLT (FR-005)

### Logic Models Domain

12. **`logic-models/overview.md`**
    - Introduction to formal methods for consensus

13. **`logic-models/knowledge-framework.md`**
    - Halpern-Moses framework (FR-006)
    - Knowledge, distributed knowledge, common knowledge

14. **`logic-models/temporal-logic.md`**
    - LTL and temporal operators
    - Expressing safety and liveness

15. **`logic-models/formal-verification.md`**
    - How to verify BFT protocols (FR-009)

### Integration Domain

16. **`integration/relationships.md`**
    - Three-way connections (FR-008)
    - BFT ↔ Broadcast, BFT ↔ Logic, Broadcast ↔ Logic

17. At least **2 case study notes** (per spec requirement FR-010):
    - `case-studies/honeybadger-complete.md`
    - `case-studies/dag-rider-analysis.md`

---

## Optional But Recommended Files

- **`bft-consensus/properties/safety-properties.md`**: Deep dive into safety
- **`bft-consensus/properties/liveness-properties.md`**: Deep dive into liveness
- **`logic-models/threshold-automata.md`**: Specific verification technique
- **`integration/design-framework.md`**: Practical guide for protocol designers

---

## File Size Guidelines

- **Target**: 500-2000 words per note (approximately)
- **Maximum**: 3000 words (beyond this, consider splitting)
- **Minimum**: 300 words (shorter notes should be merged or expanded)

**Rationale:**
- Obsidian works best with focused, linkable notes
- Prevents "wall of text" that's hard to navigate
- Encourages modular, reusable content

**Exception:** `protocol-comparison.md` and case studies may exceed 3000 words due to their comprehensive nature.

---

## Cross-Referencing Strategy

### Wikilinks

Every note should:
- Link to **prerequisite concepts** early in the note
- Link to **related topics** in a "See Also" section
- Link to **glossary terms** on first use
- Link to **detailed notes** from overview notes

### Backlinks

Obsidian automatically creates backlinks. Ensure:
- Important notes are referenced from multiple places
- Orphan notes (no inbound links) are minimized
- The graph view shows clear clusters around main topics

---

## Asset Management

### Diagrams

- **Prefer Mermaid** (text-based, version-control friendly)
- Embed directly in notes using code blocks
- No separate `diagrams/` directory needed

### Images (if needed)

If external images are required:

```
content/bft-consensus-analysis/assets/
├── diagrams/
│   └── external-diagram.png
└── figures/
    └── external-figure.svg
```

Reference with: `![Description](assets/diagrams/external-diagram.png)`

**Note:** Minimize external images; Mermaid is preferred.

---

## Navigation Helpers

### Tags-Based Navigation

Notes are also navigable by tags (defined in YAML frontmatter):

- **By domain**: `#bft`, `#broadcast`, `#logic-model`
- **By property**: `#safety`, `#liveness`
- **By level**: `#introductory`, `#intermediate`, `#advanced`
- **By protocol**: `#pbft`, `#honeybadger`, `#hotstuff`

### Folder-Based Navigation

Users browsing the file explorer see logical groupings:

```
bft-consensus/        → "I want to learn about BFT protocols"
provable-broadcast/   → "I want to understand broadcast mechanisms"
logic-models/         → "I want to learn formal verification"
integration/          → "I want to see how these areas connect"
```

---

## Versioning & Updates

### Adding New Protocols

New protocol notes go in `bft-consensus/protocols/`:

```
protocols/new-protocol.md
```

Update `protocols/protocol-comparison.md` to include the new protocol.

### Adding New Case Studies

New case studies go in `integration/case-studies/`:

```
integration/case-studies/new-case-study.md
```

Update `integration/relationships.md` to reference the new case study.

### Refactoring

If a note becomes too large:
1. Create a subdirectory with the note's name
2. Split content into focused sub-notes
3. Convert original note to an overview with links

**Example:**
```
# Before
provable-broadcast.md (4000 words, too long)

# After
provable-broadcast/
├── overview.md (500 words, links to sub-notes)
├── properties.md
├── mechanisms.md
└── applications.md
```

---

## Quality Gates

Before merging content:

- ✅ All mandatory files exist
- ✅ No orphan notes (every note is linked from at least one other note)
- ✅ Directory structure matches this contract
- ✅ File naming conventions followed
- ✅ Each note has proper YAML frontmatter (per `note-schema.md`)
- ✅ Glossary and references are populated
- ✅ `index.md` provides clear navigation

---

## Migration Path

If restructuring becomes necessary:

1. **Document the change** in this contract
2. **Create redirects** (use Obsidian aliases in YAML frontmatter):
   ```yaml
   aliases: [old-note-name, another-alias]
   ```
3. **Update all wikilinks** to new paths
4. **Test navigation** (ensure no broken links)

---

## Examples

### Example: Adding a New Protocol Note

1. Create file: `bft-consensus/protocols/tendermint.md`
2. Add YAML frontmatter (per `note-schema.md`):
   ```yaml
   ---
   title: "Tendermint"
   type: protocol
   tags: [bft, consensus, tendermint, partial-synchrony]
   created: 2026-01-22
   updated: 2026-01-22
   status: draft
   synchrony_model: partially-synchronous
   fault_tolerance: "f < n/3"
   year_introduced: 2014
   related:
     - [[hotstuff]]
     - [[pbft]]
   references:
     - buchman-2016-tendermint
   ---
   ```
3. Write content following body structure standards
4. Update `protocols/protocol-comparison.md` to include Tendermint
5. Add entry to `glossary.md` if needed
6. Add citation to `references.md`

### Example: Linking Between Notes

In `bft-consensus/fundamentals.md`:
```markdown
Byzantine failures are discussed in detail in [[byzantine-failures]].

For specific protocols, see:
- [[pbft]]
- [[honeybadger-bft]]
- [[hotstuff]]
```

In `provable-broadcast/applications.md`:
```markdown
Provable broadcast is a key building block in [[honeybadger-bft]]
and other modern [[bft-consensus-fundamentals|BFT consensus protocols]].
```

---

## Version History

- **v1.0 (2026-01-21)**: Initial directory structure contract

---

## See Also

- [[note-schema]] - YAML frontmatter and metadata standards
- [[data-model]] - Conceptual knowledge domain model
- [[quickstart]] - User navigation guide

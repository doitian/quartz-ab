# Data Model: BFT Consensus Analysis Knowledge Base

**Feature**: 001-bft-consensus-analysis  
**Phase**: 1 - Design & Contracts  
**Date**: 2026-01-21

## Overview

This document defines the conceptual data model for the BFT Consensus Analysis knowledge base. Since this is a documentation system (not a software application), the "data model" represents the **knowledge domain structure** - the entities, their attributes, and relationships that organize our understanding of BFT consensus, provable broadcast, and logic models.

---

## Entity Definitions

### 1. BFT Consensus Protocol

**Description:** A consensus protocol designed to tolerate Byzantine (arbitrary/malicious) failures.

**Attributes:**
- `name` (string): Protocol identifier (e.g., "PBFT", "HoneyBadgerBFT", "HotStuff")
- `synchrony_model` (enum): `synchronous` | `partially_synchronous` | `asynchronous`
- `fault_tolerance` (string): Mathematical expression of tolerable faults (typically "f < n/3")
- `communication_complexity` (string): Big-O notation for message complexity (e.g., "O(n²)", "O(n)")
- `safety_property` (string): Formal statement of safety guarantee
- `liveness_property` (string): Formal statement of liveness guarantee
- `year_introduced` (integer): Publication year
- `key_innovation` (string): Main contribution or distinguishing feature

**Relationships:**
- `uses` → Broadcast Mechanism (which broadcast primitive the protocol employs)
- `verified_by` → Formal Verification Result (proofs of correctness)
- `compared_with` → Other BFT Consensus Protocols (trade-off analysis)

**Validation Rules:**
- `fault_tolerance` must be mathematically consistent with `synchrony_model`
- Safety and liveness properties should be expressed in formal logic notation (where applicable)

**Example Instance:**
```yaml
name: HoneyBadgerBFT
synchrony_model: asynchronous
fault_tolerance: f < n/3 Byzantine faults
communication_complexity: O(n² × |input|) with batching
safety_property: "Agreement: All honest nodes output the same set of values"
liveness_property: "Termination: All honest nodes eventually output (no timing assumptions)"
year_introduced: 2016
key_innovation: "First fully asynchronous BFT with guaranteed liveness"
```

---

### 2. Broadcast Mechanism

**Description:** A communication primitive for distributing messages in a distributed system.

**Attributes:**
- `name` (string): Mechanism identifier (e.g., "Reliable Broadcast", "Provable Broadcast", "Byzantine Reliable Broadcast")
- `type` (enum): `reliable` | `provable` | `atomic` | `byzantine_reliable`
- `properties` (list): Properties guaranteed (e.g., ["validity", "agreement", "integrity", "provability"])
- `certificate_type` (string?): Type of delivery proof if applicable (e.g., "quorum certificate", "threshold signature")
- `cryptographic_primitive` (string?): Underlying crypto (e.g., "threshold encryption", "digital signatures")
- `message_complexity` (string): Number of messages exchanged

**Relationships:**
- `extends` → Simpler Broadcast Mechanism (e.g., provable extends reliable)
- `used_in` → BFT Consensus Protocol
- `formally_specified_by` → Logic Model Specification

**Validation Rules:**
- If `type` is `provable`, `certificate_type` must be specified
- `properties` must include at least "validity" and "agreement"

**Example Instance:**
```yaml
name: Provable Broadcast
type: provable
properties: [validity, agreement, integrity, provability]
certificate_type: quorum certificate (n - 2f signatures)
cryptographic_primitive: digital signatures or threshold signatures
message_complexity: O(n²) messages
```

---

### 3. Byzantine Failure Model

**Description:** Characterization of how nodes can fail maliciously in the system.

**Attributes:**
- `failure_type` (enum): `crash` | `omission` | `byzantine_arbitrary`
- `max_faulty_nodes` (string): Mathematical bound (e.g., "f < n/3", "f < n/2")
- `attack_vectors` (list): Types of malicious behavior (e.g., ["equivocation", "message suppression", "value alteration"])
- `detection_mechanism` (string?): How failures are detected or tolerated

**Relationships:**
- `tolerated_by` → BFT Consensus Protocol
- `requires` → Cryptographic Mechanism (to prevent certain attacks)

**Example Instance:**
```yaml
failure_type: byzantine_arbitrary
max_faulty_nodes: f < n/3
attack_vectors: [equivocation, message suppression, value alteration, timing attacks]
detection_mechanism: "Quorum-based verification via certificates"
```

---

### 4. Consensus Property

**Description:** A correctness requirement that consensus protocols must satisfy.

**Attributes:**
- `name` (string): Property identifier (e.g., "Safety", "Liveness", "Agreement", "Validity", "Termination")
- `category` (enum): `safety` | `liveness`
- `informal_description` (string): Plain language explanation
- `formal_specification` (string): Temporal logic or mathematical formulation
- `verification_method` (string): How the property is proven (e.g., "model checking", "manual proof", "theorem prover")

**Relationships:**
- `satisfied_by` → BFT Consensus Protocol
- `expressed_in` → Logic Model Framework

**Validation Rules:**
- Safety properties must be of the form "something bad never happens"
- Liveness properties must be of the form "something good eventually happens"

**Example Instance:**
```yaml
name: Agreement
category: safety
informal_description: "No two honest nodes decide on different values"
formal_specification: "∀i,j ∈ Correct : decided(i) ∧ decided(j) → value(i) = value(j)"
verification_method: "Model checking with threshold automata"
```

---

### 5. Logic Model Framework

**Description:** A formal mathematical system for reasoning about distributed consensus.

**Attributes:**
- `name` (string): Framework identifier (e.g., "Halpern-Moses Knowledge Logic", "Temporal Logic (LTL)", "Threshold Automata")
- `logic_type` (enum): `epistemic` | `temporal` | `modal` | `automata_based`
- `key_operators` (list): Logical operators or constructs (e.g., ["K (knows)", "C (common knowledge)", "◇ (eventually)", "□ (always)"])
- `expressiveness` (string): What can be specified (e.g., "knowledge states", "temporal properties")
- `tool_support` (string?): Automated tools (e.g., "ByMC", "TLA+", "Coq")

**Relationships:**
- `used_to_verify` → BFT Consensus Protocol
- `expresses` → Consensus Property
- `based_on_paper` → Reference (research paper)

**Example Instance:**
```yaml
name: Linear Temporal Logic (LTL)
logic_type: temporal
key_operators: ["◇ (eventually)", "□ (always)", "○ (next)", "U (until)"]
expressiveness: "Temporal properties over infinite execution traces"
tool_support: "Model checkers (SPIN, NuSMV), TLA+"
```

---

### 6. Protocol Case Study

**Description:** An integrated analysis of a real-world protocol showing BFT, broadcast, and logic model perspectives.

**Attributes:**
- `protocol_name` (string): Name of the analyzed protocol
- `application_domain` (string): Where it's used (e.g., "permissionless blockchain", "permissioned ledger", "critical infrastructure")
- `bft_properties` (object): Safety/liveness analysis
- `broadcast_mechanism` (string): Which broadcast primitive is used
- `formal_verification_status` (enum): `fully_verified` | `partially_verified` | `unverified`
- `performance_characteristics` (object): Throughput, latency, scalability

**Relationships:**
- `analyzes` → BFT Consensus Protocol
- `demonstrates` → Broadcast Mechanism usage
- `verified_using` → Logic Model Framework

**Example Instance:**
```yaml
protocol_name: HoneyBadgerBFT
application_domain: permissionless blockchain (cryptocurrency)
bft_properties:
  safety: "Agreement and validity with f < n/3 Byzantine nodes"
  liveness: "Guaranteed termination in asynchronous network"
broadcast_mechanism: "Threshold-encrypted provable broadcast"
formal_verification_status: partially_verified
performance_characteristics:
  throughput: "10-50k transactions/sec (batched)"
  latency: "seconds (varies with network asynchrony)"
  scalability: "Tested up to 100 nodes"
```

---

### 7. Knowledge Entity (from Logic Model)

**Description:** Represents different levels of knowledge in a distributed system (from Halpern-Moses framework).

**Attributes:**
- `level` (enum): `local` | `distributed` | `common`
- `definition` (string): Formal definition of the knowledge level
- `achievability` (enum): `always_achievable` | `conditionally_achievable` | `impossible_in_practice`
- `role_in_consensus` (string): Why this knowledge level matters for consensus

**Relationships:**
- `required_for` → Consensus Property
- `modeled_by` → Logic Model Framework

**Example Instance:**
```yaml
level: common
definition: "Everyone knows X, everyone knows that everyone knows X, recursively to infinite depth"
achievability: impossible_in_practice
role_in_consensus: "True common knowledge cannot be achieved in asynchronous systems with failures; consensus protocols approximate it"
```

---

## Relationships Summary

### Entity Relationship Diagram (Textual)

```
BFT Consensus Protocol
  ├── uses → Broadcast Mechanism
  ├── tolerates → Byzantine Failure Model
  ├── satisfies → Consensus Property (Safety)
  ├── satisfies → Consensus Property (Liveness)
  └── verified_by → Logic Model Framework

Broadcast Mechanism
  ├── extends → Simpler Broadcast Mechanism
  ├── used_in → BFT Consensus Protocol
  └── formally_specified_by → Logic Model Framework

Consensus Property
  ├── satisfied_by → BFT Consensus Protocol
  └── expressed_in → Logic Model Framework

Logic Model Framework
  ├── expresses → Consensus Property
  ├── verifies → BFT Consensus Protocol
  └── models → Knowledge Entity

Protocol Case Study
  ├── analyzes → BFT Consensus Protocol
  ├── demonstrates → Broadcast Mechanism
  └── verified_using → Logic Model Framework

Knowledge Entity
  ├── required_for → Consensus Property
  └── modeled_by → Logic Model Framework
```

---

## State Transitions

### Consensus Protocol Execution States

While individual protocols have unique state machines, the general consensus progression follows:

```
[Initial State]
    ↓
[Proposal Phase] ← leader proposes value using broadcast
    ↓
[Echo/Voting Phase] ← nodes exchange messages (may use provable broadcast)
    ↓
[Certificate Formation] ← quorum is reached, delivery certificate created
    ↓
[Commit/Decision Phase] ← nodes commit to value
    ↓
[Decided State] ← consensus achieved
```

**Safety Invariant:** Once in Decided state, the value cannot change  
**Liveness Requirement:** Eventually reach Decided state (under model assumptions)

---

## Knowledge Base Navigation Model

### How Users Navigate Through Entities

```
Entry Point: index.md
    ├── Fundamentals Path
    │   ├── BFT Consensus Fundamentals
    │   ├── Byzantine Failure Models
    │   └── Consensus Properties (Safety/Liveness)
    │
    ├── Protocols Path
    │   ├── PBFT
    │   ├── HoneyBadgerBFT
    │   └── HotStuff
    │
    ├── Broadcast Path
    │   ├── Reliable Broadcast
    │   ├── Byzantine Reliable Broadcast
    │   └── Provable Broadcast
    │
    ├── Logic Models Path
    │   ├── Knowledge Framework (Halpern-Moses)
    │   ├── Temporal Logic (LTL)
    │   └── Formal Verification Techniques
    │
    └── Integration Path
        ├── Relationships Between Areas
        ├── Case Study: HoneyBadgerBFT
        └── Case Study: DAG-Based BFT
```

---

## Metadata Schema (YAML Frontmatter)

Every Obsidian note will follow this metadata structure:

```yaml
---
title: "Human-Readable Title"
type: concept | protocol | mechanism | framework | case-study
tags: [bft, consensus, broadcast, logic-model, <specific-tags>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: draft | review | complete
related:
  - [[related-note-1]]
  - [[related-note-2]]
references:
  - source-key-1
  - source-key-2
---
```

**Field Definitions:**
- `type`: Category of knowledge (helps with filtering and organization)
- `tags`: Searchable keywords (use consistent tag vocabulary)
- `status`: Editorial status (enables incremental development)
- `related`: Explicit cross-references to related notes (in addition to inline wikilinks)
- `references`: Keys to entries in the central references.md file

---

## Validation & Quality Rules

### Completeness Criteria

Each entity instance (Obsidian note) must:
1. **Have all required attributes** from its entity definition
2. **Cite authoritative sources** for all technical claims
3. **Link to related entities** using Obsidian wikilinks
4. **Include examples** where applicable (concrete before abstract)
5. **Provide visual aids** (diagrams, tables) for complex concepts

### Consistency Checks

- **Bidirectional Links:** If Note A links to Note B, Note B should link back (or list A in `related`)
- **Tag Consistency:** Use standardized tags from defined vocabulary
- **Citation Completeness:** All `references` keys must exist in `references.md`
- **Formal Notation:** Mathematical/logical notation should be consistent across notes

### Accessibility Standards

- **Prerequisites Stated:** Each note lists assumed background knowledge
- **Progressive Complexity:** Start with intuitive explanations before formal definitions
- **Glossary Integration:** Link technical terms to `glossary.md` on first use
- **Multiple Perspectives:** Provide both theoretical rigor and practical intuition

---

## Implementation Notes

### Note Creation Order

To ensure dependencies are satisfied:

1. **Foundation Notes** (no dependencies):
   - `glossary.md`
   - `references.md`
   - Byzantine Failure Models
   - Basic Consensus Properties

2. **Core Concept Notes** (depend on foundation):
   - BFT Consensus Fundamentals
   - Reliable/Byzantine Reliable Broadcast
   - Knowledge Framework Basics

3. **Advanced Concept Notes** (depend on core):
   - Provable Broadcast (depends on reliable broadcast)
   - Temporal Logic (depends on consensus properties)
   - Formal Verification Techniques

4. **Protocol Notes** (depend on core & advanced):
   - PBFT
   - HoneyBadgerBFT
   - HotStuff

5. **Integration Notes** (depend on everything):
   - Relationships Between Areas
   - Case Studies

### Diagram Standards

- Use **Mermaid** for sequence diagrams, flowcharts, state machines
- Use **ASCII tables** for comparisons and property matrices
- Use **LaTeX** (via $...$ or $$...$$) for mathematical notation
- Embed diagrams inline using code blocks (not external images)

---

## Success Criteria

This data model is successful if:

- ✅ All entities map to specific Obsidian notes in the planned structure
- ✅ Relationships are expressible using Obsidian wikilinks and YAML metadata
- ✅ The model supports all user scenarios from the feature spec
- ✅ The structure scales to accommodate future additions (new protocols, mechanisms, verification techniques)
- ✅ Navigation paths exist from entry point to all major concepts

---

## Next Steps

1. Create `contracts/` directory with schema definitions (YAML frontmatter templates)
2. Create `quickstart.md` with navigation guide
3. Begin creating actual Obsidian notes in `content/bft-consensus-analysis/` following this data model

---
title: "Glossary: BFT Consensus, Provable Broadcast, and Logic Models"
type: glossary
tags: [glossary, reference, terminology]
created: 2026-01-21
updated: 2026-01-21
status: draft
---

# Glossary

A comprehensive glossary of technical terms used across BFT consensus, provable broadcast, and logic models domains.

## A

**Agreement**  
A consensus property requiring that all correct (non-faulty) nodes decide on the same value. This is a **safety property**. See [[bft-consensus-analysis/bft-consensus/properties/safety-properties|Safety]].

**Asynchronous Model**  
A system model where there are no bounds on message delays or relative process speeds. Messages can be delayed arbitrarily, but eventually arrive. See [[bft-consensus/fundamentals|bft-consensus/fundamentals#synchrony-models]].

**Atomic Broadcast**  
A broadcast primitive that guarantees both agreement (all correct nodes deliver the same messages) and total order (all correct nodes deliver messages in the same order). Also called Total Order Broadcast. See [[bft-consensus-analysis/provable-broadcast/overview|Provable Broadcast Overview]].

## B

**Byzantine Failure**  
Arbitrary or malicious behavior by a faulty node, including sending inconsistent messages, not responding, or actively trying to disrupt the protocol. Named after the Byzantine Generals Problem. See [[bft-consensus-analysis/bft-consensus/byzantine-failures|Byzantine Failures]].

**Byzantine Fault Tolerance (BFT)**  
The ability of a distributed system to function correctly even when some nodes exhibit Byzantine (arbitrary/malicious) failures. See [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]].

**Byzantine Reliable Broadcast**  
A broadcast primitive that guarantees validity, agreement, and integrity even in the presence of Byzantine failures. See [[bft-consensus-analysis/provable-broadcast/byzantine-reliable-broadcast|Byzantine Reliable Broadcast]].

## C

**Certificate** (Delivery Certificate, Quorum Certificate)  
Cryptographic or quorum-based proof that a message has been delivered by a sufficient number of nodes (typically n - 2f in BFT systems). Key component of provable broadcast. See [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]].

**Common Knowledge**  
In distributed systems, a state where everyone knows fact X, everyone knows that everyone knows X, and so on recursively to infinite depth. Cannot be achieved in practice with failures. See [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]].

**Consensus**  
The problem of getting distributed nodes to agree on a single value, even in the presence of failures. Requires agreement, validity, and termination properties. See [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]].

**Crash Failure**  
A failure mode where a node stops functioning (crashes) but does not send incorrect or malicious messages before stopping. Less severe than Byzantine failure. See [[bft-consensus-analysis/bft-consensus/byzantine-failures|Byzantine Failures]].

## D

**Delivery Certificate**  
See **Certificate**.

**Distributed Knowledge**  
Knowledge that exists collectively across all nodes in a system but may not be known to any individual node. See [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]].

## E

**Echo Broadcast**  
Another name for **Provable Broadcast**, emphasizing the "echo" phase where nodes re-broadcast received messages. See [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]].

**Equivocation**  
When a Byzantine sender sends different values to different recipients, trying to cause disagreement. Provable broadcast prevents this. See [[provable-broadcast/provable-broadcast|provable-broadcast/provable-broadcast#preventing-equivocation]].

**Eventual Consistency**  
A liveness property where the system eventually reaches a consistent state, though there may be temporary inconsistencies. Common in asynchronous systems. See [[bft-consensus-analysis/bft-consensus/properties/liveness-properties|Liveness]].

## F

**Fault Tolerance Threshold**  
The maximum number of faulty nodes a system can tolerate while maintaining correctness. For BFT consensus, typically f < n/3. See [[bft-consensus-analysis/bft-consensus/properties/fault-tolerance-threshold|Fault Tolerance Threshold: Why f < n/3 for Byzantine Failures]].

**FLP Impossibility**  
Fisher, Lynch, and Paterson's result showing that deterministic consensus is impossible in an asynchronous system with even one faulty process. See [[bft-consensus-analysis/logic-models/overview|Logic Models for Distributed Systems#impossibility-results]].

## H

**HoneyBadgerBFT**  
A fully asynchronous BFT consensus protocol with guaranteed liveness, using threshold encryption and provable broadcast. See [[bft-consensus-analysis/bft-consensus/protocols/honeybadger-bft|HoneyBadgerBFT]].

**HotStuff**  
A partially synchronous BFT protocol with linear communication complexity (O(n)), using a three-phase commit and leader rotation. See [[bft-consensus-analysis/bft-consensus/protocols/hotstuff|HotStuff]].

## I

**Integrity**  
A broadcast property requiring that a message is only delivered if it was actually sent by the claimed sender. See [[bft-consensus-analysis/provable-broadcast/properties|Provable Broadcast Properties]].

## K

**Knowledge (in Logic Models)**  
What an agent knows based on its local observations and messages received. Formalized using modal logic operators. See [[bft-consensus-analysis/logic-models/knowledge-framework|Halpern-Moses Knowledge Framework]].

## L

**Leader**  
A distinguished node responsible for proposing values in many consensus protocols (e.g., PBFT, HotStuff). May rotate among nodes. See [[bft-consensus/protocols/pbft|bft-consensus/protocols/pbft#leader-based-consensus]].

**Linear Temporal Logic (LTL)**  
A formal logic for expressing properties over infinite execution traces, using operators like ◇ (eventually) and □ (always). See [[bft-consensus-analysis/logic-models/temporal-logic|Expressing Safety & Liveness]].

**Liveness**  
A property stating that "something good eventually happens." For consensus, typically means a decision is eventually reached. See [[bft-consensus-analysis/bft-consensus/properties/liveness-properties|Liveness]].

## M

**Model Checking**  
Automated verification technique that exhaustively explores a system's state space to verify properties. See [[logic-models/formal-verification|logic-models/formal-verification#model-checking]].

## N

**n (Total Nodes)**  
The total number of nodes in the system. In BFT literature, typically n = 3f + 1 to tolerate f Byzantine faults. See [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]].

**No Duplication**  
A broadcast property ensuring a message is delivered at most once. See [[bft-consensus-analysis/provable-broadcast/properties|Provable Broadcast Properties]].

## O

**Omission Failure**  
A failure where a node fails to send or receive some messages but is otherwise correct. Less severe than Byzantine, more severe than crash. See [[bft-consensus-analysis/bft-consensus/byzantine-failures|Byzantine Failures]].

## P

**Partial Synchrony**  
A system model where message delays are eventually bounded, but the bound is unknown or holds only after some unknown time (Global Stabilization Time). See [[bft-consensus/fundamentals|bft-consensus/fundamentals#synchrony-models]].

**PBFT (Practical Byzantine Fault Tolerance)**  
A classic BFT consensus protocol for partially synchronous systems, introduced by Castro and Liskov in 1999. See [[bft-consensus-analysis/bft-consensus/protocols/pbft|PBFT]].

**Provable Broadcast**  
A broadcast mechanism that produces a delivery certificate proving that a message has been delivered by a supermajority of nodes. See [[bft-consensus-analysis/provable-broadcast/provable-broadcast|Provable Broadcast Mechanisms]].

**Provability**  
The property that a broadcast mechanism produces cryptographic or quorum-based proof of message delivery. Distinguishing feature of provable broadcast. See [[bft-consensus-analysis/provable-broadcast/properties|Provable Broadcast Properties]].

## Q

**Quorum**  
A subset of nodes large enough to ensure that any two quorums intersect in at least one correct node. In BFT, typically n - f nodes form a quorum. See [[bft-consensus/fundamentals|bft-consensus/fundamentals#quorums]].

**Quorum Certificate**  
See **Certificate**.

## R

**Reliable Broadcast**  
A broadcast primitive guaranteeing that if any correct node delivers a message, all correct nodes deliver it. See [[bft-consensus-analysis/provable-broadcast/reliable-broadcast|Reliable Broadcast]].

**Replica**  
A node participating in a consensus protocol. In BFT literature, often used synonymously with "node" or "process." See [[bft-consensus-analysis/bft-consensus/fundamentals|BFT Fundamentals]].

## S

**Safety**  
A property stating that "something bad never happens." For consensus, typically means no two correct nodes decide on different values. See [[bft-consensus-analysis/bft-consensus/properties/safety-properties|Safety]].

**Synchronous Model**  
A system model where there are known bounds on message delays and process execution speeds. Strong assumption but enables simpler protocols. See [[bft-consensus/fundamentals|bft-consensus/fundamentals#synchrony-models]].

## T

**Temporal Logic**  
A formal logic for reasoning about properties over time, using operators for "eventually," "always," "next," etc. See [[bft-consensus-analysis/logic-models/temporal-logic|Expressing Safety & Liveness]].

**Termination**  
A consensus property (liveness) requiring that all correct nodes eventually decide on a value. See [[bft-consensus-analysis/bft-consensus/properties/liveness-properties|Liveness]].

**Threshold Automata**  
A formal model for representing distributed protocols, enabling automated verification of safety and liveness. See [[bft-consensus-analysis/logic-models/threshold-automata|Threshold Automata]].

**Threshold Encryption/Signature**  
Cryptographic primitives requiring cooperation of f+1 nodes to decrypt/sign, used in protocols like HoneyBadgerBFT. See [[bft-consensus/protocols/honeybadger-bft|bft-consensus/protocols/honeybadger-bft#threshold-cryptography]].

**Total Order Broadcast**  
See **Atomic Broadcast**.

## V

**Validity**  
A consensus property requiring that if all correct nodes propose the same value, that value must be decided. Also a broadcast property. See [[bft-consensus-analysis/bft-consensus/properties/safety-properties|Safety]] and [[bft-consensus-analysis/provable-broadcast/properties|Provable Broadcast Properties]].

**View**  
In protocols like PBFT, a configuration with a designated leader. View changes occur when the leader is suspected to be faulty. See [[bft-consensus/protocols/pbft|bft-consensus/protocols/pbft#view-changes]].

## W

**Wikilink**  
Obsidian's `[[full/path/to/note|Note Title]]` syntax for linking between notes. See [[bft-consensus-analysis/quickstart|Quickstart Guide: BFT Consensus Analysis Knowledge Base#using-the-knowledge-base]].

---

## See Also

- [[bft-consensus-analysis/references|References]] - Bibliography and external sources
- [[index|Welcome to Quartz AB]] - Knowledge base entry point
- [[bft-consensus-analysis/quickstart|Quickstart]] - Navigation guide

## Contributing to This Glossary

When adding terms:
- Use **bold** for the term being defined
- Provide concise definition (1-3 sentences)
- Link to detailed notes using wikilinks
- Alphabetize entries
- Include cross-references where helpful (See **Other Term**)

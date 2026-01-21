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
A consensus property requiring that all correct (non-faulty) nodes decide on the same value. This is a **safety property**. See [[bft-consensus/properties/safety-properties]].

**Asynchronous Model**  
A system model where there are no bounds on message delays or relative process speeds. Messages can be delayed arbitrarily, but eventually arrive. See [[bft-consensus/fundamentals#synchrony-models]].

**Atomic Broadcast**  
A broadcast primitive that guarantees both agreement (all correct nodes deliver the same messages) and total order (all correct nodes deliver messages in the same order). Also called Total Order Broadcast. See [[provable-broadcast/overview]].

## B

**Byzantine Failure**  
Arbitrary or malicious behavior by a faulty node, including sending inconsistent messages, not responding, or actively trying to disrupt the protocol. Named after the Byzantine Generals Problem. See [[bft-consensus/byzantine-failures]].

**Byzantine Fault Tolerance (BFT)**  
The ability of a distributed system to function correctly even when some nodes exhibit Byzantine (arbitrary/malicious) failures. See [[bft-consensus/fundamentals]].

**Byzantine Reliable Broadcast**  
A broadcast primitive that guarantees validity, agreement, and integrity even in the presence of Byzantine failures. See [[provable-broadcast/byzantine-reliable-broadcast]].

## C

**Certificate** (Delivery Certificate, Quorum Certificate)  
Cryptographic or quorum-based proof that a message has been delivered by a sufficient number of nodes (typically n - 2f in BFT systems). Key component of provable broadcast. See [[provable-broadcast/provable-broadcast]].

**Common Knowledge**  
In distributed systems, a state where everyone knows fact X, everyone knows that everyone knows X, and so on recursively to infinite depth. Cannot be achieved in practice with failures. See [[logic-models/knowledge-framework]].

**Consensus**  
The problem of getting distributed nodes to agree on a single value, even in the presence of failures. Requires agreement, validity, and termination properties. See [[bft-consensus/fundamentals]].

**Crash Failure**  
A failure mode where a node stops functioning (crashes) but does not send incorrect or malicious messages before stopping. Less severe than Byzantine failure. See [[bft-consensus/byzantine-failures]].

## D

**Delivery Certificate**  
See **Certificate**.

**Distributed Knowledge**  
Knowledge that exists collectively across all nodes in a system but may not be known to any individual node. See [[logic-models/knowledge-framework]].

## E

**Echo Broadcast**  
Another name for **Provable Broadcast**, emphasizing the "echo" phase where nodes re-broadcast received messages. See [[provable-broadcast/provable-broadcast]].

**Equivocation**  
When a Byzantine sender sends different values to different recipients, trying to cause disagreement. Provable broadcast prevents this. See [[provable-broadcast/provable-broadcast#preventing-equivocation]].

**Eventual Consistency**  
A liveness property where the system eventually reaches a consistent state, though there may be temporary inconsistencies. Common in asynchronous systems. See [[bft-consensus/properties/liveness-properties]].

## F

**Fault Tolerance Threshold**  
The maximum number of faulty nodes a system can tolerate while maintaining correctness. For BFT consensus, typically f < n/3. See [[bft-consensus/properties/fault-tolerance-threshold]].

**FLP Impossibility**  
Fisher, Lynch, and Paterson's result showing that deterministic consensus is impossible in an asynchronous system with even one faulty process. See [[logic-models/overview#impossibility-results]].

## H

**HoneyBadgerBFT**  
A fully asynchronous BFT consensus protocol with guaranteed liveness, using threshold encryption and provable broadcast. See [[bft-consensus/protocols/honeybadger-bft]].

**HotStuff**  
A partially synchronous BFT protocol with linear communication complexity (O(n)), using a three-phase commit and leader rotation. See [[bft-consensus/protocols/hotstuff]].

## I

**Integrity**  
A broadcast property requiring that a message is only delivered if it was actually sent by the claimed sender. See [[provable-broadcast/properties]].

## K

**Knowledge (in Logic Models)**  
What an agent knows based on its local observations and messages received. Formalized using modal logic operators. See [[logic-models/knowledge-framework]].

## L

**Leader**  
A distinguished node responsible for proposing values in many consensus protocols (e.g., PBFT, HotStuff). May rotate among nodes. See [[bft-consensus/protocols/pbft#leader-based-consensus]].

**Linear Temporal Logic (LTL)**  
A formal logic for expressing properties over infinite execution traces, using operators like ◇ (eventually) and □ (always). See [[logic-models/temporal-logic]].

**Liveness**  
A property stating that "something good eventually happens." For consensus, typically means a decision is eventually reached. See [[bft-consensus/properties/liveness-properties]].

## M

**Model Checking**  
Automated verification technique that exhaustively explores a system's state space to verify properties. See [[logic-models/formal-verification#model-checking]].

## N

**n (Total Nodes)**  
The total number of nodes in the system. In BFT literature, typically n = 3f + 1 to tolerate f Byzantine faults. See [[bft-consensus/fundamentals]].

**No Duplication**  
A broadcast property ensuring a message is delivered at most once. See [[provable-broadcast/properties]].

## O

**Omission Failure**  
A failure where a node fails to send or receive some messages but is otherwise correct. Less severe than Byzantine, more severe than crash. See [[bft-consensus/byzantine-failures]].

## P

**Partial Synchrony**  
A system model where message delays are eventually bounded, but the bound is unknown or holds only after some unknown time (Global Stabilization Time). See [[bft-consensus/fundamentals#synchrony-models]].

**PBFT (Practical Byzantine Fault Tolerance)**  
A classic BFT consensus protocol for partially synchronous systems, introduced by Castro and Liskov in 1999. See [[bft-consensus/protocols/pbft]].

**Provable Broadcast**  
A broadcast mechanism that produces a delivery certificate proving that a message has been delivered by a supermajority of nodes. See [[provable-broadcast/provable-broadcast]].

**Provability**  
The property that a broadcast mechanism produces cryptographic or quorum-based proof of message delivery. Distinguishing feature of provable broadcast. See [[provable-broadcast/properties]].

## Q

**Quorum**  
A subset of nodes large enough to ensure that any two quorums intersect in at least one correct node. In BFT, typically n - f nodes form a quorum. See [[bft-consensus/fundamentals#quorums]].

**Quorum Certificate**  
See **Certificate**.

## R

**Reliable Broadcast**  
A broadcast primitive guaranteeing that if any correct node delivers a message, all correct nodes deliver it. See [[provable-broadcast/reliable-broadcast]].

**Replica**  
A node participating in a consensus protocol. In BFT literature, often used synonymously with "node" or "process." See [[bft-consensus/fundamentals]].

## S

**Safety**  
A property stating that "something bad never happens." For consensus, typically means no two correct nodes decide on different values. See [[bft-consensus/properties/safety-properties]].

**Synchronous Model**  
A system model where there are known bounds on message delays and process execution speeds. Strong assumption but enables simpler protocols. See [[bft-consensus/fundamentals#synchrony-models]].

## T

**Temporal Logic**  
A formal logic for reasoning about properties over time, using operators for "eventually," "always," "next," etc. See [[logic-models/temporal-logic]].

**Termination**  
A consensus property (liveness) requiring that all correct nodes eventually decide on a value. See [[bft-consensus/properties/liveness-properties]].

**Threshold Automata**  
A formal model for representing distributed protocols, enabling automated verification of safety and liveness. See [[logic-models/threshold-automata]].

**Threshold Encryption/Signature**  
Cryptographic primitives requiring cooperation of f+1 nodes to decrypt/sign, used in protocols like HoneyBadgerBFT. See [[bft-consensus/protocols/honeybadger-bft#threshold-cryptography]].

**Total Order Broadcast**  
See **Atomic Broadcast**.

## V

**Validity**  
A consensus property requiring that if all correct nodes propose the same value, that value must be decided. Also a broadcast property. See [[bft-consensus/properties/safety-properties]] and [[provable-broadcast/properties]].

**View**  
In protocols like PBFT, a configuration with a designated leader. View changes occur when the leader is suspected to be faulty. See [[bft-consensus/protocols/pbft#view-changes]].

## W

**Wikilink**  
Obsidian's `[[note-name]]` syntax for linking between notes. See [[quickstart#using-the-knowledge-base]].

---

## See Also

- [[references]] - Bibliography and external sources
- [[index]] - Knowledge base entry point
- [[quickstart]] - Navigation guide

## Contributing to This Glossary

When adding terms:
- Use **bold** for the term being defined
- Provide concise definition (1-3 sentences)
- Link to detailed notes using wikilinks
- Alphabetize entries
- Include cross-references where helpful (See **Other Term**)

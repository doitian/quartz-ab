---
title: "References: Bibliography and External Sources"
type: reference
tags: [references, bibliography, citations]
created: 2026-01-21
updated: 2026-01-22
status: complete
---

# References

Complete bibliography of sources cited in the BFT Consensus Analysis knowledge base.

---

## Academic Papers

### Byzantine Fault Tolerance & Consensus

**castro-liskov-1999-pbft**  
Castro, M., & Liskov, B. (1999). *Practical Byzantine Fault Tolerance*. Proceedings of the Third Symposium on Operating Systems Design and Implementation (OSDI), 173-186.  
📄 [PDF](http://pmg.csail.mit.edu/papers/osdi99.pdf) | 🔗 [ACM](https://dl.acm.org/doi/10.5555/296806.296824)

**miller-2016-honeybadger**  
Miller, A., Xia, Y., Croman, K., Shi, E., & Song, D. (2016). *The Honey Badger of BFT Protocols*. Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security (CCS), 31-42.  
📄 [PDF](https://eprint.iacr.org/2016/199.pdf) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/2976749.2978399)

**yin-2019-hotstuff**  
Yin, M., Malkhi, D., Reiter, M. K., Gueta, G. G., & Abraham, I. (2019). *HotStuff: BFT Consensus with Linearity and Responsiveness*. Proceedings of the 2019 ACM Symposium on Principles of Distributed Computing (PODC), 347-356.  
📄 [arXiv](https://arxiv.org/abs/1803.05069) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/3293611.3331591)

**lamport-shostak-pease-1982-byzantine**  
Lamport, L., Shostak, R., & Pease, M. (1982). *The Byzantine Generals Problem*. ACM Transactions on Programming Languages and Systems (TOPLAS), 4(3), 382-401.  
🔗 [ACM](https://dl.acm.org/doi/10.1145/357172.357176)

**fischer-lynch-paterson-1985-flp**  
Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985). *Impossibility of Distributed Consensus with One Faulty Process*. Journal of the ACM, 32(2), 374-382.  
🔗 [ACM](https://dl.acm.org/doi/10.1145/3149.214121)

---

### Logic Models & Formal Verification

**halpern-moses-1990-knowledge**  
Halpern, J. Y., & Moses, Y. (1990). *Knowledge and common knowledge in a distributed environment*. Journal of the ACM, 37(3), 549-587.  
📄 [arXiv cs/0006009](https://arxiv.org/abs/cs/0006009) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/79147.79161)  
**Note**: Originally published in 1990; arXiv version is cs/0006009 (2000 preprint). Also cited as **halpern-moses-2000-knowledge** in some references.

**halpern-moses-2000-knowledge**  
Alias for **halpern-moses-1990-knowledge** (arXiv preprint version from 2000).

**fagin-halpern-moses-vardi-1995-reasoning**  
Fagin, R., Halpern, J. Y., Moses, Y., & Vardi, M. Y. (1995). *Reasoning About Knowledge*. MIT Press.  
🔗 [MIT Press](https://mitpress.mit.edu/9780262562003/reasoning-about-knowledge/)  
**Note**: Foundational textbook on epistemic logic and knowledge in distributed systems.

**pnueli-1977-temporal-logic**  
Pnueli, A. (1977). *The Temporal Logic of Programs*. Proceedings of the 18th Annual Symposium on Foundations of Computer Science (FOCS), 46-57.  
🔗 [IEEE](https://ieeexplore.ieee.org/document/4567924)  
**Note**: Seminal paper introducing temporal logic for program verification.

**lamport-1994-temporal-logic**  
Lamport, L. (1994). *The Temporal Logic of Actions*. ACM Transactions on Programming Languages and Systems, 16(3), 872-923.  
🔗 [ACM](https://dl.acm.org/doi/10.1145/177492.177726)  
**Note**: TLA (Temporal Logic of Actions) framework for specifying and verifying concurrent systems.

**lamport-2002-tla**  
Lamport, L. (2002). *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley.  
🔗 [TLA+ Home](https://lamport.azurewebsites.net/tla/tla.html)  
**Note**: Comprehensive guide to TLA+ specification language.

**baier-katoen-2008-principles**  
Baier, C., & Katoen, J. P. (2008). *Principles of Model Checking*. MIT Press.  
🔗 [MIT Press](https://mitpress.mit.edu/9780262026499/principles-of-model-checking/)  
**Note**: Standard textbook on model checking and temporal logic.

**konnov-veith-widder-2017-threshold**  
Konnov, I., Veith, H., & Widder, J. (2017). *On the Completeness of Bounded Model Checking for Threshold-Based Distributed Algorithms: Reachability*. Information and Computation, 252, 95-109.  
📄 [PDF](https://forsyte.at/wp-content/uploads/ic-2017.pdf) | 🔗 [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0890540116301146)  
**Note**: Theoretical foundations of threshold automata model checking.

**john-konnov-schmid-veith-widder-2013-parameterized**  
John, A., Konnov, I., Schmid, U., Veith, H., & Widder, J. (2013). *Parameterized Model Checking of Fault-Tolerant Distributed Algorithms by Abstraction*. Proceedings of Formal Methods in Computer-Aided Design (FMCAD), 201-209.  
📄 [PDF](https://forsyte.at/wp-content/uploads/fmcad13.pdf) | 🔗 [IEEE](https://ieeexplore.ieee.org/document/6679408)

**lazic-triberti-widder-2017-cutoff**  
Lazić, M., Triberti, G., & Widder, J. (2017). *A Short Counterexample Property for Safety and Liveness Verification of Fault-Tolerant Distributed Algorithms*. Proceedings of POPL 2017.  
📄 [PDF](https://forsyte.at/wp-content/uploads/popl17.pdf)

**hawblitzel-howell-kapritsos-lorch-parno-roberts-setty-zill-2015-ironfleet**  
Hawblitzel, C., Howell, J., Kapritsos, M., Lorch, J. R., Parno, B., Roberts, M. L., Setty, S., & Zill, B. (2015). *IronFleet: Proving Practical Distributed Systems Correct*. Proceedings of the 25th Symposium on Operating Systems Principles (SOSP), 1-17.  
📄 [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ironfleet.pdf) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/2815400.2815428)  
**Note**: End-to-end verification of distributed systems using Dafny.

**wilcox-woos-panchekha-tatlock-wang-ernst-anderson-2015-verdi**  
Wilcox, J. R., Woos, D., Panchekha, P., Tatlock, Z., Wang, X., Ernst, M. D., & Anderson, T. (2015). *Verdi: A Framework for Implementing and Formally Verifying Distributed Systems*. Proceedings of PLDI 2015, 357-368.  
📄 [PDF](https://homes.cs.washington.edu/~mernst/pubs/verify-distsystem-pldi2015.pdf) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/2737924.2737958)  
**Note**: Coq-based framework for verified distributed systems.

**konnov-2017-threshold-automata**  
Konnov, I., Lazić, M., Veith, H., & Widder, J. (2017). *A Short Counterexample Property for Safety and Liveness Verification of Fault-Tolerant Distributed Algorithms*. Proceedings of the 44th ACM SIGPLAN Symposium on Principles of Programming Languages (POPL), 719-734.  
📄 [PDF](https://forsyte.at/wp-content/uploads/popl17.pdf) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/3009837.3009860)

**gramoli-2022-holistic**  
Gramoli, V., Guerraoui, R., & Komatovic, J. (2022). *Holistic Verification of Blockchain Consensus*. arXiv preprint arXiv:2206.04489.  
📄 [arXiv](https://arxiv.org/abs/2206.04489)

**berkovits-2024-bythos**  
Berkovits, I., Lazic, M., Losa, G., Padon, O., & Sergey, I. (2024). *Compositional Verification of Composite Byzantine Protocols (Bythos)*. arXiv preprint.  
📄 [PDF](https://ilyasergey.net/assets/pdf/papers/bythos-ccs24.pdf)

---

### Broadcast Mechanisms

**bracha-1987-asynchronous-broadcast**  
Bracha, G. (1987). *Asynchronous Byzantine Agreement Protocols*. Information and Computation, 75(2), 130-143.  
🔗 [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0890540187900543)

**cachin-2001-reliable-broadcast**  
Cachin, C., Guerraoui, R., & Rodrigues, L. (2001). *Reliable Broadcast in Distributed Systems*. In Introduction to Reliable and Secure Distributed Programming (pp. 61-78). Springer.  
🔗 [Springer](https://link.springer.com/chapter/10.1007/978-3-642-15260-3_4)

**cachin-guerraoui-rodrigues-2011-reliable-broadcast**  
Cachin, C., Guerraoui, R., & Rodrigues, L. (2011). *Introduction to Reliable and Secure Distributed Programming* (2nd ed.). Springer. Chapter 3: Reliable Broadcast.  
🔗 [Springer](https://link.springer.com/book/10.1007/978-3-642-15260-3)  
**Note**: Comprehensive treatment of broadcast primitives including reliable broadcast, Byzantine reliable broadcast, and their properties.

**bracha-asynchronous-consensus-1987**  
Bracha, G. (1987). *Asynchronous Byzantine Agreement Protocols*. Information and Computation, 75(2), 130-143.  
🔗 [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0890540187900543)  
**Note**: Seminal paper introducing the ECHO-READY protocol for Byzantine reliable broadcast.

**danezis-2022-narwhal**  
Danezis, G., Kogias, E. K., Sonnino, A., & Spiegelman, A. (2022). *Narwhal and Tusk: A DAG-based Mempool and Efficient BFT Consensus*. Proceedings of the Seventeenth European Conference on Computer Systems (EuroSys), 221-238.  
📄 [arXiv](https://arxiv.org/abs/2105.11827) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/3492321.3519594)  
**Note**: Modern DAG-based BFT using provable broadcast for data dissemination layer.

**danezis-2022-narwhal-tusk**  
Alias for **danezis-2022-narwhal** (same paper covering both Narwhal and Tusk components).

**keidar-2021-dag-rider**  
Keidar, I., Kokoris-Kogias, E., Naor, O., & Spiegelman, A. (2021). *All You Need is DAG*. Proceedings of the 2021 ACM Symposium on Principles of Distributed Computing (PODC), 165-175.  
📄 [arXiv](https://arxiv.org/abs/2102.08325) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/3465084.3467905)  
**Note**: DAG-Rider protocol - DAG-based asynchronous BFT with optimal resilience.

**cachin-2001-random-oracles-async**  
Cachin, C., Kursawe, K., & Shoup, V. (2001). *Random Oracles in Constantinople: Practical Asynchronous Byzantine Agreement using Cryptography*. Proceedings of PODC 2001, 123-132.  
📄 [PDF](https://eprint.iacr.org/2000/034.pdf) | 🔗 [ACM](https://dl.acm.org/doi/10.1145/383962.384024)  
**Note**: Foundational work on cryptographic techniques for asynchronous BFT.

**cachin-2011-introduction-reliable-broadcast**  
Cachin, C., Guerraoui, R., & Rodrigues, L. (2011). *Introduction to Reliable and Secure Distributed Programming* (2nd ed.). Chapter 3: Reliable Broadcast. Springer.  
🔗 [Springer](https://link.springer.com/book/10.1007/978-3-642-15260-3)  
**Note**: Standard reference for broadcast primitives (alias for cachin-guerraoui-rodrigues-2011-textbook, Chapter 3 specific).

**decentralized-thoughts-impossibility**  
Decentralized Thoughts. (Various dates). *Impossibility Results in Distributed Computing*.  
🔗 [Blog](https://decentralizedthoughts.github.io/)  
**Note**: Collection of articles on FLP impossibility and related results.

---

## Online Articles & Tutorials

**decentralized-thoughts-2022-provable-broadcast**  
Decentralized Thoughts. (2022, September 10). *Provable Broadcast*.  
🔗 [Article](https://decentralizedthoughts.github.io/2022-09-10-provable-broadcast/)  
**Status**: Cited as primary source for provable broadcast concepts. (Note: URL was inaccessible during research; concepts sourced from web search synthesis.)

**decentralized-thoughts-2025-pbft**  
Decentralized Thoughts. (2025, February 14). *Practical Byzantine Fault Tolerant Consensus (PBFT)*.  
🔗 [Article](https://decentralizedthoughts.github.io/2025-02-14-PBFT/)

**decentralized-thoughts-blog**  
Decentralized Thoughts Blog. (n.d.). *Distributed Systems, Consensus, and Blockchains*.  
🔗 [Blog](https://decentralizedthoughts.github.io/)  
**Note**: Comprehensive blog with tutorials and explanations of consensus protocols.

---

## Textbooks & Surveys

**cachin-guerraoui-rodrigues-2011-textbook**  
Cachin, C., Guerraoui, R., & Rodrigues, L. (2011). *Introduction to Reliable and Secure Distributed Programming* (2nd ed.). Springer.  
🔗 [Springer](https://link.springer.com/book/10.1007/978-3-642-15260-3)  
**Note**: Foundational textbook covering broadcast primitives, consensus, and Byzantine fault tolerance.

**lynch-1996-distributed-algorithms**  
Lynch, N. A. (1996). *Distributed Algorithms*. Morgan Kaufmann Publishers.  
🔗 [Publisher](https://www.elsevier.com/books/distributed-algorithms/lynch/978-1-55860-348-6)  
**Note**: Classic textbook on distributed algorithm theory, including consensus and Byzantine agreement.

**raynal-2018-concurrent-survey**  
Raynal, M. (2018). *Fault-Tolerant Message-Passing Distributed Systems: An Algorithmic Approach*. Springer.  
🔗 [Springer](https://link.springer.com/book/10.1007/978-3-319-94141-7)

**comprehensive-bft-survey-2022**  
Ferdous, M. S., et al. (2022). *Reaching Consensus in the Byzantine Empire: A Comprehensive Review of BFT Consensus Algorithms*. arXiv preprint arXiv:2204.03181.  
📄 [arXiv](https://arxiv.org/abs/2204.03181)  
**Note**: Excellent survey comparing numerous BFT protocols.

---

## Technical Specifications & Standards

**ietf-consensus-rfc**  
Various IETF RFCs on distributed consensus and fault tolerance.  
🔗 [IETF Datatracker](https://datatracker.ietf.org/)

---

## Code Repositories & Implementations

**github-honeybadgerbft**  
HoneyBadgerBFT Reference Implementation.  
🔗 [GitHub](https://github.com/amiller/HoneyBadgerBFT)

**github-hotstuff**  
HotStuff Protocol Implementation.  
🔗 [GitHub](https://github.com/hot-stuff/libhotstuff)

**github-bymc**  
Byzantine Model Checker (ByMC) - Threshold automata model checker.  
🔗 [GitHub](https://github.com/konnov/bymc)

**github-awesome-consensus**  
Awesome Consensus: Curated bibliography of consensus protocol resources.  
🔗 [GitHub](https://github.com/hellas-ai/awesome-consensus)

---

## Educational Resources

**epfl-distributed-systems-lectures**  
EPFL Distributed Computing Lab - Lecture Notes on Consensus, Broadcast, and Byzantine Fault Tolerance.  
🔗 [EPFL DCL](https://dcl.epfl.ch/site/education)  
**Notable**: 
- Reliable Broadcast Slides: [PDF](https://dcl.epfl.ch/site/_media/education/da14-reliablebroadcast.pdf)
- Total Order Broadcast Slides: [PDF](https://dcl.epfl.ch/site/_media/education/da18-totalorderbroadcast.pdf)

**mit-distributed-systems**  
MIT 6.824: Distributed Systems Course Materials.  
🔗 [MIT Course](https://pdos.csail.mit.edu/6.824/)

---

## Citation Format

Throughout this knowledge base, sources are cited using keys in the format:

```
[author-year-shortname]
```

**Examples:**
- `castro-liskov-1999-pbft`
- `halpern-moses-1990-knowledge`
- `decentralized-thoughts-2022-provable-broadcast`

These keys are used in YAML frontmatter `references:` fields and can be referenced inline.

---

## Access Notes

### Accessibility

- **Open Access**: Papers with arXiv or freely available PDFs
- **Paywalled**: Papers behind ACM/IEEE/Springer paywalls (institutional access may be required)
- **Blogs/Web**: Freely accessible online articles

### Archival

If a URL becomes unavailable:
1. Check [Wayback Machine](https://web.archive.org/)
2. Search for the title on academic search engines (Google Scholar, DBLP, Semantic Scholar)
3. Consult the [arXiv](https://arxiv.org/) for preprints

---

## Contributing to References

When adding a new reference:

1. **Assign a unique key**: `author-year-shortname`
2. **Provide full citation**: Author(s), Year, Title, Venue/Publisher
3. **Include links**: PDF, DOI, or URL
4. **Add context**: Brief note on relevance or content
5. **Categorize appropriately**: Place in the correct section
6. **Update related notes**: Add the key to YAML frontmatter `references:` fields in notes that cite it

---

## Version History

- **v1.0 (2026-01-21)**: Initial bibliography with core BFT, broadcast, and logic model references
- **v1.1 (2026-01-22)**: Added provable broadcast references (Bracha, Danezis Narwhal, expanded Cachin et al.)

---

## See Also

- [[bft-consensus-analysis/glossary|Glossary]] - Technical terminology
- [[index|Welcome to Quartz AB]] - Knowledge base entry point
- [[bft-consensus-analysis/quickstart|Quickstart]] - Navigation guide

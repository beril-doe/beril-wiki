<!-- tension-hash: b132d581d7195e13 -->
# Lability or Vertical Inheritance: How to Read Phylogenetic Signal in Metal Resistance Gene Content

Two readings of phylogenetic signal in antimicrobial resistance (AMR) genes sit side by side in [[concepts/phylogenetic-signal-of-gene-content-and-traits]]. Pagel's λ is a statistic from 0 to 1 that measures how strongly a trait follows the phylogeny. A Mantel test is a permutation test that correlates two distance matrices. One report reads intermediate metal AMR λ as lability through mobile genetic element (MGE) exchange, and it also reads the core-over-accessory ordering as vertical inheritance. Another report suggests the core-versus-acquired Mantel difference is partly a statistical artifact. The disagreement matters because it affects how the core-versus-accessory signal ordering should be interpreted.

## Evidence Sides

**Side A: the signal ordering reflects biology (lability plus vertical core inheritance)**
- Across genera, metal AMR λ is intermediate (about 0.26–0.44), and the report reads it as lability through MGE exchange among distant taxa. [src: microbeatlas_metal_ecology]
- The same report reads the core-over-accessory ordering as mainly vertical inheritance of core resistance. [src: microbeatlas_metal_ecology]

**Side B: the core-versus-acquired difference is partly statistical**
- The core-versus-acquired Mantel difference is partly a statistical artifact of near-zero Jaccard variance in core genes. Jaccard distance measures how different two gene sets are. [src: amr_strain_variation]

The two sides use different tests. Side A uses λ across genera, and Side B uses Mantel tests. Neither claim is a null result. Both are interpretations, and neither has been tested against the other.

## Possible Reconciliations

- **Hypothesis 1: both effects operate.** Core genes may be inherited vertically, and low Jaccard variance may also shrink their Mantel signal. This has not been tested.
- **Hypothesis 2: the artifact is specific to Mantel tests.** λ-based ordering may be unaffected by near-zero variance. This is untested, and it would leave the Mantel contrast weaker than the λ contrast.
- **Hypothesis 3: lability and vertical core inheritance describe different gene classes.** MGE-borne accessory genes may be labile while core genes track lineage. This is a proposal, not a finding.

## Resolving Work

- Data: core and accessory gene sets with their Jaccard variances. Method: subsample or variance-match the core genes and rerun the Mantel test. Question: does the core-versus-acquired difference persist?
- Data: the metal AMR trait tables behind the λ estimates. Method: fit λ with a permutation null and with simulated traits of matched variance. Question: is the core-over-accessory ordering robust to low variance?
- Data: gene annotations marking MGE association. Method: compare λ between MGE-linked and non-MGE-linked metal resistance genes. Question: does MGE linkage track lability?
- Data: the same taxa analysed in both projects. Method: run both the Mantel and λ analyses on one shared tree. Question: do the two methods give the same ordering?
- Data: simulated gene content with known vertical and horizontal transfer rates. Method: apply both statistics. Question: which one recovers the simulated inheritance mode?

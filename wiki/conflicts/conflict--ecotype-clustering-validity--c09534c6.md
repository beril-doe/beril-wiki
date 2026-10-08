<!-- tension-hash: c09534c6dbea31a9 -->
# Is the environment–gene-content partial correlation near zero or modestly positive?

Two projects measured how strongly environmental similarity tracks bacterial gene-content similarity after controlling for phylogeny. A partial correlation is the association between two variables after the effect of a third, here phylogenetic distance, is removed. The projects' median partial correlations differ substantially. Both projects agree that environmental bacteria do not show stronger environment effects than host-associated bacteria, but they disagree on how large the environment signal is overall. This matters for [[concepts/ecotype-clustering-validity]]. One hypothesis is that a near-zero signal would favour reading gene-content clusters as mostly phylogenetic, while a modest positive signal would leave more room for environmental structuring. Because the two values come from different methods, neither interpretation is established.

## Evidence Sides

**Side 1: original ecotype analysis (near-zero magnitude)**

The original ecotype analysis reported a median partial correlation of 0.003 across its analysis. [src: ecotype_env_reanalysis] It used diversity-maximizing downsampling, which reduces each species to a subset of its genomes, with a maximum of 250 genomes. [src: ecotype_env_reanalysis] Using a coarse classification, it found no significant difference between environmental and host-associated groups, with p=0.66. [src: ecotype_analysis, ecotype_env_reanalysis] Here p is the p-value, the probability of a difference at least this large if no true difference exists.

**Side 2: environmental reanalysis (larger magnitude)**

The reanalysis reported a median partial correlation of 0.081, which it characterized as a 27x difference from the original. [src: ecotype_env_reanalysis] It used all genomes with embeddings (precomputed numerical vector representations of each genome), including up to 3,505 genomes per species, rather than downsampling. [src: ecotype_env_reanalysis] It also used different genome sets and distance distributions. [src: ecotype_env_reanalysis] With genome-level harmonized classification, its Environmental versus Human-associated comparison yielded p=0.83. [src: ecotype_analysis, ecotype_env_reanalysis]

**Shared ground and scope of the disagreement**

The reanalysis states that these absolute values are not comparable across methodologies. [src: ecotype_env_reanalysis] It also states that the Environmental versus Human-associated comparison remains valid because it was performed within one consistent method. [src: ecotype_env_reanalysis] Both projects support a null environmental-group comparison, but the methodological discrepancy leaves the magnitude of the correlations unresolved. [src: ecotype_analysis, ecotype_env_reanalysis] The tension therefore concerns effect magnitude only, not the direction of the group comparison.

## Possible Reconciliations

- *Hypothesis: sampling depth.* Larger per-species genome sets may detect weak correlations that downsampled sets cannot. Under this hypothesis, both values could be accurate for their respective designs.
- *Hypothesis: distance-distribution artifact.* Downsampling chosen to maximize diversity may change the distribution of pairwise distances. That change could compress or inflate partial correlations independently of any biological signal.
- *Hypothesis: genome-set composition.* The two analyses drew on different genome sets. Differences in which species and genomes were included, rather than in the method, may account for part of the gap.

The supplied evidence reports no test of these hypotheses, and none is preferred here.

## Resolving Work

- Rerun the reanalysis pipeline on its own species with downsampling capped at 250 genomes per species. This asks whether the median moves toward the original value, while recognizing that downsampling also changes genome composition and distance distributions, so depth is not isolated.
- Run a subsampling sweep from small sets up to the full genome sets, reaching 3,505 genomes per species where available. Track the median partial correlation at each depth to see whether it rises with sample size.
- Apply both pipelines to an identical genome set and compare the pairwise distance distributions. This would test whether distribution shape, rather than depth, drives the magnitude gap.
- Repeat the Environmental versus Human-associated test under both pipelines with the classification held fixed. This checks whether the null comparison persists regardless of the magnitude estimate.
